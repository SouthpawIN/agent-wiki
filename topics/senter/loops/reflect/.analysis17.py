import json, collections

WL = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
WINDOW_START = 1788419575  # pass-6 file mtime (2026-09-03 02:12:55 CDT)

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
        if ts is None:
            continue
        if ts >= WINDOW_START:
            evs.append(e)

print("TOTAL_EVENTS_IN_WINDOW", len(evs))
if evs:
    t0 = min(e["ts"] for e in evs); t1 = max(e["ts"] for e in evs)
    print("TIME_RANGE_min", round((t1-t0)/60, 1), "first", t0, "last", t1)

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

# approvals
print("\n== approval-related kinds ==")
ack = collections.Counter()
for e in evs:
    s = (str(e.get("kind") or "") + " " + str(e.get("summary") or "")).lower()
    if "approv" in s or "deny" in s:
        ack[e.get("kind") or "(none)"] += 1
for k, v in ack.most_common():
    print(f"  {k}: {v}")

# tool calls + latency (detector 7 + 3)
tool_cnt = collections.Counter()
open_starts = collections.defaultdict(list)
tool_dur = collections.defaultdict(list)
for e in evs:
    if e.get("kind") != "tool":
        continue
    tool = e.get("tool") or "(none)"
    phase = e.get("phase")
    bot = e.get("bot")
    if phase == "start":
        tool_cnt[tool] += 1
        open_starts[(bot, tool)].append(e["ts"])
    elif phase == "end":
        key = (bot, tool)
        if open_starts[key]:
            s = open_starts[key].pop(0)
            tool_dur[tool].append(e["ts"] - s)
print("\n== TOOL CALLS ==")
for t, c in tool_cnt.most_common():
    durs = tool_dur.get(t, [])
    if durs:
        print(f"  {t}: {c} calls, avg {sum(durs)/len(durs):.1f}s, max {max(durs):.1f}s")
    else:
        print(f"  {t}: {c} calls")

# tool calls by bot
print("\n== TOOL CALLS BY BOT ==")
bt = collections.Counter()
for e in evs:
    if e.get("kind") == "tool":
        bt[(e.get("bot"), e.get("tool") or "(none)")] += 1
for (b, t), c in bt.most_common(40):
    print(f"  {b} :: {t}: {c}")

# fleet/changed (detector 6)
fc = [e for e in evs if e.get("kind") == "fleet" and e.get("phase") == "changed"]
print("\n== fleet/changed ==", len(fc))
if fc:
    payloads = collections.Counter()
    for e in fc:
        what = tuple(e.get("what") or [])
        counts = json.dumps(e.get("counts") or {}, sort_keys=True)
        payloads[(what, counts)] += 1
    for (what, counts), c in payloads.most_common(10):
        print(f"  {c}x what={list(what)} counts={counts}")

# github events (detector 5)
gh = [e for e in evs if e.get("kind") == "github" or e.get("bot") == "github"]
print("\n== github events (detector 5) ==", len(gh))
for e in gh[:120]:
    print("  ", round(e.get("ts")), e.get("bot"), e.get("kind"), (e.get("summary") or "")[:140])

# chris messages (detector 1)
print("\n== chris message events (detector 1) ==")
cm = [e for e in evs if e.get("bot") == "chris" and e.get("kind") == "message"]
print("count", len(cm))
for e in cm:
    print("  ", round(e.get("ts")), (e.get("summary") or "")[:160])

# BLOCKED / !ok
blk = [e for e in evs if "BLOCKED" in (e.get("summary") or "") or e.get("phase") == "blocked"]
print("\n== BLOCKED events ==", len(blk))
for e in blk[:60]:
    print("  ", round(e.get("ts")), e.get("bot"), (e.get("summary") or "")[:120])

# turn end status
print("\n== turn end status ==")
sc = collections.Counter()
for e in evs:
    if e.get("kind") == "turn" and e.get("phase") == "end":
        sc[e.get("status") or "(none)"] += 1
for k, v in sc.most_common():
    print(f"  {k}: {v}")
