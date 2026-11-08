#!/usr/bin/env python3
"""Render every bot's identity into its Hermes profile.

publish_skills.py makes a bot loadable; this makes it *be* a profile. It writes
$HERMES_HOME/profiles/<profile>/SOUL.md from bots/<slug>/BOT.md, installs the
published bot skill, and reports the mapping.

The `hermes` slug maps to the profile name `mesh` because "hermes" is reserved by
Hermes itself. The wiki slug stays `hermes`; only the profile name differs.

Usage:
    python tools/publish_profiles.py [wiki-root] [hermes-home]
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# slug -> profile name (only where they differ)
PROFILE_ALIASES = {"hermes": "mesh"}


def profile_for(slug: str) -> str:
    return PROFILE_ALIASES.get(slug, slug)


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"(?:^##\s+{re.escape(heading)}[^\n]*\n|\*\*{re.escape(heading)}\.\*\*\s*)(.+?)(?=^##\s)",
        text, re.M | re.S,
    )
    return match.group(1).strip() if match else ""


def soul_for(slug: str, bot_text: str) -> str:
    title = re.search(r"^#\s+(.+)$", bot_text, re.M)
    name = title.group(1).strip() if title else slug
    mission = section(bot_text, "Mission").split("\n\n")[0].strip()
    holds = "\n".join(line for line in section(bot_text, "Hold points").splitlines()
                      if line.strip().startswith("-"))
    return f"""# {name}

{mission}

## How you work
1. Your wiki bot file is `bots/{slug}/BOT.md` — read it first.
2. Your procedures are under `bots/{slug}/skills/`. Load the one that matches the task.
3. Append one line to your `## Log` after any material change.
4. Cross-bot work is filed in `bots/_fleet/.system/queue.md`, never by editing
   another bot's BOT.md.

## Hold points — never do these alone
{holds}

## Voice
Plain, concrete, outcome-first. No hype, no filler. Public work is credited to sovthpaw.
"""


def ensure_profile(name: str, description: str) -> None:
    subprocess.run(
        ["hermes", "profile", "create", name, "--no-skills", "--no-alias",
         "--description", description],
        check=False, capture_output=True, text=True,
    )


def main() -> int:
    wiki = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    home = Path(sys.argv[2] if len(sys.argv) > 2
                else os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    profiles = home / "profiles"
    published = 0
    for bot_file in sorted(wiki.glob("bots/*/BOT.md")):
        slug = bot_file.parent.name
        if slug.startswith("_"):
            continue
        profile = profile_for(slug)
        bot_text = bot_file.read_text(encoding="utf-8")
        mission = section(bot_text, "Mission").split("\n\n")[0].strip()
        ensure_profile(profile, mission[:120])
        target = profiles / profile
        if not target.exists():
            print(f"  ! {profile}: profile missing, skipping")
            continue
        (target / "SOUL.md").write_text(soul_for(slug, bot_text), encoding="utf-8")
        skills = target / "skills"
        skills.mkdir(parents=True, exist_ok=True)
        source = home / "skills" / "bots" / slug
        if source.exists():
            dest = skills / f"bot-{slug}"
            shutil.rmtree(dest, ignore_errors=True)
            shutil.copytree(source, dest)
        published += 1
        print(f"published {slug} -> profile {profile}")
    print(f"{published} bot profiles published under {profiles}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
