import os, json, glob
from datetime import datetime, timezone, timedelta
from collections import Counter, defaultdict

CDT = timezone(timedelta(hours=-5))
base = "/Users/sovthpaw/Documents/Projects/Projects"

# Pass-22 (the most recent reflect file) completed ~10:06 CDT. Scan NEW since 10:06.
cutoff = datetime(2026, 9, 4, 10, 6, 0, tzinfo=CDT).timestamp()

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
        if ts is None or ts < cutoff:
            continue
        rows.append(o)

def ts_str(ts):
    return datetime.fromtimestamp(ts, CDT).strftime("%m-%d %H:%M:%S")

print(f"=== REFLECT window 10:06:00 -> now (2026-09-04) === total events: {len(rows)}")
if rows:
    print(f"earliest: {ts_str(rows[0]['ts'])}   latest: {ts_str(rows[-1]['ts'])}")

bots = Counter(r.get("bot") for r in rows)
print("\n=== events by bot ===")
for b, c in bots.most_common():
    print(f"{c:5d}  {b}")

kinds = Counter(r.get("kind") for r in rows)
print("\n=== events by kind ===")
for k, c in kinds.most_common():
    print(f"{c:5d}  {k}")

# Chris messages (detector 1)
print("\n=== chris messages ===")
for r in rows:
    if r.get("bot") == "chris":
        print(f"{ts_str(r['ts'])}  chris  {r.get('kind')}  {str(r.get('summary',''))[:200]}")

# approvals / gates / policy (detector 3)
print("\n=== approval / gate / policy / tirith events ===")
for r in rows:
    s = json.dumps(r)
    if any(k in s.lower() for k in ("approval", "tirith", "policy", "gate", "pending_approval", "pattern_key")):
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  phase={r.get('phase','')}  {str(r.get('summary',''))[:160]}  pattern={r.get('pattern_key','')}")

# BLOCKED (detector 6)
print("\n=== BLOCKED events ===")
for r in rows:
    s = json.dumps(r)
    if "BLOCKED" in s or "blocked" in s:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  {str(r.get('summary',''))[:200]}")

# terminal commands — inline exec / polling detection (detectors 3,4)
print("\n=== terminal commands ===")
term = [r for r in rows if r.get("tool") == "terminal"]
print(f"total terminal tool events: {len(term)}")
for r in term:
    s = str(r.get("summary", ""))
    flags = []
    for pat, name in [
        ("python3 -c", "python3-c"), ("python -c", "python-c"),
        ("<<EOF", "heredoc"), ("<<'EOF'", "heredoc"),
        ("| python3", "pipe-py"), ("| python", "pipe-py"),
        ("| cat", "pipe-cat"), ("| tail", "pipe-tail"), ("| grep", "pipe-grep"),
        ("| jq", "pipe-jq"), ("| head", "pipe-head"), ("| cut", "pipe-cut"),
        ("for i in $(seq", "seq-loop"), ("kill -0", "kill-0 poll"),
        ("sleep ", "sleep"), ("find ", "find"), ("xargs", "xargs"),
        ("$(python3", "cmdsub-py"),
    ]:
        if pat in s:
            flags.append(name)
    if flags:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('phase','')}  FLAG={','.join(flags)}  {s[:140]}")

# cron events
print("\n=== cron events ===")
for r in rows:
    ss = str(r.get("summary",""))
    if "cron" in ss.lower() or r.get("kind") == "cron" or "cron_" in str(r.get("phase","")):
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  {r.get('phase','')}  {ss[:160]}")

# github / feed messages
print("\n=== github bot messages ===")
gh = [r for r in rows if r.get("bot") == "github"]
print(f"total github events: {len(gh)}")
for r in gh[:60]:
    print(f"{ts_str(r['ts'])}  {str(r.get('summary',''))[:160]}")

# bridge message cards (status:done, needs_chris)
print("\n=== bridge 'message' kind (cards) ===")
for r in rows:
    if r.get("kind") == "message":
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:180]}")

# tool usage counts
print("\n=== tool usage ===")
tools = Counter(r.get("tool") for r in rows if r.get("tool"))
for t, c in tools.most_common(30):
    print(f"{c:5d}  {t}")

# write_file / patch targets (detector 2)
print("\n=== write_file / patch targets ===")
for r in rows:
    if r.get("tool") in ("write_file", "patch") and r.get("phase") == "start":
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('tool')}  {str(r.get('summary',''))[:160]}")

# vision_analyze (looker signal)
print("\n=== vision_analyze calls ===")
va = [r for r in rows if r.get("tool") == "vision_analyze"]
print(f"total vision_analyze: {len(va)}")
for r in va:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:160]}")

# skill_view loads (detector 5)
print("\n=== skill_view loads ===")
sv = [r for r in rows if r.get("tool") == "skill_view"]
print(f"total skill_view: {len(sv)}")
for r in sv:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:160]}")

# delegate_task / spawns (detector 4)
print("\n=== delegate_task / spawns ===")
dt = [r for r in rows if r.get("tool") == "delegate_task"]
print(f"total delegate_task: {len(dt)}")
for r in dt:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:160]}")
