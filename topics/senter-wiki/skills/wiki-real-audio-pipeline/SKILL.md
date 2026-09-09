---
name: wiki-real-audio-pipeline
description: Use when the wiki player, EQ, or volume misbehaves. Real audio only: yt-dlp proxy → <audio> → analyser; never iframe for levels.
version: 0.1.0
distilled: 2026-09-05 17:49
topic: senter-wiki
---
# wiki-real-audio-pipeline
# wiki-real-audio-pipeline

## Rule
The EQ must read REAL levels. A YouTube iframe gives the page no audio — the EQ can only "breathe" (fake). That is dummy behaviour; do not ship it.

## Pipeline (bridge :8643)
1. `GET /music/youtube/search?q=` — no API key; parses the results page. Typing a song name in the player bar hits this. A pasted URL (YouTube / .mp3 / .mp4 / m3u8) plays directly.
2. `GET /music/youtube/audio?...` — yt-dlp (installed in the Hermes venv) resolves the stream; bridge proxies it same-origin WITH Range support (seeking breaks without it).
3. Page: real `<audio>` → Web Audio analyser → EQ cells. Analyser is a passthrough — it must not change loudness.

## Volume
- `load()` MUST apply the current rocker level to every new audio element; a new track that plays at full volume means load() skipped it.
- Rocker and mute drive the same element; mute = hollow ring + dimmed rocker.
- Queue persists across reloads, but browsers block autoplay — Chris presses play; do not fake a playing state.

## Verify (DOM, not screenshot)
Chain reads `playing/media/wired/analyser/running`; count lit EQ cells during a loud section (Godhood breakdown: 40/42). Confirm the play button is the top hit at its own centre (HUD z120).

## Spotify
Blocked on a client ID only Chris can create: developer.spotify.com → app → redirect URI `http://127.0.0.1:43827/spotify/callback` → `hermes auth spotify`. Don't search for it again — it does not exist anywhere on the host.

## Evidence
> YouTube/URL playback is already wired (iframe embed, EQ breathes on iframes). So the player works today with a URL; only Spotify is gated on your ID.
> That's the root fix for the EQ: a YouTube iframe gives the page no audio, so it could only "breathe". Now it's a real `<audio>` → Web Audio analyser → real levels. Proof while Godhood played: analyser chain `playing/media/wired/analyser/running`, **40 of 42 EQ cells lit**
> Confirmed — `load()` never applies the level to the new element. Fix in `load()` so every track starts at your rocker level (and the analyser chain doesn't change loudness — it's a passthrough)
