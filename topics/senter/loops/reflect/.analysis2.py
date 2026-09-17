import json, collections

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
cutoff = 1788389805  # 2026-09-02 17:56:45 CDT

events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except Exception:
            pass

def ts(e):
    return e.get("ts") if isinstance(e.get("ts"), (int, float)) else None

new = [e for e in events if ts(e) and ts(e) > cutoff]

# approval requests only (phase == request)
reqs = [e for e in new if e.get("kind") == "approval" and e.get("phase") == "request"]
print("NEW approval REQUESTS:", len(reqs))
print("NEW approval events (all phases):", sum(1 for e in new if e.get("kind") == "approval"))

def classify(cmd):
    c = cmd or ""
    if "python3 -c" in c or "python -c" in c:
        return "python3 -c"
    if "<<'PY'" in c or "<<EOF" in c or "execute_code" in c:
        return "heredoc/execute_code"
    if "| python3" in c or "| python " in c or "| python3 -c" in c:
        return "pipe_to_python"
    if "protected" in c or "AGENTS.md" in c or "instruction-file" in c:
        return "protected_instruction_file"
    if "for " in c and "do" in c and "done" in c:
        return "shell_for_loop"
    if "mkdir" in c or "node " in c or "grep " in c:
        return "shell_scripting"
    return "other"

fam = collections.Counter()
per_bot_fam = collections.Counter()
for e in reqs:
    bot = e.get("bot")
    c = e.get("command") or e.get("description") or ""
    k = classify(c)
    fam[k] += 1
    per_bot_fam[(bot, k)] += 1

print("\nNEW approval requests by family:")
for k, c in fam.most_common():
    print(f"  {k:28s} {c}")
print("\nNEW approval requests by bot x family:")
for (b, k), c in sorted(per_bot_fam.items()):
    print(f"  {b:10s} {k:28s} {c}")

# pattern_key in NEW (all events)
pk = collections.Counter(e.get("pattern_key") for e in new if e.get("pattern_key"))
print("\nNEW pattern_key tally:")
for k, c in pk.most_common():
    print(f"  {k:32s} {c}")

# approval requests with timestamps, to see which came after rule-14 landed (~17:59:44 = 1788389984)
rule14_ts = 1788389984
print("\nApproval requests AFTER rule-14 landed (ts > 1788389984):")
for e in reqs:
    if ts(e) and ts(e) > rule14_ts:
        c = e.get("command") or e.get("description") or ""
        print(f"  {e.get('bot'):10s} {classify(c):28s} {c[:80]}")

# weaver vision_analyze in NEW
va = [e for e in new if e.get("kind") == "tool" and e.get("tool") == "vision_analyze"]
print("\nNEW vision_analyze by bot:", dict(collections.Counter(e.get('bot') for e in va)))

# node / probe scripts by weaver (screenshot probe building)
probe = [e for e in new if 'probe-R2' in json.dumps(e) or 'assets/look' in json.dumps(e)]
print("NEW events referencing probe-R2/assets/look (weaver building own screenshot probe):", len(probe))

# terminal churn
term = collections.Counter(e.get('bot') for e in new if e.get('kind')=='tool' and e.get('tool')=='terminal')
print("\nNEW terminal calls by bot:", dict(term))
