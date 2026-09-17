---
title: "UEFI boot-from-file — the only-device boot menu"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [tool, pain]
sources: [raw/inbox/2026-09-12.md]
confidence: high
---

# UEFI boot-from-file — the only-device boot menu

A **boot troubleshooting** thread from 2026-09-12 around an **x86 / HP-style machine** (EFI boot paths, not the Android Duo). Chris was trying to get a machine to boot from a USB but it was not appearing as a bootable device.

## The boot menu state
In the EFI boot menu, under **"boot from file"**, the only device listed is an **internal SATA hard drive** via the path:

```
PciRoot(0x0)/Pci(0x1F,0x2)/Sata(0x1, 0x0, 0x0,)/HD(1,GPT,A4FDCB01-6736-47f9-a09B-67…
```

Chris confirmed: "**my choices are uefi or boot from file**" — i.e. the boot menu only offers those two buckets, and neither surfaced the USB. ^[raw/2026-09-12.md]

## Troubleshooting suggested
Hermes proposed: (1) try a **USB 2.0 port** (black, not blue — "Some HPs won't boot from USB 3.0"), (2) reboot and press **F2/Del** for BIOS Setup to check Boot Options, (3) press **F9/F12/Esc** for the one-shot boot menu. ^[raw/2026-09-12.md]

## Recovery-mode password reset (re-routed from dispatched-m2s)
The same x86/HP-style box also shows up in a **Windows recovery** thread. On **2026-09-12** Hermes noted that `` `resetpassword` `` **only works in Recovery Mode, not the normal terminal**, and offered to **check the `dd`** first. ^[raw/2026-09-14-from-dispatched-m2s.md] This is a distinct sub-thread from the EFI boot-menu work — Chris was trying to reset a Windows password, hitting the wall that `resetpassword` needs Recovery Mode — while the boot-from-file probing was about getting the USB to appear. ^[raw/2026-09-14-from-dispatched-m2s.md]

## Takeaway
The machine boots (the internal HD is a valid boot file), but the **USB isn't registering** — pointing at a port/USB-version or boot-order issue rather than a dead drive. Whether this ties to the same single-device build as the Duo is unresolved; it may belong to a hardware/EFI topic. ^[raw/2026-09-12.md]

See also: [[topics-wiki/only-device/wiki/entities/duo|The Duo]] · [[topics-wiki/only-device/wiki/concepts/adb-wireless-debugging|ADB wireless debugging]]
