#!/usr/bin/env python3
"""REFLECT pass-25 analysis. Window: NEW since pass-24 scan end (14:03:36 CDT)."""
import json, datetime, collections, re

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

def s(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

# pass 24 scanned 12:07:48 -> 14:03:36 CDT. NEW = after 14:03:36.
T0 = datetime.datetime(2026, 9, 4, 14, 3, 36).timestamp()
# end: now ~16:01, but exclude this run's own tool chatter -> cut at 15:59:00
T1 = datetime.datetime(2026, 9, 4, 15, 59, 0).timestamp()

rows = []
with open(EVENTS) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue

win = [r for r in rows if T0 < r.get("ts", 0) <= T1]
print(f"=== WINDOW {s(T0)} -> {s(T1)} CDT : {len(win)} events ===")

by_bot = collections.Counter(r.get("bot") for r in win)
print("\n--- events by bot ---")
for b, c in by_bot.most_common():
    print(f"  {b:12} {c}")

by_kind = collections.Counter(r.get("kind") for r in win)
print("\n--- events by kind ---")
for k, c in by_kind.most_common():
    print(f"  {k:12} {c}")

print("\n--- MESSAGE events (full) ---")
for r in win:
    if r.get("kind") == "message":
        extra = ""
        if r.get("status"):
            extra = f" [status={r['status']}]"
        if r.get("ask"):
            extra += " [ask]"
        if r.get("url"):
            extra += f" [url={r['url'][:60]}]"
        print(f"  {s(r['ts'])} | {r.get('bot','?')} | {(r.get('summary') or '')[:300]}{extra}")

print("\n--- APPROVAL events ---")
for r in win:
    if r.get("kind") == "approval":
        print(f"  {s(r['ts'])} | {r.get('bot','?')} | phase={r.get('phase','')} | id={r.get('id','')[:12]} | {(r.get('summary') or r.get('detail') or r.get('command') or '')[:220]}")

print("\n--- BRIDGE events ---")
for r in win:
    if r.get("kind") == "bridge":
        print(f"  {s(r['ts'])} | {r.get('bot','?')} | phase={r.get('phase','')} | {(r.get('summary') or '')[:160]}")

# detector 3: inline-exec / heredoc family in tool summaries + terminal commands
PAT = re.compile(r"python3?\s+(-c\b|-\s*<<|<<\s*['\"]?EOF)|cat\s+>>|<<\s*['\"]?EOF|grep\s.*\||\|\s*(head|tail|python)|for\s+.*\sin\s+\$\(seq|while\s+read")
print("\n--- DETECTOR-3 candidate tool events (inline-exec/heredoc/pipe) ---")
d3 = [r for r in win if r.get("kind") == "tool" and PAT.search(str(r.get("summary") or "") + str(r.get("command") or ""))]
print(f"  count={len(d3)}")
for r in d3:
    print(f"  {s(r['ts'])} | {r.get('bot','?')} | {r.get('tool','')} | {(r.get('summary') or r.get('command') or '')[:200]}")

print("\n--- TOOL events by tool (top) ---")
toolc = collections.Counter(r.get("tool") for r in win if r.get("kind") == "tool")
for t, c in toolc.most_common(30):
    print(f"  {t:20} {c}")

print("\n--- TERMINAL events by bot (hand-steps) ---")
term = [r for r in win if r.get("tool") == "terminal"]
print(f"  total terminal={len(term)}")
tb = collections.Counter(r.get("bot") for r in term)
for b, c in tb.most_common():
    print(f"  {b:12} {c}")

print("\n--- terminal commands by senter (detector 4 hand-poll candidates) ---")
for r in term:
    if r.get("bot") == "senter" and r.get("phase") == "start":
        print(f"  {s(r['ts'])} | {(r.get('summary') or '')[:160]}")
