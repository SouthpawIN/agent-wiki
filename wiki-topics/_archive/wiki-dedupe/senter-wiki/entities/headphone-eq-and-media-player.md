---
title: Headphone EQ, media player, volume rocker
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, music, tool]
sources:
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Headphone EQ + media player + rocker

## The EQ (`#hpEq`)
Chris: *"an EQ visualizer, small, over the widest part of the inner circle of the girl's headphones … black dots representing the levels going up and down,
because black on white will be a good contrast."* 7 cols × 6 rows. Anchored to the wallpaper's DRAWN rect (contain/centre, `WALL_AR=1.54`), knobs
`--eqCX/--eqCY` (final 0.8282 / 0.3937), `--eqW/--eqH` (3.2 / 4.6 % of drawn size). Finding the plate: `vision_analyze` on a tight crop of
`assets/wall-contain-1456x914-wallonly.png` — pixel scans grabbed hair. 2 px ≈ 0.0011 w / 0.0017 h. ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]

**"They look gray, not black"** — three rounds; real causes were idle-dot opacity (14–28 %) and 3.5 px anti-aliasing, not z-order. Fix that satisfied him:
every dot always `#000`, `opacity:1`, 4.5 px; level expressed by **size** (`scale(.44)` unlit → `none` lit). *"His picture is pure black/white ink + cross-hatch —
any translucency reads as a mistake against it."* ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]

## Real audio (2026-09-05)
A YouTube iframe gives the page no audio, so the EQ could only "breathe". Root fix: bridge `/music/youtube/search` + `/music/youtube/audio` (yt-dlp in the
Hermes venv, same-origin proxy with Range) → real `<audio>` → Web Audio analyser (`fftSize 64`, 7 bands over the low 60 % of bins, ×1.25). Proof while
*Humanity's Last Breath – Godhood* played: chain `playing/media/wired/analyser/running`, **40 of 42 cells lit**. Type a song name in the player bar to search;
a URL (YouTube / .mp3 / .mp4 / m3u8) still plays directly. Browsers won't autoplay after reload. `load()` must apply the rocker level to each new element
(fixed 17:36). Skill: `wiki-real-audio-pipeline`. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Spotify — blocked on Chris
*"Spotify is blocked on a client ID that doesn't exist anywhere"* — searched `.env`, profile configs, `auth.json`, sessions, the vault; teknium's 09-02 note agrees
`hermes auth spotify` was never run. 2-minute task only Chris can do: developer.spotify.com → create app → redirect URI `http://127.0.0.1:43827/spotify/callback`
→ `hermes auth spotify`. Control needs Premium; status/playlists/search work on Free. See [[wiki-topics/senter-wiki/wiki/queries/open-items-2026-09-05|open items]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Volume rocker (2026-09-04, Chris trial, kept)
Page-level control: `--volLen` 495 px, top anchored to the player. Segmented look — top dot, line to a cap dot above the level, 10 px gap = slider position,
cap dot below, line to bottom dot; all four dots 5 px paper; knobs `--volDot`, `--volGap`. Caps anchored to the track, not `#mVolFill` (collapses at 0).
Mute = 5 px dot 14 px left of the track at mid-height (`--volMuteGap`), 26 px invisible hitbox (`--volMuteHit`), muted = hollow ring + dim rocker, hover = attention
yellow. Wheel owns volume while open (`passive:false`), direction INVERTED (scroll down = louder), sensitivity tuned 3 % → 1.5 % → 2.2 %/event. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Media hit zone (2026-09-04)
From the EQ's left edge (`--eqLeft`, x 936 "her headphones") to the pane edge, top down to where the feed stack begins (~60vh): click toggles mute, wheel moves level,
nothing drawn. Her face forward stays the dead zone (click → SPACE). Chris caught the regression — *"if I click the player buttons they mute and unmute … I still want
clicking on the artist or the title right below the player buttons to open up the media player"* — cause: the zone (`z-index:0`) painted over `z-index:auto` controls.
Fix: lift real controls above the zone; player opens only from `#mNow`. Skill: `wiki-hit-zone-layering`.
([[wiki-topics/senter-wiki/wiki/decisions/2026-09-04-media-zone-and-player-hits|decision]]) ^[raw/inbox/2026-09-05-legacy-inbox.md]
