---
title: Balena Etcher
created: 2026-09-12
updated: 2026-09-13
type: entity
tags: [tool]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-13.md]
confidence: high
---
Chris referred to Balena Etcher as "Bellina etcher" and later "blina etcher" in transcript dictation.^[raw/inbox/2026-09-12.md] He used it to write the Omarchy 4.0.3 ISO to `/dev/rdisk4` after `sudo dd` failed because sudo needed an interactive password in a non-terminal/background context.^[raw/inbox/2026-09-12.md] The GUI flash path became the chosen route; as of 2026-09-13 the HP device was flashed with this image and is on Tailscale.^[raw/inbox/2026-09-13.md]

Related: [[wiki/entities/macbook-sudo-password|macOS sudo password]], [[wiki/decisions/use-balena-etcher-over-sudo-dd|use Balena Etcher over sudo dd]]
