#!/usr/bin/env python3
"""Chroma check: are the nebula hues the same on both sides? Compare mean (R-G, B-G) over saturated pixels only. usage: chroma-AI.py <wiki-wallonly.png> <desk.png> [FIT]"""
import sys, os
import numpy as np
from PIL import Image
A = Image.open(sys.argv[1]).convert('RGB'); D = Image.open(sys.argv[2]).convert('RGB')
FIT = sys.argv[3] if len(sys.argv) > 3 else 'contain'
aw, ah = A.size; dw, dh = D.size
s = (min if FIT == 'contain' else max)(aw / dw, ah / dh)
Ds = D.resize((round(dw * s), round(dh * s)), Image.LANCZOS)
x0, y0 = (aw - Ds.width) // 2, (ah - Ds.height) // 2
a = np.asarray(A, dtype=float)[max(y0,0):max(y0,0)+Ds.height, max(x0,0):max(x0,0)+Ds.width]
d = np.asarray(Ds, dtype=float)[:a.shape[0], :a.shape[1]]
def chroma(x, label):
    sat = x.max(axis=2) - x.min(axis=2)
    m = sat > 25
    rg = (x[..., 0] - x[..., 1])[m].mean(); bg = (x[..., 2] - x[..., 1])[m].mean()
    hue = np.degrees(np.arctan2(bg, rg))
    print(f'{label}: saturated px {m.mean()*100:.1f}%  mean R-G {rg:+.2f}  B-G {bg:+.2f}  hue angle {hue:.1f}°  (gold ≈ R-G>0,B-G<0; purple/teal ≈ B-G>0)')
    return rg, bg
r1 = chroma(d, 'desktop'); r2 = chroma(a, 'wiki   ')
print(f'delta R-G {r2[0]-r1[0]:+.2f}, B-G {r2[1]-r1[1]:+.2f}  (|delta| < 2 ⇒ same hue within JPEG tolerance)')
