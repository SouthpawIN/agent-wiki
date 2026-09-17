#!/usr/bin/env python3
"""Find the most colorful (saturated) region of the wall-only wiki frame — for the nebula crop pair. Prints fx,fy,fw,fh."""
import sys
import numpy as np
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB'); x = np.asarray(im, dtype=float); H, W, _ = x.shape
sat = x.max(axis=2) - x.min(axis=2)
best = None
gw, gh = int(W * .25), int(H * .3)
for gy in range(0, H - gh, gh // 4):
    for gx in range(0, W - gw, gw // 4):
        v = sat[gy:gy + gh, gx:gx + gw].mean()
        if best is None or v > best[0]: best = (v, gx, gy)
v, gx, gy = best
print(f'{gx/W:.3f},{gy/H:.3f},{gw/W:.3f},{gh/H:.3f}  mean sat {v:.1f}')
