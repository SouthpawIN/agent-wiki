#!/usr/bin/env python3
"""Scan Chromium Local Storage leveldb files for 'hermes-<wall>' / 'none' values near a 'wall' key, in file order (later files/offsets = newer)."""
import sys, glob, re, os
d = sys.argv[1]
files = sorted(glob.glob(d + '/*.ldb') + glob.glob(d + '/*.log'), key=os.path.getmtime)
for f in files:
    b = open(f, 'rb').read()
    hits = []
    for m in re.finditer(rb'wall', b):
        seg = b[m.end():m.end() + 60]
        v = re.search(rb'(hermes-[a-z\-]+|none)', seg)
        u = re.search('(hermes-[a-z\\-]+|none)', seg.decode('utf-16le', 'ignore'))
        hits.append((m.start(), v.group(1).decode() if v else (u.group(1) if u else '?')))
    print(os.path.basename(f), 'mtime', int(os.path.getmtime(f)), hits[-6:])
