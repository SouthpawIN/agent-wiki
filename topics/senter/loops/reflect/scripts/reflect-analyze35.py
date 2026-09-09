#!/usr/bin/env python3
import json, collections, datetime, os

CUTOFF = 1788599070  # pass-34 file mtime = 2026-09-05 04:04:30 CDT
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
rows = []
with open(path, "r", encoding="utf-8", errors="replace") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
new = [r for r in rows if r.get("ts", 0) > CUTOFF]

def dt(ts):
    return datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc).strftime("%H:%M:%S")

print("=== TOTAL new events since cutoff (04:04:30) ===", len(new))
print("window first ts:", dt(min(r.get('ts',0) for r in new)) if new else "n/a")
print("window last  ts:", dt(max(r.get('ts',0) for r in new)) if new else "n/a")

print("\n=== by bot ===")
for b, c in collections.Counter(r.get("bot") for r in new).most_common():
    print(f"  {c:6d}  {b}")

print("\n=== by kind ===")
for k, c in collections.Counter(r.get("kind") for r in new).most_common():
    print(f"  {c:6d}  {k}")

print("\n=== turn events by bot (phase/status) ===")
turns = collections.Counter((r.get("bot"), r.get("phase"), r.get("status")) for r in new if r.get("kind") == "turn")
for k, v in turns.most_common(40):
    print("  ", v, k)

print("\n=== approvals (gate trips) ===")
for r in new:
    if r.get("kind") in ("approval", "gate"):
        print(f"  [{dt(r.get('ts',0))}] {r.get('bot')} choice={r.get('choice')} pk={r.get('pattern_key')}")
        print(f"      cmd: {(r.get('command') or r.get('summary') or '')[:200]}")

print("\n=== tool calls by tool (phase=start) ===")
tools = collections.Counter(r.get("tool") for r in new if r.get("kind") == "tool" and r.get("phase") == "start")
for t, c in tools.most_common():
    print(f"  {c:6d}  {t}")

print("\n=== tool FAILURES (phase=end, ok=false) ===")
fails = collections.Counter(r.get("tool") for r in new if r.get("kind") == "tool" and r.get("phase") == "end" and r.get("ok") is False)
for t, c in fails.most_common():
    print(f"  {c:6d}  {t}")

print("\n=== terminal commands by bot (summary) ===")
terms = [r for r in new if r.get("tool") == "terminal" and r.get("summary")]
tby = collections.Counter((r.get("bot"), r.get("summary")) for r in terms)
for k, v in tby.most_common(80):
    print("  ", v, k[0], "|", k[1][:160])

print("\n=== execute_code by bot/phase ===")
for k, v in collections.Counter((r.get("bot"), r.get("phase")) for r in new if r.get("tool") == "execute_code").most_common():
    print("  ", v, k)

print("\n=== skill loads ===")
sk = collections.Counter((r.get("bot"), (r.get("summary") or r.get("skill") or r.get("name"))) for r in new if r.get("tool") in ("skill_view", "skill_manage", "skills_list"))
for k, v in sk.most_common(40):
    print("  ", v, k[0], "|", str(k[1])[:120])

print("\n=== fleet events ===")
fl = collections.Counter((r.get("bot"), r.get("summary")) for r in new if r.get("kind") == "fleet")
for k, v in fl.most_common(20):
    print("  ", v, k[0], "|", (k[1] or "")[:100])

print("\n=== bridge events ===")
for r in new:
    if r.get("kind") == "bridge":
        print("  ", dt(r.get("ts",0)), json.dumps(r, default=str)[:240])

print("\n=== message events (non-github) ===")
for r in new:
    if r.get("kind") == "message" and r.get("bot") != "github":
        print("  ", dt(r.get("ts",0)), r.get("bot"), "|", r.get("status"), "|", (r.get("summary") or "")[:180])

print("\n=== message events (github) ===")
for r in new:
    if r.get("kind") == "message" and r.get("bot") == "github":
        print("  ", dt(r.get("ts",0)), "|", (r.get("summary") or "")[:200])

print("\n=== BLOCKED markers ===")
for r in new:
    s = (r.get("summary") or "") + (r.get("command") or "")
    if "blocked" in s.lower():
        print("  ", dt(r.get("ts",0)), r.get("bot"), "|", s[:160])

print("\n=== full event kinds seen ===")
for k in sorted(set(r.get("kind") for r in new)):
    print("  ", k)
