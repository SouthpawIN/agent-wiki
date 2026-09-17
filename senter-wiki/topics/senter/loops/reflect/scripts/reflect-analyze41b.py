#!/usr/bin/env python3
"""REFLECT pass-41 analysis part 2: messages, inline-exec, file-edit churn, .system files."""
import json, os, glob, datetime, re
from collections import Counter, defaultdict

EVENTS = os.path.expanduser("~/.hermes/senter-bridge/events.jsonl")
BOUNDARY = 1788642154.8788843
ROOT = "/Users/sovthpaw/Documents/Projects/Projects"

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

print("=" * 80)
print("ALL message-kind events (bot -> bot / chris)")
print("=" * 80)
for e in events:
    if e.get("kind") == "message":
        s = str(e.get("summary", ""))
        print(f"[{iso(e['ts'])}] {e.get('bot')} :: {s}")
        print()

# Inline-exec / heredoc family counts
print("=" * 80)
print("INLINE-EXEC / HEREDOC family (terminal tool) — detector 3 signal")
print("=" * 80)
pat_heredoc = re.compile(r"<<['\"]?EOF")
pat_pyc = re.compile(r"python3?\s+-c")
pat_pipe_py = re.compile(r"\|\s*python")
pat_cat_pipe = re.compile(r"cat\s+[^|]+\|\s*python")
counts = Counter()
examples = defaultdict(list)
for e in events:
    if e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = str(e.get("summary", ""))
        if pat_heredoc.search(s):
            counts["heredoc <<EOF"] += 1
            examples["heredoc <<EOF"].append((iso(e['ts']), e.get('bot')))
        if pat_pyc.search(s):
            counts["python -c"] += 1
            examples["python -c"].append((iso(e['ts']), e.get('bot')))
        if pat_pipe_py.search(s):
            counts["| python (pipe to interpreter)"] += 1
            examples["| python"].append((iso(e['ts']), e.get('bot')))
        if pat_cat_pipe.search(s):
            counts["cat .. | python"] += 1
for k, c in counts.most_common():
    print(f"  {k}: {c}")
    for t, b in examples[k][:12]:
        print(f"      {t} {b}")
print()

# vault-live.html edits (which regions)
print("=" * 80)
print("vault-live.html / server.py / *.py edits via terminal (heredoc targets)")
print("=" * 80)
vault_edits = []
for e in events:
    if e.get("kind") == "tool" and e.get("tool") == "terminal":
        s = str(e.get("summary", ""))
        m = re.search(r"p=['\"]([^'\"]+)['\"]", s)
        target = m.group(1) if m else None
        if target and any(x in target for x in ["vault-live.html", "server.py", "watcher", "topic-wiki", "topic-worker", "umbrella"]):
            vault_edits.append((iso(e['ts']), e.get('bot'), target, s[:120]))
for t, b, target, s in vault_edits:
    print(f"  {t} {b} target={target} :: {s}")
print(f"TOTAL file-edit terminal calls: {len(vault_edits)}")

# approval events
print()
print("=" * 80)
print("approval-kind events (with timing)")
print("=" * 80)
appr = [e for e in events if e.get("kind") == "approval"]
print(f"total approval events: {len(appr)}")
for e in appr:
    print(f"  {iso(e['ts'])} bot={e.get('bot')}")

# .system files under topics (hidden dirs)
print()
print("=" * 80)
print(".system/queue.md + session.md files, mtime newer than boundary?")
print("=" * 80)
sysfiles = []
for d in glob.glob(os.path.join(ROOT, "topics", "*", ".system")):
    for name in ["queue.md", "session.md", "injections.md"]:
        p = os.path.join(d, name)
        if os.path.exists(p):
            mt = os.path.getmtime(p)
            sysfiles.append((mt, p))
sysfiles.sort(reverse=True)
for mt, p in sysfiles:
    flag = "NEW" if mt >= BOUNDARY else "old"
    print(f"  [{iso(mt)}] {flag:3} {p.replace(ROOT+'/', '')}")
