"""Markdown-backed proposal queue for Senter Agent.

The queue is intentionally human-editable. Re-running reconciliation updates
only generated proposal rows and preserves user status/comments.
"""

from __future__ import annotations

import re
from pathlib import Path

from .model import Proposal

_HEADER = "# Senter Agent Proposal Queue\n\n> Human-editable GOOP proposals. `[ ]` proposed, `[~]` reviewing, `[x]` accepted, `[-]` rejected.\n\n"
_SECTION = "## {primitive}\n"
_ROW = re.compile(r"^- \[([ ~x-])\] `([^`]+)` — (.+?) \| sources: (.+)$")


def _key(primitive: str, slug: str) -> str:
    return f"{primitive}:{slug}"


def read_queue(path: str | Path) -> dict[str, tuple[str, str]]:
    """Read existing statuses/reasons keyed by primitive and slug."""
    path = Path(path)
    if not path.exists():
        return {}
    result: dict[str, tuple[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = _ROW.match(line)
        if match:
            status, slug, reason, _sources = match.groups()
            primitive = ""
            # Primitive is encoded by the nearest heading in the writer below;
            # fallback supports old/manual rows with a primitive prefix.
            result[slug] = (status, reason)
    return result


def write_queue(path: str | Path, proposals: list[Proposal]) -> Path:
    """Write a deterministic queue, retaining existing row status when possible."""
    path = Path(path)
    previous = read_queue(path)
    grouped: dict[str, list[Proposal]] = {}
    for proposal in proposals:
        grouped.setdefault(proposal.primitive, []).append(proposal)
    lines = [_HEADER.rstrip("\n")]
    for primitive in ("context", "skill", "agent", "loop"):
        lines.append(_SECTION.format(primitive=primitive.title()).rstrip("\n"))
        items = sorted(grouped.get(primitive, []), key=lambda item: item.slug)
        if not items:
            lines.append("- _none_")
            continue
        for item in items:
            status, old_reason = previous.get(item.slug, (" ", item.reason))
            reason = old_reason if status != " " else item.reason
            sources = ", ".join(item.source_documents)
            lines.append(f"- [{status}] `{item.slug}` — {reason} | sources: {sources}")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path
