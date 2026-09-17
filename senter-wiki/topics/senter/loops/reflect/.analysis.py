import json, collections, sys

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
cutoff = 1788389805  # 2026-09-02 17:56:45 CDT (last reflect file mtime)

events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except Exception:
            pass

print("total events:", len(events))

kinds = collections.Counter(e.get("kind") for e in events)
print("\nKINDS:", dict(kinds))

def has_ts(e):
    return isinstance(e.get("ts"), (int, float))

new = [e for e in events if has_ts(e) and e["ts"] > cutoff]
old = [e for e in events if has_ts(e) and e["ts"] <= cutoff]
print("\nnew events (ts>cutoff):", len(new), " old:", len(old))

# ---- NEW events analysis ----
print("\n=== NEW events: kind breakdown ===")
nk = collections.Counter(e.get("kind") for e in new)
print(dict(nk))

print("\n=== NEW events: bot breakdown ===")
nb = collections.Counter(e.get("bot") for e in new)
print(dict(nb))

print("\n=== NEW events: tool-by-bot (kind==tool) ===")
tb = collections.Counter()
for e in new:
    if e.get("kind") == "tool":
        tb[(e.get("bot"), e.get("tool"))] += 1
for (b, t), c in sorted(tb.items()):
    print(f"  {b:12s} {t:20s} {c}")

print("\n=== NEW events: pattern_key / status / summary ===")
pk = collections.Counter()
for e in new:
    for k in ("pattern_key", "status", "phase"):
        v = e.get(k)
        if v:
            pk[(k, v)] += 1
for (k, v), c in sorted(pk.items()):
    print(f"  {k:14s} {v:30s} {c}")

print("\n=== NEW message events (summary) ===")
for e in new:
    if e.get("kind") == "message":
        print(f"  [{e.get('bot')}] status={e.get('status')} summary={e.get('summary')}")

print("\n=== NEW bridge events ===")
for e in new:
    if e.get("kind") == "bridge":
        print(f"  [{e.get('bot')}] phase={e.get('phase')} argv={(e.get('argv') or '')[:90]}")

# approval-related events anywhere in NEW
print("\n=== NEW approval/deny/timeout/stall events ===")
for e in new:
    s = json.dumps(e)
    if any(w in s.lower() for w in ("approval", "approve", "deny", "timeout", "stall", "tirith", "analysis_incomplete")):
        print("  ", json.dumps(e)[:220])
