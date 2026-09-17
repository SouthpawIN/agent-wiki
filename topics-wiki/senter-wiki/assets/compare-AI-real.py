#!/usr/bin/env python3
"""AI real-window proof: crop the SAME wallpaper feature from (a) a Retina capture of the Hermes window (the live wiki pane)
and (b) the real desktop wallpaper window capture, at device pixels, and put them side by side at 2x zoom so sharpness is judgeable.
usage: python compare-AI-real.py <hermes-win.png> <desk-wall.png> <paneX0> <paneY0> <paneW> <paneH> <out.png>
pane* = the wiki pane's bounds inside the window capture, in DEVICE px (find them by looking at the capture).
"""
import sys
from PIL import Image, ImageDraw, ImageStat, ImageChops

win, desk, x0, y0, pw, ph, out = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), sys.argv[7]
Wn = Image.open(win).convert('RGB')
D = Image.open(desk).convert('RGB')
pane = Wn.crop((x0, y0, x0 + pw, y0 + ph))
# cover-fit the desktop image into the pane's box (same CSS rule) → the region the pane shows
dw, dh = D.size
s = max(pw / dw, ph / dh)
Ds = D.resize((round(dw * s), round(dh * s)), Image.LANCZOS)
cx, cy = (Ds.width - pw) // 2, (Ds.height - ph) // 2
Dc = Ds.crop((cx, cy, cx + pw, cy + ph))
print(f'pane {pw}x{ph} device px; cover scale {s:.4f}; desktop crop offset ({cx},{cy}) → backdrop shows {pw/s:.0f}x{ph/s:.0f} of the 3024x1964 wall')

# region = pane-relative fractions; default = right-upper band (clean wall: below the hero line, above the fleet stream). Override: REGION=x,y,w,h env.
import os
fx, fy, fw, fh = map(float, os.environ.get('REGION', '.55,.09,.40,.22').split(','))
rx0, ry0 = int(pw * fx), int(ph * fy)
rw, rh = int(pw * fw), int(ph * fh)
a = pane.crop((rx0, ry0, rx0 + rw, ry0 + rh))
b = Dc.crop((rx0, ry0, rx0 + rw, ry0 + rh))
ma, mb = ImageStat.Stat(a).mean, ImageStat.Stat(b).mean
print(f'crop region (pane-relative) {rx0},{ry0} {rw}x{rh}')
print(f'live pane crop  mean RGB ({ma[0]:.1f},{ma[1]:.1f},{ma[2]:.1f}) R/B {ma[0]/max(ma[2],1e-6):.3f}  (dimmed .45 + UI)')
print(f'desktop crop    mean RGB ({mb[0]:.1f},{mb[1]:.1f},{mb[2]:.1f}) R/B {mb[0]/max(mb[2],1e-6):.3f}  (undimmed)')
# structural similarity proxy: normalize brightness, then diff
import numpy as np
A = np.asarray(a.convert('L'), dtype=float); B = np.asarray(b.convert('L'), dtype=float)
A = (A - A.mean()) / (A.std() + 1e-6); B = (B - B.mean()) / (B.std() + 1e-6)
corr = float((A * B).mean())
print(f'normalized correlation of the two crops: {corr:.3f} (1 = identical structure/placement; <0.5 = different image or misaligned)')

z = 2
canvas = Image.new('RGB', (rw * z * 2 + 24, rh * z + 56), (0, 0, 0))
canvas.paste(b.resize((rw * z, rh * z), Image.NEAREST), (0, 56))
canvas.paste(a.resize((rw * z, rh * z), Image.NEAREST), (rw * z + 24, 56))
d = ImageDraw.Draw(canvas)
d.rectangle((rw * z, 56, rw * z + 24, rh * z + 56), fill=(255, 255, 255))
d.text((12, 18), f'REAL DESKTOP wallpaper — same cover crop, device px, 2x zoom (undimmed)', fill=(255, 255, 255))
d.text((rw * z + 36, 18), f'LIVE HERMES PANE (Retina screencapture -l 18) — wiki backdrop under UI, 2x zoom; corr {corr:.3f}', fill=(255, 255, 255))
canvas.save(out, quality=92)
print('→', out)
