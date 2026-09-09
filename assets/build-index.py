#!/usr/bin/env python3
"""build-index.py — progressive-disclosure index for a topic (2026-09-05, Chris: "the wiki is a memory layer for Hermes;
the side chat reads it by progressive disclosure, like skills are discovered").

For every topic, writes topics/<t>/.system/INDEX.md: one line per file under README.md, .system/, skills/, agents/, loops/
with size, a one-line gist (first heading or first non-empty line), and for markdown files the H2 outline with line
numbers — so an agent can pick a file, then a section, then read just that range (read_file offset/limit).

Layer 0 = the topic row in the wiki (summary).  Layer 1 = INDEX.md (this file, ~1 line per file).
Layer 2 = a file's H2 outline (in INDEX.md).  Layer 3 = read_file the range.  Nothing is summarised away.
"""
import re, sys, json
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"
SKIP_DIRS = {"mirror", "claims", "archive", "selfmodel"}

def gist(p: Path, txt: str) -> str:
    for ln in txt.splitlines():
        s = ln.strip().lstrip("#").strip()
        if s and not s.startswith("---") and not s.startswith("{"):
            return s[:110]
    return ""

def outline(txt: str, max_items=40):
    out = []
    for i, ln in enumerate(txt.splitlines(), 1):
        m = re.match(r"^(#{1,3})\s+(.+)$", ln)
        if m and len(m.group(1)) <= 2:
            out.append((i, len(m.group(1)), m.group(2).strip()[:90]))
        if len(out) >= max_items: break
    return out

def build(topic: Path):
    rows = []
    files = [topic / "README.md"] + sorted(
        [p for sub in (".system", "skills", "agents", "loops", "process", "plans") for p in (topic / sub).rglob("*")
         if p.is_file() and not any(d in p.parts for d in SKIP_DIRS) and p.name != "INDEX.md"]
    )
    total = 0
    for p in files:
        if not p.is_file(): continue
        try: txt = p.read_text(errors="replace")
        except Exception: continue
        size = len(txt); total += size
        rel = p.relative_to(topic)
        lines = txt.count("\n") + 1
        rows.append((rel, size, lines, gist(p, txt), outline(txt) if p.suffix == ".md" else []))
    lines_out = [f"# INDEX — topics/{topic.name}", f"_{len(rows)} files · {total/1024:.0f} KB · regenerate: `python3 assets/build-index.py`_", "",
                 "Read order for an agent: this file → pick a file below → its outline → `read_file offset=<line> limit=<n>`. Sessions under `.system/sessions/` are full transcripts (largest; go by outline).", ""]
    # group by folder
    groups = {}
    for rel, size, n, g, ol in rows:
        groups.setdefault(str(rel.parent) if str(rel.parent) != "." else "", []).append((rel, size, n, g, ol))
    for grp in sorted(groups, key=lambda k: (k != "", k)):
        lines_out.append(f"## {grp or 'root'}")
        for rel, size, n, g, ol in groups[grp]:
            lines_out.append(f"- `{rel}` — {size/1024:.0f} KB, {n} lines — {g}")
            for (ln, lvl, h) in ol[:14]:
                lines_out.append(f"    - L{ln} {'#'*lvl} {h}")
            if len(ol) > 14: lines_out.append(f"    - … {len(ol)-14} more headings")
        lines_out.append("")
    (topic / ".system").mkdir(exist_ok=True)
    (topic / ".system" / "INDEX.md").write_text("\n".join(lines_out) + "\n")
    return len(rows), total

if __name__ == "__main__":
    want = sys.argv[1:] or [d.name for d in (VAULT / "topics").iterdir() if d.is_dir() and not d.name.startswith("_")]
    for t in want:
        n, total = build(VAULT / "topics" / t)
        print(f"{t}: {n} files, {total/1024:.0f} KB → topics/{t}/.system/INDEX.md")
