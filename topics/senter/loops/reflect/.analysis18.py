import json, collections, re, os

WL = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
# pass-7 file mtime (2026-09-03-7.md) = 1788450607 = 10:50:07 CDT
WINDOW_START = 1788450607

evs = []
with open(WL) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("ts")
        if ts is None or ts < WINDOW_START:
            continue
        evs.append(e)

print("TOTAL_EVENTS_IN_WINDOW", len(evs))
if evs:
    t0 = min(e["ts"] for e in evs); t1 = max(e["ts"] for e in evs)
    print("TIME_RANGE_min", round((t1-t0)/60, 1), "first", round(t0), "last", round(t1))

print("\n== BY BOT ==")
for k, v in collections.Counter(e.get("bot") or "(none)" for e in evs).most_common():
    print(f"  {k}: {v}")

print("\n== BY KIND ==")
for k, v in collections.Counter(e.get("kind") or "(none)" for e in evs).most_common():
    print(f"  {k}: {v}")

print("\n== PATTERN_KEY (detector 3) ==")
pk = collections.Counter(e.get("pattern_key") for e in evs if e.get("pattern_key"))
for k, v in pk.most_common():
    print(f"  {k}: {v}")

print("\n== TOOL CALLS (detector 7 latency) ==")
tool_cnt = collections.Counter()
open_starts = collections.defaultdict(list)
tool_dur = collections.defaultdict(list)
for e in evs:
    if e.get("kind") != "tool":
        continue
    tool = e.get("tool") or "(none)"
    phase = e.get("phase"); bot = e.get("bot")
    if phase == "start":
        tool_cnt[tool] += 1
        open_starts[(bot, tool)].append(e["ts"])
    elif phase == "end":
        key = (bot, tool)
        if open_starts[key]:
            s = open_starts[key].pop(0)
            tool_dur[tool].append(e["ts"] - s)
for t, c in tool_cnt.most_common():
    durs = tool_dur.get(t, [])
    if durs:
        print(f"  {t}: {c} calls, avg {sum(durs)/len(durs):.1f}s, max {max(durs):.1f}s")
    else:
        print(f"  {t}: {c} calls")

print("\n== TOOL CALLS BY BOT ==")
bt = collections.Counter()
for e in evs:
    if e.get("kind") == "tool":
        bt[(e.get("bot"), e.get("tool") or "(none)")] += 1
for (b, t), c in bt.most_common(50):
    print(f"  {b} :: {t}: {c}")

print("\n== github events (detector 5) ==")
gh = [e for e in evs if e.get("kind") == "github" or e.get("bot") == "github"]
print("count", len(gh))
for e in gh[:200]:
    print("  ", round(e.get("ts")), e.get("bot"), e.get("kind"), (e.get("summary") or "")[:160])

print("\n== chris message events (detector 1) ==")
cm = [e for e in evs if e.get("bot") == "chris" and e.get("kind") == "message"]
print("count", len(cm))
for e in cm:
    print("  ", round(e.get("ts")), (e.get("summary") or "")[:200])

print("\n== message events (all bots) ==")
msgs = [e for e in evs if e.get("kind") == "message"]
print("count", len(msgs))
for e in msgs[:120]:
    print("  ", round(e.get("ts")), e.get("bot"), "|", (e.get("status") or ""), "|", (e.get("summary") or "")[:180])

print("\n== BLOCKED / blocked phase ==")
blk = [e for e in evs if "BLOCKED" in (e.get("summary") or "") or e.get("phase") == "blocked" or e.get("status") == "blocked"]
print("count", len(blk))
for e in blk[:60]:
    print("  ", round(e.get("ts")), e.get("bot"), (e.get("summary") or "")[:150])

print("\n== turn end status ==")
sc = collections.Counter()
for e in evs:
    if e.get("kind") == "turn" and e.get("phase") == "end":
        sc[e.get("status") or "(none)"] += 1
for k, v in sc.most_common():
    print(f"  {k}: {v}")

print("\n== approval events ==")
ap = [e for e in evs if e.get("kind") == "approval"]
print("count", len(ap))
apc = collections.Counter(e.get("phase") for e in ap)
for k, v in apc.most_common():
    print(f"  phase {k}: {v}")

print("\n== fleet/changed (detector 6) ==")
fc = [e for e in evs if e.get("kind") == "fleet" and e.get("phase") == "changed"]
print("count", len(fc))

print("\n== bridge events ==")
br = [e for e in evs if e.get("kind") == "bridge"]
print("count", len(br))
for e in br[:40]:
    print("  ", round(e.get("ts")), e.get("bot"), e.get("phase"), (e.get("summary") or "")[:140])

print("\n== patch/write_file targets (detector 2) ==")
pt = collections.Counter()
for e in evs:
    if e.get("kind") == "tool" and e.get("tool") in ("patch", "write_file") and e.get("phase") == "start":
        s = e.get("summary") or ""
        pt[(e.get("bot"), s[:90])] += 1
for (b, s), c in pt.most_common(80):
    print(f"  [{c}] {b} :: {s}")

print("\n== terminal commands (detector 3/4) ==")
tm = [e for e in evs if e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start"]
print("count", len(tm))
for e in tm[:150]:
    print("  ", round(e.get("ts")), e.get("bot"), (e.get("summary") or "")[:150])
