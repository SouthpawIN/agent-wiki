#!/usr/bin/env python3
"""REFLECT pass 11 — measure paired tool latencies (start->end) + inspect raw event fields."""
import json, time, collections

CUTOFF = 1788469740
EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
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
new = [e for e in rows if e.get("ts", 0) >= CUTOFF]

# inspect one vision_analyze event's keys
for e in new:
    if e.get("tool") == "vision_analyze":
        print("VISION EVENT KEYS:", sorted(e.keys()))
        print(json.dumps(e)[:600])
        break

# inspect a terminal end event keys
for e in new:
    if e.get("tool") == "terminal" and e.get("phase") == "end":
        print("\nTERMINAL END KEYS:", sorted(e.keys()))
        print(json.dumps(e)[:400])
        break

# measure paired durations per tool: match start/end by bot+tool via adjacent ordering
print("\n=== paired tool latency (start->end) by bot/tool ===")
lat = collections.defaultdict(list)
for i, e in enumerate(new):
    if e.get("phase") == "start" and e.get("kind") == "tool":
        # find next 'end' with same bot+tool
        for j in range(i+1, min(i+8, len(new))):
            e2 = new[j]
            if e2.get("phase") == "end" and e2.get("bot") == e.get("bot") and e2.get("tool") == e.get("tool"):
                d = e2.get("ts",0) - e.get("ts",0)
                lat[(e.get("bot"), e.get("tool"))].append(d)
                break
for (b, t), ds in sorted(lat.items()):
    if t in ("vision_analyze", "read_file", "drive_preview", "desktop_preview", "terminal", "process_manage"):
        ds2 = [d for d in ds if d >= 0]
        if ds2:
            avg = sum(ds2)/len(ds2)
            print(f"  {b} | {t}: n={len(ds2)} avg={avg:.1f}s max={max(ds2):.1f}s")
        else:
            print(f"  {b} | {t}: n={len(ds)} (no clean pairs)")
