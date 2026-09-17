"""AH pixel scan: count non-black pixels in the preview pane of a Hermes window capture (or a headless shot)."""
import sys
from PIL import Image
p = sys.argv[1]
im = Image.open(p).convert('RGB')
W, H = im.size
# preview pane = right ~70% of the window for a real capture; whole frame for a headless shot
x0 = int(W * 0.32) if 'computer_use' in p else 0
px = im.load()
tot = non = bright = 0
maxv = (0, 0, 0)
for y in range(int(H * 0.15), H - 60, 3):
    for x in range(x0 + 10, W - 10, 3):
        v = px[x, y]; tot += 1
        m = max(v)
        if m > 14: non += 1
        if m > 60: bright += 1
        if sum(v) > sum(maxv): maxv = v
print(f"{p}\n size {W}x{H} pane-x0 {x0} sampled {tot} nonblack {non} ({100*non/tot:.1f}%) bright>60 {bright} ({100*bright/tot:.1f}%) maxRGB {maxv}")
