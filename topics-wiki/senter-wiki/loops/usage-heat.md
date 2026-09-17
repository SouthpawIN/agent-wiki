# Loop: usage-heat (owner: senter · hermes sessions export)
Builds the per-item-per-day mention series that paints every row's heat chart and drives the default sort.

## Native home (verified 2026-09-04, Anser turn 4)
`hermes sessions export --format jsonl --after <date> -` (per profile → loop `-p`). Per-day bucketing stays custom in `assets/scan-topics.py scan_usage`.

## Replaces
Raw SQL on `~/.hermes/state.db messages_fts` — `SCHEMA_VERSION=30`, no stability promise; the FTS layout already changed once (v23). This is exactly the thing `hermes update` will break.

## Cadence
On every scanner pass (watchdog, launchd `com.senter.scanwatch`).

## Status
[QUEUED] — WRAP: same output, native data path.
