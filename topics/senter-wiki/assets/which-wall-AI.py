#!/usr/bin/env python3
"""Which wall is the live pane showing? For each wall asset: contain-fit into the pane box (like the CSS), dim ×(1-a), then compare against the
live pane over a UI-free region using normalized correlation on L AND chroma similarity (R/B ratio). usage: which-wall-AI.py <hermes-win.png> x y w h [REGION fx,fy,fw,fh]"""
import sys, os, glob
import numpy as np
from PIL import Image
win, x0, y0, pw, ph = sys.argv[1], *map(int, sys.argv[2:6])
fx, fy, fw, fh = map(float, (sys.argv[6] if len(sys.argv) > 6 else '.70,.22,.28,.30').split(','))
pane = Image.open(win).convert('RGB').crop((x0, y0, x0 + pw, y0 + ph))
box = (int(pw * fx), int(ph * fy), int(pw * (fx + fw)), int(ph * (fy + fh)))
P = np.asarray(pane.crop(box), dtype=float)
PL = P.mean(axis=2)
def fit(path):
    D = Image.open(path).convert('RGB'); dw, dh = D.size
    s = min(pw / dw, ph / dh); Ds = D.resize((round(dw * s), round(dh * s)), Image.LANCZOS)
    C = Image.new('RGB', (pw, ph), (6, 6, 6)); C.paste(Ds, ((pw - Ds.width) // 2, (ph - Ds.height) // 2))
    return np.asarray(C.crop(box), dtype=float)
def nc(a, b):
    a = (a - a.mean()) / (a.std() + 1e-6); b = (b - b.mean()) / (b.std() + 1e-6); return float((a * b).mean())
pm = P.reshape(-1, 3).mean(axis=0)
print(f'live pane region mean RGB ({pm[0]:.1f},{pm[1]:.1f},{pm[2]:.1f}) R/B {pm[0]/max(pm[2],1e-6):.3f}')
rows = []
for f in sorted(glob.glob('assets/walls/*@2x.jpg')):
    W = fit(f); wm = W.reshape(-1, 3).mean(axis=0) * .6
    rows.append((nc(PL, W.mean(axis=2)), os.path.basename(f), wm[0] / max(wm[2], 1e-6)))
for c, n, rb in sorted(rows, reverse=True):
    print(f'{n:32s} corr {c:+.3f}   asset R/B {rb:.3f}')
