---
title: MTPLX 131K systematic retest
created: 2026-09-06
updated: 2026-09-07
type: query
tags: [benchmark, mtplx, protocol, question]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: medium
---

# MTPLX 131K systematic retest

An unfinished attempt to establish one stable long-context benchmark for MTPLX on a 32GB Mac.^[raw/inbox/2026-09-06.md]

## What happened

- After initial 131K results varied by prompt size, Hermes shifted to a planned increase-size sweep to find the actual limit.^[raw/inbox/2026-09-06.md]
- The session explicitly stated it would test at increasing sizes after finding 131K worked with 262K context and `--no-ssd-session-cache`.^[raw/inbox/2026-09-06.md]
- The raw record ends before a single retest protocol is chosen or completed.^[raw/inbox/2026-09-06.md]
- A subsequent Hermes turn noted MTPLX is up with 131K context and that it would test speed and large prompts again.^[raw/inbox/2026-09-07.md]
- During that turn, Hermes reported deleting Maple and Unleashed and cleaning the MTPLX setup, then observed server logs showing `remaining: 60526` for a 5020-token prompt — implying an effective 65K usable window instead of 131K. This raises a new hypothesis that MTPLX may be capping the context window, which would change the retest strategy.^[raw/inbox/2026-09-07.md]
|- The same raw slice includes Chris's explicit override of `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES`, making the budget tunable but still without a stable large-prompt 131K measurement until the later q8/swap path restored non-OOM behavior at lower speed.^[raw/inbox/2026-09-07.md]
|- Chris defined the retest protocol as short prompt 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens, with port 11613 for MTPLX and port 11606 for Unleashed + DFlash2.^[raw/inbox/2026-09-07.md]
- MTPLX's own memory plan later showed 19.3GB weights + ~8GB KV at 131K = 27.3GB against a 24GB engine budget, so 131K is overcommitted on this hardware regardless of override.^[raw/inbox/2026-09-07.md]
- A clean 65K large-prompt measurement was produced in the same raw slice: 8.55 tok/s for 685 tokens and 8.43 tok/s for 5010 prompt tokens with cache shedding; these should be used as the stable baseline for future retests.^[raw/inbox/2026-09-07.md]
- The later q8/swap path showed 131K can be stable for non-OOM workloads at lower throughput: 6.9 tok/s on a 35-token prompt/800-token generation and 0.6 tok/s on a 5K prompt/100-token generation.^[raw/inbox/2026-09-07.md]
- The same raw slice recorded an explicit rejection of the 10+ tok/s 131K target on this M1 32GB box, with the same-day survey concluding the only path to materially higher throughput is a 64GB+ RAM machine.^[raw/inbox/2026-09-07.md]

## Why it matters

Chris asked for a direct long-context speed comparison. Until there is one retest protocol, no 131K figure should be treated as final.^[raw/inbox/2026-09-06.md]

## Related

- [[queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[decisions/context-benchmark-request|Context benchmark request]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
- [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
