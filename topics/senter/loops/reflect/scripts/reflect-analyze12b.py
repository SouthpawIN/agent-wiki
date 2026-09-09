#!/usr/bin/env python3
import json, collections, datetime

CUTOFF = 1788577406
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
rows = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
new = [r for r in rows if r.get("ts", 0) > CUTOFF]

# turn events
turns = [r for r in new if r.get("kind") == "turn"]
print("--- turn events (%d) ---" % len(turns))
for r in turns:
    print("  ", round(r.get("ts",0),1), r.get("bot"), r.get("phase"), str(r.get("summary",""))[:100])

# fleet events
fleets = [r for r in new if r.get("kind") == "fleet"]
print("\n--- fleet events (%d) ---" % len(fleets))
fc = collections.Counter((r.get("bot"), str(r.get("summary",""))[:60]) for r in fleets)
for (b,s), c in fc.most_common(40):
    print("  ", c, b, s)

# teknium events
tek = [r for r in new if r.get("bot") == "teknium"]
print("\n--- teknium events (%d) ---" % len(tek))
for r in tek:
    print("  ", round(r.get("ts",0),1), r.get("kind"), r.get("phase"), str(r.get("summary",""))[:110])

# count ping/tailscale
pings = [r for r in new if r.get("tool")=="terminal" and "ping" in str(r.get("summary",""))]
print("\n--- ping/tailscale calls by hermes: %d ---" % len(pings))

# any delegate_task / skill loads
for r in new:
    s = str(r.get("summary",""))
    if "delegate" in s or "skill" in s.lower() or "vision" in s or "computer_use" in s:
        print("SPECIAL:", round(r.get("ts",0),1), r.get("bot"), r.get("kind"), s[:100])
