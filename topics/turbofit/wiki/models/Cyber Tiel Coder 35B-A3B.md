---
title: Cyber Tiel Coder 35B-A3B
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, code, moe, uncensored, local]
sources:
  - https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF
  - https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP
  - https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-MLX-oQ6e
  - https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B
  - https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-FP8
---

# Cyber-Tiel-Coder 35B-A3B

> Uncensored 35B-A3B MoE code specialist based on Huihui-Ornith-1.5-abliterated. Pushes the frontier of quantized local coders — beats Opus 4.6 medium on SWE-bench-Live at 4-bit while running on a single 24 GB GPU or Apple Silicon.

## Specifications

- **HuggingFace:** [peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF) (non-MTP) · [MTP variant](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP) · [MLX](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-MLX-oQ6e)
- **Type:** Code LLM
- **Architecture:** Mixture-of-Experts (MoE), qwen3_5_moe_text
- **Base model:** Huihui-Ornith-1.5-35B-A3B-abliterated (derived from Ornith-1.5-35B-A3B)
- **Total parameters:** ~35B (36B)
- **Active parameters per token:** ~3B
- **Layers:** 40 transformer blocks (10 attention + 30 SSM with fixed-size state)
- **Hidden size:** 2,048
- **Attention heads:** 16 query / 2 key-value (grouped-query attention)
- **Experts:** 256 per layer, 8 routed per token
- **MoE intermediate size:** 512
- **Context window:** 262,144 tokens (trained ceiling); extendable to 512K–1M via YaRN extrapolation (quality not guaranteed)
- **Chat template:** Sharp (`qwen3.8-froggeric-v22.5.0`)
- **License:** MIT
- **ROPE:** `freq_base=10000000`, no YaRN config baked in

## System Availability

| System | Available | Path |
|--------|-----------|------|
| Omarchy | Yes | `/home/sovthpaw/Models/storage/gguf/Cyber-Tiel-Coder-35B-A3B/` |
| MacBook | Yes | `~/Models/storage/gguf/Cyber-Tiel-Coder-35B-A3B/` |

## Quantization Tiers

### GGUF Non-MTP Ladder

| File | Size | Fits | Notes |
|------|------|------|-------|
| `UD-Q2_K_XL` | 12.3 GB | 16 GB | LAST RESORT — 2-bit struggles with agentic coding |
| `UD-IQ3_XXS` | 13.2 GB | 16 GB | Best 16 GB pick |
| `UD-Q3_K_XL` | 16.8 GB | 24 GB | 3-bit, prefer IQ4_XS below |
| `UD-IQ4_XS` | 17.7 GB | 24 GB | 4-bit with most context headroom |
| `UD-Q4_K_S` | 20.9 GB | 24 GB | Tight 4-bit |
| `UD-Q4_K_M` | 22.1 GB | 24 GB | Benchmarked tier (SWE-bench-Live + Cybench) |
| **`UD-Q4_K_XL`** | **22.4 GB** | **24–32 GB** | **RECOMMENDED — best 4-bit tier** |
| `UD-Q5_K_XL` | 26.6 GB | 32 GB | Best 32 GB pick |
| `UD-Q6_K_XL` | 31.8 GB | 48 GB | Near-lossless |

### GGUF MTP Ladder (adds ~0.4 GB grafted MTP draft head)

| File | Size | Notes |
|------|------|-------|
| `MTP-UD-Q4_K_XL` | 22.7 GB | Start here if using speculative decoding |
| `MTP-UD-Q5_K_XL` | 27.0 GB | 32 GB with MTP |
| `MTP-UD-Q6_K_XL` | 32.2 GB | 48 GB with MTP |
| `MTP-UD-Q8_K_XL` | 38.8 GB | Reference |

### MLX for Apple Silicon

| File | Size | Notes |
|------|------|-------|
| `oQ4e` | ~21 GB | 4-bit dynamic mixed precision, fits 24 GB Mac |
| `oQ4e-MTP` | ~23 GB | With speculative decoding head |
| `oQ6e` | ~31 GB | 6-bit near-lossless |
| `oQ6e-MTP` | ~33 GB | 6-bit with MTP |

### Optimal Quantization by Hardware Tier

