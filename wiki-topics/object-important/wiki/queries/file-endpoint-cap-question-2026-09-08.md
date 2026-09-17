---
title: "2026-09-08: FILE_CAP size mismatch on Hermes /file endpoint"
created: 2026-09-08
updated: 2026-09-09
type: query
tags: [question, tool]
sources: [raw/inbox/2026-09-08.md]
confidence: high
---

# 2026-09-08: FILE_CAP size mismatch on Hermes /file endpoint

## Question raised

^[raw/inbox/2026-09-08.md] Does the server serve `.system-live.json` via the `/file` endpoint?

## Answer

The `/file` route exists but is gated by `FILE_CAP`, set to 2MB. The `.system-live.json` artifact is 2.8MB, so the route rejects it. The cleanest path forward identified was allowing `.system-live.json` to bypass `FILE_CAP` as a special case; alternatives were raising `FILE_CAP`, stripping the `text` field from live JSON, or serving the file from an in-memory cache.

## Later evidence

^[raw/inbox/2026-09-09.md] After the initial capacity question, later observation showed `.system-live.json` can also become stale because the writer merges into the existing file rather than regenerating it; this extends the `/file` issue beyond transport capacity to live-state correctness.

See also:
- [[wiki-topics/object-important/wiki/entities/hermes-file-endpoint-system-live|Hermes /file endpoint and system-live.json]]
- [[wiki-topics/object-important/wiki/concepts/watcher-status-noise|Watcher status noise]]
