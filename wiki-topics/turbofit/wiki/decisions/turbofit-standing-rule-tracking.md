---
title: Track TurboFit rules as they are stated
created: 2026-10-28
updated: 2026-10-28
type: decision
tags: [turbofit, provider, provenance, consolidation]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# Track TurboFit rules as they are stated

> Chris states fit/lane rules mid-build and expects each one implemented immediately, not batched. This page is the standing instruction plus the lane rules it produced.

**Absorbed 2026-10-28** from pages that had been filed in other topics (one spot for TurboFit knowledge). Source pages are now redirect stubs.

## Sources absorbed

- `wiki-topics/both-smarter/wiki/decisions/turbo-fit-rule-tracking-2026-09-16.md` — TurboFit Rule Tracking (2026-09-16) (created 2026-09-16)
- `wiki-topics/both-smarter/wiki/skills/turbo-fit-lane-rules.md` — TurboFit Lane & Quantization Rules (created 2026-09-16)

---

On 2026-09-16 Chris said to start **keeping a running track of the rules he gives for TurboFit** (transcribed "turbo fitness") as he goes, and to implement them as he states them rather than collecting them all at the end. ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

> "Okay, so I want you to start keeping track of rules that I tell you for This turbo fitness as we go because I'm about to give you a couple and I want you to implement the rules as we go." ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

**First rule given (CPU / unified-memory lane).** Chris noted that CPU and unified-memory hardware "don't run dense models super fast," so the 27B models "are really not optimal for those." In those places he wants the teal coder [Cyber Tiel Coder] run instead. ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

> "For CPU and unified memory. They don't run dense models super fast So the 27b is really not optimal for those So in those plays we should be running the teal coder." ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

**Standing instruction:** track and implement TurboFit rules incrementally as Chris states them, don't batch at the end. ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

## Related
- Device-Specific Model Lanes
- Cyber-Tiel-Coder Confirmed Running through Hermes (2026-09-15)
- Benchmark Maintenance Plan

---

## TurboFit Lane & Quantization Rules

Apply when choosing a quantization and model for a given device compute type on Chris's hardware, and when tracking TurboFit ("turbo fitness") lane rules as he states them.

## When to use
Chris is picking a quantization/model for a device lane, or giving a new TurboFit rule he wants tracked and implemented.

## Rules
1. Unified-memory / CPU lane — use **IQ3S** for the model all the way up through 48GB (and full-precision 16). IQ3S is near-lossless and, per Chris, better than Q4; it runs on less power and "higher quant sling[s] the higher it goes." ^[provenance: both-smarter/raw/inbox/2026-09-16.md]
2. CPU / unified-memory lanes should run **MoE models (teal coder / Cyber Tiel Coder)**, not dense 27B models — dense models "don't run ... super fast" on this hardware and 27B dense "is really not optimal." ^[provenance: both-smarter/raw/inbox/2026-09-16.md]
3. GPU (VRAM) lane — 8GB/16GB GPUs can assume some system RAM is available (that tier's memory is specifically VRAM), so they may offload an MoE to system RAM; a "good Q3 of Teal coder" may fit there. ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

## Track TurboFit rules as they come
- Keep a running log of the rules Chris gives for TurboFit and **implement them as he states them** — don't batch at the end. ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

## Evidence
- "the IQ 3S is near lossless and actually better than the Q4 So it should actually be IQ 3S Really all the way up through 48 gigabytes ... just keep it IQ 3S all the way because it's task bossless and it will be ran on less power and you just do higher contact sling the higher it goes." ^[provenance: both-smarter/raw/inbox/2026-09-16.md]
- "For CPU and unified memory. They don't run dense models super fast So the 27b is really not optimal for those So in those plays we should be running the teal coder." ^[provenance: both-smarter/raw/inbox/2026-09-16.md]
- "for the 8 and 16 like gigabytes, we can assume that they're that they can offload an MOE to a system round" ^[provenance: both-smarter/raw/inbox/2026-09-16.md]

## Pitfalls
- The GPU-lane Q3-of-Cyber-Tiel-Coder fit is **unverified math** ("check my math on that") — flag it, don't assert it. ^[provenance: both-smarter/raw/inbox/2026-09-16.md]
- "teal coder" = Cyber Tiel Coder (Ornith-1.5-35B-A3B variant); "turbo fitness" = TurboFit. ^[provenance: both-smarter/raw/inbox/2026-09-16.md]
