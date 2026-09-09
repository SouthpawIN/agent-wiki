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

# Find the ONSET of the fleet-changed storm: list fleet-changed events BEFORE the boundary window
# i.e., all fleet-changed events across the WHOLE file, with their gaps, to find when the ~6.6s cadence started.
fleet = [e for e in events if e.get("kind") == "fleet" and e.get("phase") == "changed"]
print("total fleet-changed events in ENTIRE file:", len(fleet))
ts = sorted(e["ts"] for e in fleet)
# find gaps > 60s (storm boundaries)
print("\ngaps > 30s between consecutive fleet-changed events (storm boundaries):")
for i in range(1, len(ts)):
    gap = ts[i] - ts[i-1]
    if gap > 30:
        print(f"  {ts2str(ts[i-1])} -> {ts2str(ts[i])}  gap={gap:.0f}s")
print("\nfirst fleet-changed ever:", ts2str(ts[0]), "| last:", ts2str(ts[-1]))

# What happened right before the storm onset (~20:49:54)?
print("\n=== events 20:48:00 -> 20:51:00 (all kinds, to find the trigger) ===")
for e in events:
    if 1788400000 - 120 <= e.get("ts",0) <= 1788400000 + 120:
        pass
# actually use the storm onset ts directly
onset = None
for i in range(1, len(ts)):
    if ts[i] - ts[i-1] > 30:
        onset = ts[i]
        break
print("storm onset ts:", onset, ts2str(onset))
print("\nevents in the 90s before onset:")
for e in events:
    if onset - 90 <= e.get("ts",0) <= onset:
        k = e.get("kind")
        bot = e.get("bot")
        summary = str(e.get("summary",""))[:120]
        tool = e.get("tool","")
        phase = e.get("phase","")
        print(f"  {ts2str(e['ts'])} kind={k} bot={bot} phase={phase} tool={tool} {summary}")

# Also: is the sentinel or a watcher touching .system-live.json / log.md? Check write_file tool events near onset
print("\n=== write_file tool events across window (what's being written) ===")
for e in events:
    if e.get("kind") == "tool" and e.get("tool") == "write_file" and e.get("phase") == "start" and e.get("ts",0) > 1788397733.0:
        print(f"  {ts2str(e['ts'])} [{e.get('bot')}]: {str(e.get('summary',''))[:120]}")
