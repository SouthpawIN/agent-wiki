#!/usr/bin/env python3
"""Measure the two halves of a crop-pair image (left A | 16px white gutter | right B): mean RGB, hue of saturated px, Laplacian sharpness."""
import sys
import numpy as np
from PIL import Image, ImageFilter
im = Image.open(sys.argv[1]).convert('RGB'); W, H = im.size; w = (W - 16) // 2
A = im.crop((0, 40, w, H)); B = im.crop((w + 16, 40, W, H))
def stats(img, label):
    x = np.asarray(img, dtype=float)
    m = x.reshape(-1, 3).mean(axis=0)
    sat = x.max(axis=2) - x.min(axis=2); msk = sat > 25
    rg = (x[..., 0] - x[..., 1])[msk].mean() if msk.any() else 0; bg = (x[..., 2] - x[..., 1])[msk].mean() if msk.any() else 0
    lap = np.asarray(img.convert('L').filter(ImageFilter.FIND_EDGES), dtype=float).var()
    print(f'{label}: mean RGB ({m[0]:.1f},{m[1]:.1f},{m[2]:.1f})  luma {0.299*m[0]+0.587*m[1]+0.114*m[2]:.1f}  saturated {msk.mean()*100:.1f}%  R-G {rg:+.1f} B-G {bg:+.1f}  edge-var(sharpness) {lap:.1f}')
stats(A, 'A desktop '); stats(B, 'B wiki    ')
