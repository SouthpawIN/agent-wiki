#!/usr/bin/env python3
"""REFLECT pass 2026-09-06 (n=1) — klerik terminal command samples + senter queue/session mtimes."""
import json, collections

BOUNDARY = 1788663956
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
        if e.get("ts") and e["ts"] > BOUNDARY:
            events.append(e)

# klerik terminal summaries (start phase) — full text
print("== klerik terminal commands (this window) ==")
seen = set()
for e in events:
    if e.get("kind") == "tool" and e.get("bot") == "klerik" and e.get("tool") == "terminal" and e.get("phase") == "start":
        s = e.get("summary","")
        if s not in seen:
            seen.add(s)
            print(f"  {s!r}")

print(f"\n== klerik distinct terminal commands: {len(seen)} ==")

# paladin + looker events this window
print("\n== paladin / looker events ==")
for e in events:
    if e.get("bot") in ("paladin","looker") and e.get("kind") in ("message","tool","turn"):
        print(f"  {e.get('bot')} {e.get('kind')}/{e.get('phase')} {e.get('summary','')[:120]!r}")
