#!/usr/bin/env python3
"""Verify the bot-first layout: identity, required sections, declared artifacts, links."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = ("mission", "interface", "skills", "loops", "hold points", "needs from chris")
LINK = re.compile(r"\[\[([^\]|#]+)")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}
    out: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip()
    return out


def check(root: Path) -> list[str]:
    problems: list[str] = []
    bots = sorted(p for p in root.glob("bots/*/BOT.md") if p.parent.name.startswith("_") is False)
    if not bots:
        return ["no bots found under bots/*/BOT.md"]

    for bot_file in bots:
        slug = bot_file.parent.name
        text = bot_file.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("type") != "bot":
            problems.append(f"{slug}: BOT.md missing 'type: bot'")
        if meta.get("slug") != slug:
            problems.append(f"{slug}: frontmatter slug {meta.get('slug')!r} != directory {slug!r}")
        if meta.get("status") not in {"active", "seeding", "paused", "blocked", "live"}:
            problems.append(f"{slug}: invalid status {meta.get('status')!r}")

        lowered = text.lower()
        for section in REQUIRED_SECTIONS:
            if f"## {section}" in lowered:
                continue
            # a short bold-line declaration (e.g. "**Interface.**") is equivalent
            if f"**{section}.**" in lowered:
                continue
            problems.append(f"{slug}: missing section '{section}'")

        if meta.get("status") == "blocked":
            needs = lowered.split("## needs from chris")
            if len(needs) < 2 or len(needs[1].split("## ")[0].strip()) < 20:
                problems.append(f"{slug}: status blocked but no actionable 'Needs from Chris'")

        for rel in LINK.findall(text):
            target = rel.strip()
            if target.endswith("/") or target.upper().startswith("CONFIRM"):
                continue
            if not (root / f"{target}.md").exists() and not (root / target).exists():
                problems.append(f"{slug}: broken link [[{target}]]")

        for skill in sorted((bot_file.parent / "skills").glob("*/SKILL.md")):
            head = skill.read_text(encoding="utf-8")[:400]
            if "name:" not in head or "description:" not in head:
                problems.append(f"{slug}: {skill.parent.name} skill lacks name/description frontmatter")

        for loop in sorted((bot_file.parent / "loops").glob("*.md")):
            body = loop.read_text(encoding="utf-8")
            header = body.split("---")[1] if body.startswith("---") else ""
            for field in ("bot:", "schedule:", "state:", "skill:"):
                if field not in header:
                    problems.append(f"{slug}: loop {loop.name} missing '{field}'")
    return problems


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    problems = check(root)
    bots = len(list(root.glob("bots/*/BOT.md")))
    skills = len(list(root.glob("bots/*/skills/*/SKILL.md")))
    loops = len(list(root.glob("bots/*/loops/*.md")))
    print(f"bots={bots} skills={skills} loops={loops} problems={len(problems)}")
    for problem in problems:
        print(f"  - {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
