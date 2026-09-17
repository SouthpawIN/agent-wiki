---
name: provider-lock-validation
description: Use when a provider lock is recorded or proposed. Validate acceptance criteria before treating it as final.
version: 0.1.0
distilled: 2026-09-07 10:06
topic: hermes-agent
---
# provider-lock-validation
1. Require explicit confirmation of both model variant and throughput target before accepting a lock. 2. If the lock was recorded before Chris's explicit confirmation, mark it contested/provisional in the wiki. 3. Before treating OOM or slowdown as a model failure, verify the active provider pid; stale wrong-flag attempts produce false failures. 4. After config changes, restart Hermes Agent to pick them up and re-verify the active server pid. 5. Report tok/s using streamed measurement that separates prompt processing from generation time.

## Evidence
> Unleashed + DFlash2 is locked in as the main provider at 131K context.
> Must be Qwen 3.8 27B variant. Target: 10+ tok/s at 131K context.
> The failed process was just a stale attempt with the wrong flag — the active server (pid 60316) is up.
> I need to improve the script with streaming to separate prompt processing from generation time for accurate tok/s.
