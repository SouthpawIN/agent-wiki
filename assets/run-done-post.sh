#!/bin/bash
# post a done-line to the senter-bridge feed. usage: bash assets/run-done-post.sh /path/to/post.json
T=$(cat "$HOME/.hermes/senter-bridge/token" 2>/dev/null)
[ -n "$T" ] || { echo "no bridge token"; exit 1; }
curl -s -m 5 -X POST "http://127.0.0.1:8643/post?token=$T" -H "Content-Type: application/json" -H "Origin: null" --data-binary @"$1"; echo
