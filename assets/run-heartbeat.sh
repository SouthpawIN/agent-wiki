#!/bin/bash
# touch claim heartbeats every 60s while a weaver instance works; exits when the claim dir is gone
# usage: bash assets/run-heartbeat.sh AE AB
C="$HOME/Documents/Projects/Projects/topics/senter-wiki/.system/claims"
while :; do
  alive=0
  for I in "$@"; do
    if [ -d "$C/$I" ]; then touch "$C/$I/heartbeat"; alive=1; fi
  done
  [ "$alive" = 1 ] || exit 0
  sleep 60
done
