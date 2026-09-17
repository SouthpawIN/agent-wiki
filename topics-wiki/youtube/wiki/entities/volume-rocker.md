---
title: Volume rocker (wiki player)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, music, tool]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: medium
---

# Volume rocker (wiki player)

The **volume rocker** is the on-screen volume + mute control of the Senter wiki's music player. Its audio target changed when the player moved from a YouTube iframe to the [[topics-wiki/youtube/wiki/entities/senter-audio-bridge|audio bridge]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## History of its audio path
| Date | Path | Notes |
|---|---|---|
| before 2026-09-05 | YouTube iframe via `postMessage` | "it drove YouTube via postMessage before" |
| 2026-09-05 | bridge `<audio>` element via `applyVol()` | "make the volume rocker drive the bridge audio … check that path" |

## Known defect (fixed 2026-09-05)
`applyVol()` only ran when the rocker was moved. Each new bridge `<audio>` element was created at volume 1.0, so "a freshly loaded track ignores your level until you touch it" — every track started at full blast. The old iframe "happened to mask this". Fix recorded in [[topics-wiki/youtube/wiki/decisions/apply-volume-on-track-load|apply volume on track load]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Related
- [[topics-wiki/youtube/wiki/concepts/youtube-audio-player|YouTube audio player]] — the surface the rocker lives on.
