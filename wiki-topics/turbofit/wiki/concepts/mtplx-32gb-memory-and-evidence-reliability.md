---
title: MTPLX 32GB Memory and Evidence Reliability
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [concept, pain, mtplx, evidence, memory, macos]
sources:
  - [raw/inbox/2026-09-07.md](../../raw/inbox/2026-09-07.md)
  - raw/inbox/2026-09-07-from-senter.md
confidence: medium
contested: true
---

# MTPLX 32GB Memory and Evidence Reliability

Captures two distinct reliability concerns for MTPLX on this box: 131K memory overcommit, and postcommit artifacts that can't be treated as finished TurboFit evidence without a real Hermes window capture ^[raw/inbox/2026-09-07.md].

## Memory overcommit

`mtplx serve --context-window 131072` loads the model and installs the native MTP draft head, but the memory plan marks the context as `OVERCOMMITTED` and warns that the requested context exceeds machine fit for the KV budget ^[raw/inbox/2026-09-07.md].

Live safeguard behavior:

- `prefill_admission_shed` clears KV cache when projected bytes exceed threshold.
- Under real foreground load, background processes still exit with code `-9`.
- Long prompts at 131K return `507 Insufficient Storage` or collapse to sub-1 tok/s ^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-07-from-senter.md].

## Evidence reliability

Postcommit records show `cross_session_foreground_preempted` and `foreground_preempted_postcommit`, with unsafe reasons including `retokenized_history_mismatch`. A completion artifact generated under those conditions is not trustworthy as final TurboFit evidence; the required bar is a Hermes window capture judged from the primary viewport ^[raw/inbox/2026-09-07.md].

## Stable target

65K remains the safe daily context on this box. 131K is a long-context fallback despite throughput collapse and active cache shedding ^[raw/inbox/2026-09-07.md].

## Related

- [[turbofit-mtpl-performance|TurboFit MTPLX Performance]]
- [[mtplx-memory-guard|MPLX Memory Guard]]
- [[context-window-decision|Context Window Decision]]