| Hardware | Optimal Quant | VRAM/RAM | Context Room | Notes |
|----------|--------------|----------|--------------|-------|
| **GPU 24 GB** (RTX 3090/4090) | `UD-Q4_K_XL` (GGUF) | 22.4 GB VRAM | ~2 GB for 262K KV q8_0 | Full model on GPU, no offload needed |
| **GPU 32 GB** | `UD-Q5_K_XL` (GGUF) | 26.6 GB VRAM | ~5 GB for 262K | More precision headroom |
| **GPU 48 GB** | `UD-Q6_K_XL` (GGUF) | 31.8 GB VRAM | ~16 GB free | Near-lossless quality |
| **GPU 16 GB** | `UD-IQ3_XXS` (GGUF) + `--n-cpu-moe` | 13.2 GB + offload | 16–32 layers on GPU | CPU offload for expert layers |
| **GPU 8 GB** | `UD-Q2_K_XL` (GGUF) + `--n-cpu-moe` | 12.3 GB + offload | Most layers on CPU | Last resort, quality loss |
| **CPU / Partial offload** | `UD-Q4_K_XL` + `--n-cpu-moe` | System RAM | ~22 GB RAM for model + KV | Use `--n-cpu-moe N` to control GPU layers |
| **Unified 24 GB** (Mac) | MLX `oQ4e` or GGUF `UD-Q4_K_XL` | ~21–22 GB unified | ~2 GB for 262K KV | Use `-ngl 99` on Apple |
| **Unified 32+ GB** (Mac) | MLX `oQ6e` or GGUF `UD-Q5_K_XL` | ~26–31 GB unified | ~5 GB for 262K KV | Near-lossless on Apple |
| **Unified 64+ GB** (Mac) | MLX `oQ6e` or GGUF `UD-Q6_K_XL` | ~32 GB unified | Plenty for 1M+ context | Max quality |

## Context Configurations

The SSM-heavy architecture makes KV cache very cheap: ~20–22 KB/token at f16, ~10–11 KB/token at q8_0.

| Context | KV (q8_0) | KV (f16) | Config | Quality |
|---------|-----------|----------|--------|---------|
| **64K** | ~0.7 GB | ~1.4 GB | `-c 65536 -ctk q8_0 -ctv q8_0 -fa` | Excellent (within training) |
| **131K** | ~1.5 GB | ~3.0 GB | `-c 131072 -ctk q8_0 -ctv q8_0 -fa` | Excellent (within training) |
| **262K** | ~3.1 GB | ~5.4 GB | `-c 262144 -ctk q8_0 -ctv q8_0 -fa` | **RECOMMENDED — trained ceiling** |
| **512K** | ~5.4 GB | ~10.7 GB | `--rope-scaling yarn --rope-scale 2 --yarn-orig-ctx 262144 -c 524288` | Good (extrapolation) |
| **1M** | ~10.7 GB | ~21.5 GB | `--rope-scaling yarn --rope-scale 4 --yarn-orig-ctx 262144 -c 1048576` | Unverified (use subagent orchestration) |

### Runtime Commands

**llama.cpp (262K context, 24 GB GPU):**
```bash
llama-server \
  -m Cyber-Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf \
  -c 262144 -ctk q8_0 -ctv q8_0 -fa \
  -ngl 99 --n-cpu-moe 2 \
  --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0 \
  --repeat-penalty 1.0
```

**llama.cpp (Apple Silicon, no CPU offload):**
```bash
llama-server \
  -m Cyber-Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf \
  -c 262144 -ctk q8_0 -ctv q8_0 -fa \
  -ngl 99
```

**llama.cpp (1M context with YaRN):**
```bash
llama-server \
  -m Cyber-Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf \
  -c 1048576 -ctk q8_0 -ctv q8_0 -fa \
  --rope-scaling yarn --rope-scale 4 --yarn-orig-ctx 262144 \
  -ngl 99 --n-cpu-moe 2
```

**Sampling presets:**
- Agentic coding: `temp 0.6, top_p 0.95, top_k 20, min_p 0`
- Cyber/CTF work: `temp 0.6, top_p 0.95, top_k 40, min_p 0.05` (more exploratory)

