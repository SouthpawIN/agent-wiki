#!/bin/bash
# finish-AG.sh — queue DONE line, bridge done-post, claim release. Plain bash (Tirith-safe).
cd ~/Documents/Projects/Projects || exit 1
TS=$(date -u +%FT%TZ)
echo "DONE AG weaver $TS — v14.58 comments (SETTINGS at v14.63 by siblings): 5 setIntervals → 0; scan-topics.py --watch = FSEvents + what:[…] (venv python, pid 58222); touch profile → BOTS 0.6s; reconnect backoff ≤5s = the one // fallback:; probe-ag.js 24/24 ×2 (session.md)" >> topics/senter-wiki/.system/queue.md
TOK=$(cat ~/.hermes/senter-bridge/token)
curl -s -X POST "http://127.0.0.1:8643/post?token=$TOK" -H 'Content-Type: application/json' -H 'Origin: null' --data-binary @/tmp/ag-done.json
echo
echo "done AG $TS" > topics/senter-wiki/.system/claims/AG/result
rm -r topics/senter-wiki/.system/claims/AG
ls topics/senter-wiki/.system/claims/
tail -1 topics/senter-wiki/.system/queue.md | cut -c1-100
