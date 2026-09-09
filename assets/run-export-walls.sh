#!/bin/bash
# AI: re-export every wall from Chris's ORIGINAL PNGs (~/Pictures/HermesWalls, 6048x3928) at 3024px wide
# = 1x device width of his 3024x1964 Retina panel, JPEG q92 → assets/walls/<name>@2x.jpg (picked when devicePixelRatio>1).
# The existing <name>.jpg (2560 wide, q82) stays as the dpr<=1 asset. Never reference the 22-34 MB PNGs from the page.
# usage: bash assets/run-export-walls.sh [width=3024] [quality=92]
set -e
SRC="$HOME/Pictures/HermesWalls"
DST="$HOME/Documents/Projects/Projects/assets/walls"
W="${1:-3024}"; Q="${2:-92}"
mkdir -p "$DST"
for p in "$SRC"/*.png; do
  n="$(basename "${p%.png}")"
  out="$DST/$n@2x.jpg"
  sips --resampleWidth "$W" -s format jpeg -s formatOptions "$Q" "$p" --out "$out" >/dev/null
  echo "$n@2x.jpg $(sips -g pixelWidth -g pixelHeight "$out" | awk '/pixel/{printf "%s ", $2}') $(stat -f %z "$out") bytes"
done
