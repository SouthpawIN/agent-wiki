---
title: MTP speculative decoding
created: 2026-09-06
updated: 2026-09-06
type: concept
tags: [speculative-decoding, inference, mac, mtplx]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# MTP speculative decoding

The technique behind the MTPLX setup used for the Qwen 27B model.^[raw/inbox/2026-09-06.md]

## Observed configuration

- Hermes started MTPLX with MTP depth 3.

## Role in this topic

This is the reason the tested model path can claim speed gains on Apple Silicon. Chris's later question about 131K/262K behavior should be understood against how MTP depth trades memory for throughput at long context.

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[concepts/mtplx|MTPLX]]
