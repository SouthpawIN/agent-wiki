#!/usr/bin/env python3
import os, glob, datetime

CUTOFF = 1788599070  # pass-34 mtime 04:04:30 CDT

def fmt(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

# Static inputs
static = [
    "/Users/sovthpaw/Documents/Projects/Projects/Ideas.md",
    "/Users/sovthpaw/Documents/Projects/Projects/topics/senter/process/lessons.md",
]
print("=== static inputs ===")
for p in static:
    try:
        m = os.path.getmtime(p)
        print(f"  {fmt(m)}  newer={m > CUTOFF}  {p}")
    except OSError as e:
        print(f"  MISSING  {p}  {e}")

print("\n=== queue.md / session.md newer than cutoff ===")
base = "/Users/sovthpaw/Documents/Projects/Projects/topics"
qs = glob.glob(base + "/*/.system/queue.md") + glob.glob(base + "/*/.system/session.md")
for p in sorted(qs):
    m = os.path.getmtime(p)
    if m > CUTOFF:
        print(f"  {fmt(m)}  NEWER  {p}")

print("\n=== all queue.md / session.md (with mtime, for context) ===")
for p in sorted(qs):
    m = os.path.getmtime(p)
    flag = "  <== NEW" if m > CUTOFF else ""
    print(f"  {fmt(m)}  {p}{flag}")
