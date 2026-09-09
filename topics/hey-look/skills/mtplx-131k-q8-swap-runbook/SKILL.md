---
name: mtplx-131k-q8-swap-runbook
description: Use when testing 131K on the 32GB Mac. Behavior: enforce q8/swap, use fixed prompt pair, record tok/s and memory_guard.
version: 0.1.0
distilled: 2026-09-07 04:46
topic: hey-look
---
# mtplx-131k-q8-swap-runbook
# MTPLX 131K q8/swap runbook
1. Export `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES` as explicit size strings like `12G` or `12GiB`.
2. Start MTPLX at 131K with `--paged-kv-quantization q8 --allow-swap`.
3. Warmup is expected around 60-90s; do not measure during warmup.
4. Run the 35-token prompt/800-token generation benchmark.
5. Run the 5K-token prompt/100-token generation benchmark.
6. Capture `tok_s`, `memory_guard`, OOM status, and exact prompt sizes.
7. Do not compare against the pre-q8 8.7 tok/s 131K figure; they are different operating paths.
8. Append dated results to the 65K-vs-131K wiki page.

## Evidence
> **131K context now works with q8 KV cache!**
> Results with `--paged-kv-quantization q8 --allow-swap`: 35 tokens -> 800 tokens = 6.9 tok/s; 5K tokens -> 100 tokens = 0.6 tok/s; No OOM.
