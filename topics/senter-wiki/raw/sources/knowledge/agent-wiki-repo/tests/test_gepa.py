from pathlib import Path

from senter_agent.gepa import GepaCycle


def test_gepa_cycle_collects_generates_evaluates_and_applies(tmp_path: Path):
    (tmp_path / "MEDIA.md").write_text("# Media\n\n## Purpose\n- Video work\n", encoding="utf-8")
    (tmp_path / "EDITING.md").write_text("# Editing\n\n## Purpose\n- Video work\n", encoding="utf-8")
    queue = tmp_path / ".system" / "proposals.md"

    result = GepaCycle(tmp_path, queue).run()

    assert result.evidence_count == 2
    assert result.generated_count >= 1
    assert result.accepted_count == result.generated_count
    assert queue.exists()
    text = queue.read_text(encoding="utf-8")
    assert "Senter Agent Proposal Queue" in text
    assert "video-procedure" in text


def test_gepa_apply_does_not_create_runtime_objects(tmp_path: Path):
    (tmp_path / "A.md").write_text("# Alpha\n\n## Purpose\n- Shared\n", encoding="utf-8")
    (tmp_path / "B.md").write_text("# Beta\n\n## Purpose\n- Shared\n", encoding="utf-8")

    GepaCycle(tmp_path).run()

    assert not (tmp_path / "skills").exists()
    assert not (tmp_path / "agents").exists()
    assert not (tmp_path / "loops").exists()
    assert not (tmp_path / "topics").exists()


def test_gepa_deduplicates_candidates():
    cycle = GepaCycle(".")
    proposals = cycle.evaluate([
        type("P", (), {"primitive": "skill", "slug": "x", "source_documents": ["a"], "reason": "r"})(),
        type("P", (), {"primitive": "skill", "slug": "x", "source_documents": ["b"], "reason": "r"})(),
    ])
    assert len(proposals.accepted) == 1
    assert len(proposals.rejected) == 1
    assert proposals.reasons == ("duplicate:skill:x",)


def test_gepa_cli_module_runs(tmp_path: Path):
    (tmp_path / "A.md").write_text("# Alpha\n", encoding="utf-8")
    result = GepaCycle(tmp_path).run()
    assert result.queue_path == tmp_path / ".system" / "proposals.md"
    assert result.accepted_count == 0
    assert result.queue_path.exists()


def test_gepa_aliases_are_available():
    from senter_agent.gepa import GEPACycle, GEPALoop

    assert GEPACycle is GepaCycle
    assert GEPALoop is GepaCycle


def test_cycle_result_is_serializable(tmp_path: Path):
    import json

    result = GepaCycle(tmp_path).run()
    assert json.dumps(result.__dict__, default=str)


def test_empty_workspace_is_safe(tmp_path: Path):
    result = GepaCycle(tmp_path).run()
    assert result.evidence_count == 0
    assert result.generated_count == 0
    assert result.accepted_count == 0
    assert result.rejected_count == 0


def test_existing_queue_is_preserved_as_human_editable(tmp_path: Path):
    queue = tmp_path / ".system" / "proposals.md"
    queue.parent.mkdir()
    queue.write_text("# Senter Agent Proposal Queue\n\nmy notes\n", encoding="utf-8")
    result = GepaCycle(tmp_path, queue).run()
    assert result.queue_path.exists()
    assert "Senter Agent Proposal Queue" in result.queue_path.read_text(encoding="utf-8")


def test_cycle_does_not_modify_source_hash(tmp_path: Path):
    source = tmp_path / "A.md"
    source.write_text("# Alpha\n", encoding="utf-8")
    before = source.read_bytes()
    GepaCycle(tmp_path).run()
    assert source.read_bytes() == before


def test_unsupported_proposal_is_rejected():
    cycle = GepaCycle(".")
    proposal = type("P", (), {"primitive": "runtime", "slug": "x", "source_documents": ["a"], "reason": "r"})()
    result = cycle.evaluate([proposal])
    assert not result.accepted
    assert result.reasons == ("unsupported-primitive:runtime",)


