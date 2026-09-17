---
title: TurboFit Lane & Quantization Rules
created: 2026-09-16
updated: 2026-09-16
type: skill
tags: [decision, preference, tool]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

# TurboFit Lane & Quantization Rules

Apply when choosing a quantization and model for a given device compute type on Chris's hardware, and when tracking TurboFit ("turbo fitness") lane rules as he states them.

## When to use
Chris is picking a quantization/model for a device lane, or giving a new TurboFit rule he wants tracked and implemented.

## Rules
1. Unified-memory / CPU lane — use **IQ3S** for the model all the way up through 48GB (and full-precision 16). IQ3S is near-lossless and, per Chris, better than Q4; it runs on less power and "higher quant sling[s] the higher it goes." ^[raw/inbox/2026-09-16.md]
2. CPU / unified-memory lanes should run **MoE models (teal coder / Cyber Tiel Coder)**, not dense 27B models — dense models "don't run ... super fast" on this hardware and 27B dense "is really not optimal." ^[raw/inbox/2026-09-16.md]
3. GPU (VRAM) lane — 8GB/16GB GPUs can assume some system RAM is available (that tier's memory is specifically VRAM), so they may offload an MoE to system RAM; a "good Q3 of Teal coder" may fit there. ^[raw/inbox/2026-09-16.md]

## Track TurboFit rules as they come
- Keep a running log of the rules Chris gives for TurboFit and **implement them as he states them** — don't batch at the end. ^[raw/inbox/2026-09-16.md]

## Evidence
- "the IQ 3S is near lossless and actually better than the Q4 So it should actually be IQ 3S Really all the way up through 48 gigabytes ... just keep it IQ 3S all the way because it's task bossless and it will be ran on less power and you just do higher contact sling the higher it goes." ^[raw/inbox/2026-09-16.md]
- "For CPU and unified memory. They don't run dense models super fast So the 27b is really not optimal for those So in those plays we should be running the teal coder." ^[raw/inbox/2026-09-16.md]
- "for the 8 and 16 like gigabytes, we can assume that they're that they can offload an MOE to a system round" ^[raw/inbox/2026-09-16.md]

## Pitfalls
- The GPU-lane Q3-of-Cyber-Tiel-Coder fit is **unverified math** ("check my math on that") — flag it, don't assert it. ^[raw/inbox/2026-09-16.md]
- "teal coder" = Cyber Tiel Coder (Ornith-1.5-35B-A3B variant); "turbo fitness" = TurboFit. ^[raw/inbox/2026-09-16.md]
