---
title: Execute Code Timeout Behavior
created: 2026-09-10
updated: 2026-09-10
type: concept
tags: [infra, pain, tool]
sources: [raw/inbox/2026-09-09.md]
confidence: medium
---

# Execute Code Timeout Behavior

When Hermes runs `python3` via the `terminal` tool (or `execute_code`), the shell wrapper sometimes emits `[Command timed out...]` before the actual output arrives. The command itself is still executing and completes normally — the timeout message is a shell-wrapper artifact, not a hard kill.

> When I run `python3` via terminal, sometimes it shows `[Command timed out...]` and then shows the actual output! The timeout is just a shell wrapper behavior, but the command still executes. ^[raw/inbox/2026-09-09.md]

## Impact on Verification

This timeout behavior created confusion during the scan-topics.py fix verification. Hermes edited the source file, then attempted to verify via `execute_code`/`terminal` — but the stale results (showing `skills: []` instead of `skills: 0`) were actually produced by:

1. The **watch loop** (`scan-topics.py --watch 20`, process 91303) running old code in a separate shell
2. The **module cache** (`sys.path` prepend causing `import scan_topics` to resolve to `.pyc`)

The timeout noise compounded the difficulty of distinguishing which mechanism was responsible for the stale output.

> My pycache is being used (but I deleted it) ^[raw/inbox/2026-09-09.md]
> 2. There's something modifying the data between scan and write ^[raw/inbox/2026-09-09.md]
> 3. The file was written but then overwritten ^[raw/inbox/2026-09-09.md]

## Related Root Causes

See [[wiki-topics/beyond-pissed/wiki/concepts/scan-loop-schema-fix|Scan Loop Schema Fix]] and [[wiki-topics/beyond-pissed/wiki/concepts/sys-path-module-confusion|sys.path Module Confusion]] for the full root-cause chain.

See also: [[wiki-topics/beyond-pissed/wiki/concepts/vault-live-html-load-verification|Vault-Live HTML Load Verification]]
