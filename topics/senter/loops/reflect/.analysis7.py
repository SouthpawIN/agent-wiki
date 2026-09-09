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

# ---- Chris messages in window ----
print("=== CHRIS messages in NEW window ===")
for e in new_events:
    if e.get("bot") == "chris" and e.get("kind") == "message":
        print(f"  {ts2str(e['ts'])}: {e.get('summary','')}")

# ---- skill events in window ----
print("\n=== SKILL events in NEW window (by bot+skill) ===")
sk = collections.Counter()
for e in new_events:
    if e.get("kind") == "skill":
        sk[(e.get("bot"), e.get("skill"), e.get("action"))] += 1
for k, c in sk.most_common():
    print(f"  {k}: {c}")

# ---- messages with BLOCKED / DONE / status ----
print("\n=== messages mentioning BLOCKED/DONE/stall/busy in NEW window ===")
for e in new_events:
    if e.get("kind") == "message":
        s = e.get("summary","")
        if any(w in s.lower() for w in ["blocked","done","stall","busy","reload","stale","sentinel"]):
            print(f"  {ts2str(e['ts'])} [{e.get('bot')}]: {s[:120]}")
