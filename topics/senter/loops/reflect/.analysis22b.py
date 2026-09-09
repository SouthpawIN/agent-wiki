#!/usr/bin/env python3
"""Check tail of events.jsonl and file mtime."""
import json, datetime, os

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

print("file mtime:", ts_to_str(os.path.getmtime(EVENTS)))
print("file size:", os.path.getsize(EVENTS))

rows = []
with open(EVENTS) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue

print("total rows:", len(rows))
print("last 15 event timestamps:")
for e in rows[-15:]:
    print(f"  {ts_to_str(e.get('ts'))} | {e.get('bot')} | {e.get('kind')} | {e.get('phase','')} | {e.get('tool','')} | {(e.get('summary') or '')[:50]}")
