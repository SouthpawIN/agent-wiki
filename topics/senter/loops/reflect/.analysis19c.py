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

print("=== SENTER events (detector 4) ===")
for e in new:
    if e.get("bot") == "senter":
        print(json.dumps(e)[:600])

print("\n=== HERMES terminal commands (detector 3, sample of 163) ===")
seen = set()
for e in new:
    if e.get("bot") == "hermes" and e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = e.get("summary", "")
        if s not in seen:
            seen.add(s)
            print(s[:400])
        if len(seen) >= 60:
            break

print("\n=== PATCH targets (bot=hermes, detector 4/5) ===")
patches = collections.Counter()
for e in new:
    if e.get("kind") == "tool" and e.get("tool") == "patch":
        patches[(e.get("bot"), e.get("summary", ""))] += 1
for (b, s), c in patches.most_common(40):
    print("  %s %d  %s" % (b, c, s[:120]))

print("\n=== drive_preview / vision_analyze counts by bot (looker adoption, detector 5) ===")
dp = collections.Counter()
va = collections.Counter()
for e in new:
    if e.get("kind") == "tool":
        if e.get("tool") == "drive_preview":
            dp[e.get("bot")] += 1
        if e.get("tool") == "vision_analyze":
            va[e.get("bot")] += 1
print("drive_preview:", dict(dp))
print("vision_analyze:", dict(va))
