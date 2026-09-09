import json, collections, sys

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

print("WINDOW_START", WINDOW_START)
print("TOTAL_EVENTS_IN_WINDOW", len(evs))
if evs:
    t0 = min(e["ts"] for e in evs)
    t1 = max(e["ts"] for e in evs)
    print("TIME_RANGE_SEC", round(t1 - t0, 1), "min", round((t1 - t0)/60, 1))
    print("FIRST_TS", t0, "LAST_TS", t1)

# by bot
by_bot = collections.Counter()
for e in evs:
    by_bot[e.get("bot") or "(none)"] += 1
print("\n== BY BOT ==")
for k, v in by_bot.most_common():
    print(f"  {k}: {v}")

# by kind
by_kind = collections.Counter()
for e in evs:
    by_kind[e.get("kind") or "(none)"] += 1
print("\n== BY KIND ==")
for k, v in by_kind.most_common():
    print(f"  {k}: {v}")

# pattern_key (detector 3)
pk = collections.Counter()
for e in evs:
    k = e.get("pattern_key")
    if k:
        pk[k] += 1
print("\n== PATTERN_KEY (detector 3) ==")
for k, v in pk.most_common():
    print(f"  {k}: {v}")

# tool tally + latency (detector 7)
tool_cnt = collections.Counter()
open_starts = collections.defaultdict(list)  # (bot,tool) -> [ts,...]
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
print("\n== TOOL CALLS (detector 3/7) ==")
for t, c in tool_cnt.most_common():
    durs = tool_dur.get(t, [])
    if durs:
        avg = sum(durs)/len(durs)
        mx = max(durs)
        print(f"  {t}: {c} calls, avg {avg:.1f}s, max {mx:.1f}s")
    else:
        print(f"  {t}: {c} calls, no durations")

# fleet/changed (detector 6)
fc = [e for e in evs if e.get("kind") == "fleet" and e.get("phase") == "changed"]
print("\n== fleet/changed (detector 6) ==", len(fc))
if fc:
    payloads = collections.Counter()
    for e in fc:
        what = tuple(e.get("what") or [])
        counts = json.dumps(e.get("counts") or {}, sort_keys=True)
        payloads[(what, counts)] += 1
    for (what, counts), c in payloads.most_common(10):
        print(f"  {c}x what={list(what)} counts={counts}")

# github events (detector 5)
gh = [e for e in evs if e.get("kind") == "github" or (e.get("bot") == "github") or "github" in json.dumps(e.get("summary") or "").lower()]
print("\n== github-related events (detector 5) ==", len(gh))
for e in gh[:80]:
    print("  ", e.get("ts"), e.get("bot"), e.get("kind"), (e.get("summary") or "")[:120])

# BLOCKED / approval events (detector 6)
blk = [e for e in evs if "BLOCKED" in (e.get("summary") or "") or e.get("phase") == "blocked" or e.get("ok") is False]
print("\n== BLOCKED / !ok events (detector 6) ==", len(blk))
for e in blk[:60]:
    print("  ", e.get("ts"), e.get("bot"), e.get("kind"), (e.get("summary") or "")[:100])

# approval-related kinds
apr = [e for e in evs if "approv" in str(e.get("kind") or "").lower() or "approv" in str(e.get("summary") or "").lower()]
print("\n== approval-mention events ==", len(apr))
ack = collections.Counter()
for e in apr:
    ack[e.get("kind") or "(none)"] += 1
for k, v in ack.most_common():
    print(f"  {k}: {v}")
