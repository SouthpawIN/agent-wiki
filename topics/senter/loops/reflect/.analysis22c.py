#!/usr/bin/env python3
"""REFLECT pass 15 — correct cutoff (tz-aware) + locate boundary precisely."""
import json, datetime, os

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

# Correct: cutoff = 2026-09-03 22:02:44 CDT = 03:02:44 UTC on Sep 4
CUTOFF = int(datetime.datetime(2026, 9, 4, 3, 2, 44, tzinfo=datetime.timezone.utc).timestamp())
print("cutoff ts:", CUTOFF, "=", ts_to_str(CUTOFF))

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
print("new events:", len(new))
if new:
    print("first:", ts_to_str(new[0]["ts"]), "last:", ts_to_str(new[-1]["ts"]))
    print("span min:", round((new[-1]["ts"] - new[0]["ts"])/60.0, 2))

# Also show events in the boundary zone (22:00 -> 22:20) to see exactly where pass14 ended
print("\n=== events 21:58 -> 22:15 (boundary check) ===")
for e in rows:
    t = e.get("ts", 0)
    if t >= int(datetime.datetime(2026,9,3,21,58,0,tzinfo=datetime.timezone(datetime.timedelta(hours=-5))).timestamp()) and t <= int(datetime.datetime(2026,9,3,22,15,0,tzinfo=datetime.timezone(datetime.timedelta(hours=-5))).timestamp()):
        print(f"  {ts_to_str(t)} | {e.get('bot')} | {e.get('kind')} | {e.get('phase','')} | {e.get('tool','')} | {(e.get('summary') or e.get('command') or '')[:60]}")
