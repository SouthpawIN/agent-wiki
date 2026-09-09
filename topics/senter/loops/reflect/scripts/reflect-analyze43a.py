#!/usr/bin/env python3
"""REFLECT pass-43 survey: window since pass-42 mtime (1788657030)."""
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

print(f"WINDOW events: {len(events)}")
if events:
    print(f"window start: {iso(events[0]['ts'])}  end: {iso(events[-1]['ts'])}")

# schema survey
print("\n=== kinds ===")
print(dict(Counter(e.get('kind') for e in events)))
print("\n=== bots ===")
print(dict(Counter(e.get('bot') for e in events)))
print("\n=== tools (kind=tool) ===")
tools = Counter(e.get('tool') for e in events if e.get('kind') == 'tool')
print(dict(tools.most_common(30)))

# turn events per bot
print("\n=== turns per bot ===")
print(dict(Counter(e.get('bot') for e in events if e.get('kind') == 'turn')))
