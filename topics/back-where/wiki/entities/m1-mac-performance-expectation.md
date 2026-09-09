---
title: "M1 Mac performance expectation"
created: 2026-09-06
updated: 2026-09-06
type: entity
tags:
  - preference
  - tool
  - infra
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-06-from-klerik.md
  - raw/inbox/2026-09-07.md
confidence: high
---

# M1 Mac performance expectation

## Hardware context
Chris asserted the host hardware should handle the workload: an M1 MacBook with 32 GB RAM running a model smaller than 27b, with no extra limitations imposed.

> "That is complete bullshit. You need to do more research because someone got this running at like 113 tokens a second on an iPhone This is an M1 MacBook with 32 gigabytes of RAM and this model is smaller than the 27b and I know that there's a lot of development around this model and Mac" ^[raw/inbox/2026-09-06.md]

> "You absolutely can I gave you no limitations. I said put it as the auxiliary model. That's it" ^[raw/inbox/2026-09-06.md]

## Capacity claim
He stated there is enough room to run the chosen model at Q3 with 262k contacts alongside the D flash 2 model, and expected configuration rather than another retry loop.

> "There is more than enough space to fit this model at Q3 with 262k contacts and the D flash 2 model and run everything else more than enough" ^[raw/inbox/2026-09-06.md]

^[raw/inbox/2026-09-06-from-klerik.md]

## Current work context
Chris noted that 32 GB RAM should leave enough room to do a speed/audition step while another model tests in the background, without getting in the way of other work.

> "You have 32 gigabytes, um, and the other one is testing in the background. You should have enough space to at least do a step and not get in the way." ^[raw/inbox/2026-09-07.md]

## Audition target
The next explicit baseline is the 131K configuration re-audition for speed, not a new architecture. Chris expected sufficient RAM to complete at least one step of that audition.

> "Remember, the 131K configuration because we're going to audition that again, grab that uncensored one again, and try to see what's the best speed that you can get with that one at 131K because that one's smaller." ^[raw/inbox/2026-09-07.md]

> "You have 32 gigabytes, um, and the other one is testing in the background. You should have enough space to at least do a step and not get in the way." ^[raw/inbox/2026-09-07.md]

## Speed threshold
The 131K speed test did not meet Chris's expectation. He discarded the run as too slow and redirected effort back to 27B optimization instead of repeating the same audition.

> "All right, never mind. We didn't go fast enough. My neighbor left After you generate those just put them in a folder We'll do something with those later, but uh, yeah, then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

^[raw/inbox/2026-09-07.md]

## Related
- [[topics/back-where/wiki/concepts/model-prefill-fallback|Prefill timeout triggering model fallback]]
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[topics/back-where/wiki/entities/hermes-model-download-in-progress|Hermes model download in progress]]
