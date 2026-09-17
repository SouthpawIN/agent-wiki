#!/usr/bin/env python
"""scan-AE.py — pixel-scan a probe-AE shot for the TRUE cap-height center of a nav tab and the ink centers of ‹‹ ▸ ›› and ⚙.
usage: python assets/scan-AE.py shot.png geometry.json   (geometry.json = probe-AE.js stdout JSON)
Ink = any pixel with all channels > 60 (dim/white lettering on black); gold guides are excluded by requiring blue > 90 too.
"""
import sys, json
from PIL import Image

shot, geo = sys.argv[1], json.load(open(sys.argv[2]))
im = Image.open(shot).convert('RGB'); W, H = im.size
px = im.load()
def ink_rows(box, pad=0, ymin=None, ymax=None):
    l, t, r, b = int(box['l'])-pad, int(box['t'])-pad, int(box['r'])+pad, int(box['b'])+pad
    if ymin is not None: t = max(t, ymin)
    if ymax is not None: b = min(b, ymax)
    rows = []
    for y in range(max(0,t), min(H,b)):
        n = 0
        for x in range(max(0,l), min(W,r)):
            R,G,B = px[x,y]
            if R > 60 and G > 60 and B > 90: n += 1
        if n: rows.append(y)
    return (rows[0], rows[-1]) if rows else None

out = {}
# non-active tab (no underline): pick FEED unless it's on, else first non-on
tab = next((t for t in geo['tabs'] if not t['on'] and t['v'] != 'wiki'), geo['tabs'][0])
tr = ink_rows(tab['ink'], pad=2)
out['tab'] = tab['v']; out['tabInkRows'] = tr; out['tabCapCenter'] = (tr[0]+tr[1])/2 if tr else None
# play circle ring: scan the play box (the ring is the outer ink)
pr = ink_rows(geo['play'], pad=2); out['playInkRows'] = pr; out['playCenter'] = (pr[0]+pr[1])/2 if pr else None
sr = ink_rows(geo['prevInk'], pad=3); out['prevInkRows'] = sr; out['prevCenter'] = (sr[0]+sr[1])/2 if sr else None
nr = ink_rows(geo['next'], pad=0); out['nextInkRows'] = nr; out['nextCenter'] = (nr[0]+nr[1])/2 if nr else None
gr = ink_rows(geo['gearInk'], pad=4); out['gearInkRows'] = gr; out['gearCenter'] = (gr[0]+gr[1])/2 if gr else None
# artist line ink top vs play ring bottom
ar = ink_rows(geo['mTitleInk'], pad=2); out['artistInkRows'] = ar
if ar and pr: out['artistGapInk'] = ar[0] - pr[1]
c = out['tabCapCenter']
if c is not None:
    out['dPlay'] = (out['playCenter'] - c) if out['playCenter'] is not None else None
    out['dPrev'] = (out['prevCenter'] - c) if out['prevCenter'] is not None else None
    out['dNext'] = (out['nextCenter'] - c) if out['nextCenter'] is not None else None
    out['dGear'] = (out['gearCenter'] - c) if out['gearCenter'] is not None else None
    out['AE_ok'] = all(v is not None and abs(v) <= 1 for v in [out['dPlay'], out['dGear']])
out['AB_ok'] = out.get('artistGapInk') is not None and out['artistGapInk'] >= 8
print(json.dumps(out, indent=1))
