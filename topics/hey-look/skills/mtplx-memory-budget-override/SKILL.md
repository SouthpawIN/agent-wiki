---
name: mtplx-memory-budget-override
description: Use when manually sizing MTPLX memory on a memory-constrained Mac. Set session-budget env vars with explicit size strings like `12G` or `12GiB`, restart, and verify warmup.
version: 0.1.0
distilled: 2026-09-07 01:11
topic: hey-look
---
# mtplx-memory-budget-override
## When to use
MTPLX is overcommitted at 131K on a 32GB Mac, or you need to force MTPLX to use more RAM than the default 24GB engine budget.

## Procedure
1. Set `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES` to explicit size strings.
   - Example: `12G` or `12GiB`
2. Restart MTPLX.
3. Watch for warmup complete with tok/s.
4. Test with a prompt larger than 4K tokens; if `memory_guard` clears cache or OOM occurs, lower the budget or use 65K context.

## Pitfalls
- 131K at 32GB Mac is overcommitted: ~19.3GB weights + ~8GB KV = 27.3GB > 24GB budget. Large prompts will OOM or shed cache.
- 65K is the proven stable window: ~4GB KV keeps total near 23.3GB.
- README tok/s figures from faster hardware are not transferable to this box.

## Evidence
> Override: MTPLX_SESSION_BANK_MAX_BYTES / MTPLX_SESSION_BANK_PER_SESSION_BYTES (sizes like 12G or 12GiB).
> The math: 19.3GB (weights) + 8GB (KV at 131K) = 32GB+ — but MTPLX only budgets 24GB for the engine.
> 65K context → ~4GB KV → 19.3 + 4 = 23.3GB → fits in 24GB budget
