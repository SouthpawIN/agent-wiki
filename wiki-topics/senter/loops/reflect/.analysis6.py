import json, datetime, collections, os

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except Exception:
                pass

def ts2str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

rf2 = "/Users/sovthpaw/Documents/Projects/Projects/topics/senter/loops/reflect/2026-09-02-2.md"
boundary = os.path.getmtime(rf2)
new_events = [e for e in events if e.get("ts", 0) > boundary]

# ---- Detector 3: approval pattern_keys ----
print("=== APPROVAL pattern_keys in NEW window ===")
appr = [e for e in new_events if e.get("kind") == "approval"]
print("total approvals:", len(appr))
pk = collections.Counter(e.get("pattern_key") for e in appr)
for k, c in pk.most_common():
    print(f"  {k}: {c}")
# approval by bot
print("\napprovals by bot:")
for b, c in collections.Counter(e.get("bot") for e in appr).most_common():
    print(f"  {b}: {c}")

# command family within approvals - look at inline exec
print("\n=== approval commands (dedup, top 25) ===")
cmd = collections.Counter()
for e in appr:
    c = e.get("command","")
    # categorize
    cat = c[:80]
    cmd[cat] += 1
for c, n in cmd.most_common(25):
    print(f"  [{n}] {c!r}")
