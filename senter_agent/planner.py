"""Deterministic first-pass proposal engine; it never creates live Hermes objects."""

import re
from collections import defaultdict

from .model import GoopDocument, Proposal, title_slug


def _words(documents: list[GoopDocument]) -> dict[str, list[GoopDocument]]:
    groups: dict[str, list[GoopDocument]] = defaultdict(list)
    for doc in documents:
        keys = {x.lower() for x in doc.tags if x}
        keys.update(re.findall(r"[a-z][a-z0-9-]{3,}", doc.title.lower()))
        for key in keys:
            groups[key].append(doc)
    return groups


def build_plan(documents: list[GoopDocument]) -> list[Proposal]:
    """Suggest typed GOOP artifacts from markdown evidence.

    This intentionally stops at proposals. Applying a proposal to Hermes requires
    a later approval/enforcement layer and is never implicit.
    """
    proposals: list[Proposal] = []
    groups = _words(documents)
    for key, docs in sorted(groups.items()):
        if len(docs) < 2:
            continue
        names = [str(d.path) for d in docs]
        proposals.append(Proposal("skill", f"{key}-procedure", f"Repeated concept appears in {len(docs)} markdown documents.", names))
    skill_docs = [d for d in documents if d.kind == "skill"]
    if len(skill_docs) >= 2:
        proposals.append(Proposal("agent", "skill-cluster-agent", f"{len(skill_docs)} skill documents form a candidate capability cluster.", [str(d.path) for d in skill_docs]))
    agent_docs = [d for d in documents if d.kind == "agent"]
    if len(agent_docs) >= 1 and any(d.sections.get("workflow") or d.sections.get("loop") for d in agent_docs):
        proposals.append(Proposal("loop", "workflow-loop", "An agent document declares a workflow that can be evaluated for repeatable execution.", [str(d.path) for d in agent_docs]))
    return proposals


def plan_dict(documents: list[GoopDocument]) -> dict:
    return {"documents": len(documents), "proposals": [p.as_dict() for p in build_plan(documents)]}
