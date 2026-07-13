from pathlib import Path

from senter_agent import build_plan, parse_markdown
from senter_agent.parser import parse_tree


def test_all_caps_document_is_context(tmp_path: Path):
    doc = tmp_path / "MEDIA.md"
    doc.write_text("# Media\n\n## Purpose\nEdit video.\n", encoding="utf-8")
    parsed = parse_markdown(doc)
    assert parsed.kind == "context"
    assert parsed.title == "Media"
    assert "purpose" in parsed.sections


def test_all_caps_document_extracts_declaration_without_secrets(tmp_path: Path):
    doc = tmp_path / "WALLET.md"
    doc.write_text("# Wallet\n\n## Purpose\n- Track masked cards\n\n## Forbidden\n- Reveal full card numbers\n\n## Secret References\n- bitwarden://wallet/cards\n", encoding="utf-8")
    parsed = parse_markdown(doc)
    assert parsed.declaration["purpose"] == ["Track masked cards"]
    assert parsed.declaration["forbidden"] == ["Reveal full card numbers"]
    assert parsed.declaration["secret_refs"] == ["bitwarden://wallet/cards"]


def test_explicit_skill_and_cluster_proposals(tmp_path: Path):
    (tmp_path / "one.md").write_text("---\ntype: skill\ntags: [video]\n---\n# Cut video\n", encoding="utf-8")
    (tmp_path / "two.md").write_text("---\ntype: skill\ntags: [video]\n---\n# Render video\n", encoding="utf-8")
    docs = parse_tree(tmp_path)
    proposals = build_plan(docs)
    assert any(p.primitive == "agent" for p in proposals)
    assert any(p.primitive == "skill" and p.slug == "video-procedure" for p in proposals)


def test_agent_workflow_proposes_loop(tmp_path: Path):
    doc = tmp_path / "editor.md"
    doc.write_text("---\ntype: agent\n---\n# Editor\n\n## Workflow\nAnalyze then render.\n", encoding="utf-8")
    proposals = build_plan(parse_tree(tmp_path))
    assert any(p.primitive == "loop" for p in proposals)


def test_planner_does_not_apply_side_effects(tmp_path: Path):
    (tmp_path / "A.md").write_text("# A\n", encoding="utf-8")
    before = sorted(p.name for p in tmp_path.iterdir())
    build_plan(parse_tree(tmp_path))
    assert sorted(p.name for p in tmp_path.iterdir()) == before
