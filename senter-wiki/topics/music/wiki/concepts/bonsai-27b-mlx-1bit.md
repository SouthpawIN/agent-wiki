---
title: Bonsai 27B MLX 1-bit vs ternary 2-bit
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [infra, music, pain, comparison]
sources: [raw/inbox/2026-09-07.md]
confidence: low
---
# Bonsai 27B MLX 1-bit vs ternary 2-bit

Hermes distinguished two Bonsai MLX quantizations on 2026-09-07: ternary 2-bit and pure 1-bit. The distinction matters for memory and speed if these models are later routed to local music generation. ^[raw/inbox/2026-09-07.md]

## Why it matters
For the 32 GB Mac, every bitwidth change can shift whether a 27B candidate can run concurrently with MTPLX. If the 1-bit build is materially smaller, it may enter the local music priority discussion alongside ACE-Step and Step-Audio-2-mini. If both Bonsai variants remain too large, they remain text/infra candidates.

## Evidence
- "Good - I downloaded Ternary-Bonsai-27B-mlx-2bit (7.9GB) but I need to download the 1-bit Bonsai-27B-mlx-1bit for the pure binary version." ^[raw/inbox/2026-09-07.md]
- "Bonsai-27B-mlx-1bit: should be similar size but 1-bit binary." ^[raw/inbox/2026-09-07.md]

## Related
- [[topics/music/wiki/entities/ternary-bonsai-27b|Ternary-Bonsai-27B-mlx-2bit]]
- [[topics/music/wiki/entities/bonsai-27b|Bonsai-27B-mlx-1bit]]
- [[topics/music/wiki/concepts/local-music-memory-budget|Local music memory budget]]
