---
title: Music player + YouTube audio + Spotify gate
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, music, pain]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Music player + YouTube audio + Spotify gate

## What plays
- YouTube / .mp3 / .mp4 / m3u8 URL playback via iframe embed worked first ("EQ breathes on iframes" — no audio exposed). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **2026-09-05 17:34 — live, not demo**: bridge `/music/youtube/search` (no API key, parses the results page) + `/music/youtube/audio` (yt-dlp in the Hermes venv resolves the stream; bridge proxies same-origin with Range). Real `<audio>` → Web Audio analyser → real levels. Proof while *Humanity's Last Breath – Godhood* (official, 3:23) played: analyser chain `playing/media/wired/analyser/running`, **40 of 42 EQ cells lit** on the breakdown. "Type a song name in the player bar to search; a URL still plays directly. Queue persisted — hit play to hear it (browsers won't autoplay after a reload)." ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Fix 17:36: `load()` never applied the rocker level to a new element → every track now starts at the [[wiki-topics/senter-wiki/wiki/entities/volume-rocker|rocker]] level; the analyser is a passthrough. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Interaction rules (Chris, 2026-09-04 15:26)
"if I click the player buttons they mute and unmute … I still want the player buttons to work And I still want clicking on the artist or the title right below the player buttons to open up the media player." → player opens ONLY from `#mNow` (title/artist); transport buttons keep their jobs; other widget clicks are swallowed. Cause: the fixed media zone at `z-index:0` painted over `z-index:auto` buttons — lift the real controls above it. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Media zone
From the EQ's left edge (`--eqLeft`, x 936 = her headphones) to the pane edge, top down to where the feed stack begins (~60vh, y 497): rocker + mute show, click toggles mute, wheel moves the level. Nothing drawn. Her face forward (left of the EQ, above the feed) stays the dead zone → click toggles SPACE; bottom corner = the feed's hover. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Spotify — blocked on Chris
"Spotify is blocked on a client ID that doesn't exist anywhere" — searched `.env`, all profile configs, `auth.json`, sessions, the vault; teknium's 09-02 note agrees `hermes auth spotify` was never run. Only Chris can do it: developer.spotify.com → create app → redirect URI `http://127.0.0.1:43827/spotify/callback` → `hermes auth spotify`, paste the ID. Control needs Premium; status/playlists/search work on Free. Listed in [[wiki-topics/senter-wiki/wiki/queries/open-items-as-of-2026-09-05|open items]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

Visualiser: [[wiki-topics/senter-wiki/wiki/entities/headphone-eq|headphone EQ]]. Container: [[wiki-topics/senter-wiki/wiki/entities/hud-cluster|HUD cluster]]. Layer z120 ([[wiki-topics/senter-wiki/wiki/concepts/layer-stack|layer stack]]).
