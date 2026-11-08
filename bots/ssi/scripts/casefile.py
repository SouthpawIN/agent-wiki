#!/usr/bin/env python3
"""Beacon's case binder: intake, deadlines, review sheets, and form filling.

Safety contract, enforced in code:
  * Nothing is ever submitted. `fill` writes a new PDF; it never posts, faxes,
    emails, or signs.
  * A field with no verified fact is left blank and reported as
    `[[CONFIRM: field]]`. Guessing a date or an income figure on a benefits form
    is the one failure mode this tool exists to prevent.
  * Facts carry a source path. A fact without a source is a CONFIRM, not a value.
  * Originals are never modified or moved; intake copies into the case folder.

Commands:
    init      <initials>                       create the case folder
    intake    <initials> <file> --source --doctype [--date --due --case-no --ask]
    deadlines <initials> [--days 10]           what is due, what is overdue
    review    <initials> --form NAME --facts facts.json [--send-by DATE --method MAIL]
    fill      <form.pdf> <facts.json> <out.pdf>  fill AcroForm fields, list CONFIRMs
    log       <initials> <text>                append to the timeline
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

CASE_ROOT = Path("cases")
SOURCES = ("ssa", "hhsc", "school", "medical", "court", "other")


def _today() -> date:
    return date.today()


def _case(initials: str) -> Path:
    return CASE_ROOT / initials.strip().lower()


def _index_path(initials: str) -> Path:
    return _case(initials) / "index.json"


def _load_index(initials: str) -> dict[str, Any]:
    path = _index_path(initials)
    if not path.exists():
        return {"initials": initials.strip().lower(), "documents": [], "deadlines": []}
    return json.loads(path.read_text(encoding="utf-8"))


def _save_index(initials: str, data: dict[str, Any]) -> None:
    path = _index_path(initials)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def log(initials: str, text: str) -> None:
    timeline = _case(initials) / "timeline.md"
    timeline.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with timeline.open("a", encoding="utf-8") as handle:
        handle.write(f"- {stamp} — {text}\n")


def init(initials: str) -> Path:
    root = _case(initials)
    for sub in ("inbox", "notices", "forms", "sent", "facts"):
        (root / sub).mkdir(parents=True, exist_ok=True)
    if not _index_path(initials).exists():
        _save_index(initials, {"initials": initials.strip().lower(), "documents": [], "deadlines": []})
    (root / "timeline.md").touch(exist_ok=True)
    log(initials, "case opened")
    return root


def intake(
    initials: str,
    file: str | Path,
    *,
    source: str,
    doctype: str,
    when: str | None = None,
    due: str | None = None,
    case_no: str | None = None,
    ask: str | None = None,
    consequence: str | None = None,
) -> Path:
    """Copy a document into the case, name it, index it, and calendar any deadline."""
    if source not in SOURCES:
        raise ValueError(f"source must be one of {SOURCES}")
    src = Path(file)
    if not src.exists():
        raise FileNotFoundError(src)
    stamp = when or _today().isoformat()
    dest_name = f"{stamp}_{source}_{doctype.replace(' ', '-')}{src.suffix.lower()}"
    dest = _case(initials) / "notices" / dest_name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)  # never move: the original stays where Chris put it

    data = _load_index(initials)
    entry = {
        "file": str(dest.relative_to(CASE_ROOT.parent)),
        "received": stamp,
        "source": source,
        "doctype": doctype,
        "case_no": case_no,
        "ask": ask,
        "consequence": consequence,
        "due": due,
    }
    data["documents"].append(entry)
    if due:
        data["deadlines"].append({
            "due": due, "what": ask or doctype, "source": source,
            "case_no": case_no, "status": "open", "document": entry["file"],
        })
    _save_index(initials, data)
    log(initials, f"intake {dest_name}" + (f" — due {due}" if due else ""))
    return dest


def deadlines(initials: str, *, days: int = 10) -> list[dict[str, Any]]:
    """Rows due within `days`, plus anything overdue, soonest first."""
    data = _load_index(initials)
    horizon = _today() + timedelta(days=days)
    rows = []
    for row in data.get("deadlines", []):
        if row.get("status") != "open":
            continue
        try:
            due = date.fromisoformat(row["due"])
        except (KeyError, ValueError):
            continue
        if due <= horizon:
            rows.append({**row, "days_left": (due - _today()).days})
    return sorted(rows, key=lambda item: item["days_left"])


def facts_with_sources(facts: dict[str, Any]) -> tuple[dict[str, str], list[str]]:
    """Split a facts file into usable values and CONFIRM markers.

    A usable fact is `{"field": {"value": ..., "source": "path"}}`. Anything
    missing a value or a source becomes `[[CONFIRM: field]]`.
    """
    usable: dict[str, str] = {}
    confirms: list[str] = []
    for field_name, spec in facts.items():
        if not isinstance(spec, dict):
            confirms.append(field_name)
            continue
        value = spec.get("value")
        source = spec.get("source")
        if value in (None, "") or not source:
            confirms.append(field_name)
            continue
        usable[field_name] = str(value)
    return usable, confirms


def fill(form_pdf: str | Path, facts: dict[str, Any], out_pdf: str | Path) -> dict[str, Any]:
    """Fill the AcroForm fields that have verified facts. Report the rest."""
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError("pypdf is required to fill forms: pip install pypdf") from exc

    usable, confirms = facts_with_sources(facts)
    reader = PdfReader(str(form_pdf))
    fields = reader.get_fields() or {}
    if not fields:
        raise ValueError(f"{form_pdf} has no fillable fields; type the answers by hand instead")

    known = set(fields)
    writer = PdfWriter(clone_from=str(form_pdf))
    applied: dict[str, str] = {}
    for page in writer.pages:
        page_fields = {name: value for name, value in usable.items() if name in known}
        if page_fields:
            writer.update_page_form_field_values(page, page_fields, auto_regenerate=False)
    applied = {name: usable[name] for name in usable if name in known}
    unknown = sorted(set(usable) - known)
    blank = sorted(known - set(usable))

    out = Path(out_pdf)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as handle:
        writer.write(handle)
    return {
        "output": str(out),
        "filled": applied,
        "blank_fields_needing_confirm": blank,
        "facts_not_on_form": unknown,
        "confirms": sorted(set(confirms) | set(blank)),
    }


def review_sheet(
    initials: str,
    *,
    form: str,
    facts: dict[str, Any],
    send_by: str | None = None,
    method: str = "certified mail",
    enclosures: list[str] | None = None,
) -> str:
    """The one page Chris reads before signing."""
    usable, confirms = facts_with_sources(facts)
    lines = [
        f"# Review sheet — {form}",
        "",
        f"**Case:** {initials}   **Prepared:** {_today().isoformat()}",
        f"**Send by:** {send_by or '[[CONFIRM: deadline]]'}   **Method:** {method}",
        "",
        "## Facts used (each with its source)",
        "",
    ]
    for name in sorted(usable):
        spec = facts[name]
        lines.append(f"- `{name}` = {usable[name]}  ← {spec.get('source')}")
    lines += ["", "## Must confirm before signing", ""]
    if confirms:
        lines += [f"- [[CONFIRM: {name}]]" for name in sorted(set(confirms))]
    else:
        lines.append("- none — every field has a sourced value")
    lines += ["", "## Enclosures", ""]
    lines += [f"- {item}" for item in (enclosures or ["[[CONFIRM: enclosures]]"])]
    lines += [
        "",
        "## Signature",
        "",
        "Chris signs. Beacon does not sign, submit, or speak to an agency.",
        "",
    ]
    text = "\n".join(lines)
    out = _case(initials) / "forms" / f"review-{form.replace(' ', '-').lower()}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    log(initials, f"review sheet for {form}: {len(confirms)} confirm(s)")
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init"); p.add_argument("initials")
    p = sub.add_parser("intake"); p.add_argument("initials"); p.add_argument("file")
    p.add_argument("--source", required=True, choices=SOURCES)
    p.add_argument("--doctype", required=True)
    p.add_argument("--date"); p.add_argument("--due"); p.add_argument("--case-no")
    p.add_argument("--ask"); p.add_argument("--consequence")
    p = sub.add_parser("deadlines"); p.add_argument("initials")
    p.add_argument("--days", type=int, default=10)
    p = sub.add_parser("review"); p.add_argument("initials")
    p.add_argument("--form", required=True); p.add_argument("--facts", required=True)
    p.add_argument("--send-by"); p.add_argument("--method", default="certified mail")
    p = sub.add_parser("fill"); p.add_argument("form"); p.add_argument("facts"); p.add_argument("out")
    p = sub.add_parser("log"); p.add_argument("initials"); p.add_argument("text")

    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            print(f"case ready: {init(args.initials)}")
        elif args.command == "intake":
            dest = intake(args.initials, args.file, source=args.source, doctype=args.doctype,
                          when=args.date, due=args.due, case_no=args.case_no,
                          ask=args.ask, consequence=args.consequence)
            print(f"filed: {dest}" + (f" (due {args.due})" if args.due else ""))
        elif args.command == "deadlines":
            rows = deadlines(args.initials, days=args.days)
            if not rows:
                print("clear — nothing due in the window")
            for row in rows:
                state = "OVERDUE" if row["days_left"] < 0 else f"in {row['days_left']}d"
                print(f"{state:>10}  {row['due']}  {row['what']}  [{row['source']}]")
        elif args.command == "review":
            facts = json.loads(Path(args.facts).read_text(encoding="utf-8"))
            print(review_sheet(args.initials, form=args.form, facts=facts,
                               send_by=args.send_by, method=args.method))
        elif args.command == "fill":
            facts = json.loads(Path(args.facts).read_text(encoding="utf-8"))
            result = fill(args.form, facts, args.out)
            print(json.dumps(result, indent=2))
            if result["confirms"]:
                print(f"\n{len(result['confirms'])} field(s) need Chris: "
                      + ", ".join(result["confirms"]), file=sys.stderr)
        elif args.command == "log":
            log(args.initials, args.text)
            print("logged")
        return 0
    except (ValueError, FileNotFoundError, RuntimeError) as exc:
        print(f"casefile: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
