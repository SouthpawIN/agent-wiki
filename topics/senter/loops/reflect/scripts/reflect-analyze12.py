#!/usr/bin/env python3
import json, collections, datetime, sys

CUTOFF = 1788577406  # 2026-09-04 22:03:26 CDT = pass-31 window end

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
print("new rows (post cutoff):", len(new))

if new:
    mn = min(r['ts'] for r in new)
    mx = max(r['ts'] for r in new)
    print("new window:", datetime.datetime.fromtimestamp(mn), "->", datetime.datetime.fromtimestamp(mx))

kinds = collections.Counter(r.get("kind") for r in new)
print("\nKIND:", dict(kinds))

bots = collections.Counter(r.get("bot") for r in new)
print("\nBOT:", dict(bots))

tools = collections.Counter(r.get("tool") for r in new if r.get("tool"))
print("\nTOOL:", dict(tools))

topics = collections.Counter(r.get("topic") for r in new)
print("\nTOPIC:", dict(topics))

appr = [r for r in new if r.get("kind") == "approval"]
print("\napproval events:", len(appr))
for a in appr:
    print("  ", round(a.get("ts",0),1), a.get("bot"), a.get("phase"), a.get("status"), str(a.get("summary",""))[:90])

# kind:message / user / done / blocked lines
for k in ["message", "done", "blocked", "bridge", "post"]:
    sub = [r for r in new if r.get("kind") == k]
    if sub:
        print(f"\n--- {k} ({len(sub)}) ---")
        for r in sub[:50]:
            print("  ", round(r.get("ts",0),1), r.get("bot"), r.get("phase"), str(r.get("summary",""))[:100])

# terminal commands (tool=terminal or command-ish)
term = [r for r in new if r.get("tool") == "terminal"]
print("\n--- terminal calls ---")
for r in term:
    print("  ", round(r.get("ts",0),1), r.get("bot"), r.get("phase"), r.get("ok"), str(r.get("summary",""))[:110])
