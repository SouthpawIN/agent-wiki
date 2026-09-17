#!/usr/bin/env python3
"""REFLECT pass 15 — focused follow-up: what bot=hermes did (non-reachability), senter spawns, reflect-instance logs."""
import json, collections, datetime, re, os

EVENTS = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

CUTOFF = int(datetime.datetime(2026, 9, 4, 3, 2, 44, tzinfo=datetime.timezone.utc).timestamp())

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
fleet = [e for e in rows if e.get("ts", 0) > CUTOFF and not (e.get("bot") == "anser" and e.get("ts", 0) >= int(datetime.datetime(2026,9,4,5,7,0,tzinfo=datetime.timezone.utc).timestamp()))]

# hermes non-reachability terminal + skill_view details
print("=== hermes NON-reachability terminal commands (phase=start) ===")
for e in fleet:
    if e.get("bot")=="hermes" and e.get("kind")=="tool" and e.get("tool")=="terminal" and e.get("phase")=="start":
        s = e.get("summary") or ""
        if "ping -c" in s or "tailscale" in s:
            continue
        print(f"  {ts_to_str(e.get('ts'))} | {s[:150]}")

print("\n=== hermes skill_view / skill events ===")
for e in fleet:
    if e.get("bot")=="hermes" and e.get("kind")=="skill":
        print(f"  {ts_to_str(e.get('ts'))} | skill={e.get('skill')} action={e.get('action')}")
for e in fleet:
    if e.get("bot")=="hermes" and e.get("kind")=="tool" and e.get("tool")=="skill_view" and e.get("phase")=="start":
        print(f"  {ts_to_str(e.get('ts'))} | skill_view {e.get('summary','')[:80]}")

print("\n=== hermes drive_preview ===")
print("  drive_preview count:", sum(1 for e in fleet if e.get('bot')=='hermes' and e.get('tool')=='drive_preview'))

# senter delegate_task / spawn events (full)
print("\n=== senter ALL tool commands ===")
for e in fleet:
    if e.get("bot")=="senter" and e.get("kind")=="tool" and e.get("phase")=="start":
        print(f"  {ts_to_str(e.get('ts'))} | {e.get('tool')} | {(e.get('summary') or '')[:130]}")
