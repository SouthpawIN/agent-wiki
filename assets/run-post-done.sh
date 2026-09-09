#!/bin/bash
# post a done-line to the senter-bridge feed (token from disk, JSON from a file — no inline bodies for Tirith)
T=$(cat ~/.hermes/senter-bridge/token)
curl -s -X POST "http://127.0.0.1:8643/post?token=$T" -H 'Content-Type: application/json' -H 'Origin: null' --data-binary @"${1:-/tmp/ac-done.json}"
echo
