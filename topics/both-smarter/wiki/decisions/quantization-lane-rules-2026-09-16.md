---
title: Quantization Lane Rules for Unified Memory (2026-09-16)
created: 2026-09-16
updated: 2026-09-16
type: decision
tags: [decision, preference, tool]
sources: [raw/inbox/2026-09-16.md]
confidence: medium
---

On 2026-09-16 Chris laid out quantization guidance for the per-device model lanes — the unified-memory/CPU lane and the GPU (VRAM) lane. The CPU guidance is stated firmly; the GPU guidance is his reasoning with the math explicitly unverified. ^[raw/inbox/2026-09-16.md]

**Unified-memory / CPU lane — use IQ3S all the way up.** Chris said the 24GB, 32GB, and 48GB tiers "doesn't make recommendation" because IQ3S is near-lossless and actually better than Q4, so it should be IQ3S "really all the way up through 48 gigabytes and then the full precision 16." He then corrected himself to keep it IQ3S "all the way because it's task bossless [near-lossless] and it will be ran on less power and you just do higher quant sling the higher it goes." ^[raw/inbox/2026-09-16.md]

> "the IQ 3S is near lossless and actually better than the Q4 So it should actually be IQ 3S Really all the way up through 48 gigabytes and then the full precision 16 Well, no, you want just keep it IQ 3S all the way because it's task bossless and it will be ran on less power and you just do higher contact sling the higher it goes." ^[raw/inbox/2026-09-16.md]

**GPU (VRAM) lane — 8/16GB can offload an MoE to system RAM.** For the 8GB and 16GB GPU tiers, Chris said to assume "a little bit of system RAM because for the GPU tier, that memory is going to be ... particularly V-RAM," so those machines can offload an MoE to system RAM. He speculated "you may be able to fit a good Q3 of Teal coder on there" but flagged it as unverified: "check my math on that. We may still have to have maple the lowest one." ^[raw/inbox/2026-09-16.md]

**Status:** CPU-lane IQ3S recommendation is firm; GPU-lane Q3-of-Cyber-Tiel-Coder fit is explicitly unverified math. ^[raw/inbox/2026-09-16.md]

## Related
- [[device-specific-model-lanes|Device-Specific Model Lanes]]
- [[cyber-tiel-coder-confirmed-2026-09-15|Cyber-Tiel-Coder Confirmed Running through Hermes (2026-09-15)]]
- [[model-candidates|Model Candidates on Hugging Face]]
