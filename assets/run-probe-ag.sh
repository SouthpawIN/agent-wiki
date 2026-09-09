#!/bin/bash
# run-probe-ag.sh — AG (no timers) probe: node --check on the extracted <script>, then probe-ag.js at the given viewport.
cd ~/Documents/Projects/Projects || exit 1
export PW=~/.hermes/hermes-agent/node_modules/playwright
N=~/.hermes/node/bin/node
VP=${1:-1456x914}; SHOT=${2:-assets/look}
$N assets/extract-script.js vault-live.html /tmp/vl-script.js 2>/dev/null || awk '/<script>/{f=1;next}/<\/script>/{f=0}f' vault-live.html > /tmp/vl-script.js
$N --check /tmp/vl-script.js && echo "node --check: clean" || { echo "node --check: FAILED"; exit 1; }
echo "bytes: $(wc -c < vault-live.html)"
$N assets/probe-ag.js --vp "$VP" --shot "$SHOT"
