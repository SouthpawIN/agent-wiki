---
title: MTPLX Memory Guard
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [infra, pain, tool]
sources: [raw/inbox/2026-09-07-from-senter.md]
confidence: medium
---

# MTPLX Memory Guard

MTPLX emits a memory-guard `prefill_admission_shed` event when a prompt would push the active process above its memory threshold, clearing the KV cache before admission to keep the projected bytes under the threshold ^[raw/inbox/2026-09-07-from-senter.md].

## Evidence

- Event: `{"action": "prefill_admission_shed", ...}` triggered for a 5016-token prompt ^[raw/inbox/2026-09-07-from-senter.md].
- Pre-admission values: `active_bytes: 20.70 GB`, `cache_bytes: 2.00 GB`, `projected_bytes: 26.26 GB`, `threshold_bytes: 24.99 GB`, `limit_bytes: 25.77 GB` ^[raw/inbox/2026-09-07-from-senter.md].
- Behavior: `cache_cleared: true`, then projected dropped to `24.25 GB` and was admitted against the `24.99 GB` threshold ^[raw/inbox/2026-09-07-from-senter.md].

## Note

- This is a live runtime safeguard, not an application prefetch guarantee. It shows that long-prompt admission is actively shedding cache to stay under the memory budget, which can stall throughput and explain apparent cache-hit variability.

## Related

- [[topics/turbofit/wiki/entities/turbofit-mtp-performance.md|TurboFit MTP Performance]]
- [[topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[topics/turbofit/wiki/queries/turbofit-mtplx-coexistence.md|MTPLX Coexistence]]
