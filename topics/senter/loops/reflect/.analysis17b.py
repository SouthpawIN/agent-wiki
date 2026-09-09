import json, collections

WL = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
WINDOW_START = 1788419575

evs = []
with open(WL) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("ts")
        if ts is None or ts < WINDOW_START:
            continue
        evs.append(e)

print("== PATTERN_KEY events (detector 3) ==")
for e in evs:
    if e.get("pattern_key"):
        print(f"  {round(e['ts'])} bot={e.get('bot')} key={e.get('pattern_key')} kind={e.get('kind')} phase={e.get('phase')}")
        s = e.get("summary") or e.get("command") or ""
        print(f"      summary: {s[:180]}")

print("\n== senter terminal/process/tool_describe commands ==")
for e in evs:
    if e.get("bot") == "senter" and e.get("kind") == "tool":
        print(f"  {round(e['ts'])} {e.get('tool')} {e.get('phase')} :: {(e.get('summary') or e.get('command') or '')[:160]}")

print("\n== approval events detail ==")
for e in evs:
    if e.get("kind") == "approval":
        print(f"  {round(e['ts'])} bot={e.get('bot')} phase={e.get('phase')} id={e.get('id')} choice={e.get('choice')} key={e.get('pattern_key')}")
        s = e.get("command") or e.get("summary") or e.get("description") or ""
        print(f"      cmd: {s[:200]}")

print("\n== hermes(default) patch summaries (specialist edits) ==")
for e in evs:
    if e.get("bot") == "hermes" and e.get("tool") == "patch":
        print(f"  {round(e['ts'])} patch :: {(e.get('summary') or '')[:160]}")
