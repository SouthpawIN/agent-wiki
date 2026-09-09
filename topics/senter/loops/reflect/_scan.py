#!/usr/bin/env python3
import json, collections, datetime, sys

CUTOFF = 1788563448  # pass-27 file mtime = 2026-09-04 18:10:48 CDT

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
evs = []
with open(path, "r", encoding="utf-8", errors="replace") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("ts")
        if ts is None:
            continue
        if ts > CUTOFF:
            evs.append(e)

print("=== TOTAL events since cutoff ===")
print(len(evs))

print("\n=== by bot ===")
by_bot = collections.Counter(e.get("bot") for e in evs)
for b, c in by_bot.most_common():
    print(f"{c:6d}  {b}")

print("\n=== by kind ===")
by_kind = collections.Counter(e.get("kind") for e in evs)
for k, c in by_kind.most_common():
    print(f"{c:6d}  {k}")

print("\n=== approvals (gate trips) ===")
for e in evs:
    if e.get("kind") == "approval":
        choice = e.get("choice", "")
        pk = e.get("pattern_key", "")
        bot = e.get("bot", "")
        cmd = (e.get("command") or "")[:110]
        ts = e.get("ts", 0)
        dt = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
        print(f"[{dt:%H:%M:%S}Z] {bot} choice={choice} pk={pk}\n    cmd: {cmd}")

print("\n=== tool calls by tool (phase=start) ===")
tools = collections.Counter()
for e in evs:
    if e.get("kind") == "tool" and e.get("phase") == "start":
        tools[e.get("tool")] += 1
for t, c in tools.most_common():
    print(f"{c:6d}  {t}")

print("\n=== tool FAILURES (phase=end, ok=false) ===")
fails = collections.Counter()
for e in evs:
    if e.get("kind") == "tool" and e.get("phase") == "end" and e.get("ok") is False:
        fails[e.get("tool")] += 1
for t, c in fails.most_common():
    print(f"{c:6d}  {t}")

print("\n=== turn events ===")
turns = collections.Counter()
for e in evs:
    if e.get("kind") == "turn":
        turns[(e.get("phase"), e.get("status"))] += 1
for k, c in turns.most_common():
    print(f"{c:6d}  turn {k}")

print("\n=== session_keys present ===")
sks = collections.Counter(e.get("session_key") for e in evs if e.get("session_key"))
for k, c in sks.most_common():
    print(f"{c:6d}  {k}")

print("\n=== message/feed events (bot messages) ===")
for e in evs:
    if e.get("kind") == "message":
        bot = e.get("bot", "")
        src = e.get("source", "")
        summ = (e.get("summary") or "")[:120]
        ts = e.get("ts", 0)
        dt = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
        print(f"[{dt:%H:%M:%S}Z] {bot}/{src}: {summ}")

print("\n=== github/feed source counts ===")
srcs = collections.Counter()
for e in evs:
    if e.get("source") == "github" or e.get("bot") == "github":
        srcs[e.get("source", e.get("bot"))] += 1
for s, c in srcs.most_common():
    print(f"{c:6d}  {s}")
