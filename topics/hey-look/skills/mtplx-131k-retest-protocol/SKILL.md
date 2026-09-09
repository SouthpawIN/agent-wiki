---
name: mtplx-131k-retest-protocol
description: Use when retesting MTPLX 131K speed on a 32GB Mac. This skill fixes the prompt-shape/reasoning-mode/session-cache variability Chris is seeing by defining one reusable retest workflow.
version: 0.1.0
distilled: 2026-09-06 23:36
topic: hey-look
---
# mtplx-131k-retest-protocol
## MT PLX 131K retest protocol

1. Always restart MTPLX between runs; do not benchmark a warm process.
2. Start from `--memory-budget` sized for a 32GB Mac, using the README's 23.6GB peak target for 262K context as the ceiling, not a guessed lower number.
3. For 131K validation, run with 262K context server-side plus `--no-ssd-session-cache`; this combination already proved capable of completing in the raw record.
4. Do not use reasoning-mode prompts as the benchmark stimulus; they can burn the budget before a meaningful speed figure is obtained.
5. Use one stable prompt class per retest pass; switch prompt shapes only when explicitly changing what is being measured.
6. Record: tok/s decode, tok/s prefill, total prompt tokens, reasoning-mode toggle, session-cache flag, and timestamp.
7. Treat a figure as stable only after two consecutive runs agree within 10% on both decode and prefill.
8. If a run dies near completion, treat restart as the default recovery step and resume the same protocol from the beginning of the timed section.

## Evidence
> "MTPLX process died at 19G/20.4G. Nearly done. Let me restart — it should complete quickly now."
> "MTPLX has a `--memory-budget` flag for exactly this."
> "5000 prompt tokens took 158s — the reasoning mode is burning the entire budget thinking."
> "MTPLX is working at 131K context with `--no-ssd-session-cache`."
> "8.2 tok/s at 131K."
