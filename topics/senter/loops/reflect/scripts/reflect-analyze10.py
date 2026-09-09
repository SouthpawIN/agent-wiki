import json
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta

CDT = timezone(timedelta(hours=-5))
EV = '/Users/sovthpaw/.hermes/senter-bridge/events.jsonl'
cutoff = 1788570223.0  # 2026-09-04 20:03:43 CDT (end of pass-29 window)

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
        ts = o.get('ts')
        if ts is None or ts < cutoff:
            continue
        rows.append(o)

def ts_str(ts):
    return datetime.fromtimestamp(ts, CDT).strftime('%m-%d %H:%M:%S')

print('TOTAL events in window:', len(rows))
if rows:
    print('earliest:', ts_str(rows[0]['ts']), ' latest:', ts_str(rows[-1]['ts']))
print()
print('=== by bot ===')
for b, c in Counter(r.get('bot') for r in rows).most_common():
    print(f'{c:5d}  {b}')
print()
print('=== by kind ===')
for k, c in Counter(r.get('kind') for r in rows).most_common():
    print(f'{c:5d}  {k}')
print()
print('=== chris messages (detector 1) ===')
for r in rows:
    if r.get('bot') == 'chris':
        print(f"{ts_str(r['ts'])}  chris  kind={r.get('kind')}  {str(r.get('summary',''))[:260]}")
print()
print('=== approval / gate / tirith / policy events (detector 3) ===')
for r in rows:
    s = json.dumps(r)
    if any(k in s.lower() for k in ('approval', 'tirith', 'policy', 'gate', 'pattern_key', 'analysis_incomplete', 'pipe_to_interpreter')):
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  kind={r.get('kind')}  phase={r.get('phase','')}  pattern={r.get('pattern_key','')}  {str(r.get('summary',''))[:150]}")
print()
print('=== BLOCKED events (detector 6) ===')
for r in rows:
    s = json.dumps(r)
    if 'BLOCKED' in s or 'blocked' in s:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  kind={r.get('kind')}  {str(r.get('summary',''))[:220]}")
print()
print('=== terminal commands with exec/poll flags (detectors 3,4) ===')
term = [r for r in rows if r.get('tool') == 'terminal' and r.get('phase') == 'start']
print('total terminal starts:', len(term))
for r in term:
    s = str(r.get('summary', ''))
    flags = []
    for pat, name in [
        ('python3 -c', 'python3-c'), ('python -c', 'python-c'),
        ('<<EOF', 'heredoc'), ("<<'EOF'", 'heredoc'),
        ('| python3', 'pipe-py'), ('| python', 'pipe-py'),
        ('| cat', 'pipe-cat'), ('| tail', 'pipe-tail'), ('| grep', 'pipe-grep'),
        ('| jq', 'pipe-jq'), ('| head', 'pipe-head'), ('| cut', 'pipe-cut'),
        ('for i in $(seq', 'seq-loop'), ('kill -0', 'kill-0 poll'),
        ('sleep ', 'sleep'), ('find ', 'find'), ('xargs', 'xargs'),
        ('$(python3', 'cmdsub-py'), ('while read', 'while-read'),
        ('ps aux', 'ps'),
    ]:
        if pat in s:
            flags.append(name)
    if flags:
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  FLAG={','.join(flags)}  {s[:130]}")
print()
print('=== cron events ===')
for r in rows:
    ss = str(r.get('summary', ''))
    if 'cron' in ss.lower() or r.get('kind') == 'cron' or 'cron_' in str(r.get('phase', '')) or 'cron_' in str(r.get('id', '')):
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  kind={r.get('kind')}  phase={r.get('phase','')}  {ss[:150]}")
print()
print('=== github bot messages ===')
gh = [r for r in rows if r.get('bot') == 'github']
print('total github events:', len(gh))
for r in gh[:50]:
    print(f"{ts_str(r['ts'])}  {str(r.get('summary',''))[:150]}")
print()
print('=== bridge message kind (cards / status) ===')
for r in rows:
    if r.get('kind') == 'message':
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  status={r.get('status','')}  {str(r.get('summary',''))[:170]}")
print()
print('=== tool usage counts ===')
for t, c in Counter(r.get('tool') for r in rows if r.get('tool')).most_common(30):
    print(f'{c:5d}  {t}')
print()
print('=== write_file / patch targets (detector 2) ===')
for r in rows:
    if r.get('tool') in ('write_file', 'patch') and r.get('phase') == 'start':
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  {r.get('tool')}  {str(r.get('summary',''))[:150]}")
print()
print('=== vision_analyze (looker signal) ===')
va = [r for r in rows if r.get('tool') == 'vision_analyze']
print('total vision_analyze:', len(va))
for r in va:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:150]}")
print()
print('=== skill_view loads (detector 5) ===')
sv = [r for r in rows if r.get('tool') == 'skill_view']
print('total skill_view:', len(sv))
for r in sv:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:150]}")
print()
print('=== delegate_task / spawns (detector 4) ===')
dt = [r for r in rows if r.get('tool') == 'delegate_task']
print('total delegate_task:', len(dt))
for r in dt:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  {str(r.get('summary',''))[:150]}")
print()
print('=== spawn events (kind spawn / hermes chat) ===')
for r in rows:
    s = json.dumps(r)
    if 'spawn' in s.lower() or 'hermes chat' in str(r.get('summary', '')).lower():
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  kind={r.get('kind')}  {str(r.get('summary',''))[:180]}")
print()
print('=== fleet changed events ===')
fc = [r for r in rows if str(r.get('kind','')).startswith('fleet') or 'fleet' in str(r.get('summary','')).lower()]
print('total fleet-ish:', len(fc))
for r in fc[:30]:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  kind={r.get('kind')}  phase={r.get('phase','')}  {str(r.get('summary',''))[:150]}")
