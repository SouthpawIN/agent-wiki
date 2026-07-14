"""Deterministic GEPA cycle for the markdown-native Senter language.

GEPA here means Collect -> Generate -> Evaluate -> Apply.  Apply is deliberately
limited to the human-editable proposal queue; live Hermes objects remain behind
separate approval adapters.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .model import GoopDocument, Proposal
from .parser import parse_tree
from .planner import build_plan
from .queue import write_queue


@dataclass(frozen=True)
class Evidence:
    documents: tuple[GoopDocument, ...]
    existing_queue: Path | None = None


@dataclass(frozen=True)
class Evaluation:
    accepted: tuple[Proposal, ...]
    rejected: tuple[Proposal, ...]
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class CycleResult:
    evidence_count: int
    generated_count: int
    accepted_count: int
    rejected_count: int
    queue_path: Path


class GepaCycle:
    """Run one safe reconciliation cycle over a Markdown workspace."""

    def __init__(self, root: str | Path, queue_path: str | Path | None = None):
        self.root = Path(root)
        self.queue_path = Path(queue_path) if queue_path else self.root / ".system" / "proposals.md"

    def collect(self) -> Evidence:
        return Evidence(tuple(parse_tree(self.root)), self.queue_path if self.queue_path.exists() else None)

    def generate(self, evidence: Evidence) -> list[Proposal]:
        return build_plan(list(evidence.documents))

    def evaluate(self, candidates: list[Proposal]) -> Evaluation:
        accepted: list[Proposal] = []
        rejected: list[Proposal] = []
        reasons: list[str] = []
        seen: set[tuple[str, str]] = set()
        for proposal in candidates:
            key = (proposal.primitive, proposal.slug)
            if key in seen:
                rejected.append(proposal)
                reasons.append(f"duplicate:{proposal.primitive}:{proposal.slug}")
                continue
            seen.add(key)
            if proposal.primitive not in {"context", "skill", "agent", "loop"}:
                rejected.append(proposal)
                reasons.append(f"unsupported-primitive:{proposal.primitive}")
                continue
            if not proposal.source_documents:
                rejected.append(proposal)
                reasons.append(f"no-evidence:{proposal.slug}")
                continue
            accepted.append(proposal)
        return Evaluation(tuple(accepted), tuple(rejected), tuple(reasons))

    def apply(self, evaluation: Evaluation) -> Path:
        """Apply only to the review queue, never to Hermes or source Markdown."""
        return write_queue(self.queue_path, list(evaluation.accepted))

    def run(self) -> CycleResult:
        evidence = self.collect()
        candidates = self.generate(evidence)
        evaluation = self.evaluate(candidates)
        queue_path = self.apply(evaluation)
        return CycleResult(
            evidence_count=len(evidence.documents),
            generated_count=len(candidates),
            accepted_count=len(evaluation.accepted),
            rejected_count=len(evaluation.rejected),
            queue_path=queue_path,
        )


def run_cycle(root: str | Path, queue_path: str | Path | None = None) -> CycleResult:
    return GepaCycle(root, queue_path).run()


# Friendly alias for callers that use the spelling from the whitepaper.
GEPACycle = GepaCycle
GEPALoop = GepaCycle
__all__ = ["Evidence", "Evaluation", "CycleResult", "GepaCycle", "GEPACycle", "GEPALoop", "run_cycle"]


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Run one safe Senter GEPA cycle")
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--queue", default=None)
    args = parser.parse_args()
    print(json.dumps(run_cycle(args.root, args.queue).__dict__, default=str, indent=2))
