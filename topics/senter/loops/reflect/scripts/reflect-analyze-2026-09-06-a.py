#!/usr/bin/env python3
"""REFLECT pass 2026-09-06 (n=1) — analyze events.jsonl NEW since pass-43 boundary."""
import json, sys, collections

BOUNDARY = 1788663956  # pass-43 file mtime (Sep 5 22:05:56 CDT)
PATH = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

events = []
with open(PATH) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("ts")
        if ts is None or ts <= BOUNDARY:
            continue
        events.append(e)

print(f"NEW events since boundary {BOUNDARY}: {len(events)}")
if not events:
    sys.exit(0)

# 1. by bot
by_bot = collections.Counter()
for e in events:
    by_bot[e.get("bot")] += 1
print("\n== by bot ==")
for b, c in by_bot.most_common():
    print(f"  {b}: {c}")

# 2. by kind
by_kind = collections.Counter()
for e in events:
    by_kind[e.get("kind")] += 1
print("\n== by kind ==")
for k, c in by_kind.most_common():
    print(f"  {k}: {c}")

# 3. approval events
print("\n== approval events ==")
for e in events:
    if e.get("kind") == "approval":
        print(f"  bot={e.get('bot')} tool={e.get('tool')} summary={e.get('summary','')[:120]!r}")

# 4. message events (non-feed)
print("\n== message events (non-feed) ==")
for e in events:
    if e.get("kind") == "message" and not e.get("feed"):
        print(f"  bot={e.get('bot')} status={e.get('status')} summary={e.get('summary','')[:160]!r}")

# 5. turn end / done lines
print("\n== turn end (status) ==")
for e in events:
    if e.get("kind") == "turn" and e.get("phase") == "end":
        print(f"  bot={e.get('bot')} status={e.get('status')} summary={e.get('summary','')[:100]!r}")
