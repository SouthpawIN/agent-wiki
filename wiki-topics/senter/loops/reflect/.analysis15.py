import json, collections, datetime

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

boundary = 1788397733.0
new_events = [e for e in events if e.get("ts", 0) > boundary]

print("=== non-ok tool events (failures) in window ===")
for e in new_events:
    if e.get("kind") == "tool" and e.get("phase") == "end" and e.get("ok") is False:
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] tool={e.get('tool')} summary={str(e.get('summary',''))[:160]}")

# match start events to failures to see the command
print("\n=== terminal start events with non-empty summary (to see what failed) ===")
for e in new_events:
    if e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start" and e.get("summary"):
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}]: {str(e.get('summary',''))[:160]}")

print("\n=== patch start events with summary ===")
for e in new_events:
    if e.get("kind") == "tool" and e.get("tool") == "patch" and e.get("phase") == "start" and e.get("summary"):
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}]: {str(e.get('summary',''))[:160]}")

# also: any turn with status != done/None
print("\n=== turn events with unusual status ===")
for e in new_events:
    if e.get("kind") == "turn" and e.get("status") not in (None, "done"):
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] phase={e.get('phase')} status={e.get('status')} via={e.get('via')} summary={str(e.get('summary',''))[:100]}")
