#!/bin/bash
# AI proof pipeline: probe (shots) + pixel compare against the real desktop wallpaper window.
# usage: bash assets/run-compare-AI.sh [WxH] [dpr]
cd "$(dirname "$0")/.."
VP="${1:-1456x914}"; DPR="${2:-2}"; TAG="${VP}@${DPR}"
bash assets/run-probe-AI.sh "$VP" "$DPR" assets/look || exit 1
# capture the Dock's Wallpaper window (unobstructed desktop image) — window id from list-windows.swift
WID=$(swift assets/list-windows.swift 2>/dev/null | awk -F'\t' '$3=="Dock" && $4 ~ /^Wallpaper-/ {print $1; exit}')
if [ -n "$WID" ]; then screencapture -x -l "$WID" assets/look/AI-desktop-wallpaper-3024x1964.png; echo "desktop wallpaper window $WID captured"; else echo "no Wallpaper window found; using existing capture"; fi
"$HOME/.hermes/hermes-agent/venv/bin/python" assets/compare-AI.py "assets/look/AI-wallonly-$TAG.png" assets/look/AI-desktop-wallpaper-3024x1964.png "assets/look/AI-wiki-$TAG.png" "assets/look/AI-sidebyside-$TAG.png"
