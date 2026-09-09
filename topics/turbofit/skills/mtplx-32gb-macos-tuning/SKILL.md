---
name: mtplx-32gb-macos-tuning
description: Use when tuning MTPLX on 32GB macOS. Check runtime config instead of unsupported CLI flags; validate context window against machine-bound memory plan before relying on tok/s claims.
version: 0.1.0
distilled: 2026-09-07 01:02
topic: turbofit
---
# mtplx-32gb-macos-tuning
1. Treat `--memory-budget` as unsupported on `mtplx serve`; do not retry it.
2. Read MTPLX runtime config/env docs for macOS MLX memory controls.
3. Before declaring any context window stable, require a Hermes window capture — postcommit artifacts are unreliable under foreground preemption.
4. When MTPLX is preempted or exits -9, fall back to Unleashed Q3_K_XL rather than retrying the same overcommitted window.
5. Do not use admission-shed tok/s as a stable throughput claim; it is raw telemetry showing cache clearing under memory pressure.

## Evidence
> --memory-budget is not accepted by mtplx serve
> requested context 131072 exceeds the machine fit 8192
> MTPLX service exits with code -9 under load
> Keep the Unleashed Q3_K_XL as backup (slower but handles 131K via llama.cpp offload)
