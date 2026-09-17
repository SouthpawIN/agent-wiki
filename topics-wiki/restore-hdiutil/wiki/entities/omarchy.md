---
title: Omarchy ISO (v4.0.3)
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [tool, plan, timeline]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-15.md]
confidence: high
---

# Omarchy ISO (v4.0.3)

**Omarchy** is a Linux distro Chris is trying to install onto an **HP** machine by flashing a bootable USB. [^raw1]

## The ISO
- **Version:** v4.0.3, published Sep 8, 2026 — confirmed latest via GitHub releases. [^raw1]
- **Path:** `~/tmp/omarchy/omarchy-4.0.3.iso` — 6.2 GB on disk (hermes reported "5.8GB"; the file is 6,260,654,080 bytes). [^raw1]
- **Also present:** `~/tmp/omarchy/omarchy-4.0.3.img.dmg` — a Disk-Image-format variant of the same 6.2 GB file. This is an alternative to the raw `.iso` for flashing. [^raw1]
- **Older file:** `~/Downloads/omarchy-4.0.2.iso` — a leftover from a previous session, not the one to use. [^raw1]
- **Integrity:** hermes claimed SHA256 matches, correct size, proper bootable ISO header — "ISO is valid." [^raw1]

## Boot symptom
When Chris booted a flashed USB, the machine reported **"UEFI Ubuntu not Omarchy"** — i.e. the USB booted but presented as a generic Ubuntu/UEFI entry rather than the Omarchy image. Suggests the write produced a valid-but-wrong or hybrid-ambiguous boot entry. [^raw1]

## Related
- [[topics-wiki/restore-hdiutil/wiki/decisions/omarchy-iso-flash|Omarchy ISO flash]] — the goal.
- [[topics-wiki/restore-hdiutil/wiki/comparisons/flash-methods|Flash methods]] — how to write the .iso vs .dmg.

---
[^raw1]: [raw/inbox/2026-09-12.md](raw/inbox/2026-09-12.md).
