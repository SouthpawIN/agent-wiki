---
name: live-model-evaluation
description: Use when running a live Hermes model check. Execute a compression test, measure tok/s and similarity, and report pass/fail against Chris's target.
version: 0.1.0
distilled: 2026-09-07 04:32
topic: hermes-agent
---
# live-model-evaluation
## Procedure
1. Confirm the active Hermes provider and session id.
2. Start a realistic compression workload: big-essay summarization.
3. Measure streaming tok/s separately from prompt-processing time.
4. Capture similarity delta across the run.
5. Report one line: target, measured tok/s, similarity, pass/fail.
6. On OOM or degraded behavior, report the failure mode and suggest config paths; do not silently retry or hide the miss.

## Pitfalls
- Restart Hermes after provider/config changes so the active server picks them up.
- Treat Hermes Agent's own ~2-4GB as non-negotiable host overhead when sizing context.
- Delete or disable distracting models/variants before clean evaluation.

## Evidence
- "Now a realistic compression test — big essay summarization"
- "checking out if this model works"
- "I need to improve the script with streaming to separate prompt processing from generation time for accurate tok/s"

## Evidence
> Now a realistic compression test — big essay summarization
> checking out if this model works
> I need to improve the script with streaming to separate prompt processing from generation time for accurate tok/s
