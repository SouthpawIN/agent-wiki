---
title: Candidate Comparison — Ornith, Nail, Tiel-Coder, Dirk
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags:
  - turbofit
  - comparison
  - candidate
  - benchmark
sources:
  - [raw/inbox/2026-09-07.md](../../raw/inbox/2026-09-07.md)
  - raw/inbox/2026-09-07-from-object-important.md
confidence: high
contested: true
---

# Candidate Comparison — Ornith, Nail, Tiel-Coder, Dirk

## Chris's framing

"They also have a lot to say about their quants on their pages too, check GGUF vs MLX, I like the Q3 quant that they said is near base model quality" ^[raw/inbox/2026-09-07.md]. Chris later asked for head-to-head speed numbers and wanted the comparison tied to real artifacts on this M1 32GB box.

## Measured results

The raw file contains multiple consolidated test tables and a cleanup action that removed Nail, Tiel-Coder, and Dirk test artifacts, but the benchmark evidence remains in session transcripts ^[raw/inbox/2026-09-07.md].

| Model | Type | Context tested | Short | 5K | Notes |
|-------|------|----------------|-------|----|-------|
| Ornith MLX 4-bit | MoE 35B | 131K server | 28.5 tok/s | 5.7 tok/s | Fastest short-context; drops sharply at long context |
| Ornith MLX 4-bit | MoE 35B | 11613 warmup run | ~28-29 tok/s | ~226 tok/s | Light-load MLX server result |
| Nail Q4_K_XL | MoE 35B | 32K | 23.4 tok/s | 4.7 tok/s | Stable MoE throughput; 131K not fit on this box |
| Tiel-Coder Q4_K_XL | MoE 35B | 65K | 23.1 tok/s | 4.2 tok/s | Stable at 65K; 131K deferred by size |
| Dirk Q3_K_XL | Dense 27B | 32K | 6.0 tok/s | 0.8 tok/s | OOM above 32K |

^[raw/inbox/2026-09-07.md]

## Why the comparison is contested

Hermes summaries oscillated between Nail and Ornith as winner depending on metric. Chris ultimately asked for a route change to Ornith, but the Hermes timeout evidence means the comparison is "correct on paper, not yet verified live" for the routed model. The cleanup of downloaded candidates was incomplete: rerouted re-download bursts and cleanup statements imply Nail/Tiel-Coder/Dirk files were removed, but on-disk deletion is not confirmed.

## GGUF vs MLX note

Chris wants GGUF vs MLX compared and prefers Q3 when page notes place it near base quality. Only Ornith MLX and Dirk Q3_K_XL had direct quant matches in this pass. Nail and Tiel-Coder were requested in Q4_K_XL GGUF; their GGUF vs MLX paths remain unclosed.

## Related

- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[tiel-coder|Tiel Coder]]
- [[nail-qwen36-35b|Nail Qwen 3.6 35B UD Q4_K_XL]]
- [[dirk-qwen38-27b|Dirk Qwen 3.8 27B GGUF]]
- [[candidate-quant-preference|Candidate Quant Preference]]
