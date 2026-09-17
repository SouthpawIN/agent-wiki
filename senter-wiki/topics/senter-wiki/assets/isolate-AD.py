"""isolate-AD.py — copy vault-live.html to /tmp/ad-revert.html with the AD re-home line reverted to the pre-AD behavior,
so the live ledger can be run against it and any non-AD failures attributed to other in-flight edits."""
import re, pathlib, shutil
src=pathlib.Path.home()/'Documents/Projects/Projects/vault-live.html'
html=src.read_text()
new="if(ch){ const show=STREAM_VIEWS.includes(v); ch.classList.toggle('hide', !show); ch.classList.remove('open'); pinned=false; if(show && ch.dataset.host!==v){ target.insertAdjacentElement('afterend', ch); ch.dataset.host=v; if(typeof syncFade==='function') try{ syncFade(); }catch(e){} } }"
old="if(ch){ ch.classList.toggle('hide', v!=='wiki'); if(v!=='wiki'){ ch.classList.remove('open'); window.pinned=false; } }"
assert new in html, 'AD line not found'
out=html.replace(new,old)
dst=pathlib.Path('/tmp/ad-revert/vault-live.html'); dst.parent.mkdir(exist_ok=True)
dst.write_text(out)
# assets symlink so fonts/avatars resolve
a=dst.parent/'assets'
if not a.exists(): a.symlink_to(src.parent/'assets')
for f in ['.system-live.json']:
    p=dst.parent/f
    if not p.exists() and (src.parent/f).exists(): p.symlink_to(src.parent/f)
print('wrote',dst, len(out))
