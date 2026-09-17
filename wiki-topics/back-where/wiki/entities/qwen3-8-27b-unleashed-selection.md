---
title: "Qwen3.8 27B unleashed model selection"
created: 2026-09-07
updated: 2026-09-07
type: entity
tags:
  - tool
  - infra
  - preference
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-15.md
confidence: high
---

# Qwen3.8 27B unleashed model selection

## Selected model
Chris identified the Qwen3.8 27B "unleashed" variant as the preferred model, specifically seeking Q3 quantization for optimal performance. He emphasized researching before implementing and noted its uncensored nature and smaller size compared to alternatives, with potential deep flash support.

> "Remember, the 131K configuration because we're going to audition that again, grab that uncensored one again, and try to see what's the best speed that you can get with that one at 131K because that one's smaller. It is on Lama CPP, I'm not sure if there's an MLX for it, but I really like that particular ones that I gave you. Unleashed because if you look at the unleashed page and I want you to look at the hugging face page I really want you to get in the habit of First researching and then implementing so you should look at the quen 3.8 27 be unleashed page the q3k exiles the most accurate one and it's uncensored and it's smaller And I think they have a deep flash for it." ^[raw/inbox/2026-09-07.md]

## Quantization detail
Within the Q3 family, Chris specifically cited Q3K exile as the most accurate quantization for the unleashed variant.

> "...the q3k exiles the most accurate one and it's uncensored and it's smaller..." ^[raw/inbox/2026-09-07.md]

## 2026-09-16 supersede to GSQ RCO IQ3S
On 2026-09-16 Chris moved his quantization preference away from Q3K exile to the **GSQ RCO IQ3S**, conditioned on the GSQ version being genuinely near task-lossless versus FP16 while drawing less power. See the contested note in [[wiki-topics/back-where/wiki/decisions/gsq-rco-iq3s-selection-preference|GSQ RCO IQ3S selection preference]]. The Q3K exile selection is now superseded by a conditional, unverified preference rather than confirmed.

> "let's do the GSQ RCO IQ3S because if it's near task lossless, or if it is task lossless, if it takes less kilowatts an hour to run, and if we can fit a higher context length and run it faster, and possibly have more room for more options like D Flash 2..." ^[raw/inbox/2026-09-16.md]

## Research requirements
Before implementation, Chris wants a habit of researching the unleashed page and HuggingFace page before proceeding with model implementation. The 131K configuration should be reused as the baseline speed test, not skipped.

> "I really want you to get in the habit of First researching and then implementing so you should look at the quen 3.8 27 be unleashed page the q3k exiles the most accurate one and it's uncensored and it's smaller And I think they have a deep flash for it." ^[raw/inbox/2026-09-07.md]

## Speed-test outcome
The 131K audition did not reach acceptable speed. Chris asked for generated outputs to be saved, then shifted priority back to optimizing the 27B models rather than continuing the current audition.

> "All right, never mind. We didn't go fast enough. My neighbor left After you generate those just put them in a folder We'll do something with those later, but uh, yeah, then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

## Disk state
Chris explicitly asked for generated outputs from the rejected 131K audition to be retained in a folder for later use, instead of discarding them. This makes the on-disk artifacts part of the expected recovery state before the next optimization attempt.

> "After you generate those just put them in a folder We'll do something with those later" ^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[wiki-topics/back-where/wiki/entities/m1-mac-performance-expectation|M1 Mac performance expectation]]
- [[wiki-topics/back-where/wiki/entities/recovery-background-process|Recovery background process mid-run]]
- [[wiki-topics/back-where/wiki/entities/q3k-xl-double-gpu-gaming-choice|Q3K XL / Unleashed chosen as game-adjacent model]]