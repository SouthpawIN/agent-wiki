# inbox — youtube
_Filed by the watcher per message (Chris 2026-09-05: "per message, like Cursor"). Raw context; the topic loop distils it._


## 2026-09-05 17:29 · hermes · 20260903_001447_7bc70a · sim 0.09
Real audio, 206 with Range — seekable. Now the player: YouTube → `<audio>` via the bridge (the analyser works), search box, and everything stays live (title, EQ):

## 2026-09-05 17:29 · hermes · 20260903_001447_7bc70a · sim 0.08
Also make the volume rocker drive the bridge audio (it drove YouTube via postMessage before) — check that path:

## 2026-09-05 17:36 · hermes · 20260903_001447_7bc70a · sim 0.11
Likely cause: the new `<audio>` element is created at volume 1.0 — `applyVol` only runs when you move the rocker, so a freshly loaded track ignores your level until you touch it. Let me confirm and fix at the source:

## 2026-09-05 17:37 · hermes · 20260903_001447_7bc70a · sim 0.16
Found it: the new bridge `<audio>` element was born at volume 1.0 and `applyVol()` only ran when you moved the rocker — so every track started at full blast until you touched it (the old YouTube iframe happened to mask this). Now `load()` applies your rocker level and mute state to every new track the moment it's created. The analyser itself is a passthrough and doesn't change loudness.
