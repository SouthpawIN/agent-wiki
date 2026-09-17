import json, urllib.request, os

TOKEN = open(os.path.expanduser("~/.hermes/senter-bridge/token")).read().strip()
url = "http://127.0.0.1:8643/post?token=" + TOKEN
text = ("DONE - REFLECT pass 23 (2026-09-04-23.md): 1050 events / ~2h scanned (10:06->12:04 CDT). "
        "Detector 3 fired via a NEW actor - the ANSER INTERVIEW task tripped 3 gate patterns "
        "(analysis_incomplete, stop/restart launchd, pipe_to_interpreter -> BLOCKED timeout 11:45:10); "
        "11th consecutive double-spawn (senter c377932f3933 + anser 3ef388cb08b0); reachability-watch + "
        "GitHub/turbofit feed noise unchanged. Routed 5 refinements to klerik queue. "
        "No new bot / no SOUL change -> no needs_chris card.")
body = json.dumps({"bot": "anser", "text": text, "status": "done"}).encode()
req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=10) as r:
    print("HTTP", r.status)
    print(r.read().decode())
