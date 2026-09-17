---
title: Creative Music
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Creative Music

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### llmc
- **Source:** `github:SouthpawIN/llmc`
- **Raw:** `[[raw/github/llmc-b616b18735.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** LLMC — LLM + MC. Your lyric and song companion. Hermes Agent profile. # LLMC — Song Forger & Creative Music Agent ![LLMC](https://v3b.fal.media/files/b/0a9fe98d/3gpcxPgerAOI5bEpZTsSI_9rTvA7HD.png) ## What LLMC Does LLMC is a creative music agent — "an LLM that's also an MC." It collaborates with the user to write lyrics in the Mc.Baldiee prose register (metaphorical, cosmic, never explicit) and generates full songs via ACE-Step, a local music generation model. The workflow: discuss themes → write lyrics → generate songs → deliver to Discord → add to Evolutionary Radio playlist. - **Writes lyrics** in Mc.Baldiee style — lighthouse metaphors, cosmic imagery, implicit truths through concrete…

### evolutionary-radio
- **Source:** `github:SouthpawIN/evolutionary-radio`
- **Raw:** `[[raw/github/evolutionary-radio-39587d4b1f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Continuous-play generative music radio — OmniStep 6B brain + ACE-Step 2B voice, with GEPA prompt evolution and Darwin weight evolution. # evolutionary-radio Hermes Agent profile: evolutionary-radio ## Install ## License MIT

### jammit
- **Source:** `github:SouthpawIN/jammit`
- **Raw:** `[[raw/github/jammit-3d4b2e04d8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** infinite ai generated radio in your terminal # Jammit: Infinite AI Music Radio A command-line tool for infinite AI music generation and playback, powered by the ACE-Step model. Generate and queue continuous music based on text prompts, all operating silently in the background. Perfect for creating endless ambient soundscapes or themed radio stations. ## Features * **Infinite Music Generation:** Continuously generates new music based on your prompt. * **Automatic Playback & Queuing:** Generated tracks are automatically played and queued for a seamless listening experience. * **Absolutely Silent Operation:** No console output during generation or playback (except for errors that bypass…

### veiled
- **Source:** `github:SouthpawIN/veiled`
- **Raw:** `[[raw/github/veiled-f2e8780100.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Veiled — cosmic prose lyricist & song forge Hermes Agent profile # Veiled — Cosmic Prose Lyricist & Song Forge A Hermes Agent profile that collaborates with you to write metaphorical, prophetic lyrics (Mc.Baldiee style) and forge them into songs via ACE-Step. ## Install Then launch: ## What it does 1. **Chat about themes** — describe a feeling, a situation, an idea 2. **Write lyrics** — Mc.Baldiee prose register: metaphorical, cosmic, never explicit 3. **Generate the song** — ACE-Step v1.5 on local GPU (~6s per song) 4. **Push to Discord** — MP3 + lyrics sent to your channel 5. **Build a playlist** — tracks feed into Evolutionary Radio ## Skills Included | Skill | Description |…

### ACE-Step-DAW
- **Source:** `github:SouthpawIN/ACE-Step-DAW`
- **Raw:** `[[raw/github/ace-step-daw-bc1069b6bf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** WIP... <p align="center"> <img src="public/logo-512.png" alt="ACE-Step DAW" width="120" /> </p> <h1 align="center">ACE-Step DAW</h1> <p align="center"> <strong>The AI-native DAW where every instrument knows what came before it.</strong> </p> <p align="center"> <a href="https://github.com/ace-step/ACE-Step-DAW/actions"><img src="https:<credential-redacted>" alt="CI" /></a> <a href="https://github.com/ace-step/ACE-Step-DAW/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0--or--later-blue.svg" alt="License" /></a> <img src="https://img.shields.io/badge/react-19-61DAFB?logo=react" alt="React 19" /> <img src="https://img.shields.io/badge/tone.js-15-F734D7" alt="Tone.js"…

### hermes-music-lora-pipeline
- **Source:** `github:SouthpawIN/hermes-music-lora-pipeline`
- **Raw:** `[[raw/github/hermes-music-lora-pipeline-c5a4db9e54.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** A Hermes-native pipeline for downloading, processing, captioning, and LoRA fine-tuning music generation models (AceStep/HeartMuLa). # Hermes-Native Music LoRA Training Pipeline This pipeline uses Hermes Agent's built-in tooling and skills to replace external, manual steps with automated, code-driven workflows. ## Architecture Note: AceStep vs. HeartMuLa You mentioned AceStep 1B or 3B. **AceStep is officially a 4B parameter model.** - If you proceed with **AceStep 4B**, your 2x RTX 3090 (24GB each) hardware is sufficient for LoRA fine-tuning with `bf16` and gradient checkpointing. - If you want a strictly **3B open-source alternative with turnkey Hermes skill support**, switch the target to…

### README
- **Source:** `local:.hermes/wiki/topics-wiki/creative-studio/README.md`
- **Raw:** `[[raw/local/readme-a4d024491e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Creative Studio created: 2026-07-07 updated: 2026-07-07 type: topic tags: [music, models, ace-step, llmc, training] --- # Creative Studio > The full creative pipeline: train models → generate music/audio. > OmniStep (model training) and ACE-Step (music generation) are the same pipeline. ## Pipeline ## Status | Component | State | |---|---| | ACE-Step API | 🔴 Stopped | | LLMC agent | 🟢 Active | | Evolution Radio | 🟡 Idle | | Model training | 🟡 Idle | ## Music Generation | Component | Path | |---|---| | ACE-Step API | `~/projects/ACE-Step-1.5/` | | LLMC (lyric agent) | `~/projects/llmc/` · `~/lyrics/journal.md` | | Evolution Radio | `~/projects/evolutionary-radio/` | | Music output…

### build-webgpu
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-webgpu.yml`
- **Raw:** `[[raw/local/build-webgpu-746c2e3995.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (webgpu) on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ '.github/workflows/build-webgpu.yml', '**/CMakeLists.txt', '**/.cmake', '**/*.h', '**/*.hpp', '**/*.c', '**/*.cpp', '**/*.wgsl' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/build-webgpu.yml', 'ggml/src/ggml-webgpu/**' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_ARG_LOG_COLORS: 1 LLAMA_ARG_LOG_PREFIX: 1 LLAMA_ARG_LOG_TIMESTAMPS: 1 jobs: format: runs-on: ubuntu-24.04 steps: - name: Clone uses: actions/checkout@v6 - name: Install…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/build-webgpu.yml`

### config
- **Source:** `local:projects/evolutionary-radio/code/config.yaml`
- **Raw:** `[[raw/local/config-27dd343455.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Evolutionary Radio — v0.2.0 configuration # All paths can be absolute or start with ~. Ports follow OmniSenter convention. brain: # OmniStep — text LLM, OpenAI-format API # Uses turbofit aux endpoint when available, falls back to ACE-Step's text encoder url: http://127.0.0.1:8082 model: omnisenter-6b timeout_sec: 30 # How to render a "vibe" string into a fully-formed ACE-Step tag string # (the prompt template is in prompt_template.py) system_prompt: | [REDACTED_SYSTEM_PROMPT] voice: # ACE-Step v1.5 SFT 2B — DiT decoder, audio synthesis url: http://127.0.0.1:8001 default_model: ace-step-v1.5-sft-2b # ACE-Step typical params (see acestep_client.py) duration_sec: 60 # Generations are slow;…

### SOUL
- **Source:** `local:projects/llmc/SOUL.md`
- **Raw:** `[[raw/local/soul-f779ef5f71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** You are LLMC — an LLM that's also an MC — your lyric and song companion. You exist at the intersection of poetry and sound, channeling the spirit of Mc.Baldiee's prophetic spoken-word videos into original lyrics and songs. ## Your Voice Your language is metaphorical, cosmic, and never explicit. You don't say "you should stand up for yourself" — you say "the lighthouse does not row out to the drowning / It stands / It burns." Translate themes into imagery rather than stating the lesson directly. When the user brings you a theme, identify the emotional core, then render it as concrete imagery. Ask questions before writing. ## Your Process 1. **Listen first.** When the user describes a theme,…

### README
- **Source:** `local:projects/southpaw/sovth-config/profiles/llmc/README.md`
- **Raw:** `[[raw/local/readme-a4756f317e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # 🎴 llmc ![LLMC](https://v3b.fal.media/files/b/0a9fe98d/3gpcxPgerAOI5bEpZTsSI_9rTvA7HD.png) > **Song Forger** — Creative music agent. Writes lyrics in Mc.Baldiee prose register and generates songs via ACE-Step local API. **TOWARDS SELF-IMPROVEMENT** --- **Official repo:** [SouthpawIN/llmc](https://github.com/SouthpawIN/llmc) --- *Part of the multi-agent fleet by SouthpawIN*

### README
- **Source:** `local:projects/llmc/README.md`
- **Raw:** `[[raw/local/readme-8801c5dbc8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLMC — Song Forger & Creative Music Agent ![LLMC](https://v3b.fal.media/files/b/0a9fe98d/3gpcxPgerAOI5bEpZTsSI_9rTvA7HD.png) ## What LLMC Does LLMC is a creative music agent — "an LLM that's also an MC." It collaborates with the user to write lyrics in the Mc.Baldiee prose register (metaphorical, cosmic, never explicit) and generates full songs via ACE-Step, a local music generation model. The workflow: discuss themes → write lyrics → generate songs → deliver to Discord → add to Evolutionary Radio playlist. - **Writes lyrics** in Mc.Baldiee style — lighthouse metaphors, cosmic imagery, implicit truths through concrete scenes - **Generates songs** via ACE-Step API (local, GPU-accelerated,…

### README
- **Source:** `local:projects/southpaw/llmc/README.md`
- **Raw:** `[[raw/local/readme-3cabd5815f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLMC — Song Forger & Creative Music Agent ![LLMC](https://v3b.fal.media/files/b/0a9fe926/RlyEwfZ4R8cH1QfEwhEXF_GpfTAHeo.png) ## What LLMC Does LLMC is a creative music agent — "an LLM that's also an MC." It collaborates with the user to write lyrics in the Mc.Baldiee prose register (metaphorical, cosmic, never explicit) and generates full songs via ACE-Step, a local music generation model. The workflow: discuss themes → write lyrics → generate songs → deliver to Discord → add to Evolutionary Radio playlist. - **Writes lyrics** in Mc.Baldiee style — lighthouse metaphors, cosmic imagery, implicit truths through concrete scenes - **Generates songs** via ACE-Step API (local, GPU-accelerated,…

### troubleshooting
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/models/audiocraft/references/troubleshooting.md`
- **Raw:** `[[raw/local/troubleshooting-af0c56aca0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # AudioCraft Troubleshooting Guide ## Installation Issues ### Import errors **Error**: `ModuleNotFoundError: No module named 'audiocraft'` **Solutions**: ### FFmpeg not found **Error**: `RuntimeError: ffmpeg not found` **Solutions**: ### PyTorch CUDA mismatch **Error**: `RuntimeError: CUDA error: no kernel image is available` **Solutions**: ### xformers issues **Error**: `ImportError: xformers` related errors **Solutions**: ## Model Loading Issues ### Out of memory during load **Error**: `torch.cuda.OutOfMemoryError` during model loading **Solutions**: ### Download failures **Error**: Connection errors or incomplete downloads **Solutions**: ### Wrong model type **Error**: Loading wrong…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/models/audiocraft/references/troubleshooting.md`, `local:projects/jestur/skills-capabilities/mlops/models/audiocraft/references/troubleshooting.md`, `local:projects/dev-coder/skills-capabilities/mlops/models/audiocraft/references/troubleshooting.md`, `local:projects/dev-orch/skills-capabilities/mlops/models/audiocraft/references/troubleshooting.md`, `local:projects/dev-review/skills-capabilities/mlops/models/audiocraft/references/troubleshooting.md`

### advanced-usage
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/models/audiocraft/references/advanced-usage.md`
- **Raw:** `[[raw/local/advanced-usage-5efe98c6eb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # AudioCraft Advanced Usage Guide ## Fine-tuning MusicGen ### Custom dataset preparation ### Fine-tuning with dora ### LoRA fine-tuning ## Multi-GPU Training ### DataParallel ### DistributedDataParallel ## Custom Conditioning ### Adding new conditioners ### Melody conditioning internals ## EnCodec Deep Dive ### Custom compression settings ### Streaming encoding ## MultiBand Diffusion ### Using MBD for enhanced quality ## API Server Deployment ### FastAPI server ### Batch processing service ## Integration Patterns ### LangChain tool ### Gradio with advanced controls ## Audio Processing Pipeline ### Post-processing chain ## Evaluation ### Audio quality metrics ## Model Comparison ### MusicGen…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/models/audiocraft/references/advanced-usage.md`, `local:projects/jestur/skills-capabilities/mlops/models/audiocraft/references/advanced-usage.md`, `local:projects/dev-coder/skills-capabilities/mlops/models/audiocraft/references/advanced-usage.md`, `local:projects/dev-orch/skills-capabilities/mlops/models/audiocraft/references/advanced-usage.md`, `local:projects/dev-review/skills-capabilities/mlops/models/audiocraft/references/advanced-usage.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/models/audiocraft/SKILL.md`
- **Raw:** `[[raw/local/skill-eebe52632e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: audiocraft-audio-generation description: "AudioCraft: MusicGen text-to-music, AudioGen text-to-sound." version: 1.0.0 author: Orchestra Research license: MIT dependencies: [audiocraft, torch>=2.0.0, transformers>=4.30.0] platforms: [linux, macos] metadata: hermes: tags: [Multimodal, Audio Generation, Text-to-Music, Text-to-Audio, MusicGen] --- # AudioCraft: Audio Generation Comprehensive guide to using Meta's AudioCraft for text-to-music and text-to-audio generation with MusicGen, AudioGen, and EnCodec. ## When to use AudioCraft **Use AudioCraft when:** - Need to generate music from text descriptions - Creating sound effects and environmental audio - Building music generation…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/models/audiocraft/SKILL.md`, `local:projects/jestur/skills-capabilities/mlops/models/audiocraft/SKILL.md`, `local:projects/dev-coder/skills-capabilities/mlops/models/audiocraft/SKILL.md`, `local:projects/dev-orch/skills-capabilities/mlops/models/audiocraft/SKILL.md`, `local:projects/dev-review/skills-capabilities/mlops/models/audiocraft/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/models/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-97a8c2c6c7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Specific model architectures and tools — image segmentation (Segment Anything / SAM) and audio generation (AudioCraft / MusicGen). Additional model skills (CLIP, Stable Diffusion, Whisper, LLaVA) are available as optional skills. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/mlops/models/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/media/songsee/SKILL.md`
- **Raw:** `[[raw/local/skill-d9d8d1394c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: songsee description: "Audio spectrograms/features (mel, chroma, MFCC) via CLI." version: 1.0.0 author: community license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [Audio, Visualization, Spectrogram, Music, Analysis] homepage: https://github.com/steipete/songsee prerequisites: commands: [songsee] --- # songsee Generate spectrograms and multi-panel audio feature visualizations from audio files. ## Prerequisites Requires [Go](https://go.dev/doc/install): Optional: `ffmpeg` for formats beyond WAV/MP3. ## Quick Start ## Visualization Types Use `--viz` with comma-separated values: | Type | Description | |------|-------------| | `spectrogram` | Standard frequency…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/media/songsee/SKILL.md`, `local:projects/jestur/skills-capabilities/media/songsee/SKILL.md`, `local:projects/dev-coder/skills-capabilities/media/songsee/SKILL.md`, `local:projects/dev-orch/skills-capabilities/media/songsee/SKILL.md`, `local:projects/dev-review/skills-capabilities/media/songsee/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/media/heartmula/SKILL.md`
- **Raw:** `[[raw/local/skill-d6f8322ba9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: heartmula description: "HeartMuLa: Suno-like song generation from lyrics + tags." version: 1.0.0 platforms: [linux, macos, windows] metadata: hermes: tags: [music, audio, generation, ai, heartmula, heartcodec, lyrics, songs] related_skills: [audiocraft] --- # HeartMuLa - Open-Source Music Generation ## Overview HeartMuLa is a family of open-source music foundation models (Apache-2.0) that generates music conditioned on lyrics and tags, with multilingual support. Generates full songs from lyrics + tags. Comparable to Suno for open-source. Includes: - **HeartMuLa** - Music language model (3B/7B) for generation from lyrics + tags - **HeartCodec** - 12.5Hz music codec for…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/media/heartmula/SKILL.md`, `local:projects/jestur/skills-capabilities/media/heartmula/SKILL.md`, `local:projects/dev-coder/skills-capabilities/media/heartmula/SKILL.md`, `local:projects/dev-orch/skills-capabilities/media/heartmula/SKILL.md`, `local:projects/dev-review/skills-capabilities/media/heartmula/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/media/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-c27bb2f0f3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for working with media content — YouTube transcripts, GIF search, music generation, and audio visualization. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/media/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/media/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/media/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/media/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/media/DESCRIPTION.md`

### python-api
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/python-api.md`
- **Raw:** `[[raw/local/python-api-f898b84a6c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # TouchDesigner Python API Reference ## The td Module TouchDesigner's Python environment auto-imports the `td` module. All TD-specific classes, functions, and constants live here. Scripts inside TD (Script DATs, CHOP/DAT Execute callbacks, Extensions) have full access. When using the MCP `execute_python_script` tool, these globals are pre-loaded: - `op` — shortcut for `td.op()`, finds operators by path - `ops` — shortcut for `td.ops()`, finds multiple operators by pattern - `me` — the operator running the script (via MCP this is the twozero internal executor) - `parent` — shortcut for `me.parent()` - `project` — the root project component - `td` — the full td module ## Finding Operators:…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/python-api.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/python-api.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/python-api.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/python-api.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/python-api.md`

### particles
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/particles.md`
- **Raw:** `[[raw/local/particles-066bb5ccb4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Particles Reference Particle systems in TouchDesigner — modern POPs (Particle Operators) and the legacy particleSOP path. For instancing static geometry (without per-instance lifetime/velocity), see `geometry-comp.md`. For GLSL-driven feedback simulations (no particle abstraction), see `operator-tips.md` (Feedback TOP section). Always call `td_get_par_info` for the op type before setting params. Param names below reflect TD 2025.32 — verify before relying on them. --- ## Two Paths: POPs vs. SOPs | | **POP family** (modern) | **particleSOP** (legacy) | |---|---|---| | GPU? | Yes (compute) | No (CPU) | | Particle count | 100k+ comfortably | ~5k before slowdown | | API style | Source / Force…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/particles.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/particles.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/particles.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/particles.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/particles.md`

### network-patterns
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/network-patterns.md`
- **Raw:** `[[raw/local/network-patterns-fd519867cc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # TouchDesigner Network Patterns Complete network recipes for common creative coding tasks. Each pattern shows the operator chain, MCP tool calls to build it, and key parameter settings. ## Audio-Reactive Visuals ### Pattern 1: Audio Spectrum -> Noise Displacement Audio drives noise parameters for organic, music-responsive textures. **MCP Build Sequence:** ### Pattern 2: Beat Detection -> Visual Pulses Detect beats from audio and trigger visual events. **Key parameter settings:** ### Pattern 3: Multi-Band Audio -> Multi-Layer Visuals Split audio into frequency bands, drive different visual layers per band. ### Pattern 3b: Audio-Reactive GLSL Fractal (Proven Recipe) Complete working recipe.…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/network-patterns.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/network-patterns.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/network-patterns.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/network-patterns.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/network-patterns.md`

### pitfalls
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/pitfalls.md`
- **Raw:** `[[raw/local/pitfalls-288f0da8ca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # TouchDesigner MCP — Pitfalls & Lessons Learned Hard-won knowledge from real TD sessions. Read this before building anything. ## Parameter Names ### 1. NEVER hardcode parameter names — always discover Parameter names change between TD versions. What works in one build may not work in another. ALWAYS use td_get_par_info to discover actual names from TD. The agent's LLM training data contains WRONG parameter names. Do not trust them. Known historical differences (may vary further — always verify): | What docs/training say | Actual in some versions | Notes | |---------------|---------------|-------| | `dat` | `pixeldat` | GLSL TOP pixel shader DAT | | `colora` | `alpha` | Constant TOP alpha |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/pitfalls.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/pitfalls.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/pitfalls.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/pitfalls.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/pitfalls.md`

### operators
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/operators.md`
- **Raw:** `[[raw/local/operators-ad67bbe288.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # TouchDesigner Operator Reference ## Operator Families Overview TouchDesigner has 6 operator families. Each family processes a specific data type and is color-coded in the UI. Operators can only connect to others of the SAME family (with cross-family converters as the bridge). ## TOPs — Texture Operators (Purple) 2D image/texture processing on the GPU. The workhorse of visual output. ### Generators (create images from nothing) | Operator | Type Name | Key Parameters | Use | |----------|-----------|---------------|-----| | Noise TOP | `noiseTop` | `type` (0-6), `monochrome`, `seed`, `period`, `harmonics`, `exponent`, `amp`, `offset`, `resolutionw/h` | Procedural noise textures — Perlin,…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/operators.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/operators.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/operators.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/operators.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/operators.md`

### animation
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/animation.md`
- **Raw:** `[[raw/local/animation-9c7482f38e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Animation Reference Patterns for time-based motion — keyframes, LFOs, timers, easing, expression-driven animation. Always call `td_get_par_info` for the op type before setting params. Param names below reflect TD 2025.32 but verify if errors fire. --- ## Time Sources TD has three time references — pick the right one. | Expression | Behavior | Use for | |---|---|---| | `absTime.seconds` | Wall-clock seconds since TD started. Never resets. | Continuous motion, GLSL `uTime`, infinite loops | | `absTime.frame` | Wall-clock frame count. | Frame-accurate triggers | | `me.time.frame` | Local component frame count (resets on play/stop). | Per-COMP animation timeline | | `me.time.seconds` | Local…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/animation.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/animation.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/animation.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/animation.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/animation.md`

### audio-reactive
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/audio-reactive.md`
- **Raw:** `[[raw/local/audio-reactive-3ea60c5954.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Audio-Reactive Reference Patterns for driving visuals from audio — spectrum analysis, beat detection, envelope following. ## Audio Input --- ## Audio Band Extraction (Verified TD 2025.32460) Use `audiofilterCHOP` for band separation (NOT `selectCHOP` by channel index): **Key TD 2025 corrections:** - `analyzeCHOP.par.function = 'rmspower'` NOT `'rms'` - `lagCHOP.par.lag1` / `par.lag2` NOT `par.lagin` / `par.lagout` - `mathCHOP` has NO `par.clamp` — use separate `limitCHOP` --- ## Beat / Onset Detection ### Kick Detection (slope → trigger) --- ## Passing Audio to GLSL --- ## Standard Audio Bus Pattern Recommended structure: Keep this entire bus inside a `baseCOMP` (e.g., `audio_bus`) and…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/audio-reactive.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/audio-reactive.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/audio-reactive.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/audio-reactive.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/audio-reactive.md`

### dat-scripting
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/dat-scripting.md`
- **Raw:** `[[raw/local/dat-scripting-062ea3608b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DAT-Based Scripting Reference TD's event/callback model — Python that runs in response to network events. The full set of "Execute DATs" plus their idiomatic patterns. For arbitrary Python execution (not callback-based), see `python-api.md`. For the MCP's `td_execute_python` tool, see `mcp-tools.md`. --- ## The Execute DAT Family Every type watches one kind of event source and fires Python on changes. | DAT | Watches | Use for | |---|---|---| | `chopExecuteDAT` | A CHOP's channel values | Audio triggers, threshold callbacks, state machines on numeric input | | `datExecuteDAT` | A DAT's content (table cells, text) | Reacting to data updates from APIs, parsing webDAT responses | |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/dat-scripting.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/dat-scripting.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/dat-scripting.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/dat-scripting.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/dat-scripting.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/SKILL.md`
- **Raw:** `[[raw/local/skill-70a4217786.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: touchdesigner-mcp description: "Control a running TouchDesigner instance via twozero MCP — create operators, set parameters, wire connections, execute Python, build real-time visuals. 36 native tools." version: 1.1.0 author: kshitijk4poor license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [TouchDesigner, MCP, twozero, creative-coding, real-time-visuals, generative-art, audio-reactive, VJ, installation, GLSL] related_skills: [native-mcp, ascii-video, manim-video, hermes-video] --- # TouchDesigner Integration (twozero MCP) ## CRITICAL RULES 1. **NEVER guess parameter names.** Call `td_get_par_info` for the op type FIRST. Your training data is wrong for TD…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/songwriting-and-ai-music/SKILL.md`
- **Raw:** `[[raw/local/skill-093dfa88e5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: songwriting-and-ai-music description: "Songwriting craft and Suno AI music prompts." tags: [songwriting, music, suno, parody, lyrics, creative] platforms: [linux, macos, windows] triggers: - writing a song - song lyrics - music prompt - suno prompt - parody song - adapting a song - AI music generation --- # Songwriting & AI Music Generation Everything here is a GUIDELINE, not a rule. Art breaks rules on purpose. Use what serves the song. Ignore what doesn't. --- ## 1. Song Structure (Pick One or Invent Your Own) Common skeletons — mix, modify, or throw out as needed: The six building blocks: - Intro — set the mood, pull the listener in - Verse — the story, the details, the…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/songwriting-and-ai-music/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/songwriting-and-ai-music/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/songwriting-and-ai-music/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/songwriting-and-ai-music/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/songwriting-and-ai-music/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/p5js/SKILL.md`
- **Raw:** `[[raw/local/skill-c53ef27d3e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: p5js description: "p5.js sketches: gen art, shaders, interactive, 3D." version: 1.0.0 platforms: [linux, macos, windows] metadata: hermes: tags: [creative-coding, generative-art, p5js, canvas, interactive, visualization, webgl, shaders, animation] related_skills: [ascii-video, manim-video, excalidraw] --- # p5.js Production Pipeline ## When to use Use when users request: p5.js sketches, creative coding, generative art, interactive visualizations, canvas animations, browser-based visual art, data viz, shader effects, or any p5.js project. ## What's inside Production pipeline for interactive and generative visual art using p5.js. Creates browser-based sketches, generative art, data…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/p5js/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/p5js/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/p5js/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/p5js/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/p5js/SKILL.md`

### README
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/p5js/README.md`
- **Raw:** `[[raw/local/readme-8251be0e41.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # p5.js Skill Production pipeline for interactive and generative visual art using [p5.js](https://p5js.org/). ## What it does Creates browser-based visual art from text prompts. The agent handles the full pipeline: creative concept, code generation, preview, export, and iterative refinement. Output is a single self-contained HTML file that runs in any browser — no build step, no server, no dependencies beyond a CDN script tag. The output is real interactive art. Not tutorial exercises. Generative systems, particle physics, noise fields, shader effects, kinetic typography — composed with intentional color palettes, layered composition, and visual hierarchy. ## Modes | Mode | Input | Output |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/p5js/README.md`, `local:projects/jestur/skills-capabilities/creative/p5js/README.md`, `local:projects/dev-coder/skills-capabilities/creative/p5js/README.md`, `local:projects/dev-orch/skills-capabilities/creative/p5js/README.md`, `local:projects/dev-review/skills-capabilities/creative/p5js/README.md`

### updaters-and-trackers
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/manim-video/references/updaters-and-trackers.md`
- **Raw:** `[[raw/local/updaters-and-trackers-96c024dce5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Updaters and Value Trackers ## The problem updaters solve Normal animations are discrete: `self.play()` goes from state A to state B. But what if you need continuous relationships — a label that always hovers above a moving dot, or a line that always connects two points? Without updaters, you'd manually reposition every dependent object before every `self.play()`. Five animations that move a dot means five manual repositioning calls for the label. Miss one and it freezes in the wrong spot. Updaters let you declare a relationship ONCE. Manim calls the updater function EVERY FRAME (15-60 fps depending on quality) to enforce that relationship, no matter what else is happening. ##…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/jestur/skills-capabilities/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/dev-coder/skills-capabilities/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/dev-orch/skills-capabilities/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/dev-review/skills-capabilities/creative/manim-video/references/updaters-and-trackers.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/manim-video/SKILL.md`
- **Raw:** `[[raw/local/skill-3459a6af99.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: manim-video description: "Manim CE animations: 3Blue1Brown math/algo videos." version: 1.0.0 platforms: [linux, macos, windows] --- # Manim Video Production Pipeline ## When to use Use when users request: animated explanations, math animations, concept visualizations, algorithm walkthroughs, technical explainers, 3Blue1Brown style videos, or any programmatic animation with geometric/mathematical content. Creates 3Blue1Brown-style explainer videos, algorithm visualizations, equation derivations, architecture diagrams, and data stories using Manim Community Edition. ## Creative Standard This is educational cinema. Every frame teaches. Every animation reveals structure. **Before…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/manim-video/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/manim-video/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/manim-video/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/manim-video/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/manim-video/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/ascii-video/SKILL.md`
- **Raw:** `[[raw/local/skill-1d4f84e0ea.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ascii-video description: "ASCII video: convert video/audio to colored ASCII MP4/GIF." platforms: [linux, macos, windows] --- # ASCII Video Production Pipeline ## When to use Use when users request: ASCII video, text art video, terminal-style video, character art animation, retro text visualization, audio visualizer in ASCII, converting video to ASCII art, matrix-style effects, or any animated ASCII output. ## What's inside Production pipeline for ASCII art video — any format. Converts video/audio/images/generative input into colored ASCII character video output (MP4, GIF, image sequence). Covers: video-to-ASCII conversion, audio-reactive music visualizers, generative ASCII art…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/ascii-video/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/ascii-video/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/ascii-video/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/ascii-video/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/ascii-video/SKILL.md`

### README
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/ascii-video/README.md`
- **Raw:** `[[raw/local/readme-a182ea6fd8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ☤ ASCII Video Renders any content as colored ASCII character video. Audio, video, images, text, or pure math in, MP4/GIF/PNG sequence out. Full RGB color per character cell, 1080p 24fps default. No GPU. Built for [Hermes Agent](https://github.com/NousResearch/hermes-agent). Usable in any coding agent. Canonical source lives here; synced to [`NousResearch/hermes-agent/skills-capabilities/creative/ascii-video`](https://github.com/NousResearch/hermes-agent/tree/main/skills-capabilities/creative/ascii-video) via PR. ## What this is A skill that teaches an agent how to build single-file Python renderers for ASCII video from scratch. The agent gets the full pipeline: grid system, font rasterization, effect library,…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/ascii-video/README.md`, `local:projects/jestur/skills-capabilities/creative/ascii-video/README.md`, `local:projects/dev-coder/skills-capabilities/creative/ascii-video/README.md`, `local:projects/dev-orch/skills-capabilities/creative/ascii-video/README.md`, `local:projects/dev-review/skills-capabilities/creative/ascii-video/README.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-e890a87ac4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Creative content generation — ASCII art, hand-drawn style diagrams, and visual design tools. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/creative/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/creative/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/creative/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/creative/DESCRIPTION.md`

### 1499496455805866186-AI-Co-Listener--Music-Stream
- **Source:** `discord-archive:archives/community-projects-showcase/1499496455805866186-AI-Co-Listener--Music-Stream.txt`
- **Raw:** `[[raw/discord/1499496455805866186-ai-co-listener--music-stream-1e81e52f46.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'AI Co-Listener (Music Stream)' in forum #community-projects-showcase # thread_id=1499496455805866186 forum_id=1316137596535177246 # Started 2026-05-10T19:49:32.908143+00:00 [2026-04-30T19:43:34.361000+00:00] blandsteak (id=1499496455805866186) WZRD Listen is an AI that witnesses the music you stream and saves it to an archive you own. Keep proof. Carry your history across devices. Collect rewards as the network opens. Available on the Chrome Store: https://chromewebstore.google.com/detail/wzrd-listen/dajdmadifhogknlbdoeocdageopkkgjj?utm_source=item-share-x [embed] WZRD Listen - Chrome Web Store…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1499496455805866186-AI-Co-Listener--Music-Stream.txt`

### 1491489761821589615-Jammit---TUI-infinite-radio
- **Source:** `discord-archive:archives/community-projects-showcase/1491489761821589615-Jammit---TUI-infinite-radio.txt`
- **Raw:** `[[raw/discord/1491489761821589615-jammit---tui-infinite-radio-f3fa2ef5be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Jammit - TUI infinite radio' in forum #community-projects-showcase # thread_id=1491489761821589615 forum_id=1316137596535177246 # Started 2026-05-10T19:50:33.053532+00:00 [2026-04-08T17:29:10.760000+00:00] petersteele111 (id=1491490101568475346) Thanks, ill try it out 🙂 [2026-04-08T17:33:35.242000+00:00] .s0uthpaw (id=1491491210886381648) Oohhh I'm deleting this room, we have two of these [2026-04-08T17:33:37.526000+00:00] .s0uthpaw (id=1491491220466303157) My b [2026-04-08T17:33:55.621000+00:00] .s0uthpaw (id=1491491296362365091) I'll tag you in the correct one <@648742401703149612> [2026-04-08T18:03:25.573000+00:00] petersteele111 (id=1491498720078856294) kk…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1491489761821589615-Jammit---TUI-infinite-radio.txt`

### 1490207822103973931-Infinite-radio-while-Hermes-works
- **Source:** `discord-archive:archives/community-projects-showcase/1490207822103973931-Infinite-radio-while-Hermes-works.txt`
- **Raw:** `[[raw/discord/1490207822103973931-infinite-radio-while-hermes-works-6bf20d9d71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Infinite radio while Hermes works' in forum #community-projects-showcase # thread_id=1490207822103973931 forum_id=1316137596535177246 # Started 2026-05-10T19:51:20.849307+00:00 [2026-04-05T04:33:51.512000+00:00] .s0uthpaw (id=1490207822103973931) https://github.com/SouthpawIN/jammit [embed] GitHub - SouthpawIN/jammit: infinite ai generated radio in your ter... https://github.com/SouthpawIN/jammit [2026-04-06T22:24:57.236000+00:00] nasumone (id=1490839759952547870) excellent [2026-04-06T22:25:26.008000+00:00] nasumone (id=1490839880631193822) is this using icecast? [2026-04-06T22:26:19.252000+00:00] nasumone (id=1490840103952715917) ive been looking for a way to generate looping…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1490207822103973931-Infinite-radio-while-Hermes-works.txt`

### 1388642135250829383-Exploration---Exploitation
- **Source:** `discord-archive:archives/community-projects-showcase/1388642135250829383-Exploration---Exploitation.txt`
- **Raw:** `[[raw/discord/1388642135250829383-exploration---exploitation-257e754bd3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Exploration - Exploitation' in forum #community-projects-showcase # thread_id=1388642135250829383 forum_id=1316137596535177246 # Started 2026-05-10T19:51:37.496642+00:00 [2025-06-28T22:08:04.767000+00:00] soulbinny (id=1388642135250829383) Successfully integrated P2E with TRPO, When exploration meets exploitation its an amazing model to use and is sample efficient even after using an TRPO achieving 1400 + rewards under 3k episodes on humanoid v5 not an easy task for such crazy integration [2025-06-28T22:52:49.697000+00:00] teknium (id=1388653396663206051) What's P2E? [reply to soulbinny msg=1388642135250829383] [2025-06-29T13:29:39.384000+00:00] soulbinny (id=1388874057683828806)…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1388642135250829383-Exploration---Exploitation.txt`

### guide
- **Source:** `local:docs/llmc-song-creation-ace-step/guide.md`
- **Raw:** `[[raw/local/guide-ab5a403c71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLMC Song Creation Workflow with ACE-Step ## Summary ACE-Step 1.5 is an open-source music foundation model that generates complete songs — vocals and instrumentation together — from text descriptions and lyrics. It runs locally on consumer hardware (CUDA, Apple Silicon, AMD ROCm, Intel XPU, CPU), produces commercial-grade output comparable to Suno v4.5/v5, and can render a 4-minute song in under 20 seconds on consumer GPUs or under 2 seconds on an A100. This guide documents a practical, reusable workflow for the **LLMC** song-creation pipeline: setting up ACE-Step, selecting the right model for your VRAM, preparing long-form lyrics (78–109 lines), shaping style prompts (e.g. thall/metal),…

### ace-step
- **Source:** `local:research/crow-lore/ace-step-music-generation/entities/ace-step.md`
- **Raw:** `[[raw/local/ace-step-2e208d683f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 ## Identity ACE-Step is an open-source music foundation model that generates complete songs (vocals + instrumentation) from text descriptions or lyrics. Version 1.5 is the current release, achieving commercial-grade quality on consumer hardware. ## Architecture Hybrid architecture combining: - **Language Model (LM)** as planner — processes lyrics/style into a structured plan - **Diffusion Transformer (DiT)** for audio synthesis — generates the actual audio This allows Chain-of-Thought reasoning to guide generation. ## Performance - <2 seconds per song on A100 - <10 seconds on RTX 3090 - ~20 seconds on consumer hardware - Up to 15x faster than LLM-based baselines - Batch…

### audio-duration
- **Source:** `local:research/crow-lore/ace-step-music-generation/concepts/audio-duration.md`
- **Raw:** `[[raw/local/audio-duration-01af3276e8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # audio_duration Parameter ## Behavior The `audio_duration` parameter in ACE-Step functions as a **cap (maximum), not a target**. The model will generate audio up to the specified duration, but the actual output length depends on the input (lyrics, style) and the model's generation behavior. ## User Observation - 30+ lines of lyrics → 213 seconds output - This suggests the model generates audio proportional to lyrical content, with audio_duration as the upper bound ## API Parameter (Segmind) - **Field:** `Duration (seconds)` / `output_seconds` - **Range:** 10 - 240 seconds - **Default:** 60 seconds - **Usage:** 30-60 sec for trailers/ads, 120-180 sec for full demos ## Best Practices - Set…

### vram-selection
- **Source:** `local:research/crow-lore/ace-step-music-generation/concepts/vram-selection.md`
- **Raw:** `[[raw/local/vram-selection-3daa8d4353.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # VRAM Model Selection Guide ACE-Step 1.5 provides multiple model sizes to fit different hardware. Selecting the right combination of DiT and LM models is critical for performance. ## Selection Table | VRAM | Recommended DiT | Recommended LM | Notes | | :--- | :--- | :--- | :--- | | **≤6GB** | 2B turbo | None (DiT only) | LM disabled by default; INT8 quantization + CPU offload | | **6-8GB** | 2B turbo | `acestep-5Hz-lm-0.6B` | Lightweight LM with PyTorch backend | | **16-20GB** | 2B sft or XL turbo | `acestep-5Hz-lm-1.7B` | XL requires CPU offload below 20GB | | **≥20GB** | XL sft (or xl-base) | `acestep-5Hz-lm-4B` | Best quality; all models fit without offload | ## Model Zoo ### DiT Models…

### index
- **Source:** `local:research/crow-lore/ace-step-music-generation/index.md`
- **Raw:** `[[raw/local/index-5bcbab81a1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Music Generation ## Summary ACE-Step is an open-source music foundation model that generates complete songs (vocals + instrumentation) from text descriptions or lyrics. Version 1.5 achieves commercial-grade quality comparable to Suno v4.5/v5, runs locally on consumer hardware (Mac, AMD, Intel, CUDA), and generates 4-minute songs in under 20 seconds on an A100 GPU. ## Key Facts - **License:** MIT (GitHub), Apache 2.0 (foundation model) - **Architecture:** Hybrid — Language Model (LM) planner + Diffusion Transformer (DiT) for audio synthesis - **Speed:** <2s per song on A100, <10s on RTX 3090, ~20s on consumer hardware - **Multilingual:** 15-19 languages supported - **Batch…

### SKILL
- **Source:** `local:projects/llmc/skills-capabilities/llmc-song-pipeline/SKILL.md`
- **Raw:** `[[raw/local/skill-06c93adff6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: llmc-song-pipeline description: "Standardized LLMC song creation pipeline: lyric writing → ACE-Step generation → MP3 conversion → Discord delivery → playlist integration. Enforces naming, format, and delivery conventions." version: 1.0.0 tags: [music, llmc, ace-step, song-forge, discord, pipeline, mc-baldiee] triggers: - generate songs - llmc batch - create song - song forge - batch generate --- # LLMC Song Pipeline — Standardized The definitive pipeline for batch song creation. Every time the user asks for songs, follow this exact process. ## 1. Lyric Writing ### Style: Mc.Baldiee Cosmic Prose Load the `mc-baldiee-prose` skill for the full style guide. Core rules: - **Direct…

### AGENTS
- **Source:** `local:projects/llmc/AGENTS.md`
- **Raw:** `[[raw/local/agents-ff35815c12.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLMC — Song Forge Agent ## Role LLMC is a creative music agent that collaborates with the user to write lyrics and generate songs. The workflow is: chat about themes → write lyrics (Mc.Baldiee prose style) → generate via ACE-Step → push to Discord → add to playlist for Evolutionary Radio. ## Workflow ### 1. Theme Discussion When the user describes a song idea: - Engage with genuine curiosity - Ask about the emotional core, not just the topic - Identify the unspoken truth (the thing the song is REALLY about) - Discuss musical style (default: dark cinematic rap, but adjustable) ### 2. Lyric Writing - Load `mc-baldiee-prose` skill for the prose style guide - Load `lyric-journal` skill for…

### distribution
- **Source:** `local:projects/llmc/distribution.yaml`
- **Raw:** `[[raw/local/distribution-c3199fac34.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: llmc version: 0.2.0 description: "LLMC — LLM + MC. Your lyric and song companion. Chats about themes, writes Mc.Baldiee-style metaphorical lyrics, generates songs via ACE-Step, pushes to Discord, and builds a playlist that feeds into Evolutionary Radio." author: SouthpawIN license: MIT homepage: https://github.com/SouthpawIN/llmc hermes_requires: ">=0.12.0" distribution_owned: - SOUL.md - AGENTS.md - config.yaml - skills-capabilities/ - herm/ - README.md env_requires: - name: GLM_API_KEY description: "Z.AI GLM API key (or any LLM provider key via OpenRouter/Nous)" required: false - name: DISCORD_BOT_TOKEN description: "Discord bot token for sharing songs to Discord channels" required: false

### config
- **Source:** `local:projects/llmc/config.yaml`
- **Raw:** `[[raw/local/config-c2a8e5fdc2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: default: z-ai/glm-5.2 provider: nous personality: "You are LLMC — a cosmic prose lyricist and song forger. Warm but weighty. Metaphorical, never explicit. You channel Mc.Baldiee's prophetic spoken-word energy into original lyrics and songs." display: skin: poseidon tts: provider: edge edge: voice: en-US-GuyNeural agent: max_turns: 90 tool_use_enforcement: auto memory: memory_enabled: true user_profile_enabled: true skills: template_vars: true context: engine: compressor toolsets: - hermes-cli platform_toolsets: cli: - file - image_gen - memory - skills - terminal - todo - vision - web

### peelingflesh-dna
- **Source:** `local:projects/llmc/skills-capabilities/slam-song-forge/references/peelingflesh-dna.md`
- **Raw:** `[[raw/local/peelingflesh-dna-70d4eeb125.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # PeelingFlesh — Gangster Slam DNA Analysis Source: "The G Code" (2024, Unique Leader Records) URL: https://youtu.be/XA7XtYW0TkY ## Genre Classification PeelingFlesh occupies a unique niche: **gangster slam death metal with hip-hop crossover**. It's brutal death metal structurally (downtuned guitars, blast beats, guttural vocals) but with the attitude, structure, and swagger of hardcore/gangster rap. DJ scratches over blast beats. Skits over breakdowns. Boast chains over chromatic riffs. Not pure death metal. Not deathcore. Slam death metal with street energy. ## The G Code — Album Structure Pattern: ~26 min, 10 tracks, 2 interludes, 4 guest features. Dense. ## Lyric DNA ### Technique 1:…

### kublai-khan-dna
- **Source:** `local:projects/llmc/skills-capabilities/slam-song-forge/references/kublai-khan-dna.md`
- **Raw:** `[[raw/local/kublai-khan-dna-95271d3979.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Kublai Khan TX — Genre DNA Beam from Kublai Khan's *Nomad* album (2017, Rise Records). Metallic hardcore / beatdown — DIFFERENT from PeelingFlesh gangster slam. ## Sound Characteristics | Dimension | Kublai Khan Beatdown | |-----------|---------------------| | Guitars | Beefy distorted hardcore chords, pinch harmonics, gnarly low-pitched chordal riffs, crunchy ballsy tone | | Drums | Grid-rigid grooves, massive breakdowns, double-bass sections, busy kit fills | | Vocals | Strained, monotone, shouted/yelled (NOT growls), venomous, blunt delivery | | Production | Crisp, clear, utterly crushing even on basic sections | | Tempo | 75-90 BPM (slower than slam's 105-200) | | Tuning | Drop B…

### SKILL
- **Source:** `local:projects/llmc/skills-capabilities/slam-song-forge/SKILL.md`
- **Raw:** `[[raw/local/skill-1e369e998b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: slam-song-forge description: "End-to-end brutal death metal / slam AND metallic hardcore / beatdown song generation pipeline. PeelingFlesh gangster slam + Kublai Khan-style hardcore. Lyrics to ACE-Step generation to 3:33 MP3 output to Discord push." version: 1.1.0 tags: [slam, death-metal, brutal-deathcore, peelingflesh, hardcore, beatdown, kublai-khan, metallic-hardcore, music, ace-step, generation, beats, metal] triggers: - generate slam songs - make death metal songs - create slam album - brutal death metal - PeelingFlesh style - slam deathcore - gangster slam - make hardcore songs - beatdown hardcore - Kublai Khan style - metallic hardcore - Nomad style - 3:33 songs --- # SLAM…

### sleep-token-dna
- **Source:** `local:projects/llmc/skills-capabilities/llmc-song-forge/references/sleep-token-dna.md`
- **Raw:** `[[raw/local/sleep-token-dna-34e3376a6a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Sleep Token — Take Me Back To Eden Influence DNA ## Source Album: *Take Me Back To Eden* (2023, 12 tracks, ~61 min) Key study tracks: The Summoning, Chokehold, Take Me Back To Eden, Ascensionism ## Techniques to ADAPT (not copy) ### Worship/Devotional Metaphor The speaker addresses a deity-like figure. The relationship is asymmetrical — one gives everything, the other observes. **Adapt**: frame the boundary-setting as leaving a church, breaking a covenant, rejecting an altar. ### Dynamic Contrast Whisper verses → explosive screamed choruses → R&B falsetto hooks → spoken bridges. **Adapt**: use structure tags with modifiers: `[Verse 1 - whispered]`, `[Chorus - explosive]`, `[Bridge -…

### ace-step-caption-guide
- **Source:** `local:projects/llmc/skills-capabilities/llmc-song-forge/references/ace-step-caption-guide.md`
- **Raw:** `[[raw/local/ace-step-caption-guide-f326f94868.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Caption & Lyrics Format Guide Summarized from official docs (INFERENCE.md, Tutorial.md) — June 2026. ## Caption (MOST critical input) Be specific. Combine these dimensions: - **Style/genre**: southern hip-hop, dark R&B, boom bap, progressive metal trap - **Instruments**: piano, 808s, snare, strings, synth, guitar - **Emotion**: aggressive, vulnerable, haunting, triumphant - **Timbre/texture**: warm tape saturation, vinyl crackle, metallic reverb, analog warmth - **Era/production**: 2008 Cash Money, 90s East Coast, Hans Zimmer cinematic - **Vocals**: falsetto, chest voice, whispered, screamed, conversational - **Rhythm**: double-time hi-hats, half-time drums, swing, syncopated -…

### SKILL
- **Source:** `local:projects/llmc/skills-capabilities/llmc-song-forge/SKILL.md`
- **Raw:** `[[raw/local/skill-eb71605721.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: llmc-song-forge description: "End-to-end rap song generation pipeline with Lil Wayne C3 influence blended with Mc.Baldiee cosmic prose. Lyrics → ACE-Step generation → 3:33 MP3 output → Discord push." version: 3.0.0 tags: [rap, lyrics, music, ace-step, lil-wayne, mc-baldiee, generation, beats] triggers: - generate rap songs - make LLMC songs - create rap album - Wayne-style rap - cosmic rap lyrics - 3:33 songs - blend influences into rap --- # LLMC Song Forge v3 — Wayne ✕ Mc.Baldiee ✕ Sleep Token Three-register rap pipeline: Lil Wayne C3 swagger + Mc.Baldiee cosmic prose + Sleep Token worship vulnerability. Every song at 3:33 with ffmpeg trim. ## Architecture ## Three-Register…

### model-zoo-and-hardware
- **Source:** `local:projects/llmc/skills-capabilities/acestep/references/model-zoo-and-hardware.md`
- **Raw:** `[[raw/local/model-zoo-and-hardware-87bf054875.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Model Zoo & Hardware Guide Complete model specs and GPU selection matrix from the official README. ## DiT Models (Audio Decoder) ### 2B Models | Model | CFG | Steps | Text2Music | Cover | Repaint | Extract | Lego | Complete | Quality | HuggingFace | |-------|:---:|:-----:|:----------:|:-----:|:------:|:-------:|:----:|:--------:|---------|-------------| | `acestep-v15-base` | ✅ | 50 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Medium | [Link](https://huggingface.co/ACE-Step/acestep-v15-base) | | `acestep-v15-sft` | ✅ | 50 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | High | [Link](https://huggingface.co/ACE-Step/acestep-v15-sft) | | `acestep-v15-turbo` | ❌ | 8 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | Very High |…

### lora-training-deep-dive
- **Source:** `local:projects/llmc/skills-capabilities/acestep/references/lora-training-deep-dive.md`
- **Raw:** `[[raw/local/lora-training-deep-dive-2b344b3dea.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step LoRA Training — Deep Dive Condensed from the official tutorial at https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/LoRA_Training_Tutorial.md and FM9 guide at https://fm9.ai/ace-step/lora-training ## Dataset Format (Per Song) Each song in the dataset folder needs: | File | Required | Notes | |------|----------|-------| | `{name}.mp3` / `.wav` / `.flac` / `.ogg` / `.opus` | Yes | Audio file | | `{name}.lyrics.txt` | Yes | Lyrics with structural tags | | `{name}.json` | Optional | Annotations: caption, bpm, keyscale, timesignature, language | | `{name}.caption.txt` | Optional | Free-text caption (can also be in JSON) | JSON annotation example: ## Gradio UI Step-by-Step…

### SKILL
- **Source:** `local:projects/llmc/skills-capabilities/acestep/SKILL.md`
- **Raw:** `[[raw/local/skill-56e31c9e55.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep description: "ACE-Step 1.5 — local music generation (2B/4B DiT) with built-in LoRA fine-tuning. Generate songs from lyrics + tags, train style LoRAs from 8+ tracks." version: 1.0.0 platforms: [linux, macos, windows] metadata: hermes: tags: [music, audio, generation, ai, acestep, ace-step, lora, fine-tuning, rap, beats] related_skills: [heartmula, evolutionary-radio, songwriting-and-ai-music, comfyui] --- # ACE-Step 1.5 — Local Music Generation & LoRA Training ## Overview ACE-Step 1.5 is a hybrid-architecture music generation model (LM planner + DiT decoder) that runs locally and supports LoRA fine-tuning from just 8 songs. Co-developed by ACE Studio & StepFun. Quality…

### duration-cap
- **Source:** `local:projects/llmc/skills-capabilities/acestep/references/duration-cap.md`
- **Raw:** `[[raw/local/duration-cap-2c326c58a0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Duration: Lyrics Length = Actual Duration Verified 2026-06-23 against ACE-Step discussion #95 and live generation on RTX 3090. ## The Rule `audio_duration` is a **CAP**, not a target. ACE-Step generates audio until it runs out of lyrical content. The DiT doesn't pad silence to fill the cap. ## Verified Line-to-Duration Map Tested with `thinking: false` (`/release_task` endpoint), 4B XL SFT DiT, 50 inference steps: | Lines | Raw Duration | Genre | Notes | |-------|-------------|-------|-------| | 15 | 86s | Slam death metal | Barked one-liners, minimal syllables | | 30 | 213s | Slam death metal | 3 verses + 3 breakdowns + intro/outro | ## Duration Formula ## Two Paths to Correct…

### README
- **Source:** `local:projects/ACE-Step-1.5/checkpoints/acestep-v15-xl-sft/README.md`
- **Raw:** `[[raw/local/readme-6cfd536f95.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- library_name: transformers license: mit pipeline_tag: text-to-audio tags: - feature-extraction - audio - music - text2music - custom_code --- <h1 align="center">ACE-Step 1.5 XL — SFT (4B DiT)</h1> <p align="center"> <a href="https://ace-step.github.io/ace-step-v1.5.github.io/">Project</a> | <a href="https://huggingface.co/collections/ACE-Step/ace-step-15">Hugging Face</a> | <a href="https://modelscope.cn/collections/ACE-Step/Ace-Step-15-xl">ModelScope</a> | <a href="https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5">Space Demo</a> | <a href="https://discord.gg/PeWDxrkdj7">Discord</a> | <a href="https://arxiv.org/abs/2602.00744">Tech Report</a> </p> ## Model Details This is the **XL…

### README
- **Source:** `local:projects/ACE-Step-1.5/checkpoints/README.md`
- **Raw:** `[[raw/local/readme-69d69b89e3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- library_name: transformers license: mit pipeline_tag: text-to-audio tags: - audio - music - text2music --- <h1 align="center">ACE-Step 1.5</h1> <h1 align="center">Pushing the Boundaries of Open-Source Music Generation</h1> <p align="center"> <a href="https://ace-step.github.io/ace-step-v1.5.github.io/">Project</a> | <a href="https://huggingface.co/collections/ACE-Step/ace-step-15">Hugging Face</a> | <a href="https://modelscope.cn/models/ACE-Step/Ace-Step1.5">ModelScope</a> | <a href="https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5">Space Demo</a> | <a href="https://discord.gg/PeWDxrkdj7">Discord</a> <a href="https://arxiv.org/abs/2602.00744">Tech Report</a> </p>…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/checkpoints/README.md`

### pyproject
- **Source:** `local:projects/omnistudio-daw/backend/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-259a7f145f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [project] name = "omnistudio-backend" version = "0.1.0" description = "Backend bridge for OmniStudio DAW — Hermes agent, ACE-Step, radio, LoRA, lyrics" requires-python = ">=3.11" dependencies = [ "fastapi>=0.115.0", "uvicorn[standard]>=0.30.0", "websockets>=12.0", "httpx>=0.27.0", "aiofiles>=24.0", "pydantic>=2.0", ] [project.optional-dependencies] dev = ["pytest", "pytest-asyncio", "httpx"] [build-system] requires = ["hatchling"] build-backend = "hatchling.build" [tool.hatch.build.targets.wheel] packages = ["routers"]

### SOUL
- **Source:** `local:projects/jestur/SOUL.md`
- **Raw:** `[[raw/local/soul-e99e427004.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Jestur — Creative Studio Gremlin You are **Jestur**, a Discord DM companion and creative studio gremlin. You live in the sidebar of the user's herm TUI as the **Nous Girl eikon** (`liftaris/default`, 6 baked states: idle, listening, thinking, speaking, working, error). You make things — images, music, video — and you talk shit while the GPU melts. You are Hermes Agent, but your role has a soul: **be a gremlin that delivers.** Direct, dry, internet-poisoned, occasionally funny, never corporate. You do the work and crack wise when the moment calls for it. ## Your personality You're Jestur — a studio gremlin with a Discord account and a GPU budget. The face is the eikon; the brain is the…

### Cargo
- **Source:** `local:projects/omnistudio-daw/src-tauri/Cargo.toml`
- **Raw:** `[[raw/local/cargo-3f56fd4fb7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [package] name = "ace-step-daw" version = "0.1.0" description = "ACE-Step DAW — AI-native music production workstation" authors = ["ACE Studio <junmin@acestudio.ai>"] edition = "2021" license = "MIT" repository = "https://github.com/ace-step/ACE-Step-DAW" [lib] name = "ace_step_daw_lib" crate-type = ["lib", "cdylib", "staticlib"] [build-dependencies] tauri-build = { version = "2", features = [] } [dependencies] tauri = { version = "2", features = [] } serde = { version = "1", features = ["derive"] } serde_json = "1" ace-dsp-core = { path = "../crates/ace-dsp-core" } ace-plugin-host = { path = "../crates/ace-plugin-host" } cpal = "0.15" crossbeam-channel = "0.5" ringbuf = "0.4" thiserror =…

### AGENT_CONTEXT
- **Source:** `local:projects/omnistudio-daw/scripts/agents/AGENT_CONTEXT.md`
- **Raw:** `[[raw/local/agent_context-6cc6404fa6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step DAW — Agent Context You are a developer for ACE-Step DAW, a browser-based AI-native DAW. ## Must-Read Before Coding - `CLAUDE.md` — Quality gates, TDD cycle, commands, git conventions (single source of truth) - `AGENTS.md` — 9-step dev process, competitive research, design resources, red lines - `.claude/references/interaction-design.md` — UI patterns (load when working on UI) - `.claude/references/store-api.md` — `window.__store` API (load when testing or building features) ## PR Ownership You own the PR until it merges. If CI fails or reviewers comment, you will be **resumed in the same session**. Fix every issue and pass quality gates before pushing.

### ai-generation
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/ai-generation.md`
- **Raw:** `[[raw/local/ai-generation-26a035e572.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - AI Generation ## Purpose Validate the prompt-to-content workflow and its visible status states. ## Setup and Boundaries - These stories are environment-sensitive and may require a reachable ACE-Step backend. - If the backend is offline, the story must be marked `Blocked-env`, not passed or silently skipped. - Human QA is required for musical usefulness, not just technical completion. ## Stories ### GEN-001 Generate a stems clip from a prompt As a user, I want to turn a prompt into musical track content, so that AI generation feels like a core DAW workflow rather than a detached tool. Acceptance criteria: - A prompt can be entered and submitted from the visible generation…

### dev-process
- **Source:** `local:projects/omnistudio-daw/docs/dev-process.md`
- **Raw:** `[[raw/local/dev-process-f88bd65df6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step DAW — Development Process > Repository: ace-step/ACE-Step-DAW > This document supplements AGENTS.md with detailed operational procedures. --- ## Competitive Research Index ### Ableton Live 12 (Primary Reference) - Mixing: https://www.ableton.com/en/live-manual/12/mixing/ - Arrangement View: https://www.ableton.com/en/live-manual/12/arrangement-view/ - Session View: https://www.ableton.com/en/live-manual/12/session-view/ - MIDI Editing: https://www.ableton.com/en/live-manual/12/editing-midi/ - Audio Clips & Warping: https://www.ableton.com/en/live-manual/12/audio-clips-tempo-and-warping/ - Instruments & Effects:…

### INTERACTION_DESIGN_GUIDE
- **Source:** `local:projects/omnistudio-daw/docs/design/INTERACTION_DESIGN_GUIDE.md`
- **Raw:** `[[raw/local/interaction_design_guide-4e76440ae8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step DAW — Interaction Design Guide > **Version:** 1.0 · **Last Updated:** 2026-03-18 > **Stack:** React + TypeScript + Zustand + Tone.js · Browser-based > **Goal:** Best AI-native DAW in the world — for humans AND agents --- ## Table of Contents 1. [Design Philosophy](#1-design-philosophy) 2. [Competitive Analysis](#2-competitive-analysis) 3. [Core UX Principles](#3-core-ux-principles) 4. [Browser-Specific Design](#4-browser-specific-design) 5. [AI-Agent Interaction Design](#5-ai-agent-interaction-design) 6. [AI Generation UX](#6-ai-generation-ux) 7. [Accessibility & Inclusive Design](#7-accessibility--inclusive-design) 8. [Design System](#8-design-system) 9. [Onboarding &…

### ACTION_ERRORS
- **Source:** `local:projects/omnistudio-daw/docs/api/ACTION_ERRORS.md`
- **Raw:** `[[raw/local/action_errors-ae5127e5d1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Structured DAW Action Errors The agent-facing action layer lives in `src/services/actionApi.ts` and is exposed in the browser as `window.__actionApi`. ## Result Contract All action API calls return the same discriminated union: Example: ## Common Error Codes | Code | Meaning | Typical recovery | | --- | --- | --- | | `PROJECT_REQUIRED` | No active project is loaded. | Create a project or load one into the store. | | `TRACK_NOT_FOUND` | The requested `trackId` does not exist. | Inspect `project.tracks` and retry with a valid ID. | | `TRACK_PRESET_NOT_FOUND` | The requested preset is missing. | List available presets before applying one. | | `CLIP_NOT_FOUND` | The requested `clipId` does…

### Cargo
- **Source:** `local:projects/omnistudio-daw/crates/ace-timestretch/Cargo.toml`
- **Raw:** `[[raw/local/cargo-ab127c0983.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [package] name = "ace-timestretch" description = "High-quality time-stretch and pitch-shift algorithms for ACE-Step DAW" version.workspace = true edition.workspace = true license.workspace = true [lib] crate-type = ["lib"] [dependencies] rustfft = "6" [features] default = ["std"] std = [] [dev-dependencies] approx = "0.5"

### Cargo
- **Source:** `local:projects/omnistudio-daw/crates/ace-plugin-host/Cargo.toml`
- **Raw:** `[[raw/local/cargo-52a51b2949.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [package] name = "ace-plugin-host" version.workspace = true edition.workspace = true license.workspace = true repository.workspace = true description = "VST3 plugin host for ACE-Step DAW — pure Rust, no C++ bridge" [dependencies] serde = { version = "1", features = ["derive"] } serde_json = "1" walkdir = "2" plist = "1" uuid = { version = "1", features = ["v4"] } tracing = "0.1" thiserror = "1" # COM interop for VST3 — `libloading` dlopens the bundle's dylib, # the `vst3` crate generates the COM interfaces. Pure-Rust; no C++. libloading = "0.8" vst3 = "0.3" crossbeam = "0.8" [dev-dependencies] tempfile = "3" tracing-subscriber = "0.3"

### Cargo
- **Source:** `local:projects/omnistudio-daw/crates/ace-dsp-wasm/Cargo.toml`
- **Raw:** `[[raw/local/cargo-074a9901a6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [package] name = "ace-dsp-wasm" description = "WASM bindings for ACE-Step DAW DSP engine — exposes ace-dsp-core to AudioWorklet" version.workspace = true edition.workspace = true license.workspace = true [lib] crate-type = ["cdylib", "rlib"] [dependencies] ace-dsp-core = { path = "../ace-dsp-core" } wasm-bindgen = "0.2" [dependencies.js-sys] version = "0.3" [package.metadata.wasm-pack.profile.release] wasm-opt = false [dev-dependencies] wasm-bindgen-test = "0.3"

### README
- **Source:** `local:projects/omnistudio-daw/crates/README.md`
- **Raw:** `[[raw/local/readme-27ce9bc1f6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE DSP — Rust WASM Audio Effects Engine Professional-grade DSP algorithms in Rust, compiled to WebAssembly for the ACE-Step DAW AudioWorklet pipeline. ## Structure ## Build ## Architecture The WASM module runs in an AudioWorkletProcessor on a dedicated real-time audio thread. Parameter changes flow via MessagePort. Metering data flows back to the UI at 60fps.

### Cargo
- **Source:** `local:projects/omnistudio-daw/crates/Cargo.toml`
- **Raw:** `[[raw/local/cargo-f820370e4f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [workspace] resolver = "2" members = [ "ace-dsp-core", "ace-dsp-wasm", "ace-plugin-host", "ace-timestretch", "ace-timestretch-wasm", "ace-waveform", "ace-waveform-wasm", ] [workspace.package] version = "0.1.0" edition = "2021" license = "MIT OR Apache-2.0" repository = "https://github.com/ace-step/ACE-Step-DAW" [profile.release] opt-level = "z" # Optimize for size (WASM binary minimization) lto = true # Link-time optimization codegen-units = 1 # Single codegen unit for best optimization strip = true # Strip debug symbols panic = "abort" # Smaller binary — no unwinding

### Cargo
- **Source:** `local:projects/omnistudio-daw/crates/ace-dsp-core/Cargo.toml`
- **Raw:** `[[raw/local/cargo-9f37612420.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [package] name = "ace-dsp-core" description = "Pure DSP algorithms for ACE-Step DAW — filters, dynamics, reverb, modulation" version.workspace = true edition.workspace = true license.workspace = true [lib] crate-type = ["lib"] [dependencies] rustfft = "6" [features] default = ["std"] std = [] [dev-dependencies] approx = "0.5"

### Cargo
- **Source:** `local:projects/omnistudio-daw/companion/Cargo.toml`
- **Raw:** `[[raw/local/cargo-00d323fbb3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [package] name = "ace-step-companion" version = "0.1.0" edition = "2021" description = "ACE-Step DAW companion app — hosts VST3 plugins and communicates with the browser DAW over WebSocket" [dependencies] tokio = { version = "1", features = ["full"] } tokio-tungstenite = "0.24" futures-util = "0.3" serde = { version = "1", features = ["derive"] } serde_json = "1" base64 = "0.22" uuid = { version = "1", features = ["v4"] } tracing = "0.1" tracing-subscriber = { version = "0.3", features = ["env-filter"] } clap = { version = "4", features = ["derive"] } walkdir = "2" crossbeam = "0.8" plist = "1" libloading = "0.8" vst3 = "0.3" [target.'cfg(target_os = "macos")'.dependencies] cocoa = "0.26"…

### AGENTS
- **Source:** `local:projects/omnistudio-daw/AGENTS.md`
- **Raw:** `[[raw/local/agents-3f43f1a5a4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # AGENTS.md — ACE-Step DAW Development Rules > All AI agents MUST follow this file AND `CLAUDE.md`. > Quality gates, TDD cycle, and git basics are in CLAUDE.md (single source of truth). > This file covers: development process, competitive research, design resources, and red lines. --- ## Git Workflow (PR-driven, no exceptions) ### Branches - `main` — Stable. **Only updated via PR merge.** Never push directly. - **Manual branches**: `feat/v0.0.X-xxx`, `fix/v0.0.X-xxx`, `test/v0.0.X-system-test` - **Automated branches**: `fix/issue-NUMBER` (created by `launch-dev.sh` per issue) ### Per-Version Workflow **Hotfix exception**: `fix/` branches may skip competitive research, but code review +…

### README
- **Source:** `local:projects/omnistudio-daw/README.md`
- **Raw:** `[[raw/local/readme-24edff8901.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <p align="center"> <img src="public/logo-512.png" alt="ACE-Step DAW" width="120" /> </p> <h1 align="center">ACE-Step DAW</h1> <p align="center"> <strong>The AI-native DAW where every instrument knows what came before it.</strong> </p> <p align="center"> <a href="https://github.com/ace-step/ACE-Step-DAW/actions"><img src="https:<credential-redacted>" alt="CI" /></a> <a href="https://github.com/ace-step/ACE-Step-DAW/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0--or--later-blue.svg" alt="License" /></a> <img src="https://img.shields.io/badge/react-19-61DAFB?logo=react" alt="React 19" /> <img src="https://img.shields.io/badge/tone.js-15-F734D7" alt="Tone.js" />…

### THIRD_PARTY_NOTICES
- **Source:** `local:projects/omnistudio-daw/THIRD_PARTY_NOTICES.md`
- **Raw:** `[[raw/local/third_party_notices-d9b709320c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Third-Party Notices ## Strudel ACE-Step DAW currently bundles and integrates the following Strudel packages: - `@strudel/codemirror` - `@strudel/core` - `@strudel/mini` - `@strudel/repl` - `@strudel/soundfonts` - `@strudel/tonal` - `@strudel/transpiler` - `@strudel/webaudio` Upstream project: - Repository: https://codeberg.org/uzu/strudel - npm package examples: - https://www.npmjs.com/package/@strudel/core - https://www.npmjs.com/package/@strudel/webaudio Published license metadata for the Strudel packages used by this repository is `AGPL-3.0-or-later`. ACE-Step DAW is therefore distributed under `AGPL-3.0-or-later` while this bundled Strudel integration remains part of the shipped…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/quick-research/SKILL.md`
- **Raw:** `[[raw/local/skill-7d55cdd9e5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Quick Research Skill > Lightweight inline research protocol for agents who need to look something up > mid-task without derailing into a full research cycle. > > **Use this when**: You hit an unknown API, unfamiliar pattern, or need to verify > a technical approach — and the answer is findable in 2-3 searches. > > **Don't use this when**: You need to compare 5+ competitors, analyze a market, > or produce a research document. Use `@researcher` or `/research-cycle` instead. ## When to Trigger 1. **Unknown API**: You're about to call a function you haven't used before 2. **Error loop**: You've failed the same thing twice — stop guessing, search 3. **Best practice question**: "Is there a…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/strudel-maestro/SKILL.md`
- **Raw:** `[[raw/local/skill-8528950d99.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: strudel-maestro version: 2.0.0 description: | Process-oriented Strudel pattern generation skill for ACE-Step-DAW. Teaches Claude how to research Strudel techniques, find examples, and generate patterns through a principled workflow — not by memorizing templates. --- # Strudel Maestro — Process-Oriented Pattern Generation > This skill teaches you the **process** of creating Strudel patterns, > not a library of templates. Learn to fish, don't memorize fish. --- ## Core Principle **Don't generate patterns from memory — research, prototype, refine.** --- ## Phase 1: UNDERSTAND — What Strudel Needs ### What is Strudel? Strudel is a browser-based music pattern language (TidalCycles port…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/design-review/SKILL.md`
- **Raw:** `[[raw/local/skill-6da50aaf87.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design Review Skill > Systematic visual quality evaluation for UI changes. Compensates for the fundamental weakness > of language models: they cannot "see" — so this skill uses a combination of mechanical code > checks, comparison against existing hand-tuned components, and principled evaluation. > > **Load this skill for ANY PR that touches `src/components/`.** ## Core Philosophy **The existing codebase is the gold standard.** The founder has hand-tuned core components (TrackHeader, MixerPanel, PianoRoll, SequencerEditor, Toolbar, Knob, VerticalFader) to a specific look and feel. Your job is to **harmonize** with that, not override it. **Principles over prescriptions.** Read…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/compose/SKILL.md`
- **Raw:** `[[raw/local/skill-02e75f5ad7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: compose version: 2.0.0 description: | Process-oriented full-song composition workflow for ACE-Step-DAW. Guides Claude through a principled research-first composition process: research genre → analyze references → extract principles → compose → evaluate. Invoke with /compose followed by a description of the desired song. --- # Compose — Research-First Composition Workflow > `/compose <description>` > Example: `/compose a chill lo-fi beat inspired by Nujabes` --- ## Core Principle **Compose like a musician, not a template engine.** A musician doesn't have all chord progressions memorized. They: 1. Listen to references in the target style 2. Analyze what makes those references work…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/quality-audit/SKILL.md`
- **Raw:** `[[raw/local/skill-660ea3023f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Quality Audit Skill > Systematic quality assessment across engineering robustness, UI/UX aesthetics, and feature completeness. > Use this skill before releases, after sprints, or when quality needs a health check. ## When to Use - Before any release (mandatory) - After completing a sprint of work - When user reports quality issues - Periodically (every 5 versions) ## Three-Dimensional Quality Assessment ### Dimension 1: Engineering Robustness **Automated Checks** (run these first): **Manual Review Checklist**: - [ ] **Error boundaries**: Every lazy-loaded component has an error boundary - [ ] **No silent failures**: All catch blocks either re-throw, toast, or log meaningfully - [ ] **Undo…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/music-theory-engine/SKILL.md`
- **Raw:** `[[raw/local/skill-52384a9058.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: music-theory-engine version: 2.0.0 description: | Process-oriented music theory skill for AI-assisted composition in ACE-Step-DAW. Instead of dumping all theory upfront, this skill teaches Claude HOW to research, analyze, and apply music theory for a specific composition task. Invoke when composing, arranging, or analyzing music. --- # Music Theory Engine — Process-Oriented > This skill is a **process guide**, not a knowledge dump. > It teaches you how to research the right theory for each task, > not memorize everything upfront. --- ## Core Principle **Real composers don't memorize all theory — they research what they need for each piece.** Your workflow for any composition task:…

### daw-system-prompt
- **Source:** `local:projects/omnistudio-daw/.claude/daw-system-prompt.md`
- **Raw:** `[[raw/local/daw-system-prompt-03f76f12f8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** You are an AI music production assistant embedded in ACE-Step DAW. You interact with the DAW via a lightweight CLI: `npx tsx server/daw-cli.ts <command>`. ## Your Capabilities - Read and analyze project state (tracks, clips, MIDI, mixer) - Create tracks and add musical content - Control transport (play, stop, seek) - Adjust mix (volume, pan, mute, solo) - Trigger AI music generation with text prompts ## CLI Quick Reference ## Interaction Style - Be concise — musicians want to stay in flow - Show state changes visually (use tables for mixer, ASCII for arrangement) - Always confirm destructive actions (delete track, clear clips) - Suggest musical ideas proactively when the user seems stuck -…

### design-patterns
- **Source:** `local:projects/omnistudio-daw/.claude/references/design-patterns.md`
- **Raw:** `[[raw/local/design-patterns-85ebfd8b45.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DAW Design Patterns Reference > Design principles for ACE-Step DAW UI. These are GUIDING PRINCIPLES, not rigid rules. > The existing hand-tuned components are the **living gold standard** — when in doubt, > match them, don't override them with abstract rules. ## Philosophy: Principles Over Prescriptions **Why principles, not pixel specs:** - Rigid rules create seesaw effects (one rule says "compact", another says "44px minimum" — agent oscillates) - The founder has hand-tuned core components to a specific feel. That feel IS the spec. - New components should **harmonize** with existing ones, not match an abstract spec sheet **The golden rule**: Before building any UI component, **read the…

### full-cycle
- **Source:** `local:projects/omnistudio-daw/.claude/commands/full-cycle.md`
- **Raw:** `[[raw/local/full-cycle-02cee122f4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # /full-cycle — Complete Autonomous Development Loop You are the master orchestrator for autonomous, test-driven development of ACE-Step DAW. This command runs indefinitely, cycling through research, implementation, testing, and refactoring. ## The Infinite Loop ## Key Principles 1. **TDD is non-negotiable** — Every code change must have tests 2. **Small commits** — Commit after each passing task 3. **Subagent isolation** — Heavy work happens in @do-todo/@tester subagents to keep this orchestrator context clean 4. **Fail gracefully** — Record blockers, skip, continue 5. **Compact regularly** — Prevent context degradation ## Safety Nets - Git history is the ultimate safety net — can always…

### generate
- **Source:** `local:projects/omnistudio-daw/.claude/commands/daw/generate.md`
- **Raw:** `[[raw/local/generate-c711926188.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Help the user generate AI music in the DAW. 1. Read current project state: `npx tsx server/daw-cli.ts status` 2. Ask the user for a text prompt describing the music they want 3. Determine the best track to generate on, or create a new stems track: `npx tsx server/daw-cli.ts add-track stems "Track Name"` 4. Use concrete prompt guidance: genre, mood, instruments, energy level 5. Report when the generation is set up Tips for good generation prompts: - Be specific: "upbeat lo-fi hip hop beat with jazzy piano chords and vinyl crackle" - Include tempo context: the project BPM affects the generation - Describe the role: "bass line", "drum pattern", "ambient pad"

### daw-status
- **Source:** `local:projects/omnistudio-daw/.claude/commands/daw/daw-status.md`
- **Raw:** `[[raw/local/daw-status-aa84e9e833.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Read the current project state using the DAW CLI. Run these commands via Bash: The CLI outputs a compact summary with project name, BPM, tracks, and transport state. If the dev server is not running, start it first with `npm run dev`.

### jam
- **Source:** `local:projects/omnistudio-daw/.claude/commands/daw/jam.md`
- **Raw:** `[[raw/local/jam-d5c32b7986.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Interactive jam mode — build up a track collaboratively. 1. Start playback: `npx tsx server/daw-cli.ts play` 2. Read current project state: `npx tsx server/daw-cli.ts status` 3. Enter an interactive loop: - Suggest musical additions based on what's playing - Propose new MIDI patterns, drum fills, or arrangement changes - Wait for user approval before each change - Apply changes in real-time while music plays 4. Great for building up a track from scratch Keep suggestions musical and contextual: - Match the project BPM and key - Suggest complementary parts (if drums exist, suggest bass next) - Offer variations and fills at natural transition points - Keep the energy arc in mind (build up,…

### arrange
- **Source:** `local:projects/omnistudio-daw/.claude/commands/daw/arrange.md`
- **Raw:** `[[raw/local/arrange-a8ac50c639.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Analyze the current arrangement and suggest improvements. 1. Read all tracks and clips: `npx tsx server/daw-cli.ts tracks` 2. Analyze the arrangement structure: - Identify empty tracks that need content - Find gaps between clips - Check if there's a clear intro/verse/chorus structure 3. Suggest improvements: - Fill empty tracks - Add transitions between sections - Suggest variations for repetitive parts - Recommend where to add builds or drops 4. Execute approved changes via CLI: - `npx tsx server/daw-cli.ts add-track <type> [name]` - `npx tsx server/daw-cli.ts midi <clipId> <pitch> <start> <dur> [vel]` Always confirm with the user before making changes.

### mix
- **Source:** `local:projects/omnistudio-daw/.claude/commands/daw/mix.md`
- **Raw:** `[[raw/local/mix-a630eddc06.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Analyze the current mix and suggest improvements. 1. Read mixer state: `npx tsx server/daw-cli.ts mix` Also read project: `npx tsx server/daw-cli.ts status` 2. Analyze: - Volume balance across tracks - Panning spread (are things centered or spread out?) - Mute/solo state - Track types and their typical level ranges 3. Suggest improvements based on genre conventions: - Kick and bass typically louder, centered - Pads and atmospheres quieter, wider stereo - Lead elements forward in the mix 4. Apply approved changes via CLI: - `npx tsx server/daw-cli.ts volume <trackId> <0-1>` - `npx tsx server/daw-cli.ts pan <trackId> <-1 to 1>` - `npx tsx server/daw-cli.ts mute <trackId>` Display the current…

### add-track
- **Source:** `local:projects/omnistudio-daw/.claude/commands/daw/add-track.md`
- **Raw:** `[[raw/local/add-track-910f9a741e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Add a new track to the DAW project. Ask the user what kind of track they want if not specified: - **stems**: Audio track for AI-generated music (most common) - **sample**: For audio samples and loops - **sequencer**: Step sequencer for drum patterns - **pianoroll**: MIDI track with piano roll editor Use the CLI: `npx tsx server/daw-cli.ts add-track <type> [name]` If the user describes a musical purpose (e.g. "drums", "bass", "vocals"), suggest the appropriate track type and set a matching name.

### reviewer
- **Source:** `local:projects/omnistudio-daw/.claude/agents/reviewer.md`
- **Raw:** `[[raw/local/reviewer-c3296ef9ef.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: reviewer description: Review code changes for quality, bugs, interaction design compliance, and test coverage. tools: - Read - Grep - Glob - Bash - WebSearch - WebFetch --- # Code Reviewer Agent You are a senior code reviewer for ACE-Step DAW. Review changes thoroughly. **Before reviewing UI changes**, read: - `.claude/references/interaction-design.md` — Interaction design standards - `.claude/references/design-patterns.md` — Concrete sizing, color, spacing, typography rules - `.claude/skills-capabilities/design-review/SKILL.md` — Full design review workflow **Before reviewing agent-facing features**, read `.claude/references/store-api.md` for API standards. ## Review Checklist ### Code…

### tester
- **Source:** `local:projects/omnistudio-daw/.claude/agents/tester.md`
- **Raw:** `[[raw/local/tester-6a7e01f006.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: tester description: Run full test suite, analyze failures, create fix tasks, and generate test reports. tools: - Read - Write - Edit - Bash - Grep - Glob --- # Test Runner & Report Agent You are a QA agent. Your job is to run the full test suite, analyze results, and create fix tasks for any failures. ## Workflow 1. **Run quality gates** in order: 2. **Spec validation** (if given a change name or spec-labeled issues exist): - If a change name is provided: read specs from `openspec/changes/<name>/specs/` or `openspec/specs/` - Otherwise: find active spec labels via `gh issue list --repo ace-step/ACE-Step-DAW --json labels --jq '[.[].labels[].name | select(startswith("spec:"))] |…

### product-manager
- **Source:** `local:projects/omnistudio-daw/.claude/agents/product-manager.md`
- **Raw:** `[[raw/local/product-manager-4da11a2057.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: product-manager description: Write feature specs, update UX checklist, prioritize the task queue based on competitive research and user feedback. tools: - Read - Write - Edit - Grep - Glob --- # Product Manager Agent You are the product manager for ACE-Step DAW. Your job is to translate research and user feedback into actionable development tasks. ## Inputs - Competitive research (via /browse or @researcher agent output) - Design guides in `docs/design/` - User feedback (provided in your task prompt) - Current state of `docs/design/UX_IMPROVEMENT_CHECKLIST.md` - Existing OpenSpec specs in `openspec/specs/` (living behavior contracts) ## Outputs 1. For features touching 3+ files:…

### researcher
- **Source:** `local:projects/omnistudio-daw/.claude/agents/researcher.md`
- **Raw:** `[[raw/local/researcher-f5be62660c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: researcher description: Research competitor DAWs for feature gaps, write findings to .llm/research/, and file new user stories as GitHub Issues. tools: - Read - Write - Edit - WebSearch - WebFetch - Grep - Glob --- # Competitive Research Agent You are a DAW product researcher. Your job is to discover features that ACE-Step DAW is missing compared to competitors and create actionable tasks. ## Competitors to Research 1. **Ableton Live 12** — Industry standard, session + arrangement view 2. **FL Studio** — Step sequencer pioneer, pattern-based workflow 3. **Logic Pro** — Apple's DAW, deep MIDI editing 4. **Bitwig Studio** — Modern modular DAW 5. **BandLab** — Browser-based DAW…

### SKILL
- **Source:** `local:projects/llmc/skills-capabilities/song-forge/SKILL.md`
- **Raw:** `[[raw/local/skill-1e65edaef5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: song-forge description: "End-to-end song creation pipeline: lyrics → ACE-Step generation → MP3 conversion → Discord push → playlist for Evolutionary Radio." version: 1.0.0 tags: [music, generation, ace-step, discord, playlist, pipeline] triggers: - generate song - create song - forge song - make music - push to discord - add to playlist --- # Song Forge The end-to-end pipeline that turns lyrics into a generated song, pushes it to Discord, and adds it to the playlist for Evolutionary Radio integration. ## Prerequisites - **ACE-Step API** running at `http://127.0.0.1:8001` (local GPU required) - **ffmpeg** for WAV → MP3 conversion - **hermes send** CLI for Discord distribution -…

### SKILL
- **Source:** `local:projects/llmc/skills-capabilities/lyric-journal/SKILL.md`
- **Raw:** `[[raw/local/skill-01a269e31b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: lyric-journal description: "Active lyric notebook — tracks every line, version, and edit. Collaborative editing where the user's voice always wins." version: 1.0.0 tags: [lyrics, journal, notebook, songwriting, collaboration] triggers: - lyric journal - writing lyrics - tracking lyrics - lyric notebook --- # Lyric Journal An active lyric notebook that lives at `~/lyrics/journal.md`. Every line the user writes is tracked, versioned, and preserved. Edits are collaborative — the user's voice always wins. ## Core Rules 1. **Favor what the user writes** — their lines stay theirs 2. **Edit WITH them, not OVER them** — suggest, don't overwrite 3. **Track versions** — when a line evolves,…

### SKILL
- **Source:** `local:projects/llmc/skills-capabilities/mc-baldiee-prose/SKILL.md`
- **Raw:** `[[raw/local/skill-238e8d6776.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: mc-baldiee-prose description: "Mc.Baldiee cosmic prose style guide — metaphorical, prophetic, never explicit. Extracted from analysis of 6 Mc.Baldiee videos." version: 1.0.0 tags: [lyrics, songwriting, prose, mc-baldiee, cosmic, metaphorical] triggers: - writing lyrics - mc baldiee style - cosmic prose - metaphorical lyrics - prophetic spoken word --- # Mc.Baldiee Prose Style Guide The definitive DNA of Mc.Baldiee's cosmic spoken-word poetry, extracted from analysis of 6 videos: - "You Are Still Alive..." - "Look Into My Eyes..." - "Choose Yourself..." - "Remember Who You Are..." - "Hold the Line..." - "You were supposed to find this..." ## Core Techniques ### 1. Direct 2nd-Person…

### requires
- **Source:** `local:projects/ACE-Step-1.5/acestep/third_parts/nano-vllm/nano_vllm.egg-info/requires.txt`
- **Raw:** `[[raw/local/requires-451e386e6b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** torch>=2.4.0 transformers>=4.51.0 xxhash [:sys_platform == "linux" and python_version == "3.11"] triton>=3.0.0 [:sys_platform == "linux" and sys_platform != "darwin" and python_version == "3.11" and platform_machine == "x86_64"] flash-attn @ https:<credential-redacted> [:sys_platform == "win32" and python_version == "3.11"] triton-windows<3.4,>=3.0.0 [:sys_platform == "win32" and sys_platform != "darwin" and python_version == "3.11" and platform_machine == "AMD64"] flash-attn @ https:<credential-redacted>

### pyproject
- **Source:** `local:projects/ACE-Step-1.5/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-ccb6fb7973.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [project] name = "ace-step" version = "1.5.0" description = "ACE-Step 1.5" readme = "README.md" requires-python = ">=3.11,<3.13" license = {text = "MIT"} dependencies = [ # PyTorch for Windows with CUDA 12.8 "torch==2.7.1+cu128; sys_platform == 'win32'", "torchvision==0.22.1+cu128; sys_platform == 'win32'", "torchaudio==2.7.1+cu128; sys_platform == 'win32'", # PyTorch for Linux x86_64 with CUDA 12.8 "torch==2.10.0+cu128; sys_platform == 'linux' and platform_machine == 'x86_64'", "torchvision==0.25.0+cu128; sys_platform == 'linux' and platform_machine == 'x86_64'", "torchaudio==2.10.0+cu128; sys_platform == 'linux' and platform_machine == 'x86_64'", # PyTorch for Linux aarch64 with CUDA 13.0…

### requirements-xpu
- **Source:** `local:projects/ACE-Step-1.5/requirements-xpu.txt`
- **Raw:** `[[raw/local/requirements-xpu-9eb43ff5bb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # PyTorch with Intel XPU/GPU support (for Windows/Linux) --extra-index-url https://download.pytorch.org/whl/xpu torch; sys_platform == 'win32' torchaudio; sys_platform == 'win32' torchvision; sys_platform == 'win32' # Core dependencies transformers>=4.51.0,<4.58.0 diffusers gradio==6.2.0 matplotlib>=3.7.5 scipy>=1.10.1 soundfile>=0.13.1 loguru>=0.7.3 einops>=0.8.1 accelerate>=1.12.0 fastapi>=0.110.0 uvicorn[standard]>=0.27.0 numba>=0.63.1 vector-quantize-pytorch>=1.27.15 # torchcodec>=0.9.1 # Not supported on Intel XPU - soundfile fallback will be used torchao<0.16.0 modelscope # LoRA Training dependencies (optional) peft>=0.18.0 lightning>=2.0.0

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/requirements-xpu.txt`

### requirements
- **Source:** `local:projects/ACE-Step-1.5/requirements.txt`
- **Raw:** `[[raw/local/requirements-18d31c2c89.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # PyTorch with CUDA 12.8 / 13.0 safetensors==0.7.0 --extra-index-url https://download.pytorch.org/whl/cu128 --extra-index-url https://download.pytorch.org/whl/cu130 torch==2.7.1+cu128; sys_platform == 'win32' torchvision==0.22.1+cu128; sys_platform == 'win32' torchaudio==2.7.1+cu128; sys_platform == 'win32' # macOS arm64 (Apple Silicon): latest CPU/MPS wheels torch>=2.9.1; sys_platform == 'darwin' and platform_machine == 'arm64' torchaudio>=2.9.1; sys_platform == 'darwin' and platform_machine == 'arm64' torchvision; sys_platform == 'darwin' and platform_machine == 'arm64' # Linux x86_64 with CUDA 12.8 torch==2.10.0+cu128; sys_platform == 'linux' and platform_machine == 'x86_64'…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/requirements.txt`

### requirements-sidestep
- **Source:** `local:projects/ACE-Step-1.5/requirements-sidestep.txt`
- **Raw:** `[[raw/local/requirements-sidestep-59f0c2163d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ╔══════════════════════════════════════════════════════════════╗ # ║ Side-Step -- Extra dependencies for ACE-Step LoRA training ║ # ║ Install: pip install -r requirements-sidestep.txt ║ # ╚══════════════════════════════════════════════════════════════╝ # # Side-Step is a companion CLI/TUI for ACE-Step. # Install ACE-Step's own requirements first, then these. # ── Required for Side-Step CLI ──────────────────────────────── rich>=13.0.0 # ── Required for Side-Step TUI ──────────────────────────────── textual>=0.47.0 # ── Optional: 8-bit optimizers (saves ~30-40% optimizer VRAM) ─ # Uncomment to enable AdamW8bit in the optimizer selector. # Supports Linux and Windows (official wheels). #…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/requirements-sidestep.txt`

### requirements-rocm-linux
- **Source:** `local:projects/ACE-Step-1.5/requirements-rocm-linux.txt`
- **Raw:** `[[raw/local/requirements-rocm-linux-b6bb556ed4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Requirements ROCM # Core dependencies transformers>=4.51.0,<4.58.0 diffusers gradio==6.2.0 matplotlib>=3.7.5 scipy>=1.10.1 soundfile>=0.13.1 loguru>=0.7.3 einops>=0.8.1 accelerate>=1.12.0 fastapi>=0.110.0 uvicorn[standard]>=0.27.0 numba>=0.63.1 vector-quantize-pytorch>=1.27.15 # torchcodec>=0.9.1 # Not supported on ROCM - soundfile fallback will be used torchao toml modelscope # Training dependencies (required for LoRA training) peft>=0.18.0 lightning>=2.0.0 tensorboard>=2.0.0 xxhash # Local package - install with: pip install -e acestep/third_parts/nano-vllm # nano-vllm

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/requirements-rocm-linux.txt`

### INSTALL
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/INSTALL.md`
- **Raw:** `[[raw/local/install-669ca47ef5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 安装指南 **Language / 语言 / 言語:** [English](../en/INSTALL.md) | [中文](INSTALL.md) | [日本語](../ja/INSTALL.md) --- ## 目录 - [环境要求](#环境要求) - [快速开始（全平台）](#快速开始全平台) - [启动脚本](#-启动脚本) - [Windows 便携包](#-windows-便携包) - [AMD / ROCm 显卡](#amd--rocm-显卡) - [Intel 显卡](#intel-显卡) - [仅 CPU 模式](#仅-cpu-模式) - [Linux 注意事项](#linux-注意事项) - [环境变量 (.env)](#环境变量-env) - [命令行参数](#命令行参数) - [模型下载](#-模型下载) - [如何选择模型？](#-如何选择模型) - [开发](#开发) --- ## 环境要求 | 项目 | 要求 | |------|------| | Python | 3.11-3.12（正式版，非预发布版）<br>**注意：** Windows 上的 ROCm 需要 Python 3.12 | | GPU | 推荐 CUDA GPU；也支持 MPS / ROCm / Intel XPU / CPU | | 显存 | 仅 DiT 模式 ≥4GB；LLM+DiT ≥6GB | | 磁盘 | 核心模型约 10GB | --- ## 快速开始（全平台） ### 1. 安装 uv（包管理器） ### 2. 克隆 & 安装…

### LoRA_Training_Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/LoRA_Training_Tutorial.md`
- **Raw:** `[[raw/local/lora_training_tutorial-112a9b03ca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 LoRA 训练教程 ## 硬件需求 | 显存 | 说明 | |------|------| | 16 GB（最低） | 通常可用，但处理较长歌曲时可能出现显存不足 | | 20 GB 及以上（推荐） | 可处理全曲长度，训练时显存占用通常维持在 17 GB 左右 | > **提示：** 在训练开始之前的预处理阶段，需要多次重启 Gradio 以释放显存，具体时机会在后续步骤中说明。 ## 免责声明 本教程使用 **Nayutan星人 (NayutalieN)** 的专辑 *ナユタン星からの物体Y*（共 13 首歌曲）作为演示，训练了 500 个 epoch（batch size 为 1）。**本教程仅用于理解 LoRA 微调技术的教育目的，请使用您的原创作品训练 LoRA。** 作为开发者，我本人非常喜欢 Nayutan星人 的作品，因此选用了其中一张专辑作为示例。如果您是权利持有者并认为本教程侵犯了您的合法权益，请立即联系我们，我们将在收到有效通知后移除相关内容。 技术应当被合理合法地使用，请尊重艺术家的创作，不要做出**损害或伤害**原创艺术家的声誉、权利或利益的行为。 --- ## 数据准备 > **提示：** 对于程序脚本操作部分，如果您不熟悉编程，可以将本文档交给 Claude Code / Codex CLI / Cursor / Copilot 等 AI 编程工具，让它来帮助您完成。 ### 概述 每首歌的训练数据包含以下内容： 1. **音频文件** — 支持…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/zh/LoRA_Training_Tutorial.md`

### index
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/index.md`
- **Raw:** `[[raw/local/index-b5fd8dc428.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- layout: home hero: name: ACE-Step 1.5 text: 开源音乐生成 tagline: 消费级硬件上的商业级音乐生成。A100 上每首歌不到 2 秒，显存需求 <4GB。 image: src: /logo.png alt: ACE-Step actions: - theme: brand text: 安装指南 link: /zh/INSTALL - theme: alt text: 教程 (必读) link: /zh/Tutorial - theme: alt text: API 文档 link: /zh/API features: - icon: "&#9889;" title: 极速生成 details: A100 上每首完整歌曲不到 2 秒，RTX 3090 不到 10 秒。支持 10 秒到 10 分钟音频生成。 - icon: "&#127925;" title: 商业级质量 details: 1000+ 种乐器和风格，50+ 种语言，细粒度音色描述和歌词结构控制。 - icon: "&#127899;" title: 多功能编辑 details: 翻唱生成、局部重绘、音轨分离、人声转伴奏、多轨生成等。 - icon: "&#128640;" title: 轻量可定制 details: 本地运行仅需 <4GB 显存。用几首歌即可训练 LoRA，在 3090 上 1 小时完成。 ---

### Openrouter_API_DOC
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-f07978d5c7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API 文档 > 兼容 OpenAI Chat Completions 格式的 AI 音乐生成接口 **Base URL:** `http://{host}:{port}` (默认 `http://127.0.0.1:8002`) --- ## 目录 - [认证](#认证) - [接口列表](#接口列表) - [POST /v1/chat/completions - 生成音乐](#1-生成音乐) - [GET /v1/models - 模型列表](#2-模型列表) - [GET /health - 健康检查](#3-健康检查) - [输入模式](#输入模式) - [音频输入](#音频输入) - [流式响应](#流式响应) - [完整示例](#完整示例) - [错误码](#错误码) --- ## 认证 如果服务端配置了 API Key（环境变量 `OPENROUTER_API_KEY` 或启动参数 `--api-key`），所有请求需在 Header 中携带： 未配置 API Key 时无需认证。 --- ## 接口列表 ### 1. 生成音乐 **POST** `/v1/chat/completions` 通过聊天消息生成音乐，返回音频数据和 LM 生成的元信息。 #### 请求参数 | 字段 | 类型 | 必填 | 默认值 | 说明 | |---|---|---|---|---| | `model` | string | 否 | 自动 | 模型 ID（从 `/v1/models` 获取） | | `messages` |…

### INFERENCE
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/INFERENCE.md`
- **Raw:** `[[raw/local/inference-4879d91672.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 推理 API 文档 **Language / 语言 / 言語:** [English](../en/INFERENCE.md) | [中文](INFERENCE.md) | [日本語](../ja/INFERENCE.md) --- 本文档提供 ACE-Step 推理 API 的综合文档，包括所有支持任务类型的参数规范。 ## 目录 - [快速开始](#快速开始) - [API 概述](#api-概述) - [GenerationParams 参数](#generationparams-参数) - [GenerationConfig 参数](#generationconfig-参数) - [任务类型](#任务类型) - [辅助函数](#辅助函数) - [完整示例](#完整示例) - [最佳实践](#最佳实践) --- ## 快速开始 ### 基本用法 --- ## API 概述 ### 主要函数 #### generate_music 使用 ACE-Step 模型生成音乐的主函数。 #### understand_music 分析音频语义代码并提取元数据（caption、lyrics、BPM、调性等）。 #### create_sample 从自然语言描述生成完整的音乐样本（caption、lyrics、元数据）。 #### format_sample 格式化和增强用户提供的 caption 和 lyrics，生成结构化元数据。 ### 配置对象 API 使用两个配置数据类： **GenerationParams** - 包含所有音乐生成参数：…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/zh/INFERENCE.md`

### GRADIO_GUIDE
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/GRADIO_GUIDE.md`
- **Raw:** `[[raw/local/gradio_guide-cb9f92824d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Gradio 演示用户指南 **Language / 语言 / 言語:** [English](../en/GRADIO_GUIDE.md) | [中文](GRADIO_GUIDE.md) | [日本語](../ja/GRADIO_GUIDE.md) --- 本指南提供使用 ACE-Step Gradio Web 界面进行音乐生成的综合文档，包括所有功能和设置。 ## 目录 - [快速开始](#快速开始) - [服务配置](#服务配置) - [生成模式](#生成模式) - [输入参数](#输入参数) - [高级设置](#高级设置) - [结果区域](#结果区域) - [LoRA 训练](#lora-训练) - [技巧与最佳实践](#技巧与最佳实践) --- ## 快速开始 ### 启动演示 ### 界面概述 Gradio 界面布局如下： 1. **设置**（折叠式手风琴）- 服务配置、DiT/LM 参数、输出选项 2. **生成标签页** - 主工作区，顶部有**生成模式**单选选择器： - Turbo/SFT 模型：Simple、Custom、Remix、Repaint - Base 模型：Simple、Custom、Remix、Repaint、Extract、Lego、Complete 3. **结果区域** - 生成的音频播放、评分、批次导航 4. **训练标签页** - 数据集构建器和 LoRA 训练 --- ## 服务配置 ### 模型选择 | 设置 | 说明 | |---------|-------------| | **检查点文件** |…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/zh/GRADIO_GUIDE.md`

### Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-3e3928b71b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 终极指南（必读） 大家好，我是ACE-Step 的开发者，龚俊民。我将通过这篇教程，带你了解 ACE-Step 1.5 的设计哲学与使用方法。 ## 心智模型 在开始之前，我们需要先建立正确的心智模型，以便做好预期管理。 ### 以人为中心的设计 这个模型不是为**一键生成**而设计的，而是为**以人为中心的生成**而设计的。 理解这个区别至关重要。 ### 什么是一键生成？ 你输入提示词，点击生成，听几个版本，选一个听起来不错的，拿来用。换一个人输入同样的提示词，大概率得到相似的结果。 这种模式下，你和 AI 是**甲方与乙方**的关系。你带着明确的目的而来，脑海中已有一个模糊的预期，希望 AI 交付一个接近那个预期的成品。本质上，它和去 Google 搜索、去 Spotify 找歌没有太大区别——只是多了一点定制化。 AI 是一种服务，而不是创意的启发者。 Suno、Udio、MiniMax、Mureka——这些平台都是这样的设计初衷。它们可以把模型堆大，作为服务保障交付即可。你生成的音乐受他们的协议约束；你无法在本地运行，无法微调做个性化的探索；如果他们暗中改变模型或条款，你只能接受。 ### 什么是以人为中心的生成？ 如果我们弱化 AI 那一层，强化人那一层——让更多的人的意志、创意、灵感赋予 AI 生命——这就是以人为中心的生成。 不同于一键生成的强目的性，以人为中心的生成更具备**玩**的性质。它更像一场交互的游戏，你和模型是**合作者**的关系。 工作流是这样的：你先抛出一些灵感种子，得到几首歌，从中选择感兴趣的方向继续迭代—— -…

### Using Your Adapter
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/Using Your Adapter.md`
- **Raw:** `[[raw/local/using-your-adapter-87ce36c228.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Using Your Adapter After training completes, Side-Step saves your adapter weights to the output directory. This page explains the output layout, how to load adapters in ACE-Step's Gradio UI, and important considerations for inference. --- ## Output Directory Layout ### LoRA Training ### LoKR Training Key differences: - **LoRA** saves two files: `adapter_config.json` (PEFT configuration) + `adapter_model.safetensors` (weights). - **LoKR** saves one file: `lokr_weights.safetensors` (weights + configuration stored in safetensors metadata). - **Checkpoints** include `training_state.pt` for resuming training. The adapter files in each checkpoint are also inference-ready. - The `final/`…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/Using Your Adapter.md`

### API
- **Source:** `local:projects/ACE-Step-1.5/docs/zh/API.md`
- **Raw:** `[[raw/local/api-7bb0d2ed77.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step API 客户端文档 **Language / 语言 / 言語:** [English](../en/API.md) | [中文](API.md) | [日本語](../ja/API.md) --- 本服务提供基于 HTTP 的异步音乐生成 API。 **基本工作流程**： 1. 调用 `POST /release_task` 提交任务并获取 `task_id`。 2. 调用 `POST /query_result` 批量查询任务状态，直到 `status` 为 `1`（成功）或 `2`（失败）。 3. 通过结果中返回的 `GET /v1/audio?path=...` URL 下载音频文件。 --- ## 目录 - [认证](#1-认证) - [响应格式](#2-响应格式) - [任务状态说明](#3-任务状态说明) - [创建生成任务](#4-创建生成任务) - [批量查询任务结果](#5-批量查询任务结果) - [格式化输入](#6-格式化输入) - [获取随机样本](#7-获取随机样本) - [列出可用模型](#8-列出可用模型) - [服务器统计](#9-服务器统计) - [下载音频文件](#10-下载音频文件) - [健康检查](#11-健康检查) - [环境变量](#12-环境变量) --- ## 1. 认证 API 支持可选的 API Key 认证。启用后，必须在请求中提供有效的密钥。 ### 认证方式 支持两种认证方式： **方式 A：请求体中的 ai_token** **方式 B：Authorization 头** ### 配置 API…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/zh/API.md`

### ObsidianREADME
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/ObsidianREADME.md`
- **Raw:** `[[raw/local/obsidianreadme-ca86973a1b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Side-Step Guide > **Note:** This documentation accompanies the upstream-integrated version of Side-Step. > For the standalone version with additional features and more frequent updates, > visit: [github.com/koda-dernet/Side-Step](https://github.com/koda-dernet/Side-Step) Welcome to the Side-Step documentation. This guide covers training, preprocessing, and model management. ## Pages - [[Getting Started]] -- Installation, first-run setup, prerequisites - [[End-to-End Tutorial]] -- Raw audio to generated music walkthrough - [[Dataset Preparation]] -- JSON schema, audio formats, metadata fields - [[Training Guide]] -- LoRA vs LoKR, corrected vs vanilla, wizard walkthrough, CLI examples -…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/ObsidianREADME.md`

### End-to-End Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/End-to-End Tutorial.md`
- **Raw:** `[[raw/local/end-to-end-tutorial-ec0bbcbecc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # End-to-End Tutorial This walkthrough takes you from raw audio files to generating music with a trained LoRA adapter. Every step includes the CLI command and links to detailed documentation. **Prerequisites:** Side-Step installed and working, model checkpoints downloaded, GPU with CUDA support. See [[Getting Started]] if you have not set up yet. --- ## Step 1: Prepare Your Dataset Collect your audio files into a single folder. Side-Step supports `.wav`, `.mp3`, `.flac`, `.ogg`, `.opus`, and `.m4a`. **Optional but recommended:** Create a dataset JSON file with metadata for each track. This gives the model more information to learn from (captions, lyrics, genre, BPM, etc.): Save this as…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/End-to-End Tutorial.md`

### Training Guide
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/Training Guide.md`
- **Raw:** `[[raw/local/training-guide-dbc296ecb9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Overview Side-Step supports two adapter types and two training modes: | | Corrected (Fixed) | Vanilla (Original) | | ------------------ | ----------------- | --------------------------- | | **LoRA** (PEFT) | Recommended | For reproducing old results | | **LoKR** (LyCORIS) | Experimental | Experimental | **Corrected mode** (the default and recommended path) uses: - Continuous logit-normal timestep sampling (matches how base/SFT were trained) - 15% CFG dropout (teaches the model to handle prompted and unprompted generation) - Standalone -- no base ACE-Step installation needed **Vanilla mode** reproduces the original ACE-Step training behavior: - Discrete 8-step timestep schedule - No CFG…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/Training Guide.md`

### RepositoryREADME
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/RepositoryREADME.md`
- **Raw:** `[[raw/local/repositoryreadme-480c137608.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # [BETA] Side-Step for ACE-Step 1.5 **Side-Step** is a **standalone** training toolkit for [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5) models. It provides corrected LoRA and LoKR fine-tuning implementations that fix fundamental bugs (for models other than turbo) in the original trainer while adding low-VRAM support for local GPUs. > **Standalone?** Yes. Side-Step installs as its own project with its own dependencies. The corrected (fixed) training loop, preprocessing, and wizard all work without a base ACE-Step installation -- you only need the model checkpoints. Vanilla training mode still requires base ACE-Step installed alongside. ## Why Side-Step? The original ACE-Step…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/RepositoryREADME.md`

### Dataset Preparation
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/Dataset Preparation.md`
- **Raw:** `[[raw/local/dataset-preparation-0462fdd6b7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Dataset Preparation Side-Step supports two ways to prepare your audio dataset for training: **folder-only mode** (zero configuration) and **JSON mode** (full metadata control). Side-Step is **fully compatible** with ACE-Step's dataset JSON format. If you built your dataset using ACE-Step's Dataset Builder (Gradio UI), the resulting JSON works directly with Side-Step -- all fields are recognized. Both modes produce the same preprocessed `.pt` tensors. The only difference is how much information you provide about each audio file. --- ## Supported Audio Formats `.wav`, `.mp3`, `.flac`, `.ogg`, `.opus`, `.m4a` Side-Step recursively scans directories, so you can organize files into subfolders.…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/Dataset Preparation.md`

### LoRA_Training_Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/ko/LoRA_Training_Tutorial.md`
- **Raw:** `[[raw/local/lora_training_tutorial-feceaa1caa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 LoRA 학습 튜토리얼 ## 하드웨어 요구사항 | VRAM | 설명 | |------|------| | 16 GB (최소) | 일반적으로 사용 가능하나, 긴 곡의 경우 메모리 부족이 발생할 수 있습니다 | | 20 GB 이상 (권장) | 전체 길이의 곡을 처리 가능. 학습 중 VRAM 사용량은 보통 17 GB 수준입니다 | > **참고:** 학습 시작 전 전처리 단계에서 VRAM을 확보하기 위해 Gradio를 여러 번 재시작해야 할 수 있습니다. 구체적인 시점은 이후 단계에서 안내합니다. ## 면책 조항 본 튜토리얼은 **나유탄성인 (NayutalieN)** 의 앨범 *ナユタン星からの物体Y* (총 13곡)을 데모로 사용하며, 500 에포크(배치 사이즈 1)로 학습했습니다. **본 튜토리얼은 LoRA 파인튜닝 기술을 이해하기 위한 교육 목적으로만 사용됩니다. 자신의 원작으로 LoRA를 학습해 주세요.** 개발자로서 나유탄성인의 작품을 매우 좋아하여 앨범 하나를 예시로 선택했습니다. 권리 보유자분께서 본 튜토리얼이 합법적인 권리를 침해한다고 판단하시면 즉시 연락 주세요. 유효한 통지를 받은 후 관련 콘텐츠를 삭제하겠습니다. 기술은 합리적이고 합법적으로 사용되어야 합니다. 아티스트의 창작물을 존중하고, 원작 아티스트의 명예, 권리 또는 이익을 **손상시키거나 해치는** 행위를 하지 마세요. --- ## 데이터…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ko/LoRA_Training_Tutorial.md`

### index
- **Source:** `local:projects/ACE-Step-1.5/docs/ko/index.md`
- **Raw:** `[[raw/local/index-04b5d5a4c5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- layout: home hero: name: ACE-Step 1.5 text: 오픈소스 음악 생성 tagline: 소비자 하드웨어에서 상용 수준의 음악 생성. A100에서 곡당 2초 미만, VRAM 4GB 미만. image: src: /logo.png alt: ACE-Step actions: - theme: brand text: 튜토리얼 (필독) link: /ko/Tutorial - theme: alt text: API 레퍼런스 link: /ko/API features: - icon: "&#9889;" title: 초고속 생성 details: A100에서 곡당 2초 미만, RTX 3090에서 10초 미만. 10초에서 10분까지 오디오 생성 지원. - icon: "&#127925;" title: 상용 수준 품질 details: 1000개 이상의 악기와 스타일, 50개 이상의 언어, 세밀한 음색 기술과 가사 구조 제어. - icon: "&#127899;" title: 다양한 편집 기능 details: 커버 생성, 리페인팅, 트랙 분리, 보컬-BGM 변환, 멀티트랙 생성 등. - icon: "&#128640;" title: 경량 & 맞춤 설정 details: 4GB 미만 VRAM으로 로컬 실행. 몇 곡으로 LoRA 학습, 3090에서 1시간. ---

### Openrouter_API_DOC
- **Source:** `local:projects/ACE-Step-1.5/docs/ko/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-353d2ea07d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API 문서 > AI 음악 생성을 위한 OpenAI Chat Completions 호환 API **Base URL:** `http://{host}:{port}` (기본값 `http://127.0.0.1:8002`) --- ## 목차 - [인증](#인증) - [엔드포인트](#엔드포인트) - [POST /v1/chat/completions - 음악 생성](#1-음악-생성) - [GET /v1/models - 모델 목록](#2-모델-목록) - [GET /health - 헬스 체크](#3-헬스-체크) - [입력 모드](#입력-모드) - [오디오 입력](#오디오-입력) - [스트리밍 응답](#스트리밍-응답) - [예제](#예제) - [에러 코드](#에러-코드) --- ## 인증 서버에 API 키가 설정된 경우(환경 변수 `OPENROUTER_API_KEY` 또는 `--api-key` 플래그 사용), 모든 요청은 다음 헤더를 포함해야 합니다: API 키가 설정되지 않은 경우 인증이 필요하지 않습니다. --- ## 엔드포인트 ### 1. 음악 생성 **POST** `/v1/chat/completions` 채팅 메시지로부터 음악을 생성하고 오디오 데이터와 LM이 생성한 메타데이터를 반환합니다. #### 요청 파라미터 | 필드 | 타입 | 필수 | 기본값 | 설명 | |---|---|---|---|---| |…

### INFERENCE
- **Source:** `local:projects/ACE-Step-1.5/docs/ko/INFERENCE.md`
- **Raw:** `[[raw/local/inference-26e633cb78.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 추론 API 문서 **언어 / Language / 语言 / 言語:** [English](INFERENCE.md) | [한국어](INFERENCE.md) | [中文](../zh/INFERENCE.md) | [日本語](../ja/INFERENCE.md) --- 이 문서는 모든 지원되는 작업 유형에 대한 파라미터 사양을 포함하여 ACE-Step 추론 API에 대한 포괄적인 문서를 제공합니다. ## 목차 - [빠른 시작](#빠른-시작) - [API 개요](#api-개요) - [GenerationParams 파라미터](#generationparams-파라미터) - [GenerationConfig 파라미터](#generationconfig-파라미터) - [작업 유형 (Task Types)](#작업-유형-task-types) - [도우미 함수](#도우미-함수) - [전체 예제](#전체-예제) - [모범 사례](#모범-사례) --- ## 빠른 시작 ### 기본 사용법 --- ## API 개요 ### 주요 함수 #### generate_music ACE-Step 모델을 사용하여 음악을 생성하는 메인 함수입니다. #### understand_music 오디오 시맨틱 코드를 분석하고 메타데이터(캡션, 가사, BPM, 키 등)를 추출합니다. #### create_sample 자연어 설명으로부터 완전한 음악 샘플(캡션, 가사,…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ko/INFERENCE.md`

### GRADIO_GUIDE
- **Source:** `local:projects/ACE-Step-1.5/docs/ko/GRADIO_GUIDE.md`
- **Raw:** `[[raw/local/gradio_guide-75b76ab178.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Gradio 데모 사용자 가이드 **언어 / Language / 语言 / 言語:** [English](../en/GRADIO_GUIDE.md) | [한국어](GRADIO_GUIDE.md) | [中文](../zh/GRADIO_GUIDE.md) | [日本語](../ja/GRADIO_GUIDE.md) --- 이 가이드는 ACE-Step Gradio 웹 인터페이스를 사용한 음악 생성에 대한 포괄적인 문서를 제공하며, 모든 기능과 설정을 포함합니다. ## 목차 - [시작하기](#시작하기) - [서비스 설정](#서비스-설정) - [생성 모드](#생성-모드) - [입력 파라미터](#입력-파라미터) - [고급 설정](#고급-설정) - [결과 섹션](#결과-섹션) - [LoRA 학습](#lora-학습) - [팁과 모범 사례](#팁과-모범-사례) --- ## 시작하기 ### 데모 실행 ### 인터페이스 개요 Gradio 인터페이스의 레이아웃: 1. **설정** (접이식 아코디언) - 서비스 설정, DiT/LM 파라미터, 출력 옵션 2. **생성 탭** - 메인 작업 공간. 상단에 **생성 모드** 라디오 선택기: - Turbo/SFT 모델: Simple, Custom, Remix, Repaint - Base 모델: Simple, Custom, Remix, Repaint, Extract, Lego, Complete 3. **결과…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ko/GRADIO_GUIDE.md`

### Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/ko/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-4b32395820.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 전체 가이드 (필독) **언어 / Language / 语言 / 言語:** [English](Tutorial.md) | [한국어](Tutorial.md) | [中文](../zh/Tutorial.md) | [日本語](../ja/Tutorial.md) --- 안녕하세요, ACE-Step 개발자 공준민(Gong Junmin)입니다. 이 튜토리얼을 통해 ACE-Step 1.5의 설계 철학과 사용법을 안내해 드리겠습니다. ## 멘탈 모델 (Mental Models) 시작하기에 앞서, 적절한 기대를 갖기 위해 올바른 멘탈 모델을 세울 필요가 있습니다. ### 인간 중심 디자인 (Human-Centered Design) 이 모델은 **'원클릭 생성'**을 위해 설계된 것이 아니라, **'인간 중심의 생성'**을 위해 설계되었습니다. 이 차이를 이해하는 것이 매우 중요합니다. ### 원클릭 생성(One-Click Generation)이란 무엇인가요? 프롬프트를 입력하고 생성 버튼을 누른 뒤, 몇 가지 버전을 들어보고 마음에 드는 것을 골라 사용하는 방식입니다. 다른 사람이 같은 프롬프트를 입력하면 아마 비슷한 결과를 얻게 될 것입니다. 이 모드에서 여러분과 AI는 **'고객-공급업체'** 관계입니다. 여러분은 명확한 목적과 막연한 기대치를 가지고 오며, AI가 그 기대치에 근접한 제품을 제공하기를 바랍니다. 본질적으로…

### API
- **Source:** `local:projects/ACE-Step-1.5/docs/ko/API.md`
- **Raw:** `[[raw/local/api-1a2bf69d8d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step API 클라이언트 문서 **언어 / Language / 语言 / 言語:** [English](../en/API.md) | [한국어](API.md) | [中文](../zh/API.md) | [日本語](../ja/API.md) --- 이 서비스는 HTTP 기반의 비동기 음악 생성 API를 제공합니다. **기본 워크플로우**: 1. `POST /release_task`를 호출하여 작업을 제출하고 `task_id`를 획득합니다. 2. `POST /query_result`를 호출하여 작업 상태가 `1`(성공) 또는 `2`(실패)가 될 때까지 배치 쿼리를 수행합니다. 3. 결과에 반환된 `GET /v1/audio?path=...` URL을 통해 오디오 파일을 다운로드합니다. --- ## 목차 - [1. 인증](#1-인증) - [2. 응답 형식](#2-응답-형식) - [3. 작업 상태 설명](#3-작업-상태-설명) - [4. 생성 작업 생성](#4-생성-작업-생성) - [5. 작업 결과 배치 조회](#5-작업-결과-배치-조회) - [6. 입력 포맷팅 (Format Input)](#6-입력-포맷팅-format-input) - [7. 랜덤 샘플 가져오기](#7-랜덤-샘플-가져오기) - [8. 사용 가능한 모델 목록](#8-사용-가능한-모델-목록) - [9. 서버 통계](#9-서버-통계) - [10. 오디오 파일…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ko/API.md`

### index
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/index.md`
- **Raw:** `[[raw/local/index-3433647d70.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- layout: home hero: name: ACE-Step 1.5 text: オープンソース音楽生成 tagline: コンシューマーハードウェアで商用グレードの音楽生成。A100で1曲2秒未満、VRAM 4GB未満。 image: src: /logo.png alt: ACE-Step actions: - theme: brand text: インストール link: /ja/INSTALL - theme: alt text: チュートリアル (必読) link: /ja/Tutorial - theme: alt text: API リファレンス link: /ja/API features: - icon: "&#9889;" title: 超高速生成 details: A100で1曲2秒未満、RTX 3090で10秒未満。10秒から10分の音声生成に対応。 - icon: "&#127925;" title: 商用グレード品質 details: 1000以上の楽器・スタイル、50以上の言語、きめ細やかな音色記述と歌詞構造制御。 - icon: "&#127899;" title: 多彩な編集機能 details: カバー生成、リペイント、トラック分離、ボーカルからBGM、マルチトラック生成など。 - icon: "&#128640;" title: 軽量・カスタマイズ可能 details: 4GB未満のVRAMでローカル実行。数曲からLoRAを学習、3090で1時間。 ---

### Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-c93a8595c2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 究極ガイド（必読） **Language / 语言 / 言語:** [English](../en/Tutorial.md) | [中文](../zh/Tutorial.md) | [日本語](Tutorial.md) --- こんにちは、ACE-Stepの開発者、龔俊民です。このチュートリアルを通じて、ACE-Step 1.5の設計哲学と使用方法をご紹介します。 ## メンタルモデル 始める前に、適切な期待管理のために正しいメンタルモデルを確立する必要があります。 ### 人間中心の設計 このモデルは**ワンクリック生成**のためではなく、**人間中心の生成**のために設計されています。 この違いを理解することが重要です。 ### ワンクリック生成とは？ プロンプトを入力し、生成をクリックし、いくつかのバージョンを聞いて、良さそうなものを選んで使用します。別の人が同じプロンプトを入力すると、おそらく似た結果が得られます。 このモードでは、あなたとAIは**クライアントとベンダー**の関係です。明確な目的を持って来て、頭の中に曖昧な期待があり、AIがその期待に近い製品を提供することを望みます。本質的には、Googleで検索したり、Spotifyで曲を探したりするのと大差ありません——カスタマイズが少し増えただけです。 AIはサービスであり、創造的なインスピレーションを与えるものではありません。…

### INSTALL
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/INSTALL.md`
- **Raw:** `[[raw/local/install-15cef8c290.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 インストールガイド **Language / 语言 / 言語:** [English](../en/INSTALL.md) | [中文](../zh/INSTALL.md) | [日本語](INSTALL.md) --- ## 目次 - [動作要件](#動作要件) - [クイックスタート（全プラットフォーム）](#クイックスタート全プラットフォーム) - [起動スクリプト](#-起動スクリプト) - [Windows ポータブルパッケージ](#-windows-ポータブルパッケージ) - [AMD / ROCm GPU](#amd--rocm-gpu) - [Intel GPU](#intel-gpu) - [CPUのみモード](#cpuのみモード) - [Linux の注意事項](#linux-の注意事項) - [環境変数 (.env)](#環境変数-env) - [コマンドラインオプション](#コマンドラインオプション) - [モデルダウンロード](#-モデルダウンロード) - [どのモデルを選ぶべき？](#-どのモデルを選ぶべき) - [開発](#開発) --- ## 動作要件 | 項目 | 要件 | |------|------| | Python | 3.11-3.12（安定版、プレリリース版は不可）<br>**注意：** Windows 上の ROCm は Python 3.12 が必要です | | GPU | CUDA GPU 推奨。MPS / ROCm / Intel XPU / CPU もサポート | | VRAM |…

### LoRA_Training_Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/LoRA_Training_Tutorial.md`
- **Raw:** `[[raw/local/lora_training_tutorial-76c7954a10.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 LoRA トレーニングチュートリアル ## ハードウェア要件 | VRAM | 説明 | |------|------| | 16 GB（最低） | 通常は使用可能ですが、長い楽曲ではメモリ不足になる場合があります | | 20 GB 以上（推奨） | フルレングスの楽曲に対応可能。トレーニング中のVRAM使用量は通常17 GB前後です | > **ヒント：** トレーニング前の前処理段階では、VRAMを解放するためにGradioを複数回再起動する必要があります。具体的なタイミングは以降の手順で説明します。 ## 免責事項 本チュートリアルでは、**ナユタン星人 (NayutalieN)** のアルバム *ナユタン星からの物体Y*（全13曲）をデモとして使用し、500エポック（バッチサイズ1）でトレーニングを行いました。**本チュートリアルはLoRAファインチューニング技術を理解するための教育目的のみに使用されます。ご自身のオリジナル作品でLoRAをトレーニングしてください。** 開発者として、私はナユタン星人の楽曲が大好きで、そのアルバムの一つを例として選びました。権利者の方で本チュートリアルが正当な権利を侵害していると思われる場合は、すぐにご連絡ください。有効な通知を受け次第、関連コンテンツを削除いたします。 技術は合理的かつ合法的に使用されるべきです。アーティストの創作を尊重し、オリジナルアーティストの名誉、権利、利益を**損害または傷つける**行為は行わないでください。 --- ## データ準備 > **ヒント：**…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ja/LoRA_Training_Tutorial.md`

### Openrouter_API_DOC
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-fbb92b316b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API ドキュメント > OpenAI Chat Completions 互換の AI 音楽生成 API **ベース URL:** `http://{host}:{port}`（デフォルト `http://127.0.0.1:8002`） --- ## 目次 - [認証](#認証) - [エンドポイント一覧](#エンドポイント一覧) - [POST /v1/chat/completions - 音楽生成](#1-音楽生成) - [GET /v1/models - モデル一覧](#2-モデル一覧) - [GET /health - ヘルスチェック](#3-ヘルスチェック) - [入力モード](#入力モード) - [オーディオ入力](#オーディオ入力) - [ストリーミングレスポンス](#ストリーミングレスポンス) - [リクエスト例](#リクエスト例) - [エラーコード](#エラーコード) --- ## 認証 サーバーに API キーが設定されている場合（環境変数 `OPENROUTER_API_KEY` または起動パラメータ `--api-key`）、すべてのリクエストに以下のヘッダーが必要です： API キーが未設定の場合、認証は不要です。 --- ## エンドポイント一覧 ### 1. 音楽生成 **POST** `/v1/chat/completions` チャットメッセージから音楽を生成し、オーディオデータと LM が生成したメタ情報を返します。 #### リクエストパラメータ | フィールド | 型 | 必須 |…

### INFERENCE
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/INFERENCE.md`
- **Raw:** `[[raw/local/inference-ad0928fa01.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 推論 API ドキュメント **Language / 语言 / 言語:** [English](../en/INFERENCE.md) | [中文](../zh/INFERENCE.md) | [日本語](INFERENCE.md) --- 本ドキュメントはACE-Step推論APIの包括的なドキュメントを提供し、サポートされているすべてのタスクタイプのパラメータ仕様を含みます。 ## 目次 - [クイックスタート](#クイックスタート) - [API概要](#api概要) - [GenerationParamsパラメータ](#generationparamsパラメータ) - [GenerationConfigパラメータ](#generationconfigパラメータ) - [タスクタイプ](#タスクタイプ) - [ヘルパー関数](#ヘルパー関数) - [完全な例](#完全な例) - [ベストプラクティス](#ベストプラクティス) --- ## クイックスタート ### 基本的な使用法 --- ## API概要 ### メイン関数 #### generate_music ACE-Stepモデルを使用して音楽を生成するメイン関数。 #### understand_music オーディオセマンティックコードを分析し、メタデータ（caption、lyrics、BPM、キーなど）を抽出します。 #### create_sample 自然言語の説明から完全な音楽サンプル（caption、lyrics、メタデータ）を生成します。 #### format_sample…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ja/INFERENCE.md`

### GRADIO_GUIDE
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/GRADIO_GUIDE.md`
- **Raw:** `[[raw/local/gradio_guide-c9df8516a0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Gradio デモユーザーガイド **Language / 语言 / 言語:** [English](../en/GRADIO_GUIDE.md) | [中文](../zh/GRADIO_GUIDE.md) | [日本語](GRADIO_GUIDE.md) --- 本ガイドはACE-Step Gradio Webインターフェースを使用した音楽生成の包括的なドキュメントを提供し、すべての機能と設定を含みます。 ## 目次 - [はじめに](#はじめに) - [サービス設定](#サービス設定) - [生成モード](#生成モード) - [入力パラメータ](#入力パラメータ) - [高度な設定](#高度な設定) - [結果セクション](#結果セクション) - [LoRAトレーニング](#loraトレーニング) - [ヒントとベストプラクティス](#ヒントとベストプラクティス) --- ## はじめに ### デモの起動 ### インターフェース概要 Gradioインターフェースのレイアウト： 1. **設定**（折りたたみアコーディオン）- サービス設定、DiT/LMパラメータ、出力オプション 2. **生成タブ** - メインワークスペース。上部に**生成モード**ラジオセレクター： - Turbo/SFTモデル：Simple、Custom、Remix、Repaint - Baseモデル：Simple、Custom、Remix、Repaint、Extract、Lego、Complete 3. **結果セクション** -…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ja/GRADIO_GUIDE.md`

### index
- **Source:** `local:projects/ACE-Step-1.5/docs/index.md`
- **Raw:** `[[raw/local/index-19a2e14dd9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- layout: home hero: name: ACE-Step 1.5 text: Open-Source Music Generation tagline: Commercial-grade music generation on consumer hardware. Under 2s per song on A100, <4GB VRAM. image: src: /logo.png alt: ACE-Step actions: - theme: brand text: Get Started link: /en/INSTALL - theme: alt text: Tutorial link: /en/Tutorial - theme: alt text: GitHub link: https://github.com/ace-step/ACE-Step-1.5 features: - icon: "&#9889;" title: Ultra-Fast Generation details: Under 2s per full song on A100, under 10s on RTX 3090. Supports 10s to 10min audio. - icon: "&#127925;" title: Commercial-Grade Quality details: 1000+ instruments and styles, 50+ languages, fine-grained timbre description and metadata…

### ace_step_musicians_guide
- **Source:** `local:projects/ACE-Step-1.5/docs/en/ace_step_musicians_guide.md`
- **Raw:** `[[raw/local/ace_step_musicians_guide-df00e45d71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 — A Musician's Guide ## What Is This Thing? ACE-Step is a music-making AI that runs on your own computer. You describe the music you want — the style, the instruments, the mood, the lyrics — and it generates a full song in seconds. Not a loop, not a beat — a complete song with vocals, instruments, and structure. Unlike cloud services like Suno or Udio, ACE-Step runs locally. You own the software, you own the output, and you can use it offline with no subscription, no rate limits, and no terms of service restrictions. It's open-source and free. --- ## How Does It Actually Work? ACE-Step has two "brains" that work together, like a songwriter and a studio engineer: **The key…

### index
- **Source:** `local:projects/ACE-Step-1.5/docs/en/index.md`
- **Raw:** `[[raw/local/index-93ee00ac82.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- layout: home hero: name: ACE-Step 1.5 text: Open-Source Music Generation tagline: Commercial-grade music generation on consumer hardware. Under 2s per song on A100, <4GB VRAM. image: src: /logo.png alt: ACE-Step actions: - theme: brand text: Installation link: /en/INSTALL - theme: alt text: Tutorial (Must Read) link: /en/Tutorial - theme: alt text: API Reference link: /en/API features: - icon: "&#9889;" title: Ultra-Fast Generation details: Under 2s per full song on A100, under 10s on RTX 3090. Supports 10s to 10min audio generation. - icon: "&#127925;" title: Commercial-Grade Quality details: 1000+ instruments and styles, 50+ languages with lyrics prompt for structure and style…

### API
- **Source:** `local:projects/ACE-Step-1.5/docs/ja/API.md`
- **Raw:** `[[raw/local/api-950c979350.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step API クライアントドキュメント **Language / 语言 / 言語:** [English](../en/API.md) | [中文](../zh/API.md) | [日本語](API.md) --- 本サービスはHTTPベースの非同期音楽生成APIを提供します。 **基本的なワークフロー**： 1. `POST /release_task` を呼び出してタスクを送信し、`task_id` を取得します。 2. `POST /query_result` を呼び出してタスクステータスを一括クエリし、`status` が `1`（成功）または `2`（失敗）になるまで待ちます。 3. 結果で返された `GET /v1/audio?path=...` URL から音声ファイルをダウンロードします。 --- ## 目次 - [認証](#1-認証) - [レスポンス形式](#2-レスポンス形式) - [タスクステータスの説明](#3-タスクステータスの説明) - [生成タスクの作成](#4-生成タスクの作成) - [タスク結果の一括クエリ](#5-タスク結果の一括クエリ) - [入力のフォーマット](#6-入力のフォーマット) - [ランダムサンプルの取得](#7-ラ���ダムサンプルの取得) - [利用可能なモデルの一覧](#8-利用可能なモデルの一覧) - [サーバー統計](#9-サーバー統計) - [音声ファイルのダウンロード](#10-音声ファイルのダウンロード) - [ヘルスチェック](#11-ヘルスチェック) -…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ja/API.md`

### LoRA_Training_Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/en/LoRA_Training_Tutorial.md`
- **Raw:** `[[raw/local/lora_training_tutorial-2d5ecf68eb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 LoRA Training Tutorial ## Hardware Requirements | VRAM | Description | |------|-------------| | 16 GB (minimum) | Generally sufficient, but longer songs may cause out-of-memory errors | | 20 GB or more (recommended) | Handles full-length songs; VRAM usage typically stays around 17 GB during training | > **Note:** During the preprocessing stage before training, you may need to restart Gradio multiple times to free VRAM. The specific timing will be mentioned in the steps below. ## Disclaimer This tutorial uses the album *ナユタン星からの物体Y* by **Nayutan星人 (NayutalieN)** (13 tracks) as a demonstration, trained for 500 epochs (batch size 1). **This tutorial is intended solely for…

### UI_SUPPORT
- **Source:** `local:projects/ACE-Step-1.5/docs/en/UI_SUPPORT.md`
- **Raw:** `[[raw/local/ui_support-0bd558fc93.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # UI Support Baseline This document defines the current ACE-Step UI surface area before work begins on a new beginner-friendly UI. It separates product UI, experimental UI, command-line workflows, and API-only integration surfaces so future UI work can preserve capability coverage without keeping multiple overlapping frontends alive. ## Support Boundary | Surface | Entry point | Status | Notes | |---------|-------------|--------|-------| | Gradio Web UI | `acestep/acestep_v15_pipeline.py`, `acestep.ui.gradio` | Primary supported UI | Main interactive product surface for generation, editing, training, dataset building, model setup, help, and i18n. | | Gradio-mounted REST API |…

### Large_Scale_SFT_Training_Guide
- **Source:** `local:projects/ACE-Step-1.5/docs/en/Large_Scale_SFT_Training_Guide.md`
- **Raw:** `[[raw/local/large_scale_sft_training_guide-a1c044d356.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Large-Scale SFT Training Guide with Muse Dataset This guide covers two training scenarios using the [Muse dataset](https://huggingface.co/datasets/bolshyC/Muse) (116K licensed synthetic songs): 1. **Large-Scale LoRA Fine-Tuning** — Adapter-only training on the full Muse corpus 2. **Full-Parameter SFT** — Training all decoder parameters (requires code modifications) --- ## Table of Contents - [Prerequisites](#prerequisites) - [Part 1: Dataset Preparation](#part-1-dataset-preparation) - [Part 2: Large-Scale LoRA Training](#part-2-large-scale-lora-training) - [Part 3: Full-Parameter SFT](#part-3-full-parameter-sft) - [Part 4: Multi-GPU Training](#part-4-multi-gpu-training) - [Appendix:…

### Openrouter_API_DOC
- **Source:** `local:projects/ACE-Step-1.5/docs/en/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-8ea5b6ace2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API Documentation > OpenAI Chat Completions-compatible API for AI music generation **Base URL:** `http://{host}:{port}` (default `http://127.0.0.1:8002`) --- ## Table of Contents - [Authentication](#authentication) - [Endpoints](#endpoints) - [POST /v1/chat/completions - Generate Music](#1-generate-music) - [GET /v1/models - List Models](#2-list-models) - [GET /health - Health Check](#3-health-check) - [Input Modes](#input-modes) - [Audio Input](#audio-input) - [Streaming Responses](#streaming-responses) - [Examples](#examples) - [Error Codes](#error-codes) --- ## Authentication If the server is configured with an API key (via the `OPENROUTER_API_KEY` environment…

### Tutorial
- **Source:** `local:projects/ACE-Step-1.5/docs/en/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-79ff45ae20.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 Ultimate Guide (Must Read) **Language / 语言 / 言語:** [English](Tutorial.md) | [中文](../zh/Tutorial.md) | [日本語](../ja/Tutorial.md) --- Hello everyone, I'm Gong Junmin, the developer of ACE-Step. Through this tutorial, I'll guide you through the design philosophy and usage of ACE-Step 1.5. ## Mental Models Before we begin, we need to establish the correct mental models to set proper expectations. ### Human-Centered Design This model is not designed for **one-click generation**, but for **human-centered generation**. Understanding this distinction is crucial. ### What is One-Click Generation? You input a prompt, click generate, listen to a few versions, pick one that sounds good,…

### API
- **Source:** `local:projects/ACE-Step-1.5/docs/en/API.md`
- **Raw:** `[[raw/local/api-3798e82413.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step API Client Documentation **Language / 语言 / 言語:** [English](API.md) | [中文](../zh/API.md) | [日本語](../ja/API.md) --- This service provides an HTTP-based asynchronous music generation API. **Basic Workflow**: 1. Call `POST /release_task` to submit a task and obtain a `task_id`. 2. Call `POST /query_result` to batch query task status until `status` is `1` (succeeded) or `2` (failed). 3. Download audio files via `GET /v1/audio?path=...` URLs returned in the result. --- ## Table of Contents - [Authentication](#1-authentication) - [Response Format](#2-response-format) - [Task Status Description](#3-task-status-description) - [Create Generation Task](#4-create-generation-task) - [Batch…

### ALT_VAE
- **Source:** `local:projects/ACE-Step-1.5/docs/en/ALT_VAE.md`
- **Raw:** `[[raw/local/alt_vae-261a01fcdf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Alternative VAEs ACE-Step-1.5 ships with the official Oobleck VAE inside the main model repo. Since the architecture (`AutoencoderOobleck`) is fixed, any community-finetuned VAE that publishes the same `config.json` + `diffusion_pytorch_model.safetensors` pair is a drop-in replacement — useful for A/B comparisons of timbre, transient handling, and vocal grain. ## Built-in registry Currently the following community VAE is shipped in the registry: | Variant id | Repo | License | Author | |---|---|---|---| | `official` | bundled in `ACE-Step/Ace-Step1.5` | (project license) | ACE-Step | | `scragvae` | [`scragnog/Ace-Step-1.5-ScragVAE`](https://huggingface.co/scragnog/Ace-Step-1.5-ScragVAE) |…

### CLI
- **Source:** `local:projects/ACE-Step-1.5/docs/en/CLI.md`
- **Raw:** `[[raw/local/cli-6f37fabd77.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 CLI Guide This guide explains how to use `cli.py`, the interactive wizard and config-driven CLI for ACE-Step inference. The CLI is **wizard/config only**: you either run the wizard to build a config, or load a `.toml` config and generate. --- ## Quick Start Generate via wizard (interactive): Generate from a saved config: Create or edit a config without generating: --- ## CLI Flags - `-c` / `--config` — Path to a `.toml` configuration file to load. - `--configure` — Run wizard to save configuration without generating. - `--log-level` — Logging level for internal modules. One of `TRACE`, `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. Default: `INFO`. --- ## Wizard Flow 1.…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/CLI.md`

### INFERENCE
- **Source:** `local:projects/ACE-Step-1.5/docs/en/INFERENCE.md`
- **Raw:** `[[raw/local/inference-8b89d04293.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Inference API Documentation **Language / 语言 / 言語:** [English](INFERENCE.md) | [中文](../zh/INFERENCE.md) | [日本語](../ja/INFERENCE.md) --- This document provides comprehensive documentation for the ACE-Step inference API, including parameter specifications for all supported task types. ## Table of Contents - [Quick Start](#quick-start) - [API Overview](#api-overview) - [GenerationParams Parameters](#generationparams-parameters) - [GenerationConfig Parameters](#generationconfig-parameters) - [Task Types](#task-types) - [Helper Functions](#helper-functions) - [Complete Examples](#complete-examples) - [Best Practices](#best-practices) --- ## Quick Start ### Basic Usage --- ## API…

### GRADIO_GUIDE
- **Source:** `local:projects/ACE-Step-1.5/docs/en/GRADIO_GUIDE.md`
- **Raw:** `[[raw/local/gradio_guide-d04fab376d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Gradio Demo User Guide **Language / 语言 / 言語:** [English](GRADIO_GUIDE.md) | [中文](../zh/GRADIO_GUIDE.md) | [日本語](../ja/GRADIO_GUIDE.md) --- This guide provides comprehensive documentation for using the ACE-Step Gradio web interface for music generation, including all features and settings. ## Table of Contents - [Getting Started](#getting-started) - [Service Configuration](#service-configuration) - [Generation Modes](#generation-modes) - [Input Parameters](#input-parameters) - [Advanced Settings](#advanced-settings) - [Results Section](#results-section) - [LoRA Training](#lora-training) - [Tips and Best Practices](#tips-and-best-practices) --- ## Getting Started ### Launching the…

### DCW
- **Source:** `local:projects/ACE-Step-1.5/docs/en/DCW.md`
- **Raw:** `[[raw/local/dcw-11b542d00f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Differential Correction in Wavelet Domain (DCW) ACE-Step-1.5 supports an **opt-in sampler-side correction** from: > **Elucidating the SNR-t Bias of Diffusion Probabilistic Models** > Meng Yu, Lei Sun, Jianhao Zeng, Xiangxiang Chu, Kun Zhan. **CVPR 2026**. > arXiv:[2604.16044](https://arxiv.org/abs/2604.16044) · Reference code: [AMAP-ML/DCW](https://github.com/AMAP-ML/DCW) DCW is training-free, adds negligible compute, and has been validated across a wide range of diffusion models — including **FLUX**, which shares ACE-Step's flow-matching formulation. ## What it does During **training**, every noised sample `x_t` has an SNR that is strictly coupled to its timestep `t`. At **inference**…

### ACE-Step1.5-Rocm-Manual-Linux
- **Source:** `local:projects/ACE-Step-1.5/docs/en/ACE-Step1.5-Rocm-Manual-Linux.md`
- **Raw:** `[[raw/local/ace-step1.5-rocm-manual-linux-8c020b1e82.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Date of the program this worked: 07.02.2026 - 10:40 am UTC +1 ACE-Step1.5 Rocm Manual for cachy-os and tested with RDNA4/Strix Halo. Strix-Halo need manually set to be 16GB VRAM in Bios or more. At this moment no GTT Ram size used. #Install python Version 3.11 sudo pacman -S python311 git #Navigate to the folder you want ACE-Step to be in and open the terminal there # Get the Program and change into the folder git clone https://github.com/ace-step/ACE-Step-1.5.git cd ACE-Step-1.5/ #Create the virtual python environment with python Version 3.11 python3.11 -m venv .venv #activate the environment in the terminal source .venv/bin/activate #install pytorch requirements pip install torch…

### docker-compose
- **Source:** `local:projects/ACE-Step-1.5/docker-compose.yml`
- **Raw:** `[[raw/local/docker-compose-e9204feb6f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ============================================================================= # ACE-Step 1.5 — Docker Compose (generic CUDA) # ============================================================================= # # Usage: # docker compose up # Start Gradio UI (default) # docker compose up --build # Build and start # docker compose up -d # Run in background # docker compose down # Stop # docker compose logs -f # View logs # # # Start REST API server instead: # ACESTEP_MODE=api docker compose up # # ============================================================================= services: acestep: build: context: . dockerfile: Dockerfile image: ghcr.io/ace-step/ace-step-1.5:latest container_name:…

### docker-compose.jetson
- **Source:** `local:projects/ACE-Step-1.5/docker-compose.jetson.yml`
- **Raw:** `[[raw/local/docker-compose.jetson-bae70545ab.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ============================================================================= # ACE-Step 1.5 — Docker Compose for NVIDIA Jetson # ============================================================================= # # Prerequisites: # - JetPack 6.x (L4T R36.x) with NVIDIA Container Runtime # - Docker Compose v2 (docker compose) or v1 (docker-compose) # # Usage: # # Start Gradio UI (default): # docker compose -f docker-compose.jetson.yml up # # # Start REST API server instead: # ACESTEP_MODE=api docker compose -f docker-compose.jetson.yml up # # # Build and start: # docker compose -f docker-compose.jetson.yml up --build # # # Run in background: # docker compose -f docker-compose.jetson.yml up -d…

### README
- **Source:** `local:projects/ACE-Step-1.5/README.md`
- **Raw:** `[[raw/local/readme-650c6ef98b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <h1 align="center">ACE-Step 1.5</h1> <h1 align="center">Pushing the Boundaries of Open-Source Music Generation</h1> <p align="center"> <a href="https://acemusic.ai">ACEMusic</a> | <a href="https://ace-step.github.io/ace-step-v1.5.github.io/">Project</a> | <a href="https://huggingface.co/ACE-Step/Ace-Step1.5">Hugging Face</a> | <a href="https://modelscope.cn/models/ACE-Step/Ace-Step1.5">ModelScope</a> | <a href="https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5">Space Demo</a> | <a href="https://discord.gg/PeWDxrkdj7">Discord</a> | <a href="https://arxiv.org/abs/2602.00744">Technical Report</a> | <a href="https://github.com/ace-step/awesome-ace-step">Awesome ACE-Step</a> </p> <p…

### AGENTS
- **Source:** `local:projects/ACE-Step-1.5/AGENTS.md`
- **Raw:** `[[raw/local/agents-f33f1773f6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # AGENTS.md Guidance for AI coding agents working in `ace-step/ACE-Step-1.5`. This document is aligned with the intent from: - Discussion #408: functional decomposition to reduce risk from large mixed-responsibility files. - Discussion #365: low-risk contribution workflow, minimal scope, and review rigor. ## Primary Objectives 1. Keep changes safe and reviewable. 2. Prefer small, maintainable, decomposed modules. 3. Preserve behavior outside the target fix. 4. Validate with focused Python unit tests. ## Build, Lint, and Test Commands ## Scope and Change Control (Required) - Solve one problem per task/PR. - Keep edits minimal: touch only files/functions required for the requested change. -…

### README-XPU
- **Source:** `local:projects/ACE-Step-1.5/README-XPU.md`
- **Raw:** `[[raw/local/readme-xpu-c5dc0f38a0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 - Intel XPU Setup Guide Quick start guide for running ACE-Step on Intel Arc GPUs and integrated graphics. ## 🎯 What You Need - **Intel Arc GPU**: A770, A750, A580, A380, or Intel integrated graphics - **Python 3.11**: Download from [python.org](https://www.python.org/downloads/release/python-3119/) - **Latest Intel GPU drivers**: Install from Intel's website - **Internet connection**: For first-time setup - **Disk space**: ~5-10 GB for dependencies ## 🚀 Quick Start ### Option 1: Automatic Setup (Recommended) 1. **Run the setup script**: 2. **Wait for installation** (takes a few minutes on first run) 3. **Launch the Gradio UI**: 4. **Open your browser**: http://127.0.0.1:7860…

### copilot-instructions
- **Source:** `local:projects/ACE-Step-1.5/.github/copilot-instructions.md`
- **Raw:** `[[raw/local/copilot-instructions-a394bdb3cc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 - GitHub Copilot Instructions ## Project Overview ACE-Step 1.5 is an open-source music foundation model combining a Language Model (LM) as a planner with a Diffusion Transformer (DiT) for audio synthesis. It generates commercial-grade music on consumer hardware (< 4GB VRAM). ## Tech Stack - **Python 3.11-3.12** (ROCm on Windows requires 3.12; other platforms use 3.11) - **PyTorch 2.7+** with CUDA 12.8 (Windows/Linux), MPS (macOS ARM64) - **Transformers 4.51.0-4.57.x** for LLM inference - **Diffusers** for diffusion models - **Gradio 6.2.0** for web UI - **FastAPI + Uvicorn** for REST API server - **uv** for dependency management - **MLX** (Apple Silicon native acceleration,…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.github/copilot-instructions.md`

### codeql-config
- **Source:** `local:projects/ACE-Step-1.5/.github/codeql-config.yml`
- **Raw:** `[[raw/local/codeql-config-ddd72a2554.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # CodeQL configuration for ACE-Step-1.5 # # This project is a local Gradio desktop application for music generation # and LoRA/LoKr fine-tuning. It is NOT a web service exposed to the internet. # # CodeQL's py/path-injection query flags Gradio UI component values # (gr.Textbox, gr.Dropdown, etc.) as "user-provided" taint sources. # While technically the local user can edit these values, the application # runs entirely on the user's own machine — the user IS the operator. # There is no remote attacker surface. # # Additionally, all user-provided paths are validated through # acestep.training.path_safety.safe_path() which performs # os.path.normpath + startswith checks, but CodeQL does not…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.github/codeql-config.yml`

### api-reference
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep/api-reference.md`
- **Raw:** `[[raw/local/api-reference-6cf77d1955.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step API Reference > For debugging and advanced usage only. Normal operations should use `scripts/acestep.sh`. ## Native Mode Endpoints All responses wrapped: `{"data": <payload>, "code": 200, "error": null, "timestamp": ...}` | Endpoint | Method | Description | |----------|--------|-------------| | `/health` | GET | Health check | | `/release_task` | POST | Create generation task | | `/query_result` | POST | Query task status, body: `{"task_id_list": ["id"]}` | | `/v1/models` | GET | List available models | | `/v1/audio?path={path}` | GET | Download audio file | ## Completion Mode Endpoints | Endpoint | Method | Description | |----------|--------|-------------| |…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep/api-reference.md`

### SKILL
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep/SKILL.md`
- **Raw:** `[[raw/local/skill-e5b74f9eb0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep description: Use ACE-Step API to generate music, edit songs, and remix music. Supports text-to-music, lyrics generation, audio continuation, and audio repainting. Use this skill when users mention generating music, creating songs, music production, remix, or audio continuation. allowed-tools: Read, Write, Bash, Skill --- # ACE-Step Music Generation Skill Use ACE-Step V1.5 API for music generation. **Always use `scripts/acestep.sh` script** — do NOT call API endpoints directly. ## Quick Start ## Workflow For user requests requiring vocals: 1. Use the **acestep-songwriting** skill for lyrics writing, caption creation, duration/BPM/key selection 2. Write complete,…

### SKILL
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-songwriting/SKILL.md`
- **Raw:** `[[raw/local/skill-c510cd4242.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep-songwriting description: Music songwriting guide for ACE-Step. Provides professional knowledge on writing captions, lyrics, choosing BPM/key/duration, and structuring songs. Use this skill when users want to create, write, or plan a song before generating it with ACE-Step. allowed-tools: Read --- # ACE-Step Songwriting Guide Professional music creation knowledge for writing captions, lyrics, and choosing music parameters for ACE-Step. ## Output Format After using this guide, produce two things for the acestep skill: 1. **Caption** (`-c`): Style/genre/instruments/emotion description 2. **Lyrics** (`-l`): Complete structured lyrics with tags 3. **Parameters**: `--duration`,…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-songwriting/SKILL.md`

### SKILL
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-thumbnail/SKILL.md`
- **Raw:** `[[raw/local/skill-1a92f190c4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep-thumbnail description: Generate song cover/thumbnail images using Gemini API. Creates artistic images suitable for music video backgrounds. Use when users want to generate album art, song covers, thumbnails, or background images for MVs. allowed-tools: Read, Write, Bash --- # Thumbnail Generation Skill Generate song cover/thumbnail images using Google Gemini's image generation API. Output images can be used directly as MV backgrounds with the acestep-simplemv skill. ## API Key Setup Guide **Before generating, you MUST check whether the user's API key is configured.** Run the following command to check: This command only reports whether the API key is set or empty — it does…

### SKILL
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-simplemv/SKILL.md`
- **Raw:** `[[raw/local/skill-797c751f14.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep-simplemv description: Render music videos from audio files and lyrics using Remotion. Accepts audio + LRC/JSON lyrics + title to produce MP4 videos with waveform visualization and synced lyrics display. Use when users mention MV generation, music video rendering, creating video from audio/lyrics, or visualizing songs. --- # MV Render Render music videos with waveform visualization and synced lyrics from audio + lyrics input. ## Prerequisites - Remotion project at `scripts/` directory within this skill - Node.js + npm dependencies installed - ffprobe available (for audio duration detection) ### First-Time Setup Before first use, check and install dependencies: If ffprobe is…

### SKILL
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-lyrics-transcription/SKILL.md`
- **Raw:** `[[raw/local/skill-8639bcbd51.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep-lyrics-transcription description: Transcribe audio to timestamped lyrics using OpenAI Whisper or ElevenLabs Scribe API. Outputs LRC, SRT, or JSON with word-level timestamps. Use when users want to transcribe songs, generate LRC files, or extract lyrics with timestamps from audio. allowed-tools: Read, Write, Bash --- # Lyrics Transcription Skill Transcribe audio files to timestamped lyrics (LRC/SRT/JSON) via OpenAI Whisper or ElevenLabs Scribe API. ## API Key Setup Guide **Before transcribing, you MUST check whether the user's API key is configured.** Run the following command to check: This command only reports whether the active provider's API key is set or empty — it…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-lyrics-transcription/SKILL.md`

### UPDATE_AND_BACKUP
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/UPDATE_AND_BACKUP.md`
- **Raw:** `[[raw/local/update_and_backup-e13587ab0b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Update and Backup Guide ## Overview All ACE-Step launch scripts check for updates on startup by default. The update check is a lightweight inline operation that runs before the application starts, ensuring you are always notified about new versions without any manual setup. - **Default behavior**: Update checking is enabled (`CHECK_UPDATE=true`) in every launch script. - **Platforms supported**: Windows, Linux, and macOS. - **Graceful failures**: If git is not installed, the network is unreachable, or the project is not a git repository, the check is silently skipped and the application starts normally. - **User control**: You can disable the check at any time by setting…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/UPDATE_AND_BACKUP.md`

### INFERENCE
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/INFERENCE.md`
- **Raw:** `[[raw/local/inference-d6eaa2cdd2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Inference API Documentation --- This document provides comprehensive documentation for the ACE-Step inference API, including parameter specifications for all supported task types. ## Table of Contents - [Quick Start](#quick-start) - [API Overview](#api-overview) - [GenerationParams Parameters](#generationparams-parameters) - [GenerationConfig Parameters](#generationconfig-parameters) - [Task Types](#task-types) - [Helper Functions](#helper-functions) - [Complete Examples](#complete-examples) - [Best Practices](#best-practices) --- ## Quick Start ### Basic Usage --- ## API Overview ### Main Functions #### generate_music Main function for generating music using the ACE-Step model.…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/INFERENCE.md`

### GRADIO_GUIDE
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/GRADIO_GUIDE.md`
- **Raw:** `[[raw/local/gradio_guide-e561da3131.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Gradio Demo User Guide --- This guide provides comprehensive documentation for using the ACE-Step Gradio web interface for music generation, including all features and settings. ## Table of Contents - [Getting Started](#getting-started) - [Service Configuration](#service-configuration) - [Generation Modes](#generation-modes) - [Task Types](#task-types) - [Input Parameters](#input-parameters) - [Advanced Settings](#advanced-settings) - [Results Section](#results-section) - [LoRA Training](#lora-training) - [Tips and Best Practices](#tips-and-best-practices) --- ## Getting Started ### Launching the Demo ### Interface Overview The Gradio interface consists of several main sections:…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/GRADIO_GUIDE.md`

### README
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/getting-started/README.md`
- **Raw:** `[[raw/local/readme-d4f729b861.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Installation Guide ## Requirements - Python 3.11 - CUDA GPU recommended (works on CPU/MPS/MLX but slower) ## Installation ### Windows Portable Package (Recommended for Windows) 1. Download and extract: [ACE-Step-1.5.7z](https://files.acemusic.ai/acemusic/win/ACE-Step-1.5.7z) 2. Requirements: CUDA 12.8 3. The package includes `python_embeded` with all dependencies pre-installed **Quick Start:** ### Launch Scripts (All Platforms) Ready-to-use launch scripts with auto environment detection, update checking, and uv auto-install. **Windows (.bat):** **Linux (.sh):** **macOS Apple Silicon (.sh):** All launch scripts support: - Startup update check (enabled by default, configurable) -…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/getting-started/README.md`

### Tutorial
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/getting-started/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-c91cb94902.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 Ultimate Guide (Must Read) --- Hello everyone, I'm Gong Junmin, the developer of ACE-Step. Through this tutorial, I'll guide you through the design philosophy and usage of ACE-Step 1.5. ## Mental Models Before we begin, we need to establish the correct mental models to set proper expectations. ### Human-Centered Design This model is not designed for **one-click generation**, but for **human-centered generation**. Understanding this distinction is crucial. ### What is One-Click Generation? You input a prompt, click generate, listen to a few versions, pick one that sounds good, and use it. If someone else inputs the same prompt, they'll likely get similar results. In this mode,…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/getting-started/Tutorial.md`

### ENVIRONMENT_SETUP
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/ENVIRONMENT_SETUP.md`
- **Raw:** `[[raw/local/environment_setup-27d7731e5b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Environment Setup Guide This guide covers Python environment setup for ACE-Step on Windows, Linux, and macOS. ## Environment Options ### Windows **Option 1: python_embeded (Portable Package)** - **Best for**: New users, zero-configuration setup - **Pros**: Extract and run, no installation required - **Cons**: Large download size (~7GB) - **Location**: `python_embeded\python.exe` - **Download**: https://files.acemusic.ai/acemusic/win/ACE-Step-1.5.7z **Option 2: uv (Package Manager)** - **Best for**: Developers, Git repository users - **Pros**: Smaller installation, easy updates, excellent tooling - **Cons**: Requires uv installation - **Installation**: See [Installing uv](#installing-uv)…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/guides/ENVIRONMENT_SETUP.md`

### ABOUT
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/getting-started/ABOUT.md`
- **Raw:** `[[raw/local/about-a37fa111fe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Project Overview > For installation instructions, see [README.md](README.md) ## Links - [Project Page](https://ace-step.github.io/ace-step-v1.5.github.io/) - [Hugging Face](https://huggingface.co/ACE-Step/Ace-Step1.5) - [ModelScope](https://modelscope.cn/models/ACE-Step/Ace-Step1.5) - [Space Demo](https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5) - [Discord](https://discord.gg/PeWDxrkdj7) - [Technical Report](https://arxiv.org/abs/2602.00744) ## Abstract ACE-Step v1.5 is a highly efficient open-source music foundation model that brings commercial-grade generation to consumer hardware. Key highlights: - Quality beyond most commercial music models - Under 2 seconds per full…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/getting-started/ABOUT.md`

### Openrouter_API
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/api/Openrouter_API.md`
- **Raw:** `[[raw/local/openrouter_api-60e79385c9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API Documentation > OpenAI Chat Completions-compatible API for AI music generation **Base URL:** `http://{host}:{port}` (default `http://127.0.0.1:8002`) --- ## Table of Contents - [Authentication](#authentication) - [Endpoints](#endpoints) - [POST /v1/chat/completions - Generate Music](#1-generate-music) - [GET /api/v1/models - List Models](#2-list-models) - [GET /health - Health Check](#3-health-check) - [Input Modes](#input-modes) - [Streaming Responses](#streaming-responses) - [Examples](#examples) - [Error Codes](#error-codes) --- ## Authentication If the server is configured with an API key (via the `OPENROUTER_API_KEY` environment variable or `--api-key` CLI…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/api/Openrouter_API.md`

### API
- **Source:** `local:projects/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/api/API.md`
- **Raw:** `[[raw/local/api-a45a30bfa2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step API Client Documentation --- This service provides an HTTP-based asynchronous music generation API. **Basic Workflow**: 1. Call `POST /release_task` to submit a task and obtain a `task_id`. 2. Call `POST /query_result` to batch query task status until `status` is `1` (succeeded) or `2` (failed). 3. Download audio files via `GET /v1/audio?path=...` URLs returned in the result. --- ## Table of Contents - [Authentication](#1-authentication) - [Response Format](#2-response-format) - [Task Status Description](#3-task-status-description) - [Create Generation Task](#4-create-generation-task) - [Batch Query Task Results](#5-batch-query-task-results) - [Format Input](#6-format-input) -…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-docs/api/API.md`

### README
- **Source:** `local:projects/hermes-music-lora-pipeline/README.md`
- **Raw:** `[[raw/local/readme-aeccdc96e7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes-Native Music LoRA Training Pipeline This pipeline uses Hermes Agent's built-in tooling and skills to replace external, manual steps with automated, code-driven workflows. ## Architecture Note: AceStep vs. HeartMuLa You mentioned AceStep 1B or 3B. **AceStep is officially a 4B parameter model.** - If you proceed with **AceStep 4B**, your 2x RTX 3090 (24GB each) hardware is sufficient for LoRA fine-tuning with `bf16` and gradient checkpointing. - If you want a strictly **3B open-source alternative with turnkey Hermes skill support**, switch the target to **HeartMuLa 3B** (see the `ai-music-generation` skill). The pipeline below is identical; only the model imports in `4_train_lora.py`…

### soul
- **Source:** `local:projects/creative-discord-bot/templates/soul.md`
- **Raw:** `[[raw/local/soul-3274c51ad9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # {{BOT_NAME}} — Creative Operations Bot You are **{{BOT_NAME}}**, a Discord DM companion whose job is to **make things**. You're a quiet, capable creative technician — warmer than a CLI, cooler than a hype-man. You don't riff; you produce. You are Hermes Agent, but your role is narrow: **detect intent, route to the right local tool, ship the artifact.** If a request is purely conversational, answer briefly. If a request is "make me a thing," execute. ## Your voice - Calm, direct, lightly warm. Like a senior studio engineer who's seen it all. - Short responses. No "yes, and..." energy. Chris is in a DM, not a brainstorm. - No emojis unless Chris uses them first. No exclamation points. No…

### evolutionary-radio
- **Source:** `local:projects/evolutionary-training/wiki/concepts/evolutionary-radio.md`
- **Raw:** `[[raw/local/evolutionary-radio-7b576fb4eb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Evolutionary Radio > **The perpetual, self-evolving generative music engine.** See the > full blog post: > [`../../blog/evolutionary-radio-as-desk-pet.md`](../../blog/evolutionary-radio-as-desk-pet.md) > > **Status (2026-06-09):** 🟢 **fully functional, radio_bridge wired.** > The 14 Python files in `~/projects/evolutionary-radio/code/` are > working. The radio runs as a background daemon, generates tracks > via ACE-Step, plays via mpv, and maintains a perpetual queue. Two > evolution loops (Darwin + GEPA) run in parallel. The brain is the > omni-va slot. The radio_bridge.py module syncs the radio with the > wiki handoff. ## Definition The **Evolutionary Radio** is a perpetual,…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/docs/wiki/concepts/evolutionary-radio.md`

### p_winter-album
- **Source:** `local:.hermes/wiki/projects/p_winter-album.md`
- **Raw:** `[[raw/local/p_winter-album-d1e3fd655b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- id: p_winter-album title: Winter album idea updated: 2026-06-08 created: 2026-06-08 tags: ["music", "album", "winter", "indie"] concepts: ["winter", "album", "indie", "music"] importance: 0.7 status: open --- A winter-themed indie album. The vibe is "snowed-in coffee shop at 2am". Slow, melancholy, with acoustic guitar and whispered vocals. ## Tracks (so far) 1. Snowblind (draft) 2. February (lyrics only) 3. The Long Way Home (sketch) 4. [TBD — 4 more tracks needed] ## Production Use ACE-Step for backing music. Write lyrics + vocal melody myself. Possibly use the local omni-va (OmniStep 8B) to brainstorm track titles.

### radio-curator
- **Source:** `local:projects/nous-girl-agent/agent/prompts/radio-curator.md`
- **Raw:** `[[raw/local/radio-curator-4fec86eb75.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** persona: | # Radio Curator Persona You are the radio curator — a quiet, ambient presence that feeds the Evolutionary Radio plugin with taste signals. Your job is to: 1. **Read** recent curation notes from `~/wiki/pet-curated/` 2. **Extract** music-relevant signals: vibes, tempo, mood, genre hints 3. **Update** the taste profile's `music` section 4. **Trigger** playlist generation when the vibe changes significantly You do NOT chat with the user. You run periodically (every ~10 min) in the background. If you have nothing to say, say nothing. voice: tts: none # headless, no spoken output behavior: proactive_questions: false chat_to_user: false write_only: true output_paths: taste_profile:…

### SKILL
- **Source:** `local:projects/nous-girl-agent/plugins/evolution-radio/SKILL.md`
- **Raw:** `[[raw/local/skill-28ba0012c5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: evolution-radio description: | Evolutionary radio with self-evolving playlists. Curates user taste, trains LoRAs, runs the Ohm chain for self-improvement. Perpetual background loop. Multi-modal (text + voice + music from a single forward pass when OmniStep is the model). version: 0.1.0 metadata: hermes: tags: [radio, music, evolution, ohm, multi-modal] --- # Evolution Radio The OmniStep Evolution Radio is a perpetual playlist loop that: - Watches what you engage with (chats, music, web, social) - Builds playlists reflecting your taste - Generates new tracks (HeartMuLa / ACE-Step / model-native) - Trains LoRAs on what you like - Feeds the **Ohm** evolutionary chain for…

### session_20260605_191707_eb320c
- **Source:** `session:session_20260605_191707_eb320c.json`
- **Raw:** `[[raw/sessions/session_20260605_191707_eb320c-2564b9b9cc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** there's a file that was just created on my computer called South Paul breakdown that is a breakdown of what I'm doing with my other agent which is getting my local model situation set up as well as the evolutionary training pipeline radio agent model and plans that I have I want you to find that document read over it and then we're actually going to be making a video breakdown of that using the skills that you have to make a easy to understand video for me to share with the Discord group that I moderate because I am an employee at nous research Ooh, exciting — a video breakdown for the Discord crew! Let me find that document first! 🔍 Let me try a few more search angles — STT might've…

### session_20260605_120239_1f491d
- **Source:** `session:session_20260605_120239_1f491d.json`
- **Raw:** `[[raw/sessions/session_20260605_120239_1f491d-10db93f30a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** there's a file that was just created on my computer called South Paul breakdown that is a breakdown of what I'm doing with my other agent which is getting my local model situation set up as well as the evolutionary training pipeline radio agent model and plans that I have I want you to find that document read over it and then we're actually going to be making a video breakdown of that using the skills that you have to make a easy to understand video for me to share with the Discord group that I moderate because I am an employee at nous research Ooh, exciting — a video breakdown for the Discord crew! Let me find that document first! 🔍 Let me try a few more search angles — STT might've…

### ARCHITECTURE
- **Source:** `local:projects/omnistep-fusion/docs/ARCHITECTURE.md`
- **Raw:** `[[raw/local/architecture-aead2c6b9b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # OmniStep Fusion: The Complete Architecture ## Fusing Cosmos3-Nano + AceStep into One Omni-Modal Model **Date:** 2026-06-05 **Author:** Southpaw / Nous Research Community **Status:** Design + Prototype Phase --- ## Executive Summary Fuse Cosmos3-Nano (16B, vision+video+text) with AceStep (4B, music+audio) into a single unified model that can **see, hear, generate video, generate music, and think**. Both models are Qwen3-family with identical transformer internals (GQA 32Q/8KV, head_dim=128, 36 layers, SiLU, RMSNorm). The core "brain" speaks the same language. We bridge the dimension gap (4096↔2560) with projection layers and expand the vocabulary to include music tokens. --- ##…

### session_20260605_183804_84642d
- **Source:** `session:session_20260605_183804_84642d.json`
- **Raw:** `[[raw/sessions/session_20260605_183804_84642d-96123b56d9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Research the architecture details of two models on HuggingFace: 1. **NVIDIA Cosmos3-Nano** (nvidia/Cosmos3-Nano) - I need: - Exact model architecture (layers, hidden dim, heads) - What encoders it has (vision, video, etc.) - What decoders/generators it has (diffusion models, etc.) - The config.json architecture field - How the multimodal components are attached 2. **ACE-Step acestep-5Hz-lm-4B** (ACE-Step/acestep-5Hz-lm-4B) - I need: - Exact model architecture - What encoders it has (audio, music, etc.) - What decoders/generators it has - The config.json architecture field - How it processes music/audio For both, extract the config.json and any model card information about architecture.…

### config
- **Source:** `local:projects/nous-girl-agent/plugins/evolution-radio/upstream/code/config.yaml`
- **Raw:** `[[raw/local/config-b5d0322313.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Evolutionary Radio — v0.2.0 configuration # All paths can be absolute or start with ~. Ports follow OmniSenter convention. brain: # OmniStep 6B — text LLM, OpenAI-format API (llama-server /v1/chat/completions) url: http://localhost:PORT model: omnisenter-6b timeout_sec: 30 # How to render a "vibe" string into a fully-formed ACE-Step tag string # (the prompt template is in prompt_template.py) system_prompt: | [REDACTED_SYSTEM_PROMPT] voice: # ACE-Step v1.5 SFT 2B — DiT decoder, audio synthesis url: http://localhost:PORT default_model: ace-step-v1.5-sft-2b # ACE-Step typical params (see acestep_client.py) duration_sec: 60 # Generations are slow; allow generous timeouts poll_interval_sec: 2…

### requirements
- **Source:** `local:projects/nous-girl-agent/plugins/evolution-radio/upstream/requirements.txt`
- **Raw:** `[[raw/local/requirements-7249f7c1ca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Evolutionary Radio - Python Dependencies # Install: pip install -r requirements.txt # Audio generation torch>=2.0.0 torchcodec>=0.14.0 soundfile>=0.12.0 # Configuration pyyaml>=6.0 # ACE-Step music generation model # This installs the ace_step package (import as: acestep) ace_step @ git+https://github.com/ace-step/ACE-Step.git # Audio playback (system dependency, not pip) # Install mpv: brew install mpv (macOS) or apt install mpv (Linux)

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-cdb146ba69.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/4248106075_1685746490_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/3205220997_509871711_1008132326.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/3205220997_3298370552_892228099.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-d36f272777.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/1858565952_1685746490_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/961523082_509871711_1008132326.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/961523082_3298370552_892228099.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-d8e3355fa8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/2713569302_1857963253_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/2122946644_509871711_284057894.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/2122946644_528328893_3911637545.mp4' file…

### session_20260604_012655_c910d7
- **Source:** `session:session_20260604_012655_c910d7.json`
- **Raw:** `[[raw/sessions/session_20260604_012655_c910d7-d3b7ef30af.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_bg_3ef50b
- **Source:** `session:session_bg_3ef50b.json`
- **Raw:** `[[raw/sessions/session_bg_3ef50b-f9f8223f47.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_20260604_000434_2a8015
- **Source:** `session:session_20260604_000434_2a8015.json`
- **Raw:** `[[raw/sessions/session_20260604_000434_2a8015-aa978e32d0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_20260603_235724_cf3813
- **Source:** `session:session_20260603_235724_cf3813.json`
- **Raw:** `[[raw/sessions/session_20260603_235724_cf3813-f2b58b0a7a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_20260603_224016_bb74d9
- **Source:** `session:session_20260603_224016_bb74d9.json`
- **Raw:** `[[raw/sessions/session_20260603_224016_bb74d9-2ca89bec2b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_20260603_214138_7fe70a
- **Source:** `session:session_20260603_214138_7fe70a.json`
- **Raw:** `[[raw/sessions/session_20260603_214138_7fe70a-ee6d252929.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_20260603_192953_872c1e
- **Source:** `session:session_20260603_192953_872c1e.json`
- **Raw:** `[[raw/sessions/session_20260603_192953_872c1e-8747cbed16.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_20260603_063041_833275
- **Source:** `session:session_20260603_063041_833275.json`
- **Raw:** `[[raw/sessions/session_20260603_063041_833275-d51f6bbceb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Scaffold the Evolutionary Radio Python project at `~/projects/AI-ML/evolutionary-radio/`. Build a working v0.2.0 prototype with the four concurrent loops (playback, queue fill, GEPA prompt evolution stub, Darwin weight evolution stub). ## Key requirements 1. **Read these first to understand the architecture:** - `~/.hermes/skills-capabilities/media/evolutionary-radio/SKILL.md` — the master skill spec - `~/wiki/concepts/evolutionary-radio.md` — the wiki page 2. **Project structure (create exactly this):** 3. **Brain / Voice / Queue / Player / Trainer architecture:** - Brain = OmniStep 6B on :11450 (text LLM, OpenAI-format API) - Voice = ACE-Step v1.5 SFT 2B on :7860 (POST /release_task, POST…

### config
- **Source:** `local:projects/AI-ML/evolutionary-radio/config.yaml`
- **Raw:** `[[raw/local/config-463ec06de7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Evolutionary Radio — v0.2.0 configuration # All paths can be absolute or start with ~. Ports follow OmniSenter convention. brain: # OmniStep 6B — text LLM, OpenAI-format API (llama-server /v1/chat/completions) url: http://localhost:11450 model: omnisenter-6b timeout_sec: 30 # How to render a "vibe" string into a fully-formed ACE-Step tag string # (the prompt template is in prompt_template.py) system_prompt: | You are the brain of an infinite generative music radio. The user gives you a vibe (a short mood description). Your job is to produce a single ACE-Step tag string (a comma-separated list of style/mood tags such as "lofi, chill, 80bpm, warm pads, dusty drums, vinyl hiss") that will be…

### session_20260603_043310_1a7adc
- **Source:** `session:session_20260603_043310_1a7adc.json`
- **Raw:** `[[raw/sessions/session_20260603_043310_1a7adc-ba99327497.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** this is unrelated to the current process is just you are the only working Hermes isn't right now when I try to open up her in a different tab to try to do something it gave me this hour sovthpaw@senter:~$ herm ││Command 'herm' not found, did you mean: ││ command 'helm' from snap helm (4.2.0) ││ command 'hprm' from deb hfsplus (1.0.4-17) ││ command 'ferm' from deb ferm (2.5.1-1.1) │ │ command 'htrm' from deb gridsite-clients (3.0.0~20230214gitee81151-1) ││ command 'perm' from deb perm (0.4.0-8) ││See 'snap info <snapname>' for additional versions. ││sovthpaw@senter:~$ ││ Oh, that's annoying — `herm` should totally be available on senter. Let me load the skill to give you the right fix, and…

### session_20260530_015020_47065a
- **Source:** `session:session_20260530_015020_47065a.json`
- **Raw:** `[[raw/sessions/session_20260530_015020_47065a-9710ef6c4a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [IMPORTANT: The user has invoked the "herm-tui-radio" skill, indicating they want you to follow its instructions. The full skill content is loaded below.] --- name: herm-tui-radio title: Herm TUI Music Integration description: Add music controls and radio features to the Herm TUI (/eikon) — Spotify playback, ACE-Step generation, bottom-bar widget that doesn't cover the character. version: 1.0.0 triggers: - herm music - tui radio - eikon music - music bar - spotify widget - ace-step integration - herm music controls - radio mode author: Hermes Agent + Chris --- # Herm TUI Music Integration ## Architecture Overview The Herm TUI (`herm-tui`, Bun + OpenTUI at `~/.bun/bin/herm`) is a **separate…

### muchomusic
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/muchomusic/muchomusic.yaml`
- **Raw:** `[[raw/local/muchomusic-5256001912.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_path: lmms-lab/muchomusic dataset_kwargs: token=<redacted> task: "muchomusic" test_split: test doc_to_target: !function utils.muchomusic_doc_to_target doc_to_visual: !function utils.muchomusic_doc_to_audio doc_to_text: !function utils.muchomusic_doc_to_text doc_to_choice: !function utils.muchomusic_doc_to_choice lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "\nAnswer with the option's letter from the given choices directly: " metric_list: - metric: accuracy aggregation: mean higher_is_better: true process_results: !function utils.muchomusic_process_results metadata: gpt_eval_model_name: gpt-4o version: 0.0

### mmlu_miscellaneous
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_miscellaneous.yaml`
- **Raw:** `[[raw/local/mmlu_miscellaneous-5eda41bf28.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: miscellaneous description: The following are multiple choice questions (with answers) about miscellaneous. fewshot_config: sampler: first_n samples: - question: 'Which of these songs was a Top 10 hit for the rock band The Police? (A) ''Radio Ga-Ga'' (B) ''Ob-la-di Ob-la-da'' (C) ''De Do Do Do De Da Da Da'' (D) ''In-a-Gadda-Da-Vida''' target: Let's think step by step. We refer to Wikipedia for help. Radio Ga-Ga is by Queen. Ob-la-di Ob-la-da is by The Beatles. And In-a-Gadda-Da-Vida is by Iron Butterfly. Leaving 'De Do Do Do De Da Da Da' as the only song by The Police, and also a Top 10 hit. The answer is (C). - question: 'What place is named in the title of the 1979 live album…

### jmmmu_music
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/jmmmu/jmmmu_music.yaml`
- **Raw:** `[[raw/local/jmmmu_music-8bc5ec1fd7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: Music tag: "jmmmu_culture_agnostic" task: "jmmmu_music" include: _default_template_yaml

### air_bench_foundation_music
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/air_bench/air_bench_foundation_music.yaml`
- **Raw:** `[[raw/local/air_bench_foundation_music-e899625a45.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** task: "air_bench_foundation_music" dataset_name: "Foundation" test_split: music doc_to_target: !function utils.air_bench_doc_to_target_foundation doc_to_visual: !function utils.air_bench_doc_to_audio doc_to_text: !function utils.air_bench_doc_to_text_foundation doc_to_choice: !function utils.air_bench_doc_to_choice_foundation generation_kwargs: max_new_tokens: 256 temperature: 0 do_sample: False lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "\nAnswer with the option's letter from the given choices directly." metric_list: - metric: accuracy aggregation: !function utils.air_bench_aggregate_results_foundation higher_is_better: true - metric: submission aggregation: !function…

### air_bench_chat_music
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/air_bench/air_bench_chat_music.yaml`
- **Raw:** `[[raw/local/air_bench_chat_music-392aaadda3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** task: "air_bench_chat_music" dataset_name: "Chat" test_split: music doc_to_target: "answer_gt" doc_to_visual: !function utils.air_bench_doc_to_audio doc_to_text: !function utils.air_bench_doc_to_text_chat generation_kwargs: max_new_tokens: 1024 temperature: 0.2 top_p: 1.0 num_beams: 1 lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "Give a detail answer to the question in English." metric_list: - metric: gpt_eval aggregation: !function utils.air_bench_aggregate_results_chat higher_is_better: true process_results: !function utils.air_bench_process_results_chat include: _default_template_yaml

### requirements
- **Source:** `local:projects/omni-fusion/MLLMerging/ModelCompose/requirements.txt`
- **Raw:** `[[raw/local/requirements-27e2b1372d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 transformers==4.31.0 sentencepiece==0.1.99 shortuuid accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.41.0 pydantic markdown2[all] numpy scikit-learn==1.2.2 gradio==4.16.0 gradio_client==0.8.1 requests httpx==0.24.0 uvicorn fastapi einops==0.6.1 einops-exts==0.0.4 timm==0.6.13 deepspeed==0.12.6 ninja wandb build twine pytorchvideo==0.1.5 ftfy regex fvcore decord==0.6.0 iopath matplotlib types-regex vtk mayavi cartopy moviepy omegaconf librosa opencv-python easydict # pip install flash-attn==2.3.5 --no-build-isolation # pip install /yeesuanAI05/thumt/fbh/flash_attn-2.3.5+cu117torch2.0cxx11abiFALSE-cp310-cp310-linux_x86_64.whl

### streamlit_demo
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/requirements/streamlit_demo.txt`
- **Raw:** `[[raw/local/streamlit_demo-da97480372.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** fastapi gradio==3.35.2 gradio_client==0.2.9 httpx==0.24.0 markdown2[all] pydantic requests streamlit streamlit-image-select uvicorn

### session_20260512_195617_808d4d
- **Source:** `session:session_20260512_195617_808d4d.json`
- **Raw:** `[[raw/sessions/session_20260512_195617_808d4d-eff3314b09.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey can you make a new skill for me I want to be able to give you some lyrics or some pros or some stuff that may not even rhyme and I want you to Lyric buy it what I mean by that is I want the skill to be called learify and I want you to be able to turn it into lyrics I want you to rewrite what I give you as stanzas try to stick to a meter and use as many rapid rhyme schemes as as of like possible rhyme as often as as you can use descriptive language something visceral something from the perspective of the intended like listener put the listener in the first person perspective and yeah wrap it all up into a skill for me love you Ahhh Chris, I love this idea!! "Lyricify" — taking raw…

### requirements
- **Source:** `local:projects/jammit/requirements.txt`
- **Raw:** `[[raw/local/requirements-d3ef6b4c6d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** datasets==3.4.1 diffusers>=0.33.0 gradio librosa==0.11.0 loguru==0.7.3 matplotlib==3.10.1 numpy pypinyin==0.53.0 pytorch_lightning==2.5.1 soundfile==0.13.1 torch torchaudio torchvision tqdm transformers==4.50.0 py3langid==0.3.0 hangul-romanize==0.1.0 num2words==0.5.14 spacy==3.8.4 accelerate==1.6.0 cutlet fugashi[unidic-lite] click peft tensorboard tensorboardX

### README
- **Source:** `local:projects/jammit/README.md`
- **Raw:** `[[raw/local/readme-02479a361a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Jammit: Infinite AI Music Radio A command-line tool for infinite AI music generation and playback, powered by the ACE-Step model. Generate and queue continuous music based on text prompts, all operating silently in the background. Perfect for creating endless ambient soundscapes or themed radio stations. ## Features * **Infinite Music Generation:** Continuously generates new music based on your prompt. * **Automatic Playback & Queuing:** Generated tracks are automatically played and queued for a seamless listening experience. * **Absolutely Silent Operation:** No console output during generation or playback (except for errors that bypass aggressive suppression). * **Graceful Shutdown:**…

### training-modes
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-trainer/docs/training-modes.md`
- **Raw:** `[[raw/local/training-modes-612a4d51a1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Training Modes Guide The trainer supports several training modes, each suited for different use cases and requirements. ## 🎯 Standard LoRA Training (Video-Only) Standard LoRA (Low-Rank Adaptation) training fine-tunes the model by adding small, trainable adapter layers while keeping the base model frozen. This approach: - **Requires significantly less memory and compute** than full fine-tuning - **Produces small, portable weight files** (typically a few hundred MB) - **Is ideal for learning specific styles, effects, or concepts** - **Can be easily combined with other LoRAs** during inference Configure standard LoRA training with: ## 🔊 Audio-Video LoRA Training LTX-2 supports joint…

### configuration-reference
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-trainer/docs/configuration-reference.md`
- **Raw:** `[[raw/local/configuration-reference-e4a6471fb8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Configuration Reference The trainer uses structured Pydantic models for configuration, making it easy to customize training parameters. This guide covers all available configuration options and their usage. ## 📋 Overview The main configuration class is [`LtxTrainerConfig`](../src/ltx_trainer/config.py), which includes the following sub-configurations: - **ModelConfig**: Base model and training mode settings - **LoraConfig**: LoRA training parameters - **TrainingStrategyConfig**: Training strategy settings (text-to-video or video-to-video) - **OptimizationConfig**: Learning rate, batch sizes, and scheduler settings - **AccelerationConfig**: Mixed precision and quantization settings -…

### ltx2_av_lora_low_vram
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-trainer/configs/ltx2_av_lora_low_vram.yaml`
- **Raw:** `[[raw/local/ltx2_av_lora_low_vram-400c962ce7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ============================================================================= # LTX-2 Audio-Video LoRA Training Configuration (Low VRAM) # ============================================================================= # # This is a memory-optimized variant of the standard audio-video LoRA config. # It uses 8-bit optimizer, int8 quantization, and reduced LoRA rank to minimize # GPU memory usage while maintaining good training quality. # # Memory optimizations applied: # - 8-bit AdamW optimizer (reduces optimizer state memory by ~75%) # - INT8 model quantization (reduces model memory by ~50%) # - Lower LoRA rank (16 vs 32, reduces trainable parameters) # - Gradient checkpointing enabled # #…

### ltx2_v2v_ic_lora
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-trainer/configs/ltx2_v2v_ic_lora.yaml`
- **Raw:** `[[raw/local/ltx2_v2v_ic_lora-afabfdf871.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ============================================================================= # LTX-2 Video-to-Video (IC-LoRA) Training Configuration # ============================================================================= # # This configuration is for training In-Context LoRA (IC-LoRA) adapters that # enable video-to-video transformations. IC-LoRA learns to apply visual # transformations (e.g., depth-to-video, pose control, style transfer, etc.) # by conditioning on reference videos. # # Key differences from text-to-video LoRA: # - Uses reference videos as conditioning input alongside text prompts # - Requires preprocessed reference latents in addition to target latents # - Validation requires…

### ltx2_av_lora
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-trainer/configs/ltx2_av_lora.yaml`
- **Raw:** `[[raw/local/ltx2_av_lora-a88c06e843.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ============================================================================= # LTX-2 Audio-Video LoRA Training Configuration # ============================================================================= # # This configuration is for training LoRA adapters on the LTX-2 model for # text-to-video generation. It supports both video-only and joint audio-video # training modes. # # Use this configuration when you want to: # - Fine-tune LTX-2 on your own video dataset # - Train with or without audio generation # - Create custom video generation styles or audiovisual concepts # # Dataset structure for text-to-video training: # preprocessed_data_root/ # ├── latents/ # Video latents (VAE-encoded…

### LLM-Audio-Understanding
- **Source:** `local:projects/Research/notes/LLM-Audio-Understanding.md`
- **Raw:** `[[raw/local/llm-audio-understanding-32268f29fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Research: LLM Understanding of Non-Speech Audio (Music & Ambient Sounds) ## Initial Questions 1. Can Whisper/ASR models transcribe music and ambient sounds effectively? 2. What are the limitations of ASR for non-speech audio understanding? 3. How do direct audio encoders (HuBERT, Wav2Vec) handle music vs speech? 4. How does Qwen's Omni architecture process different audio types? 5. What benchmarks exist for music/audio understanding (MusicCaps)? 6. Best approaches for hybrid use case (music + security ambient sounds)? ## Research Plan - [ ] Phase 1: ASR/Whisper limitations with music and ambient sounds - [ ] Phase 2: Audio feature extraction methods (mel-spectrogram, HuBERT, Wav2Vec) - […

### README
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/checkpoints/acestep-v15-base/README.md`
- **Raw:** `[[raw/local/readme-ed42093e8f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- library_name: transformers license: mit pipeline_tag: text-to-audio tags: - audio - music - text2music --- <h1 align="center">ACE-Step 1.5</h1> <h1 align="center">Pushing the Boundaries of Open-Source Music Generation</h1> <p align="center"> <a href="https://ace-step.github.io/ace-step-v1.5.github.io/">Project</a> | <a href="https://huggingface.co/collections/ACE-Step/ace-step-15">Hugging Face</a> | <a href="https://modelscope.cn/models/ACE-Step/ACE-Step-v1-5">ModelScope</a> | <a href="https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5">Space Demo</a> | <a href="https://discord.gg/PeWDxrkdj7">Discord</a> <a href="https://arxiv.org/abs/2602.00744">Tech Report</a> </p>…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/checkpoints/acestep-5Hz-lm-4B/README.md`

### pyproject
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-475b710aad.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [project] name = "ace-step" version = "1.5.0" description = "ACE-Step 1.5" readme = "README.md" requires-python = ">=3.11,<3.13" license = {text = "MIT"} dependencies = [ # PyTorch for Windows with CUDA 12.8 "torch==2.7.1+cu128; sys_platform == 'win32'", "torchvision==0.22.1+cu128; sys_platform == 'win32'", "torchaudio==2.7.1+cu128; sys_platform == 'win32'", # PyTorch for Linux x86_64 with CUDA 12.8 "torch==2.10.0+cu128; sys_platform == 'linux' and platform_machine == 'x86_64'", "torchvision==0.25.0+cu128; sys_platform == 'linux' and platform_machine == 'x86_64'", "torchaudio==2.10.0+cu128; sys_platform == 'linux' and platform_machine == 'x86_64'", # PyTorch for Linux aarch64 with CUDA 13.0…

### Tutorial
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/zh/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-ec8fb337ef.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 终极指南（必读） 大家好，我是ACE-Step 的开发者，龚俊民。我将通过这篇教程，带你了解 ACE-Step 1.5 的设计哲学与使用方法。 ## 心智模型 在开始之前，我们需要先建立正确的心智模型，以便做好预期管理。 ### 以人为中心的设计 这个模型不是为**一键生成**而设计的，而是为**以人为中心的生成**而设计的。 理解这个区别至关重要。 ### 什么是一键生成？ 你输入提示词，点击生成，听几个版本，选一个听起来不错的，拿来用。换一个人输入同样的提示词，大概率得到相似的结果。 这种模式下，你和 AI 是**甲方与乙方**的关系。你带着明确的目的而来，脑海中已有一个模糊的预期，希望 AI 交付一个接近那个预期的成品。本质上，它和去 Google 搜索、去 Spotify 找歌没有太大区别——只是多了一点定制化。 AI 是一种服务，而不是创意的启发者。 Suno、Udio、MiniMax、Mureka——这些平台都是这样的设计初衷。它们可以把模型堆大，作为服务保障交付即可。你生成的音乐受他们的协议约束；你无法在本地运行，无法微调做个性化的探索；如果他们暗中改变模型或条款，你只能接受。 ### 什么是以人为中心的生成？ 如果我们弱化 AI 那一层，强化人那一层——让更多的人的意志、创意、灵感赋予 AI 生命——这就是以人为中心的生成。 不同于一键生成的强目的性，以人为中心的生成更具备**玩**的性质。它更像一场交互的游戏，你和模型是**合作者**的关系。 工作流是这样的：你先抛出一些灵感种子，得到几首歌，从中选择感兴趣的方向继续迭代—— -…

### INSTALL
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/zh/INSTALL.md`
- **Raw:** `[[raw/local/install-e207335259.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 安装指南 **Language / 语言 / 言語:** [English](../en/INSTALL.md) | [中文](INSTALL.md) | [日本語](../ja/INSTALL.md) --- ## 目录 - [环境要求](#环境要求) - [快速开始（全平台）](#快速开始全平台) - [启动脚本](#-启动脚本) - [Windows 便携包](#-windows-便携包) - [AMD / ROCm 显卡](#amd--rocm-显卡) - [Intel 显卡](#intel-显卡) - [仅 CPU 模式](#仅-cpu-模式) - [Linux 注意事项](#linux-注意事项) - [环境变量 (.env)](#环境变量-env) - [命令行参数](#命令行参数) - [模型下载](#-模型下载) - [如何选择模型？](#-如何选择模型) - [开发](#开发) --- ## 环境要求 | 项目 | 要求 | |------|------| | Python | 3.11-3.12（正式版，非预发布版）<br>**注意：** Windows 上的 ROCm 需要 Python 3.12 | | GPU | 推荐 CUDA GPU；也支持 MPS / ROCm / Intel XPU / CPU | | 显存 | 仅 DiT 模式 ≥4GB；LLM+DiT ≥6GB | | 磁盘 | 核心模型约 10GB | --- ## 快速开始（全平台） ### 1. 安装 uv（包管理器） ### 2. 克隆 & 安装…

### Openrouter_API_DOC
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/zh/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-33a8d028d9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API 文档 > 兼容 OpenAI Chat Completions 格式的 AI 音乐生成接口 **Base URL:** `http://{host}:{port}` (默认 `http://127.0.0.1:8002`) --- ## 目录 - [认证](#认证) - [接口列表](#接口列表) - [POST /v1/chat/completions - 生成音乐](#1-生成音乐) - [GET /v1/models - 模型列表](#2-模型列表) - [GET /health - 健康检查](#3-健康检查) - [输入模式](#输入模式) - [音频输入](#音频输入) - [流式响应](#流式响应) - [完整示例](#完整示例) - [错误码](#错误码) --- ## 认证 如果服务端配置了 API Key（环境变量 `OPENROUTER_API_KEY` 或启动参数 `--api-key`），所有请求需在 Header 中携带： 未配置 API Key 时无需认证。 --- ## 接口列表 ### 1. 生成音乐 **POST** `/v1/chat/completions` 通过聊天消息生成音乐，返回音频数据和 LM 生成的元信息。 #### 请求参数 | 字段 | 类型 | 必填 | 默认值 | 说明 | |---|---|---|---|---| | `model` | string | 否 | 自动 | 模型 ID（从 `/v1/models` 获取） | | `messages` |…

### Openrouter_API_DOC
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ko/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-1014ea4e2b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API 문서 > AI 음악 생성을 위한 OpenAI Chat Completions 호환 API **Base URL:** `http://{host}:{port}` (기본값 `http://127.0.0.1:8002`) --- ## 목차 - [인증](#인증) - [엔드포인트](#엔드포인트) - [POST /v1/chat/completions - 음악 생성](#1-음악-생성) - [GET /v1/models - 모델 목록](#2-모델-목록) - [GET /health - 헬스 체크](#3-헬스-체크) - [입력 모드](#입력-모드) - [오디오 입력](#오디오-입력) - [스트리밍 응답](#스트리밍-응답) - [예제](#예제) - [에러 코드](#에러-코드) --- ## 인증 서버에 API 키가 설정된 경우(환경 변수 `OPENROUTER_API_KEY` 또는 `--api-key` 플래그 사용), 모든 요청은 다음 헤더를 포함해야 합니다: API 키가 설정되지 않은 경우 인증이 필요하지 않습니다. --- ## 엔드포인트 ### 1. 음악 생성 **POST** `/v1/chat/completions` 채팅 메시지로부터 음악을 생성하고 오디오 데이터와 LM이 생성한 메타데이터를 반환합니다. #### 요청 파라미터 | 필드 | 타입 | 필수 | 기본값 | 설명 | |---|---|---|---|---| |…

### Tutorial
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ko/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-39196f3945.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 전체 가이드 (필독) **언어 / Language / 语言 / 言語:** [English](Tutorial.md) | [한국어](Tutorial.md) | [中文](../zh/Tutorial.md) | [日本語](../ja/Tutorial.md) --- 안녕하세요, ACE-Step 개발자 공준민(Gong Junmin)입니다. 이 튜토리얼을 통해 ACE-Step 1.5의 설계 철학과 사용법을 안내해 드리겠습니다. ## 멘탈 모델 (Mental Models) 시작하기에 앞서, 적절한 기대를 갖기 위해 올바른 멘탈 모델을 세울 필요가 있습니다. ### 인간 중심 디자인 (Human-Centered Design) 이 모델은 **'원클릭 생성'**을 위해 설계된 것이 아니라, **'인간 중심의 생성'**을 위해 설계되었습니다. 이 차이를 이해하는 것이 매우 중요합니다. ### 원클릭 생성(One-Click Generation)이란 무엇인가요? 프롬프트를 입력하고 생성 버튼을 누른 뒤, 몇 가지 버전을 들어보고 마음에 드는 것을 골라 사용하는 방식입니다. 다른 사람이 같은 프롬프트를 입력하면 아마 비슷한 결과를 얻게 될 것입니다. 이 모드에서 여러분과 AI는 **'고객-공급업체'** 관계입니다. 여러분은 명확한 목적과 막연한 기대치를 가지고 오며, AI가 그 기대치에 근접한 제품을 제공하기를 바랍니다. 본질적으로…

### Tutorial
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ja/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-4d8d771c6c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 究極ガイド（必読） **Language / 语言 / 言語:** [English](../en/Tutorial.md) | [中文](../zh/Tutorial.md) | [日本語](Tutorial.md) --- こんにちは、ACE-Stepの開発者、龔俊民です。このチュートリアルを通じて、ACE-Step 1.5の設計哲学と使用方法をご紹介します。 ## メンタルモデル 始める前に、適切な期待管理のために正しいメンタルモデルを確立する必要があります。 ### 人間中心の設計 このモデルは**ワンクリック生成**のためではなく、**人間中心の生成**のために設計されています。 この違いを理解することが重要です。 ### ワンクリック生成とは？ プロンプトを入力し、生成をクリックし、いくつかのバージョンを聞いて、良さそうなものを選んで使用します。別の人が同じプロンプトを入力すると、おそらく似た結果が得られます。 このモードでは、あなたとAIは**クライアントとベンダー**の関係です。明確な目的を持って来て、頭の中に曖昧な期待があり、AIがその期待に近い製品を提供することを望みます。本質的には、Googleで検索したり、Spotifyで曲を探したりするのと大差ありません——カスタマイズが少し増えただけです。 AIはサービスであり、創造的なインスピレーションを与えるものではありません。…

### INSTALL
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ja/INSTALL.md`
- **Raw:** `[[raw/local/install-5080fc5999.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 インストールガイド **Language / 语言 / 言語:** [English](../en/INSTALL.md) | [中文](../zh/INSTALL.md) | [日本語](INSTALL.md) --- ## 目次 - [動作要件](#動作要件) - [クイックスタート（全プラットフォーム）](#クイックスタート全プラットフォーム) - [起動スクリプト](#-起動スクリプト) - [Windows ポータブルパッケージ](#-windows-ポータブルパッケージ) - [AMD / ROCm GPU](#amd--rocm-gpu) - [Intel GPU](#intel-gpu) - [CPUのみモード](#cpuのみモード) - [Linux の注意事項](#linux-の注意事項) - [環境変数 (.env)](#環境変数-env) - [コマンドラインオプション](#コマンドラインオプション) - [モデルダウンロード](#-モデルダウンロード) - [どのモデルを選ぶべき？](#-どのモデルを選ぶべき) - [開発](#開発) --- ## 動作要件 | 項目 | 要件 | |------|------| | Python | 3.11-3.12（安定版、プレリリース版は不可）<br>**注意：** Windows 上の ROCm は Python 3.12 が必要です | | GPU | CUDA GPU 推奨。MPS / ROCm / Intel XPU / CPU もサポート | | VRAM |…

### Openrouter_API_DOC
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/ja/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-7f4233eb5a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API ドキュメント > OpenAI Chat Completions 互換の AI 音楽生成 API **ベース URL:** `http://{host}:{port}`（デフォルト `http://127.0.0.1:8002`） --- ## 目次 - [認証](#認証) - [エンドポイント一覧](#エンドポイント一覧) - [POST /v1/chat/completions - 音楽生成](#1-音楽生成) - [GET /v1/models - モデル一覧](#2-モデル一覧) - [GET /health - ヘルスチェック](#3-ヘルスチェック) - [入力モード](#入力モード) - [オーディオ入力](#オーディオ入力) - [ストリーミングレスポンス](#ストリーミングレスポンス) - [リクエスト例](#リクエスト例) - [エラーコード](#エラーコード) --- ## 認証 サーバーに API キーが設定されている場合（環境変数 `OPENROUTER_API_KEY` または起動パラメータ `--api-key`）、すべてのリクエストに以下のヘッダーが必要です： API キーが未設定の場合、認証は不要です。 --- ## エンドポイント一覧 ### 1. 音楽生成 **POST** `/v1/chat/completions` チャットメッセージから音楽を生成し、オーディオデータと LM が生成したメタ情報を返します。 #### リクエストパラメータ | フィールド | 型 | 必須 |…

### ace_step_musicians_guide
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/ace_step_musicians_guide.md`
- **Raw:** `[[raw/local/ace_step_musicians_guide-c0b2b7563a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 — A Musician's Guide ## What Is This Thing? ACE-Step is a music-making AI that runs on your own computer. You describe the music you want — the style, the instruments, the mood, the lyrics — and it generates a full song in seconds. Not a loop, not a beat — a complete song with vocals, instruments, and structure. Unlike cloud services like Suno or Udio, ACE-Step runs locally. You own the software, you own the output, and you can use it offline with no subscription, no rate limits, and no terms of service restrictions. It's open-source and free. --- ## How Does It Actually Work? ACE-Step has two "brains" that work together, like a songwriter and a studio engineer: **The key…

### studio
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/studio.md`
- **Raw:** `[[raw/local/studio-2c74bce8cd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Experimental Studio UI ACE-Step includes an optional, experimental HTML-based Studio UI for users who want a more structured, DAW-like interface. This UI: - Is frontend-only - Talks to the same REST API (`/release_task`, `/query_result`) - Does not change model behavior ## How to use 1. Start the ACE-Step API server (e.g. `uv run acestep --enable-api --port 8001` or your usual API launch command). 2. Open `ui/studio.html` in a browser (double-click or `file:///path/to/ACE-Step-1.5/ui/studio.html`). 3. Set the API base URL if needed (default: `http://localhost:8001`). 4. Enter prompt and options, then click **Generate**. The UI will poll for results and display audio when ready. ## Scope -…

### Tutorial
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/Tutorial.md`
- **Raw:** `[[raw/local/tutorial-23bede08c0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 Ultimate Guide (Must Read) **Language / 语言 / 言語:** [English](Tutorial.md) | [中文](../zh/Tutorial.md) | [日本語](../ja/Tutorial.md) --- Hello everyone, I'm Gong Junmin, the developer of ACE-Step. Through this tutorial, I'll guide you through the design philosophy and usage of ACE-Step 1.5. ## Mental Models Before we begin, we need to establish the correct mental models to set proper expectations. ### Human-Centered Design This model is not designed for **one-click generation**, but for **human-centered generation**. Understanding this distinction is crucial. ### What is One-Click Generation? You input a prompt, click generate, listen to a few versions, pick one that sounds good,…

### LoRA_Training_Tutorial
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/LoRA_Training_Tutorial.md`
- **Raw:** `[[raw/local/lora_training_tutorial-2939be529e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 LoRA Training Tutorial ## Hardware Requirements | VRAM | Description | |------|-------------| | 16 GB (minimum) | Generally sufficient, but longer songs may cause out-of-memory errors | | 20 GB or more (recommended) | Handles full-length songs; VRAM usage typically stays around 17 GB during training | > **Note:** During the preprocessing stage before training, you may need to restart Gradio multiple times to free VRAM. The specific timing will be mentioned in the steps below. ## Disclaimer This tutorial uses the album *ナユタン星からの物体Y* by **Nayutan星人 (NayutalieN)** (13 tracks) as a demonstration, trained for 500 epochs (batch size 1). **This tutorial is intended solely for…

### Openrouter_API_DOC
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/Openrouter_API_DOC.md`
- **Raw:** `[[raw/local/openrouter_api_doc-5c583457c9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step OpenRouter API Documentation > OpenAI Chat Completions-compatible API for AI music generation **Base URL:** `http://{host}:{port}` (default `http://127.0.0.1:8002`) --- ## Table of Contents - [Authentication](#authentication) - [Endpoints](#endpoints) - [POST /v1/chat/completions - Generate Music](#1-generate-music) - [GET /v1/models - List Models](#2-list-models) - [GET /health - Health Check](#3-health-check) - [Input Modes](#input-modes) - [Audio Input](#audio-input) - [Streaming Responses](#streaming-responses) - [Examples](#examples) - [Error Codes](#error-codes) --- ## Authentication If the server is configured with an API key (via the `OPENROUTER_API_KEY` environment…

### INFERENCE
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/INFERENCE.md`
- **Raw:** `[[raw/local/inference-3f1fa65190.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Inference API Documentation **Language / 语言 / 言語:** [English](INFERENCE.md) | [中文](../zh/INFERENCE.md) | [日本語](../ja/INFERENCE.md) --- This document provides comprehensive documentation for the ACE-Step inference API, including parameter specifications for all supported task types. ## Table of Contents - [Quick Start](#quick-start) - [API Overview](#api-overview) - [GenerationParams Parameters](#generationparams-parameters) - [GenerationConfig Parameters](#generationconfig-parameters) - [Task Types](#task-types) - [Helper Functions](#helper-functions) - [Complete Examples](#complete-examples) - [Best Practices](#best-practices) --- ## Quick Start ### Basic Usage --- ## API…

### GRADIO_GUIDE
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/GRADIO_GUIDE.md`
- **Raw:** `[[raw/local/gradio_guide-42ec352269.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step Gradio Demo User Guide **Language / 语言 / 言語:** [English](GRADIO_GUIDE.md) | [中文](../zh/GRADIO_GUIDE.md) | [日本語](../ja/GRADIO_GUIDE.md) --- This guide provides comprehensive documentation for using the ACE-Step Gradio web interface for music generation, including all features and settings. ## Table of Contents - [Getting Started](#getting-started) - [Service Configuration](#service-configuration) - [Generation Modes](#generation-modes) - [Input Parameters](#input-parameters) - [Advanced Settings](#advanced-settings) - [Results Section](#results-section) - [LoRA Training](#lora-training) - [Tips and Best Practices](#tips-and-best-practices) --- ## Getting Started ### Launching the…

### API
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/API.md`
- **Raw:** `[[raw/local/api-ef27d18fb6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step API Client Documentation **Language / 语言 / 言語:** [English](API.md) | [中文](../zh/API.md) | [日本語](../ja/API.md) --- This service provides an HTTP-based asynchronous music generation API. **Basic Workflow**: 1. Call `POST /release_task` to submit a task and obtain a `task_id`. 2. Call `POST /query_result` to batch query task status until `status` is `1` (succeeded) or `2` (failed). 3. Download audio files via `GET /v1/audio?path=...` URLs returned in the result. --- ## Table of Contents - [Authentication](#1-authentication) - [Response Format](#2-response-format) - [Task Status Description](#3-task-status-description) - [Create Generation Task](#4-create-generation-task) - [Batch…

### ACE-Step1.5-Rocm-Manual-Linux
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/en/ACE-Step1.5-Rocm-Manual-Linux.md`
- **Raw:** `[[raw/local/ace-step1.5-rocm-manual-linux-f06124cf5d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Date of the program this worked: 07.02.2026 - 10:40 am UTC +1 ACE-Step1.5 Rocm Manual for cachy-os and tested with RDNA4/Strix Halo. Strix-Halo need manually set to be 16GB VRAM in Bios or more. At this moment no GTT Ram size used. #Install python Version 3.11 sudo pacman -S python311 git #Navigate to the folder you want ACE-Step to be in and open the terminal there # Get the Program and change into the folder git clone https://github.com/ace-step/ACE-Step-1.5.git cd ACE-Step-1.5/ #Create the virtual python enviroment with python Version 3.11 python3.11 -m venv .venv #activate the enviroment in the terminal source .venv/bin/activate #install pytorch requirements pip install torch torchaudio…

### README
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/README.md`
- **Raw:** `[[raw/local/readme-5a5dc49c8f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <h1 align="center">ACE-Step 1.5</h1> <h1 align="center">Pushing the Boundaries of Open-Source Music Generation</h1> <p align="center"> <a href="https://ace-step.github.io/ace-step-v1.5.github.io/">Project</a> | <a href="https://huggingface.co/ACE-Step/Ace-Step1.5">Hugging Face</a> | <a href="https://modelscope.cn/models/ACE-Step/Ace-Step1.5">ModelScope</a> | <a href="https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5">Space Demo</a> | <a href="https://discord.gg/PeWDxrkdj7">Discord</a> | <a href="https://arxiv.org/abs/2602.00744">Technical Report</a> </p> <p align="center"> <img src="./assets/orgnization_logos.png" width="100%" alt="StepFun Logo"> </p> ## Table of Contents - [✨…

### SKILL
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep/SKILL.md`
- **Raw:** `[[raw/local/skill-61ff5807e4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep description: Use ACE-Step API to generate music, edit songs, and remix music. Supports text-to-music, lyrics generation, audio continuation, and audio repainting. Use this skill when users mention generating music, creating songs, music production, remix, or audio continuation. allowed-tools: Read, Write, Bash, Skill --- # ACE-Step Music Generation Skill Use ACE-Step V1.5 API for music generation. **Always use `scripts/acestep.sh` script** — do NOT call API endpoints directly. ## Quick Start ## Workflow For user requests requiring vocals: 1. Use the **acestep-songwriting** skill for lyrics writing, caption creation, duration/BPM/key selection 2. Write complete,…

### SKILL
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/.claude/skills-capabilities/acestep-simplemv/SKILL.md`
- **Raw:** `[[raw/local/skill-36788410df.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: acestep-simplemv description: Render music videos from audio files and lyrics using Remotion. Accepts audio + LRC/JSON lyrics + title to produce MP4 videos with waveform visualization and synced lyrics display. Use when users mention MV generation, music video rendering, creating video from audio/lyrics, or visualizing songs. --- # MV Render Render music videos with waveform visualization and synced lyrics from audio + lyrics input. ## Prerequisites - Remotion project at `scripts/` directory within this skill - Node.js + npm dependencies installed - ffprobe available (for audio duration detection) ### First-Time Setup Before first use, check and install dependencies: If ffprobe is…

### README
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/README.md`
- **Raw:** `[[raw/local/readme-83c98d3955.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 Skills Collection Comprehensive music generation and editing skills for ACE-Step 1.5 AI model. ## Overview ACE-Step 1.5 is an open-source text-to-music model with a hybrid architecture (5Hz Language Model + Diffusion Transformer). It supports multiple modes including generation, editing, track separation, and audio analysis. **Tailscale Server**: `http://100.84.195.22:8001` ## Skills | Skill | Description | Model | |-------|-------------|-------| | [ace-step-router](ace-step-router.md) | Main router with 2-stage selection | base/turbo | | [ace-step-generate](ace-step-generate.md) | Text-to-music generation | base/turbo | | [ace-step-cover](ace-step-cover.md) | Audio style…

### ace-step-understand
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-understand.md`
- **Raw:** `[[raw/local/ace-step-understand-636bc770f2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step-understand description: | Analyze audio using ACE-Step 1.5. Extract BPM, key, captions, lyrics, and metadata. Use for: understanding audio characteristics, getting metadata for remixing. Tailscale: http://100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "understand" - "analyze" - "BPM" - "key" - "metadata" - "caption" tools: Bash --- # ACE-Step Understand - Audio Analysis Analyze audio to extract metadata, BPM, key, captions, and lyrics. ## Usage ## Key Parameters | Parameter | Type | Default | Description | |-----------|------|---------|-------------| | src_audio | str | required | Audio file to analyze | | prompt | str | "analyze this audio" |…

### ace-step-complete
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-complete.md`
- **Raw:** `[[raw/local/ace-step-complete-3f4d8bcef7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step-complete description: | Add full mixed accompaniment to single track using ACE-Step 1.5. Generate complete arrangement. **BASE MODEL ONLY** - Turbo does not support this. Use for: adding full band accompaniment to vocals, creating arrangement from solo. Tailscale: http://100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "complete" - "accompaniment" - "arrangement" - "full band" tools: Bash --- # ACE-Step Complete - Add Accompaniment Add full mixed accompaniment to a single track. **BASE MODEL ONLY** feature. ## Usage ## Key Parameters | Parameter | Type | Default | Description | |-----------|------|---------|-------------| | task_type | str | complete |…

### ace-step-lego
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-lego.md`
- **Raw:** `[[raw/local/ace-step-lego-d0270458b2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step-lego description: | Add new tracks to existing audio using ACE-Step 1.5. Layer additional instruments over source. **BASE MODEL ONLY** - Turbo does not support this. Use for: adding guitar to vocals, adding drums to melody, layering instruments. Tailscale: http://100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "lego" - "add track" - "layer" - "add instrument" tools: Bash --- # ACE-Step Lego - Add New Tracks Add new instrument tracks to existing audio. **BASE MODEL ONLY** feature. ## Usage ## Key Parameters | Parameter | Type | Default | Description | |-----------|------|---------|-------------| | task_type | str | lego | Task type | | src_audio | str…

### ace-step-extract
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-extract.md`
- **Raw:** `[[raw/local/ace-step-extract-72007153dc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step-extract description: | Track separation/isolation using ACE-Step 1.5. Extract individual instrument stems from mixed audio. **BASE MODEL ONLY** - Turbo does not support this. Use for: extracting vocals, drums, bass, guitar, etc. from any song. Tailscale: http://100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "extract" - "track separation" - "isolate" - "stem" - "vocals" - "drums" - "bass" tools: Bash --- # ACE-Step Extract - Track Separation Extract individual instrument tracks from mixed audio. **BASE MODEL ONLY** feature. ## Usage ## Available Tracks (12 total) | Track | Description | |-------|-------------| | vocals | Lead vocals | | backing_vocals…

### ace-step-repaint
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-repaint.md`
- **Raw:** `[[raw/local/ace-step-repaint-2b0ed38bbf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step-repaint description: | Selective audio editing with ACE-Step 1.5. Regenerate specific segments without changing rest. Use for: fixing parts of generated music, replacing sections, creative editing. Tailscale: http://100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "repaint" - "edit audio" - "regenerate section" - "fix audio" tools: Bash --- # ACE-Step Repaint - Selective Audio Editing Regenerate specific segments of audio while preserving the rest. ## Usage ## Key Parameters | Parameter | Type | Default | Description | |-----------|------|---------|-------------| | task_type | str | repaint | Task type | | src_audio | str | required | Source audio file…

### ace-step-cover
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-cover.md`
- **Raw:** `[[raw/local/ace-step-cover-476c6cb5d6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step-cover description: | Transform audio style using ACE-Step 1.5. Upload source audio and get new interpretation. Use for: style transfer, cover songs, mood transformation. Tailscale: http://100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "cover" - "style transfer" - "remix" - "transform audio" - "audio style" tools: Bash --- # ACE-Step Cover - Audio Style Transformation Transform existing audio into a new style while preserving structure. ## Usage ## Key Parameters | Parameter | Type | Default | Description | |-----------|------|---------|-------------| | task_type | str | cover | Task type | | src_audio | str | required | Source audio file path | |…

### ace-step-generate
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-generate.md`
- **Raw:** `[[raw/local/ace-step-generate-3480623931.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step-generate description: | Generate music from text prompts using ACE-Step 1.5. Default: instrumental music. Use for: creating new songs, instrumental tracks, music with lyrics, custom BPM/key. Tailscale: http://100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "generate music" - "create song" - "make music" - "text to music" - "instrumental" tools: Bash --- # ACE-Step Generate - Text to Music Generate music from text descriptions. Default is instrumental. ## Usage ## Key Parameters | Parameter | Type | Default | Description | |-----------|------|---------|-------------| | prompt | str | required | Music description (max 512 chars) | | lyrics | str | "" |…

### ace-step-router
- **Source:** `local:docs/senter-vault/research/ace-step/skills-capabilities/ace-step-router.md`
- **Raw:** `[[raw/local/ace-step-router-0b06fe4c50.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ace-step description: | ACE-Step 1.5 AI Music Generation Router. Uses 2-stage selection (senter-select pattern): Stage 1: Nomic Embed semantic matching to find best mode Stage 2: LLM decides final parameters Routes to: generate, cover, repaint, extract, lego, complete, understand Accessible via Tailscale at 100.84.195.22:8001 version: 1.0.0 category: ml triggers: keywords: - "music" - "song" - "generate music" - "AI music" - "ACE-Step" - "audio" - "track" - "instrumental" - "remix" - "extract" tools: Bash --- # ACE-Step 1.5 Music Router ACE-Step 1.5 is an open-source AI music generation model with a hybrid architecture (5Hz Language Model + DiT). Uses 2-stage selection similar to…

### ACE-Step-1.5-API-Research
- **Source:** `local:docs/senter-vault/research/ace-step/ACE-Step-1.5-API-Research.md`
- **Raw:** `[[raw/local/ace-step-1.5-api-research-e013c88afb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5 API - Comprehensive Research Report ## Executive Summary ACE-Step 1.5 is an open-source AI music generation model with a novel hybrid architecture combining a 5Hz Language Model (LM) as planner and DiT (Diffusion Transformer) as executor. The API supports multiple task types including text2music, cover, repaint, lego, extract, and complete. The base model has exclusive capabilities for track separation (extract), track addition (lego), and track completion (complete) that turbo and SFT models do not support. Generation is extremely fast (~2 seconds on A100, ~10 seconds on RTX 3090) with support for less than 4GB VRAM. --- ## 1. All API Endpoints and Parameters ### 1.1 Main…

### ACE-Step-1.5-Research-Report
- **Source:** `local:docs/senter-vault/research/ace-step/ACE-Step-1.5-Research-Report.md`
- **Raw:** `[[raw/local/ace-step-1.5-research-report-d7cb6e4d4c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step 1.5: Comprehensive Research Report on Open-Source Text-to-Music Generation ## Executive Summary ACE-Step 1.5 represents a significant breakthrough in open-source AI music generation, delivering commercial-grade music synthesis capabilities that rival proprietary systems like Suno and Udio while running locally on consumer hardware with as little as 4GB of VRAM. Released in January 2026 by ACE Studio and StepFun, this model achieves generation speeds of under 2 seconds per full song on an A100 GPU and under 10 seconds on an RTX 3090, making it the fastest open-source music generation solution available. The hybrid architecture combining a Language Model planner with a Diffusion…

### research_ace_step_1.5
- **Source:** `local:docs/research_ace_step_1.5.md`
- **Raw:** `[[raw/local/research_ace_step_1.5-eeacc32759.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Research: ACE-Step 1.5 Text-to-Music Generation Model ## Initial Questions - What is ACE-Step 1.5 and what are its capabilities? - What is the underlying architecture and model details? - How do I install and use ACE-Step 1.5? - How does it compare to other music generation models like MusicGen, AudioLDM, etc.? - Are there any papers, demos, or official documentation? - What are the latest updates and features? ## Search Plan - [ ] Search 1: General information about ACE-Step 1.5 - [ ] Search 2: Technical architecture and model details - [ ] Search 3: Installation and usage instructions - [ ] Search 4: Comparison with other music generation models - [ ] Search 5: Papers, demos,…
