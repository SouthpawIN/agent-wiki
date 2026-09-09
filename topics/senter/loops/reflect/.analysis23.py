#!/usr/bin/env python3
"""REFLECT pass 15 — comprehensive window analysis (22:02:44 CDT Sep 3 -> now)."""
import json, collections, datetime

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

CUTOFF = int(datetime.datetime(2026, 9, 4, 3, 2, 44, tzinfo=datetime.timezone.utc).timestamp())
# also exclude my own current run: anser events after 00:00 (this pass-15 run)
SELFCUT = int(datetime.datetime(2026, 9, 4, 5, 0, 0, tzinfo=datetime.timezone.utc).timestamp())  # 00:00 CDT

rows = []
with open(EVENTS) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue

new = [e for e in rows if e.get("ts", 0) > CUTOFF]
fleet = [e for e in new if not (e.get("bot") == "anser" and e.get("ts", 0) >= SELFCUT)]

print("=== WINDOW ===")
print("new total:", len(new), "| fleet (excl this run):", len(fleet))
if fleet:
    print("span:", ts_to_str(fleet[0]["ts"]), "->", ts_to_str(fleet[-1]["ts"]),
          round((fleet[-1]["ts"]-fleet[0]["ts"])/60,1), "min")

# bot x kind
print("\n=== bot x kind ===")
bk = collections.Counter()
for e in fleet:
    bk[(e.get("bot"), e.get("kind"))] += 1
for k, v in sorted(bk.items()):
    print(f"  {k[0]} | {k[1]}: {v}")

# bot x tool
print("\n=== bot x tool ===")
bt = collections.Counter()
for e in fleet:
    if e.get("kind") == "tool":
        bt[(e.get("bot"), e.get("tool"))] += 1
for k, v in sorted(bt.items()):
    print(f"  {k[0]} | {k[1]}: {v}")

# hermes terminal command families
print("\n=== hermes terminal command families ===")
fam = collections.Counter()
for e in fleet:
    if e.get("bot") == "hermes" and e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        s = e.get("summary") or e.get("command") or ""
        if "python3 - <<'EOF'" in s or "python3 - <<EOF" in s or "python3 - <<\"EOF\"" in s:
            fam["python3 heredoc-stdin"] += 1
        elif "python3 -c" in s or "python -c" in s:
            fam["python3 -c"] += 1
        elif s.strip().startswith("grep") or "grep -n" in s:
            fam["grep -n"] += 1
        elif "screencapture" in s:
            fam["screencapture"] += 1
        elif "drive_preview" in s:
            fam["drive_preview"] += 1
        elif "ping -c" in s or "tailscale" in s:
            fam["ping/tailscale (reachability)"] += 1
        else:
            fam["other"] += 1
for k, v in sorted(fam.items()):
    print(f"  {k}: {v}")

# hermes grep/heredoc target regions (extract keywords)
print("\n=== hermes terminal targets (sample of keywords) ===")
import re
kw = collections.Counter()
for e in fleet:
    if e.get("bot") == "hermes" and e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        s = e.get("summary") or ""
        for m in re.findall(r'"(#[a-zA-Z][\w-]*|[a-zA-Z]+[a-zA-Z0-9_-]*)"', s):
            if m not in ("vault", "live", "html", "EOF", "p", "import", "cd", "tmp"):
                kw[m] += 1
top = kw.most_common(30)
for k, v in top:
    print(f"  {k}: {v}")

# approvals
print("\n=== approvals ===")
for e in fleet:
    if e.get("kind") == "approval":
        print(f"  [{e.get('bot')}] {e.get('phase')} {e.get('pattern_key')} :: {e.get('command','')[:90]}")

# turn starts (cron fires)
print("\n=== turn starts (cron/direct) ===")
for e in fleet:
    if e.get("kind") == "turn" and e.get("phase") == "start":
        print(f"  {ts_to_str(e.get('ts'))} | {e.get('bot')} | {e.get('summary','')}")

# github messages (deduped)
print("\n=== github messages (deduped) ===")
gh = collections.Counter()
for e in fleet:
    if e.get("bot") == "github":
        gh[e.get("summary") or ""] += 1
for k, v in gh.most_common(40):
    print(f"  {v}x  {k[:120]}")

# senter terminal commands
print("\n=== senter terminal commands ===")
for e in fleet:
    if e.get("bot") == "senter" and e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        print(f"  {ts_to_str(e.get('ts'))} | {(e.get('summary') or '')[:100]}")

# senter process_manage / other manual
print("\n=== senter process_manage count ===")
print("  process_manage:", sum(1 for e in fleet if e.get('bot')=='senter' and e.get('tool')=='process_manage'))

# BLOCKED / DONE / needs markers in messages
print("\n=== status messages ===")
for e in fleet:
    if e.get("kind") == "message":
        s = (e.get("summary") or e.get("text") or "")
        print(f"  [{e.get('bot')}] status={e.get('status','')} :: {s[:130]}")

# skill events
print("\n=== skill events ===")
for e in fleet:
    if e.get("kind") == "skill":
        print(f"  [{e.get('bot')}] {e.get('skill')} {e.get('action')}")
