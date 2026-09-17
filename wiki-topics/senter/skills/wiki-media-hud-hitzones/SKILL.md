---
name: wiki-media-hud-hitzones
description: Use when touching the wiki music HUD volume/mute/transport. Enforces Chris's locked rocker look and click/scroll zones, DOM-proven.
version: 0.1.0
distilled: 2026-09-05 17:48
topic: senter
---
# wiki-media-hud-hitzones
# Wiki media HUD hit-zones (LOCKED 2026-09-04)

## Visual spec — volume rocker
- Two segments, each capped with a dot; a small visible gap between them IS the slider. Gap slightly larger than the first cut.
- Top and bottom end-dots are FIXED elements on the track (never children of the fill bar — the fill shrinks to zero and drags the dot).
- Maxed high AND maxed low must both read as three dots in succession (end-dot straddled by the segment dots).
- Mute dot: mid-height, on the inner/app-facing side of the rocker. Visually tiny, no glow. Muted = hollow ring + dimmed rocker.

## Interaction zones
- Only clicking the artist or the song title opens the full media player. Nothing else does.
- Volume/mute zone = fixed region from the EQ's left edge ("from the girl's headphones back") to the pane edge, from the top down to the feed's top. In it: hover highlights volume+mute, click toggles mute, scroll moves volume. It is a dead zone for opening the player.
- From her face forward, above the feed chat: click = play/pause toggle.
- Bottom corners hover = raise the feed.

## Rules
1. Transport buttons and `#mNow` must paint ABOVE the mute zone. Prove with `document.elementFromPoint(playCenter)` returning the play button — never assume from z-index reading.
2. Check for later `left:`/`--volShift` overrides on `#mVolZone` before declaring a position fix done; the mute dot must inherit `--volDot` from the track, not the parent.
3. Every change: reload in Chris's real preview and capture; volume level/behaviour must be unchanged (Chris flagged 'the volume volume is different now').
4. Root-cause only — attaching a dot to the fill bar is the canonical band-aid to avoid.

## Evidence
> What if the slider was actually the space between two segments and those segments were both capped with a dot
> you want to make it so maxing out on the bottom also straddles like it does on the top so it looks like three dots together in succession
> I only want clicking on the artists or the song title to open up the full media player
> anywhere from the EQ levels over in that area to make the volume and mute buttons highlight and be clickable to toggle mute on and off and scrollable to make it go up and down
> Let's actually move that to the side of it around the middle just to the left side, so towards the inner side of the app