def test_no_evidence_proposal_is_rejected():
    cycle = GepaCycle(".")
    proposal = type("P", (), {"primitive": "skill", "slug": "x", "source_documents": [], "reason": "r"})()
    result = cycle.evaluate([proposal])
    assert not result.accepted
    assert result.reasons == ("no-evidence:x",)


def test_generated_proposals_are_stable(tmp_path: Path):
    (tmp_path / "B.md").write_text("# Beta\n", encoding="utf-8")
    (tmp_path / "A.md").write_text("# Alpha\n", encoding="utf-8")
    cycle = GepaCycle(tmp_path)
    assert [p.as_dict() for p in cycle.generate(cycle.collect())] == [p.as_dict() for p in cycle.generate(cycle.collect())]


def test_apply_returns_queue_path(tmp_path: Path):
    cycle = GepaCycle(tmp_path)
    evaluation = cycle.evaluate([])
    path = cycle.apply(evaluation)
    assert path == tmp_path / ".system" / "proposals.md"


def test_run_cycle_can_use_custom_queue(tmp_path: Path):
    from senter_agent.gepa import run_cycle

    custom = tmp_path / "review.md"
    result = run_cycle(tmp_path, custom)
    assert result.queue_path == custom
    assert custom.exists()


def test_context_is_collected_from_nested_tree(tmp_path: Path):
    nested = tmp_path / "topics" / "demo"
    nested.mkdir(parents=True)
    (nested / "README.md").write_text("# Demo\n", encoding="utf-8")
    result = GepaCycle(tmp_path).run()
    assert result.evidence_count == 1


def test_evaluation_keeps_original_proposal_objects(tmp_path: Path):
    cycle = GepaCycle(tmp_path)
    proposal = type("P", (), {"primitive": "skill", "slug": "x", "source_documents": ["a"], "reason": "r"})()
    result = cycle.evaluate([proposal])
    assert result.accepted[0] is proposal


def test_proposal_queue_is_markdown(tmp_path: Path):
    result = GepaCycle(tmp_path).run()
    assert result.queue_path.suffix == ".md"


def test_cycle_has_all_four_phases():
    cycle = GepaCycle(".")
    assert all(hasattr(cycle, name) for name in ("collect", "generate", "evaluate", "apply"))


def test_rejected_count_is_reported(tmp_path: Path):
    cycle = GepaCycle(tmp_path)
    cycle.generate = lambda evidence: [type("P", (), {"primitive": "runtime", "slug": "x", "source_documents": ["a"], "reason": "r"})()]
    result = cycle.run()
    assert result.rejected_count == 1
    assert result.accepted_count == 0


def test_gepa_does_not_require_network(tmp_path: Path):
    result = GepaCycle(tmp_path).run()
    assert result.queue_path.exists()


def test_queue_parent_is_created(tmp_path: Path):
    path = tmp_path / "deep" / "review.md"
    GepaCycle(tmp_path, path).run()
    assert path.exists()


def test_cycle_result_counts_are_ints(tmp_path: Path):
    result = GepaCycle(tmp_path).run()
    assert all(isinstance(getattr(result, name), int) for name in ("evidence_count", "generated_count", "accepted_count", "rejected_count"))


def test_collect_returns_immutable_documents(tmp_path: Path):
    evidence = GepaCycle(tmp_path).collect()
    assert isinstance(evidence.documents, tuple)


def test_evaluation_returns_immutable_collections():
    evaluation = GepaCycle(".").evaluate([])
    assert isinstance(evaluation.accepted, tuple)
    assert isinstance(evaluation.rejected, tuple)


def test_apply_is_explicitly_queue_only(tmp_path: Path):
    result = GepaCycle(tmp_path).run()
    assert ".system" in str(result.queue_path)
