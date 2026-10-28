---
title: MPLX Integration
created: 2026-09-06
updated: 2026-09-06
type: query
tags: [question, plan, tool]
sources: [raw/inbox/2026-09-06.md]
confidence: low
---

# MPLX Integration

## Question

Can MPLX be added as a fast local TurboFit provider alongside Unleashed 27B without evicting the main model, and what is the memory ceiling under MTP?

## Evidence gathered

- 12.4 tok/s measured under MTP, faster than Unleashed Q3_K_XL.
- Download completed at 21:39; 26 GB used, 5.7 GB free alongside Unleashed.
- Testing halted before serving, so integration path, provider config, and context limit are unknown ^[raw/inbox/2026-09-06.md].

## Why this matters

If MPLX can share the box with Unleashed, it may become a faster aux or alternate main path. If not, it may replace Unleashed or run as an offline benchmark lane.

## Related

- [[mplx|MPLX]]
- [[turbofit|TurboFit]]
- [[main-model-selection|Main Model Selection]]
