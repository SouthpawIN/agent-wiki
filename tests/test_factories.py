from pathlib import Path

from senter_agent.factories import materialize_all
from senter_agent.model import Proposal


def test_materialize_all_builds_bot_stack(tmp_path: Path):
    proposals = [Proposal("skill", "repeated-procedure", "repeated evidence", ["A.md", "B.md"])]
    output = materialize_all(tmp_path, "demo", proposals)
    assert (tmp_path / "bots/demo/BOT.md").exists()
    assert (tmp_path / "bots/demo/skills/repeated-procedure-SKILL.md").exists()
    assert (tmp_path / "bots/demo/.system").is_dir()
    assert len(output) == 2


def test_materialize_all_is_idempotent(tmp_path: Path):
    proposal = Proposal("agent", "reviewer", "cluster", ["A.md"])
    first = materialize_all(tmp_path, "demo", [proposal])
    before = first[-1].path.read_text(encoding="utf-8")
    second = materialize_all(tmp_path, "demo", [proposal])
    assert second[-1].path.read_text(encoding="utf-8") == before


def test_materialize_loop_is_markdown_not_live_cron(tmp_path: Path):
    proposal = Proposal("loop", "daily-check", "repeatable", ["A.md"])
    materialize_all(tmp_path, "demo", [proposal])
    path = tmp_path / "bots/demo/loops/daily-check.md"
    assert "proposed" in path.read_text(encoding="utf-8")
    assert not (tmp_path / "cron").exists()


def test_context_includes_evidence(tmp_path: Path):
    proposal = Proposal("skill", "x", "reason", ["one.md"])
    materialize_all(tmp_path, "demo", [proposal])
    text = (tmp_path / "bots/demo/BOT.md").read_text(encoding="utf-8")
    assert "skill:x" in text
    assert "reason" in text


def test_skill_has_metadata(tmp_path: Path):
    proposal = Proposal("skill", "x", "reason", ["one.md"])
    materialize_all(tmp_path, "demo", [proposal])
    text = (tmp_path / "bots/demo/skills/x-SKILL.md").read_text(encoding="utf-8")
    assert "name: x" in text
    assert "review before installing" in text


def test_materialized_bot_document_declares_type(tmp_path: Path):
    materialize_all(tmp_path, "demo", [Proposal("skill", "x", "reason", ["one.md"])])
    text = (tmp_path / "bots/demo/BOT.md").read_text(encoding="utf-8")
    assert "type: bot" in text
    assert "slug: demo" in text
