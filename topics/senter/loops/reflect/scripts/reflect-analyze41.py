#!/usr/bin/env python3
"""REFLECT pass-41 analysis: scan events since pass-40 boundary."""
import json, os, glob, datetime
from collections import Counter, defaultdict

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
BOUNDARY = 1788642154.8788843  # mtime of 2026-09-05-40.md

def iso(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

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

print("WINDOW EVENTS (ts >= boundary):", len(events))
if events:
    print("WINDOW START", iso(min(e['ts'] for e in events)))
    print("WINDOW END  ", iso(max(e['ts'] for e in events)))

kinds = Counter(e.get("kind") for e in events)
print("\n=== kinds ===")
for k, c in kinds.most_common():
    print(f"  {k}: {c}")

bots = Counter(e.get("bot") for e in events)
print("\n=== bots ===")
for b, c in bots.most_common():
    print(f"  {b}: {c}")

# tool usage per bot
tool_by_bot = defaultdict(Counter)
for e in events:
    if e.get("kind") == "tool":
        tool_by_bot[e.get("bot")][e.get("tool")] += 1
print("\n=== tool usage per bot (top 15 each) ===")
for b, tools in sorted(tool_by_bot.items()):
    top = ", ".join(f"{t}:{c}" for t, c in tools.most_common(15))
    print(f"  {b}: {top}")

# phases
phases = Counter(e.get("phase") for e in events)
print("\n=== phases ===")
for p, c in phases.most_common():
    print(f"  {p}: {c}")

# ok:false / approval signals
print("\n=== ok:false / approval / tirith signals ===")
for e in events:
    ok = e.get("ok")
    if ok is False or "tirith" in str(e.get("summary", "")) or "approval" in str(e.get("kind", "")) or "approval" in str(e.get("summary", "")):
        print(f"  {iso(e['ts'])} bot={e.get('bot')} kind={e.get('kind')} tool={e.get('tool')} ok={ok} :: {str(e.get('summary'))[:200]}")

# BLOCKED / DONE / NEEDS-CHRIS markers
print("\n=== BLOCKED / DONE / NEEDS-CHRIS / NEEDS_CHRIS in summaries ===")
for e in events:
    s = str(e.get("summary", ""))
    if any(m in s for m in ["BLOCKED", "DONE", "NEEDS-CHRIS", "needs_chris", "NEEDS_CHRIS"]):
        print(f"  {iso(e['ts'])} bot={e.get('bot')} kind={e.get('kind')} :: {s[:160]}")
