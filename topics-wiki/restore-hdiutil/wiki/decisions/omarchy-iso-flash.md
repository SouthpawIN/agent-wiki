---
title: Omarchy ISO flash
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, plan, pain, timeline]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-15.md]
confidence: high
---

# Omarchy ISO flash

**Goal:** write `~/tmp/omarchy/omarchy-4.0.3.iso` to a USB and boot it on an HP to install Omarchy v4.0.3. [^raw1]

## What was tried
1. **`hdiutil restore -nomount`** to `/dev/rdisk4` — the intended CLI path. **Failed:** `restore: verb not recognized`, exit 1. [^raw1]
2. **balenaEtcher (GUI):** "Flash from file → select target → Flash!" — Chris ran it. It reported the ISO *might be corrupted*, and the boot entry showed **"UEFI Ubuntu not Omarchy."** [^raw1]
3. **Disk Utility erase** of the USB to create a partition table (no sudo needed), then re-try Etcher. [^raw1]

## Problems encountered (contested / unresolved)
- **USB keeps ejecting** when Chris isn't touching it → hermes attributed it to a "flaky connection" and advised a different USB port. [^raw1]
- **Etcher says the ISO might be corrupted** — hermes insisted the ISO is valid (SHA256 matches, 5.8GB, proper header) and blamed the drive. [^raw1]
- **Partition table destroyed** by failed writes → macOS stopped exposing a disk device; hermes said only Etcher's IOKit raw access can rewrite it. [^raw1]
- **Booted as "UEFI Ubuntu", not Omarchy** — the write succeeded as a bootable USB but presented the wrong entry. [^raw1]

## Decisions made
- Use the **latest ISO, v4.0.3** (Sep 8, 2026), not the leftover `omarchy-4.0.2.iso`. [^raw1]
- **Quit balenaEtcher, replug into a different USB port, reopen Etcher** and retry — hermes's proposed fix for the ejection. [^raw1]
- **ISO is valid; the USB drive is the problem** — hermes's conclusion, not yet confirmed by Chris. [^raw1]

## Status
Unresolved as of 2026-09-15 (only a hermes "restore the working configuration" note in the newer raw). The `restore` verb being unavailable on this macOS build removes the clean CLI fallback; a raw `dd` write or the `.dmg` variant remain open options. [^raw1]

## Related
- [[topics-wiki/restore-hdiutil/wiki/entities/hdiutil|hdiutil / restore verb]] — why the CLI path failed.
- [[topics-wiki/restore-hdiutil/wiki/entities/omarchy|Omarchy ISO (v4.0.3)]] — the image.
- [[topics-wiki/restore-hdiutil/wiki/comparisons/flash-methods|Flash methods]] — Etcher vs raw `dd` vs `makehybrid`.

---
[^raw1]: [raw/inbox/2026-09-12.md](raw/inbox/2026-09-12.md).
