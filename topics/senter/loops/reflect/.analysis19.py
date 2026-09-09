import json, collections, sys

BOUNDARY = 1788455673  # pass-8 file mtime = 2026-09-03 12:14:33 CDT

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
        events.append(e)

new = [e for e in events if e.get("ts", 0) > BOUNDARY]
print("TOTAL events:", len(events))
print("NEW events (ts > %d):" % BOUNDARY, len(new))
if new:
    t0 = min(e["ts"] for e in new)
    t1 = max(e["ts"] for e in new)
    print("NEW window: %s -> %s (%.1f min)" % (t0, t1, (t1 - t0) / 60.0))

# kind distribution
kinds = collections.Counter()
for e in new:
    kinds[e.get("kind", "?")] += 1
print("\nKIND counts (new):")
for k, c in kinds.most_common():
    print("  %-14s %d" % (k, c))

# bot distribution
bots = collections.Counter()
for e in new:
    bots[e.get("bot", "?")] += 1
print("\nBOT counts (new):")
for b, c in bots.most_common():
    print("  %-14s %d" % (b, c))

# tool distribution
tools = collections.Counter()
for e in new:
    if e.get("kind") == "tool":
        tools[e.get("tool", "?")] += 1
print("\nTOOL counts (new):")
for t, c in tools.most_common():
    print("  %-18s %d" % (t, c))
