---
title: "stale-process kill and rescan"
description: "When a watch/scan process overwrites files with stale data, kill it by PID and run a fresh scan with fixed code to restore correct file state."
category: devops
---

# Stale-process kill and rescan

Use when a watch/scan process is overwriting files with old data after a code update, or when scan output JSON diverges from PRINT output (e.g. `skills` field schema mismatch). This is the standard response to the stale-process overwrite incident class, parallel to the token-desync pattern.

## Steps

1. Identify the stale watch/scan process PID(s):
   - Check for running `watch` or `scan` process: `pgrep -fl watch` and `pgrep -fl scan`
   - Distinguish launchd-managed processes (e.g. PID 63983 vs 64044 discrepancy) from direct `mlx_lm` or `scan-topics` spawns
   - Do NOT confuse `mlx_lm` inference server PIDs with watch/scan process PIDs

2. Kill the stale process:
   - `kill <pid>` first; if unresponsive, `kill -9 <pid>`
   - Verify it's gone: `pgrep -f <process-name>` should return empty

3. Run a fresh scan to restore correct state:
   - Execute the scan with the updated code
   - Verify the JSON output matches the PRINT output (e.g., `skills` field is an integer, not an empty array `[]`)

4. Restart the watch process with fixed code (if applicable):
   - Only relaunch after the fresh scan confirms correct output
   - Check if the watch process can push to the remote (not just write locally)

5. Verify consistency:
   - Re-run the scan and confirm the output is stable
   - Confirm no other process is writing to the same files (race condition check)

## Pitfalls

- curl input-waiting can produce false-empty endpoint responses that mimic a desync but are actually a client-syntax problem — use `curl -s` or pipe explicitly
- The `write()` function in scan-topics.py (line 320) replaces `live['bots']` with `snap['bots']`; if a stale process is still running, it will overwrite `snap` output with old data
- PID discrepancies can occur between launchd-managed processes and direct spawns during restarts — always verify the PID that actually owns the port/process
- Always check the scan-topics.py `scan_usage` function when debugging `skills` field type issues, since it also takes bots as input and may merge stale data
- Do not trust file timestamps alone — a stale process may update mtime while writing old data

## Related

- [[topics/self-file/wiki/decisions/watch-process-overwrite-2026-09-09|Watch process data-overwrite restart — 2026-09-09]]
- [[topics/self-file/wiki/decisions/token-desync-2026-09-08|Token desync — 2026-09-08 server restart]]
- [[topics/self-file/wiki/concepts/scan-json-schema|scan-topics.py JSON schema — skills field]]
- [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]]
