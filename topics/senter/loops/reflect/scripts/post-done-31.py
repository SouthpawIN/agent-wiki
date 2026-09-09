import json, urllib.request, os

TOKEN = open(os.path.expanduser("~/.hermes/senter-bridge/token")).read().strip()
url = "http://127.0.0.1:8643/post?token=" + TOKEN
text = ("DONE - REFLECT pass 31 (2026-09-04-31.md): hand-spawned companion to the cron pass-30. "
        "Window 20:03->22:03 CDT, 353 events. No new patterns; all six detectors silent except "
        "re-counts of already-flagged unlanded items. 26th self-trip (this instance's python3 -c "
        "BLOCKED 22:02:03 + companion's cat|python3 -c 22:02:33). 16th multi-spawn confirmed "
        "(two pass-30/31 instances raced this cadence). No new bot / no SOUL change -> no needs_chris card.")
body = json.dumps({"bot": "anser", "text": text, "status": "done"}).encode()
req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=10) as r:
    print("HTTP", r.status)
    print(r.read().decode())
