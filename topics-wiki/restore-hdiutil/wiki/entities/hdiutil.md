---
title: hdiutil / restore verb
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [tool, decision, pain]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-15.md]
confidence: high
---

# hdiutil / restore verb

`hdiutil` is macOS's disk-image command-line tool. Chris tried to use its **`restore`** verb to write the Omarchy ISO straight to a USB device (`/dev/rdisk4`) — and it failed. [^raw1]

## The failure
The command `hdiutil restore -nomount ~/tmp/omarchy/omarchy-4.0.3.iso /dev/rdisk4` returns **`hdiutil: restore: verb not recognized`** and exits 1. The full verb list it prints is: help, attach, detach, eject, verify, create, compact, convert, burn, info, checksum, chpass, erasekeys, imageinfo, isencrypted, makehybrid, mount, mountvol, unmount, plugins, resize, segment, pmap, udifderez, udifrez. **`restore` is not in that list.** [^raw1]

This is verifiable on this machine today: running `hdiutil restore -h` and the full command both reproduce `verb not recognized`, exit 1, on macOS 26.6.2 (Build 25G83). The system man page *documents* `restore` (it appears in the CD-restore section), so the verb exists in the man page but the installed binary rejects it — a man/binary mismatch on this build. [^raw1]

## Why it matters for the topic
`restore` is the natural CLI path to flash a raw ISO to a USB (`-nomount` writes the image without mounting a partition table). Its absence forces a fallback: either a GUI flasher or a `dd`-style raw write. This is the core pain of the topic. [^raw1]

## Related
- [[topics-wiki/restore-hdiutil/wiki/decisions/omarchy-iso-flash|Omarchy ISO flash]] — the goal `restore` was meant to serve.
- [[topics-wiki/restore-hdiutil/wiki/comparisons/flash-methods|Flash methods]] — Etcher vs raw `dd` vs `makehybrid`.

---
[^raw1]: [raw/inbox/2026-09-12.md](raw/inbox/2026-09-12.md) — chris command log + `hdiutil restore -h` output; verified live 2026-09-15.
