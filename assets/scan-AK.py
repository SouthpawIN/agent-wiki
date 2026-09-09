# AK scan: locate the bright line-art figure in a wall-only screenshot. Prints per-band bright-pixel centroids
# (rows in 40px bands: mean x of pixels with luma > thr, count) so the head/chest columns can be read off.
import sys
from PIL import Image
p = sys.argv[1]; thr = int(sys.argv[2]) if len(sys.argv) > 2 else 150
im = Image.open(p).convert('L'); W, H = im.size; px = im.load()
print('size', W, H)
for y0 in range(0, H, 40):
    xs = []
    for y in range(y0, min(y0 + 40, H)):
        for x in range(W // 2, W):
            if px[x, y] > thr: xs.append(x)
    if xs:
        xs.sort(); n = len(xs)
        print(f'y {y0:4d}-{y0+39:4d}: n={n:6d} xmin={xs[0]} p10={xs[n//10]} med={xs[n//2]} p90={xs[9*n//10]} xmax={xs[-1]}')
    else:
        print(f'y {y0:4d}-{y0+39:4d}: none')
