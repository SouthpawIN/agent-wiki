import os, json
from datetime import datetime, timezone, timedelta
from collections import Counter, defaultdict

CDT = timezone(timedelta(hours=-5))
base = "/Users/sovthpaw/Documents/Projects/Projects"

# Pass-22 completed 10:06:47 CDT 2026-09-04. Scan NEW since then.
cutoff = datetime(2026, 9, 4, 10, 6, 47, tzinfo=CDT).timestamp()

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

print("=== REFLECT window 10:06:47 -> now (2026-09-04) ===")
print("total events:", len(rows))
if rows:
    print("earliest:", ts_str(rows[0]['ts']), "  latest:", ts_str(rows[-1]['ts']))

bots = Counter(r.get("bot") for r in rows)
print("\n=== events by bot ===")
for b, c in bots.most_common():
    print(f"{c:5d}  {b}")

kinds = Counter(r.get("kind") for r in rows)
print("\n=== events by kind ===")
for k, c in kinds.most_common():
    print(f"{c:5d}  {k}")

print("\n=== chris messages (detector 1) ===")
for r in rows:
    if r.get("bot") == "chris":
        print(f"{ts_str(r['ts'])}  chris  {r.get('kind')}  {str(r.get('summary',''))[:220]}")

print("\n=== approval / gate / tirith / policy events (detector 3) ===")
for r in rows:
    s = json.dumps(r)
    if any(k in s.lower() for k in ("approval", "tirith", "policy", "gate", "pattern_key")):
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  phase={r.get('phase','')}  id={str(r.get('id',''))[:12]}  {str(r.get('summary',''))[:140]}  pattern={r.get('pattern_key','')}")

print("\n=== BLOCKED events (detector 6) ===")
for r in rows:
    s = json.dumps(r)
    if "BLOCKED" in s or "blocked" in s:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  {str(r.get('summary',''))[:200]}")

print("\n=== terminal commands with exec/poll flags (detectors 3,4) ===")
term = [r for r in rows if r.get("tool") == "terminal" and r.get("phase") == "start"]
print("total terminal starts:", len(term))
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
        ("$(python3", "cmdsub-py"), ("while read", "while-read"),
        ("ps aux", "ps"),
    ]:
        if pat in s:
            flags.append(name)
    if flags:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  FLAG={','.join(flags)}  {s[:130]}")

print("\n=== cron events ===")
for r in rows:
    ss = str(r.get("summary",""))
    if "cron" in ss.lower() or r.get("kind") == "cron" or "cron_" in str(r.get("phase","")) or "cron_" in str(r.get("id","")):
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('kind')}  {r.get('phase','')}  {ss[:150]}")

print("\n=== github bot messages ===")
gh = [r for r in rows if r.get("bot") == "github"]
print("total github events:", len(gh))
for r in gh[:40]:
    print(f"{ts_str(r['ts'])}  {str(r.get('summary',''))[:150]}")

print("\n=== bridge 'message' kind (cards / status lines) ===")
for r in rows:
    if r.get("kind") == "message":
        st = r.get("status","")
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  status={st}  {str(r.get('summary',''))[:160]}")

print("\n=== tool usage counts ===")
tools = Counter(r.get("tool") for r in rows if r.get("tool"))
for t, c in tools.most_common(30):
    print(f"{c:5d}  {t}")

print("\n=== write_file / patch targets (detector 2) ===")
for r in rows:
    if r.get("tool") in ("write_file", "patch") and r.get("phase") == "start":
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('tool')}  {str(r.get('summary',''))[:150]}")

print("\n=== vision_analyze calls (looker signal) ===")
va = [r for r in rows if r.get("tool") == "vision_analyze"]
print("total vision_analyze:", len(va))
for r in va:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:150]}")

print("\n=== skill_view loads (detector 5) ===")
sv = [r for r in rows if r.get("tool") == "skill_view"]
print("total skill_view:", len(sv))
for r in sv:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:150]}")

print("\n=== delegate_task / spawns (detector 4) ===")
dt = [r for r in rows if r.get("tool") == "delegate_task"]
print("total delegate_task:", len(dt))
for r in dt:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:150]}")
