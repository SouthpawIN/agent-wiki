#!/usr/bin/env python3
"""REFLECT pass 39 analysis — scan events.jsonl for the window since pass-38 mtime."""
import json, sys, collections

BOUNDARY = 1788627835  # pass-38 file mtime (Sep 5 12:03 CDT)

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
print("events in window (ts > %d): %d" % (BOUNDARY, len(events)))

# per-bot counts
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

# Detector 3: approval events / gate trips
print("\n=== DETECTOR 3: approval/gate events ===")
approvals = [e for e in events if e.get('kind') in ('approval', 'approval_prompt', 'approval_request') or 'approval' in str(e.get('kind','')).lower() or e.get('tool') == 'approval']
# also look for summary containing 'tirith' or 'pattern_key' or 'approval'
gate = [e for e in events if 'tirith' in str(e.get('summary','')) or 'pattern_key' in str(e.get('summary','')) or 'approval' in str(e.get('summary','')).lower()]
print("kind-approval events: %d" % len(approvals))
print("gate/approval-summary events: %d" % len(gate))
for e in gate[:40]:
    print("  ts=%.0f bot=%s kind=%s tool=%s phase=%s" % (e.get('ts',0), e.get('bot','?'), e.get('kind','?'), e.get('tool','?'), e.get('phase','?')))
    s = str(e.get('summary',''))[:200]
    print("    summary: %s" % s)

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

# Detector 2: repeated fix (patch/write_file on same files)
print("\n=== DETECTOR 2: file-edit events (patch/write_file) ===")
edits = [e for e in events if e.get('tool') in ('patch','write_file')]
print("edit events: %d" % len(edits))
edit_targets = collections.Counter()
for e in edits:
    edit_targets[e.get('summary','')[:120]] += 1
for t, c in edit_targets.most_common(30):
    print("  %4d  %s" % (c, t))

# Detector 5: skill loads
print("\n=== DETECTOR 5: skill events ===")
skills = [e for e in events if e.get('tool') in ('skill_view','skill_manage','skills_list','skill_list')]
print("skill events: %d" % len(skills))
for e in skills[:40]:
    print("  ts=%.0f bot=%s tool=%s" % (e.get('ts',0), e.get('bot','?'), e.get('tool','?')))
    print("    summary: %s" % str(e.get('summary',''))[:160])

# vision / computer_use / delegate latency (detector 7 bonus)
print("\n=== DETECTOR 7 (bonus): vision_analyze / computer_use latency ===")
def dur(e):
    return e.get('duration') or e.get('latency') or e.get('dur')
vis = [e for e in events if e.get('tool') in ('vision_analyze','computer_use','delegate_task') and e.get('phase')=='end']
for e in vis:
    print("  ts=%.0f bot=%s tool=%s ok=%s dur=%s" % (e.get('ts',0), e.get('bot','?'), e.get('tool','?'), e.get('ok'), e.get('duration') or e.get('dur')))

# github feed events (external noise)
print("\n=== github feed events ===")
gh = [e for e in events if e.get('bot') == 'github' or e.get('kind') == 'github']
print("github events: %d" % len(gh))
ghsum = collections.Counter()
for e in gh:
    ghsum[str(e.get('summary',''))[:140]] += 1
for t, c in ghsum.most_common(25):
    print("  %4d  %s" % (c, t))
