#!/bin/bash
# run-probe-AE.sh — geometry JSON + full-frame shot + pixel scan. usage: bash assets/run-probe-AE.sh [WxH] [tag] [guideY]
cd "$(dirname "$0")/.." || exit 1
VP="${1:-1456x914}"; TAG="${2:-AE}"; GY="${3:-}"
SHOT="assets/look/${TAG}-${VP}.png"; JSON="/tmp/probe-AE-${TAG}-${VP}.json"
export PW="$HOME/.hermes/hermes-agent/node_modules/playwright"
NODE="$HOME/.hermes/node/bin/node"; [ -x "$NODE" ] || NODE=node
if [ -n "$GY" ]; then
  "$NODE" assets/probe-AE.js "$VP" "$SHOT" "$GY" > "$JSON.raw" 2>&1
else
  "$NODE" assets/probe-AE.js "$VP" "$SHOT" > "$JSON.raw" 2>&1
fi
# first JSON object only (probe prints JSON then 'errors:' + 'shot' lines)
awk 'BEGIN{p=1} /^errors:/{p=0} p' "$JSON.raw" > "$JSON"
grep -E '^(errors|shot)' "$JSON.raw"
"$HOME/.hermes/hermes-agent/venv/bin/python" assets/scan-AE.py "$SHOT" "$JSON"
