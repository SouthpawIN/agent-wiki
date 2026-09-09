---
name: wiki-player-audio-path
description: Use when changing the Senter wiki music player's audio element or source. Apply state on creation, then verify in Chris's window.
version: 0.1.0
distilled: 2026-09-05 18:27
topic: youtube
---
# wiki-player-audio-path
## Rule
Any time the player creates a new audio target (new `<audio>`, new iframe, new bridge stream), apply ALL persisted UI state in the creation path (`load()`), not in the control handlers.

## Steps
1. Locate where the audio element is created (`load()` in vault-live.html / bridge player).
2. Right after creation: set `.volume` from the rocker level, `.muted` from mute state, and re-attach the analyser node.
3. Confirm the analyser is a passthrough (GainNode/AnalyserNode with no gain change) — it must not alter loudness.
4. Confirm the source answers Range requests with 206 so seeking works.
5. Verify in Chris's REAL window (looker capture): set rocker ~30%, load a second track — it must start at 30%. A description of the fix is not done.

## Pitfalls
- `applyVol()` running only on rocker input masks the bug until the first track change; the old YouTube iframe hid this because volume lived in the iframe.
- postMessage volume calls target the iframe — they are dead once the source is `<audio>`; remove or redirect them.
- Fix at the source (creation path), never by programmatically 'nudging' the rocker after load.

## Evidence
> the new bridge `<audio>` element was born at volume 1.0 and `applyVol()` only ran when you moved the rocker — so every track started at full blast until you touched it (the old YouTube iframe happened to mask this)
> Also make the volume rocker drive the bridge audio (it drove YouTube via postMessage before) — check that path
