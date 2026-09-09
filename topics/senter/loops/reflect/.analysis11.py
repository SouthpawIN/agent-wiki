import json, collections, datetime, os

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except Exception:
                pass

def ts2str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

# boundary = mtime of pass-3 file
boundary = 1788397733.0
new_events = [e for e in events if e.get("ts", 0) > boundary]
print("=== WINDOW ===")
print("boundary (pass3 mtime):", ts2str(boundary))
if new_events:
    print("first new event:", ts2str(new_events[0]["ts"]), "| last:", ts2str(new_events[-1]["ts"]))
    print("total new events:", len(new_events))
    span_min = (new_events[-1]["ts"] - new_events[0]["ts"]) / 60
    print("span (min): %.1f" % span_min)
else:
    print("NO NEW EVENTS")

# ---- schema discovery: unique keys per kind ----
print("\n=== SCHEMA: unique keys by kind ===")
keys_by_kind = collections.defaultdict(set)
for e in new_events:
    for k in e.keys():
        keys_by_kind[e.get("kind")].add(k)
for k in sorted(keys_by_kind):
    print(f"  kind={k}: {sorted(keys_by_kind[k])}")

# ---- pattern_key tally (approval gates / block reasons) ----
print("\n=== pattern_key tally (new window) ===")
pk = collections.Counter()
for e in new_events:
    p = e.get("pattern_key")
    if p:
        pk[p] += 1
for k, v in pk.most_common():
    print(f"  {v:4d}  {k}")

# ---- approval / pending events ----
print("\n=== approval-ish events (kind/status) ===")
appr = collections.Counter()
for e in new_events:
    if e.get("kind") in ("approval", "approval_request", "blocked", "needs_approval"):
        appr[e.get("kind")] += 1
    if e.get("status") in ("needs_chris", "blocked", "needs_approval"):
        appr["status:" + str(e.get("status"))] += 1
for k, v in appr.most_common():
    print(f"  {v:4d}  {k}")

# ---- tools by bot ----
print("\n=== tool calls by bot (new window) ===")
tool_by_bot = collections.defaultdict(collections.Counter)
for e in new_events:
    if e.get("kind") == "tool" and e.get("phase") == "start":
        tool_by_bot[e.get("bot")][e.get("tool")] += 1
for bot in sorted(tool_by_bot):
    tc = tool_by_bot[bot]
    total = sum(tc.values())
    top = ", ".join(f"{t}:{c}" for t, c in tc.most_common(6))
    print(f"  [{bot}] total={total}  {top}")

# ---- vision_analyze + computer_use (looker adoption detector 5) ----
print("\n=== vision_analyze / computer_use by bot ===")
va = collections.Counter()
cu = collections.Counter()
for e in new_events:
    if e.get("kind") == "tool" and e.get("phase") == "start":
        if e.get("tool") == "vision_analyze":
            va[e.get("bot")] += 1
        if e.get("tool") == "computer_use":
            cu[e.get("bot")] += 1
print("  vision_analyze:", dict(va))
print("  computer_use:", dict(cu))

# ---- skill loads (detector 5) ----
print("\n=== skill_view / skill loads by bot ===")
skill_loads = collections.defaultdict(collections.Counter)
for e in new_events:
    if e.get("kind") == "tool" and e.get("phase") == "start":
        if e.get("tool") in ("skill_view", "skill_manage"):
            skill_loads[e.get("bot")][e.get("tool")] += 1
        if e.get("tool") == "skill_view" and e.get("summary"):
            skill_loads[e.get("bot")][str(e.get("summary"))[:60]] += 1
for bot in sorted(skill_loads):
    print(f"  [{bot}]: {dict(skill_loads[bot])}")

# ---- needs_chris messages ----
print("\n=== needs_chris / needs_approval messages ===")
for e in new_events:
    if e.get("kind") == "message" and e.get("status") in ("needs_chris", "needs_approval", "blocked"):
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] status={e.get('status')}: {str(e.get('summary',''))[:220]}")
        print()

# ---- sentinel messages (detector 4) ----
print("\n=== sentinel spawn/restart/stall messages ===")
for e in new_events:
    s = str(e.get("summary", ""))
    if e.get("kind") == "message" and any(k in s for k in ("daemon didn't", "spawned", "restart", "stalled", "silent", "sentinel online", "sentinel offline")):
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}]: {s[:220]}")
        print()

# ---- BLOCKED events ----
print("\n=== BLOCKED / error / non-ok tool events ===")
blk = collections.Counter()
for e in new_events:
    s = str(e.get("summary", ""))
    if "BLOCKED" in s or "blocked" in s:
        blk["summary:" + s[:80]] += 1
    if e.get("kind") == "tool" and e.get("phase") == "end" and e.get("ok") is False:
        blk["tool_fail:" + str(e.get("tool"))] += 1
for k, v in blk.most_common(40):
    print(f"  {v:4d}  {k}")

# ---- execute_code / heredoc evidence (detector 3 inline-exec) ----
print("\n=== inline-exec signature evidence (terminal summaries) ===")
sigs = collections.Counter()
for e in new_events:
    if e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = str(e.get("summary", ""))
        for sig in ("python3 -c", "python -c", "python3 - <<", "python - <<", "execute_code", "<<'PY'", "<< 'PY'", "| python3", "| python "):
            if sig in s:
                sigs[sig] += 1
for k, v in sigs.most_common():
    print(f"  {v:4d}  {k}")

# ---- execute_code tool direct ----
print("\n=== execute_code tool calls by bot ===")
ec = collections.Counter()
for e in new_events:
    if e.get("kind") == "tool" and e.get("tool") == "execute_code" and e.get("phase") == "start":
        ec[e.get("bot")] += 1
print("  ", dict(ec))

# ---- terminal total by bot (churn) ----
print("\n=== terminal calls by bot ===")
term = collections.Counter()
for e in new_events:
    if e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        term[e.get("bot")] += 1
print("  ", dict(term))
