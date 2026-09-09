import json, collections
from datetime import datetime, timezone, timedelta

CDT = timezone(timedelta(hours=-5))
# Exclude my own pass-18 run: it started ~06:01:09. Scan up to 06:00:30.
cutoff = datetime(2026, 9, 4, 4, 3, 5, tzinfo=CDT).timestamp()
end = datetime(2026, 9, 4, 6, 0, 30, tzinfo=CDT).timestamp()

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        t = e.get("ts", 0)
        if t >= cutoff and t < end:
            events.append(e)

def ts(e):
    return datetime.fromtimestamp(e["ts"], CDT).strftime("%H:%M:%S")

print("=== TURN events ===")
for e in events:
    if e.get("kind") == "turn":
        print(f"{ts(e)} | {e.get('bot')} | {e.get('phase','')} | {str(e.get('summary'))[:160]}")
        if 'topic' in e and e.get('topic'):
            print(f"     topic={e.get('topic')}")

print("\n=== MESSAGE events (bot + summary) ===")
for e in events:
    if e.get("kind") == "message":
        print(f"{ts(e)} | {e.get('bot')} | status={e.get('status','')} | {str(e.get('summary'))[:200]}")

print("\n=== terminal commands (bot=hermes/anser/senter) ===")
for e in events:
    if e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        s = str(e.get("summary",""))
        print(f"{ts(e)} | {e.get('bot')} | {s[:220]}")
