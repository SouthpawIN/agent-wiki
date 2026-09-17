#!/usr/bin/env python3
"""REFLECT pass 2026-09-06 (n=1) — deep dives: no-JSON loop, klerik tool family, latency, wiki."""
import json, sys, collections

BOUNDARY = 1788663956
PATH = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

events = []
with open(PATH) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("ts") and e["ts"] > BOUNDARY:
            events.append(e)

# 1. no-JSON loop — count working/blocked per topic, min/max ts
loop = collections.Counter()
loop_ts = collections.defaultdict(list)
for e in events:
    if e.get("kind") == "message":
        s = e.get("summary", "")
        if "bot returned no JSON" in s:
            # extract topic from "AGENT senter · ..." or "AGENT senter-wiki · ..."
            m = s.split("AGENT ")[1].split(" ·")[0] if "AGENT " in s else "?"
            loop[m] += 1
            loop_ts[m].append(e.get("ts"))
print("== no-JSON loop (blocked) counts ==")
for k, c in loop.most_common():
    tss = sorted(loop_ts[k])
    span = f"{tss[0]:.0f} -> {tss[-1]:.0f}" if tss else "n/a"
    print(f"  {k}: {c}  span {span}")
# also count "reading N new raw items"
working = collections.Counter()
for e in events:
    if e.get("kind") == "message" and "reading" in e.get("summary","") and "new raw items" in e.get("summary",""):
        m = e.get("summary","").split("AGENT ")[1].split(" ·")[0] if "AGENT " in e.get("summary","") else "?"
        working[m] += 1
print("== reading-N-new-raw-items (working) counts ==")
for k, c in working.most_common():
    print(f"  {k}: {c}")

# 2. klerik tool family — detect inline-exec / heredoc / execute_code
print("\n== klerik tool calls (kind=tool, bot=klerik) ==")
klerik_tools = collections.Counter()
for e in events:
    if e.get("kind") == "tool" and e.get("bot") == "klerik":
        t = e.get("tool", "?")
        klerik_tools[t] += 1
        if e.get("phase") == "start":
            s = e.get("summary","")
            fam = []
            if "execute_code" in t or "execute_code" in s:
                fam.append("EXECUTE_CODE")
            if "-c" in t or "python3 -c" in s or "python -c" in s or "python - <<" in s or "python3 - <<" in s or "<<'EOF'" in s or "<<EOF" in s:
                fam.append("INLINE/HEREDOC")
            if " | " in s and ("python" in s or "json" in s):
                fam.append("PIPE-INTERP")
            if "cat" in s and ">>" in s:
                fam.append("CAT-APPEND")
            if fam:
                print(f"  [{'/'.join(fam)}] {t}: {s[:120]!r}")
print("  tool histogram:", dict(klerik_tools))

# 3. latency — tool start/end pairs
print("\n== tool latency (start->end, per tool, this window) ==")
starts = {}
lat = collections.defaultdict(list)
for e in events:
    if e.get("kind") == "tool":
        key = (e.get("bot"), e.get("tool"), e.get("summary"))
        if e.get("phase") == "start":
            starts[key] = e.get("ts")
        elif e.get("phase") == "end" and key in starts:
            lat[e.get("tool")].append(e.get("ts") - starts[key])
            del starts[key]
for t, vals in lat.items():
    if len(vals) >= 1:
        avg = sum(vals)/len(vals)
        print(f"  {t}: n={len(vals)} avg={avg:.1f}s max={max(vals):.1f}s")

# 4. wiki events
print("\n== wiki events ==")
for e in events:
    if e.get("kind") == "wiki":
        print(f"  bot={e.get('bot')} phase={e.get('phase')} summary={e.get('summary','')[:120]!r}")
