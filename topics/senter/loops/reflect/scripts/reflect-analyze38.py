#!/usr/bin/env python3
"""REFLECT pass 38 analysis — scan events.jsonl for events NEW since pass-37 file mtime."""
import json, sys, collections

BOUNDARY = 1788620597.0  # pass-37 file mtime (Sep 5 10:03:17 CDT)

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

rows = []
with open(EVENTS) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("ts", 0)
        if isinstance(ts, (int, float)) and ts > BOUNDARY:
            rows.append(e)

print(f"TOTAL events in window (ts > {BOUNDARY}): {len(rows)}")

# time range
ts_min = min((r["ts"] for r in rows), default=0)
ts_max = max((r["ts"] for r in rows), default=0)
import datetime
def h(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S") if ts else "n/a"
print(f"window: {h(ts_min)} -> {h(ts_max)}")

# bot counts
bots = collections.Counter(r.get("bot") for r in rows)
print("\n== events by bot ==")
for b, c in bots.most_common():
    print(f"  {b}: {c}")

# kind counts
kinds = collections.Counter(r.get("kind") for r in rows)
print("\n== events by kind ==")
for k, c in kinds.most_common():
    print(f"  {k}: {c}")

# tool counts
tools = collections.Counter()
for r in rows:
    if r.get("kind") == "tool":
        tools[r.get("tool")] += 1
print("\n== tool calls ==")
for t, c in tools.most_common():
    print(f"  {t}: {c}")

# chris messages
chris = [r for r in rows if r.get("bot") == "chris"]
print(f"\n== chris messages: {len(chris)} ==")
for r in chris:
    print(f"  {h(r['ts'])} {r.get('kind')} {r.get('summary','')[:120]}")

# approvals / gate
approvals = [r for r in rows if r.get("kind") == "approval" or "approval" in str(r.get("phase","")) or "approve" in str(r.get("summary","")).lower()]
print(f"\n== approval-related events: {len(approvals)} ==")
for r in approvals[:60]:
    print(f"  {h(r['ts'])} {r.get('bot')} {r.get('kind')} {r.get('phase')} {r.get('summary','')[:120]}")

# gate trips: look for pattern_key / tirith
gate = [r for r in rows if "tirith" in str(r.get("summary","")) or "pattern_key" in str(r.get("summary","")) or "analysis_incomplete" in str(r.get("summary","")) or "pipe_to_interpreter" in str(r.get("summary","")) or "interpreter" in str(r.get("summary",""))]
print(f"\n== gate/tirith events: {len(gate)} ==")
for r in gate[:60]:
    print(f"  {h(r['ts'])} {r.get('bot')} {r.get('kind')} {r.get('summary','')[:140]}")

# reachability pings
pings = [r for r in rows if "ping -c 2" in str(r.get("summary","")) or "tailscale status" in str(r.get("summary",""))]
print(f"\n== reachability ping events: {len(pings)} ==")

# fleet changed
fleet = [r for r in rows if "fleet changed" in str(r.get("summary","")) or "fleet/changed" in str(r.get("summary",""))]
print(f"== fleet/changed events: {len(fleet)} ==")

# teknium turns
tek_turns = [r for r in rows if r.get("bot") == "teknium" and r.get("kind") == "turn"]
print(f"== teknium turn events: {len(tek_turns)} ==")
tek_start = [r for r in tek_turns if r.get("phase") == "start"]
tek_end = [r for r in tek_turns if r.get("phase") == "end"]
print(f"   turn start: {len(tek_start)}, turn end: {len(tek_end)}")

# BLOCKED markers
blocked = [r for r in rows if "BLOCKED" in str(r.get("summary",""))]
print(f"== BLOCKED markers: {len(blocked)} ==")
for r in blocked[:30]:
    print(f"  {h(r['ts'])} {r.get('bot')} {r.get('summary','')[:120]}")

# vision / computer_use / delegate
print(f"\n== special tools ==")
print(f"  vision_analyze: {tools.get('vision_analyze',0)}")
print(f"  computer_use: {tools.get('computer_use',0)}")
print(f"  delegate_task: {tools.get('delegate_task',0)}")
print(f"  skill_view: {tools.get('skill_view',0)}")
print(f"  skill_manage: {tools.get('skill_manage',0)}")

# github events
gh = [r for r in rows if r.get("bot") == "github"]
print(f"\n== github events: {len(gh)} ==")
# summarize github kinds
ghk = collections.Counter()
for r in gh:
    s = str(r.get("summary",""))
    if "teknium1" in s:
        ghk["teknium1"] += 1
    elif "opened" in s or "PR #" in s:
        ghk["pr_activity"] += 1
    else:
        ghk["other"] += 1
for k, c in ghk.most_common():
    print(f"  {k}: {c}")

# turbofit CI
ci = [r for r in rows if "ci_activity" in str(r.get("summary","")) or "Model intelligence" in str(r.get("summary","")) or "CheckSuite" in str(r.get("summary",""))]
print(f"\n== turbofit CI events: {len(ci)} ==")
for r in ci[:20]:
    print(f"  {h(r['ts'])} {r.get('summary','')[:140]}")

# terminal events with 'python3 -c' / heredoc / pipe (rule-14 family) - quick check
inline = [r for r in rows if r.get("kind") == "tool" and r.get("tool") == "terminal" and ("python3 -c" in str(r.get("summary","")) or "python -c" in str(r.get("summary","")) or "<<'EOF'" in str(r.get("summary","")) or "<<EOF" in str(r.get("summary","")))]
print(f"\n== inline-exec/heredoc terminal events: {len(inline)} ==")
for r in inline[:20]:
    print(f"  {h(r['ts'])} {r.get('bot')} {r.get('summary','')[:140]}")

print("\nDONE analysis")
