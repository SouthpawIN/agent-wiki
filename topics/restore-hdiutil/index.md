---
title: restore-hdiutil
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# restore-hdiutil

Last updated: 2026-09-16 | Total pages: 7

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [hdiutil / restore verb](wiki/hdiutil.md) — `hdiutil` is macOS's disk-image command-line tool. Chris tried to use its **`restore`** verb to write the Omarchy ISO straight to a USB device (`/dev/rdisk4`) —
- [Omarchy ISO (v4.0.3)](wiki/omarchy.md) — **Omarchy** is a Linux distro Chris is trying to install onto an **HP** machine by flashing a bootable USB. [^raw1]

### Concepts

- [USB drive instability](wiki/usb-instability.md) — While flashing the Omarchy ISO, Chris's USB drive exhibited hardware-level problems. [^raw1]

### Decisions

- [Omarchy ISO flash](wiki/omarchy-iso-flash.md) — **Goal:** write `~/tmp/omarchy/omarchy-4.0.3.iso` to a USB and boot it on an HP to install Omarchy v4.0.3. [^raw1]
- [2026-09-16 wiki structure rebuild](wiki/wiki-structure-rebuild.md) — The topic's wiki scaffolding was rebuilt on 2026-09-16 after hermes reported the structure was wrong. [^raw1]

### Comparisons

- [Flash methods for the Omarchy ISO](wiki/flash-methods.md) — Three ways to write the Omarchy image to a USB, and what the raw log says about each. [^raw1]

### Queries

- [Why does `hdiutil restore` fail here?](wiki/why-does-hdiutil-restore-fail.md) — **Question:** Chris ran `hdiutil restore -nomount ~/tmp/omarchy/omarchy-4.0.3.iso /dev/rdisk4` and got `restore: verb not recognized` (exit 1), even though the

---

## SKILLS

Topic skills stored in this wiki:

- **[flash-raw-linux-iso-to-usb](skills/flash-raw-linux-iso-to-usb/SKILL.md) — Write a raw `.iso` to a USB so the firmware boots the distro's own entry, not a generic UEFI/Ubuntu one.

---

## BOTS

Proposed bots:

- **[hdiutil-restore-detect](agents/hdiutil-restore-detect.md.proposed) — **I see the `hdiutil restore` verb keeps getting rejected on your Mac even though the man page lists it — want a bot that checks whether it's a per-bu
- **[omarchy-flasher](agents/omarchy-flasher.md.proposed) — **I see you're still stuck flashing the Omarchy v4.0.3 ISO onto a USB that keeps misbooting as 'UEFI Ubuntu' — want a bot that writes the ISO correctl


---

## LOOPS

No loops yet.