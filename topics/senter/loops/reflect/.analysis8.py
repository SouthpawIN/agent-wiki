import json, datetime, collections, os

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

rf2 = "/Users/sovthpaw/Documents/Projects/Projects/topics/senter/loops/reflect/2026-09-02-2.md"
boundary = os.path.getmtime(rf2)
new_events = [e for e in events if e.get("ts", 0) > boundary]

appr = [e for e in new_events if e.get("kind") == "approval"]

# analysis_incomplete sample commands
print("=== analysis_incomplete: sample commands (dedup) ===")
ai = [e for e in appr if e.get("pattern_key") == "tirith:analysis_incomplete"]
seen = collections.Counter(e.get("command","")[:90] for e in ai)
for c, n in seen.most_common(20):
    print(f"  [{n}] {c!r}")

# pipe_to_interpreter samples
print("\n=== pipe_to_interpreter: sample commands ===")
pi = [e for e in appr if e.get("pattern_key") == "tirith:pipe_to_interpreter"]
seen2 = collections.Counter(e.get("command","")[:100] for e in pi)
for c, n in seen2.most_common(12):
    print(f"  [{n}] {c!r}")

# execute_code approvals
print("\n=== execute_code approvals ===")
ec = [e for e in appr if e.get("pattern_key") == "execute_code"]
for e in ec:
    print(f"  {ts2str(e['ts'])} [{e.get('bot')}] {e.get('command','')[:80]!r}")

# protected_instruction_file - which files
print("\n=== protected_instruction_file: files targeted ===")
pf = [e for e in appr if e.get("pattern_key") == "protected_instruction_file"]
for e in pf:
    print(f"  {ts2str(e['ts'])} [{e.get('bot')}] {e.get('command','')[:70]!r}")

# BLOCKED events - any kind/status
print("\n=== BLOCKED occurrences (message + status) ===")
for e in new_events:
    s = str(e.get("summary","")) + " " + str(e.get("status","")) + " " + str(e.get("description",""))
    if "blocked" in s.lower():
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}] {e.get('kind')} {e.get('status','')} {str(e.get('summary',''))[:100]}")
