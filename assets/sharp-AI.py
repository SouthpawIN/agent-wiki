#!/usr/bin/env python3
"""Sharpness ledger: old 2560 jpg (upscaled to render size) vs new 3024@2x jpg (downscaled) vs the PNG source, all at the same device-px render width.
usage: sharp-AI.py <render_width_devicepx> [fx,fy,fw,fh]"""
import sys
import numpy as np
from PIL import Image, ImageFilter
import os
RW = int(sys.argv[1]); reg = list(map(float, (sys.argv[2] if len(sys.argv) > 2 else '.625,.225,.25,.30').split(',')))
H = os.path.expanduser
srcs = [('PNG source 6048', H('~/Pictures/HermesWalls/hermes-galactic.png')), ('old 2560 q82 (UPscaled)', 'assets/walls/hermes-galactic.jpg'), ('new 3024 q92 @2x', 'assets/walls/hermes-galactic@2x.jpg')]
base = None
for label, p in srcs:
    im = Image.open(p).convert('L'); w, h = im.size
    r = im.resize((RW, round(h * RW / w)), Image.LANCZOS)
    W, Hh = r.size; box = (int(W * reg[0]), int(Hh * reg[1]), int(W * (reg[0] + reg[2])), int(Hh * (reg[1] + reg[3])))
    c = np.asarray(r.crop(box), dtype=float)
    ev = np.asarray(r.crop(box).filter(ImageFilter.FIND_EDGES), dtype=float).var()
    if base is None: base = c
    mad = np.abs(c - base).mean()
    print(f'{label:28s} native {w}x{h} → {RW}px  scale {RW/w:.3f}  edge-var {ev:8.1f}  |diff vs PNG| {mad:.2f}')
