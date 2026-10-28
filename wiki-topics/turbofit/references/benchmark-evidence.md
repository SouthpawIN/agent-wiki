# Benchmark Evidence

What we have measured, and the evidence gaps.

> Grounded in [`external-benchmarks.md`](external-benchmarks.md), [`research-report.md`](research-report.md), and [`benchmark-analysis.md`](benchmark-analysis.md) in the product repo.

## External (discovery evidence only)
- **DeepSWE v1.1** (2026-08-04, 113 tasks, `mini-swe-agent` harness): top frontier agents score 0.53–0.736 pass@1.
  - The **only local Turbofit candidate on DeepSWE is `glm-5-2-2-788bpw`** (0.438 pass@1 → 78.8 bpw) — a 2× jump over the previous local baseline.
  - All frontier API models (Claude, GPT-5.x, Kimi, Gemini, Grok) are `-` (not local candidates).

## Local (the gap)
- **Most local benchmark numbers are missing.** The only measured local numbers recorded so far:
  - GLM-5.1: **1.75 tok/s** on M1 (2026-10-14, single run, not validated)
  - Qwen3-30B: 8.3 tok/s · Qwen3.5-35B-A3B: 4.4 tok/s (earlier runs)
- The "all dashes" in the local benchmark tables is the **#1 evidence gap**: local candidates are not yet benchmarked at Tier-S standard.

## Pending
- **DeepSpec** (DeepSpec-0.5B-DSV4-20260602, 39.1 tok/s draft, 1.77x on 3090, SWE 48.4%) — next local frontier candidate, not yet in the catalog.
- **DeepSWE 2.0** — the next external eval run.

External results are discovery evidence only; Turbofit promotes a local runtime profile only after a reproducible local run passes its gates.
