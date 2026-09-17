---
title: Senter audio bridge (YouTube → <audio>)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, infra, music, ui]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: medium
---

# Senter audio bridge (YouTube → `<audio>`)

The **bridge** is the local component that turns a YouTube pick into a plain HTML `<audio>` element inside the Senter wiki player, replacing the earlier embedded YouTube iframe. It was verified on 2026-09-05 as serving "real audio, 206 with Range — seekable", i.e. it answers HTTP Range requests with 206 Partial Content so the player can scrub. ^[raw/inbox/2026-09-05-legacy-inbox.md]

Because the sound now flows through a real `<audio>` element rather than an opaque iframe, the Web Audio **analyser** can tap it ("the analyser works") and drive the live EQ visual. The analyser "is a passthrough and doesn't change loudness". ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Why it matters
- Enables the [[topics-wiki/youtube/wiki/concepts/youtube-audio-player|YouTube audio player]] in the wiki: search box, live title, live EQ.
- Changed the audio path for the [[topics-wiki/youtube/wiki/entities/volume-rocker|volume rocker]] — it used to talk to YouTube via `postMessage`; now it must drive the bridge's `<audio>` directly.
- Exposed the [[topics-wiki/youtube/wiki/decisions/apply-volume-on-track-load|apply-volume-on-track-load]] bug: a fresh `<audio>` element is born at volume 1.0.

## Provenance note
All four raw lines in the 2026-09-05 filing are the assistant's (hermes) build narration from session `20260903_001447_7bc70a`, not Chris's own words. Chris's stated intent for this player is not yet in `raw/` — only the resulting build is. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Open questions
- Where does the bridge run (senter-bridge on :8643, or a separate process)? Not stated in raw.
- How the YouTube source is fetched/transcoded is not recorded.
