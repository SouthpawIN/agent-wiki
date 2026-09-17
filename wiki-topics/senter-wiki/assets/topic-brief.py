#!/usr/bin/env python3
"""topic-brief.py — the PRE-PROMPT for a topic (Chris 2026-09-05: "any kind of pre-prompting or pre-planning … when context is being sorted
into the wiki"). Each topic carries `BRIEF.md`: what belongs here (scope), what does NOT (anti-scope → other topic), aliases the cutter
should bind on, the lens the agent should read with (Chris's goal, the questions that matter), standing preferences, and what a good
suggestion looks like for THIS topic. Three readers:
  • the watcher's cutter  — aliases/scope/anti-scope tighten routing (before TF-IDF)
  • the topic agent       — BRIEF.md is prepended to its prompt (pre-planning: what to look for, what to ignore, house rules)
  • Chris                 — it's markdown; edit it to steer a topic. `<!-- chris -->` lines are never rewritten.
The brief is itself maintained by the agent: after each pass it may propose brief deltas (appended under "## Learned"), never rewriting Chris's lines.

  python3 assets/topic-brief.py init <topic>|--all      write a starter BRIEF.md (from README + SCHEMA + wiki index) if missing
  python3 assets/topic-brief.py load <topic>            print the brief as the agent sees it (debug)
"""
import re, sys, json
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"; TOPICS = VAULT / "topics"

def first_para(md):
    body = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)
    for ln in body.splitlines():
        t = ln.strip()
        if t and not t.startswith("#") and not t.startswith("_"): return t[:300]
    return ""

def starter(t):
    d = TOPICS / t; readme = (d / "README.md").read_text(errors="replace") if (d / "README.md").is_file() else ""
    idx = (d / "index.md").read_text(errors="replace") if (d / "index.md").is_file() else ""
    entities = re.findall(r"\[\[topics/[^/]+/wiki/entities/[^|\]]+\|([^\]]+)\]\]", idx)[:12]
    aliases = sorted({t, t.replace("-", " ")} | {e.lower() for e in entities if 3 <= len(e) <= 24})
    others = [p.name for p in TOPICS.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")) and p.name != t]
    return f"""# BRIEF — {t}
_Pre-prompt for the cutter and this topic's agent. Chris edits freely; lines ending `<!-- chris -->` are never rewritten._

## What this topic is
{first_para(readme) or f"Everything Chris says, decides, builds or worries about regarding {t}."}

## Belongs here (scope)
- Anything about: {", ".join(aliases[:8])}
- Decisions, preferences, pains, tools, people and timelines tied to the above

## Does NOT belong here (anti-scope → route elsewhere)
- General Hermes/fleet coordination → `senter` · the wiki UI itself → `senter-wiki` · video/YouTube → `youtube`
- If a cut mentions another topic by name ({", ".join(others[:6])}…) more than this one, it goes there

## Aliases (the cutter binds hard on these words)
{chr(10).join("- " + a for a in aliases)}

## Lens — how to read new context for this topic
- What is Chris trying to achieve here, in his words? What changed since the last pass?
- Which statements are DECISIONS (dated, with why), which are PREFERENCES, which are PAINS, which are open QUESTIONS?
- What did he say twice? (repetition = a skill or a rule)

## Standing preferences (apply to every suggestion)
- Root causes, never band-aids. Everything live and visible. Markdown + built-in Hermes over custom code.
- Bots first, then loops; reuse a fleet bot when one fits; skills auto-apply. No pitches about the build process itself.

## What a good suggestion looks like here
- One line, phrased as a question Chris can say yes to, tied to a quote from him, naming the bot that would do it.

## Learned (agent-appended, newest first)
"""

def load(t):
    p = TOPICS / t / "BRIEF.md"
    return p.read_text(errors="replace") if p.is_file() else ""

def aliases(t):
    b = load(t); m = re.search(r"## Aliases[^\n]*\n([\s\S]*?)(\n## |\Z)", b)
    return [ln[2:].strip().lower() for ln in (m.group(1).splitlines() if m else []) if ln.startswith("- ") and ln[2:].strip()]

def antiscope(t):
    b = load(t); m = re.search(r"## Does NOT belong here[^\n]*\n([\s\S]*?)(\n## |\Z)", b)
    return m.group(1) if m else ""

if __name__ == "__main__":
    a = sys.argv[1:]; cmd = a[0] if a else "init"; tgt = a[1] if len(a) > 1 else "--all"
    names = [p.name for p in sorted(TOPICS.iterdir()) if p.is_dir() and not p.name.startswith(("_", "."))] if tgt == "--all" else [tgt]
    for t in names:
        if cmd == "init":
            p = TOPICS / t / "BRIEF.md"
            if not p.exists(): p.write_text(starter(t)); print("brief", t)
        elif cmd == "load": print(load(t))
        elif cmd == "aliases": print(t, aliases(t))
