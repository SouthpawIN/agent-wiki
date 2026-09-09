#!/usr/bin/env python3
import json, collections, datetime

CUTOFF = 1788591936  # pass-33 file mtime
path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
rows = []
with open(path, "r", encoding="utf-8", errors="replace") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
new = [r for r in rows if r.get("ts", 0) > CUTOFF]

def dt(ts):
    return datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc).strftime("%H:%M:%S")

# phase-filtered terminal (start only)
print("=== terminal commands (phase=start ONLY) by bot ===")
starts = [r for r in new if r.get("kind") == "tool" and r.get("tool") == "terminal" and r.get("phase") == "start"]
tby = collections.Counter((r.get("bot"), r.get("summary")) for r in starts)
for k, v in tby.most_common(60):
    print(f"  {v:3d}  {k[0]} | {k[1][:140]}")

# ping count exact
pings = [r for r in starts if r.get("bot") == "hermes" and "ping -c 2" in (r.get("summary") or "")]
print("\nhermes ping count (start-only):", len(pings))

# approvals detail
print("\n=== approvals (all fields) ===")
for r in new:
    if r.get("kind") == "approval":
        print("  ", dt(r.get("ts",0)), "bot=", r.get("bot"), "choice=", r.get("choice"), "pk=", r.get("pattern_key"))
        for key in ("tool","command","summary","rule","analysis"):
            if r.get(key):
                print(f"      {key}: {str(r[key])[:300]}")

# weaver terminal command detail (what did verify-nightly do/decide)
print("\n=== weaver terminal starts (full command) ===")
for r in starts:
    if r.get("bot") == "weaver":
        print("  ", dt(r.get("ts",0)), "|", (r.get("summary") or "")[:200])

# skill events
print("\n=== skill events (all) ===")
for r in new:
    if r.get("kind") == "skill":
        print("  ", dt(r.get("ts",0)), json.dumps(r, default=str)[:220])

# bridge done/status posts
print("\n=== bridge posts (bot + text) ===")
for r in new:
    if r.get("kind") == "bridge" and (r.get("phase") in ("post","done","needs_chris","message")):
        print("  ", dt(r.get("ts",0)), r.get("bot"), "|", (r.get("text") or r.get("summary") or "")[:200])

# execute_code detail
print("\n=== execute_code (weaver) ===")
for r in new:
    if r.get("tool") == "execute_code":
        print("  ", dt(r.get("ts",0)), r.get("bot"), r.get("phase"), "ok=", r.get("ok"), "|", (r.get("summary") or "")[:160])

# vision / read_file / patch / write_file by bot
print("\n=== other tools by bot (start-only) ===")
ot = collections.Counter((r.get("bot"), r.get("tool")) for r in new if r.get("kind") == "tool" and r.get("phase") == "start" and r.get("tool") not in ("terminal",))
for k, v in ot.most_common():
    print(f"  {v:3d}  {k}")
