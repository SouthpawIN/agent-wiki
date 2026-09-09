#!/bin/bash
# AH: pixel-scan the live Hermes window capture — how much of the preview pane is non-black (wall bleeding through)?
cd ~/Documents/Projects/Projects
~/.hermes/hermes-agent/venv/bin/python assets/ah-pixscan.py "$1"
