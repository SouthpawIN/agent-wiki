#!/usr/bin/env python3
import json, collections, datetime, sys, os

CUTOFF = 1788577406  # pass-31 window end = 2026-09-04 22:03:26 CDT

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
print("total rows:", len(rows))
print("new rows (post pass-31 cutoff):", len(new))
if new:
    mn = min(r['ts'] for r in new); mx = max(r['ts'] for r in new)
    print("new window:", datetime.datetime.fromtimestamp(mn), "->", datetime.datetime.fromtimestamp(mx))

kinds = collections.Counter(r.get("kind") for r in new)
print("\nKIND:", dict(kinds))
bots = collections.Counter(r.get("bot") for r in new)
print("\nBOT:", dict(bots))
tools = collections.Counter(r.get("tool") for r in new if r.get("tool"))
print("\nTOOL:", dict(tools))
topics = collections.Counter(r.get("topic") for r in new)
print("\nTOPIC:", dict(topics))

# Detector 1: chris messages / asks
chris = [r for r in new if r.get("bot") == "chris" or (r.get("kind") == "message" and r.get("bot") == "chris")]
print("\n[CHRIS messages]:", len(chris))
for c in chris:
    print("  ", c.get("summary") or c.get("text") or str(c)[:200])

# Detector 2: repeated file writes/patches on same path by same bot
writes = collections.Counter()
for r in new:
    if r.get("kind") == "tool" and r.get("tool") in ("write_file", "patch") and r.get("summary"):
        writes[(r.get("bot"), r.get("tool"), r.get("summary"))] += 1
print("\n[file write/patch counts (bot, tool, path)]:")
for k, v in writes.most_common(30):
    print("  ", v, k)

# Detector 3: approval events
appr = [r for r in new if r.get("kind") == "approval"]
print("\n[approval events]:", len(appr))
for a in appr:
    print("  ", json.dumps(a, default=str)[:300])

# Detector 6: blocked / done / needs_chris status
for k in ("blocked", "done", "needs_chris", "status"):
    pass
st = collections.Counter(r.get("status") for r in new if r.get("status"))
print("\n[status counts]:", dict(st))
blk = [r for r in new if r.get("status") == "blocked" or r.get("kind") == "blocked"]
print("[blocked events]:", len(blk))
for b in blk[:20]:
    print("  ", json.dumps(b, default=str)[:300])

# skill loads
skills = collections.Counter(r.get("summary") for r in new if r.get("kind") == "skill" or (r.get("tool") == "skill_view"))
sk_events = [r for r in new if r.get("kind") == "skill" or r.get("tool") in ("skill_view", "skill_manage", "skill_create")]
print("\n[skill events]:", len(sk_events))
skc = collections.Counter((r.get("bot"), r.get("tool"), r.get("summary")) for r in sk_events)
for k, v in skc.most_common(20):
    print("  ", v, k)

# messages summary
msgs = [r for r in new if r.get("kind") == "message"]
print("\n[message events]:", len(msgs))
for m in msgs[:40]:
    print("  ", m.get("bot"), "|", m.get("status"), "|", (m.get("summary") or m.get("text") or "")[:160])
