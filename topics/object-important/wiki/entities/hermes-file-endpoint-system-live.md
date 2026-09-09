---
title: "Hermes /file endpoint and system-live.json"
created: 2026-09-08
updated: 2026-09-08
type: entity
tags: [tool, infra, spec]
sources: [raw/inbox/2026-09-08.md]
confidence: high
---

# Hermes /file endpoint and system-live.json

A local Hermes server's file-serving route and the capacity limit that prevents it from serving a larger live-state artifact.

## FILE_CAP blocks system-live.json

^[raw/inbox/2026-09-08.md] The server's `/file` route has a `FILE_CAP` of 2MB, but `.system-live.json` is 2.8MB. The question under consideration was whether the server serves `.system-live.json` via the `/file` endpoint. The size mismatch means the endpoint cannot serve the file as currently configured — the fix is to raise `FILE_CAP` above 2.8MB so the route can serve the live-state JSON.

## /file route

^[raw/inbox/2026-09-08.md] The `/file` route was inspected from the server.py content captured in terminal output earlier in the same session.

See also:
- [[topics/object-important/wiki/concepts/watcher-status-noise|Watcher status noise]]
- [[topics/object-important/wiki/queries/no-topic-substance-2026-09-07|2026-09-07: no actionable object-important substance in raw/inbox]]
