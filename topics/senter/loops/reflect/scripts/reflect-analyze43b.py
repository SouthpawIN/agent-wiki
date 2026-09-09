#!/usr/bin/env python3
"""REFLECT pass-43 detail: approvals, inline-exec, chris msgs, BLOCKED, proposals, bot tool breakdown."""
import json, os, datetime, re
from collections import Counter

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
BOUNDARY = 1788657030.0

def iso(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M:%S")

events = []
with open(EVENTS) as fh:
    for ln in fh:
        ln = ln.strip()
        if not ln:
            continue
        try:
            o = json.loads(ln)
        except Exception:
            continue
        ts = o.get("ts", 0)
        if isinstance(ts, (int, float)) and ts >= BOUNDARY:
            events.append(o)

# ---- Detector 3: approval events + their context
print("=== APPROVAL events (7) ===")
for i, e in enumerate(events):
    if e.get("kind") == "approval":
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} :: {str(e.get('summary',''))[:180]}")

# ---- inline-exec patterns in terminal tool summaries
print("\n=== terminal commands w/ inline-exec family ===")
INLINE = re.compile(r"<<\s*'?EOF|python3?\s+-c\b|python3?\s+-e\b|\|\s*python|\|\s*cat|\$\(|execute_code|`|while kill|for .*; do|sqlite3")
pat_count = Counter()
inline_examples = []
for e in events:
    if e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = str(e.get("summary", ""))
        for pat in ["<<EOF", "python3 -c", "python -c", "python3 -e", "| python", "| cat", "$(", "execute_code", "sqlite3", "for ", "; do"]:
            if pat in s:
                pat_count[pat] += 1
        if INLINE.search(s):
            inline_examples.append((e.get("bot"), iso(e["ts"]), s[:140]))
print("pattern counts:", dict(pat_count))
print(f"inline-family terminal events: {len(inline_examples)}")
for bot, t, s in inline_examples[:40]:
    print(f"  [{t}] {bot} :: {s}")

# execute_code tool usage
print("\n=== execute_code tool usage ===")
for e in events:
    if e.get("kind") == "tool" and e.get("tool") == "execute_code":
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} :: {str(e.get('summary',''))[:140]}")

# ---- chris messages (detector 1)
print("\n=== chris / message events with text ===")
for e in events:
    if e.get("bot") == "chris" or (e.get("kind") == "message" and "chris" in str(e.get("summary","")).lower()):
        print(f"  [{iso(e['ts'])}] bot={e.get('bot')} kind={e.get('kind')} :: {str(e.get('summary',''))[:220]}")
