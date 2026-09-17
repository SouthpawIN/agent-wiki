#!/usr/bin/env python3
"""AI real-window alignment: is the live pane's backdrop the desktop wallpaper at the same cover/center crop?
Masks out UI ink (bright pixels) and searches small x/y shifts for the best normalized correlation.
usage: python align-AI-real.py <hermes-win.png> <desk-wall.png> <paneX> <paneY> <paneW> <paneH>
"""
import sys
import os
import numpy as np
from PIL import Image

win, desk, x0, y0, pw, ph = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
pane = Image.open(win).convert('L').crop((x0, y0, x0 + pw, y0 + ph))
D = Image.open(desk).convert('L')
dw, dh = D.size
if os.environ.get('MODE') == 'screen':
    # hypothesis test: the pane is see-through (liquid glass) → wallpaper at the SAME SCREEN coords, no cover math. SCREEN_Y0 = window top in device px (menu bar 33 CSS → 66).
    Ds = D; cx, cy = x0, y0 + int(os.environ.get('SCREEN_Y0', 66)); s = 1.0
else:
    FIT = os.environ.get('FIT', 'contain')
    s = (min if FIT == 'contain' else max)(pw / dw, ph / dh)
    Dsr = D.resize((round(dw * s), round(dh * s)), Image.LANCZOS)
    if FIT == 'contain':
        # pad with page black so the letterbox bands exist, then the pane box = the padded image → offset 0
        pad = Image.new('L', (max(pw, Dsr.width) + 400, max(ph, Dsr.height) + 400), 6)
        pad.paste(Dsr, ((pad.width - Dsr.width) // 2, (pad.height - Dsr.height) // 2)); Ds = pad
        cx, cy = (Ds.width - pw) // 2, (Ds.height - ph) // 2
    else:
        Ds = Dsr; cx, cy = (Ds.width - pw) // 2, (Ds.height - ph) // 2

P = np.asarray(pane, dtype=float)
# optional REGION=x,y,w,h (pane fractions) to restrict to a clean-wall band (full pane is dominated by the topic list / stream cards)
import os
if os.environ.get('REGION'):
    fx, fy, fw, fh = map(float, os.environ['REGION'].split(','))
    rx, ry, rw, rh = int(pw * fx), int(ph * fy), int(pw * fw), int(ph * fh)
else:
    rx, ry, rw, rh = 0, 0, pw, ph
P = P[ry:ry + rh, rx:rx + rw]
print(f'region (pane px) {rx},{ry} {rw}x{rh}')
# downsample 4x for speed
def ds(a): 
    h, w = a.shape; h -= h % 4; w -= w % 4
    return a[:h, :w].reshape(h // 4, 4, w // 4, 4).mean(axis=(1, 3))
Pd = ds(P)
mask = Pd < 135  # wall under .45 dim tops out at 255*.55=140; white UI text/cards are brighter → excluded (the figure's pale lines land at ~60-130, keep them)
print(f'pane {pw}x{ph}; cover scale {s:.4f}; nominal desktop crop offset ({cx},{cy}); mask keeps {mask.mean()*100:.0f}% of pixels (wall, not UI)')

def corr(dx, dy):
    Dc = np.asarray(Ds.crop((cx + dx + rx, cy + dy + ry, cx + dx + rx + rw, cy + dy + ry + rh)), dtype=float)
    Dd = ds(Dc)
    a = Pd[mask]; b = Dd[mask]
    a = (a - a.mean()) / (a.std() + 1e-6); b = (b - b.mean()) / (b.std() + 1e-6)
    return float((a * b).mean())

best = (corr(0, 0), 0, 0)
SX, SY, ST = int(os.environ.get('SX', 160)), int(os.environ.get('SY', 80)), int(os.environ.get('ST', 8))
for dy in range(-SY, SY + 1, ST):
    for dx in range(-SX, SX + 1, ST):
        if cx + dx + rx < 0 or cy + dy + ry < 0 or cx + dx + rx + rw > Ds.width or cy + dy + ry + rh > Ds.height: continue
        c = corr(dx, dy)
        if c > best[0]: best = (c, dx, dy)
print(f'corr at nominal offset: {corr(0,0):.3f}; best {best[0]:.3f} at shift dx={best[1]} dy={best[2]} device px (0,0 ⇒ same crop)')
