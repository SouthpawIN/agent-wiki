"""Markdown-backed coordination queue for Senter Agent.

The queue is the stable boundary between comprehension and factory work. It is
human-editable, deterministic, and preserves user status/comments on refresh.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .model import Proposal

_HEADER = "# Senter Agent Proposal Queue\n\n> Human-editable GOOP proposals. `[ ]` proposed, `[~]` reviewing, `[x]` accepted, `[-]` rejected.\n\n"
_ROW = re.compile(r"^- \[([ ~x-])\] `([^:]+):([^`]+)` — (.+?) \| sources: (.+)$")
_LEGACY_ROW = re.compile(r"^- \[([ ~x-])\] `([^`]+)` — (.+?) \| sources: (.+)$")

@dataclass(frozen=True)
class QueueEntry:
    primitive: str
    slug: str
    status: str
    reason: str
    sources: str


def _key(primitive: str, slug: str) -> str:
    return f"{primitive}:{slug}"


def read_queue(path: str | Path) -> dict[str, QueueEntry]:
    path = Path(path)
    if not path.exists():
        return {}
    entries: dict[str, QueueEntry] = {}
    primitive = "context"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            primitive = line[3:].strip().lower().rstrip("s")
            continue
        match = _ROW.match(line)
        if match:
            status, row_primitive, slug, reason, sources = match.groups()
            entries[_key(row_primitive, slug)] = QueueEntry(row_primitive, slug, status, reason, sources)
            continue
        legacy = _LEGACY_ROW.match(line)
        if legacy:
            status, slug, reason, sources = legacy.groups()
            entries[_key(primitive, slug)] = QueueEntry(primitive, slug, status, reason, sources)
    return entries


def write_queue(path: str | Path, proposals: list[Proposal]) -> Path:
    path = Path(path)
    previous = read_queue(path)
    grouped: dict[str, list[Proposal]] = {}
    for proposal in proposals:
        grouped.setdefault(proposal.primitive, []).append(proposal)
    lines = [_HEADER.rstrip("\n")]
    for primitive in ("context", "skill", "agent", "loop"):
        lines += [f"## {primitive.title()}"]
        items = sorted(grouped.get(primitive, []), key=lambda item: item.slug)
        if not items:
            lines.append("- _none_")
            continue
        for item in items:
            old = previous.get(_key(item.primitive, item.slug))
            status = old.status if old else " "
            reason = old.reason if old and status != " " else item.reason
            sources = ", ".join(item.source_documents)
            # Keep the original human-facing slug format for compatibility;
            # the section supplies the primitive and remains easy to edit.
            lines.append(f"- [{status}] `{item.slug}` — {reason} | sources: {sources}")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def update_status(path: str | Path, primitive: str, slug: str, status: str) -> Path:
    """Update one queue row without changing its reason or evidence."""
    if status not in {" ", "~", "x", "-"}:
        raise ValueError("status must be one of: space, ~, x, -")
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    needle = f"`{primitive}:{slug}`"
    plain_needle = f"`{slug}`"
    lines = []
    changed = False
    current_primitive = "context"
    for line in text.splitlines():
        if line.startswith("## "):
            current_primitive = line[3:].strip().lower().rstrip("s")
        if line.startswith("- [") and (needle in line or (plain_needle in line and current_primitive == primitive)):
            line = re.sub(r"^- \[[ ~x-]\]", f"- [{status}]", line, count=1)
            changed = True
        lines.append(line)
    if not changed:
        raise KeyError(f"queue item not found: {primitive}:{slug}")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path

__all__ = ["QueueEntry", "read_queue", "write_queue", "update_status"]
