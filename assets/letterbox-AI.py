#!/usr/bin/env python3
"""Detect the wiki pane's box inside a Retina Hermes window capture + the backdrop's letterbox, by scanning for the pane's black band vs neighbours.
Prints pane bounds guess and the columns where the wallpaper (non-#060606) starts/ends on a mid-row."""
import sys
import numpy as np
from PIL import Image
im = np.asarray(Image.open(sys.argv[1]).convert('RGB'), dtype=int); H, W, _ = im.shape
x0, y0, pw, ph = map(int, sys.argv[2:6])
pane = im[y0:y0 + ph, x0:x0 + pw]
# rows/cols whose pixels are (near) page black #060606 = letterbox / chrome
isblk = (np.abs(pane - 6).sum(axis=2) <= 6)
colfrac = isblk.mean(axis=0); rowfrac = isblk.mean(axis=1)
def runs(frac, thr=.97):
    out = []; start = None
    for i, v in enumerate(frac):
        if v >= thr and start is None: start = i
        if (v < thr or i == len(frac) - 1) and start is not None:
            end = i if v < thr else i + 1
            if end - start >= 6: out.append((start, end))
            start = None
    return out
print('pane', pw, 'x', ph, 'at', x0, y0)
print('all-black column runs (letterbox / gutters):', runs(colfrac))
print('all-black row runs:', runs(rowfrac))
