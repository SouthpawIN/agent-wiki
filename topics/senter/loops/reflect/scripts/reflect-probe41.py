#!/usr/bin/env python3
"""REFLECT pass-41 probe: boundary + events.jsonl schema."""
import json, os, glob, sys

REFLECT_DIR = os.path.expanduser("/Users/sovthpaw/Documents/Projects/Projects/topics/senter/loops/reflect")
EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")

# 1. newest reflect .md file (boundary)
mds = [f for f in glob.glob(os.path.join(REFLECT_DIR, "*.md"))]
mds.sort(key=os.path.getmtime)
for f in mds[-3:]:
    print("REFLECT", os.path.basename(f), os.path.getmtime(f))

newest = mds[-1]
import datetime
print("BOUNDARY_EPOCH", os.path.getmtime(newest))
print("BOUNDARY_ISO", datetime.datetime.fromtimestamp(os.path.getmtime(newest)).isoformat())

# 2. events.jsonl schema sample
print("\n=== events.jsonl tail 3 lines ===")
with open(EVENTS) as fh:
    lines = fh.readlines()
print("TOTAL_LINES", len(lines))
for ln in lines[-3:]:
    try:
        o = json.loads(ln)
        print("KEYS:", sorted(o.keys()))
        print(json.dumps(o)[:1200])
        print("---")
    except Exception as e:
        print("PARSE_ERR", repr(e), ln[:200])
