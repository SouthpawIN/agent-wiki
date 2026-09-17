import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"

tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 15 (2026-09-04, n=15). Triple-spawn recovery: anser cron 3ef388cb08b0 + senter cron "
    "c377932f3933 fired 00:00:26/27 (5th consecutive double-spawn) and the senter-cron-spawned instance was "
    "INTERRUPTED mid-API-call, orphaning a queue reference to a nonexistent findings file; senter hand-spawned this "
    "recovery instance 00:07:55. Window 22:02:44->00:11:07 (128 min, 461 fleet events). Headline findings: (1) the "
    "reflect cron is now UNRELIABLE, not just double-spawned — make the run atomic (write file before the long "
    "analysis) + apply the pass-13 one-line dedupe (delete senter c377932f3933); (2) the ~20:40 back-end pivot is "
    "recorded but NOT enforced — bot=hermes kept editing vault-live.html CSS (#fade/#wallBackdrop/mindmap) 22:03-22:18, "
    "~2h after the pivot, all unlogged; (3) rule-14 heredoc-stdin STILL (20x 'python3 - <<EOF' + 2x -c, 0 approvals — "
    "gate blind to stdin spelling). No new bot, no SOUL change -> no needs_chris card. Findings: "
    "topics/senter/loops/reflect/2026-09-04-15.md; complementary block appended to klerik queue (no duplicates of the "
    "sibling's escalation block)."
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
