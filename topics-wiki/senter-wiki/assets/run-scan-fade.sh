#!/bin/bash
# scan a screenshot column for the fade ramp: prints brightness of the card's left border pixel at y=90..200
cd ~/Documents/Projects/Projects || exit 1
~/.hermes/hermes-agent/venv/bin/python assets/scan-fade.py "$@"
