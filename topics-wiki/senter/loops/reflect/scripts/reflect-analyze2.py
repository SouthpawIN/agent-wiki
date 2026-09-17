import json, collections
from datetime import datetime, timezone, timedelta

CDT = timezone(timedelta(hours=-5))
cutoff = datetime(2026, 9, 4, 4, 3, 5, tzinfo=CDT).timestamp()

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("ts", 0) >= cutoff:
            events.append(e)

print("=== APPROVAL events ===")
for e in events:
    if e.get("kind") == "approval":
        print(json.dumps(e, indent=None)[:600])
        print("---")

print("\n=== BRIDGE events ===")
for e in events:
    if e.get("kind") == "bridge":
        print(json.dumps(e, indent=None)[:600])
        print("---")

print("\n=== MESSAGE events (non-github) ===")
for e in events:
    if e.get("kind") == "message" and e.get("bot") != "github":
        print(json.dumps(e, indent=None)[:500])
        print("---")
