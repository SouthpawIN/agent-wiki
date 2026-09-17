#!/bin/bash
# run-probe-AC.sh — node --check the page script, run the AC fade probe, pixel-scan the top-right column of both shots.
cd ~/Documents/Projects/Projects || exit 1
export PW=~/.hermes/hermes-agent/node_modules/playwright
N=~/.hermes/node/bin/node
PY=~/.hermes/hermes-agent/venv/bin/python
VP=${1:-1456x914}; DIR=${2:-assets/look}
$PY - <<'EOF'
import re
s=open('vault-live.html').read()
js=re.findall(r'<script>(.*?)</script>',s,re.S)
open('/tmp/vl-script.js','w').write('\n'.join(js))
for tok in ['id="topnav"','id="view-feed"','FLEET STREAM','id="stream"','id="chat"']:
    assert tok in s, tok
print('sentinels ok, bytes',len(s))
EOF
$N --check /tmp/vl-script.js && echo "node --check ok"
$N assets/probe-AC.js "$VP" "$DIR"
$PY - "$VP" "$DIR" <<'EOF'
import sys
from PIL import Image
vp,d=sys.argv[1],sys.argv[2]
for st in ('rest','hover'):
    im=Image.open(f'{d}/AC-{st}-{vp}.png').convert('L'); w,h=im.size
    # column band across the card (x 1050..1420), luma max per 10px row band from y=0..200
    out=[]
    for y0 in range(0,200,10):
        box=im.crop((1050,y0,1420,y0+10)); out.append(max(box.getdata()))
    print(st,'max-luma per 10px band y0..200:',out)
EOF
