#!/usr/bin/env python3
"""Read a Chromium Local Storage leveldb for a key — no leveldb lib: scan raw bytes for the key and print the bytes after it (values are UTF-16LE or latin1 tagged)."""
import sys, glob, re
d = sys.argv[1]; key = sys.argv[2].encode()
for f in sorted(glob.glob(d + '/*.log') + glob.glob(d + '/*.ldb')):
    b = open(f, 'rb').read()
    for m in re.finditer(re.escape(key), b):
        seg = b[m.end():m.end() + 80]
        # chromium value: 1 byte type tag (0 = utf16le, 1 = latin1) then the string
        tag = seg[:1]
        if tag == b'\x01': val = seg[1:41].split(b'\x00')[0].decode('latin1', 'replace')
        elif tag == b'\x00': val = seg[1:81].decode('utf-16le', 'replace').split('\x00')[0]
        else: val = repr(seg[:40])
        print(f, key.decode(), '→', val[:60])
