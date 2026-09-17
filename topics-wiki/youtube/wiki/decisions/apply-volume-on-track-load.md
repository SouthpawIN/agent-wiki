---
title: Decision — apply rocker volume and mute on every track load
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, pain, music, ui]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Decision — apply rocker volume and mute on every track load

**What**: `load()` in the wiki player now applies the [[topics-wiki/youtube/wiki/entities/volume-rocker|rocker]]'s current level and mute state to each new bridge `<audio>` element "the moment it's created". ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Why**: After the switch to the [[topics-wiki/youtube/wiki/entities/senter-audio-bridge|audio bridge]], "the new bridge `<audio>` element was born at volume 1.0 and `applyVol()` only ran when you moved the rocker — so every track started at full blast until you touched it (the old YouTube iframe happened to mask this)". ^[raw/inbox/2026-09-05-legacy-inbox.md]

**When**: 2026-09-05, 17:36 (cause hypothesised) → 17:37 (confirmed and fixed), session `20260903_001447_7bc70a`.

**Evidence chain**
1. 17:29 — rocker must drive bridge audio; "check that path".
2. 17:36 — "Likely cause: the new `<audio>` element is created at volume 1.0 … Let me confirm and fix at the source".
3. 17:37 — "Found it … Now `load()` applies your rocker level and mute state to every new track".

**Ruled out**: the analyser — "a passthrough and doesn't change loudness".

**Verification status**: the raw record contains the fix claim only; no capture of Chris's window confirming a second track starts at the set level is filed. Per Chris's standard, unverified = not done. See [[topics-wiki/youtube/wiki/concepts/youtube-audio-player|YouTube audio player]].
