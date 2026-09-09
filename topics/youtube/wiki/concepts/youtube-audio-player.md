---
title: YouTube audio player in the Senter wiki
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [music, ui, plan, idea]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: medium
---

# YouTube audio player in the Senter wiki

The wiki carries a music player whose source is **YouTube**, played as plain audio rather than as an embedded video. The 2026-09-05 build step, in the assistant's words: "Now the player: YouTube → `<audio>` via the bridge (the analyser works), search box, and everything stays live (title, EQ)". ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Components
- **Source**: YouTube, resolved through the [[topics/youtube/wiki/entities/senter-audio-bridge|audio bridge]] into a seekable `<audio>` stream (HTTP 206 / Range).
- **Search box**: pick a track by searching YouTube from inside the wiki.
- **Live title**: the now-playing title updates as tracks change.
- **Live EQ**: a Web Audio analyser (passthrough, no loudness change) feeds the equalizer visual.
- **[[topics/youtube/wiki/entities/volume-rocker|Volume rocker]]**: volume + mute, now driving the bridge `<audio>` directly.

## Design principle observed
"Everything stays live" — title and EQ must not freeze when the audio path changes. Fixes are made "at the source" (in `load()`), not by nudging the rocker after the fact; see [[topics/youtube/wiki/decisions/apply-volume-on-track-load|apply volume on track load]]. This matches Chris's standing rule of root causes over band-aids. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Gaps in the record
No raw line from Chris himself yet describes why he wants YouTube-as-audio in the wiki (vs. Spotify, which needs a Dev-app client_id per Senter notes), what a "done" player looks like, or a playlist/queue model. Those are assistant lines only.
