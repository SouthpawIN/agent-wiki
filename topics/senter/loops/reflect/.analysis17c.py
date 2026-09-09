import json, collections

WL = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
WINDOW_START = 1788419575

evs = []
with open(WL) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("ts")
        if ts is None or ts < WINDOW_START:
            continue
        evs.append(e)

# fleet/changed timing
fc = [e for e in evs if e.get("kind") == "fleet" and e.get("phase") == "changed"]
if fc:
    t0 = min(e["ts"] for e in fc); t1 = max(e["ts"] for e in fc)
    gaps = [fc[i+1]["ts"] - fc[i]["ts"] for i in range(len(fc)-1)]
    gaps.sort()
    n = len(gaps)
    print(f"fleet/changed: {len(fc)} events, first {round(t0)} last {round(t1)}, span {round((t1-t0)/60,1)} min")
    print(f"gap median {gaps[n//2]:.1f}s, min {gaps[0]:.1f}s, max {gaps[-1]:.1f}s")

# github PR-specific tally (opened/merged/closed counts by teknium)
from collections import Counter
ops = Counter()
for e in evs:
    if e.get("bot") == "github":
        s = e.get("summary") or ""
        who = "teknium1" if "teknium1" in s else ("other" if ("PR" in s or "issue" in s.lower()) else "noise")
        for op in ["opened PR", "merged PR", "closed PR", "closed #", "reopened", "opened #", "pushed 0 commit", "commented on", "create "]:
            if op in s:
                ops[(who, op)] += 1
print("\n== github op tally ==")
for (who, op), c in sorted(ops.items(), key=lambda x:-x[1]):
    print(f"  {who} :: {op}: {c}")

# teknium1 distinct PR numbers touched
import re
prs = set()
for e in evs:
    if e.get("bot") == "github" and "teknium1" in (e.get("summary") or ""):
        for m in re.findall(r'#(\d+)', e.get("summary") or ""):
            prs.add(int(m))
print(f"\nteknium1 distinct PR/issue numbers: {len(prs)}")

# weaver events breakdown
wv = [e for e in evs if e.get("bot") == "weaver"]
print("\n== weaver events ==")
print("  total", len(wv))
for e in wv[:15]:
    print("  ", round(e["ts"]), e.get("kind"), e.get("tool") or "", (e.get("summary") or "")[:100])
