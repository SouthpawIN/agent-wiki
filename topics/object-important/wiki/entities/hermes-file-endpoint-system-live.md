---
title: "Hermes /file endpoint and system-live.json"
created: 2026-09-08
updated: 2026-09-10
type: entity
tags: [tool, infra, spec]
sources: [raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md]
confidence: high
---

# Hermes /file endpoint and system-live.json

A local Hermes server's file-serving route and the capacity limit that prevents it from serving a larger live-state artifact.

## FILE_CAP blocks system-live.json

^[raw/inbox/2026-09-08.md] The server's `/file` route has a `FILE_CAP` of 2MB, but `.system-live.json` is 2.8MB. The question under consideration was whether the server serves `.system-live.json` via the `/file` endpoint. The size mismatch means the endpoint cannot serve the file as currently configured — the cleanest fix identified was to allow `.system-live.json` to bypass `FILE_CAP` as a special case, since it is the live data contract. Other options considered were raising `FILE_CAP` above 2.8MB, stripping the `text` field when writing live JSON, or serving `.system-live.json` from an in-memory cache regenerated on each scan rather than from disk.

## /file route and client caller

^[raw/inbox/2026-09-08.md] The `/file` route was inspected from the `server.py` content captured in terminal output earlier in the same session. `vault-live.html`'s `loadLive` function fetches this file via `/file` with the token, but the server rejects it with HTTP 413 because it exceeds `FILE_CAP` of 2MB.

## Regeneration lag

^[raw/inbox/2026-09-09.md 20:15] `.system-live.json` retained `"skills": []` after a change that set the value to `0`, indicating the file was not regenerated after the edit. The scan output showed `skills=0` but the file on disk still had `skills: []`.

## Observed stale-write mechanism

^[raw/inbox/2026-09-09.md 20:27] Inspection identified the root cause at line 320: `if OUT.exists(): try: live = json.loads(OUT.read_text())`. The writer reads the existing `.system-live.json`, then merges new data via `live.update(snap)`. Old fields survive even when newer intent changes them. The file on disk had `skills: []` while the scan output showed `skills=0`, confirming the merge preserves stale values.

^[raw/inbox/2026-09-09.md 20:27] A scan confirmed the file was 2931072 bytes, recently updated at 20:27, with no second `.system-live.json` elsewhere and writes going to the expected vault location — the stale behavior is localized to the single merge-write path rather than multiple writers.

## Diagnosis options evaluated

^[raw/inbox/2026-09-09.md 20:34] No alternative `.system-live.json` files were found. The scan correctly writes to the vault location. The issue is confined to the `live.update(snap)` merge step overwriting new scalar values onto stale top-level state.

See also:
- [[topics/object-important/wiki/queries/file-endpoint-cap-question-2026-09-08|2026-09-08: FILE_CAP size mismatch on Hermes /file endpoint]]
- [[topics/object-important/wiki/concepts/git-lfs-model-storage|git-lfs model storage strategy]]
