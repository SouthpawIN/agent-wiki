#!/usr/bin/env python3
"""REFLECT loop — events.jsonl analyzer (pass 42).

Reads ~/.hermes/senter-bridge/events.jsonl, filters events NEW since the
most recent reflect file mtime, and prints a compact, structured summary
for the six detectors. No inline-exec: run by path.
"""
import json, os, sys, collections, datetime

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
REFLECT_DIR = "/Users/sovthpaw/Documents/Projects/Projects/topics/senter/loops/reflect"

# Boundary = mtime of the most recent reflect file (pass 41).
def latest_reflect_file():
    files = [f for f in os.listdir(REFLECT_DIR) if f.endswith(".md")]
    files.sort()
    return os.path.join(REFLECT_DIR, files[-1]), files[-1]

latest_path, latest_name = latest_reflect_file()
boundary = os.path.getmtime(latest_path)
print(f"# boundary file: {latest_name}  mtime={boundary:.3f}  ({datetime.datetime.fromtimestamp(boundary).strftime('%Y-%m-%d %H:%M:%S %Z')})")

rows = []
with open(EVENTS, "r") as fh:
    for line in fh:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = e.get("ts")
        if ts is None:
            continue
        if ts > boundary:
            rows.append(e)

print(f"# NEW events: {len(rows)}")
if not rows:
    sys.exit(0)

tmin = min(r["ts"] for r in rows)
tmax = max(r["ts"] for r in rows)
print(f"# window: {datetime.datetime.fromtimestamp(tmin).strftime('%H:%M:%S')} -> {datetime.datetime.fromtimestamp(tmax).strftime('%H:%M:%S')} CDT")

# --- per bot ---
bots = collections.Counter(r.get("bot") for r in rows)
print("\n== per-bot event counts ==")
for b, c in bots.most_common():
    print(f"  {b}: {c}")

# --- per tool (kind=tool) ---
tools = collections.Counter()
tool_ok = collections.Counter()
for r in rows:
    if r.get("kind") == "tool":
        t = r.get("tool", "?")
        tools[t] += 1
        if r.get("phase") == "end":
            tool_ok[(t, bool(r.get("ok")))] += 1
print("\n== tool counts (start events) ==")
for t, c in tools.most_common():
    ok = tool_ok.get((t, True), 0)
    bad = tool_ok.get((t, False), 0)
    print(f"  {t}: {c} (end ok={ok} fail={bad})")

# --- approvals ---
approvals = collections.Counter()
approval_commands = collections.Counter()
for r in rows:
    if r.get("kind") == "approval" and r.get("phase") == "request":
        pk = r.get("pattern_key", "?")
        approvals[pk] += 1
        cmd = r.get("command", "") or ""
        # classify inline-exec family
        fam = None
        if "<<'EOF'" in cmd or "<<EOF" in cmd or "<< \"EOF\"" in cmd:
            fam = "heredoc"
        elif "python3 -c" in cmd or "python -c" in cmd or "python3 -e" in cmd or "python -e" in cmd:
            fam = "python -c/-e"
        elif " | python" in cmd or "| python" in cmd:
            fam = "pipe-to-interpreter"
        elif "cat >" in cmd or "cat >>" in cmd or "echo" in cmd and ">>" in cmd:
            fam = "shell-append"
        elif "for " in cmd and " done" in cmd:
            fam = "shell-for-loop"
        elif "$(" in cmd:
            fam = "command-substitution"
        else:
            fam = "other"
        approval_commands[fam] += 1
print("\n== approval requests by pattern_key ==")
for pk, c in approvals.most_common():
    print(f"  {pk}: {c}")
print("== approval requests by command family ==")
for f, c in approval_commands.most_common():
    print(f"  {f}: {c}")

