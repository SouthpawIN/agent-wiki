import json,time
rows=[json.loads(l) for l in open('/Users/sovthpaw/.hermes/senter-bridge/events.jsonl') if 'Senter Wiki edit' in l]
chris=[r for r in rows if r.get('bot')=='chris']
print(len(chris),'chris edit posts; last at', time.strftime('%H:%M:%S',time.localtime(chris[-1]['ts'])), 'now', time.strftime('%H:%M:%S'))
for r in chris[-6:]: print(time.strftime('%H:%M:%S',time.localtime(r['ts'])), r['summary'][:70])
