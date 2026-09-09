#!/bin/bash
# Retry the animation-row pass for the three fleet pets from their APPROVED base looks.
cd /Users/sovthpaw/Documents/Projects/Projects || exit 1
export HERMES_HOME=/Users/sovthpaw/.hermes/profiles/senter
PY=/Users/sovthpaw/.hermes/hermes-agent/venv/bin/python
IMG=/Users/sovthpaw/.hermes/profiles/senter/cache/images

hatch() {  # bot slug base concept
  "$PY" assets/hatch-pet.py --bot "$1" --slug "$2" --base "$3" --tries 4 "$4" > "/tmp/hatch-$1.log" 2>&1
  echo "$1 exit $?" >> "/tmp/hatch-$1.log"
}

hatch klerik  klerik-octopus "$IMG/nous_gen_20260902_110532_b022af0c.png" "a calm pale-cyan octopus surgeon with tiny round spectacles, one tentacle holding a needle and thread, another a scalpel, the profile factory that stitches other bots" &
hatch anser   anser-goose    "$IMG/nous_gen_20260902_110537_01538543.png" "a stern grey goose auditor with a black bow tie, half-moon reading glasses, holding a clipboard with a red checkmark, the redundancy gatekeeper" &
hatch paladin paladin-knight "$IMG/nous_gen_20260902_110535_ebd945af.png" "a small armored knight in polished silver plate with a white tabard bearing a gold branch sigil, holding a shield and a scroll, the standards keeper" &
wait
for b in klerik anser paladin; do echo "== $b"; grep -E "^\[hatch\]|exit " "/tmp/hatch-$b.log"; done
