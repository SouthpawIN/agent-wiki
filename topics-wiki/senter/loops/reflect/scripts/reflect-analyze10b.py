import json
from collections import Counter
from datetime import datetime, timezone, timedelta

CDT = timezone(timedelta(hours=-5))
EV = '/Users/sovthpaw/.hermes/senter-bridge/events.jsonl'
cutoff = 1788570223.0

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

print('=== teknium events (empty-turn check) ===')
for r in rows:
    if r.get('bot') == 'teknium':
        print(f"{ts_str(r['ts'])}  kind={r.get('kind')}  phase={r.get('phase','')}  tool={r.get('tool','')}  {str(r.get('summary',''))[:160]}")

print()
print('=== senter events that are NOT fleet ===')
for r in rows:
    if r.get('bot') == 'senter' and r.get('kind') != 'fleet':
        print(f"{ts_str(r['ts'])}  kind={r.get('kind')}  phase={r.get('phase','')}  tool={r.get('tool','')}  {str(r.get('summary',''))[:180]}")

print()
print('=== approval events full detail ===')
for r in rows:
    if r.get('kind') == 'approval':
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  phase={r.get('phase','')}  pattern={r.get('pattern_key','')}  id={str(r.get('id',''))[:20]}  {str(r.get('summary',''))[:200]}")

print()
print('=== turn events (start/end) by bot ===')
turns = [r for r in rows if r.get('kind') == 'turn']
print('total turn events:', len(turns))
for r in turns:
    print(f"{ts_str(r['ts'])}  {r.get('bot')}  phase={r.get('phase','')}  {str(r.get('id',''))[:40]}")

print()
print('=== bridge kind ===')
for r in rows:
    if r.get('kind') == 'bridge':
        print(f"{ts_str(r['ts'])}  {r.get('bot')}  phase={r.get('phase','')}  {str(r.get('summary',''))[:180]}")

print()
print('=== all hermes events summary (non-terminal) ===')
for r in rows:
    if r.get('bot') == 'hermes' and r.get('tool') != 'terminal':
        print(f"{ts_str(r['ts'])}  kind={r.get('kind')}  phase={r.get('phase','')}  tool={r.get('tool','')}  {str(r.get('summary',''))[:160]}")

print()
print('=== anser events non-terminal non-tool (context for what cron reflect did) ===')
for r in rows:
    if r.get('bot') == 'anser' and r.get('tool') not in ('terminal', 'read_file', 'write_file', 'search_files', 'patch', 'process_manage'):
        print(f"{ts_str(r['ts'])}  kind={r.get('kind')}  phase={r.get('phase','')}  {str(r.get('summary',''))[:200]}")
