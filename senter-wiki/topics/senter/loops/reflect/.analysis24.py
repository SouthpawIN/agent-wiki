#!/usr/bin/env python3
"""Check anser spawn events around midnight + cron job files state."""
import json, datetime, os

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

# midnight boundary
T0 = int(datetime.datetime(2026, 9, 4, 4, 58, 0, tzinfo=datetime.timezone.utc).timestamp())
T1 = int(datetime.datetime(2026, 9, 4, 5, 5, 0, tzinfo=datetime.timezone.utc).timestamp())

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

print("=== events 23:58 -> 00:05 (spawn detection) ===")
for e in rows:
    t = e.get("ts", 0)
    if T0 <= t <= T1:
        print(f"  {ts_to_str(t)} | {e.get('bot')} | {e.get('kind')} | {e.get('phase','')} | {e.get('tool','')} | {(e.get('summary') or e.get('argv') or '')[:90]}")

# cron job files
print("\n=== cron jobs (anser + senter) ===")
for p in ["/Users/sovthpaw/.hermes/profiles/anser/cron/jobs.json",
          "/Users/sovthpaw/.hermes/profiles/senter/cron/jobs.json"]:
    print(f"\n--- {p} (mtime {ts_to_str(os.path.getmtime(p))}) ---")
    try:
        with open(p) as f:
            data = json.load(f)
        jobs = data if isinstance(data, list) else data.get("jobs", data)
        if isinstance(jobs, dict):
            jobs = list(jobs.values())
        for j in jobs:
            print(f"  id={j.get('id','')[:12]} name={j.get('name','')!r} sched={j.get('schedule', j.get('cron',''))} enabled={j.get('enabled', True)} last_status={j.get('last_status','')}")
    except Exception as ex:
        print("  ERR", ex)
