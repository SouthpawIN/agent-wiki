#!/bin/bash
# sync-pets.sh — mirror the petdex spritesheets the wiki needs into the vault (file:// page → images must live beside it)
# and publish the bot→pet mapping AS DATA (assets/pets/map.json). Idempotent: copies only when missing/changed, rewrites
# map.json only when its content changed. Re-run whenever a profile gains a `pet: {slug: …}` or a pet is (re)hatched.
#
#   bash assets/sync-pets.sh            # sync + report
#   bash assets/sync-pets.sh --dry      # report only
#
# Mapping rule (WEAVER v14.77): ~/.hermes/profiles/<bot>/config.yaml `pet: { slug: X }` wins; a profile without one falls
# back to the first ~/.hermes/pets/<slug>/ whose slug starts with the bot name (senter→senter-owl, klerik→klerik-stitcher,
# anser→anser-goose, paladin→paladin-knight, looker→looker, weaver→weaver). No table is hand-typed anywhere.
# Sheet geometry comes from hermes-agent/agent/pet/constants.py (CODEX_STATE_ROWS: 8 cols × 9 rows of 192×208; row order
# idle, running-right, running-left, waving, jumping, failed, waiting, running, review). Frames per row: pet.json
# framesPerState when present, else 8.
set -u
HH="${HERMES_HOME_ROOT:-$HOME/.hermes}"
PETS="$HH/pets"; PROFILES="$HH/profiles"
VAULT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$VAULT/assets/pets"; MAP="$OUT/map.json"
DRY=0; [ "${1:-}" = "--dry" ] && DRY=1
mkdir -p "$OUT"

copied=0; same=0; bots_json=""; pets_json=""; NEED=""   # NEED = newline list of slugs (macOS bash 3: no assoc arrays)
for pdir in "$PROFILES"/*/; do
  bot="$(basename "$pdir")"
  [ -f "$pdir/SOUL.md" ] || [ -f "$pdir/config.yaml" ] || continue
  slug=""
  if [ -f "$pdir/config.yaml" ]; then
    slug="$(awk '/^  pet:/{f=1;next} f&&/^  [A-Za-z_]/{f=0} f&&/^ *slug:/{print $2; exit}' "$pdir/config.yaml" | tr -d '"'"'")"
  fi
  if [ -z "$slug" ] || [ ! -f "$PETS/$slug/spritesheet.webp" ]; then
    slug=""
    for cand in "$PETS/$bot"*/; do
      [ -f "$cand/spritesheet.webp" ] || continue
      slug="$(basename "$cand")"; break
    done
  fi
  [ -z "$slug" ] && { echo "  $bot → (no pet)"; continue; }
  echo "  $bot → $slug"
  NEED="$NEED$slug
"
  bots_json="$bots_json${bots_json:+,}\"$bot\":\"$slug\""
done

for slug in $(printf '%s' "$NEED" | sort -u); do
  src="$PETS/$slug"; dst="$OUT/$slug"
  frames="$(grep -o '"framesPerState"[[:space:]]*:[[:space:]]*[0-9]*' "$src/pet.json" 2>/dev/null | grep -o '[0-9]*$')"
  [ -z "$frames" ] && frames=8
  pets_json="$pets_json${pets_json:+,}\"$slug\":{\"frames\":$frames}"
  for f in spritesheet.webp pet.json; do
    if [ -f "$dst/$f" ] && cmp -s "$src/$f" "$dst/$f"; then same=$((same+1)); continue; fi
    if [ $DRY = 0 ]; then mkdir -p "$dst"; cp "$src/$f" "$dst/$f"; fi
    copied=$((copied+1))
  done
done

# sorted bots for a stable file (idempotent rewrite check)
bots_sorted="$(printf '%s' "$bots_json" | tr ',' '\n' | sort | paste -sd, -)"
pets_sorted="$(printf '%s' "$pets_json" | tr ',' '\n' | sort | paste -sd, -)"
body="{\"frame\":{\"w\":192,\"h\":208,\"cols\":8},\"rows\":[\"idle\",\"running-right\",\"running-left\",\"waving\",\"jumping\",\"failed\",\"waiting\",\"running\",\"review\"],\"run\":\"running\",\"bots\":{$bots_sorted},\"pets\":{$pets_sorted}}"
if [ $DRY = 0 ]; then
  if [ -f "$MAP" ] && [ "$(cat "$MAP")" = "$body" ]; then echo "map.json unchanged"; else printf '%s\n' "$body" > "$MAP"; printf '%s' "$(cat "$MAP")" > "$MAP"; echo "map.json written"; fi
fi
echo "pets: copied $copied file(s), $same already current → $OUT"
