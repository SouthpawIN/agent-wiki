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

print("=== needs_chris messages (new window) ===")
for e in new_events:
    if e.get("kind") == "message" and e.get("status") == "needs_chris":
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}]: {e.get('summary','')[:300]}")
        print()

# daemon-spawn sentinel messages count
print("=== sentinel daemon-spawn messages (full text) ===")
cnt = collections.Counter()
for e in new_events:
    if e.get("kind") == "message" and "daemon didn't" in str(e.get("summary","")):
        cnt[e.get("bot")] += 1
print("count of 'daemon didn't' messages:", sum(cnt.values()))
for e in new_events:
    if e.get("kind") == "message" and "daemon didn't" in str(e.get("summary","")):
        print(f"  {ts2str(e['ts'])}: {e.get('summary','')}")
