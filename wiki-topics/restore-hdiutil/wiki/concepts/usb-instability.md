---
title: USB drive instability
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [pain, tool, question]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-15.md]
confidence: medium
---

# USB drive instability

While flashing the Omarchy ISO, Chris's USB drive exhibited hardware-level problems. [^raw1]

## Symptoms
- **Keeps ejecting when not touching it** → hermes diagnosed a "flaky connection" and advised switching USB ports. [^raw1]
- **Partition table destroyed** by the failed `hdiutil restore` writes → macOS stopped exposing a usable disk device (it briefly mounted as `disk5`). [^raw1]
- **Etcher refuses / warns "ISO might be corrupted"** — hermes insisted the ISO is fine and blamed the drive. [^raw1]

## Contested points
- **Cause:** hermes attributes it to a flaky port + destroyed partition table; Chris never confirmed the port swap fixed it. [^raw1]
- **ISO integrity:** hermes claims SHA256 matches and the header is valid; Etcher's "corrupted" warning is unexplained — either a bad write caused by the unstable connection, or a genuinely bad burn. [^raw1]

## Open question
Whether the USB is a **hardware fault** (port/drive) or simply a **write-method** problem (raw ISO misbooting as UEFI Ubuntu). Unresolved. [^raw1]

## Related
- [[wiki-topics/restore-hdiutil/wiki/decisions/omarchy-iso-flash|Omarchy ISO flash]] — the attempt.
- [[wiki-topics/restore-hdiutil/wiki/comparisons/flash-methods|Flash methods]] — alternatives to Etcher.

---
[^raw1]: [raw/inbox/2026-09-12.md](raw/inbox/2026-09-12.md).
