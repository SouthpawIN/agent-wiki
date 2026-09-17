#!/usr/bin/env python3
"""List topics/*/.system/queue.md + session.md with mtimes (fresh = new since pass-41)."""
import os, glob, datetime

TOPICS = "/Users/sovthpaw/Documents/Projects/Projects/topics"
SKIP = {"_archive", "_global", "_inbox"}
BOUNDARY = 1788649670.249  # pass-41 file mtime

rows = []
for d in sorted(os.listdir(TOPICS)):
    if d in SKIP:
        continue
    base = os.path.join(TOPICS, d)
    if not os.path.isdir(base):
        continue
    for fn in ("queue.md", "session.md"):
        p = os.path.join(base, ".system", fn)
        if os.path.isfile(p):
            mt = os.path.getmtime(p)
            rows.append((mt, d, fn, p))

rows.sort(reverse=True)
print("== queue.md / session.md by mtime (newest first) ==")
for mt, d, fn, p in rows:
    fresh = "NEW" if mt > BOUNDARY else "    "
    print(f"{fresh} {datetime.datetime.fromtimestamp(mt).strftime('%m-%d %H:%M:%S')}  {d}/{fn}")
print(f"\nTotal: {len(rows)} files, {sum(1 for r in rows if r[0] > BOUNDARY)} NEW since pass-41")
