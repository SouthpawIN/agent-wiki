---
title: MPLX Foreground Preemption
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [pain, tool, preference]
| sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-senter.md, raw/inbox/2026-09-07-from-senter-wiki.md]
confidence: medium
---

# MPLX Foreground Preemption

When MTPLX handles long-running Hermes foreground work, postcommit records show `cross_session_foreground_preempted` and `foreground_preempted_postcommit`, and idle async sessions can end with `stored: false` because of `unsafe_reason: retokenized_history_mismatch` ^[raw/inbox/2026-09-07.md].

## Evidence

- postcommit event: `{"admitting_session_id": "anon-41e824508a39fedf", "count": 1, "reason": "cross_session_foreground_preempted", "sessions": ["anon-1acc43591680e54c"]}` ^[raw/inbox/2026-09-07.md].
- idle async session postcommit: `{"mode": "aborted", "reason": "foreground_preempted_postcommit", "session_id": "anon-1acc43591680e54c", "stored": false, "unsafe_reason": "retokenized_history_mismatch"}` ^[raw/inbox/2026-09-07.md].
- Second postcommit: `{"mode": "retokenized_history", "session_commit": {"committed": false, "prefix_len": 26, "reason": "retokenized_prefix_older_than_session"}, "unsafe_reason": "retokenized_history_mismatch"}` ^[raw/inbox/2026-09-07.md].

## Preference

- Finish-state evidence for TurboFit should be captured from Chris's actual Hermes window; postcommit artifacts alone are unreliable under foreground preemption ^[raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-senter-wiki.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/turbofit-mtp-performance.md|TurboFit MTP Performance]]
- [[wiki-topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[wiki-topics/turbofit/wiki/queries/turbofit-mtplx-coexistence.md|MTPLX Coexistence]]
