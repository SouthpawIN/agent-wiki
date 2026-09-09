#!/usr/bin/env bash
# AB pixel scan: for each screen row across the media widget's columns, count white-ish ink pixels (ignoring the gold guide rows).
# usage: bash assets/run-scan-AB.sh <png> <x0> <x1> <y0> <y1>
~/.hermes/hermes-agent/venv/bin/python - "$@" <<'PY'
import sys
from PIL import Image
png,x0,x1,y0,y1=sys.argv[1],*map(int,sys.argv[2:6])
im=Image.open(png).convert('RGB')
for y in range(y0,y1):
    row=[im.getpixel((x,y)) for x in range(x0,x1)]
    gold=sum(1 for r,g,b in row if r>200 and g>180 and b<140)
    ink=sum(1 for r,g,b in row if r>70 and g>70 and b>70 and not(r>200 and g>180 and b<140))
    tag=' GOLD' if gold>20 else ''
    print(f"y={y:4d} ink={ink:3d}{tag}")
PY
