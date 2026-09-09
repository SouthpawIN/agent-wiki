---
title: "Interrupted Calibri and Bonsai request"
created: 2026-09-07
updated: 2026-09-07
type: entity
tags:
  - tool
  - infra
  - pain
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Interrupted Calibri and Bonsai request

## System interruption notice
A session turn was interrupted before completion at 11:35. The partial intent had to be examined for follow-up.

> "[System note: Your previous turn was interrupted mid-run — the app or its backend process stopped before the turn could finish. Some of the work may already be complete; check the current state before redoing anything, then finish the task. The interrupted request was:]" ^[raw/inbox/2026-09-07.md]
> "You need to do this for Calibri and bonsai." ^[raw/inbox/2026-09-07.md]

## Follow-up requests
A second interruption occurred at 13:18 with a different request. Chris later redirected priority to Ornith startup before completing the Calibri and Bonsai work.

> "[System note: Your previous turn was interrupted mid-run — the app or its backend process stopped before the turn could finish. Some of the work may already be complete; check the current state before redoing anything, The interrupted request was:]" ^[raw/inbox/2026-09-07.md]
> "Can you do me a favor and just make sure we get Ornith up first?" ^[raw/inbox/2026-09-07.md]

## Active-task directive
At 14:28, the session instructed that only the latest message should be treated as the active task, with stale snapshot items discarded unless the latest message explicitly asks for them to be finished. This means the Calibri/Bonsai request from the 11:35 interruption is not the active task unless the latest message says so.

> "Treat ONLY the latest message as the active task and discard stale items from '## Historical Task Snapshot' entirely — do not 'wrap up' or 'finish' work described there unless the latest message explicitly asks for it." ^[raw/inbox/2026-09-07.md]

## State verification required
Per the recovery pattern learned: interrupted background processes may complete work on disk; verify state before redoing. Chris's note implies some work may already be complete on disk.

> "Chris's note implies some work may already be complete on disk and should be verified before redoing." ^[raw/inbox/2026-09-07.md]

## Related
- [[topics/back-where/wiki/entities/recovery-background-process|Recovery background process mid-run]]
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/concepts/ornith-startup-priority|Ornith startup priority]]