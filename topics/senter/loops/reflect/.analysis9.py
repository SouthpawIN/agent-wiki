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

# Actual BLOCKED status events / message text starting with BLOCKED
print("=== message events with status blocked, or text BLOCKED ===")
for e in new_events:
    if e.get("kind") == "message":
        s = e.get("summary","")
        st = e.get("status","")
        if st == "blocked" or s.upper().startswith("BLOCKED"):
            print(f"  {ts2str(e['ts'])} [{e.get('bot')}] status={st} {s[:110]}")

# all message status values in window
print("\n=== message status value tally (new window) ===")
st = collections.Counter(e.get("status") for e in new_events if e.get("kind")=="message")
print(dict(st))

# vision_analyze + computer_use usage by bot (detector 5 adoption check)
print("\n=== vision_analyze + computer_use by bot (new window) ===")
va = collections.Counter()
cu = collections.Counter()
for e in new_events:
    if e.get("kind") == "tool":
        t = e.get("tool")
        if t == "vision_analyze":
            va[e.get("bot")] += 1
        if t == "computer_use":
            cu[e.get("bot")] += 1
print("vision_analyze:", dict(va))
print("computer_use:", dict(cu))
