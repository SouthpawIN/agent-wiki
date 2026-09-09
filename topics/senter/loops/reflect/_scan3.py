#!/usr/bin/env python3
import json, collections, datetime
CUTOFF = 1788563448
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
fleet = []
with open(path, "r", encoding="utf-8", errors="replace") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("ts")
        if ts and ts > CUTOFF and e.get("kind") == "fleet":
            fleet.append(e)
print("fleet/changed count:", len(fleet))
# show fields present
if fleet:
    print("sample keys:", sorted(fleet[0].keys()))
    print("sample:", json.dumps(fleet[0], default=str)[:400])
    # payload variety
    payloads = collections.Counter()
    for e in fleet:
        payloads[json.dumps({k: e.get(k) for k in e if k not in ("ts","bot","kind")}, default=str, sort_keys=True)] += 1
    print("distinct payloads:", len(payloads))
    for p, c in payloads.most_common(10):
        print(f"{c:4d}  {p[:200]}")