# sample some approval command texts (dedup)
print("\n== sample approval command texts (dedup) ==")
seen_cmds = set()
for r in rows:
    if r.get("kind") == "approval" and r.get("phase") == "request":
        cmd = r.get("command", "") or ""
        if cmd not in seen_cmds and len(cmd) > 3:
            seen_cmds.add(cmd)
            print(f"  [{r.get('bot')}] {r.get('pattern_key')}: {cmd[:160]}")
            if len(seen_cmds) >= 30:
                break

# --- messages (chris) and senter narrative (non-empty summary) ---
print("\n== chris message summaries ==")
for r in rows:
    if r.get("bot") == "chris" and r.get("kind") == "message":
        print(f"  {r.get('summary','')[:200]}")

# --- turn starts/ends per bot (activity) ---
turns = collections.Counter()
for r in rows:
    if r.get("kind") == "turn" and r.get("phase") == "start":
        turns[r.get("bot")] += 1
print("\n== turn starts per bot ==")
for b, c in turns.most_common():
    print(f"  {b}: {c}")

# --- senter FILED / PROPOSAL / SKILL / WORKER / AGENT / WIKI / NEEDS / BLOCKED / DONE in summaries ---
print("\n== senter narrative events (non-empty summary, kind bridge/turn) ==")
narr = 0
for r in rows:
    s = (r.get("summary") or "").strip()
    if not s:
        continue
    if r.get("bot") == "senter" or r.get("kind") in ("turn", "bridge"):
        if any(k in s for k in ("FILED", "PROPOSAL", "SKILL", "WORKER", "AGENT", "WIKI", "NEEDS", "BLOCKED", "DONE", "chris:", "Chris:", "distilled", "proposed", "spawn")):
            narr += 1
            print(f"  [{r.get('bot')}/{r.get('kind')}/{r.get('phase')}] {s[:180]}")
            if narr >= 120:
                print("  ... (truncated)")
                break
print(f"(narrative events shown: {narr})")

# --- BLOCKED / DONE markers anywhere in summaries ---
blocked = [r for r in rows if "BLOCKED" in (r.get("summary") or "")]
done = [r for r in rows if "DONE" in (r.get("summary") or "")]
print(f"\n== markers: BLOCKED={len(blocked)} DONE={len(done)} ==")
for r in blocked[:20]:
    print(f"  BLOCKED [{r.get('bot')}] {r.get('summary','')[:160]}")

# --- write_file / patch targets (detector 2: same file/region) ---
writes = collections.Counter()
patches = collections.Counter()
for r in rows:
    if r.get("kind") == "tool" and r.get("phase") == "start":
        if r.get("tool") == "write_file":
            writes[r.get("summary") or "(no summary)"] += 1
        if r.get("tool") == "patch":
            patches[r.get("summary") or "(no summary)"] += 1
print("\n== write_file targets (summary field, may be empty) ==")
for t, c in writes.most_common(30):
    print(f"  {c}x  {t[:120]}")
print("== patch targets ==")
for t, c in patches.most_common(30):
    print(f"  {c}x  {t[:120]}")

# --- skill loads / skill_manage (detector 5) ---
skill_events = collections.Counter()
for r in rows:
    if r.get("kind") == "tool":
        if r.get("tool") in ("skill_view", "skill_manage", "skills_list"):
            skill_events[(r.get("bot"), r.get("tool"))] += 1
print("\n== skill tool usage per bot ==")
for (b, t), c in skill_events.most_common():
    print(f"  {b} {t}: {c}")

# --- delegate_task / computer_use / vision_analyze (detector 4/5 visual QA re-implementation) ---
visual = collections.Counter()
for r in rows:
    if r.get("kind") == "tool" and r.get("phase") == "start":
        if r.get("tool") in ("vision_analyze", "computer_use", "delegate_task"):
            visual[(r.get("bot"), r.get("tool"))] += 1
print("\n== vision/computer/delegate usage per bot ==")
for (b, t), c in visual.most_common():
    print(f"  {b} {t}: {c}")
