#!/usr/bin/env python3
"""REFLECT pass 39 analysis part 2 — detail on hermes/senter/anser activity + terminal summaries."""
import json, collections

BOUNDARY = 1788627835
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
        if e.get('ts', 0) > BOUNDARY:
            events.append(e)

# terminal events by bot
print("=== terminal events by bot ===")
term = collections.Counter()
for e in events:
    if e.get('tool') == 'terminal':
        term[e.get('bot','?')] += 1
for b, c in term.most_common():
    print("  %-20s %d" % (b, c))

# hermes terminal summaries (sample)
print("\n=== hermes terminal summaries (first 40) ===")
cnt = 0
for e in events:
    if e.get('bot') == 'hermes' and e.get('tool') == 'terminal' and e.get('phase') == 'start':
        print("  ts=%.0f  %s" % (e.get('ts',0), str(e.get('summary',''))[:140]))
        cnt += 1
        if cnt >= 40:
            break

# execute_code events
print("\n=== execute_code events ===")
for e in events:
    if e.get('tool') == 'execute_code':
        print("  ts=%.0f bot=%s phase=%s ok=%s" % (e.get('ts',0), e.get('bot','?'), e.get('phase','?'), e.get('ok')))
        print("    summary: %s" % str(e.get('summary',''))[:160])

# turn events by bot
print("\n=== turn events by bot ===")
turn = collections.Counter()
for e in events:
    if e.get('kind') == 'turn':
        turn[e.get('bot','?')] += 1
for b, c in turn.most_common():
    print("  %-20s %d" % (b, c))

# turn details
print("\n=== turn detail (phase/status) ===")
for e in events:
    if e.get('kind') == 'turn':
        print("  ts=%.0f bot=%s phase=%s status=%s" % (e.get('ts',0), e.get('bot','?'), e.get('phase','?'), e.get('status','?')))

# fleet events detail
print("\n=== fleet events (senter) sample ===")
cnt = 0
for e in events:
    if e.get('kind') == 'fleet':
        print("  ts=%.0f bot=%s phase=%s  %s" % (e.get('ts',0), e.get('bot','?'), e.get('phase','?'), str(e.get('summary',''))[:100]))
        cnt += 1
        if cnt >= 6:
            break

# message events by bot
print("\n=== message events by bot ===")
msg = collections.Counter()
for e in events:
    if e.get('kind') == 'message':
        msg[e.get('bot','?')] += 1
for b, c in msg.most_common():
    print("  %-20s %d" % (b, c))

# hermes non-terminal tools
print("\n=== hermes non-terminal tool activity ===")
for e in events:
    if e.get('bot') == 'hermes' and e.get('kind') == 'tool' and e.get('tool') != 'terminal':
        print("  ts=%.0f tool=%s phase=%s  %s" % (e.get('ts',0), e.get('tool','?'), e.get('phase','?'), str(e.get('summary',''))[:120]))

# senter non-fleet activity
print("\n=== senter non-fleet activity ===")
for e in events:
    if e.get('bot') == 'senter' and e.get('kind') != 'fleet':
        print("  ts=%.0f kind=%s tool=%s phase=%s  %s" % (e.get('ts',0), e.get('kind','?'), e.get('tool','?'), e.get('phase','?'), str(e.get('summary',''))[:140]))

# anser activity (self)
print("\n=== anser activity (this pass + any prior) ===")
for e in events:
    if e.get('bot') == 'anser':
        print("  ts=%.0f kind=%s tool=%s phase=%s ok=%s  %s" % (e.get('ts',0), e.get('kind','?'), e.get('tool','?'), e.get('phase','?'), e.get('ok'), str(e.get('summary',''))[:110]))
