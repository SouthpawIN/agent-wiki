import json, collections, datetime

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

boundary = 1788397733.0
new_events = [e for e in events if e.get("ts", 0) > boundary]
print("total new events:", len(new_events))

# breakdown by kind
kind_cnt = collections.Counter(e.get("kind") for e in new_events)
print("\nby kind:", dict(kind_cnt))

# fleet changed analysis
fleet = [e for e in new_events if e.get("kind") == "fleet" and e.get("phase") == "changed"]
print("\nfleet-changed events:", len(fleet))
if fleet:
    ts = sorted(e["ts"] for e in fleet)
    gaps = [ts[i+1]-ts[i] for i in range(len(ts)-1)]
    avg = sum(gaps)/len(gaps)
    print("  first:", ts2str(ts[0]), "last:", ts2str(ts[-1]))
    print("  avg gap: %.2fs  min gap: %.2fs  max gap: %.2fs" % (avg, min(gaps), max(gaps)))
    # unique counts values
    counts_set = set(json.dumps(e.get("counts"), sort_keys=True) for e in fleet)
    print("  distinct counts payloads:", len(counts_set), list(counts_set)[:3])
    # unique 'what' values
    what_set = set(json.dumps(e.get("what")) for e in fleet)
    print("  distinct 'what':", list(what_set)[:5])

# github events
gh = [e for e in new_events if e.get("bot") == "github"]
print("\ngithub events:", len(gh))

# bridge events
br = [e for e in new_events if e.get("kind") == "bridge"]
print("\nbridge events:", len(br))
for e in br:
    print(f"  {ts2str(e['ts'])} bot={e.get('bot')} phase={e.get('phase')} pid={e.get('pid')} port={e.get('port')} argv={str(e.get('argv',''))[:80]}")

# NON-noise events: tool, turn, message, approval, skill (exclude fleet, github)
print("\n=== NON-NOISE events (tool/turn/message/approval/skill) ===")
non = [e for e in new_events if e.get("kind") in ("tool", "turn", "message", "approval", "skill")]
print("count:", len(non))
print("\n--- message events (dedup) ---")
seen_msg = set()
for e in non:
    if e.get("kind") == "message" and e.get("bot") != "github":
        key = (e.get("bot"), e.get("summary", "")[:60])
        if key in seen_msg:
            continue
        seen_msg.add(key)
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] status={e.get('status')}: {str(e.get('summary',''))[:200]}")

print("\n--- tool events by bot (non-noise) ---")
tb = collections.defaultdict(collections.Counter)
for e in non:
    if e.get("kind") == "tool" and e.get("phase") == "start":
        tb[e.get("bot")][e.get("tool")] += 1
for bot in sorted(tb):
    print(f"  [{bot}]: {dict(tb[bot])}")
