import os, json
from datetime import datetime, timezone, timedelta
from collections import Counter

CDT = timezone(timedelta(hours=-5))
# Pass 18 scan end = 06:00:30 CDT; scan NEW since then.
cutoff = datetime(2026, 9, 4, 6, 0, 30, tzinfo=CDT).timestamp()

EV = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")

rows = []
with open(EV) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            continue
        ts = o.get("ts")
        if ts is None:
            continue
        if ts < cutoff:
            continue
        rows.append(o)

def ts_str(ts):
    return datetime.fromtimestamp(ts, CDT).strftime("%m-%d %H:%M:%S")

print(f"=== REFLECT window 06:00:30 -> now (2026-09-04) === total events: {len(rows)}")

bots = Counter(r.get("bot") for r in rows)
print("\n=== events by bot ===")
for b, c in bots.most_common():
    print(f"{c:5d}  {b}")

kinds = Counter(r.get("kind") for r in rows)
print("\n=== events by kind ===")
for k, c in kinds.most_common():
    print(f"{c:5d}  {k}")

# Chris messages
print("\n=== chris messages (kind=message) ===")
for r in rows:
    if r.get("bot") == "chris":
        print(f"{ts_str(r['ts'])}  chris  {r.get('kind')}  {r.get('summary','')[:200]}")

# Approvals / gates
print("\n=== approval / gate / policy events ===")
for r in rows:
    s = json.dumps(r)
    if "approval" in s.lower() or "tirith" in s.lower() or "policy" in s.lower() or "gate" in s.lower():
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  {r.get('phase','')}  {str(r.get('summary',''))[:180]}")

# BLOCKED
print("\n=== BLOCKED events ===")
for r in rows:
    s = json.dumps(r)
    if "BLOCKED" in s or "blocked" in s:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  {str(r.get('summary',''))[:200]}")

# terminal commands (inline exec / polling detection)
print("\n=== terminal commands ===")
term = [r for r in rows if r.get("tool") == "terminal" and r.get("phase") == "start"]
print(f"total terminal starts: {len(term)}")
for r in term:
    s = str(r.get("summary", ""))
    # flag suspicious inline-exec / polling patterns
    flags = []
    for pat, name in [
        ("python3 -c", "python3 -c"), ("python -c", "python -c"),
        ("<<EOF", "heredoc"), ("<<'EOF'", "heredoc"),
        ("| python3", "pipe-py"), ("| python", "pipe-py"),
        ("| cat", "pipe-cat"), ("| tail", "pipe-tail"), ("| grep", "pipe-grep"),
        ("| jq", "pipe-jq"), ("| head", "pipe-head"), ("| cut", "pipe-cut"),
        ("for i in $(seq", "seq-loop"), ("kill -0", "kill-0 poll"),
        ("sleep ", "sleep"), ("find ", "find"), ("xargs", "xargs"),
    ]:
        if pat in s:
            flags.append(name)
    if flags:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  FLAG={','.join(flags)}  {s[:140]}")

# cron events
print("\n=== cron events ===")
for r in rows:
    if "cron" in str(r.get("summary","")).lower() or r.get("kind") == "cron" or "cron_" in str(r.get("phase","")):
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  {r.get('phase','')}  {str(r.get('summary',''))[:160]}")

# github / feed messages
print("\n=== github bot messages ===")
gh = [r for r in rows if r.get("bot") == "github"]
print(f"total github events: {len(gh)}")
for r in gh[:60]:
    print(f"{ts_str(r['ts'])}  {str(r.get('summary',''))[:160]}")

# bridge message cards (status:done, needs_chris, etc.)
print("\n=== bridge 'message' kind (cards) ===")
for r in rows:
    if r.get("kind") == "message":
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:180]}")

# tool usage counts
print("\n=== tool usage ===")
tools = Counter(r.get("tool") for r in rows if r.get("tool"))
for t, c in tools.most_common(30):
    print(f"{c:5d}  {t}")

# write_file / patch targets (to detect same fix on same file)
print("\n=== write_file / patch targets ===")
for r in rows:
    if r.get("tool") in ("write_file", "patch") and r.get("phase") == "start":
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('tool')}  {str(r.get('summary',''))[:160]}")
