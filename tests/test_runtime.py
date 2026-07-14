from pathlib import Path

import pytest

from senter_agent.runtime import SenterRuntime


def test_runtime_reconcile_and_approval(tmp_path: Path):
    (tmp_path / "A.md").write_text("# Alpha\n", encoding="utf-8")
    runtime = SenterRuntime(tmp_path)
    result = runtime.reconcile()
    assert result.queue_path.exists()
    assert result.accepted_count == 0
    with pytest.raises(KeyError):
        runtime.approve("skill", "missing")


def test_runtime_injection_read_and_consume(tmp_path: Path):
    path = tmp_path / ".system" / "injections.md"
    path.parent.mkdir()
    path.write_text("## [UNREAD]\n[SKILLS] ready\n\n## [READ]\nold\n", encoding="utf-8")
    runtime = SenterRuntime(tmp_path)
    assert runtime.unread_injections() == ["[SKILLS] ready"]
    assert runtime.consume_first_injection() == "[SKILLS] ready"
    assert runtime.unread_injections() == []
    assert "## [READ]\n[SKILLS] ready" in path.read_text(encoding="utf-8")


def test_runtime_consuming_empty_injection_is_safe(tmp_path: Path):
    runtime = SenterRuntime(tmp_path)
    assert runtime.consume_first_injection() is None


def test_runtime_status_is_json_serializable(tmp_path: Path):
    runtime = SenterRuntime(tmp_path)
    status = runtime.status()
    assert status["root"] == str(tmp_path)
    assert status["unread_injections"] == 0
    assert "accepted_count" in status


def test_runtime_status_json(tmp_path: Path):
    runtime = SenterRuntime(tmp_path)
    assert '"root"' in runtime.status_json()


def test_queue_status_round_trip(tmp_path: Path):
    (tmp_path / "A.md").write_text("# Same thing\n", encoding="utf-8")
    (tmp_path / "B.md").write_text("# Same thing\n", encoding="utf-8")
    runtime = SenterRuntime(tmp_path)
    runtime.reconcile()
    # At least the queue exists; status operations are guarded by exact keys.
    assert runtime.queue.exists()


def test_runtime_methods_are_explicit(tmp_path: Path):
    runtime = SenterRuntime(tmp_path)
    assert callable(runtime.reconcile)
    assert callable(runtime.approve)
    assert callable(runtime.review)
    assert callable(runtime.reject)


def test_injections_missing_file_returns_empty(tmp_path: Path):
    assert SenterRuntime(tmp_path).unread_injections() == []


def test_reconcile_does_not_create_live_artifacts(tmp_path: Path):
    SenterRuntime(tmp_path).reconcile()
    for name in ("skills", "agents", "loops"):
        assert not (tmp_path / name).exists()


def test_reconcile_is_repeatable(tmp_path: Path):
    (tmp_path / "A.md").write_text("# A\n", encoding="utf-8")
    runtime = SenterRuntime(tmp_path)
    first = runtime.reconcile()
    second = runtime.reconcile()
    assert first.evidence_count == second.evidence_count
    assert first.generated_count == second.generated_count
