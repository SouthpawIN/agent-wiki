"""Single safe entry point for the markdown-native Senter runtime."""
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .gepa import CycleResult, run_cycle
from .queue import update_status


class SenterRuntime:
    """Coordinates comprehension without granting runtime permissions."""

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.queue = self.root / ".system" / "proposals.md"
        self.injections = self.root / ".system" / "injections.md"

    def reconcile(self) -> CycleResult:
        return run_cycle(self.root, self.queue)

    def approve(self, primitive: str, slug: str) -> None:
        update_status(self.queue, primitive, slug, "x")

    def review(self, primitive: str, slug: str) -> None:
        update_status(self.queue, primitive, slug, "~")

    def reject(self, primitive: str, slug: str) -> None:
        update_status(self.queue, primitive, slug, "-")

    def unread_injections(self) -> list[str]:
        if not self.injections.exists():
            return []
        lines = self.injections.read_text(encoding="utf-8").splitlines()
        unread = []
        active = False
        for line in lines:
            if line.strip() == "## [UNREAD]":
                active = True
                continue
            if line.startswith("## ") and active:
                break
            if active and line.strip():
                unread.append(line.strip())
        return unread

    def consume_first_injection(self) -> str | None:
        messages = self.unread_injections()
        if not messages:
            return None
        text = self.injections.read_text(encoding="utf-8")
        first = messages[0]
        text = text.replace(f"## [UNREAD]\n{first}", f"## [UNREAD]\n\n## [READ]\n{first}", 1)
        self.injections.write_text(text, encoding="utf-8")
        return first

    def status(self) -> dict:
        result = self.reconcile()
        return {"root": str(self.root), **asdict(result), "unread_injections": len(self.unread_injections())}

    def status_json(self) -> str:
        return json.dumps(self.status(), default=str, indent=2)

__all__ = ["SenterRuntime"]
