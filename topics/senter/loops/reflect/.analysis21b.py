#!/usr/bin/env python3
"""REFLECT pass 11 detail — dump terminal summaries + message/turn text per bot."""
import json, time

CUTOFF = 1788469740
EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
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
new = [e for e in rows if e.get("ts", 0) >= CUTOFF]

def ts(e):
    return time.strftime('%H:%M:%S', time.localtime(e.get('ts', 0)))

# Terminal summaries for hermes and senter
for target in ["hermes", "senter"]:
    print(f"\n########## {target} terminal summaries ##########")
    for e in new:
        if e.get("bot") == target and e.get("tool") == "terminal":
            s = (e.get("summary") or "").replace("\n", " ")
            print(f"  {ts(e)} [{e.get('phase')}] {s[:200]}")

print("\n########## anser terminal summaries (exclude my own reflect run) ##########")
for e in new:
    if e.get("bot") == "anser" and e.get("tool") == "terminal":
        s = (e.get("summary") or "").replace("\n", " ")
        print(f"  {ts(e)} [{e.get('phase')}] {s[:160]}")

print("\n########## hermes non-tool (message/turn/skill/bridge) ##########")
for e in new:
    if e.get("bot") == "hermes" and e.get("kind") in ("message", "turn", "skill", "bridge"):
        s = (e.get("summary") or e.get("text") or "").replace("\n", " ")
        print(f"  {ts(e)} kind={e.get('kind')} {s[:180]}")

print("\n########## senter non-tool ##########")
for e in new:
    if e.get("bot") == "senter" and e.get("kind") != "tool":
        s = (e.get("summary") or e.get("text") or "").replace("\n", " ")
        print(f"  {ts(e)} kind={e.get('kind')} {s[:180]}")

print("\n########## senter tool (non-terminal) ##########")
for e in new:
    if e.get("bot") == "senter" and e.get("kind") == "tool" and e.get("tool") != "terminal":
        s = (e.get("summary") or "").replace("\n", " ")
        print(f"  {ts(e)} tool={e.get('tool')} {s[:160]}")
