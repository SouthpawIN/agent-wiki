#!/usr/bin/env python3
"""AI proof: compare the wiki's rendered backdrop against the REAL macOS desktop wallpaper, same image, same crop.
usage: venv/bin/python assets/compare-AI.py <wiki-wallonly.png> <desk-wall.png> <wiki-full.png> <out-sidebyside.png>
- Applies `cover`/center math to the desktop capture so the crop matches the wiki pane's aspect, then diffs.
- Reports mean per-channel color of the dimmed wiki frame vs the neutral-dimmed desktop (cast check: R/B ratio must match).
"""
import sys
from PIL import Image, ImageChops, ImageStat, ImageDraw

wiki_wall, desk, wiki_full, out = sys.argv[1:5]
A = Image.open(wiki_wall).convert('RGB')          # wiki: wall only, no dim, no UI (device px)
D = Image.open(desk).convert('RGB')               # desktop wallpaper window capture (device px)
F = Image.open(wiki_full).convert('RGB')          # wiki: full page (wall + dim + map + UI)

# fit the desktop image into the wiki pane's box, centered — same rule the CSS applies. FIT=contain (current, v14.66 Chris: whole artwork) | cover
import os
FIT = os.environ.get('FIT', 'contain')
aw, ah = A.size
dw, dh = D.size
s = (min if FIT == 'contain' else max)(aw / dw, ah / dh)
sw, sh = round(dw * s), round(dh * s)
Ds = D.resize((sw, sh), Image.LANCZOS)
Dc = Image.new('RGB', (aw, ah), (6, 6, 6))           # letterbox bands = page black, like #wallBackdrop background-color
x0, y0 = (aw - sw) // 2, (ah - sh) // 2
if FIT == 'contain':
    Dc.paste(Ds, (x0, y0))
else:
    Dc = Ds.crop((-x0, -y0, -x0 + aw, -y0 + ah))
print(f'FIT={FIT}')

diff = ImageChops.difference(A, Dc)
st = ImageStat.Stat(diff)
mad = sum(st.mean) / 3
print(f'wiki wall frame {aw}x{ah}; desktop {dw}x{dh} → cover scale {s:.4f} → {sw}x{sh}, crop offset ({x0},{y0})')
print(f'mean abs diff per channel (0-255): R {st.mean[0]:.2f} G {st.mean[1]:.2f} B {st.mean[2]:.2f} → avg {mad:.2f}')

def cast(img, label):
    m = ImageStat.Stat(img).mean
    r, g, b = m
    print(f'{label}: mean RGB ({r:.1f},{g:.1f},{b:.1f})  R/B {r/max(b,1e-6):.3f}  R/G {r/max(g,1e-6):.3f}')
    return r / max(b, 1e-6)

rb_desk = cast(Dc, 'desktop (same crop, undimmed)')
rb_wall = cast(A, 'wiki wall only (undimmed)')
# a neutral dim leaves channel RATIOS unchanged; a warm dim raises R/B. Measure the LAYERS, not the whole page (white UI text pushes any ratio toward 1).
import os
base = wiki_wall.replace('AI-wallonly-', 'AI-{}-')
for layer in ('walldim', 'walldimmap'):
    pth = base.format(layer)
    if os.path.exists(pth):
        cast(Image.open(pth).convert('RGB'), f'wiki {layer}')
rb_full = cast(F, 'wiki full page (dim + map + UI; white text skews this toward 1 — informational)')
wd = base.format('walldim')
if os.path.exists(wd):
    rb_wd = ImageStat.Stat(Image.open(wd).convert('RGB')).mean
    print(f'cast check (dim layer): R/B desktop {rb_desk:.3f} vs wiki wall+dim {rb_wd[0]/max(rb_wd[2],1e-6):.3f} → delta {rb_wd[0]/max(rb_wd[2],1e-6)-rb_desk:+.3f} (neutral ⇒ ~0)')

# side-by-side: left = real desktop (cover crop), right = wiki backdrop, thin white gutter; label in header strip
gut = 24
W = aw * 2 + gut
canvas = Image.new('RGB', (W, ah + 60), (0, 0, 0))
canvas.paste(Dc, (0, 60)); canvas.paste(A, (aw + gut, 60))
d = ImageDraw.Draw(canvas)
d.rectangle((aw, 60, aw + gut, ah + 60), fill=(255, 255, 255))
d.text((16, 20), f'REAL DESKTOP WALLPAPER (screencapture -l Wallpaper window, cover-cropped to pane)  {aw}x{ah}', fill=(255, 255, 255))
d.text((aw + gut + 16, 20), f'SENTER WIKI #wallBackdrop (dim + UI hidden)  mean|diff| {mad:.2f}/255', fill=(255, 255, 255))
canvas.thumbnail((3200, 3200))
canvas.save(out, quality=90)
print('side-by-side →', out)
