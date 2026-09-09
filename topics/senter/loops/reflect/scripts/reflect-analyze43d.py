#!/usr/bin/env python3
"""REFLECT pass-43 detail 3: proposals, chris FILED, per-bot terminal work, senter 225 breakdown."""
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

# proposals / PROPOSAL / chris FILED / skill distill
print("=== PROPOSAL / FILED / SKILL / WORKER / AGENT / DISTILL signals ===")
for e in events:
    s = str(e.get("summary", ""))
    if any(x in s for x in ["PROPOSAL", "FILED", "SKILL", "distill", "WORKER", "AGENT ", "new bot", "needs_chris", "NEEDS-CHRIS"]):
        print(f"  [{iso(e['ts'])}] {e.get('bot')} {e.get('kind')} :: {s[:200]}")

# what did hermes do (117 events, 69 turns)
print("\n=== hermes (live/default) tool work ===")
hm = [e for e in events if e.get("bot") == "hermes"]
print(f"hermes events: {len(hm)}")
ht = Counter(e.get("tool") for e in hm if e.get("kind") == "tool")
print("hermes tools:", dict(ht))
for e in hm:
    if e.get("kind") == "tool":
        print(f"  [{iso(e['ts'])}] {e.get('tool')} :: {str(e.get('summary',''))[:130]}")

# what did senter do beyond the topic-agent cycle
print("\n=== senter non-topic-agent activity (terminal/patch/write) ===")
for e in events:
    if e.get("bot") == "senter" and e.get("kind") == "tool":
        s = str(e.get("summary",""))
        if "reading" not in s:
            print(f"  [{iso(e['ts'])}] {e.get('tool')} :: {s[:150]}")
