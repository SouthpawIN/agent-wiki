---
title: "2026-09-08: FILE_CAP size mismatch on Hermes /file endpoint"
created: 2026-09-08
updated: 2026-09-08
type: query
tags: [question, tool]
sources: [raw/inbox/2026-09-08.md]
confidence: high
---

# 2026-09-08: FILE_CAP size mismatch on Hermes /file endpoint

## Question raised

^[raw/inbox/2026-09-08.md] Does the server serve `.system-live.json` via the `/file` endpoint?

## Answer

The `/file` route exists but is gated by `FILE_CAP`, set to 2MB. The `.system-live.json` artifact is 2.8MB, so the route rejects it. The path forward is raising `FILE_CAP` to exceed 2.8MB.

See also:
- [[topics/object-important/wiki/entities/hermes-file-endpoint-system-live|Hermes /file endpoint and system-live.json]]
- [[topics/object-important/wiki/concepts/watcher-status-noise|Watcher status noise]]
