import json, collections

WL = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
WINDOW_START = 1788450607

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

print("== skill events ==")
sk = [e for e in evs if e.get("kind") == "skill"]
for e in sk[:60]:
    print("  ", round(e.get("ts")), e.get("bot"), e.get("phase") or e.get("tool") or "", (e.get("summary") or "")[:150])

print("\n== skill_manage + skill_view (tool) details ==")
for e in evs:
    if e.get("kind") == "tool" and e.get("tool") in ("skill_manage", "skill_view") and e.get("phase") == "start":
        print("  ", round(e.get("ts")), e.get("bot"), e.get("tool"), (e.get("summary") or "")[:160])

print("\n== hermes skill_manage write payloads ==")
for e in evs:
    if e.get("kind") == "tool" and e.get("tool") == "skill_manage" and e.get("phase") == "start" and e.get("bot") == "hermes":
        print("  ", round(e.get("ts")), (e.get("summary") or "")[:300])

print("\n== drive_preview / desktop_preview (detector 4) ==")
dp = [e for e in evs if e.get("kind") == "tool" and e.get("tool") in ("drive_preview", "desktop_preview") and e.get("phase") == "start"]
print("count", len(dp))
for e in dp[:40]:
    print("  ", round(e.get("ts")), e.get("bot"), e.get("tool"), (e.get("summary") or "")[:130])

print("\n== computer_use details ==")
cu = [e for e in evs if e.get("kind") == "tool" and e.get("tool") == "computer_use" and e.get("phase") == "start"]
print("count", len(cu))
for e in cu[:30]:
    print("  ", round(e.get("ts")), e.get("bot"), (e.get("summary") or "")[:140])

print("\n== approval details (pattern_key + command) ==")
for e in evs:
    if e.get("kind") == "approval":
        print("  ", round(e.get("ts")), e.get("bot"), e.get("phase"), "| pk=", e.get("pattern_key"), "|", (e.get("command") or e.get("summary") or "")[:200])
