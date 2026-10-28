---
title: Maple Metal Compatibility
created: 2026-09-06
updated: 2026-09-06
type: query
tags: [question, pain, tool]
sources: [raw/inbox/2026-09-06.md]
confidence: medium
---

# Maple Metal Compatibility

## Question

Can Maple serve stable long-context compression workloads on Apple Silicon Metal without repeated OOM, or is a non-server execution path required?

## Evidence gathered

- The `stamsam/llama.cpp` fork does not have Metal kernels for `tq2_0` quant.
- Q2_0 GGUF under the fork fails tensor reads.
- Generic `mlx_lm` server grows prompt cache until Metal heap dies.
- `deepgrove-ai/mlx-lm-deepgrove` with `--flash-head --trust-remote-code` handled 130K tokens without OOM, but server mode remains cache-pressure sensitive ^[raw/inbox/2026-09-06.md].

## Why this matters

Chris wants Maple as auxiliary on this M1 Mac. If Metal server mode cannot stay stable, TurboFit needs a safer local execution strategy than naive server reuse.

## Related

- [[aux-runtime-options|Aux Runtime Options]]
- [[maple|Maple]]
- [[mplx|MPLX]]
