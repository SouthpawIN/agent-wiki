#!/usr/bin/env python3
"""Where does the pane's top edge actually sit? Find the first row (from a given y) in a column band where pixels stop being #060606 for real
(pane content) and where the hero title ink appears. usage: paneTop-AI.py <png> x0 x1 yStart yEnd"""
import sys
import numpy as np
from PIL import Image
im = np.asarray(Image.open(sys.argv[1]).convert('L'), dtype=int)
x0, x1, ys, ye = map(int, sys.argv[2:6])
band = im[ys:ye, x0:x1]
for y in range(0, ye - ys, 2):
    r = band[y]
    print(f'y={ys+y}: mean {r.mean():6.1f} max {r.max():3d} nonblack% {(np.abs(r-6)>3).mean()*100:5.1f}')
