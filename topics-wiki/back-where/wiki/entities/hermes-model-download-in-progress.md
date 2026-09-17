---
title: "Hermes model download in progress"
created: 2026-09-07
updated: 2026-09-07
type: entity
tags:
  - infra
  - tool
  - timeline
sources:
  - raw/inbox/2026-09-07.md
confidence: high
notes:
  - 20.8GB verification remains open after the last observed status.
---

# Hermes model download in progress

## Timeline
- **01:32**: Download started for a 13GB model file
- **01:40**: Download reported at 13GB, nearly complete
- **02:35**: Chris noted 32GB RAM is sufficient for dual-model operation
- **03:01**: Chris abandoned the 131K audition because it was too slow; generated outputs were retained for later use instead of being discarded, and priority shifted back to optimizing a 27B model
- **04:46**: Follow-up reported the IQ3_XXS download was incomplete at 4.7GB of ~10GB, indicating the earlier 13GB file was not the final completed artifact.
- **08:43**: A separate large-file download was in progress at ~6.5GB of 20.8GB, indicating a larger candidate model was being fetched alongside the incomplete smaller download.
- **08:58**: Download status at 94% (19.7GB / 20.8GB), approximately 1 minute remaining.
- **10:56**: A cache-related issue was noted, prompting a fresh restart check before further action.

> "Download started. Let me wait for it to complete." ^[raw/inbox/2026-09-07.md]

> "Download is at 13GB, nearly done. Let me wait for it to finish." ^[raw/inbox/2026-09-07.md]

> "You have 32 gigabytes, um, and the other one is testing in the background. You should have enough space to at least do a step and not get in the way." ^[raw/inbox/2026-09-07.md]

> "All right, never mind. We didn't go fast enough. My neighbor left After you generate those just put them in a folder We'll do something with those later, but uh, yeah, then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

> "Let me research these models and check what'll fit on this box." ^[raw/inbox/2026-09-07.md]

> "You're absolutely right — I've been sitting idle. Let me fix that. The IQ3_XXS download was incomplete (only 4.7GB of ~10GB). Let me get everything running in parallel." ^[raw/inbox/2026-09-07.md]

> "The large file is still downloading (~6.5GB / 20.8GB). Let me wait for it to complete." ^[raw/inbox/2026-09-07.md]

> "Almost done - 94% (19.7GB / 20.8GB), about 1 minute remaining. Let me wait for completion." ^[raw/inbox/2026-09-07.md]

> "Something's cached. Let me check and restart fresh." ^[raw/inbox/2026-09-07.md]

## Context
The session involved multiple download attempts for Qwen3.8 27B-related quantizations. The 13GB file was reported nearly complete, but later status showed an IQ3_XXS download still needed completion, suggesting parallel or fragmented fetches rather than one finished model.

## Tooling rejected
**FreeToken** was considered and rejected because it is NVIDIA-only (RTX 30/40/50) and will not run on this Mac.

> "FreeToken — NVIDIA-only (RTX 30/40/50). Won't work on Mac." ^[raw/inbox/2026-09-07.md]

## Hardware headroom note
Chris asserted that 32GB RAM should be sufficient to run the audition step without blocking other background testing, treating the machine's capacity as available headroom rather than a limiting constraint.

## Speed-test outcome
Chris decided the 131K audition did not reach acceptable speed. He asked for generated outputs to be retained in a folder for later use, then shifted priority back to optimizing the 27B models rather than continuing the current download/audition path.

## Verification status
**Pending**: Has the 20.8GB model completed downloading and is it loadable in the runtime?
- A cache concern appeared at 10:56 and prompted a fresh restart check, so loadability verification must be attempted against clean runtime state, not the previous session's partial attempt.

## Related
- [[topics-wiki/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics-wiki/back-where/wiki/concepts/model-prefill-fallback|Prefill timeout triggering model fallback]]
- [[topics-wiki/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[topics-wiki/back-where/wiki/queries/20-8gb-download-completion-verification|20.8GB download completion and loadability verification]]
- [[topics-wiki/back-where/wiki/decisions/131k-audition-rejection|131K audition rejection and speed target]]
- [[topics-wiki/back-where/wiki/entities/retained-outputs-folder|Retained outputs folder for rejected 131K audition]]
- [[topics-wiki/back-where/wiki/entities/hardware-headroom-note|Hardware headroom note for M1 32GB]]