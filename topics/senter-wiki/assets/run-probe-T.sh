#!/bin/bash
# run-probe-T.sh — syntax check + probe T at Chris's viewport (no nested shell bodies for Tirith)
cd ~/Documents/Projects/Projects || exit 1
~/.hermes/hermes-agent/venv/bin/python - <<'PY'
import re,pathlib
h=pathlib.Path('vault-live.html').read_text()
scripts=re.findall(r'<script>(.*?)</script>',h,re.S)
pathlib.Path('/tmp/vl-script.js').write_text('\n;\n'.join(scripts))
print('bytes',len(h),'sentinels',all(s in h for s in ['topnav','view-feed','FLEET STREAM']))
PY
~/.hermes/node/bin/node --check /tmp/vl-script.js && echo "node --check OK"
export PW=~/.hermes/hermes-agent/node_modules/playwright
~/.hermes/node/bin/node assets/probe-T.js "${1:-1456x914}" "${2:-assets/look}" > /tmp/probe-T.json
~/.hermes/hermes-agent/venv/bin/python - <<'PY'
import json;d=json.load(open('/tmp/probe-T.json'))
print('errs',d['errs'])
for k in ('model','context','flip'):
    m=d[k]; print(k,'btn',m['btn'],'pop',m['pop'],'up',m['up'],'checks',m['checks'])
PY
