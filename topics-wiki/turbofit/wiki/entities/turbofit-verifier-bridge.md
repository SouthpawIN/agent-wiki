---
title: TurboFit Verifier Bridge
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [tool, infra, bot, loop]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# TurboFit Verifier Bridge

`turbofit-verifier` is the existing TurboFit topic bot. This page records the new evidence that it should drive verification through `desktop_preview` on a real Hermes window instead of summary claims, and that long-running TurboFit workstreams need foreground-preemption handling so parked-on-card captures still count toward live work without breaking the 12/20-min sentinel rules ^[raw/inbox/2026-09-07.md].

## Evidence

- "Background process proc_a162ec9b4e3c exited (exit code -9)" while running `mtplx serve` ^[raw/inbox/2026-09-07.md].
- "cross_session_foreground_preempted" and "foreground_preempted_postcommit" during generation, with unsafe reason `retokenized_history_mismatch` ^[raw/inbox/2026-09-07.md].
- `unsafe_reason: retokenized_history_mismatch` and `ssd_prefix_miss` indicate session restore/path mismatch rather than stable committed capture state ^[raw/inbox/2026-09-07.md].

## Standing rule inferred

- Verify against actual Hermes window content only; do not assert preview state from process metadata or speculative reparented session summaries ^[raw/inbox/2026-09-07.md].

## Related

- [[topics-wiki/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics-wiki/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]
