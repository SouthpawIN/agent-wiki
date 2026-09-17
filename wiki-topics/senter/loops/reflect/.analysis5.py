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

# boundary = mtime of reflect-2 file
rf2 = "/Users/sovthpaw/Documents/Projects/Projects/topics/senter/loops/reflect/2026-09-02-2.md"
boundary = os.path.getmtime(rf2)
print("reflect-2 mtime:", ts2str(boundary), "ts =", boundary)

new_events = [e for e in events if e.get("ts", 0) > boundary]
print("events NEW since pass 2:", len(new_events))
if new_events:
    print("new window:", ts2str(new_events[0]["ts"]), "->", ts2str(new_events[-1]["ts"]))

# bots in new window
print("\n--- bots in NEW window ---")
for b, c in collections.Counter(e.get("bot") for e in new_events).most_common():
    print(f"  {b}: {c}")

# kinds in new window
print("\n--- kinds in NEW window ---")
for k, c in collections.Counter(e.get("kind") for e in new_events).most_common():
    print(f"  {k}: {c}")

# looker events - all time
print("\n--- looker bot events (all time) ---")
for e in events:
    if e.get("bot") == "looker":
        print(f"  {ts2str(e['ts'])} {e.get('kind')} {e.get('tool','')} {e.get('phase','')} {str(e.get('summary',''))[:60]}")

# fleet changed events
print("\n--- fleet changed events ---")
for e in events:
    if e.get("kind") == "fleet":
        print(f"  {ts2str(e['ts'])} {e.get('phase')} {str(e.get('summary',''))[:80]}")
