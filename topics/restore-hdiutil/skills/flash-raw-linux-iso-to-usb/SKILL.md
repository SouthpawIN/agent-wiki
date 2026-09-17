---
name: flash-raw-linux-iso-to-usb
description: Use when writing a raw Linux distro ISO (.iso) to a USB so it boots as the right distro on macOS. Steps: verify SHA256, diskutil list to pick rdisk, dd raw write to /dev/rdiskN, unmountDisk; avoid hdiutil restore (verb not recognized on recent macOS) and use makehybrid when the entry misboots as generic UEFI.
version: 0.1.0
distilled: 2026-09-15 15:31
topic: restore-hdiutil
---
# flash-raw-linux-iso-to-usb
# Flash a Raw Linux ISO to USB (macOS)

Write a raw `.iso` to a USB so the firmware boots the distro's own entry, not a generic UEFI/Ubuntu one.

## Steps
1. Verify the source: `shasum -a 256 <iso>` against the publisher's hash. If it mismatches, re-download — don't flash a bad ISO.
2. Plug in the USB. `diskutil list` — identify the USB device id (e.g. `/dev/disk2`). For raw speed use the `r` variant: `/dev/rdisk2`.
3. Write raw: `sudo dd if=<iso> of=/dev/rdisk2 bs=1m status=progress`.
4. Finish: `diskutil unmountDisk /dev/disk2` so the firmware sees the untouched image.
5. Boot it and confirm the entry is named for the distro.

## Pitfalls
- `hdiutil restore -nomount` is unreliable on recent macOS (reports 'verb not recognized'); use dd or `hdiutil makehybrid`.
- If the USB boots as 'UEFI Ubuntu' or a generic entry, the raw ISO's hybrid boot record is ambiguous — rebuild with `hdiutil makehybrid -iso -bootinfo -o out.iso <iso>` and flash that instead.
- A USB that ejects when untouched is a port/hardware fault — switch ports, keep retrying the same one won't help.
- Never guess the device id; a wrong `of=` wipes the wrong drive.

## Evidence
> Command: # Use hdiutil restore to write the ISO to the USB hdiutil restore -nomount ~/tmp/omarchy/omarchy-4.0.3.iso /dev/rdisk4 ... hdiutil: restore: verb not recognized
> well it said UEFI Ubuntu not Omarchy
> it keeps ejecting when I'm not touching it. That may be an issue too
