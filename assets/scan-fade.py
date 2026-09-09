"""scan-fade.py <png> [x] — print max brightness across a 440px lane row-by-row from y=90..220 (step 6).
A fade ramp shows brightness rising gradually from ~0 to the card's border/text level; a hard clip jumps in one step."""
import sys
from PIL import Image
p=sys.argv[1]; im=Image.open(p).convert('RGB'); W,H=im.size
x0=int(sys.argv[2]) if len(sys.argv)>2 else W-14-440; x1=W-14
rows=[]
for y in range(90,221,6):
    m=0
    for x in range(x0,x1):
        r,g,b=im.getpixel((x,y)); m=max(m,max(r,g,b))
    rows.append((y,m))
print(' '.join(f'{y}:{m}' for y,m in rows))
