#!/bin/bash
# run-probe-AD.sh — node --check the inline <script>, then run probe-AD at a viewport, writing LOOK shots
cd ~/Documents/Projects/Projects || exit 1
export PW=~/.hermes/hermes-agent/node_modules/playwright
N=~/.hermes/node/bin/node
VP=${1:-1456x914}; SHOTS=${2:-assets/look}
awk '/<script>/{f=1;next} /<\/script>/{f=0} f' vault-live.html > /tmp/vault-script.js
$N --check /tmp/vault-script.js && echo "node --check OK" || { echo "SYNTAX FAIL"; exit 1; }
wc -c vault-live.html
grep -c 'id="topnav"\|id="view-feed"\|FLEET STREAM' vault-live.html
$N assets/probe-AD.js "$VP" "$SHOTS" > /tmp/probe-AD-$VP.json 2>&1
tr -d '\n' < /tmp/probe-AD-$VP.json | sed 's/  */ /g'
echo
