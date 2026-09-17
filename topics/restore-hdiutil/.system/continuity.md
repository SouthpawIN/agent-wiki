# Continuity — restore-hdiutil
- New subject 2026-09-12 20:18: Command: # Use hdiutil restore to write the ISO to the USB
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
c
