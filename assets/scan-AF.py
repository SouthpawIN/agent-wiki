#!/usr/bin/env python
# scan-AF.py — find gold guide columns/row in a shot, then white-ink extents near them. usage: python scan-AF.py shot.png
import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB'); W,H=im.size; px=im.load()
gold=lambda p: p[0]>200 and p[1]>190 and p[2]<140
ink=lambda p: p[0]>60 and p[1]>60 and p[2]>90 and not gold(p)
cols=[x for x in range(W) if sum(gold(px[x,y]) for y in range(0,200))>150]
rows=[y for y in range(200) if sum(gold(px[x,y]) for x in range(0,W,4))>W/8]
print('gold cols',cols,'gold row',rows)
# ink column extents in y band 95..122 (nav/media row), between x=600..W
band=range(95,122)
inkcols=[x for x in range(600,W) if any(ink(px[x,y]) for y in band)]
# group into runs
runs=[];s=None
for x in inkcols:
    if s is None: s=p=x
    elif x==p+1: p=x
    else: runs.append((s,p)); s=p=x
if s is not None: runs.append((s,p))
print('ink runs x (row band 95-122, x>600):',runs)
