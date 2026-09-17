#!/usr/bin/env python3
"""REFLECT pass-41 verification: github feed, turbofit CI, teknium1 PRs, klerik, reflect twin, approvals detail."""
import json, os, datetime, re
from collections import Counter

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
BOUNDARY = 1788642154.8788843

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

# github events of interest
print("=== github events: teknium1 + turbofit CI + fleet-owned ===")
for e in events:
    if e.get("bot") == "github":
        s = str(e.get("summary", ""))
        if any(x in s for x in ["teknium1", "turbofit", "ci_activity", "CheckSuite", "Model intelligence", "SouthpawIN"]):
            print(f"  [{iso(e['ts'])}] {s[:200]}")

# any reflect twin / hand-spawn / poll
print("\n=== reflect twin / hand-spawn / poll signals ===")
for e in events:
    s = str(e.get("summary", ""))
    if any(x in s for x in ["REFLECT pass", "Run one REFLECT", "anser-reflect", "c377932f3933", "hermes chat -q", "HERMES_HOME", "profiles/anser"]):
        print(f"  [{iso(e['ts'])}] {e.get('bot')} {e.get('tool')} :: {s[:160]}")

# klerik activity
print("\n=== klerik events (positive: is the queue being consumed?) ===")
klerik = [e for e in events if e.get("bot") == "klerik"]
print(f"klerik event count: {len(klerik)}")
kt = Counter(e.get("tool") for e in klerik if e.get("kind") == "tool")
print("klerik tools:", dict(kt))
for e in klerik[:15]:
    print(f"  [{iso(e['ts'])}] {e.get('kind')} {e.get('tool')} :: {str(e.get('summary',''))[:120]}")

# approval events: what tool/command preceded them (look for gate pattern)
print("\n=== approval events + preceding terminal commands (gate trippers) ===")
for i, e in enumerate(events):
    if e.get("kind") == "approval":
        # look back a few events for the terminal command
        ctx = []
        for j in range(max(0, i-3), i):
            pe = events[j]
            if pe.get("kind") == "tool" and pe.get("tool") == "terminal":
                ctx.append(str(pe.get("summary",""))[:120])
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} preceding_terminals={ctx}")

# turn events per bot
print("\n=== turn events per bot ===")
turn = Counter(e.get("bot") for e in events if e.get("kind") == "turn")
print(dict(turn))
