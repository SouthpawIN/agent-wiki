#!/usr/bin/env python3
"""Publish every wiki bot as a Hermes skill, one loader per bot.

The wiki is the source of truth. This script renders `bots/<slug>/BOT.md` into
`$HERMES_HOME/skills/bots/<slug>/SKILL.md` so a session can load the bot with a
single skill_view("bot-<slug>").

Usage:
    python tools/publish_skills.py [wiki-root] [hermes-home]
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

DESC_LIMIT = 60


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}
    out: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip().strip("[]")
    return out


def section(text: str, heading: str) -> str:
    """Return a block declared as `**Heading.** ...` or `## Heading ...` (prefix match)."""
    bold = re.search(rf"^\*\*{re.escape(heading)}\.\*\*\s*(.+?)(?=\n\s*\n##\s)", text, re.M | re.I | re.S)
    if bold:
        return bold.group(1).strip()
    head = re.search(rf"^##\s+{re.escape(heading)}\b[^\n]*\n(.+?)(?=^##\s)", text, re.M | re.I | re.S)
    if head:
        return head.group(1).strip()
    return ""


def mission(text: str) -> str:
    value = section(text, "Mission")
    if value:
        return value.split("\n\n")[0].strip()
    head = re.search(r"^##\s+Mission[^\n]*\n(.+?)(?=^##\s)", text, re.M | re.I | re.S)
    return head.group(1).strip() if head else ""


def first_sentence(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"^\*\*Mission\.\*\*\s*", "", value)
    cut = re.split(r"(?<=[.!?])\s", value, maxsplit=1)[0]
    return cut


def render(bot_file: Path, wiki_root: Path) -> tuple[str, str]:
    text = bot_file.read_text(encoding="utf-8")
    meta = frontmatter(text)
    slug = meta.get("slug") or bot_file.parent.name
    name = meta.get("name") or slug
    status = meta.get("status", "seeding")
    description = first_sentence(mission(text) or f"{name} bot for {slug}")
    if len(description) > DESC_LIMIT:
        description = description[: DESC_LIMIT - 1].rsplit(" ", 1)[0] + "…"

    skills = sorted((bot_file.parent / "skills").glob("*/SKILL.md"))
    loops = sorted((bot_file.parent / "loops").glob("*.md"))
    holds = section(text, "Hold points")
    needs = section(text, "Needs from Chris")
    loop_steps = section(text, "Operating loop")

    lines = [
        "---",
        f"name: bot-{slug}",
        f"description: \"{description}\"",
        "version: 1.0.0",
        "author: Klerik",
        "license: MIT",
        "metadata:",
        "  hermes:",
        f"    tags: [bot, {slug}]",
        "---",
        "",
        f"# {name} — {slug}",
        "",
        f"**Status.** `{status}` · wiki: `{bot_file}`",
        "",
        f"**Mission.** {mission(text) or 'n/a'}",
        "",
    ]
    if loop_steps:
        lines += ["## Operating loop", "", loop_steps, ""]
    if skills:
        lines += ["## Skills (full procedures in the wiki)", ""]
        for skill in skills:
            lines.append(f"- `{skill}`")
        lines.append("")
    if loops:
        lines += ["## Loops", ""]
        for loop in loops:
            state = frontmatter(loop.read_text(encoding="utf-8")).get("state", "spec")
            sched = frontmatter(loop.read_text(encoding="utf-8")).get("schedule", "")
            lines.append(f"- `{loop}` ({sched}, {state})")
        lines.append("")
    if holds:
        lines += ["## Hold points — never do these alone", "", holds, ""]
    if needs:
        lines += ["## Needs from Chris", "", needs, ""]
    lines += [
        "## How to use this skill",
        "",
        f"1. Read `{bot_file}` for the current mission and log.",
        f"2. Open the specific procedure under `{bot_file.parent}/skills/` before acting.",
        "3. Append one line to the bot's `## Log` after any material change.",
        "",
    ]
    return slug, "\n".join(lines)


def main() -> int:
    wiki_root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    hermes_home = Path(sys.argv[2] if len(sys.argv) > 2 else os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    skills_root = hermes_home / "skills"
    published = 0
    for bot_file in sorted(wiki_root.glob("bots/*/BOT.md")):
        if bot_file.parent.name.startswith("_"):
            continue
        slug, content = render(bot_file, wiki_root)
        target = skills_root / "bots" / slug / "SKILL.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        published += 1
        print(f"published bot-{slug} -> {target}")
    print(f"{published} bot skills published under {skills_root}/bots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
