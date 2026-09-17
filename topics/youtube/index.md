---
title: youtube
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# youtube

Last updated: 2026-09-15 | Total pages: 6

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Senter audio bridge (YouTube → <audio>)](wiki/senter-audio-bridge.md) — The **bridge** is the local component that turns a YouTube pick into a plain HTML `<audio>` element inside the Senter wiki player, replacing the earlier embedde
- [Volume rocker (wiki player)](wiki/volume-rocker.md) — The **volume rocker** is the on-screen volume + mute control of the Senter wiki's music player. Its audio target changed when the player moved from a YouTube if

### Concepts

- [Mac screen recording](wiki/mac-screen-recording.md) — Screen recording on macOS uses built-in controls in **Screenshot** or **QuickTime Player**.
- [YouTube audio player in the Senter wiki](wiki/youtube-audio-player.md) — The wiki carries a music player whose source is **YouTube**, played as plain audio rather than as an embedded video. The 2026-09-05 build step, in the assistant

### Decisions

- [Decision — apply rocker volume and mute on every track load](wiki/apply-volume-on-track-load.md) — **What**: `load()` in the wiki player now applies the [[topics/youtube/wiki/entities/volume-rocker|rocker]]'s current level and mute state to each new bridge `<

### Queries

- [Mac screen recording hotkeys](wiki/mac-screen-recording-hotkeys.md) — Chris asked the hotkey sequence for starting screen recording on macOS.

---

## SKILLS

Topic skills stored in this wiki:

- **[wiki-player-audio-path](skills/wiki-player-audio-path/SKILL.md) — Any time the player creates a new audio target (new `<audio>`, new iframe, new bridge stream), apply ALL persisted UI state in the creation path (`loa

---

## BOTS

No bots yet.

---

## LOOPS

Proposed loops:

- **[player-regression-check](loops/player-regression-check.md) — owner: looker · cadence: on change to vault-live.html or the bridge source (event-driven, no polling) · status: LIVE
