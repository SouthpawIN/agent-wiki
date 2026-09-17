---
name: stale-process-kill-rescan
description: When a watch/scan process overwrites files with stale data after a code update, kill it by PID and run a fresh scan with fixed code to restore correct file state.
version: 0.1.0
distilled: 2026-09-10 13:30
topic: self-file
---
# stale-process-kill-rescan
# Stale-process kill and rescan

Use when a watch/scan process is overwriting files with old data after a code update, or when scan output JSON diverges from PRINT output (e.g. skills field schema mismatch).

## Steps
1. Identify stale watch/scan process PID(s) via pgrep; distinguish launchd-managed from direct spawns
2. Kill stale process (kill then kill -9 if needed); verify gone
3. Run fresh scan with updated code; verify JSON matches PRINT output
4. Restart watch process with fixed code; check remote-push capability
5. Verify consistency by re-running scan

## Pitfalls
- curl input-waiting mimics desync but is a client-syntax problem
- write() in scan-topics.py line 320 replaces live['bots'] with snap['bots']; stale process overwrites
- PID discrepancies between launchd and direct spawns during restarts
- Check scan_usage function for skills field type issues
- File timestamps alone are untrustworthy — stale process may update mtime while writing old data

## Related
- [[wiki-topics/self-file/wiki/decisions/watch-process-overwrite-2026-09-09|Watch process data-overwrite restart]]
- [[wiki-topics/self-file/wiki/decisions/token-desync-2026-09-08|Token desync — 2026-09-08]]
- [[wiki-topics/self-file/wiki/concepts/scan-json-schema|scan-topics.py JSON schema]]

## Evidence
> When it runs, it overwrites the file with the old data! I need to restart this watch process with the updated code, or kill it and let it be restarted properly
> The scan output shows skills=0 but the file has skills=[]
> Good. Now let me verify it's gone and run a fresh scan:
> At 10:29, after the commit worked, Hermes restarted the watch process with the fixed code and checked whether it could push to the remote
