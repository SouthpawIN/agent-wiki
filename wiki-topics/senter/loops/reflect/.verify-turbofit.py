#!/usr/bin/env python3
"""Verify turbofit CI failure events: raw ts + local + UTC."""
import json, datetime
EV = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
def loc(ts): return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")
def utc(ts): return datetime.datetime.utcfromtimestamp(ts).strftime("%m-%d %H:%M:%S")
hits = []
with open(EV) as f:
    for i, line in enumerate(f, 1):
        if "turbofit" in line and ("workflow run failed" in line or "CheckSuite" in line):
            try:
                r = json.loads(line)
            except Exception:
                continue
            hits.append((i, r.get("ts", 0), r.get("summary", "")[:90]))
print(f"total turbofit CheckSuite lines: {len(hits)}")
for i, ts, summ in hits:
    print(f"  line {i} | raw_ts={ts} | local={loc(ts)} | utc={utc(ts)} | {summ}")
