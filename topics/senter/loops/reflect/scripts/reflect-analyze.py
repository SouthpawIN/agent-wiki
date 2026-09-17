import json, sys, collections
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

print("TOTAL new events:", len(events))
if events:
    print("window start ts:", events[0]["ts"], "->", datetime.fromtimestamp(events[0]["ts"], CDT).isoformat())
    print("window end   ts:", events[-1]["ts"], "->", datetime.fromtimestamp(events[-1]["ts"], CDT).isoformat())

# bot distribution
botc = collections.Counter(e.get("bot") for e in events)
print("\nBOT distribution:", dict(botc))

# kind distribution
kindc = collections.Counter(e.get("kind") for e in events)
print("KIND distribution:", dict(kindc))

# tool distribution
toolc = collections.Counter(e.get("tool") for e in events if e.get("kind") == "tool")
print("\nTOOL distribution:", dict(toolc))
