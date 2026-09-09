import json

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
cutoff = 1788389805

events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except Exception:
            pass

new = [e for e in events if isinstance(e.get("ts"), (int,float)) and e["ts"] > cutoff]

print("=== ALL NEW approval REQUESTS (full command) ===")
for e in new:
    if e.get("kind") == "approval" and e.get("phase") == "request":
        ts = e.get("ts")
        hhmmss = ""
        print(f"\n[{e.get('bot')}] ts={ts}")
        print("  command:", (e.get("command") or "")[:600])
        if e.get("description"):
            print("  description:", e.get("description")[:200])
