"""Anser's corpus: caching, citation, and the refusal to answer from nothing."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import corpus as c  # noqa: E402


def post(ident: str, text: str, *, account: str = "NousResearch", days_ago: int = 1,
         reply: bool = False) -> c.Post:
    stamp = (datetime.now(timezone.utc) - timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return c.Post(id=ident, account=account, created_at=stamp, text=text,
                  url=f"https://x.com/{account}/status/{ident}", is_reply=reply)


@pytest.fixture(autouse=True)
def isolated_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(c, "DATA", Path("data"))
    monkeypatch.setattr(c, "CORPUS", Path("data/x-corpus.jsonl"))
    monkeypatch.setattr(c, "STATE", Path("data/corpus-state.json"))
    return tmp_path


def test_upsert_is_append_only_and_dedupes(isolated_data: Path) -> None:
    added, total = c.upsert([post("1", "hermes web app is live"), post("2", "strata update")])
    assert (added, total) == (2, 2)

    added, total = c.upsert([post("1", "a different text entirely"), post("3", "new one")])
    assert (added, total) == (1, 3), "an existing id keeps its original line"

    stored = c.load_corpus()
    assert stored["1"].text == "hermes web app is live"
    assert len((isolated_data / "data/x-corpus.jsonl").read_text().splitlines()) == 3


def test_post_from_raw_builds_a_url_when_missing() -> None:
    made = c.Post.from_raw({"id": "42", "text": "hello", "created_at": "2026-11-01"}, "Teknium")
    assert made.url == "https://x.com/Teknium/status/42"
    assert made.account == "Teknium"


def test_post_without_an_id_is_rejected() -> None:
    with pytest.raises(ValueError, match="no id"):
        c.Post.from_raw({"text": "anonymous"})


def test_search_returns_citations_not_just_text(isolated_data: Path) -> None:
    c.upsert([
        post("1", "Hermes can now be served as a web app on your tailnet", days_ago=2),
        post("2", "Lunch was great", days_ago=2),
        post("3", "web app dashboard tips", account="Teknium", days_ago=400),
    ])
    hits = c.search("web app")
    assert hits and all(h["url"].startswith("https://x.com/") for h in hits)
    assert all("@" in h["citation"] and h["citation"].endswith(h["url"]) for h in hits)
    assert hits[0]["id" if "id" in hits[0] else "url"], "each hit is citable"
    assert "Lunch" not in json.dumps(hits)


def test_recency_and_reply_penalties_shape_ranking(isolated_data: Path) -> None:
    c.upsert([
        post("old", "hermes web app", days_ago=700),
        post("new", "hermes web app", days_ago=1),
        post("reply", "hermes web app", days_ago=1, reply=True),
    ])
    order = [h["url"].rsplit("/", 1)[-1] for h in c.search("hermes web app", top=3)]
    assert order[0] == "new"
    assert order.index("reply") > order.index("new")


def test_account_and_day_filters(isolated_data: Path) -> None:
    c.upsert([post("1", "strata news", account="Teknium", days_ago=1),
              post("2", "strata news", account="NousResearch", days_ago=200)])
    assert [h["account"] for h in c.search("strata news", account="Teknium")] == ["Teknium"]
    assert len(c.search("strata news", days=30)) == 1


def test_answer_pack_refuses_when_the_corpus_is_silent(isolated_data: Path) -> None:
    c.upsert([post("1", "unrelated chatter")])
    pack = c.answer_pack("what is the price of the enterprise tier")
    assert pack["grounded"] is False
    assert "Not publicly stated" in pack["answer_stub"]


def test_answer_pack_reports_a_stale_corpus(isolated_data: Path) -> None:
    c.write_state(["NousResearch"], stale=True, error="@NousResearch: xurl failed: 401")
    pack = c.answer_pack("anything")
    assert pack["corpus_state"]["stale"] is True
    assert "401" in pack["corpus_state"]["error"]


def test_refresh_marks_stale_instead_of_pretending(isolated_data: Path,
                                                   monkeypatch: pytest.MonkeyPatch) -> None:
    def boom(account: str, *, limit: int = 50) -> list[c.Post]:
        raise RuntimeError("xurl failed: unauthorized")
    monkeypatch.setattr(c, "fetch_xurl", boom)

    result = c.refresh(["NousResearch", "Teknium"])
    assert result["total"] == 0
    assert len(result["errors"]) == 2
    assert result["state"]["stale"] is True


def test_refresh_keeps_the_old_corpus_when_one_account_fails(isolated_data: Path,
                                                             monkeypatch: pytest.MonkeyPatch) -> None:
    c.upsert([post("1", "existing post")])

    def half(account: str, *, limit: int = 50) -> list[c.Post]:
        if account == "NousResearch":
            return [post("2", "fresh official post")]
        raise RuntimeError("rate limited")

    monkeypatch.setattr(c, "fetch_xurl", half)
    result = c.refresh(["NousResearch", "Teknium"])
    assert result["added"] == 1 and result["total"] == 2
    assert result["state"]["stale"] is False, "we still have data, so say what failed"
    assert "rate limited" in result["state"]["error"]


def test_import_json_round_trip(isolated_data: Path, tmp_path: Path) -> None:
    fixture = tmp_path / "posts.json"
    fixture.write_text(json.dumps([
        {"id": "9", "text": "imported post", "created_at": "2026-11-01", "user": "Teknium"},
    ]), encoding="utf-8")
    result = c.import_json(fixture)
    assert result == {"added": 1, "total": 1, "imported": 1}
    assert c.search("imported post")[0]["account"] == "Teknium"


def test_cli_status_reports_counts(isolated_data: Path, capsys) -> None:
    c.upsert([post("1", "one"), post("2", "two")])
    c.write_state(["NousResearch"])
    assert c.main(["status"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["posts"] == 2 and out["state"]["count"] == 2
