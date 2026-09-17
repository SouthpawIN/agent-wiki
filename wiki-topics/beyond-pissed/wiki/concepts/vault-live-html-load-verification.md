---
title: Vault-Live HTML Load Verification
created: 2026-09-10
updated: 2026-09-10
type: concept
tags: [tool, infra, ui]
sources: [raw/inbox/2026-09-10.md]
confidence: high
---

# Vault-Live HTML Load Verification

Hermes verified how `vault-live.html` loads and serves live data, tracing through the `loadLive` function and the `/file` route that serves `.system-live.json`.

## Live File Serving

The system serves `.system-live.json` via a `/file` route. On 2026-09-10 Hermes directly checked the current git state and the JSON file to confirm that `.system-live.json` is correctly updated and accessible^[raw/inbox/2026-09-10.md].

## Token Rotation

The token used by Hermes changes when `--new-token` is invoked. After a token rotation, `.system-live.json` should be reread through the `/file` route; previously loaded session/system state must never be assumed current^[raw/inbox/2026-09-10.md].

## vault-live.html Inspection

Hermes inspected `vault-live.html`'s `loadLive` function, verified the BOTS view and session display, and confirmed the CSS is well-structured. A footer containing the agent-wiki GitHub reference was added to the end of the file^[raw/inbox/2026-09-10.md].

## Continuous Scan Loop

A `scan-topics.py --watch 20` loop is running continuously, repacking data into `.system-live.json` every 20 seconds. This process is actively modifying data and must be accounted for when verifying live state^[raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md].

## Git Repository Status

On 2026-09-10 Hermes confirmed the live git repository at `~/Documents/Projects/Projects` is on branch `main` with origin `https://github.com/SouthpawIN/agent-wiki`. The working tree carries many uncommitted changes^[raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]. The `main` branch has no upstream set — see [[wiki-topics/beyond-pissed/wiki/queries/git-upstream-not-set|Git Upstream Not Set on main Branch]]^[raw/inbox/2026-09-10.md].

See also: [[wiki-topics/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[wiki-topics/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[wiki-topics/beyond-pissed/wiki/concepts/readme-rendering-issue|README Rendering Issue]], [[wiki-topics/beyond-pissed/wiki/decisions/fix-discrepancy-to-updates|Fix Discrepancy to Updates]]
