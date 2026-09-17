"""Deterministic first-pass proposal engine; it never creates live Hermes objects."""

import re
from collections import defaultdict

from .model import GoopDocument, Proposal, title_slug


_STOP = {"agent", "agents", "allow", "allowed", "application", "context", "document", "files", "from", "into", "loop", "loops", "markdown", "only", "procedure", "proposal", "read", "runtime", "skill", "skills", "source", "system", "that", "the", "this", "with", "workflow"}


def _words(documents: list[GoopDocument]) -> dict[str, list[GoopDocument]]:
    groups: dict[str, list[GoopDocument]] = defaultdict(list)
    for doc in documents:
        keys = {x.lower() for x in doc.tags if x and x.lower() not in _STOP}
        keys.update(x for x in re.findall(r"[a-z][a-z0-9-]{3,}", doc.title.lower()) if x not in _STOP)
        if doc.path.stem.isupper():
            for values in doc.declaration.values():
                for item in values:
                    keys.update(x for x in re.findall(r"[a-z][a-z0-9-]{3,}", item.lower()) if x not in _STOP)
        for key in keys:
            if doc not in groups[key]:
                groups[key].append(doc)
    return groups


def _evidence(doc: GoopDocument) -> bool:
    return bool(doc.tags or doc.explicit_kind or doc.path.stem.isupper())


def build_plan(documents: list[GoopDocument]) -> list[Proposal]:
    """Suggest typed GOOP artifacts from markdown evidence.

    This intentionally stops at proposals. Applying a proposal to Hermes requires
    a later approval/enforcement layer and is never implicit.
    """
    proposals: list[Proposal] = []
    documents = [doc for doc in documents if _evidence(doc)]
    groups = _words(documents)
    for key, docs in sorted(groups.items()):
        if len(docs) < 2:
            continue
        names = [str(d.path) for d in docs]
        proposals.append(Proposal("skill", f"{key}-procedure", f"Repeated tagged concept appears in {len(docs)} source documents.", names))
    skill_docs = [d for d in documents if d.kind == "skill"]
    if len(skill_docs) >= 2:
        proposals.append(Proposal("agent", "skill-cluster-agent", f"{len(skill_docs)} skill documents form a candidate capability cluster.", [str(d.path) for d in skill_docs]))
    agent_docs = [d for d in documents if d.kind == "agent"]
    if len(agent_docs) >= 1 and any(d.sections.get("workflow") or d.sections.get("loop") for d in agent_docs):
        proposals.append(Proposal("loop", "workflow-loop", "An agent document declares a workflow that can be evaluated for repeatable execution.", [str(d.path) for d in agent_docs]))
    return proposals


def plan_dict(documents: list[GoopDocument]) -> dict:
    return {"documents": len(documents), "proposals": [p.as_dict() for p in build_plan(documents)]}
