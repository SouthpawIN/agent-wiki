---
name: turbo-fit-evidence-capture
description: Use when capturing TurboFit performance or behavior evidence. Capture from Chris's actual Hermes window using desktop_preview, never from process metadata or postcommit summaries.
version: 0.1.0
distilled: 2026-09-07 00:30
topic: turbofit
---
# turbo-fit-evidence-capture
## TurboFit Evidence Capture

1. Always verify TurboFit state from Chris's actual Hermes window using `desktop_preview`.
2. Never assert preview state from process metadata, exit codes, or speculative reparented session summaries.
3. If a foreground task is preempted, record the preemption event but do not treat the postcommit artifact as finished evidence.
4. Require a real Hermes window capture before claiming any TurboFit behavior as verified.

## Evidence
> Foreground preemption plus retokenized-history mismatch make standalone MTPLX postcommit artifacts unreliable as finished evidence for TurboFit without a real Hermes window capture.
> Verify against actual Hermes window content only; do not assert preview state from process metadata or speculative reparented session summaries.
