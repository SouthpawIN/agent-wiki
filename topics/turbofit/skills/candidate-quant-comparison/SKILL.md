---
name: candidate-quant-comparison
description: Use when evaluating new local TurboFit candidates. Compare GGUF vs MLX artifacts and prefer Q3 when page notes say near base quality.
version: 0.1.0
distilled: 2026-09-07 09:43
topic: turbofit
---
# candidate-quant-comparison
## Steps
1. For each new candidate, query the HuggingFace repo page for quant notes and quality claims.
2. If page notes say Q3 is near base quality, request the Q3 GGUF artifact first.
3. Check whether an MLX 4-bit package exists for the same model.
4. If both GGUF Q3 and MLX 4-bit exist, record both paths and the page recommendation in the candidate's wiki page.
5. If no quant recommendation exists, compare Q3_K_XL vs Q4_K_XL and note page evidence before choosing.

## Pitfalls
- Do not download without verifying file size first.
- Do not benchmark at 131K until the 32GB fit is confirmed from artifact size + KV cache estimate.
- Do not mix repo lookup failures with model capability claims; verify both independently.

## Evidence
> They also have a lot to say about their quants on their pages too, check GGUF vs MLX, I like the Q3 quant that they said is near base model quality
> Download Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf (12.24 GB) to ~/Models/storage/dirk-gguf/.
> Download Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf (20.82 GB) to ~/Models/storage/nail/.
