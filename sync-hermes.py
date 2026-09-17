#!/usr/bin/env python3
"""Generate live index pages for Senter Wiki from Hermes state."""
import json, os, sqlite3, subprocess
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"
SKILLS_SRC = Path.home() / ".hermes/skills"
PROFILES_SRC = Path.home() / ".hermes/profiles"
KANBAN_DB = Path.home() / ".hermes/kanban.db"

def gen_skills_index():
    skills = sorted([d.name for d in SKILLS_SRC.iterdir() if d.is_dir() and not d.name.startswith('.')])
    lines = ["---", "title: Skills", "updated: 2026-09-17", "type: skills-index", "---", "",
             "# Skills", "", "> Live index of all Hermes skills. Each links to its SKILL.md.", ""]
    for s in skills:
        lines.append(f"- **[{s}](hermes-skills/{s}/SKILL.md)**")
    (VAULT / "skills-capabilities/index.md").write_text("\n".join(lines))
    print(f"Skills index: {len(skills)} skills")

def gen_bots_index():
    profiles = sorted([d.name for d in PROFILES_SRC.iterdir() if d.is_dir()])
    lines = ["---", "title: Bots", "updated: 2026-09-17", "type: bots-index", "---", "",
             "# Bots", "", "> Live index of all Hermes profiles. Each links to its profile.", ""]
    for p in profiles:
        soul = PROFILES_SRC / p / "SOUL.md"
        desc = ""
        if soul.exists():
            text = soul.read_text()
            for line in text.split('\n'):
                if line.startswith('description:'):
                    desc = line.split(':',1)[1].strip().strip("'\"")
                    break
        lines.append(f"- **[{p}](hermes-profiles/{p}/SOUL.md)**" + (f" — {desc}" if desc else ""))
    (VAULT / "bots-profiles/index.md").write_text("\n".join(lines))
    print(f"Bots index: {len(profiles)} profiles")

def gen_loops_index():
    result = subprocess.run(['hermes', 'cron', 'list'], capture_output=True, text=True)
    lines = ["---", "title: Loops", "updated: 2026-09-17", "type: loops-index", "---", "",
             "# Loops", "", "> Live index of all cron jobs and automations.", "",
             "## Cron Jobs", ""]
    if result.returncode == 0 and result.stdout.strip():
        lines.append(result.stdout)
    else:
        lines.append("No cron jobs installed.")
    
    # Kanban tasks
    if KANBAN_DB.exists():
        conn = sqlite3.connect(KANBAN_DB)
        conn.row_factory = sqlite3.Row
        tasks = conn.execute("SELECT id, status, assignee, title FROM tasks WHERE status != 'archived' ORDER BY created_at DESC LIMIT 50").fetchall()
        conn.close()
        lines.extend(["", "## Kanban Tasks", ""])
        for t in tasks:
            icon = "✓" if t['status'] == 'done' else "⊘" if t['status'] == 'blocked' else "◻"
            lines.append(f"- {icon} **{t['assignee']}** — {t['title']}")
    
    (VAULT / "triggers-loops/index.md").write_text("\n".join(lines))
    print(f"Loops index: cron + kanban")

if __name__ == '__main__':
    gen_skills_index()
    gen_bots_index()
    gen_loops_index()
    print("Done.")
