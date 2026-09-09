---
title: turbofit
updated: 2026-09-02
type: topic
repo: https://github.com/SouthpawIN/turbofit
status: active
tags: [adaptive-runtime, benchmarking, gguf, gpu, hermes-agent]
---

# turbofit

> Adaptive local inference for Hermes — TurboFit Check, evidence-built TurboFit List, repaired discovery/benchmark campaigns, Qwen 3.8 DFlash2, Bonsai DSpark, FreeToken, and Sirvir.

**[Open on GitHub](https://github.com/SouthpawIN/turbofit)** · ACTIVE · last push 2026-08-27

## Facts
- **Language:** Python
- **Stars / forks:** 83 / 16
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-22 · **Last push:** 2026-08-27
- **Open issues:** 0
- **Status:** ACTIVE
- **Topics:** adaptive-runtime, benchmarking, gguf, gpu, hermes-agent, llama-cpp, local-llm

## From the README

# Turbofit

**One model provider. Every machine. The best local configuration the hardware can safely sustain.**

Turbofit is a first-class [Hermes Agent](https://github.com/NousResearch/hermes-agent) provider and adaptive local-inference runtime. It inventories physical compute and **total usable memory**, recommends an evidence-backed ladder, launches a native backend, and exposes one OpenAI-compatible endpoint. The client-facing name stays `auto` while the backing model, context, and auxiliary mode change.

```text
provider: custom:turbofit
model: auto
```

**TurboFit Check** scans this machine — dedicated VRAM, unified/integrated memory, or RAM-only — and applies Auto or a selected compatible lane. The **[TurboFit List](docs/turbofit-list.md)** is the separate evidence-only winner table by hardware class.

> Catalog entries are **candidates** until the physical campaign passes. Compile, download, or estimated fit is not a winner.

## 2.4 lineup

2.4 keeps the Unleashed / Ornith / Nous-free stack and splits the 8 GB problem into two topologies. **Dedicated VRAM is not the same as total RAM.**

| Model | Entries | Role | Status |
|---|---|---|---|
| **Maple Preview 20B-A1B** | `TQ2_0` | Small-device MoE, ~1B active, native 128K | **Auto on 8 GB at 64K and 128K** |
| **Qwen 3.8 27B Unleashed** | `UD-IQ3_XXS`, `UD-Q3_K_XL` | Uncensored dense 27B, 262K, vision | Active catalog candidates |
| **Ornith 1.5 35A3B** | `Q4_K_M` MoE | Default auxiliary; 16 GB RAM-only main | Active auxiliary candidate |
| **Qwen 3.8 27B** | `Q4_K_M`, `Q8_0`, `BF16` ± MTP | Native image/video | Active catalog candidates |
| **Bonsai 27B** | Q1 / 1-bit | Still in the catalog; no longer the 8 GB Fit List default | Active catalog candidate |
| **MiniMax Music 3** | `minimax-music3` | Full-song music | Pinned integration candidate |
| **NVIDIA Parakeet TDT 0.6B v3** | `parakeet-tdt-0-6b-v3` | Local STT | Pinned integration candidate |
| **Soprano TTS** | `soprano-tts` | Local TTS | Pinned integration candidate |

### Dedicated VRAM

| Capacity | Main path |
|---|---|
| 96 GB+ | Qwen 3.8 27B 16-bit until Unleashed FP16 GGUF exists |
| 24–95 GB | Unleashed UD-Q3_K_XL + DFlash2 |
| 16 GB | Unleashed UD-IQ3_XXS + DFlash2 |
| 8 GB | Maple Preview TQ2_0; Ornith if host RAM can hold offloaded experts |
| Below 8 GB dedicated | Portable-fit only until that box is benched. Never a 9B. |

### Integrated / RAM-only total memory

| Capacity | Main path |
|---|---|
| 24 GB+ | Unleashed UD-Q3_K_XL |
| 16–23 GB | Ornith 1.5 35A3B |
| 8–15 GB | Maple Preview TQ2_0 |

## Mac local run — 2026-09-06 (M1 32 GB unified)

- **Unleashed UD-Q3_K_XL @ 262144 live on Metal**, port 11606, proven-recipe flags (`-ngl 99 --fit off -fa on -b 2048 -ub 512`, q4_0 KV, `--parallel 1`, mmproj loaded). Text + vision verified through the endpoint; Hermes main + vision pointed at it.
- Measured here: ~45–76 tok/s prompt, ~4.3 tok/s decode. The 38 tok/s evidence number is senter's CUDA box, not this Mac.
- **DFlash2 draft does NOT load on stock llama.cpp** (`wrong number of tensors; expected 81, got 58`) and embedded-MTP self-draft OOMs the Metal heap at 262k — so this box runs baseline until the fork builds.
- **dflash2-llama.cpp Metal build in progress** (`z-lab/llama.cpp-fork @ 1deefcca`, only a CUDA binary existed). Switch to `--spec-type draft-dflash` once it compiles.
- **Maple = default aux (2026-09-06):** TurboFit code updated (`recommended_artifact_families` + catalog `auxiliary_options` now lead with `maple-preview-tq2`, was Ornith). `maple-tq2_0.gguf` downloaded SHA-verified (5.45 GB). Stock llama.cpp can't load it (`unknown model architecture: 'maple'`) — building `stamsam/llama.cpp @ 9ee03eec` for Metal. No mmproj exists for Maple anywhere, so it serves text aux only; vision stays on Unleashed main. Target: Maple on :11612 at 262144 to match main.


*…truncated — full README at repo link*

## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/turbohaul-llmfit/README|turbohaul-llmfit]] — Generate optimized llama-server launch strings and turbohaul-manager manifests using llmfit hardware detection + TurboQuant flag doctrine (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/turbohaul-manager/README|turbohaul-manager]] — Ollama-shape inference manager using Tom's TurboQuant llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Blackwell. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/southpaw-turbohaul/README|southpaw-turbohaul]] — Curated model server for Nous Research community. Fork of turbohaul-manager with AtomicBot llama.cpp (TQ3/TQ4 + MTP + NextN) and Southpaw… (absorbed 2026-09-02; was DORMANT (since 2026-07-26))
- [[topics/_archive/sirvir/README|sirvir]] — Sirvir — GitHub-current TurboFit support for Hermes; installs TurboFit when missing, compares machine fit, answers Q&A, troubleshoots, an… (absorbed 2026-09-02; was ACTIVE)

## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| turbofit | [repo](https://github.com/SouthpawIN/turbofit) | ACTIVE | 83 |
| turbohaul-llmfit | [repo](https://github.com/SouthpawIN/turbohaul-llmfit) | DORMANT (since 2026-07-08) | 2 |
| turbohaul-manager | [repo](https://github.com/SouthpawIN/turbohaul-manager) | DORMANT (since 2026-07-08) | 1 |
| southpaw-turbohaul | [repo](https://github.com/SouthpawIN/southpaw-turbohaul) | DORMANT (since 2026-07-26) | 7 |
| sirvir | [repo](https://github.com/SouthpawIN/sirvir) | ACTIVE | 27 |
