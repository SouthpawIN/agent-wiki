#!/usr/bin/env python3
"""Gold audit: where in a frame are WARM pixels (R-B > thr and R>G>B)? Reports fraction + bbox + centroid, and the mean of those pixels.
usage: gold-AI.py <png> [x y w h] [thr=30]"""
import sys
import numpy as np
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
if len(sys.argv) >= 6:
    x, y, w, h = map(int, sys.argv[2:6]); im = im.crop((x, y, x + w, y + h))
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 30
a = np.asarray(im, dtype=int); R, G, B = a[..., 0], a[..., 1], a[..., 2]
warm = (R - B > thr) & (R >= G) & (G >= B)
n = warm.sum(); H, W = warm.shape
print(f'frame {W}x{H}: warm px {n} = {n / warm.size * 100:.3f}%')
if n:
    ys, xs = np.nonzero(warm)
    print(f'  bbox x {xs.min()}–{xs.max()} y {ys.min()}–{ys.max()}  centroid ({xs.mean() / W:.2f},{ys.mean() / H:.2f}) of frame')
    m = a[warm].mean(axis=0); print(f'  mean warm RGB ({m[0]:.0f},{m[1]:.0f},{m[2]:.0f})')
    # coarse heat map 8x6
    gy, gx = H // 6, W // 8
    for j in range(6):
        print('  ' + ' '.join(f'{warm[j*gy:(j+1)*gy, i*gx:(i+1)*gx].mean()*100:5.1f}' for i in range(8)))
