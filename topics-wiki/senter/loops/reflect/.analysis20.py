import json, collections, os, datetime, sys, re

path = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
cutoff = 1788464047  # end of pass 9 window (14:34:07 CDT)

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

def fmt(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%m-%d %H:%M:%S')

new = [e for e in events if e.get("ts", 0) > cutoff]
print("TOTAL events in file:", len(events))
print("NEW since cutoff:", len(new))
if new:
    print("window:", fmt(min(e['ts'] for e in new)), "->", fmt(max(e['ts'] for e in new)))

# distinct field keys + kinds
keys = collections.Counter()
for e in new:
    keys.update(e.keys())
print("\n=== distinct field keys ===")
print(dict(keys))

kinds = collections.Counter(e.get("kind") for e in new)
print("\n=== per-kind (NEW) ===")
for k, c in kinds.most_common():
    print(f"  {k}: {c}")

bots = collections.Counter(e.get("bot") for e in new)
print("\n=== per-bot (NEW) ===")
for b, c in bots.most_common():
    print(f"  {b}: {c}")

toolbot = collections.Counter()
for e in new:
    if e.get("kind") == "tool" and e.get("phase") == "start":
        toolbot[(e.get("bot"), e.get("tool"))] += 1
print("\n=== tool calls (start) per bot (NEW) ===")
for (b, t), c in toolbot.most_common(300):
    print(f"  {b} | {t}: {c}")

# detector 3: approval/gate events
print("\n=== DETECTOR 3: approval/gate/blocked events (NEW) ===")
for e in new:
    blob = json.dumps(e)
    if any(k in blob for k in ["approval", "analysis_incomplete", "pipe_to_interpreter", "tirith", "needs_approval", "approved", "allow"]):
        print(f"  {fmt(e.get('ts',0))} bot={e.get('bot')} kind={e.get('kind')} tool={e.get('tool')} status={e.get('status')} {str(e.get('summary'))[:150]}")

# detector 3: inline-exec patterns per bot
print("\n=== DETECTOR 3: inline-exec terminal patterns (start) per bot (NEW) ===")
pat = collections.Counter()
for e in new:
    if e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        s = str(e.get("summary", ""))
        b = e.get("bot")
        if "<<'EOF'" in s or '<<EOF' in s or '<< "EOF"' in s:
            pat[(b, "heredoc")] += 1
        if re.search(r'python3?\s+-c\b', s):
            pat[(b, "python3 -c")] += 1
        if 'cat >>' in s:
            pat[(b, "cat >>")] += 1
        if 'grep -' in s or ' | grep' in s:
            pat[(b, "grep")] += 1
        if 'sed -' in s:
            pat[(b, "sed")] += 1
        if 'screencapture' in s:
            pat[(b, "screencapture")] += 1
        if 'find ' in s and 'xargs' in s:
            pat[(b, "find|xargs")] += 1
for (b, p), c in pat.most_common():
    print(f"  {b} | {p}: {c}")

# detector 4: senter sleep-polls
print("\n=== DETECTOR 4: senter sleep-poll / reflect-watch (NEW) ===")
for e in new:
    if e.get("bot") == "senter" and e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = str(e.get("summary", ""))
        if "sleep" in s or "reflect" in s or "pgrep" in s:
            print(f"  {fmt(e.get('ts',0))} phase={e.get('phase')} {s[:160]}")

# message/status events
print("\n=== message/status events (NEW) ===")
for e in new:
    if e.get("kind") == "message":
        print(f"  {fmt(e.get('ts',0))} bot={e.get('bot')} status={e.get('status')} {str(e.get('text'))[:160]}")

# detector 6: BLOCKED
print("\n=== DETECTOR 6: BLOCKED / blocked text (NEW) ===")
for e in new:
    blob = json.dumps(e)
    if "BLOCKED" in blob or "blocked" in str(e.get("status","")).lower():
        print(f"  {fmt(e.get('ts',0))} bot={e.get('bot')} status={e.get('status')} {str(e.get('summary') or e.get('text'))[:160]}")

# github events
print("\n=== github bot events (NEW) ===")
gsum = collections.Counter()
for e in new:
    if e.get("bot") == "github":
        gsum[str(e.get("summary"))[:130]] += 1
for s, c in gsum.most_common(60):
    print(f"  x{c}: {s}")

# detector 7: latency
print("\n=== DETECTOR 7: tool latency (NEW, matched start->end) ===")
starts = {}
lats = collections.defaultdict(list)
for e in new:
    if e.get("kind") == "tool":
        key = (e.get("bot"), e.get("tool"), e.get("summary"))
        if e.get("phase") == "start":
            starts[key] = e.get("ts")
        elif e.get("phase") == "end" and key in starts:
            d = e.get("ts") - starts[key]
            if 0 <= d < 3600:
                lats[e.get("tool")].append(d)
            del starts[key]
for t, v in sorted(lats.items(), key=lambda x: -sum(x[1])/len(x[1])):
    print(f"  {t}: n={len(v)} avg={sum(v)/len(v):.1f}s max={max(v):.1f}s")
