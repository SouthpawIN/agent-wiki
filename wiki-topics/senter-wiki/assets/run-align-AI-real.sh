#!/bin/bash
# usage: bash assets/run-align-AI-real.sh [paneX paneY paneW paneH device px]  (uses /tmp/hermes-win.png from run-compare-AI-real.sh)
cd "$(dirname "$0")/.."
# REGION default: right band between hero line and stream cards = mostly clean wall
REGION="${REGION:-.55,.09,.40,.22}" "$HOME/.hermes/hermes-agent/venv/bin/python" assets/align-AI-real.py /tmp/hermes-win.png assets/look/AI-desktop-wallpaper-3024x1964.png "${1:-666}" "${2:-190}" "${3:-2302}" "${4:-1668}"
