---
title: TurboFit Session Mismatch
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [pain, infra, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# TurboFit Session Mismatch

MTLPX generation events show foreground/preemption behavior and session-store mismatch that make some TurboFit captures unreliable as finished-state evidence ^[raw/inbox/2026-09-07.md].

## Signals

- `cross_session_foreground_preempted`
- `foreground_preempted_postcommit`
- `unsafe_reason: retokenized_history_mismatch`
- `cache_hit: false`, `cache_miss_reason: ssd_prefix_miss`, `cached_tokens: 0` ^[raw/inbox/2026-09-07.md].

## Impact

- The stored prefix/suffix can differ from the current runtime session history, so Hermes state remains likely but not provably stable from those captures alone ^[raw/inbox/2026-09-07.md].
- Preferred decision path: prefer committed results shown on Chris’s actual Hermes window rather than postcommit cache state ^[raw/inbox/2026-09-07.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/turbofit-verifier-bridge.md|TurboFit Verifier Bridge]]
- [[wiki-topics/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]
