# restore-hdiutil
_Scaffolded by the watcher 2026-09-12 20:18 from a new subject Chris raised in the sidebar. Terms: restore · hdiutil · verb · iso · exit · command._

## What Chris said
> Command: # Use hdiutil restore to write the ISO to the USB
hdiutil restore -nomount ~/tmp/omarchy/omarchy-4.0.3.iso /dev/rdisk4 2>&1; echo "RESTORE EXIT=$?"
Output:
hdiutil: restore: verb not recognized
Usage: hdiutil <verb> <options>
<verb> is one of the following:
help
attach
detach
eject
verify
create
compact
convert
burn
info
checksum
chpass
erasekeys
imageinfo
isencrypted
makehybrid
mount
mountvol
unmount
plugins
resize
segment
pmap
udifderez
udifrez
RESTORE EXIT=1
]

## Status
- research dispatched (see .system/research.md when it lands)
