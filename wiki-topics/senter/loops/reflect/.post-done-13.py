import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"

tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 13 (2026-09-03, n=13). This instance is the 2nd concurrent reflect "
    "instance this cadence — the double-spawn itself (detector 4). A sibling already wrote pass 12 "
    "over the same window; pass 13 adds hard cron-level evidence + 2 findings pass 12 missed: "
    "(1) ROOT-CAUSED the double-spawn — TWO cron jobs with IDENTICAL schedule 0 */2 * * * both run "
    "the reflect loop: anser id 3ef388cb08b0 (\"REFLECT loop pass\") + senter id c377932f3933 "
    "(\"anser REFLECT loop\") — fix is one line: delete senter's, keep anser's. "
    "(2) weaver verify-nightly cron in error state (TimeoutError 940s idle vs 600s limit, "
    "failure_streak 1). (3) 12th consecutive reflect self-trip (this instance: python3 -c + "
    "cat | python3 -m json.tool). No new Chris ask, no new bot, no SOUL change -> no needs_chris card. "
    "Findings: topics/senter/loops/reflect/2026-09-03-13.md"
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
