#!/usr/bin/env python3
"""REFLECT pass 38 detail — deeper look at specific event families."""
import json, collections, datetime

BOUNDARY = 1788620597.0
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

def h(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")

print("== TURN events (bot, phase, status) ==")
turns = [r for r in rows if r.get("kind") == "turn"]
tc = collections.Counter((r.get("bot"), r.get("phase")) for r in turns)
for k, c in tc.most_common():
    print(f"  {k}: {c}")

print("\n== turbofit CI events (full) ==")
for r in rows:
    if "ci_activity" in str(r.get("summary","")) or "Model intelligence" in str(r.get("summary","")):
        print(json.dumps(r)[:600])

print("\n== teknium1 github events ==")
for r in rows:
    s = str(r.get("summary",""))
    if "teknium1" in s:
        print(json.dumps(r)[:500])

print("\n== github 'pr_activity' sample (first 20 distinct summaries) ==")
seen = set()
for r in rows:
    if r.get("bot") == "github":
        s = str(r.get("summary",""))
        if s not in seen:
            seen.add(s)
print(f"  total distinct github summaries: {len(seen)}")
for s in list(seen)[:40]:
    print(f"  - {s[:140]}")

print("\n== senter fleet events: distinct summaries ==")
fleet = [r for r in rows if r.get("bot") == "senter" and r.get("kind") == "fleet"]
fs = collections.Counter(str(r.get("summary",""))[:120] for r in fleet)
print(f"  total fleet events: {len(fleet)}, distinct: {len(fs)}")
for s, c in fs.most_common(10):
    print(f"  {c}x  {s}")

print("\n== senter non-fleet events ==")
snf = [r for r in rows if r.get("bot") == "senter" and r.get("kind") != "fleet"]
print(f"  count: {len(snf)}")
for r in snf[:30]:
    print(f"  {h(r['ts'])} {r.get('kind')} {r.get('phase','')} {r.get('summary','')[:120]}")

print("\n== hermes terminal events: distinct summaries ==")
ht = [r for r in rows if r.get("bot") == "hermes" and r.get("kind") == "tool" and r.get("tool") == "terminal"]
hs = collections.Counter(str(r.get("summary",""))[:100] for r in ht)
print(f"  total hermes terminal: {len(ht)}, distinct: {len(hs)}")
for s, c in hs.most_common(10):
    print(f"  {c}x  {s}")

print("\n== anser events ==")
ae = [r for r in rows if r.get("bot") == "anser"]
ak = collections.Counter((r.get("kind"), r.get("tool","")) for r in ae)
for k, c in ak.most_common():
    print(f"  {k}: {c}")
for r in ae[:10]:
    print(f"  {h(r['ts'])} {r.get('kind')} {r.get('tool','')} {r.get('summary','')[:100]}")

print("\nDONE detail")
