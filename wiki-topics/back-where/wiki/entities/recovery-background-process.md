|---
title: "Recovery background process mid-run"
created: 2026-09-06
updated: 2026-09-07
type: entity
tags:
  - infra
  - pain
  - preference
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-06-from-klerik.md
  - raw/inbox/2026-09-07.md
confidence: medium
---

# Recovery background process mid-run

## What happened
A background process exited mid-run during recovery, interrupting an in-flight turn. Chris’s note implies some work may already be complete on disk and should be checked before redoing anything.

> "[System note: Your previous turn was interrupted mid-run — the app or its backend process stopped before the turn could finish. Some of the work may already be complete; check the current state before redoing anything, then finish the task.]" ^[raw/inbox/2026-09-06.md]

> "Background process proc_a2754324cf05 exited (exit code -9)." ^[raw/inbox/2026-09-06.md]

> "Server is running but still loading model into memory. Let me wait." ^[raw/inbox/2026-09-06-from-klerik.md]

## 2026-09-07 follow-up
The same pattern repeated: a turn was interrupted at 11:35 before the requested Calibri/Bonsai action could finish. Chris left a one-line request after the system note, implying the prior work should be inspected before redoing.

> "[System note: Your previous turn was interrupted mid-run — the app or its backend process stopped before the turn could finish. Some of the work may already be complete; check the current state before redoing anything, then finish the task. The interrupted request was:]" ^[raw/inbox/2026-09-07.md]

> "You need to do this for Calibri and bonsai." ^[raw/inbox/2026-09-07.md]

## Relevance
This is part of the same recovery session family: interrupted turn plus later model-load wait both point to unstable runtime paths during repair. The operative behavior is state-check first, then finish the task.

^[raw/inbox/2026-09-06.md]

^[raw/inbox/2026-09-06-from-klerik.md]

^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
- [[wiki-topics/back-where/wiki/entities/hermes-fallback-causes|Hermes fallback causes]]
- [[wiki-topics/back-where/wiki/entities/interrupted-calibri-bonsai-request|Interrupted Calibri and Bonsai request]]
