# hey-look BRIEF

## Learned

- Chris asks direct lookups for Mac-local model claims, with specific hardware constraints (32GB+ Mac).
- Follow-up speed comparisons should include longer context lengths if a baseline was reported.
- When MTPLX stalls near completion at 19G/20.4G, restarting is an effective recovery step.
- Hermes identified MTPLX's `--memory-budget` flag as the correct sizing control for a 32GB Mac after correcting a README peak-memory math error.
- 131K context tests required restarting MTPLX with 262K context and `--no-ssd-session-cache`; figures are still inconsistent across prompt sizes.
- Stable 131K benchmarking remains open; a single retest protocol is still needed before treating any figure as final.
- Integration pending: auxiliary compression and the model catalog still need to switch to MTPLX as the main provider.
- Long-context results are prompt-shape sensitive; a 5000-token warmup can take 158s in reasoning mode before meaningful speed measurements begin.
- Stable 131K benchmarking remains open; Hermes planned an increase-size sweep but the raw record ends before a single retest protocol is chosen.
- Chris directly set `MTPLX_SESSION_BANK_MAX_BYTES` / `MTPLX_SESSION_BANK_PER_SESSION_BYTES` with size strings like `12G` or `12GiB`, making the memory budget explicitly tunable rather than README-derived.
- On the current 32GB Mac, 65K context is stable and fast; 131K remains unverified for large prompts despite the override.
- `--paged-kv-quantization q8 --allow-swap` makes 131K non-OOM on this box at lower speed: ~6.9 tok/s short prompt, ~0.6 tok/s 5K prompt.
- Same-day same-box 131K comparison shows Unleashed + DFlash2 uses ~13GB vs MTPLX ~20GB, faster on medium prompts, uncensored.
- HuggingFace search for DFlash2 on the base Qwen 3.8 27B model is still open/unresolved from the latest raw slice.
- Chris issued a port-mapped 131K test protocol: port 11613 = MTPLX Qwen 3.8 27B optimized speed, port 11606 = Unleashed + DFlash2, with explicit prompt shapes (short 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens).^[raw/inbox/2026-09-07.md]
- 10+ tok/s at 131K on this M1 32GB box is impossible because 27B + KV + macOS + Hermes totals 22-36GB against 32GB total; the M5 Max README 58 tok/s used a faster memory bus with almost nothing else running.^[raw/inbox/2026-09-07.md]
- A 5010-token 65K prompt hit `memory_guard` `prefill_admission_shed` with exact bytes: `active_bytes` 20.3GB, `cache_bytes` 1.5GB, `projected_bytes` 25.0GB, threshold 24.0GB, limit 25.8GB, `cache_cleared: true`, post-clear `projected_bytes_after` 24.0GB.^[raw/inbox/2026-09-07.md]
