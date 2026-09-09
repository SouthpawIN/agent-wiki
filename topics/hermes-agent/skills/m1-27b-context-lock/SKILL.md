---
name: m1-27b-context-lock
description: Use when evaluating Qwen 3.8 27B on 32GB M1 with MTPLX/DFlash2. Apply memory-cap evidence to choose a stable context lock and avoid impossible 131K targets.
version: 0.1.0
distilled: 2026-09-07 14:11
topic: hermes-agent
---
# m1-27b-context-lock
1. Confirm model variant explicitly before testing: `Qwen 3.8 27B` only. 2. Clean environment first: remove Maple; delete any uncensored model variant; do not stop Hermes Agent. 3. Before treating OOM as a model failure, verify the active server pid — stale wrong-flag processes create false failures. 4. Use live Hermes compression test: realistic workload such as big-essay summarization, then check whether the model works. 5. Measure with streaming so prompt processing and generation tok/s are separate stages; aggregate timing is unreliable. 6. Record actual measurements, not prose summaries: prompt size, tok/s, context size, similarity delta. 7. On `M1 32GB`, record the memory budget: `Qwen 3.8 27B Q3_K_XL = 12.3GB`, `131K KV cache = ~8GB`, `DFlash2 = 1GB`, `macOS + Hermes Agent = 6-8GB`, total `27.3-29.3GB`. 8. Treat `65K` as the stable lockpoint on this hardware; retain `131K` only for long-context needs and record expected lower throughput. 9. Treat `58 tok/s` on `M5 Max` as a hardware reference only, not a target for `M1 32GB`. 10. If the config write refuses to apply a provider lock, switch to the Hermes CLI and only then treat the lock as pending, not done.

## Evidence
> Chris: Must be Qwen 3.8 27B variant. Target: 10+ tok/s at 131K context.
> Chris repeated the cleanup precondition three times in quick succession on 2026-09-07; treat it as a mandatory pre-test step, not optional.
> Hermes reported the tool refused to write to the Hermes config and needed to use the Hermes CLI instead.
> The 10+ tok/s target at 131K is not happening on M1 32GB with a 27B model. It's like asking a Honda Civic to go 200mph. The engine isn't big enough.
