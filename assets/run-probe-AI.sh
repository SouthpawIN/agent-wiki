#!/bin/bash
# usage: bash assets/run-probe-AI.sh [WxH] [dpr] [shotDir]
cd "$(dirname "$0")/.."
export PATH="$HOME/.hermes/node/bin:$PATH"
PW="$HOME/.hermes/hermes-agent/node_modules/playwright" node assets/probe-AI.js "${1:-1456x914}" "${2:-2}" "${3:-assets/look}"
