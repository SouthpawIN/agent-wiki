#!/usr/bin/env python3
"""REFLECT pass 15 — comprehensive window analysis. Cutoff = pass-14 scan end 22:02:44 CDT."""
import json, collections, datetime, re, os

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

# cutoff = 2026-09-03 22:02:44 CDT = 2026-09-04 03:02:44 UTC
CUTOFF = int(datetime.datetime(2026, 9, 4, 3, 2, 44, tzinfo=datetime.timezone.utc).timestamp())
# exclude THIS reflect run (anser events >= 00:07:00 CDT = 05:07:00 UTC)
SELFCUT = int(datetime.datetime(2026, 9, 4, 5, 7, 0, tzinfo=datetime.timezone.utc).timestamp())

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
          round((fleet[-1]["ts"]-fleet[0]["ts"])/60, 1), "min")

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

# turn starts
print("\n=== turn starts ===")
for e in fleet:
    if e.get("kind") == "turn" and e.get("phase") == "start":
        print(f"  {ts_to_str(e.get('ts'))} | {e.get('bot')} | {(e.get('summary') or '')[:80]}")

# hermes terminal command families
print("\n=== hermes terminal command families ===")
fam = collections.Counter()
for e in fleet:
    if e.get("bot") == "hermes" and e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        s = e.get("summary") or e.get("command") or ""
        if "python3 - <<'EOF'" in s or "python3 - <<EOF" in s or 'python3 - <<"EOF"' in s or "python - <<'EOF'" in s:
            fam["python3 heredoc-stdin"] += 1
        elif "python3 -c" in s or "python -c" in s:
            fam["python3 -c"] += 1
        elif "grep -n" in s or s.strip().startswith("grep"):
            fam["grep -n"] += 1
        elif "screencapture" in s:
            fam["screencapture"] += 1
        elif "drive_preview" in s:
            fam["drive_preview"] += 1
        elif "ping -c" in s or "tailscale" in s:
            fam["ping/tailscale (reachability)"] += 1
        elif "cat >>" in s or "cat <<" in s:
            fam["cat append/heredoc"] += 1
        else:
            fam["other"] += 1
for k, v in sorted(fam.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")

# approvals
print("\n=== approvals (request) ===")
for e in fleet:
    if e.get("kind") == "approval" and e.get("phase") in ("request", "start"):
        print(f"  [{e.get('bot')}] pattern_key={e.get('pattern_key')} :: {e.get('command','')[:100]}")
apc = sum(1 for e in fleet if e.get("kind") == "approval")
print("  total approval events:", apc)

# skill events
print("\n=== skill events ===")
sk = collections.Counter()
for e in fleet:
    if e.get("kind") == "skill":
        sk[(e.get("bot"), e.get("skill"), e.get("action"))] += 1
for k, v in sorted(sk.items()):
    print(f"  {k[0]} | {k[1]} | {k[2]}: {v}")

# vision_analyze latency
print("\n=== vision_analyze latency ===")
vtimes = []
vstarts = {}
for e in fleet:
    if e.get("kind") == "tool" and e.get("tool") == "vision_analyze":
        if e.get("phase") == "start":
            vstarts[id(e)] = e.get("ts")
        elif e.get("phase") == "end" and e.get("ts"):
            # pair by nearest start (approx: just record end ts and bot)
            vtimes.append((e.get("bot"), e.get("ts")))
print("  vision_analyze events:", len(vtimes), "bots:", set(b for b,_ in vtimes))

# any tool latency > 20s (detector 7): compute from start->end pairs per bot+tool
print("\n=== detector 7: tool latency (start->end pairs, >15s) ===")
pairs = collections.defaultdict(dict)
lat = collections.defaultdict(list)
for e in fleet:
    if e.get("kind") == "tool":
        key = (e.get("bot"), e.get("tool"))
        if e.get("phase") == "start":
            pairs[key][e.get("ts", 0)] = e
        elif e.get("phase") == "end":
            t = e.get("ts", 0)
            # find nearest start <= t
            best = None
            for st in list(pairs[key].keys()):
                if st <= t and (best is None or st > best):
                    best = st
            if best is not None:
                d = t - best
                lat[key].append(d)
                del pairs[key][best]
for key, ds in lat.items():
    if ds:
        avg = sum(ds)/len(ds)
        mx = max(ds)
        if avg > 15 or mx > 20:
            print(f"  {key[0]} | {key[1]}: n={len(ds)} avg={avg:.1f}s max={mx:.1f}s")

# memory tool ok=false
print("\n=== memory tool results ===")
mem = collections.Counter()
for e in fleet:
    if e.get("kind") == "tool" and e.get("tool") == "memory":
        mem[(e.get("bot"), e.get("ok"))] += 1
for k, v in sorted(mem.items()):
    print(f"  {k[0]} | ok={k[1]}: {v}")

# BLOCKED / DONE / needs markers
print("\n=== status markers in messages ===")
for e in fleet:
    if e.get("kind") == "message":
        s = (e.get("summary") or "") + (e.get("text") or "")
        print(f"  [{e.get('bot')}] status={e.get('status','')} :: {s[:150]}")

# github messages deduped
print("\n=== github messages (deduped) ===")
gh = collections.Counter()
for e in fleet:
    if e.get("bot") == "github":
        gh[(e.get("summary") or e.get("text") or "")[:120]] += 1
for k, v in gh.most_common(30):
    print(f"  {v}x  {k}")

# senter terminal + process_manage
print("\n=== senter terminal commands ===")
for e in fleet:
    if e.get("bot") == "senter" and e.get("kind") == "tool" and e.get("tool") == "terminal" and e.get("phase") == "start":
        print(f"  {ts_to_str(e.get('ts'))} | {(e.get('summary') or '')[:110]}")
print("  senter process_manage count:", sum(1 for e in fleet if e.get('bot')=='senter' and e.get('tool')=='process_manage'))
print("  senter delegate_task count:", sum(1 for e in fleet if e.get('bot')=='senter' and e.get('tool')=='delegate_task'))

# which bots were active at all
print("\n=== active bots ===")
print(" ", sorted(set(e.get('bot') for e in fleet)))
