---
name: mtplx-reasoning-budget-troubleshoot
description: Use when a local-serving model returns empty content or stalls on Mac. Behaviour: diagnose the token budget as the cause of reasoning eating the allowance, not the draft method — set --reasoning off or raise the budget to ~4000 tokens, then re-measure.
version: 0.1.0
distilled: 2026-09-15 14:46
topic: hey-look
---
# mtplx-reasoning-budget-troubleshoot
# Reasoning-budget troubleshooting

When a local-serving model (MTPLX, Unleashed, DFlash2, llama.cpp) returns empty content or stalls, the cause is usually the token budget reasoning consumed — not the draft/speculative-decoding method.

## Steps
1. Reproduce: send a prompt that should yield a real answer; note if output is empty or truncated to reasoning traces.
2. Check the reasoning budget. If the model is spending its whole token allowance on reasoning traces, empty content is expected.
3. Fix one of two ways:
   - `--reasoning off` to measure pure decode speed (recovers full tok/s).
   - `--reasoning` ON with a ~4000-token budget so reasoning and content both fit.
4. Re-measure tok/s and confirm the actual answer returns.

## Pitfalls
- Do NOT chase the draft model or speculative-decoding config first — the 2026-09-15 run proved "the issue was never the draft method — it was the token budget."
- Always state whether a reported tok/s figure is reasoning-on or reasoning-off; reasoning-off (e.g. 85.7) is not comparable to reasoning-on (~66-70).
- DFlash2 needs the main model via --spec-draft-model; qwen4 llama.cpp has no --draft-model flag, only --hf-repo-draft (downloads from HuggingFace).

## Evidence
> Empty content — Unleashed's reasoning is eating the token budget. Let me test properly with reasoning disabled and more budget
> The issue is Unleashed's reasoning eating the budget. Let me restart with --reasoning off
> The issue was never the draft method — it was the token budget.
