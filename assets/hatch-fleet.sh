#!/bin/bash
# Fleet pets v2.1 — same dark-fantasy concepts, NARROW silhouettes (the row slicer fails on wide/split shapes).
cd /Users/sovthpaw/Documents/Projects/Projects || exit 1
export HERMES_HOME=/Users/sovthpaw/.hermes/profiles/senter
PY=/Users/sovthpaw/.hermes/hermes-agent/venv/bin/python

hatch() { "$PY" assets/hatch-pet.py --bot "$1" --slug "$2" --tries 4 "$3" > "/tmp/hatch-$1.log" 2>&1; echo "$1 exit $?" >> "/tmp/hatch-$1.log"; }

# klerik — hooded stitcher: cloak hangs straight down (no flare), grimoire tucked under one arm, needle held close to the chest
hatch klerik klerik-stitcher "a small hooded anime figure in a narrow black cloak that hangs straight down to the feet, two glowing pale-cyan eyes in the hood's shadow, silver stitches across the chest, a small grimoire tucked tightly under one arm, a bone needle with glowing cyan thread held close against the chest, compact upright silhouette, arms kept in, dark fantasy" &

# anser — raven warden: coat closed and narrow, ledger chained at the hip, scale hung from the belt (nothing held out)
hatch anser anser-warden "a slim upright anime raven in a long narrow grey plague-doctor coat buttoned closed, white beaked mask with one glowing amber lens, a small chained ledger hanging flat at the hip, a tiny brass balance scale hanging from the belt, arms folded inside the coat, compact vertical silhouette, dark fantasy judge" &

wait
for b in klerik anser; do echo "== $b"; grep -E "^\[hatch\]|exit " "/tmp/hatch-$b.log"; done
