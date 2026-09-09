#!/usr/bin/env python3
"""probe-runind-inject.py — push turn/start events for the weaver children THROUGH the live bridge (append to
~/.hermes/senter-bridge/events.jsonl, the file the running server tails into /events SSE) so the running indicator can
be exercised when the plugin hooks are silent. Same record shape as plugins/senter-bridge/__init__.py emit().
Usage: python3 assets/probe-runind-inject.py weaver:2 senter:1   → 2 weaver instances (distinct pids) + 1 senter."""
import json, os, sys, time
EV = os.path.expanduser(os.environ.get("SENTER_BRIDGE_DATA", "~/.hermes/senter-bridge")) + "/events.jsonl"
recs = []
for arg in sys.argv[1:]:
    bot, n = (arg.split(":") + ["1"])[:2]
    for i in range(int(n)):
        pid = 900000 + (abs(hash(bot)) % 1000) * 10 + i
        recs.append({"ts": time.time(), "bot": bot, "kind": "turn", "phase": "start", "pid": pid, "topic": "senter-wiki", "summary": "probe-runind synthetic instance", "via": "probe"})
with open(EV, "a") as f:
    for r in recs:
        f.write(json.dumps(r) + "\n")
print("appended", len(recs), "turn/start records to", EV)
