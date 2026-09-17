#!/usr/bin/env python3
"""Find the webview pane box in a Retina Hermes capture: the largest rectangle whose border is the Hermes chrome color (~26,28,31) around
page content. Scans one row and one column for transitions from chrome → page. usage: panebox-AI.py <png> <probeY> <probeX>"""
import sys
import numpy as np
from PIL import Image
im = np.asarray(Image.open(sys.argv[1]).convert('RGB'), dtype=int); H, W, _ = im.shape
py, px = int(sys.argv[2]), int(sys.argv[3])
def is_chrome(p): return abs(p[0] - 26) <= 3 and abs(p[1] - 28) <= 3 and abs(p[2] - 31) <= 3
row = im[py]; col = im[:, px]
# from the probe point walk left/right until chrome
def walk(arr, start, step):
    i = start
    while 0 <= i < len(arr) and not is_chrome(arr[i]): i += step
    return i
L = walk(row, px, -1) + 1; R = walk(row, px, 1)
T = walk(col, py, -1) + 1; B = walk(col, py, 1)
print(f'pane box (device px): x={L} y={T} w={R-L} h={B-T}   (probe row {py}, col {px}; chrome colour 26,28,31)')
