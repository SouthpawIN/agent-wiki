#!/usr/bin/env python3
"""REFLECT pass-42 — second-pass targeted detail extraction."""
import json, os, collections, datetime

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
BOUNDARY = 1788649670.249  # pass-41 file mtime

rows = []
with open(EVENTS) as fh:
    for line in fh:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("ts", 0) > BOUNDARY:
            rows.append(e)

# 1. patch / write_file bot attribution
print("== patch tool calls by bot ==")
pc = collections.Counter()
for r in rows:
    if r.get("kind") == "tool" and r.get("tool") == "patch" and r.get("phase") == "start":
        pc[r.get("bot")] += 1
for b, c in pc.most_common():
    print(f"  {b}: {c}")

print("== write_file tool calls by bot ==")
wc_ = collections.Counter()
for r in rows:
    if r.get("kind") == "tool" and r.get("tool") == "write_file" and r.get("phase") == "start":
        wc_[r.get("bot")] += 1
for b, c in wc_.most_common():
    print(f"  {b}: {c}")

print("== execute_code by bot ==")
ec = collections.Counter()
for r in rows:
    if r.get("kind") == "tool" and r.get("tool") == "execute_code" and r.get("phase") == "start":
        ec[r.get("bot")] += 1
for b, c in ec.most_common():
    print(f"  {b}: {c}")

print("== terminal by bot ==")
tc = collections.Counter()
for r in rows:
    if r.get("kind") == "tool" and r.get("tool") == "terminal" and r.get("phase") == "start":
        tc[r.get("bot")] += 1
for b, c in tc.most_common():
    print(f"  {b}: {c}")

# 2. github events
print("\n== github events (summaries, dedup) ==")
gh = [r for r in rows if r.get("bot") == "github"]
print(f"total github: {len(gh)}")
seen = set()
for r in gh:
    s = (r.get("summary") or "").strip()
    key = s[:80]
    if key not in seen:
        seen.add(key)
        print(f"  [{r.get('kind','?')}] {s[:150]}")
        if len(seen) >= 40:
            print("  ... trunc")
            break

# 3. 'you' and 'fleet-orchestrator' bot detail
print("\n== 'you' bot events ==")
for r in rows:
    if r.get("bot") == "you":
        print(f"  [{r.get('kind')}/{r.get('phase')}] tool={r.get('tool','')} ok={r.get('ok','')} summary={ (r.get('summary') or '')[:120] }")
print("== 'fleet-orchestrator' bot events ==")
for r in rows:
    if r.get("bot") == "fleet-orchestrator":
        print(f"  [{r.get('kind')}/{r.get('phase')}] tool={r.get('tool','')} ok={r.get('ok','')} summary={ (r.get('summary') or '')[:120] }")

# 4. klerik-queue-drain cron FAILED full text
print("\n== klerik-queue-drain / cron FAILED summaries ==")
for r in rows:
    s = (r.get("summary") or "")
    if "klerik-queue-drain" in s or "cron FAILED" in s or "cron FAIL" in s:
        print(f"  [{r.get('bot')}/{r.get('kind')}] {s[:300]}")
        print("  ---")

# 5. senter hand-polling (sleep / /tmp/anser-reflect / kill -0)
print("\n== senter hand-poll / hand-spawn evidence ==")
poll = 0
for r in rows:
    if r.get("bot") == "senter" and r.get("kind") == "tool" and r.get("tool") == "terminal":
        s = (r.get("summary") or "")
        if any(k in s for k in ("/tmp/anser-reflect", "kill -0", "sleep 2", "sleep 3", "sleep 4", "sleep 5", "anser-reflect")):
            poll += 1
            if poll <= 15:
                print(f"  {s[:150]}")
print(f"(hand-poll terminal events: {poll})")

# 6. approvals by bot (who is tripping the gate)
print("\n== approval requests by bot ==")
ap = collections.Counter()
for r in rows:
    if r.get("kind") == "approval" and r.get("phase") == "request":
        ap[r.get("bot")] += 1
for b, c in ap.most_common():
    print(f"  {b}: {c}")

# 7. senter narrative events AFTER first 120 (tail portion)
print("\n== senter narrative (LATE window, index > 120 of narrative) ==")
narr = []
for r in rows:
    s = (r.get("summary") or "").strip()
    if not s:
        continue
    if r.get("bot") == "senter" and any(k in s for k in ("FILED", "PROPOSAL", "SKILL", "WORKER", "AGENT", "WIKI", "NEEDS", "BLOCKED", "DONE", "chris:", "distilled", "proposed", "spawn", "approved", "created")):
        narr.append(r)
print(f"total senter narrative: {len(narr)}")
for r in narr[-60:]:
    print(f"  [{r.get('kind')}/{r.get('phase')}] {r.get('summary','')[:170]}")

# 8. chris asks (message kind) + any 'chris:' in summaries near end
print("\n== chris-directed summaries (any bot, contains 'chris:') ==")
for r in rows:
    s = (r.get("summary") or "")
    if "chris:" in s.lower() or ("· chris:" in s):
        print(f"  [{r.get('bot')}] {s[:200]}")
