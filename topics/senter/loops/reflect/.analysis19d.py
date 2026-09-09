import json, collections

BOUNDARY = 1788455673
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except Exception:
            continue
new = [e for e in events if e.get("ts", 0) > BOUNDARY]

# Latency per tool (start->end), per bot
starts = {}
lat = collections.defaultdict(list)
for e in new:
    if e.get("kind") != "tool":
        continue
    key = (e.get("bot"), e.get("tool"), e.get("summary", "")[:80])
    if e.get("phase") == "start":
        starts[key] = e["ts"]
    elif e.get("phase") == "end" and key in starts:
        d = e["ts"] - starts[key]
        lat[(e.get("bot"), e.get("tool"))].append(d)
        del starts[key]

print("=== Tool latency (detector 7), new window ===")
for (bot, tool), v in sorted(lat.items(), key=lambda x: -max(x[1])):
    n = len(v)
    avg = sum(v) / n
    mx = max(v)
    flag = "  <-- WATCH (avg>20s)" if avg > 20 else ""
    print("  %-10s %-18s n=%-3d avg=%.1fs max=%.1fs%s" % (bot, tool, n, avg, mx, flag))

# inline-exec / heredoc / shell-append patterns in terminal commands (detector 3)
print("\n=== Detector 3: inline-exec family in terminal (bot=hermes), new window ===")
pat = collections.Counter()
for e in new:
    if e.get("bot") == "hermes" and e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = e.get("summary", "")
        for p in ["python3 -c", "python -c", "<<'EOF'", "| python3", "cat >>", "cat /tmp/", "screencapture", "grep -n", "sed -n", "find ", "for ", "while "]:
            if p in s:
                pat[p] += 1
for p, c in pat.most_common():
    print("  %-16s %d" % (p, c))

# shell-append log writes (detector 3)
print("\n=== 'cat >> log.md' or 'cat /tmp/*.md >>' (shell append for vault writes) ===")
c = 0
for e in new:
    if e.get("bot") == "hermes" and e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = e.get("summary", "")
        if ("cat >>" in s) or (">> log.md" in s) or (">> .system" in s):
            c += 1
print("  count:", c)

# verify-nightly / cron events
print("\n=== any 'verify-nightly' or 'cron' terminal refs this window ===")
for e in new:
    if e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = e.get("summary", "")
        if "verify" in s or "cron" in s.lower():
            print("  %s %s: %s" % (e.get("bot"), e.get("phase"), s[:160]))

# message 'done'/'blocked' status lines
print("\n=== turn end status (done/blocked) ===")
tc = collections.Counter()
for e in new:
    if e.get("kind") == "turn" and e.get("phase") == "end":
        tc[(e.get("bot"), e.get("status"))] += 1
for (b, st), c in tc.most_common():
    print("  %-10s %-8s %d" % (b, st, c))
