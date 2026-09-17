---
title: Compression Timeouts
created: 2026-09-06
updated: 2026-09-06
type: concept
tags: [pain, infra, decision]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Compression Timeouts

## What happened

Hermes failed with:

```
Context compression timed out before it could commit while the request was still approximately 270,285 tokens.
```

The provider call was not sent. Compression ran repeatedly until it timed out instead of committing in time ^[raw/inbox/2026-09-06.md].

## Root cause

Local main-model compression at very large context sizes is too slow for Hermes’s timeout. The problem moved from Unleashed 27B to Maple MLX before the Apple-Silicon runtime fixed it locally ^[raw/inbox/2026-09-06.md].

## Mitigations

- 131k context cap for both main and aux.
- Maple MLX aux via `deepgrove-ai/mlx-lm-deepgrove` tested to handle 130K compression workloads in 103 s without OOM.
- If local compression still stalls, route compression to Nous free tier ^[raw/inbox/2026-09-06.md].

## Evidence

- "Context compression timed out before it could commit while the request was still approximately 233,656 tokens" ^[raw/inbox/2026-09-06.md].
- "130K-token compression workload: 103 seconds, no OOM" ^[raw/inbox/2026-09-06.md].

## Related

- [[topics-wiki/turbofit/wiki/decisions/context-sizing.md|Context Sizing]]
- [[topics-wiki/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics-wiki/turbofit/wiki/entities/maple.md|Maple]]
