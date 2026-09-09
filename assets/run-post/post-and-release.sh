#!/bin/bash
# Post a done-line JSON file to the senter bridge, then release a claim dir.
# Usage: bash assets/run-post/post-and-release.sh <json-file> <claim-item> "<result line>"
set -e
cd "$(dirname "$0")/../.."
TOK=$(cat ~/.hermes/senter-bridge/token)
curl -s -X POST "http://127.0.0.1:8643/post?token=$TOK" -H 'Content-Type: application/json' --data-binary @"$1"
echo
C=topics/senter-wiki/.system/claims/$2
if [ -d "$C" ]; then echo "$3" > "$C/result"; rm -r "$C"; echo "released $2"; fi
