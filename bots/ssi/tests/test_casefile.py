"""Beacon's case binder. Synthetic PDFs, no personal data, no submissions."""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import casefile  # noqa: E402


def make_form(path: Path, fields: tuple[str, ...] = ("case_number", "claimant_name")) -> Path:
    """A minimal AcroForm PDF with one text widget per field."""
    from pypdf.generic import (
        ArrayObject, BooleanObject, DictionaryObject, NameObject, NumberObject, TextStringObject,
    )
    from pypdf import PdfWriter

    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)
    annots = ArrayObject()
    for name in fields:
        widget = DictionaryObject()
        widget[NameObject("/FT")] = NameObject("/Tx")
        widget[NameObject("/T")] = TextStringObject(name)
        widget[NameObject("/Rect")] = ArrayObject(
            [NumberObject(72), NumberObject(700), NumberObject(300), NumberObject(720)]
        )
        widget[NameObject("/Subtype")] = NameObject("/Widget")
        widget[NameObject("/F")] = NumberObject(4)
        widget[NameObject("/V")] = TextStringObject("")
        annots.append(writer._add_object(widget))
    writer.pages[0][NameObject("/Annots")] = annots
    acro = DictionaryObject()
    acro[NameObject("/Fields")] = annots
    acro[NameObject("/NeedAppearances")] = BooleanObject(True)
    writer._root_object[NameObject("/AcroForm")] = acro
    with path.open("wb") as handle:
        writer.write(handle)
    return path


@pytest.fixture(autouse=True)
def isolated_case_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(casefile, "CASE_ROOT", Path("cases"))
    return tmp_path


def test_init_builds_the_binder(isolated_case_root: Path) -> None:
    root = casefile.init("ab")
    for sub in ("inbox", "notices", "forms", "sent", "facts"):
        assert (root / sub).is_dir()
    assert json.loads((root / "index.json").read_text())["initials"] == "ab"
    assert "case opened" in (root / "timeline.md").read_text()


def test_intake_copies_never_moves_and_indexes(isolated_case_root: Path, tmp_path: Path) -> None:
    casefile.init("ab")
    original = tmp_path / "letter.pdf"
    original.write_bytes(b"%PDF-1.4 fake")

    filed = casefile.intake("ab", original, source="ssa", doctype="notice",
                            when="2026-10-02", case_no="TX-999", ask="Return form 827")
    assert filed.exists() and original.exists(), "the original must stay put"
    assert filed.name == "2026-10-02_ssa_notice.pdf"

    index = json.loads((isolated_case_root / "cases/ab/index.json").read_text())
    assert index["documents"][-1]["case_no"] == "TX-999"
    assert index["documents"][-1]["ask"] == "Return form 827"


def test_intake_with_a_due_date_creates_a_deadline(isolated_case_root: Path, tmp_path: Path) -> None:
    casefile.init("ab")
    note = tmp_path / "n.pdf"; note.write_bytes(b"%PDF-1.4 fake")
    due = (date.today() + timedelta(days=4)).isoformat()
    casefile.intake("ab", note, source="hhsc", doctype="renewal", due=due, ask="Medicaid renewal")

    rows = casefile.deadlines("ab", days=10)
    assert len(rows) == 1 and rows[0]["days_left"] == 4
    assert casefile.deadlines("ab", days=1) == [], "outside the window"


def test_overdue_sorts_first(isolated_case_root: Path, tmp_path: Path) -> None:
    casefile.init("ab")
    note = tmp_path / "n.pdf"; note.write_bytes(b"%PDF-1.4 fake")
    casefile.intake("ab", note, source="ssa", doctype="a", due=(date.today() + timedelta(days=9)).isoformat(), ask="soon")
    casefile.intake("ab", note, source="ssa", doctype="b", due=(date.today() - timedelta(days=2)).isoformat(), ask="late")

    rows = casefile.deadlines("ab")
    assert rows[0]["what"] == "late" and rows[0]["days_left"] < 0


def test_unsourced_facts_become_confirms_not_values() -> None:
    usable, confirms = casefile.facts_with_sources({
        "case_number": {"value": "TX-1", "source": "notices/2026-10-02_ssa_notice.pdf"},
        "monthly_income": {"value": None, "source": "paystub.pdf"},
        "claimant_name": {"value": "A B"},                      # no source
        "phone": "555",                                        # not a dict
    })
    assert usable == {"case_number": "TX-1"}
    assert set(confirms) == {"monthly_income", "claimant_name", "phone"}


def test_fill_writes_sourced_values_and_reports_the_rest(tmp_path: Path) -> None:
    form = make_form(tmp_path / "form.pdf", ("case_number", "claimant_name", "monthly_income"))
    facts = {
        "case_number": {"value": "TX-12345", "source": "notices/notice.pdf"},
        "claimant_name": {"value": "A B", "source": None},
    }
    out = tmp_path / "out" / "filled.pdf"
    result = casefile.fill(form, facts, out)

    assert out.exists()
    assert result["filled"] == {"case_number": "TX-12345"}
    assert "claimant_name" in result["confirms"]
    assert "monthly_income" in result["blank_fields_needing_confirm"]

    from pypdf import PdfReader
    values = {k: str(v.get("/V")) for k, v in (PdfReader(str(out)).get_fields() or {}).items()}
    assert values["case_number"] == "TX-12345"
    assert values["claimant_name"] == "", "an unsourced fact must never be written"


def test_fill_refuses_a_form_with_no_fields(tmp_path: Path) -> None:
    from pypdf import PdfWriter
    blank = tmp_path / "blank.pdf"
    writer = PdfWriter(); writer.add_blank_page(width=200, height=200)
    with blank.open("wb") as handle:
        writer.write(handle)
    with pytest.raises(ValueError, match="no fillable fields"):
        casefile.fill(blank, {"x": {"value": "1", "source": "s"}}, tmp_path / "o.pdf")


def test_review_sheet_names_every_confirm_and_never_signs(isolated_case_root: Path) -> None:
    casefile.init("ab")
    text = casefile.review_sheet(
        "ab", form="SSA-827",
        facts={"case_number": {"value": "TX-1", "source": "notices/n.pdf"},
               "monthly_income": {"value": None, "source": None}},
        send_by="2026-11-20", enclosures=["Copy of the notice", "Signed 827"],
    )
    assert "[[CONFIRM: monthly_income]]" in text
    assert "notices/n.pdf" in text
    assert "Chris signs. Beacon does not sign, submit, or speak to an agency." in text
    assert (isolated_case_root / "cases/ab/forms/review-ssa-827.md").exists()


def test_cli_deadlines_says_clear_when_nothing_is_due(isolated_case_root: Path, capsys) -> None:
    casefile.init("ab")
    assert casefile.main(["deadlines", "ab"]) == 0
    assert "clear" in capsys.readouterr().out
