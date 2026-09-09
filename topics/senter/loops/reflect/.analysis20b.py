import json, collections, os, datetime, sys, re

path = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
cutoff = 1788464047
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

def fmt(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

new = [e for e in events if e.get("ts", 0) > cutoff]

# bot=hermes patch targets
print("=== bot=hermes patch targets (start) ===")
hp = collections.Counter()
for e in new:
    if e.get("bot") == "hermes" and e.get("tool") == "patch" and e.get("phase") == "start":
        hp[str(e.get("summary"))[:130]] += 1
for s, c in hp.most_common():
    print(f"  x{c}: {s}")

# bot=hermes skill events
print("\n=== bot=hermes skill events ===")
for e in new:
    if e.get("bot") == "hermes" and e.get("tool") in ("skill_manage", "skill_view"):
        print(f"  {fmt(e.get('ts',0))} {e.get('tool')} action={e.get('action')} {str(e.get('summary'))[:110]}")

# turn events (what each bot's turn was about)
print("\n=== turn events (NEW) ===")
for e in new:
    if e.get("kind") == "turn":
        print(f"  {fmt(e.get('ts',0))} bot={e.get('bot')} {str(e.get('summary'))[:140]}")

# bridge events
print("\n=== bridge events (NEW) ===")
for e in new:
    if e.get("kind") == "bridge":
        print(f"  {fmt(e.get('ts',0))} bot={e.get('bot')} {json.dumps(e, default=str)[:200]}")

# hermes terminal commands (start) - full
print("\n=== bot=hermes terminal commands (start) ===")
for e in new:
    if e.get("bot") == "hermes" and e.get("tool") == "terminal" and e.get("phase") == "start":
        print(f"  {fmt(e.get('ts',0))} {str(e.get('summary'))[:140]}")
