#!/usr/bin/env python3
"""REFLECT pass 40 analysis — scan events.jsonl for the window since pass-39 mtime."""
import json, collections

BOUNDARY = 1788635023  # pass-39 file mtime (Sep 5 14:03:43 CDT)

events = []
with open('/Users/sovthpaw/.hermes/senter-bridge/events.jsonl') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get('ts')
        if ts is None:
            continue
        if ts > BOUNDARY:
            events.append(e)

print("=== WINDOW ===")
print("boundary ts = %d" % BOUNDARY)
print("events in window (ts > boundary): %d" % len(events))
if events:
    print("window first ts = %.0f  last ts = %.0f" % (events[0].get('ts',0), events[-1].get('ts',0)))

bots = collections.Counter()
kinds = collections.Counter()
tools = collections.Counter()
phases = collections.Counter()
for e in events:
    bots[e.get('bot','?')] += 1
    kinds[e.get('kind','?')] += 1
    if e.get('kind') == 'tool':
        tools[e.get('tool','?')] += 1
    if e.get('phase'):
        phases[e.get('phase','?')] += 1

print("\n=== BOTS ===")
for b, c in bots.most_common():
    print("  %-24s %d" % (b, c))

print("\n=== KINDS ===")
for k, c in kinds.most_common():
    print("  %-24s %d" % (k, c))

print("\n=== TOOLS ===")
for t, c in tools.most_common():
    print("  %-24s %d" % (t, c))

print("\n=== PHASES ===")
for p, c in phases.most_common():
    print("  %-24s %d" % (p, c))

# Detector 3: approval/gate events
print("\n=== DETECTOR 3: approval/gate events ===")
gate = [e for e in events if 'tirith' in str(e.get('summary','')) or 'pattern_key' in str(e.get('summary','')) or 'approval' in str(e.get('summary','')).lower() or e.get('kind') in ('approval','approval_prompt','approval_request')]
print("gate/approval-summary events: %d" % len(gate))
for e in gate[:60]:
    print("  ts=%.0f bot=%s kind=%s tool=%s phase=%s ok=%s" % (e.get('ts',0), e.get('bot','?'), e.get('kind','?'), e.get('tool','?'), e.get('phase','?'), e.get('ok')))
    print("    summary: %s" % str(e.get('summary',''))[:220])

# Detector 6: BLOCKED
print("\n=== DETECTOR 6: BLOCKED markers ===")
blocked = [e for e in events if 'BLOCKED' in str(e.get('summary','')) or 'blocked' in str(e.get('summary','')).lower()]
print("blocked-marker events: %d" % len(blocked))
for e in blocked[:30]:
    print("  ts=%.0f bot=%s kind=%s tool=%s" % (e.get('ts',0), e.get('bot','?'), e.get('kind','?'), e.get('tool','?')))
    print("    summary: %s" % str(e.get('summary',''))[:200])

# Detector 1: Chris messages
print("\n=== DETECTOR 1: chris messages ===")
chris = [e for e in events if e.get('bot') == 'chris' or (e.get('bot','') and 'chris' in str(e.get('bot','')).lower())]
print("chris events: %d" % len(chris))
for e in chris[:20]:
    print("  ts=%.0f %s" % (e.get('ts',0), str(e.get('summary',''))[:160]))

# Detector 2: repeated fix (patch/write_file)
print("\n=== DETECTOR 2: file-edit events (patch/write_file) ===")
edits = [e for e in events if e.get('tool') in ('patch','write_file')]
print("edit events: %d" % len(edits))
edit_targets = collections.Counter()
for e in edits:
    edit_targets[str(e.get('summary',''))[:140]] += 1
for t, c in edit_targets.most_common(40):
    print("  %4d  %s" % (c, t))

# Detector 5: skill events
print("\n=== DETECTOR 5: skill events ===")
skills = [e for e in events if e.get('tool') in ('skill_view','skill_manage','skills_list','skill_list')]
print("skill events: %d" % len(skills))
for e in skills[:40]:
    print("  ts=%.0f bot=%s tool=%s" % (e.get('ts',0), e.get('bot','?'), e.get('tool','?')))
    print("    summary: %s" % str(e.get('summary',''))[:160])

# vision / computer_use / delegate
print("\n=== vision_analyze / computer_use / delegate_task ===")
vis = [e for e in events if e.get('tool') in ('vision_analyze','computer_use','delegate_task')]
print("vision/computer_use/delegate events: %d" % len(vis))
for e in vis:
    print("  ts=%.0f bot=%s tool=%s phase=%s ok=%s dur=%s" % (e.get('ts',0), e.get('bot','?'), e.get('tool','?'), e.get('phase','?'), e.get('ok'), e.get('duration') or e.get('dur')))

# github feed events
print("\n=== github feed events ===")
gh = [e for e in events if e.get('bot') == 'github' or e.get('kind') == 'github']
print("github events: %d" % len(gh))
ghsum = collections.Counter()
for e in gh:
    ghsum[str(e.get('summary',''))[:160]] += 1
for t, c in ghsum.most_common(30):
    print("  %4d  %s" % (c, t))

# fleet events
print("\n=== fleet events (senter) ===")
fleet = [e for e in events if e.get('kind') == 'fleet']
print("fleet events: %d" % len(fleet))
fsum = collections.Counter()
for e in fleet:
    fsum[str(e.get('summary',''))[:100]] += 1
for t, c in fsum.most_common(10):
    print("  %4d  %s" % (c, t))

# turn events by bot
print("\n=== turn events by bot ===")
turn = collections.Counter()
for e in events:
    if e.get('kind') == 'turn':
        turn[e.get('bot','?')] += 1
for b, c in turn.most_common():
    print("  %-20s %d" % (b, c))

# teknium empty-turn check (turn phase=end, status=done)
print("\n=== teknium turn detail ===")
for e in events:
    if e.get('kind') == 'turn' and e.get('bot') == 'teknium':
        print("  ts=%.0f phase=%s status=%s" % (e.get('ts',0), e.get('phase','?'), e.get('status','?')))

# hermes terminal summaries (reachability-watch)
print("\n=== hermes terminal summaries (first 30) ===")
cnt = 0
for e in events:
    if e.get('bot') == 'hermes' and e.get('tool') == 'terminal' and e.get('phase') == 'start':
        print("  ts=%.0f  %s" % (e.get('ts',0), str(e.get('summary',''))[:120]))
        cnt += 1
        if cnt >= 30:
            break

# anser activity (self)
print("\n=== anser activity ===")
for e in events:
    if e.get('bot') == 'anser':
        print("  ts=%.0f kind=%s tool=%s phase=%s ok=%s  %s" % (e.get('ts',0), e.get('kind','?'), e.get('tool','?'), e.get('phase','?'), e.get('ok'), str(e.get('summary',''))[:110]))

# execute_code events
print("\n=== execute_code events ===")
for e in events:
    if e.get('tool') == 'execute_code':
        print("  ts=%.0f bot=%s phase=%s ok=%s" % (e.get('ts',0), e.get('bot','?'), e.get('phase','?'), e.get('ok')))
        print("    summary: %s" % str(e.get('summary',''))[:160])
