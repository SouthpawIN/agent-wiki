---
title: "scan-topics.py JSON schema — skills field"
created: 2026-09-09
updated: 2026-09-10
type: concept
tags: [infra, tool, concept, pain]
sources: [raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: medium
contested: true
---

# scan-topics.py JSON schema — skills field

A `skills` field schema mismatch surfaced in the raw→wiki compilation loop on 2026-09-09. The scan's PRINT output reported `skills=0` (an integer count) while the JSON file written to disk still held `skills=[]` (an empty array). Hermes traced this to the stale watch process running old code that wrote arrays, while the updated code expected integers. ^[raw/inbox/2026-09-09.md]

## Evidence

- "The scan output shows `skills=0` but the file has `skills=[]`. The most likely explanation is that either: 1. The file wasn't actually written with that value, 2. Something overwrote the file after the scan." ^[raw/inbox/2026-09-09.md]
- "Wait, I realize I should just use integers consistently. But actually, looking at the print statement, I changed it to `len(b['skills'])` which handles both. Actually, the current approach works - but let me think about what the vault-live.html expects..." ^[raw/inbox/2026-09-09.md]
- "Actually, I just realized I should check what `write()` function does more carefully - specifically line 320: This should replace `live['bots']` with `snap['bots']`. But wait - what if there's another bot with the same name that has `skills: []` from an earlier scan, and it's being merged somehow? Let me check the `scan_usage` function since it also takes bots as input." ^[raw/inbox/2026-09-09.md]
- "The issue is that the JSON file still has `[]`. Let me check if maybe there's a race condition where another process is also writing to the file, or there's a different write happening." ^[raw/inbox/2026-09-09.md]

## Schema conflict

The `write()` function at line 320 of `scan-topics.py` replaces `live['bots']` with `snap['bots']`, where `snap` is the fresh scan snapshot. ^[raw/inbox/2026-09-09.md] The `skills` field on each bot object in `snap` was expected to be an integer (count of skills), which the PRINT statement confirmed via `len(b['skills'])` — but the on-disk JSON persisted as an empty array `[]`. ^[raw/inbox/2026-09-09.md]

This persisted because the stale watch process — still running old code — kept overwriting the file with its own (array-typed) output after the fresh scan completed. ^[raw/inbox/2026-09-09.md]

## Resolution path

Killing the stale watch process and running a fresh scan with fixed code. ^[raw/inbox/2026-09-09.md] At 10:18 on 2026-09-10, Hermes ran a fresh scan to verify the JSON was correct after the restart. ^[raw/inbox/2026-09-10.md] At 10:29, after the commit worked, Hermes restarted the watch process with the fixed code and checked whether it could push to the remote. ^[raw/inbox/2026-09-10.md]

This remains contested: true — pending confirmation that the restarted watch process (with fixed code) consistently writes `skills` as an integer and that no other process is overwriting the file with stale schema types.

## Related

- [[wiki-topics/self-file/wiki/decisions/watch-process-overwrite-2026-09-09|Watch process data-overwrite restart — 2026-09-09]]
- [[wiki-topics/self-file/wiki/entities/hermes|Hermes]]
- [[wiki-topics/self-file/wiki/concepts/local-model-serving|local model serving]]
