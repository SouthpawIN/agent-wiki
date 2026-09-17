#!/usr/bin/env python3
import json, collections, datetime

CUTOFF = 1788577406
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
rows = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
new = [r for r in rows if r.get("ts", 0) > CUTOFF]

print("=== turn events by bot (phase/status) ===")
turns = collections.Counter((r.get("bot"), r.get("phase"), r.get("status")) for r in new if r.get("kind") == "turn")
for k, v in turns.most_common(40):
    print("  ", v, k)

print("\n=== terminal commands by bot (summary) ===")
terms = [r for r in new if r.get("tool") == "terminal" and r.get("summary")]
tby = collections.Counter((r.get("bot"), r.get("summary")) for r in terms)
for k, v in tby.most_common(50):
    print("  ", v, k[0], "|", k[1][:130])

print("\n=== execute_code by bot ===")
ex = collections.Counter((r.get("bot"), r.get("phase")) for r in new if r.get("tool") == "execute_code")
for k, v in ex.most_common():
    print("  ", v, k)

print("\n=== fleet events by bot/summary ===")
fl = collections.Counter((r.get("bot"), r.get("summary")) for r in new if r.get("kind") == "fleet")
for k, v in fl.most_common(20):
    print("  ", v, k[0], "|", (k[1] or "")[:100])

print("\n=== bridge events ===")
for r in new:
    if r.get("kind") == "bridge":
        print("  ", json.dumps(r, default=str)[:200])

print("\n=== non-github message events (senter/anser/teknium/hermes done/blocked) ===")
for r in new:
    if r.get("kind") == "message" and r.get("bot") != "github":
        print("  ", r.get("bot"), "|", r.get("status"), "|", (r.get("summary") or "")[:180])
