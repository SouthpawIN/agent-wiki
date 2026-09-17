#!/bin/bash
# run-ledgers.sh — static + live ledgers at the three house viewports
cd ~/Documents/Projects/Projects || exit 1
export PW=~/.hermes/hermes-agent/node_modules/playwright
N=~/.hermes/node/bin/node
echo "== static"; $N assets/verify-wiki.js 2>&1 | tail -3
for vp in 1456x914 1040x880 1136x850; do
  echo "== live $vp"; $N assets/verify-wiki-live.js --vp $vp > /tmp/ledger-$vp.txt 2>&1; grep -E "FAIL|passed" /tmp/ledger-$vp.txt
done
