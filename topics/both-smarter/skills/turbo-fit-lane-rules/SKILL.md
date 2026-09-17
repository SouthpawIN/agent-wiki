---
name: turbo-fit-lane-rules
description: Use when choosing a quantization/model for a device lane on Chris's hardware or tracking his TurboFit rules. Apply IQ3S all the way on unified-memory/CPU lanes, run MoE (teal coder) not dense 27B on CPU lanes, and may offload MoE to system RAM on 8/16GB GPU lanes; log and implement TurboFit rules as he states them.
version: 0.1.0
distilled: 2026-09-16 23:20
topic: both-smarter
---
# turbo-fit-lane-rules
See wiki/skills/turbo-fit-lane-rules.md

## Evidence
> the IQ 3S is near lossless and actually better than the Q4 So it should actually be IQ 3S Really all the way up through 48 gigabytes ...
> For CPU and unified memory. They don't run dense models super fast So the 27b is really not optimal for those So in those plays we should be running the teal coder.
