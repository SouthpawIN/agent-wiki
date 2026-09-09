#!/usr/bin/env python3
import json, collections, datetime

CUTOFF = 1788563448
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
evs = []
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
        if ts and ts > CUTOFF:
            evs.append(e)

def dt(ts):
    return datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc).strftime("%H:%M:%S")

print("=== TEKNIUM events (chronological) ===")
for e in evs:
    if e.get("bot") == "teknium":
        kind = e.get("kind"); phase = e.get("phase"); tool = e.get("tool")
        summ = (e.get("summary") or "")[:90]
        print(f"[{dt(e.get('ts',0))}Z] {kind}/{phase}/{tool} | {summ}")

print("\n=== SENTER events: tool summaries (unique, phase=start) ===")
seen = set()
for e in evs:
    if e.get("bot") == "senter" and e.get("kind") == "tool" and e.get("phase") == "start":
        summ = (e.get("summary") or "")[:110]
        key = (e.get("tool"), summ)
        if key not in seen:
            seen.add(key)
            print(f"[{dt(e.get('ts',0))}Z] {e.get('tool')}: {summ}")

print("\n=== SENTER tool counts ===")
c = collections.Counter()
for e in evs:
    if e.get("bot") == "senter" and e.get("kind") == "tool" and e.get("phase") == "start":
        c[e.get("tool")] += 1
for t, n in c.most_common():
    print(f"{n:4d}  {t}")

print("\n=== HERMES bot events (sample) ===")
hk = collections.Counter()
for e in evs:
    if e.get("bot") == "hermes":
        hk[(e.get("kind"), e.get("phase"), e.get("tool"))] += 1
for k, n in hk.most_common():
    print(f"{n:4d}  {k}")

print("\n=== HERMES bot summaries (unique) ===")
hseen = set()
for e in evs:
    if e.get("bot") == "hermes":
        summ = (e.get("summary") or "")[:110]
        if summ not in hseen:
            hseen.add(summ)
            print(f"[{dt(e.get('ts',0))}Z] {e.get('kind')}/{e.get('tool')}: {summ}")

print("\n=== FLEET events ===")
fk = collections.Counter()
for e in evs:
    if e.get("kind") == "fleet":
        fk[(e.get("bot"), e.get("event") or e.get("type") or e.get("phase"))] += 1
for k, n in fk.most_common():
    print(f"{n:4d}  {k}")

print("\n=== BRIDGE events ===")
for e in evs:
    if e.get("kind") == "bridge":
        print(json.dumps(e, default=str)[:300])

print("\n=== TURN events by bot ===")
tk = collections.Counter()
for e in evs:
    if e.get("kind") == "turn":
        tk[(e.get("bot"), e.get("phase"), e.get("status"))] += 1
for k, n in tk.most_common():
    print(f"{n:4d}  {k}")
