#!/usr/bin/env python3
"""REFLECT pass-41: post needs_chris card for the two NEW BOT proposals."""
import json, urllib.request, os

TOKEN = open(os.path.expanduser("~/.hermes/senter-bridge/token")).read().strip()
url = "http://127.0.0.1:8643/post?token=" + TOKEN
text = ("NEEDS-CHRIS \u2014 senter-bot (8 approved skills in 'senter', no owning agent) "
        "+ senter-wiki-bot (4 approved skills in 'senter-wiki', no owning agent) "
        "\u2014 umbrella auto-proposed; approve klerik spawn (via bot-card-approval-spawn).")
body = json.dumps({"bot": "anser", "text": text, "status": "needs_chris"}).encode()
req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        print("HTTP", r.status)
        print(r.read().decode())
except Exception as e:
    print("ERROR", type(e).__name__, str(e))
