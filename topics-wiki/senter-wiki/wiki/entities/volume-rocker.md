---
title: Volume rocker + mute dot
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Volume rocker + mute dot

## Page-level control (Chris trial, kept)
Track length `--volLen` (495px), top anchored to the player so only the bottom moves; hit-zone height derives from it. While `#media.volOpen` or `.drag`, a `document` capture `wheel` listener (`passive:false`) owns the wheel — volume moves, the list does NOT scroll. Direction INVERTED at his request (scroll down = louder); sensitivity proportional to `deltaY`, tuned 3 % → 1.5 % → 2.2 %/event (`Math.max(-.022,Math.min(.022,deltaY*0.0006))`). Scope trap: inside the radio IIFE the player is `m`, not `media`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Look (2026-09-04, "built as you described")
- Top segment: dot at the very top, line down to a cap dot just above the level.
- Gap (10px) = the slider position.
- Bottom segment: cap dot just below the level, line down to a dot at the bottom.
- All four dots 5px, paper colour; the old round knob is gone. Knobs `--volDot` (5px), `--volGap` (10px) on `#mVolTrack`. Bug fixed: bottom cap sat on `#mVolFill` (collapses at volume 0) → anchor both end caps to the track. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Centre derived to 1140 = midpoint of feed-card right edge (1128) and pane edge (1152); 6px left of where it was, "your instinct was exact." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Mute
A 5px dot of the same family floating 14px left of the track at mid-height, toward the app interior (`--volMuteGap`). Muted = hollow ring + rocker dims; hover = attention yellow. Hitbox 26px invisible pad (`--volMuteHit`) with a soft paper glow on entry. ^[raw/inbox/2026-09-05-legacy-inbox.md]

The JS sets `fill.height` and `knob.bottom` as percentages; the whole look is CSS off those two values. ^[raw/inbox/2026-09-05-legacy-inbox.md]

Drives the [[topics-wiki/senter-wiki/wiki/entities/headphone-eq|EQ]] loudness via the [[topics-wiki/senter-wiki/wiki/entities/music-player|player]]; lives in the [[topics-wiki/senter-wiki/wiki/entities/hud-cluster|HUD cluster]]. Colours from [[topics-wiki/senter-wiki/wiki/concepts/paper-palette|paper palette]].
