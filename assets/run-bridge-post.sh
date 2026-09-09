#!/bin/bash
# post a bot done-line to the senter-bridge feed: bash assets/run-bridge-post.sh /path/to/body.json
T=$(cat ~/.hermes/senter-bridge/token)
curl -s -X POST "http://127.0.0.1:8643/post?token=$T" -H 'Content-Type: application/json' -H 'Origin: null' --data-binary @"$1"
echo
