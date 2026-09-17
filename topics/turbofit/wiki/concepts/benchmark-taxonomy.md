---
title: Benchmark Taxonomy
created: 2026-09-16
updated: 2026-09-16
type: concept
tags: [benchmarks, model-comparison, taxonomy]
sources: []
---

# Benchmark Taxonomy

> Common benchmarks tracked across all models. Each model page records scores where available.

## Reasoning & Knowledge

| Benchmark | What it measures | Why it matters |
|-----------|------------------|----------------|
| MMLU | Multitask language understanding (57 subjects) | General knowledge breadth |
| ARC-Challenge | Grade-school science questions | Logical reasoning |
| HellaSwag | Sentence completion | Common-sense reasoning |
| WinoGrande | Pronoun resolution | Contextual understanding |
| TruthfulQA | Truthfulness | Hallucination resistance |

## Coding

| Benchmark | What it measures | Why it matters |
|-----------|------------------|----------------|
| HumanEval | Python code generation | Raw coding ability |
| MBPP | Basic Python problems | Everyday coding |
| LiveCodeBench | Competitive programming | Complex problem solving |

## Math

| Benchmark | What it measures | Why it matters |
|-----------|------------------|----------------|
| GSM8K | Grade-school math word problems | Mathematical reasoning |
| MATH | Competition mathematics | Advanced math |

## Long Context

| Benchmark | What it measures | Why it matters |
|-----------|------------------|----------------|
| RULER | Long-context retrieval | Context window quality |
| Needle-in-Haystack | Needle retrieval at length | Factual recall at depth |

## Inference Performance

| Metric | What it measures | Why it matters |
|--------|------------------|----------------|
| tok/s @ 4K ctx | tokens/sec at 4K context | Short-context tok/s |
| tok/s @ 32K ctx | tokens/sec at 32K context | Mid-context sustained |
| tok/s @ 128K ctx | tokens/sec at 128K context | Long-context sustained |
| TTFT | Time to first token | Initial latency |
| VRAM usage | GPU memory at load | Hardware feasibility |
| RAM usage | System memory at load | Unified memory feasibility |

## Vision (for multimodal models)

| Benchmark | What it measures |
|-----------|------------------|
| MMMU | Multimodal understanding |
| TextVQA | Text reading in images |
| OCRBench | Document OCR |

## Retrieval (for embedding models)

| Benchmark | What it measures |
|-----------|------------------|
| MTEB | General retrieval |
| BEIR | Zero-shot retrieval |

## Usage

When adding a model page, fill in any of the above benchmarks where data is available from:
- HuggingFace model card (they often list benchmarks)
- Independent benchmarks (llama.cpp community, etc.)
- Our own testing results

Models without data simply show "—" — this is expected and motivates future research.
