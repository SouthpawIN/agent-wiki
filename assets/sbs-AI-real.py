#!/usr/bin/env python3
"""Full-pane side-by-side: live Hermes wiki pane (device px) vs the desktop wallpaper cover-cropped to the pane box. For eyes + vision."""
import sys
from PIL import Image, ImageDraw
win, desk, x0, y0, pw, ph, out = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), sys.argv[7]
pane = Image.open(win).convert('RGB').crop((x0, y0, x0 + pw, y0 + ph))
import os
FIT = os.environ.get('FIT', 'contain')
D = Image.open(desk).convert('RGB'); dw, dh = D.size
s = (min if FIT == 'contain' else max)(pw / dw, ph / dh); Ds = D.resize((round(dw * s), round(dh * s)), Image.LANCZOS)
Dc = Image.new('RGB', (pw, ph), (6, 6, 6)); ox, oy = (pw - Ds.width) // 2, (ph - Ds.height) // 2
if FIT == 'contain': Dc.paste(Ds, (ox, oy))
else: Dc = Ds.crop((-ox, -oy, -ox + pw, -oy + ph))
print('FIT', FIT, 'scale', round(s, 4), 'offset', ox, oy)
# brighten the desktop crop by the dim factor so the eye compares like with like (wiki has .45 black over it → ×0.55)
Dd = Image.eval(Dc, lambda v: int(v * .55))
if os.environ.get('REGION'):  # zoom on one clean-wall region (pane fractions) instead of the whole pane
    fx, fy, fw, fh = map(float, os.environ['REGION'].split(','))
    box = (int(pw * fx), int(ph * fy), int(pw * (fx + fw)), int(ph * (fy + fh)))
    Dd, pane = Dd.crop(box), pane.crop(box); pw, ph = pane.size
    from PIL import ImageFilter
    import numpy as np
    for lab, img in (('desktop', Dd), ('live pane', pane)):
        ev = np.asarray(img.convert('L').filter(ImageFilter.FIND_EDGES), dtype=float).var(); m = np.asarray(img, dtype=float).reshape(-1, 3).mean(axis=0)
        print(f'{lab:10s} region mean RGB ({m[0]:.1f},{m[1]:.1f},{m[2]:.1f}) R/B {m[0]/max(m[2],1e-6):.3f}  edge-var {ev:.1f}')
W = pw * 2 + 24; c = Image.new('RGB', (W, ph + 60), (0, 0, 0))
c.paste(Dd, (0, 60)); c.paste(pane, (pw + 24, 60))
d = ImageDraw.Draw(c); d.rectangle((pw, 60, pw + 24, ph + 60), fill=(255, 255, 255))
d.text((16, 20), 'REAL DESKTOP wallpaper, cover-cropped to the pane box, x0.55 (= the .45 neutral dim)', fill=(255, 255, 255))
d.text((pw + 40, 20), 'LIVE HERMES wiki pane (Retina screencapture, device px) — UI over the backdrop', fill=(255, 255, 255))
c.thumbnail((3000, 3000)); c.save(out, quality=90); print('→', out, c.size)
