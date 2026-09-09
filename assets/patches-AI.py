#!/usr/bin/env python3
"""Print mean RGB of a few sample patches in a capture so I can see the letterbox / page colors. usage: patches-AI.py <png> x,y ..."""
import sys
import numpy as np
from PIL import Image
im = np.asarray(Image.open(sys.argv[1]).convert('RGB'), dtype=int)
for a in sys.argv[2:]:
    x, y = map(int, a.split(','))
    p = im[y:y + 12, x:x + 12].reshape(-1, 3).mean(axis=0)
    print(f'({x},{y}) → RGB ({p[0]:.0f},{p[1]:.0f},{p[2]:.0f})')
