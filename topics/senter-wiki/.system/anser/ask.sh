#!/bin/bash
# ask.sh <turn-number> "<area>" "<question>"  — runs one anser turn, appends verbatim to 01-transcript.md
N="$1"; AREA="$2"; Q="$3"
T=/Users/sovthpaw/Documents/Projects/Projects/topics/senter-wiki/.system/anser/01-transcript.md
PRE="Plain text only, no MEDIA attachments, no TL;DR format — this is an internal fleet conversation, not Discord. You are being interviewed by the default Hermes profile on behalf of Chris about what is ALREADY built into Hermes that the Senter wiki should use instead of custom code. Be precise: name the exact CLI subcommand / tool / plugin, say how to verify it exists on this install, give a verdict REPLACE / WRAP / KEEP-CUSTOM with one-sentence why, and the first concrete read-only command to try. If you are not sure something exists, say so — do not guess."
OUT=$(hermes -p anser -z "$PRE

$Q" --no-restore-cwd 2>&1)
{
  echo ""
  echo "## Turn $N — $AREA"
  echo ""
  echo "**Q (to anser):**"
  echo ""
  echo "$Q"
  echo ""
  echo "**A (anser, verbatim):**"
  echo ""
  echo "$OUT"
  echo ""
} >> "$T"
echo "$OUT"
