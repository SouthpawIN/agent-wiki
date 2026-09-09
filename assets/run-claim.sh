#!/bin/bash
# atomic claim (CLAIM v2): mkdir is the lock. usage: bash assets/run-claim.sh <ITEM> <BOT>
C="$HOME/Documents/Projects/Projects/topics/senter-wiki/.system/claims"
ITEM="$1"; BOT="${2:-weaver}"
if mkdir "$C/$ITEM" 2>/dev/null; then
  echo "$BOT $$ $(date -u +%FT%TZ)" > "$C/$ITEM/owner"
  touch "$C/$ITEM/heartbeat"
  echo "CLAIMED $ITEM by $BOT $(date -u +%FT%TZ)"
else
  echo "EEXIST $ITEM — owner: $(cat "$C/$ITEM/owner" 2>/dev/null)"
  exit 1
fi
