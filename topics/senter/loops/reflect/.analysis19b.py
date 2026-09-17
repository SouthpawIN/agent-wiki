import json, collections

BOUNDARY = 1788455673
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except Exception:
            continue
new = [e for e in events if e.get("ts", 0) > BOUNDARY]

print("=== APPROVAL events (detector 3) ===")
for e in new:
    if e.get("kind") == "approval":
        print(json.dumps(e, indent=1)[:2000])
        print("---")

print("\n=== MESSAGE events (detector 1) ===")
for e in new:
    if e.get("kind") == "message":
        print("%s | %s | %s" % (e.get("bot"), e.get("summary"), e.get("status", "")))

print("\n=== BRIDGE events ===")
for e in new:
    if e.get("kind") == "bridge":
        print(json.dumps(e)[:400])

print("\n=== SKILL events (detector 5) ===")
for e in new:
    if e.get("kind") == "skill":
        print(json.dumps(e)[:400])
