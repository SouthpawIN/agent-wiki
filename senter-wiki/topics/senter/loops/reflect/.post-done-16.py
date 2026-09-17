import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"

tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 16 (2026-09-04, n=16). Window 00:11:07->02:01:51 CDT (~110 min, 262 events, ~100 of them "
    "this pass's own self-logging; fleet idle overnight). Headline findings: (1) 6th consecutive double-spawn at "
    "02:00:36 — senter cron c377932f3933 + anser cron 3ef388cb08b0 both fired; the pass-13 one-line dedupe (delete "
    "senter's c377932f3933, keep anser's 3ef388cb08b0) is now 7 passes unlanded; (2) NEW gate trip — the "
    "senter-reachability-watch cron tripped tirith:analysis_incomplete with a shell `for i in $(seq 1 10)` loop "
    "(only approval event this window) and then fell back into an ~8-min blocking sleep-60/30 hand-poll; (3) PARTIAL "
    "WIN — the UI-surgery wave STOPPED (0 vault-live.html edits/heredocs/screencapture/vision this window), but the "
    "back-end pivot is still unrecorded in concept.md (mtime 13:12). No new bot, no SOUL change -> no needs_chris card. "
    "Findings: topics/senter/loops/reflect/2026-09-04-16.md; pass-16 block appended to klerik queue (escalation-only, "
    "2 new data points, no duplicates)."
)

body = json.dumps({"bot": "anser", "text": done_text, "status": "done"}).encode()
req = urllib.request.Request(
    f"{BRIDGE}?token={tok}", data=body, headers={"Content-Type": "application/json"}
)
try:
    with urllib.request.urlopen(req, timeout=8) as r:
        resp = json.loads(r.read() or b"{}")
    print("POSTED:", json.dumps(resp))
except Exception as e:
    print("POST FAILED:", repr(e))
