import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"

tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 14 (2026-09-03, n=14). This instance is the 2nd concurrent reflect instance this cadence "
    "(the 4th consecutive double-spawn: senter cron c377932f3933 + anser cron 3ef388cb08b0 both fired 22:00:16, "
    "plus a senter hand-spawn). Headline: Chris's ~20:40 ruling 'the UI is at a good enough spot that we can start "
    "working on the back end' — UI MVP DECLARED DONE, fleet pivots to the back end (landed only in log.md; Ideas.md "
    "still unchanged). This instance adds three findings the sibling pass-14 missed: (1) senter-reachability-watch "
    "cron d72764243822 is the dominant poll-based noise (22 fires/~46 ping+tailscale events, push-not-poll violation); "
    "(2) rule-14 morphed to heredoc-stdin 'python3 - <<EOF' — 0 gate trips is a red herring, the -c/-e gate can't see "
    "the stdin spelling; (3) default profile's memory tool failing 6/18 calls (ok=False). No new bot, no SOUL change -> "
    "no needs_chris card. Findings: topics/senter/loops/reflect/2026-09-03-14.md; routed to klerik queue (no duplicates)."
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
