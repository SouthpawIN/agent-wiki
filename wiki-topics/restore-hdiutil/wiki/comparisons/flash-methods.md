---
title: Flash methods for the Omarchy ISO
created: 2026-09-15
updated: 2026-09-15
type: comparison
tags: [tool, decision, pain]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-15.md]
confidence: high
---

# Flash methods for the Omarchy ISO

Three ways to write the Omarchy image to a USB, and what the raw log says about each. [^raw1]

| Method | Status | Note |
|---|---|---|
| `hdiutil restore -nomount` | **Fails** on this macOS (26.6.2 / 25G83) — `restore: verb not recognized` | Natural CLI path; man page documents it but the binary rejects it. [^raw1] |
| **balenaEtcher (GUI)** | **Used; unreliable** — reports "ISO might be corrupted", USB ejects mid-write, boots as "UEFI Ubuntu not Omarchy" | Uses IOKit raw device access; can rewrite a destroyed partition table. [^raw1] |
| **`dd` raw write** (`dd if=… of=/dev/rdiskN`) | **Open option** — not yet tried in the log | The canonical Unix raw-image writer; bypasses the missing `restore` verb. |
| **`hdiutil makehybrid`** | **Open option** — not yet tried | Hybrid ISO9660+MBR/GPT writer; the verb that *is* present in this build. |
| `.dmg` variant | **Present** — `omarchy-4.0.3.img.dmg` | Disk-Image format instead of raw `.iso`; may flash cleanly where the `.iso` misboots. [^raw1] |

## Why the raw ISO misboots
Etcher wrote a bootable USB but it presented as **"UEFI Ubuntu not Omarchy."** A raw `.iso` written with `dd`/`rdisk` (no partition table, `-nomount`-style) tends to behave like a bare hybrid — sometimes the firmware reads the Ubuntu/UEFI hybrid entry first. `makehybrid` with explicit `-iso -bootinfo` control is the usual fix. [^raw1]

## Related
- [[wiki-topics/restore-hdiutil/wiki/entities/hdiutil|hdiutil / restore verb]] — the missing verb.
- [[wiki-topics/restore-hdiutil/wiki/decisions/omarchy-iso-flash|Omarchy ISO flash]] — the overall attempt.

---
[^raw1]: [raw/inbox/2026-09-12.md](raw/inbox/2026-09-12.md).