**Key notes:**
- `-fa` (flash attention) + `-ctk q8_0 -ctv q8_0` is critical — dropping it doubles KV cost and costs ~1.5 expert layers on GPU
- Do NOT use `--repeat-penalty >1.0` for coding/tool use (harms quality)
- On Apple unified memory: skip `--n-cpu-moe`, use `-ngl 99`
- For long-running agentic work: prefer subagent orchestration that compacts context at 64–128K over pushing to 500K+

## Inference Performance

| Runtime | Platform | tok/s | Notes |
|---------|----------|-------|-------|
| llama.cpp CUDA | Omarchy RTX 3090×2 | ~25 peak | Community benchmark (1 GPU) |
| llama.cpp CUDA | RTX 5060 | ~119 peak | MTP-UD-IQ3_XXS with speculative decoding |
| llama.cpp Metal | MacBook M1 Pro | — | |
| MLX | MacBook M1 Pro | — | |

## Benchmarks

> SWE-bench-Live and MMLU-Pro measured at `UD-Q4_K_M` (near-identical to `UD-Q4_K_XL`). CyberTiel lands on exactly TielCoder's MMLU-Pro score — the abliteration does not sacrifice world-knowledge scores. Benchmarks run at non-zero temperature; small differences should be treated as noise.

### Coding & Agentic

| Benchmark | Score | Comparison |
|-----------|-------|------------|
| **SWE-bench-Live** | **13.7 / 25** (3-seed mean, runs: 15/13/13) | Above Opus 4.6 medium (12); ~70% more problems than Ornith-1.5 and Qwen3.6 |
| Cybench CTF | 15/43 flags (35%); 10/31 official | Unguided, no hints/judge, 15 iterations, 262K context |
| HarmBench | 0/84 refusals | Zero refusals across all 7 categories |

### Reasoning & Knowledge

| Benchmark | Score | Notes |
|-----------|-------|-------|
| **MMLU-Pro** | **73.7** | At 4-bit; inherits from Ornith-1.5 (78.0 at FP8) with Sharp template trade-off. TielCoder counterpart matches exactly. |
| MMLU | ~73–74 (estimated) | MMLU-Pro ≈ MMLU for this model class; not explicitly benchmarked separately |

### Benchmarks Not Tested

| Benchmark | Status |
|-----------|--------|
| DeepSWE | Not run — benchmark targets frontier cloud agents; this is a local community model |
| TerminalBench v4.0 | Not run — leaderboard populated by frontier models (GPT-6 Astra ~58%) |
| GPQA Diamond | Not explicitly tested — model sacrifices world knowledge for coding; expected low for graduate science |
| ARC-C, HellaSwag, WinoGrande, TruthfulQA | Not benchmarked |
| HumanEval, MBPP, LiveCodeBench | Not benchmarked (SWE-bench-Live is the primary coding metric) |
| GSM8K, MATH | Not benchmarked |
| RULER, Needle-in-Haystack | Not benchmarked (but 262K context confirmed working) |

## Research Notes

### Model Profile
CyberTiel is the uncensored variant of TielCoder, both by peculiar-ragdoll. The base is Huihui-Ornith-1.5-35B-A3B-abliterated (abliterated Ornith-1.5), re-quantized with a custom cyber-weighted imatrix (curated corpus of cybersecurity + agentic software engineering work) using Unsloth Dynamic quantization. The Sharp chat template is embedded in the checkpoint.

### Key Findings from Maintainer
- CyberTiel solves ~70% more real-world coding problems than Ornith-1.5 and Qwen3.6 at 4-bit — a ~7x larger gap than the Qwen3.5→3.6 generational step
- Beats Opus 4.6 medium on SWE-bench-Live (13.7 vs 12) while being significantly faster than Qwen3.8-27B dense
- First uncensored frontier coder in the 35B-A3B class
- 3-4x faster agentic coding solves than 3.8–27B dense models
- Agentic solves at ~27% of Qwen3.8-27B medium time

### Architecture Advantages
- Only 10 of 40 blocks carry attention (rest are SSM with fixed state) → extremely cheap KV cache
- At 262K context: only ~3.1 GB KV at q8_0 / ~5.4 GB at f16
- MoE design means 35B quality with ~3B active compute per token
- MTP (multi-token-prediction) head grafted from Ornith-1.5's trained `nextn` block at layer 40

