import json
from datetime import datetime, timezone, timedelta
from collections import Counter

CDT = timezone(timedelta(hours=-5))
cutoff = datetime(2026, 9, 4, 10, 6, 0, tzinfo=CDT).timestamp()
EV = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"

rows = []
with open(EV) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            continue
        ts = o.get("ts")
        if ts is None or ts < cutoff:
            continue
        rows.append(o)

# 1. heredoc transcript appends (cat >> ...01-transcript.md <<EOF)
heredoc_transcript = 0
heredoc_other = 0
python_heredoc = 0
for r in rows:
    s = str(r.get("summary", ""))
    if "01-transcript.md" in s and "<<'EOF'" in s:
        heredoc_transcript += 1
    elif "<<'EOF'" in s or "<<EOF" in s:
        heredoc_other += 1
    if "python3 - <<'EOF'" in s or "python - <<'EOF'" in s:
        python_heredoc += 1
print("heredoc transcript appends (cat >> 01-transcript.md):", heredoc_transcript)
print("other heredoc writes:", heredoc_other)
print("python3 - <<EOF heredoc (vault-live.html edits):", python_heredoc)

# 2. reachability-watch fires (ping 100.84.195.22)
reach = sum(1 for r in rows if "100.84.195.22" in str(r.get("summary","")))
print("reachability-watch ping events:", reach)

# 3. turbofit CI failure
turbofit = sum(1 for r in rows if "Model intelligence workflow run failed" in str(r.get("summary","")))
print("turbofit CI 'workflow run failed':", turbofit)

# 4. gate/approval trips by pattern
from collections import Counter
patterns = Counter()
for r in rows:
    if r.get("kind") == "approval":
        patterns[r.get("pattern_key") or r.get("pattern") or "(none)"] += 1
print("approval events by pattern:", dict(patterns))

# 5. write_file / patch targets (non-reflect)
print("\nwrite_file/patch targets (bot + file):")
for r in rows:
    if r.get("tool") in ("write_file","patch"):
        print(" ", r.get("bot"), r.get("tool"), str(r.get("summary",""))[:90])

# 6. bot event counts
print("\nbot counts:", dict(Counter(r.get("bot") for r in rows)))
