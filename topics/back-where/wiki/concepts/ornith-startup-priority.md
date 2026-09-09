---
title: "Ornith startup priority"
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - tool
  - infra
  - priority
sources:
  - raw/inbox/2026-09-07.md
confidence: medium
---

# Ornith startup priority

## Observation
During recovery, Chris explicitly requested that Ornith be started before addressing Calibri and Bonsai. This appeared as a pre-requisite request when previous turns were interrupted. The same request was repeated multiple times after API retry interruptions, indicating stalled progress on the Ornith startup step. Chris also noted that other models were added to the list without his request, but said they could remain.

> "Can you do me a favor and just make sure we get Ornith up first?" ^[raw/inbox/2026-09-07.md]

> "Yes, I want you to do that because there was other models added that I didn't ask for We can keep those on there, but you were able to do it previously now add ornith to that can fit for me. Thank you" ^[raw/inbox/2026-09-07.md]

> "Treat ONLY the latest message as the active task and discard stale items from '## Historical Task Snapshot' entirely — do not 'wrap up' or 'finish' work described there unless the latest message explicitly asks for it." ^[raw/inbox/2026-09-07.md]

## Status
The request was interrupted by API retry errors at 13:19 and 13:29. The startup of Ornith needs to be verified before proceeding with Calibri or Bonsai actions.

> "Operation interrupted: retrying API call after error (retry 1/3)." ^[raw/inbox/2026-09-07.md]

## 14:28 live-task directive
Chris later specified that only the latest message should be treated as the active task, with stale snapshot items discarded unless the latest message explicitly asks for them to be finished. This keeps the current focus on getting Ornith up rather than retroactively finishing the Calibri/Bonsai request from the 11:35 interruption.

> "Treat ONLY the latest message as the active task and discard stale items from '## Historical Task Snapshot' entirely — do not 'wrap up' or 'finish' work described there unless the latest message explicitly asks for it." ^[raw/inbox/2026-09-07.md]

## Persistence requirement
Chris explicitly asked that Ornith be added to the existing model list because it can fit there. He noted that other models had been added without his request, but said they can remain, so Ornith should coexist with the current set instead of replacing it.

> "Yes, I want you to do that because there was other models added that I didn't ask for We can keep those on there, but you were able to do it previously now add ornith to that can fit for me. Thank you" ^[raw/inbox/2026-09-07.md]

## Calibri/Bonsai context
The Ornith request preceded the Calibri and Bonsai work. Calibri/Bonsai should not be resumed unless the latest message explicitly reopens that thread.

## Verification requirement
Before any local completion is claimed, Hermes must verify the runtime/model list with Ornith present and executable in the actual Hermes surface.

## Related
- [[topics/back-where/wiki/entities/interrupted-calibri-bonsai-request|Interrupted Calibri and Bonsai request]]
- [[topics/back-where/wiki/concepts/recovery-repair-plan|Recovery repair plan]]
- [[topics/back-where/wiki/entities/hermes-model-download-in-progress|Hermes model download in progress]]
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/concepts/model-prefill-fallback|Prefill timeout triggering model fallback]]
