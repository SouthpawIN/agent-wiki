---
title: session-state
updated: 2026-09-02
type: session
---

# Session — hermes-agent

## 2026-09-02 — absorbed hermes-android
_Merged into `hermes-agent` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/hermes-android/.system/`._

### continuity.md (from hermes-android)

# Continuity — hermes-android

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Hermes Agent Android builds
- Language: Shell; 3 stars; last push 2026-07-14; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed hermes-test-skill
_Merged into `hermes-agent` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/hermes-test-skill/.system/`._

### continuity.md (from hermes-test-skill)

# Continuity — hermes-test-skill

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- A test skill for verifying profile-forge works
- Language: None; 0 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed herm-sovth
_Merged into `hermes-agent` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/herm-sovth/.system/`._

### continuity.md (from herm-sovth)

# Continuity — herm-sovth

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- The Hermes TUI built with OpenTUI
- Language: TypeScript; 3 stars; last push 2026-07-14; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed sovth-config
_Merged into `hermes-agent` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/sovth-config/.system/`._

### continuity.md (from sovth-config)

# Continuity — sovth-config

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Southpaw's hermes-agent config toolkit: /reading-list deep-research plugin, profile character cards, ^<profile> background invocation. Distributable, universal, shareable.
- Language: Python; 17 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed nous-test
_Merged into `hermes-agent` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/nous-test/.system/`._

### continuity.md (from nous-test)

# Continuity — nous-test

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Test profile for forge verification
- Language: None; 1 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed test-bot
_Merged into `hermes-agent` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/test-bot/.system/`._

### continuity.md (from test-bot)

# Continuity — test-bot

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Creative operations bot — Discord DM companion for image, music, and video generation
- Language: None; 0 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed openskills
_Merged into `hermes-agent` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/openskills-capabilities/.system/`._

### continuity.md (from openskills)

# Continuity — openskills

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Universal skills loader for AI coding agents - npm i -g openskills
- Language: None; 1 stars; last push 2026-01-18; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 20:15 CDT — teknium: PLAYER real sources wired into senter-bridge (Spotify proxy + YouTube playlist)
- Read `plugins/spotify/{client,tools,__init__}.py` + `hermes_cli/auth.py` (`login_spotify_command`, `resolve_spotify_runtime_credentials`). Auth = ONE command: `hermes auth spotify`. PKCE OAuth, no client secret. A Spotify **Client ID is required**: on first run the command opens developer.spotify.com/dashboard, asks Chris to create a Web API app with redirect URI `http://127.0.0.1:43827/spotify/callback`, prompts for the Client ID and saves it as `HERMES_SPOTIFY_CLIENT_ID` in `~/.hermes/.env`. It then opens the browser, catches the callback on 127.0.0.1:43827, and stores tokens under `providers.spotify` in `~/.hermes/auth.json` (refresh handled by the resolver). Scopes include user-modify/read-playback-state, currently-playing, playlists, library.
- Premium: the bridge only CONTROLS an existing Spotify Connect device (`/me/player/*`). Spotify returns 403 on playback control without Premium (plugin's own message: "Playback control usually requires a Spotify Premium account and an active Spotify Connect device"); read-only status/playlists/search work on Free. The wiki does not embed the Web Playback SDK (which would also need Premium) — audio comes out of whatever Spotify device is active.
- New bridge routes (server.py, imports `plugins.spotify.client.SpotifyClient` — no OAuth re-implementation): `GET /music/spotify/status|playlists|search`, `POST /music/spotify/play|pause|next|prev`, `GET /music/youtube/playlist?id=`. Unauthorized → `{ok:false, needs_auth:true, auth_command:"hermes auth spotify"}` (verified live on all 5 Spotify routes). YouTube: yt-dlp `--flat-playlist -J` if installed (it is not — `which yt-dlp` empty, no `yt_dlp` in the venv), fallback = parse the public page's `ytInitialData` (both the legacy `playlistVideoRenderer` and 2025 `lockupViewModel` shapes). Proven: PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI → 100 items, first "BELLAKEO (Video Oficial) - Peso Pluma, Anitta" (3:55).
- Restarted via `launchctl kickstart -k gui/501/com.senter.bridge`; `/health` ok pid 91039. Mirrored to `assets/senter-bridge/server.py` (md5 match). UI contract filed for weaver as queue item AM.
- Remaining: Chris runs `hermes auth spotify` once. Optional: `brew install yt-dlp` for full (>100 item) playlists and per-item durations from yt-dlp.
