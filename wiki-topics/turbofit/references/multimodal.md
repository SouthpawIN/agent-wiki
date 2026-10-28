---
title: Multimodal
updated: 2026-10-28
type: reference
tags: [turbofit, reference]
sources: [raw/sources/2026-10-28-github-consolidation.md]
---

> **Source of truth:** absorbed from [`SouthpawIN/turbofit`](https://github.com/SouthpawIN/turbofit) `docs/multimodal.md` @ `0ff572b` (2026-10-28). This vault copy is canonical for reading; the repo file remains the shipped copy.

# Multimodal model manager

## Multimodal model manager

Turbofit scans total usable memory and platform support, then labels each option as ready, candidate, unsupported, or too large. Candidate integrations are never marked ready until their adapter exists.

| Modality | Managed options |
|---|---|
| Image | Hermes configured image-generation provider |
| Video | Hermes configured video provider; MiniMax H3 research candidate |
| Music | Hermes music generation; MiniMax Music 3; ACE-Step 1.5 2B and 4B local candidates |
| Speech-to-text | Hermes local transcription; Parakeet TDT 0.6B v3; Nemotron 3.5 ASR 0.6B |
| Text-to-speech | Edge TTS; Soprano TTS; Darwin TTS 1.7B Cross |

### New multimodal candidates in 2.3

- **MiniMax Music 3** is pinned to the official [`MiniMaxAI/MiniMax-Music3`](https://huggingface.co/MiniMaxAI/MiniMax-Music3) commit `fbdf52fbaaca799592917417eb05f1899f1255ec`. Its model card describes complete songs up to five minutes, an 8B global LLM plus 0.6B local LLM, 32 kHz 16-bit stereo output, a full-precision route under 24 GB VRAM, and streamed CPU offload down to 8 GB VRAM.
- **NVIDIA Parakeet TDT 0.6B v3** is pinned to [`nvidia/parakeet-tdt-0.6b-v3`](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) commit `541d1f99c6b0c3cd0b11a95167540bb8edefd82b` as the new local speech-to-text candidate.
- **Soprano TTS** is pinned to [`MurrayMacdonald/soprano-tts`](https://huggingface.co/MurrayMacdonald/soprano-tts) commit `55651f7b114c8c2a4d98d612e9f13bfa3b6a8123` as the new local text-to-speech candidate.

All three remain explicitly labeled `candidate` until their Turbofit adapter and physical generation/transcription receipt pass. A pinned entry is reproducible metadata, not a false claim of completed integration.

![Turbofit 2.3 multimodal manager: MiniMax Music 3, Parakeet TDT 0.6B v3, Soprano TTS, and local MiniMax H3 video](https://github.com/SouthpawIN/turbofit/blob/main/assets/turbofit-2.3-multimodal.png)

The MiniMax H3 repository is a roughly 498 GB BF16 audio/video model release, not a small image model. Its official full-precision workflow recommends four GPUs. Turbofit separately preserves the physically demonstrated local INT8 streamed host-offload route: 24 GB accelerator memory minimum, 96 GB host RAM minimum, and 192 GB host RAM recommended. The 2.3 promo uses only clips generated locally on this machine from the pinned H3 revision in six requested styles; no sample footage or output from another machine is used. Prompts, seeds, timings, logs, checksums, contact sheet, TTS, and ffmpeg/ffprobe evidence are under `promo/`.

Catalog and pinned revisions: [`references/multimodal-models.json`](https://github.com/SouthpawIN/turbofit/blob/main/references/multimodal-models.json).

---


---

## Curated vault notes kept from the earlier copy (pre-2026-10-28)

Local multimodal (vision + long context) is the hard frontier.
> Grounded in [`ROADMAP.md`](../ROADMAP.md) and [`model-intel.md`](model-intel.md).
- **MoE + vision + 300K+ ctx doesn't fit one GPU.** A 24B dense or 744B MoE plus a vision tower plus 300K ctx exceeds 24GB. This is why there's no single local multimodal flagship yet.
- **Qwen3-Next-80B-A3B** — 3.4 tok/s, 300K ctx, MoE 3B active. The multimodal flagship, but needs ~2× 40GB to run at quality.
- **Qwen2.5-Omni-3B** — 49 tok/s, 3B, 300K ctx. The small always-on multimodal (fits anything). **3B models don't reach Tier S** — this is an aux, not a main.
- **Best current vision pairing**: Qwen3.5-35B-A3B + qwen3-vl-8b-instruct-v2 (76.31%).
- **Principle:** a 3B multimodal is an always-on aux; a real local multimodal main is a 2-GPU job today.