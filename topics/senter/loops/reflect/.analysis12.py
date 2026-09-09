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

print("=== ALL approval events (new window) ===")
for e in new_events:
    if e.get("kind") == "approval":
        print(f"  {ts2str(e['ts'])} bot={e.get('bot')} by={e.get('by')} pattern_key={e.get('pattern_key')} resolved={e.get('resolved')} choice={e.get('choice')}")
        cmd = str(e.get("command", ""))
        print(f"      command: {cmd[:300]}")
        desc = str(e.get("description", ""))
        if desc:
            print(f"      desc: {desc[:300]}")
        print()

print("\n=== ALL message events (new window) ===")
for e in new_events:
    if e.get("kind") == "message":
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] status={e.get('status')} source={e.get('source')}: {str(e.get('summary',''))[:300]}")
        print()

print("\n=== ALL turn events (new window) ===")
for e in new_events:
    if e.get("kind") == "turn":
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] phase={e.get('phase')} status={e.get('status')} via={e.get('via')} topic={e.get('topic')} summary={str(e.get('summary',''))[:80]}")

print("\n=== skill events (new window) ===")
for e in new_events:
    if e.get("kind") == "skill":
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] action={e.get('action')} skill={e.get('skill')} topic={e.get('topic')}")

print("\n=== fleet changed events (new window) ===")
for e in new_events:
    if e.get("kind") == "fleet" and e.get("phase") == "changed":
        print(f"  {ts2str(e['ts'])}: {e.get('summary')} counts={e.get('counts')}")
