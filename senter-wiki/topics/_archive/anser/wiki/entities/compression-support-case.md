---
title: "Compression support case — 2026-09-06"
created: 2026-09-06
updated: 2026-09-07
type: entity
tags: [tool, infra, pain]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07-from-senter.md]
confidence: low
contested: false
---

# Compression support case — 2026-09-06

A Hermes support case filed on 2026-09-06, concerning local-model compression speed on large contexts. ^[raw/inbox/2026-09-06.md]

## What happened
- Connection accepted but no response in 120s because the local model was too slow to compress a 387k context. ^[raw/inbox/2026-09-06.md]
- Compression was rerouted from the local model to Nous. ^[raw/inbox/2026-09-06.md]
- Subsequent validation used Maple MLX with the deepgrove fork: 5000 tokens in 9s, then 130K tokens in 103s with no OOM. ^[raw/inbox/2026-09-06.md]
- The follow-up goal at filing time was final end-to-end Hermes verification after confirming both servers were up and config was correct. ^[raw/inbox/2026-09-06.md]

## Notes
- Filed under `anser` but its subject is Hermes infrastructure/compression routing, not Discord moderation. ^[raw/inbox/2026-09-06.md]
- The 2026-09-07 raw filing repeats the same compression evidence and adds repeated timeout messages; no new moderation facts were introduced. ^[raw/inbox/2026-09-07-from-senter.md]

## Links
- [[topics/anser/wiki/entities/anser|anser]]
- [[topics/anser/wiki/concepts/local-model-compression|Local-model context compression → route to Nous]]
