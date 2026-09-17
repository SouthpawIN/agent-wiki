#!/bin/bash
# AI real-window proof: Retina-capture the Hermes window (id 18), crop the wiki pane (device px), compare a clean-wall region
# against the real desktop wallpaper window (Dock 'Wallpaper-…'). Pane bounds from the AX tree: AXWebArea 'Senter Vault — Live' [333,128 1151x834] CSS → ×2 device.
# usage: bash assets/run-compare-AI-real.sh [winId=18] [paneX paneY paneW paneH in device px]
cd "$(dirname "$0")/.."
WIN="${1:-18}"; X="${2:-666}"; Y="${3:-256}"; W="${4:-2302}"; H="${5:-1668}"
screencapture -x -l "$WIN" /tmp/hermes-win.png || exit 1
cp /tmp/hermes-win.png assets/look/AI-realwindow-retina.png
WID=$(swift assets/list-windows.swift 2>/dev/null | awk -F'\t' '$3=="Dock" && $4 ~ /^Wallpaper-/ {print $1; exit}')
[ -n "$WID" ] && screencapture -x -l "$WID" assets/look/AI-desktop-wallpaper-3024x1964.png
"$HOME/.hermes/hermes-agent/venv/bin/python" assets/compare-AI-real.py /tmp/hermes-win.png assets/look/AI-desktop-wallpaper-3024x1964.png "$X" "$Y" "$W" "$H" assets/look/AI-realwindow-vs-desktop-2x.png
