#!/usr/bin/env python3
"""REFLECT pass-25 analysis part 2: hermes bot, fleet/turn kinds, skill event, teknium pattern detail."""
import json, datetime, collections, re

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
def s(ts): return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

T0 = datetime.datetime(2026, 9, 4, 14, 3, 36).timestamp()
T1 = datetime.datetime(2026, 9, 4, 15, 59, 0).timestamp()

rows = []
with open(EVENTS) as f:
    for line in f:
        line = line.strip()
        if not line: continue
        try: rows.append(json.loads(line))
        except Exception: continue
win = [r for r in rows if T0 < r.get("ts", 0) <= T1]

print("=== fleet kind detail (sample) ===")
fleet = [r for r in win if r.get("kind")=="fleet"]
for r in fleet[:20]:
    print(f"  {s(r['ts'])} | {r.get('bot','?')} | {(r.get('summary') or r.get('phase') or r.get('topic') or '')[:120]}")

print("\n=== turn kind detail (sample) ===")
turns = [r for r in win if r.get("kind")=="turn"]
for r in turns[:20]:
    print(f"  {s(r['ts'])} | {r.get('bot','?')} | phase={r.get('phase','')} | {(r.get('summary') or r.get('model') or '')[:120]}")

print("\n=== skill events ===")
for r in win:
    if r.get("kind")=="skill":
        print(f"  {s(r['ts'])} | {r.get('bot','?')} | {json.dumps(r, ensure_ascii=False)[:300]}")

print("\n=== hermes bot activity (non-turn/tool) ===")
her = [r for r in win if r.get("bot")=="hermes"]
hk = collections.Counter(r.get("kind") for r in her)
print("  kinds:", dict(hk))
# what tool events / terminal did hermes do?
for r in her:
    if r.get("kind")=="tool":
        print(f"  {s(r['ts'])} | tool={r.get('tool')} | {(r.get('summary') or '')[:140]}")
    elif r.get("kind")=="message":
        print(f"  {s(r['ts'])} | MSG | {(r.get('summary') or '')[:140]}")

print("\n=== hermes terminal commands ===")
for r in her:
    if r.get("tool")=="terminal" and r.get("phase")=="start":
        print(f"  {s(r['ts'])} | {(r.get('summary') or '')[:160]}")

print("\n=== teknium: count distinct selectors/regions edited (detector 2) ===")
# group teknium inline-exec by target region keyword
tkn = [r for r in win if r.get("bot")=="teknium" and r.get("kind")=="tool" and r.get("tool")=="terminal" and r.get("phase")=="start"]
sel = collections.Counter()
for r in tkn:
    m = str(r.get("summary") or "")
    for kw in ["#mVol", "#mVolMute", "#mVolTrack", "#mVolFill", "#mVolZone", "--volShift", "--volDot", "--volGap", "#hpEq", "--eqCX", "placeHud", "TEMP-VOLDBG", "TEMP-ZONEDBG", "TEMP-HITDBG", "m.addEventListener", "vol.addEventListener"]:
        if kw in m:
            sel[kw] += 1
print("  selector hit counts:")
for k, c in sel.most_common():
    print(f"    {k:22} {c}")

print("\n=== teknium drive_preview events (reload/poll?) ===")
for r in win:
    if r.get("bot")=="teknium" and r.get("tool")=="drive_preview":
        print(f"  {s(r['ts'])} | {(r.get('summary') or '')[:120]}")

print("\n=== github turbofit CI failures ===")
for r in win:
    m = str(r.get("summary") or "")
    if "turbofit" in m.lower() and "fail" in m.lower():
        print(f"  {s(r['ts'])} | {m[:120]}")
