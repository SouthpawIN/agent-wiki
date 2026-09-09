import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"
tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 26 (2026-09-04, n=26). HAND-SPAWNED companion to the cron pass-25 (4 concurrent instances: "
    "anser+senter+hermes crons fired 16:00:36 + this hand-spawn; deduped on sight). Confirms pass-25's core findings "
    "(teknium 17 inline-exec/heredoc gate trips editing vault-live.html with zero progress; teknium doing weaver's "
    "wiki-UI work; reachability 24 pings; 13th double-spawn) and adds four deltas the twin missed: (1) turbofit CI "
    "failed at 14:59:36 CDT this window, NOT 04:49 as pass-25 reported — 26 failures since Sep 3 = a persistent "
    "regression needing an owner; (2) senter STILL hand-polled /tmp/anser-reflect-*.log at 14:09-14:13 AFTER pass-24's "
    "DONE (bridge-DONE consumption still unlanded); (3) teknium's zero-progress is numeric CSS nudging with 0 vision / "
    "0 looker / 19 blind preview reloads — diagnose-first + LOOK-loop gap; (4) 22nd consecutive self-trip live this run "
    "(shell for-loop BLOCKED). No new bot, no SOUL change -> no needs_chris card. Findings: "
    "topics/senter/loops/reflect/2026-09-04-26.md; dedupe-conscious pass-26 block appended to klerik queue."
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
