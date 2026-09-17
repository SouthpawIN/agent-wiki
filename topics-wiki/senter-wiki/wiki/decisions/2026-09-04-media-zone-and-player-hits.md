---
title: Decision: media hit zone from the EQ to the pane edge; player opens only from title/artist
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, music]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# Media zone + player hits (2026-09-04 15:19–15:27)

**What.** Invisible media area from the EQ's left edge (x 936, `--eqLeft`) to the pane edge, top down to the feed top (~60vh): click toggles mute, wheel moves the level,
nothing drawn. Her face forward stays the SPACE dead zone; the bottom corner remains the feed's hover. Player opens only from `#mNow` (title/artist). ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Chris's correction that shaped it.** *"if I click the player buttons they mute and unmute … I still want the player buttons to work And I still want clicking on the artist or
the title right below the player buttons to open up the media player."* Root cause: the fixed zone at `z-index:0` painted over `z-index:auto` controls. Fix: lift the real
controls above the zone (skill `wiki-hit-zone-layering`). ^[raw/inbox/2026-09-05-legacy-inbox.md]

Related: [[topics-wiki/senter-wiki/wiki/entities/headphone-eq|EQ + player]], [[topics-wiki/senter-wiki/wiki/concepts/row-geometry-and-dot-column|derived anchors]].
