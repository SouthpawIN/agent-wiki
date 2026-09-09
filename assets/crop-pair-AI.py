#!/usr/bin/env python3
"""Tight crop pair for the vision verdict: same region of nebula from desktop (fitted) vs wiki wall-only frame. usage: crop-pair-AI.py <wiki.png> <desk.png> <fx,fy,fw,fh> <out.png> [FIT]"""
import sys
from PIL import Image, ImageDraw
A = Image.open(sys.argv[1]).convert('RGB'); D = Image.open(sys.argv[2]).convert('RGB')
fx, fy, fw, fh = map(float, sys.argv[3].split(',')); out = sys.argv[4]; FIT = sys.argv[5] if len(sys.argv) > 5 else 'contain'
aw, ah = A.size; dw, dh = D.size
s = (min if FIT == 'contain' else max)(aw / dw, ah / dh)
Ds = D.resize((round(dw * s), round(dh * s)), Image.LANCZOS)
Dc = Image.new('RGB', (aw, ah), (6, 6, 6)); x0, y0 = (aw - Ds.width) // 2, (ah - Ds.height) // 2
if FIT == 'contain': Dc.paste(Ds, (x0, y0))
else: Dc = Ds.crop((-x0, -y0, -x0 + aw, -y0 + ah))
box = (int(aw * fx), int(ah * fy), int(aw * (fx + fw)), int(ah * (fy + fh)))
a, b = A.crop(box), Dc.crop(box)
w, h = a.size; c = Image.new('RGB', (w * 2 + 16, h + 40), (0, 0, 0))
c.paste(b, (0, 40)); c.paste(a, (w + 16, 40)); d = ImageDraw.Draw(c); d.rectangle((w, 40, w + 16, h + 40), fill=(255, 255, 255))
d.text((8, 12), 'A: real desktop wallpaper', fill=(255, 255, 255)); d.text((w + 24, 12), 'B: Senter Wiki backdrop layer', fill=(255, 255, 255))
c.save(out, quality=92); print('→', out, c.size)
