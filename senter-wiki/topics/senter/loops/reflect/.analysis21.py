#!/usr/bin/env python3
"""REFLECT pass 11 analysis — scan events.jsonl for data NEW since pass 10 (mtime 16:09:00)."""
import json, collections, time

CUTOFF = 1788469740  # 2026-09-03 16:09:00 (pass-10 file mtime)
EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

rows = []
with open(EVENTS) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        rows.append(e)

new = [e for e in rows if e.get("ts", 0) >= CUTOFF]
print(f"TOTAL events: {len(rows)}, NEW since cutoff (16:09:00): {len(new)}")

if new:
    tmin = min(e["ts"] for e in new)
    tmax = max(e["ts"] for e in new)
    print(f"window: {time.strftime('%H:%M:%S', time.localtime(tmin))} -> {time.strftime('%H:%M:%S', time.localtime(tmax))}  ({(tmax-tmin)/60:.1f} min)")

# bot counts
bots = collections.Counter(e.get("bot") for e in new)
print("\n=== bot counts ===")
for b, c in bots.most_common():
    print(f"  {b}: {c}")

# kind counts
kinds = collections.Counter(e.get("kind") for e in new)
print("\n=== kind counts ===")
for k, c in kinds.most_common():
    print(f"  {k}: {c}")

# tool counts per bot
toolbots = collections.Counter((e.get("bot"), e.get("tool")) for e in new if e.get("kind") == "tool")
print("\n=== tool counts (bot, tool) ===")
for (b, t), c in toolbots.most_common(60):
    print(f"  {b} | {t}: {c}")

# terminal command families (rule 14 inline-exec)
print("\n=== terminal command family scan (rule 14) ===")
fam = collections.Counter()
for e in new:
    if e.get("tool") == "terminal":
        s = (e.get("summary") or "")
        if "python3 -c" in s or "python -c" in s:
            fam["python -c"] += 1
        elif "<<'EOF'" in s or "<<EOF" in s or "<< \"EOF\"" in s:
            fam["heredoc"] += 1
        elif "cat >>" in s or ">> log.md" in s or "cat >" in s:
            fam["shell-append"] += 1
        elif "| xargs" in s or "| sort" in s or "find " in s:
            fam["find|xargs"] += 1
        elif "| grep" in s or "grep -n" in s:
            fam["grep"] += 1
        elif "| python" in s or "| tail" in s:
            fam["pipe-to-interp"] += 1
        elif "screencapture" in s:
            fam["screencapture"] += 1
        elif "sed -n" in s or "sed " in s:
            fam["sed"] += 1
        else:
            fam["other"] += 1
for k, c in fam.most_common():
    print(f"  {k}: {c}")

# github events
print("\n=== github events (kind=github or tool=github) ===")
gh = [e for e in new if e.get("tool") == "github" or "github" in str(e.get("kind",""))]
for e in gh[-40:]:
    print(f"  [{e.get('bot')}] {e.get('summary','')[:160]}")

# BLOCKED / DONE / needs_chris messages
print("\n=== DONE / BLOCKED / needs_chris ===")
for e in new:
    s = (e.get("summary") or "") + " " + (e.get("text") or "")
    if any(x in s for x in ["DONE", "BLOCKED", "needs_chris", "NEEDS_CHRIS", "needs-chris"]):
        print(f"  [{e.get('bot')}] kind={e.get('kind')} ts={time.strftime('%H:%M:%S', time.localtime(e.get('ts',0)))}: {s[:200]}")

# approval events
print("\n=== approval prompts ===")
ap = [e for e in new if e.get("kind") == "approval" or "approve" in str(e.get("kind","")).lower() or "approval" in (e.get("summary") or "")]
for e in ap:
    print(f"  [{e.get('bot')}] ts={time.strftime('%H:%M:%S', time.localtime(e.get('ts',0)))}: {(e.get('summary') or '')[:140]}")
print(f"  (total approval-ish events: {len(ap)})")

# vision latency
print("\n=== vision_analyze latency ===")
v = [e for e in new if e.get("tool") == "vision_analyze"]
if v:
    dur = [e.get("duration", e.get("dur", 0)) for e in v]
    print(f"  calls={len(v)}, durations={dur[:20]}")

# summary tail of non-tool events (messages, turns)
print("\n=== message/turn events (tail 30) ===")
ms = [e for e in new if e.get("kind") in ("message","turn","event","done","status") or e.get("kind") not in ("tool",)]
for e in ms[-30:]:
    print(f"  [{e.get('bot')}] kind={e.get('kind')} ts={time.strftime('%H:%M:%S', time.localtime(e.get('ts',0)))}: {(e.get('summary') or e.get('text') or '')[:160]}")
