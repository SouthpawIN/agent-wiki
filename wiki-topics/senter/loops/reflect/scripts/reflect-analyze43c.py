#!/usr/bin/env python3
"""REFLECT pass-43 detail 2: message/bridge/fleet/wiki events + BLOCKED + per-bot summaries."""
import json, os, datetime
from collections import Counter

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
BOUNDARY = 1788657030.0

def iso(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

events = []
with open(EVENTS) as fh:
    for ln in fh:
        ln = ln.strip()
        if not ln:
            continue
        try:
            o = json.loads(ln)
        except Exception:
            continue
        ts = o.get("ts", 0)
        if isinstance(ts, (int, float)) and ts >= BOUNDARY:
            events.append(o)

# full message events
print("=== ALL message events (full) ===")
for e in events:
    if e.get("kind") == "message":
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} status={e.get('status')} :: {str(e.get('summary',''))[:400]}")

# BLOCKED anywhere
print("\n=== BLOCKED mentions ===")
for e in events:
    s = str(e.get("summary", ""))
    if "BLOCKED" in s.upper():
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} kind={e.get('kind')} :: {s[:300]}")

# bridge events
print("\n=== bridge events ===")
for e in events:
    if e.get("kind") == "bridge":
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} :: {str(e.get('summary',''))[:200]}")

# fleet events (churn?)
print("\n=== fleet events ===")
fleet = [e for e in events if e.get("kind") == "fleet"]
print(f"count={len(fleet)}")
fc = Counter(str(e.get('summary',''))[:80] for e in fleet)
for k, v in fc.most_common(15):
    print(f"  {v:3d}x  {k}")

# wiki events
print("\n=== wiki events ===")
for e in events:
    if e.get("kind") == "wiki":
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} :: {str(e.get('summary',''))[:180]}")
