#!/usr/bin/env python3
"""REFLECT pass-42 — resolve the you/APPROVED/REJECTED vs PROPOSAL ordering."""
import json, os, datetime

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
BOUNDARY = 1788649670.249

rows = []
with open(EVENTS) as fh:
    for line in fh:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("ts", 0) > BOUNDARY:
            rows.append(e)

def ts(t):
    return datetime.datetime.fromtimestamp(t).strftime('%H:%M:%S')

print("== you (Chris decision) events, ordered ==")
for r in rows:
    if r.get("bot") == "you":
        print(f"  {ts(r['ts'])}  {r.get('summary','')[:90]}")

print("\n== PROPOSAL / approved / created / rejected (senter) ordered ==")
for r in rows:
    s = (r.get("summary") or "")
    if r.get("bot") == "senter" and any(k in s for k in ("PROPOSAL", "approved →", "REJECTED", "approved → creating", "profile created", "spawn", "proposed")):
        print(f"  {ts(r['ts'])}  {s[:150]}")

print("\n== all 'needs_chris' / 'NEEDS-CHRIS' summaries ==")
for r in rows:
    s = (r.get("summary") or "")
    if "needs_chris" in s.lower():
        print(f"  {ts(r['ts'])} [{r.get('bot')}] {s[:150]}")

print("\n== looker events (1) ==")
for r in rows:
    if r.get("bot") == "looker":
        print(f"  {ts(r['ts'])} [{r.get('kind')}/{r.get('phase')}] {r.get('summary','')[:150]}")

print("\n== paladin turn/summary sample ==")
pal = [r for r in rows if r.get("bot") == "paladin" and (r.get("summary") or "").strip()]
for r in pal[:20]:
    print(f"  {ts(r['ts'])} [{r.get('kind')}] {r.get('summary','')[:150]}")

print("\n== teknium turn/summary sample ==")
tek = [r for r in rows if r.get("bot") == "teknium" and (r.get("summary") or "").strip()]
for r in tek[:20]:
    print(f"  {ts(r['ts'])} [{r.get('kind')}] {r.get('summary','')[:150]}")
