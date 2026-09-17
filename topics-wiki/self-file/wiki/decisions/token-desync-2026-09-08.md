---
title: "Token desync — 2026-09-08 server restart"
created: 2026-09-08
updated: 2026-09-09
type: decision
tags: [decision, infra, pain, person]
sources: [raw/inbox/2026-09-08.md]
confidence: medium
contested: true
---

# Token desync — 2026-09-08 server restart

On 2026-09-08, after both local servers came back up, Hermes found the `/token` endpoint returning a stale value different from the newly written token file. The issue was that a previous server process was still alive and fielding requests even after `--new-token` was used to start a fresh process. ^[raw/inbox/2026-09-08.md]

## Evidence

- "Both servers are running. The issue was that curl was waiting for input." ^[raw/inbox/2026-09-08.md]
- "The `/token` endpoint returns the old token `E5vz4M5lt...` but the token file was rewritten with a new one. The server process might have been killed and a new one started but there's a stale process." ^[raw/inbox/2026-09-08.md]
- "The process 63522 is still running, but it was started before the `--new-token` flag was used. The `/token` endpoint says the token is `E5vz4M5lt...` which is the old token. The server was started with `--new-token` but the PID 63522 is not the new process." ^[raw/inbox/2026-09-08.md]
- "Now let me start the server with the patched code: … The server is running with PID 64361 and a new token." ^[raw/inbox/2026-09-08.md]

## Diagnosis

A stale server process (PID 63522) outlived the intended restart. Because the old process held the port and the old token state, the new process (PID 64361) could not fully take over the `/token` endpoint, which kept serving the old value. The token file on disk and the live endpoint disagreed, a classic stale-process-desync condition.

## Outcome

Hermes started a fresh server with PID 64361 and a new token, using patched code. The desync remains contested: true because there is no follow-up verification that PID 64361 actually owns the port and that `/token` now returns the new value consistently. ^[raw/inbox/2026-09-08.md]

## Additional context — 2026-09-08 09:28–09:43

Hermes reported that both servers were running and the initial problem was that curl was waiting for input, producing empty model-endpoint responses. ^[raw/inbox/2026-09-08.md] Hermes then inspected the vault-live.html `loadLive` function to compare what it expects against what the server actually serves. ^[raw/inbox/2026-09-08.md]

A PID discrepancy was noted: Hermes observed PID 63983, not 64044, suggesting a launchd-managed process or another instance was involved. ^[raw/inbox/2026-09-08.md]

## Implication

A repeatable compatibility-check procedure should include killing orphans by PID before reading `/token`. This reinforces the pattern noted in `server-compatibility-constraints`: endpoint/config management is coupled to whether the correct process owns the port. The curl input-waiting issue also shows that endpoint probing can produce false empties that mimic a desync but are actually a client-syntax problem.

Related: [[topics-wiki/self-file/wiki/entities/hermes|Hermes]], [[topics-wiki/self-file/wiki/entities/ornith-server|ornith server]], [[topics-wiki/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]], [[topics-wiki/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]].
