---
title: "Watch process data-overwrite restart — 2026-09-09"
created: 2026-09-09
updated: 2026-09-10
type: decision
tags: [decision, infra, pain, person]
sources: [raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: low
contested: true
---

# Watch process data-overwrite restart — 2026-09-09

On 2026-09-09, Hermes observed that a running watch process was overwriting files with old data, creating a stale-data consistency issue in the raw→wiki compilation loop. Hermes decided to kill the stale watch process and run a fresh scan to restore correct state. ^[raw/inbox/2026-09-09.md]

## Evidence

- "When it runs, it overwrites the file with the old data! I need to restart this watch process with the updated code, or kill it and let it be restarted properly:" ^[raw/inbox/2026-09-09.md]
- "Good. Now let me verify it's gone and run a fresh scan:" ^[raw/inbox/2026-09-09.md]

## Diagnosis

A stale watch/scan process outlived a code update and continued writing old data to files, mirroring the stale-PID token-desync pattern documented in `[[wiki-topics/self-file/wiki/decisions/token-desync-2026-09-08|Token desync — 2026-09-08 server restart]]`. In both cases, an old process retains state that disagrees with updated on-disk files — the first serves an old `/token` value, the second overwrites file data with stale content. ^[raw/inbox/2026-09-09.md]

## Outcome

Hermes killed the stale watch process and ran a fresh scan to restore correct file state. The process is now running with updated code. The desync remains contested: true pending confirmation that the fresh scan produced consistent, current file data.

## Implication

This is a second incident class of the stale-process pattern (cf. token desync): monitoring/watch processes must be cycled alongside code updates, not just inference servers. The compatibility-check procedure should include verifying that any watch/scan process is running current code before trusting its output.

## Fresh scan and watch-process restart — 2026-09-10

Continuing from the 2026-09-09 kill, at 10:18 Hermes ran a fresh scan to verify the JSON was correct. ^[raw/inbox/2026-09-10.md] At 10:29, after the commit worked, Hermes restarted the watch process with the fixed code and additionally checked whether it could push to the remote. ^[raw/inbox/2026-09-10.md] The restart-with-fixed-code step resolves the overwrite condition from 09-09; the remote-push check extends the procedure to include verifying that the watch process can publish its scan output to the remote, not just write locally.

This remains contested: true — pending confirmation that the restarted watch process (with fixed code) is running current code and that the remote push succeeds without reintroducing stale-data overwrites.

Related: [[wiki-topics/self-file/wiki/entities/hermes|Hermes]], [[wiki-topics/self-file/wiki/decisions/token-desync-2026-09-08|Token desync — 2026-09-08 server restart]], [[wiki-topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], and [[wiki-topics/self-file/wiki/concepts/scan-json-schema|scan-topics.py JSON schema — skills field]].