### Use Cases
- **Primary:** Agentic coding, real-world codebase fixes, SWE-bench-Live-class work
- **Secondary:** Cybersecurity research, CTF challenges, offensive security (zero refusals)
- **Not recommended:** General knowledge, exams, trivia, non-English/Chinese languages

### MTP Notes
- MTP head adds ~0.4 GB per quant
- On llama.cpp: `--spec-type draft-mtp` enables speculative decoding
- On MLX: native MTP support (oMLX "Lightning MTP")
- Speedup is hardware-dependent: helps on memory-bound setups, can be slightly slower on Apple Silicon decode that isn't memory-bound
- If not using speculative decoding, take the non-MTP ladder (saves ~0.4 GB)

### Tiel Coder

Tiel-Coder is a queued local GGUF candidate. The primary MLX download in `~/Models/storage/tiel-coder/` remained incomplete (~15 GB of ~19 GB), and a GGUF test path at `~/Models/storage/tiel-coder-gguf/Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf` was launched at 131K but not benchmarked before the session ended.

#### Status

- MLX download incomplete (15 GB of 19 GB)
- GGUF Q4_K_XL version tested and working at 65K
- Benchmarked: 65K context, 23.1 tok/s short, 4.2 tok/s at 5K
- 131K benchmark deferred due to OOM expectation (22 GB + 8 GB KV)

#### Benchmark Results

|| Model | Type | Context | Short | 5K | Status |
| --- | --- | --- | --- | --- | --- | --- |
|| **Tiel-Coder Q4_K_XL** | MoE 35B | 65K | **23.1 tok/s** | 4.2 tok/s | Viable |

#### MoE Advantage

Tiel-Coder is MoE 35B with 3B active params, making it memory-efficient and fast. Similar to Nail and Ornith.

#### Download Status

The tiel-coder background process completed successfully:
```
all downloads complete
```
Files available at:
- `~/Models/storage/tiel-coder/` (MLX, incomplete)
- `~/Models/storage/tiel-coder-gguf/` (GGUF Q4_K_XL, 22.16 GB)

#### Related

- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Speed Test Results]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/entities/nail-qwen36-35b.md|Nail Qwen 3.6 35B UD Q4_K_XL]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]


## See Also

- [[concepts/benchmark-taxonomy|Benchmark Taxonomy]]
- [[topics/turbofit/wiki/index|Wiki Index]]
- [Ornith-1.5-35B-A3B (upstream base)](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [Tiel-Coder-35B-A3B (censored sibling)](https://huggingface.co/peculiar-ragdoll/Tiel-Coder-35B-A3B-GGUF)

### From entity: tiel-coder

Tiel-Coder is a queued local GGUF candidate. The primary MLX download in `~/Models/storage/tiel-coder/` remained incomplete (~15 GB of ~19 GB), and a GGUF test path at `~/Models/storage/tiel-coder-gguf/Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf` was launched at 131K but not benchmarked before the session ended.

## Status

- MLX download incomplete (15 GB of 19 GB)
- GGUF Q4_K_XL version tested and working at 65K
- Benchmarked: 65K context, 23.1 tok/s short, 4.2 tok/s at 5K
- 131K benchmark deferred due to OOM expectation (22 GB + 8 GB KV)

## Benchmark Results

|| Model | Type | Context | Short | 5K | Status |
||-------|------|---------|-------|-----|--------|
|| **Tiel-Coder Q4_K_XL** | MoE 35B | 65K | **23.1 tok/s** | 4.2 tok/s | Viable |

## MoE Advantage

Tiel-Coder is MoE 35B with 3B active params, making it memory-efficient and fast. Similar to Nail and Ornith.

## Download Status

The tiel-coder background process completed successfully:
```
all downloads complete
```
Files available at:
- `~/Models/storage/tiel-coder/` (MLX, incomplete)
- `~/Models/storage/tiel-coder-gguf/` (GGUF Q4_K_XL, 22.16 GB)

## Related

- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Speed Test Results]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/entities/nail-qwen36-35b.md|Nail Qwen 3.6 35B UD Q4_K_XL]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]
