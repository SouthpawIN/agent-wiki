#!/usr/bin/env python3
"""Check mtimes of active .system files + Ideas.md/lessons.md since pass-24 (14:03:36)."""
import os, datetime
ROOT = "/Users/sovthpaw/Documents/Projects/Projects"
TOP = os.path.join(ROOT, "topics")
CUT = datetime.datetime(2026, 9, 4, 14, 3, 36).timestamp()

topics = ["senter", "klerik", "anser", "senter-wiki", "hermes-agent", "weaver", "turbofit", "_global", "evolutionary", "pocket-shop", "burner-phone"]
targets = []
for t in topics:
    for fn in ("queue.md", "session.md"):
        p = os.path.join(TOP, t, ".system", fn)
        if os.path.exists(p):
            targets.append(p)
targets += [os.path.join(ROOT, "Ideas.md"), os.path.join(TOP, "senter", "process", "lessons.md")]

print("=== files sorted by mtime (desc) ===")
rows = []
for p in targets:
    mt = os.path.getmtime(p)
    rows.append((mt, p))
for mt, p in sorted(rows, reverse=True):
    flag = "  <-- NEW (since 14:03)" if mt > CUT else ""
    print(f"  {datetime.datetime.fromtimestamp(mt).strftime('%m-%d %H:%M:%S')}  {p}{flag}")
