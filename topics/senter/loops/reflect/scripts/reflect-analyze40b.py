#!/usr/bin/env python3
"""REFLECT pass 40 — precise counts for the findings table."""
import json, collections

BOUNDARY = 1788635023
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

# hermes terminal (reachability-watch) count + distinct commands
hermes_term = [e for e in events if e.get('bot')=='hermes' and e.get('tool')=='terminal']
print("hermes terminal events: %d" % len(hermes_term))
print("hermes terminal phase=start: %d" % len([e for e in hermes_term if e.get('phase')=='start']))

# anser terminal events (this pass)
anser_term = [e for e in events if e.get('bot')=='anser' and e.get('tool')=='terminal']
print("anser terminal events: %d" % len(anser_term))

# senter events breakdown
senter_events = [e for e in events if e.get('bot')=='senter']
sk = collections.Counter(e.get('kind') for e in senter_events)
print("senter kinds: %s" % dict(sk))
senter_nonfleet = [e for e in senter_events if e.get('kind') != 'fleet']
print("senter non-fleet events: %d" % len(senter_nonfleet))
for e in senter_nonfleet:
    print("  ts=%.0f kind=%s tool=%s phase=%s  %s" % (e.get('ts',0), e.get('kind','?'), e.get('tool','?'), e.get('phase','?'), str(e.get('summary',''))[:120]))

# fleet summary detail
fleet = [e for e in events if e.get('kind')=='fleet']
print("\nfleet event count: %d" % len(fleet))
# sample one full summary
if fleet:
    print("sample fleet summary: %s" % str(fleet[0].get('summary',''))[:200])

# teknium (bot) events
teknium = [e for e in events if e.get('bot')=='teknium']
print("\nteknium bot events: %d" % len(teknium))

# github: teknium1 activity specifically
teknium1 = [e for e in events if e.get('bot')=='github' and 'teknium1' in str(e.get('summary',''))]
print("\nteknium1 github events: %d" % len(teknium1))
for e in teknium1:
    print("  ts=%.0f  %s" % (e.get('ts',0), str(e.get('summary',''))[:160]))

# turbofit CI
turbofit = [e for e in events if 'turbofit' in str(e.get('summary','')) or 'CheckSuite' in str(e.get('summary',''))]
print("\nturbofit/CheckSuite events: %d" % len(turbofit))
for e in turbofit:
    print("  ts=%.0f  %s" % (e.get('ts',0), str(e.get('summary',''))[:180]))

# hermes turn detail (reachability cron id)
print("\nhermes turn detail:")
for e in events:
    if e.get('bot')=='hermes' and e.get('kind')=='turn':
        print("  ts=%.0f phase=%s status=%s  %s" % (e.get('ts',0), e.get('phase','?'), e.get('status','?'), str(e.get('summary',''))[:80]))
