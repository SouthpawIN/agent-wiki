#!/usr/bin/env python3
"""REFLECT pass 15 — full window scan since pass 14 (2026-09-03-14.md, scan end 22:02:44 CDT)."""
import json, collections, datetime

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

# cutoff = 2026-09-03 22:02:44 CDT = 2026-09-04 03:02:44 UTC
CUTOFF = int(datetime.datetime(2026, 9, 4, 3, 2, 44).timestamp())

rows = []
with open(EVENTS) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue

new = [e for e in rows if e.get("ts", 0) > CUTOFF]
print("=== WINDOW ===")
if new:
    print("new events:", len(new))
    print("first:", ts_to_str(new[0]["ts"]), "last:", ts_to_str(new[-1]["ts"]))
    print("span min:", (new[-1]["ts"] - new[0]["ts"]) / 60.0)
else:
    print("NO NEW EVENTS after cutoff", ts_to_str(CUTOFF))

# bot activity
bot_kind = collections.Counter()
bot_tool = collections.Counter()
for e in new:
    bot_kind[(e.get("bot"), e.get("kind"))] += 1
    if e.get("kind") == "tool":
        bot_tool[(e.get("bot"), e.get("tool"))] += 1

print("\n=== bot x kind ===")
for k, v in sorted(bot_kind.items()):
    print(f"  {k[0]} | {k[1]}: {v}")

print("\n=== bot x tool ===")
for k, v in sorted(bot_tool.items()):
    print(f"  {k[0]} | {k[1]}: {v}")

# approvals
print("\n=== approvals ===")
appr = collections.Counter()
for e in new:
    if e.get("kind") == "approval":
        appr[(e.get("phase"), e.get("pattern_key"), e.get("bot"))] += 1
for k, v in sorted(appr.items()):
    print(f"  {k[0]} | {k[1]} | {k[2]}: {v}")

# approval commands (unique)
print("\n=== approval commands (unique, first 120 chars) ===")
seen = set()
for e in new:
    if e.get("kind") == "approval" and e.get("phase") == "request":
        c = e.get("command", "")[:120]
        if c not in seen:
            seen.add(c)
            print(f"  [{e.get('bot')}] ({e.get('pattern_key')}) {c}")

# messages
print("\n=== message events ===")
for e in new:
    if e.get("kind") == "message":
        print(f"  [{e.get('bot')}] {e.get('summary','')[:120]}")

# turns (bot + phase)
print("\n=== turn start/end by bot ===")
turn = collections.Counter()
for e in new:
    if e.get("kind") == "turn":
        turn[(e.get("bot"), e.get("phase"))] += 1
for k, v in sorted(turn.items()):
    print(f"  {k[0]} | {k[1]}: {v}")

# skill events
print("\n=== skill events ===")
sk = collections.Counter()
for e in new:
    if e.get("kind") == "skill":
        sk[(e.get("bot"), e.get("skill"), e.get("action"))] += 1
for k, v in sorted(sk.items()):
    print(f"  {k[0]} | {k[1]} | {k[2]}: {v}")

# BLOCKED / NEEDS-CHRIS / DONE markers in messages or summaries
print("\n=== status markers ===")
for e in new:
    s = (e.get("summary") or "") + (e.get("text") or "")
    if any(m in s for m in ("BLOCKED", "NEEDS-CHRIS", "needs_chris", "DONE", "done")):
        print(f"  [{e.get('bot')}] {e.get('kind')} {e.get('status','')}: {s[:140]}")
