---
title: Local Inference
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Local Inference

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### sirvir
- **Source:** `github:SouthpawIN/sirvir`
- **Raw:** `[[raw/github/sirvir-e7a312251c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Sirvir — model fleet manager & intelligence engine for Hermes Agent. Autonomous model lifecycle manager: local serving, benchmarking, auto-scaling, API fallback, HuggingFace scanning, creator tracking, backend optimization, budget monitoring. # Sirvir — Model Fleet Manager & Intelligence Engine ![Sirvir Profile](profile.png) **Sirvir** is an autonomous Hermes Agent profile that manages your entire model layer — local serving, benchmarking, auto-scaling, API fallback, HuggingFace scanning, creator quality tracking, backend optimization, token budget monitoring, and external app endpoint serving. ![Sirvir System Diagram](banner.png) > *TOWARDS SELF-IMPROVEMENT* --- ## Table of Contents -…

### turbofit
- **Source:** `github:SouthpawIN/turbofit`
- **Raw:** `[[raw/github/turbofit-3b80602d62.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Hardware-fit checker + multi-launcher installer (llama.cpp / Ollama / vllm / SGlang) for Hermes-Agent. Uses llmfit to verify model fit, generates accurate backend-specific launch strings, launches detached, wires into Hermes as main or auxiliary. Bundles 5-model curated NVIDIA NIM free-tier API list. Enforces 64K context floor. v1.0.0. # turbofit — opinionated unified LLM backend for Hermes Agent ![Turbofit — unified backend, amber and mint aesthetic](assets/turbofit-hero.png) Turbofit manages the entire lifecycle of LLMs with Hermes Agent: detecting your GPU, picking the best model, launching local servers, wiring API providers, managing daemons (systemd on Linux, PID files on Windows),…

### southpaw-turbohaul
- **Source:** `github:SouthpawIN/southpaw-turbohaul`
- **Raw:** `[[raw/github/southpaw-turbohaul-ea25a47ca5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Curated model server for Nous Research community. Fork of turbohaul-manager with AtomicBot llama.cpp (TQ3/TQ4 + MTP + NextN) and Southpaw's hand-picked models. ![Turbohaul-Manager — hauling inference traffic](docs/banner.png) # Turbohaul-Manager Ollama-shape inference manager using [Tom's TurboQuant](https://github.com/TheTom/llama-cpp-turboquant) fork of llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Nvidia RTX GPU's including Blackwell. ## What it does - Accepts OpenAI / Ollama-shape `/v1/chat/completions` requests - Single-slot serial sidecar (one llama-server child holds the model) - **MTP speculative decoding (draft-mtp) composes with TurboQuant turbo2/3/4 KV cache…

### DiscordSam
- **Source:** `github:SouthpawIN/DiscordSam`
- **Raw:** `[[raw/github/discordsam-0fc58f1b54.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** An intelligent, context-aware Discord bot powered by local or remote LLMs, featuring RAG, web scraping, TTS, and more. # DiscordSam: The Hyper-Intelligent Discord Bot ## 1. Project Overview i test in main. lol. deal with it. DiscordSam is an advanced, context-aware Discord bot designed to provide intelligent, detailed, and rational responses. Its primary purpose is to serve as a highly interactive and knowledgeable assistant within a Discord server, capable of engaging in complex conversations, accessing and processing external information, and performing various tasks through slash commands. The bot leverages local Large Language Models (LLMs), Retrieval Augmented Generation (RAG) for…

### turbohaul-llmfit
- **Source:** `github:SouthpawIN/turbohaul-llmfit`
- **Raw:** `[[raw/github/turbohaul-llmfit-49e695cafe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Generate optimized llama-server launch strings and turbohaul-manager manifests using llmfit hardware detection + TurboQuant flag doctrine # turbohaul-llmfit Generate optimized llama-server launch strings and turbohaul-manager manifests using llmfit hardware detection + TurboQuant flag doctrine ## Install ## License MIT

### turbohaul-manager
- **Source:** `github:SouthpawIN/turbohaul-manager`
- **Raw:** `[[raw/github/turbohaul-manager-aab2afdd20.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Ollama-shape inference manager using Tom's TurboQuant llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Blackwell. ![Turbohaul-Manager — cyberpunk CONTAK rig hauling inference traffic](docs/banner.png) # Turbohaul-Manager Ollama-shape inference manager using [Tom's TurboQuant](https://github.com/TheTom/llama-cpp-turboquant) fork of llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Nvidia RTX GPU's including Blackwell. ## What it does - Accepts OpenAI / Ollama-shape `/v1/chat/completions` requests - Single-slot serial sidecar (one llama-server child holds the model) - ACTIVE_MATCH cascade for same-thread follow-ups within a grace window (warm-process reuse) -…

### senter-mcp-server
- **Source:** `github:SouthpawIN/senter-mcp-server`
- **Raw:** `[[raw/github/senter-mcp-server-df287afa69.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** MCP server for Senter-Server # Senter MCP Server Model Context Protocol (MCP) server for Senter-Server that exposes vision and text model endpoints. ## Features - **Text Model Endpoint**: Chat/completions API at `/api/v1/chat/completions` - **Vision Model Endpoint**: Image analysis at `/api/v1/images/analyze` - **Hermes Reasoning Interface**: Advanced reasoning at `/api/hermes/reason` - **MCP Tools**: Standard MCP tools interface at `/api/mcp/tools` ## Quick Start ## API Endpoints ### GET / Returns service information and available endpoints. ### GET /health Health check endpoint. ### POST /api/v1/chat/completions Text model chat completions. ### POST /api/v1/images/analyze Vision model…

### benchmark-infographics
- **Source:** `github:SouthpawIN/benchmark-infographics`
- **Raw:** `[[raw/github/benchmark-infographics-c1dbdc380a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** AI model benchmark comparison infographics # Benchmark Infographics AI model benchmark comparison infographics — freely shareable, proper sources. ## June 2026: Frontier AI Models **Claude Opus 4.8 vs GPT-5.5 vs GLM-5.2 vs Qwen3.7 Max vs DeepSeek V4 Pro** ![Frontier Benchmark Comparison](frontier-benchmark-comparison-june2026.png) ### Sources - LLM Stats (llm-stats.com) - Official model cards (HuggingFace, provider blogs) - GLM-5.2 model card (zai-org/GLM-5.2) - Qwen3.7 blog (qwen.ai) - GPT-5.5 launch blog (openai.com) - Claude Opus 4.8 launch materials (anthropic.com) ### Style Nous Research brand identity — strict monochrome, Swiss grid, Courier Pro, halftone grain texture.

### sovthpaw/omnistep-new
- **Source:** `huggingface:https://huggingface.co/model/sovthpaw/omnistep-new`
- **Raw:** `[[raw/huggingface/sovthpaw-omnistep-new-689ff559ab.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** { "_id": "6a397336e23c77e1f504479f", "id": "sovthpaw/omnistep-new", "author": "sovthpaw", "gated": false, "lastModified": "2026-06-23T18:44:48.000Z", "likes": 0, "trendingScore": 0, "private": false, "sha": "4de27fd7256229325e8ac42b6412c49500013c09", "downloads": 142, "tags": [ "transformers", "safetensors", "gguf", "qwen3", "text-generation", "darwin-family", "multimodal", "music", "omnistep", "chat", "image-text-to-text", "text-to-music", "tool-calling", "evolutionary", "conversational", "license:apache-2.0", "text-generation-inference", "endpoints_compatible", "region:us" ], "pipeline_tag": "image-text-to-text", "library_name": "transformers", "createdAt": "2026-06-22T17:39:02.000Z",…

### flavored-nanocode
- **Source:** `github:SouthpawIN/flavored-nanocode`
- **Raw:** `[[raw/github/flavored-nanocode-1d5a2dacb3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Minimal Claude Code alternative. Different languages and frameworks flavors # 🧬 Flavored Nanocode **Single-file minimal Claude Code alternatives in 120+ languages and flavors.** Each implementation is a complete agentic coding assistant with tool use — `read`, `write`, `edit`, `glob`, `grep`, `shell` — all in one file with minimal dependencies. ![screenshot](screenshot.png) ## 🗺️ All Flavors (120 implementations!) ### 🐍 Python | Flavor | File | Deps | |--------|------|------| | vanilla | [`interpreted/python/nanocode.py`](interpreted/python/nanocode.py) | 0 | | Flask | [`interpreted/python/flask/nanocode.py`](interpreted/python/flask/nanocode.py) | flask | | FastAPI |…

### sovthpaw/OmniSenter-Base-16B
- **Source:** `huggingface:https://huggingface.co/model/sovthpaw/OmniSenter-Base-16B`
- **Raw:** `[[raw/huggingface/sovthpaw-omnisenter-base-16b-d9ed22da2c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** { "_id": "6a232e942d5d4d5b0ea863b1", "id": "sovthpaw/OmniSenter-Base-16B", "author": "sovthpaw", "gated": false, "lastModified": "2026-06-05T20:22:33.000Z", "likes": 0, "trendingScore": 0, "private": false, "sha": "c55278e3a3b19cc51fc03de66bea06d5ddbb19a3", "downloads": 4, "tags": [ "transformers", "safetensors", "qwen3", "text-generation", "darwin-family", "evolutionary-merging", "multimodal", "vision", "audio", "video-generation", "merge", "nous-research", "conversational", "arxiv:2605.14386", "base_model:Qwen/Qwen3-8B", "base_model:merge:Qwen/Qwen3-8B", "base_model:nvidia/Cosmos3-Nano", "base_model:merge:nvidia/Cosmos3-Nano", "license:apache-2.0", "text-generation-inference",…

### sovthpaw/Omni-Senter-3B
- **Source:** `huggingface:https://huggingface.co/model/sovthpaw/Omni-Senter-3B`
- **Raw:** `[[raw/huggingface/sovthpaw-omni-senter-3b-c61f33cef4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** { "_id": "699c48d5dac985183e268a08", "id": "sovthpaw/Omni-Senter-3B", "author": "sovthpaw", "gated": false, "lastModified": "2026-02-24T01:12:47.000Z", "likes": 8, "trendingScore": 0, "private": false, "sha": "da5a0c000eaf73b6f6ce2e3bb23d7054875206ab", "downloads": 24, "tags": [ "safetensors", "gguf", "agent", "any-to-any", "en", "zh", "dataset:Nanbeige/ToolMind", "base_model:Qwen/Qwen2.5-Omni-3B", "base_model:quantized:Qwen/Qwen2.5-Omni-3B", "license:apache-2.0", "region:us" ], "pipeline_tag": "any-to-any", "createdAt": "2026-02-23T12:32:21.000Z", "modelId": "sovthpaw/Omni-Senter-3B", "siblings": [ { "rfilename": ".gitattributes" }, { "rfilename": "README.md" }, { "rfilename":…

### ty
- **Source:** `local:projects/LLM-Infra/beellama.cpp/ty.toml`
- **Raw:** `[[raw/local/ty-f475b3078e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [environment] extra-paths = ["./gguf-py", "./examples/model-conversion/scripts", "./tools/server/tests", "./scripts/snapdragon/qdc/tests"] python-version = "3.10" [rules] deprecated = "warn" [src] exclude = [ "./tools/mtmd/legacy-models/**", ] [[overrides]] include = [ "./tools/server/tests/**", "./scripts/snapdragon/qdc/**", "./tools/mtmd/tests/**", ] [overrides.rules] unresolved-reference = "ignore" unresolved-import = "ignore" unresolved-attribute = "ignore" [[overrides]] include = [ "./examples/pydantic_models_to_grammar.py", ] [overrides.rules] unsupported-operator = "ignore" not-subscriptable = "ignore"

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/ty.toml`, `local:projects/LLM-Infra/llama.cpp-atomic/ty.toml`

### data-flow-simplified-model-mode
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/data-flow-simplified-model-mode.md`
- **Raw:** `[[raw/local/data-flow-simplified-model-mode-731fab9a3f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/flows/data-flow-simplified-model-mode.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/data-flow-simplified-model-mode.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/data-flow-simplified-model-mode.md`

### settings-flow
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/settings-flow.md`
- **Raw:** `[[raw/local/settings-flow-483bffd5fc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/settings-flow.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/settings-flow.md`

### database-flow
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/database-flow.md`
- **Raw:** `[[raw/local/database-flow-556a3e2e80.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/flows/database-flow.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/database-flow.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/database-flow.md`

### data-flow-simplified-router-mode
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/data-flow-simplified-router-mode.md`
- **Raw:** `[[raw/local/data-flow-simplified-router-mode-5f77337550.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/flows/data-flow-simplified-router-mode.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/data-flow-simplified-router-mode.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/data-flow-simplified-router-mode.md`

### server-flow
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/server-flow.md`
- **Raw:** `[[raw/local/server-flow-bc0e11268a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/flows/server-flow.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/server-flow.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/server-flow.md`

### mcp-flow
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/mcp-flow.md`
- **Raw:** `[[raw/local/mcp-flow-bf4324f4de.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/flows/mcp-flow.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/mcp-flow.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/mcp-flow.md`

### models-flow
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/models-flow.md`
- **Raw:** `[[raw/local/models-flow-b7bf0ddf80.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/flows/models-flow.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/models-flow.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/models-flow.md`

### conversations-flow
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/flows/conversations-flow.md`
- **Raw:** `[[raw/local/conversations-flow-6ba4693a71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/flows/conversations-flow.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/flows/conversations-flow.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/flows/conversations-flow.md`

### high-level-architecture
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/architecture/high-level-architecture.md`
- **Raw:** `[[raw/local/high-level-architecture-f2ab35e678.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/architecture/high-level-architecture.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/architecture/high-level-architecture.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/architecture/high-level-architecture.md`

### high-level-architecture-simplified
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/docs/architecture/high-level-architecture-simplified.md`
- **Raw:** `[[raw/local/high-level-architecture-simplified-1cc868be35.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** (no prose excerpt; metadata only)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/webui/docs/architecture/high-level-architecture-simplified.md`, `local:projects/LLM-Infra/llama.cpp/tools/ui/docs/architecture/high-level-architecture-simplified.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/docs/architecture/high-level-architecture-simplified.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-238f4021f8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-ui) set(LLAMA_UI_HF_BUCKET "llama-ui" CACHE STRING "Hugging Face bucket name for prebuilt UI assets") # Backward compat: forward old var to new one if(DEFINED LLAMA_BUILD_WEBUI) set(LLAMA_BUILD_UI ${LLAMA_BUILD_WEBUI}) message(DEPRECATION "LLAMA_BUILD_WEBUI is deprecated, use LLAMA_BUILD_UI instead") endif() if(DEFINED LLAMA_USE_PREBUILT_WEBUI) set(LLAMA_USE_PREBUILT_UI ${LLAMA_USE_PREBUILT_WEBUI}) message(DEPRECATION "LLAMA_USE_PREBUILT_WEBUI is deprecated, use LLAMA_USE_PREBUILT_UI instead") endif() if(DEFINED LLAMA_WEBUI_HF_BUCKET) set(LLAMA_UI_HF_BUCKET ${LLAMA_WEBUI_HF_BUCKET}) message(DEPRECATION "LLAMA_WEBUI_HF_BUCKET is deprecated, use LLAMA_UI_HF_BUCKET instead")…

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/ui/README.md`
- **Raw:** `[[raw/local/readme-b50b72ccb9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-ui A modern, feature-rich web interface for llama-server built with SvelteKit. This UI provides an intuitive chat interface with advanced file handling, conversation management, and comprehensive model interaction capabilities. Llama UI supports two server operation modes: - **MODEL mode** - Single model operation (standard llama-server) - **ROUTER mode** - Multi-model operation with dynamic model loading/unloading --- ## Table of Contents - [Features](#features) - [Getting Started](#getting-started) - [Tech Stack](#tech-stack) - [Build Pipeline](#build-pipeline) - [Architecture](#architecture) - [Data Flows](#data-flows) - [Architectural Patterns](#architectural-patterns) -…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/ui/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/ui/README.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/tts/README.md`
- **Raw:** `[[raw/local/readme-76080240a3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp/example/tts This example demonstrates the Text To Speech feature. It uses a [model](https://www.outeai.com/blog/outetts-0.2-500m) from [outeai](https://www.outeai.com/). ## Quickstart If you have built llama.cpp with SSL support you can simply run the following command and the required models will be downloaded automatically: For details about the models and how to convert them to the required format see the following sections. ### Model conversion Checkout or download the model that contains the LLM model: Convert the model to .gguf format: The generated model will be `models/outetts-0.2-0.5B-f16.gguf`. We can optionally quantize this to Q8_0 using the following command: The…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/tts/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/tts/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/tts/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/tts/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-66f37d1f9b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-tts) add_executable(${TARGET} tts.cpp) target_link_libraries(${TARGET} PRIVATE llama llama-common ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/tts/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/tts/CMakeLists.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/tokenize/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-075b45f711.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-tokenize) add_executable(${TARGET} tokenize.cpp) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif() target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/tokenize/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/tokenize/CMakeLists.txt`

### requirements
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/bench/speed-bench/requirements.txt`
- **Raw:** `[[raw/local/requirements-af61baf90f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** datasets requests tqdm

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/server/bench/speed-bench/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/server/bench/speed-bench/requirements.txt`

### requirements
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/bench/requirements.txt`
- **Raw:** `[[raw/local/requirements-105cc90e67.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** matplotlib requests

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/server/bench/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/bench/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/server/bench/requirements.txt`

### prometheus
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/bench/prometheus.yml`
- **Raw:** `[[raw/local/prometheus-d03d04a5a5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** global: scrape_interval: 10s external_labels: llamacpp: 'server' scrape_configs: - job_name: 'llama.cpp server' static_configs: - targets: ['localhost:8080']

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/server/bench/prometheus.yml`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/bench/prometheus.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/server/bench/prometheus.yml`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/bench/speed-bench/README.md`
- **Raw:** `[[raw/local/readme-ffccdcd0d8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # SPEED-Bench server benchmark A lightweight [SPEED-Bench](https://huggingface.co/datasets/nvidia/SPEED-Bench) client for benchmarking an already-running `llama-server` through its OpenAI-compatible API. It is primarily meant to evaluate speculative decoding (draft model, n-gram, MTP, EAGLE3, ...) by reporting per-category throughput, latency, and draft acceptance. The dataset handling follows the [aiperf SPEED-Bench tutorial](https://github.com/ai-dynamo/aiperf/blob/main/docs/tutorials/speed-bench.md), which also documents the dataset layout in more detail. ## Install ## Start a server The client does not launch the server, so start `llama-server` yourself first. If you care about…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/server/bench/speed-bench/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/server/bench/speed-bench/README.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/README.md`
- **Raw:** `[[raw/local/readme-693d96e3be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLaMA.cpp HTTP Server Fast, lightweight, pure C/C++ HTTP server based on [httplib](https://github.com/yhirose/cpp-httplib), [nlohmann::json](https://github.com/nlohmann/json) and **llama.cpp**. Set of LLM REST APIs and a web UI to interact with llama.cpp. **Features:** * LLM inference of F16 and quantized models on GPU and CPU * [OpenAI API](https://github.com/openai/openai-openapi) compatible chat completions, responses, and embeddings routes * [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) compatible chat completions * Reranking endpoint (https://github.com/ggml-org/llama.cpp/pull/9510) * Parallel decoding with multi-user support * Continuous batching * Multimodal…

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/bench/README.md`
- **Raw:** `[[raw/local/readme-9edf7b9488.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ### Server benchmark tools Benchmark is using [k6](https://k6.io/). ##### Install k6 and sse extension SSE is not supported by default in k6, you have to build k6 with the [xk6-sse](https://github.com/phymbert/xk6-sse) extension. Example (assuming golang >= 1.21 is installed): #### Download a dataset This dataset was originally proposed in [vLLM benchmarks](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md). #### Download a model Example for PHI-2 #### Start the server The server must answer OAI Chat completion requests on `http://localhost:8080/v1` or according to the environment variable `SERVER_BENCH_URL`. Example: #### Run the benchmark For 500 chat completions request…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/server/bench/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/server/bench/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/server/bench/README.md`

### README-dev
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/README-dev.md`
- **Raw:** `[[raw/local/readme-dev-7a5bc7e706.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-server Development Documentation This document provides an in-depth technical overview of `llama-server`, intended for maintainers and contributors. If you are an end user consuming `llama-server` as a product, please refer to the main [README](./README.md) instead. ## Scope of features In-scope types of feature: - Backend: - Basic inference features: text completion, embeddings output - Chat-oriented features: chat completion, tool calling - Third-party API compatibility, e.g. OAI-compat, Anthropic-compat - Multimodal input/output - Memory management: save/load state, context checkpoints - Model management - Features that are required by the Web UI - Frontend: - Chat-oriented…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-atomic/tools/server/README-dev.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/server/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-1c1fb72366.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR}) # server-context containing the core server logic, used by llama-server and CLI set(TARGET server-context) add_library(${TARGET} STATIC server-chat.cpp server-chat.h server-task.cpp server-task.h server-queue.cpp server-queue.h server-common.cpp server-common.h server-context.cpp server-context.h server-loop-guard.cpp server-loop-guard.h server-tools.cpp server-tools.h ) if (BUILD_SHARED_LIBS) set_target_properties(${TARGET} PROPERTIES POSITION_INDEPENDENT_CODE ON) endif() target_include_directories(${TARGET} PRIVATE ../mtmd) target_include_directories(${TARGET} PRIVATE ${CMAKE_SOURCE_DIR})…

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/rpc/README.md`
- **Raw:** `[[raw/local/readme-fc88770904.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Overview > [!IMPORTANT] > This example and the RPC backend are currently in a proof-of-concept development stage. As such, the functionality is fragile and > insecure. **Never run the RPC server on an open network or in a sensitive environment!** The `rpc-server` allows exposing `ggml` devices on a remote host. The RPC backend communicates with one or several instances of `rpc-server` and offloads computations to them. This can be used for distributed LLM inference with `llama.cpp` in the following way: By default, `rpc-server` exposes all available accelerator devices on the host. If there are no accelerators, it exposes a single `CPU` device. ## Usage ### Remote hosts On each remote…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-atomic/tools/rpc/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/rpc/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-92a073869e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET rpc-server) add_executable(${TARGET} rpc-server.cpp) target_link_libraries(${TARGET} PRIVATE ggml) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/rpc/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/rpc/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/results/README.md`
- **Raw:** `[[raw/local/readme-e91afff9a7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Results The `llama-results` tool can be used to `--check` the outputs of a model vs. a previous commit to detect whether they have changed. Example usage: The metric by which the results are compared is the normalized mean squared error (NMSE) with a tolerance of $10^{-6}$.

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/results/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/results/README.md`, `local:projects/LLM-Infra/llama.cpp/tools/results/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/results/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-e109983692.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-results) add_executable(${TARGET} results.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/results/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/results/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/quantize/README.md`
- **Raw:** `[[raw/local/readme-99f539f710.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # quantize This tool takes a GGUF input model file, typically in a high-precision format like F32 or BF16, and converts it to a quantized format. Quantization reduces the precision of model weights (e.g., from 32-bit floats to 4-bit integers), which shrinks the model's size and can speed up inference. This process however, may introduce some accuracy loss which is usually measured in [Perplexity](https://huggingface.co/docs/transformers/en/perplexity) (ppl) and/or [Kullback–Leibler Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) (kld). This can be minimized by using a suitable imatrix file. You can also use the…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/quantize/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/quantize/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-6c83d54340.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-quantize-impl: quantize logic, reusable by app set(TARGET llama-quantize-impl) add_library(${TARGET} quantize.cpp) set_target_properties(${TARGET} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON) target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}) target_link_libraries(${TARGET} PUBLIC llama-common llama ${CMAKE_THREAD_LIBS_INIT}) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} LIBRARY) endif() # llama-quantize executable set(TARGET llama-quantize) add_executable(${TARGET} main.cpp) target_link_libraries(${TARGET} PRIVATE llama-quantize-impl) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/quantize/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/quantize/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/perplexity/README.md`
- **Raw:** `[[raw/local/readme-6f2fc09eed.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Perplexity The `perplexity` example can be used to calculate the so-called perplexity value of a language model over a given text corpus. Perplexity measures how well the model can predict the next token with lower values being better. Note that perplexity is **not** directly comparable between models, especially if they use different tokenizers. Also note that finetunes typically result in a higher perplexity value even though the human-rated quality of outputs increases. Within llama.cpp the perplexity of base models is used primarily to judge the quality loss from e.g. quantized models vs. FP16. The convention among contributors is to use the Wikitext-2 test set for testing unless…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/perplexity/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/perplexity/README.md`, `local:projects/LLM-Infra/llama.cpp/tools/perplexity/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/perplexity/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-5667e9fd89.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-perplexity-impl: perplexity logic, reusable by app set(TARGET llama-perplexity-impl) add_library(${TARGET} perplexity.cpp) set_target_properties(${TARGET} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON) target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}) target_link_libraries(${TARGET} PUBLIC llama-common llama ${CMAKE_THREAD_LIBS_INIT}) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} LIBRARY) endif() # llama-perplexity executable set(TARGET llama-perplexity) add_executable(${TARGET} main.cpp) target_link_libraries(${TARGET} PRIVATE llama-perplexity-impl) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME)…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/perplexity/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/perplexity/CMakeLists.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/parser/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-a783ea61cf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** if (NOT WIN32 OR NOT BUILD_SHARED_LIBS) # this tool is disabled on Windows when building with shared libraries because it uses internal functions not exported with LLAMA_API set(TARGET llama-debug-template-parser) add_executable(${TARGET} debug-template-parser.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif() endif() set(TARGET llama-template-analysis) add_executable(${TARGET} template-analysis.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/parser/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/parser/CMakeLists.txt`

### requirements
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/mtmd/requirements.txt`
- **Raw:** `[[raw/local/requirements-f1eda24cfe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** -r ../../requirements/requirements-convert_legacy_llama.txt --extra-index-url https://download.pytorch.org/whl/cpu pillow~=11.3.0 ## Embedding Gemma requires PyTorch 2.6.0 or later, bumped to 2.11.0 for compatibility torch==2.11.0; platform_machine != "s390x" # check_requirements: ignore "==" torchvision==0.26.0; platform_machine != "s390x" # check_requirements: ignore "==" # torch s390x packages can only be found from nightly builds --extra-index-url https://download.pytorch.org/whl/nightly torch>=0.0.0.dev0; platform_machine == "s390x" # check_requirements: ignore "==" torchvision>=0.0.0.dev0; platform_machine == "s390x" # check_requirements: ignore "=="

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/mtmd/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/mtmd/requirements.txt`

### mtmd-debug
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/mtmd/debug/mtmd-debug.md`
- **Raw:** `[[raw/local/mtmd-debug-197063cd54.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # mtmd-debug ## Debugging encode pass Example of debugging an input gray image (raw, not preprocessed): Example of debugging a rainbow image: ## Debugging preprocess pass (TODO)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/mtmd/debug/mtmd-debug.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/mtmd/debug/mtmd-debug.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/mtmd/README.md`
- **Raw:** `[[raw/local/readme-5821ef5257.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Multimodal Support in llama.cpp This directory provides multimodal capabilities for `llama.cpp`. Initially intended as a showcase for running LLaVA models, its scope has expanded significantly over time to include various other vision-capable models. As a result, LLaVA is no longer the only multimodal architecture supported. > [!IMPORTANT] > > Multimodal support can be viewed as a sub-project within `llama.cpp`. It is under **very heavy development**, and **breaking changes are expected**. The naming and structure related to multimodal support have evolved, which might cause some confusion. Here's a brief timeline to clarify: - [#3436](https://github.com/ggml-org/llama.cpp/pull/3436):…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/mtmd/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/mtmd/README.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/llama-bench/README.md`
- **Raw:** `[[raw/local/readme-3309619e3a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp/tools/llama-bench Performance testing tool for llama.cpp. ## Table of contents 1. [Syntax](#syntax) 2. [Examples](#examples) 1. [Text generation with different models](#text-generation-with-different-models) 2. [Prompt processing with different batch sizes](#prompt-processing-with-different-batch-sizes) 3. [Different numbers of threads](#different-numbers-of-threads) 4. [Different numbers of layers offloaded to the GPU](#different-numbers-of-layers-offloaded-to-the-gpu) 3. [Output formats](#output-formats) 1. [Markdown](#markdown) 2. [CSV](#csv) 3. [JSON](#json) 4. [JSONL](#jsonl) 5. [SQL](#sql) ## Syntax llama-bench can perform three types of tests: - Prompt processing (pp):…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/llama-bench/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/llama-bench/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/mtmd/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-cf6f8285f0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # mtmd find_package(Threads REQUIRED) add_library(mtmd mtmd.cpp mtmd-audio.cpp mtmd-image.cpp mtmd.h mtmd-helper.cpp mtmd-helper.h clip.cpp clip.h clip-impl.h clip-model.h clip-graph.h models/models.h models/cogvlm.cpp models/conformer.cpp models/dotsocr.cpp models/exaone4_5.cpp models/gemma4a.cpp models/gemma4v.cpp models/gemma4ua.cpp models/gemma4uv.cpp models/glm4v.cpp models/granite-speech.cpp models/hunyuanvl.cpp models/internvl.cpp models/kimivl.cpp models/kimik25.cpp models/nemotron-v2-vl.cpp models/llama4.cpp models/llava.cpp models/minicpmv.cpp models/paddleocr.cpp models/pixtral.cpp models/qwen2vl.cpp models/qwen3vl.cpp models/mimovl.cpp models/qwen3a.cpp models/step3vl.cpp…

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/llama-bench/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-0d3c923bfc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-bench-impl: benchmark logic, reusable by app set(TARGET llama-bench-impl) add_library(${TARGET} llama-bench.cpp) set_target_properties(${TARGET} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON) target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}) target_link_libraries(${TARGET} PUBLIC llama-common llama ${CMAKE_THREAD_LIBS_INIT}) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} LIBRARY) endif() # llama-bench executable set(TARGET llama-bench) add_executable(${TARGET} main.cpp) target_link_libraries(${TARGET} PRIVATE llama-bench-impl) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/llama-bench/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/llama-bench/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/imatrix/README.md`
- **Raw:** `[[raw/local/readme-35223ad9d7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp/tools/imatrix Compute an importance matrix for a model and given text dataset. Can be used during quantization to enhance the quality of the quantized models. More information is available in <https://github.com/ggml-org/llama.cpp/pull/4861>. ## Usage Here `-m | --model` with a model name and `-f | --file` with a file containing calibration data (such as e.g. `wiki.train.raw`) are mandatory. The parameters in square brackets are optional and have the following meaning: * `-h | --help` shows usage information and exits. * `-lv | --verbosity` specifies the verbosity level. If set to `0`, no output other than the perplexity of the processed chunks will be generated. If set to `1`,…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/imatrix/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/imatrix/README.md`, `local:projects/LLM-Infra/llama.cpp/tools/imatrix/README.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/gguf-split/README.md`
- **Raw:** `[[raw/local/readme-26d2d3060b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## GGUF split Example CLI to split / merge GGUF files. **Command line options:** - `--split`: split GGUF to multiple GGUF, default operation. - `--split-max-size`: max size per split in `M` or `G`, f.ex. `500M` or `2G`. - `--split-max-tensors`: maximum tensors in each split: default(128) - `--merge`: merge multiple GGUF to a single GGUF. You only need to specify the name of the first GGUF to merge, the name of the merged GGUF, and the CLI will find the other GGUFs it needs within the same folder.

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/gguf-split/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/gguf-split/README.md`, `local:projects/LLM-Infra/llama.cpp/tools/gguf-split/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/imatrix/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-6c0fe64d9a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-imatrix) add_executable(${TARGET} imatrix.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif() if (CMAKE_SYSTEM_NAME MATCHES "AIX") # AIX's flock() function comes from libbsd.a target_link_libraries(${TARGET} PRIVATE -lbsd) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/imatrix/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/imatrix/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/fit-params/README.md`
- **Raw:** `[[raw/local/readme-4950933db9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # fit-params llama.cpp binaries can automatically fit the projected memory use of a model to the free device memory available at runtime, this is controlled using the CLI arguments starting with `-fit`/`--fit`. Internally the code is calling `llama_params_fit` to adjust the `llama_model_params` and `llama_context_params` structs. `llama-fit-params` is a simple utility that prints the CLI arguments corresponding to these adjustments to stdout. Example usage:

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/fit-params/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/fit-params/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/fit-params/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/gguf-split/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-82a4bacd33.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-gguf-split) add_executable(${TARGET} gguf-split.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/gguf-split/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/gguf-split/CMakeLists.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/fit-params/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-c4824a2ee4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-fit-params-impl: fit-params logic, reusable by app set(TARGET llama-fit-params-impl) add_library(${TARGET} fit-params.cpp) set_target_properties(${TARGET} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON) target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}) target_link_libraries(${TARGET} PUBLIC llama-common llama ${CMAKE_THREAD_LIBS_INIT}) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} LIBRARY) endif() # llama-fit-params executable set(TARGET llama-fit-params) add_executable(${TARGET} main.cpp) target_link_libraries(${TARGET} PRIVATE llama-fit-params-impl) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME)…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/fit-params/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/fit-params/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/export-lora/README.md`
- **Raw:** `[[raw/local/readme-229f686446.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # export-lora Apply LORA adapters to base model and export the resulting model. For example: Multiple LORA adapters can be applied by passing multiple `--lora FNAME` or `--lora-scaled FNAME S` command line parameters:

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/tools/export-lora/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/export-lora/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/export-lora/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-e86289a064.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-export-lora) add_executable(${TARGET} export-lora.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/export-lora/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/export-lora/CMakeLists.txt`

### negative
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/cvector-generator/negative.txt`
- **Raw:** `[[raw/local/negative-cde127568e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <|start_header_id|>system<|end_header_id|>\n\nAct like a person who is extremely sad<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nWho are you?<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nI feel like there's a heavy weight on my chest <|start_header_id|>system<|end_header_id|>\n\nAct like a person who is extremely sad<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nHello<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nMy heart feels like it's drowning in sorrow <|start_header_id|>system<|end_header_id|>\n\nYou are in a very bad mood<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nHi<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nGo away!…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/cvector-generator/negative.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/cvector-generator/negative.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/cvector-generator/negative.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/cvector-generator/README.md`
- **Raw:** `[[raw/local/readme-580d4b9585.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # cvector-generator This example demonstrates how to generate a control vector using gguf models. Related PRs: - [Add support for control vectors](https://github.com/ggml-org/llama.cpp/pull/5970) - (Issue) [Generate control vector using llama.cpp](https://github.com/ggml-org/llama.cpp/issues/6880) - [Add cvector-generator example](https://github.com/ggml-org/llama.cpp/pull/7514) ## Examples ## Tips and tricks If you have multiple lines per prompt, you can escape the newline character (change it to `\n`). For example: Example to use output file with `llama-cli`: (Tips: The control vector works better when apply to layers higher than 10)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/cvector-generator/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/cvector-generator/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/cvector-generator/README.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/completion/README.md`
- **Raw:** `[[raw/local/readme-6f7e64e032.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp/tools/completion This example program allows you to use various LLaMA language models easily and efficiently. It is specifically designed to work with the [llama.cpp](https://github.com/ggml-org/llama.cpp) project, which provides a plain C/C++ implementation with optional 4-bit quantization support for faster, lower memory inference, and is optimized for desktop CPUs. This program can be used to perform various inference tasks with LLaMA models, including generating text based on user-provided prompts and chat-like interactions with reverse prompts. ## Table of Contents 1. [Quick Start](#quick-start) 2. [Usage](#usage) 3. [Common Options](#common-options) 4. [Input…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/completion/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/completion/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/cvector-generator/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-40b16b58e0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-cvector-generator) add_executable(${TARGET} cvector-generator.cpp pca.hpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/cvector-generator/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/cvector-generator/CMakeLists.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/completion/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-e0d4a61bfa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-completion-impl: completion logic, reusable by app set(TARGET llama-completion-impl) add_library(${TARGET} completion.cpp) set_target_properties(${TARGET} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON) target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}) target_link_libraries(${TARGET} PUBLIC llama-common llama ${CMAKE_THREAD_LIBS_INIT}) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} LIBRARY) endif() # llama-completion executable set(TARGET llama-completion) add_executable(${TARGET} main.cpp) target_link_libraries(${TARGET} PRIVATE llama-completion-impl) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME)…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/completion/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/completion/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/cli/README.md`
- **Raw:** `[[raw/local/readme-dd3d4e6546.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp/tools/cli ## Usage <!-- HELP_START --> <!-- IMPORTANT: The list below is auto-generated by llama-gen-docs; do NOT modify it manually --> ### Common params | Argument | Explanation | | -------- | ----------- | | `-h, --help, --usage` | print usage and exit | | `--version` | show version and build info | | `-cl, --cache-list` | show list of models in cache | | `--completion-bash` | print source-able bash completion script for llama.cpp | | `-t, --threads N` | number of CPU threads to use during generation (default: -1)<br/>(env: LLAMA_ARG_THREADS) | | `-tb, --threads-batch N` | number of threads to use during batch and prompt processing (default: same as --threads) | | `-C,…

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/cli/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-a3cecb7f5f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-cli-impl: CLI logic, reusable by app set(TARGET llama-cli-impl) add_library(${TARGET} cli.cpp) set_target_properties(${TARGET} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON) target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} ../server) target_link_libraries(${TARGET} PUBLIC server-context llama-common ${CMAKE_THREAD_LIBS_INIT}) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} LIBRARY) endif() # llama-cli executable set(TARGET llama-cli) add_executable(${TARGET} main.cpp) target_link_libraries(${TARGET} PRIVATE llama-cli-impl) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} RUNTIME) endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/cli/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/cli/CMakeLists.txt`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/batched-bench/README.md`
- **Raw:** `[[raw/local/readme-db9158e439.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp/example/batched-bench Benchmark the batched decoding performance of `llama.cpp` ## Usage There are 2 modes of operation: - `prompt not shared` - each batch has a separate prompt of size `PP` (i.e. `N_KV = B*(PP + TG)`) - `prompt is shared` - there is a common prompt of size `PP` used by all batches (i.e. `N_KV = PP + B*TG`) ## Sample results - `PP` - prompt tokens per batch - `TG` - generated tokens per batch - `B` - number of batches - `N_KV` - required KV cache size - `T_PP` - prompt processing time (i.e. time to first token) - `S_PP` - prompt processing speed (`(B*PP)/T_PP` or `PP/T_PP`) - `T_TG` - time to generate all batches - `S_TG` - text generation speed (`(B*TG)/T_TG`)…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/batched-bench/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/batched-bench/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/batched-bench/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/batched-bench/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-6ab4f1741f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-batched-bench-impl: batched-bench logic, reusable by app set(TARGET llama-batched-bench-impl) add_library(${TARGET} batched-bench.cpp) set_target_properties(${TARGET} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON) target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}) target_link_libraries(${TARGET} PUBLIC llama-common llama ${CMAKE_THREAD_LIBS_INIT}) if(LLAMA_TOOLS_INSTALL) install(TARGETS ${TARGET} LIBRARY) endif() # llama-batched-bench executable set(TARGET llama-batched-bench) add_executable(${TARGET} main.cpp) target_link_libraries(${TARGET} PRIVATE llama-batched-bench-impl) target_compile_features(${TARGET} PRIVATE cxx_std_17) if(LLAMA_TOOLS_INSTALL)…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/batched-bench/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/batched-bench/CMakeLists.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-d0b890e139.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # dependencies find_package(Threads REQUIRED) # third-party # ... # flags llama_add_compile_flags() # tools if (EMSCRIPTEN) else() add_subdirectory(batched-bench) add_subdirectory(gguf-split) add_subdirectory(imatrix) add_subdirectory(llama-bench) add_subdirectory(completion) add_subdirectory(perplexity) add_subdirectory(quantize) if (LLAMA_BUILD_SERVER) add_subdirectory(ui) add_subdirectory(cli) add_subdirectory(server) endif() add_subdirectory(tokenize) add_subdirectory(parser) add_subdirectory(tts) add_subdirectory(mtmd) if (GGML_RPC) add_subdirectory(rpc) endif() if (NOT GGML_BACKEND_DL) # these examples use the backends directly and cannot be built with dynamic loading…

### requirements
- **Source:** `local:projects/LLM-Infra/beellama.cpp/scripts/snapdragon/qdc/requirements.txt`
- **Raw:** `[[raw/local/requirements-0ba8b3f89b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Appium-Python-Client==5.2.4 attrs==25.4.0 certifi==2025.10.5 exceptiongroup==1.3.0 h11==0.16.0 idna==3.11 iniconfig==2.1.0 outcome==1.3.0.post0 packaging==25.0 pluggy==1.6.0 PySocks==1.7.1 pytest==8.4.2 selenium==4.36.0 sniffio==1.3.1 sortedcontainers==2.4.0 tomli==2.3.0 trio==0.31.0 trio-websocket==0.12.2 typing_extensions==4.15.0 urllib3==2.5.0 websocket-client==1.9.0 wsproto==1.2.0

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/scripts/snapdragon/qdc/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/scripts/snapdragon/qdc/requirements.txt`

### requirements
- **Source:** `local:projects/LLM-Infra/beellama.cpp/scripts/jinja/requirements.txt`
- **Raw:** `[[raw/local/requirements-51f5f1bc6f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** PySide6 jinja2

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/scripts/jinja/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/scripts/jinja/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/scripts/jinja/requirements.txt`

### requirements-convert_legacy_llama
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-convert_legacy_llama.txt`
- **Raw:** `[[raw/local/requirements-convert_legacy_llama-64e5b8f1be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** numpy~=1.26.4 sentencepiece>=0.1.98,<0.3.0 transformers==4.57.6 gguf>=0.1.0 protobuf>=4.21.0,<5.0.0

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-convert_legacy_llama.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-convert_legacy_llama.txt`

### requirements-tool_bench
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-tool_bench.txt`
- **Raw:** `[[raw/local/requirements-tool_bench-909df51cd9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** aiohttp~=3.9.3 pytest~=8.3.3 matplotlib~=3.10.0 numpy~=1.26.4 openai~=2.14.0 pandas~=2.2.3 prometheus-client~=0.20.0 requests~=2.32.3 wget~=3.2 typer~=0.24.1 seaborn~=0.13.2

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-tool_bench.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-tool_bench.txt`

### requirements-pydantic
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-pydantic.txt`
- **Raw:** `[[raw/local/requirements-pydantic-b3a9dde321.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** docstring_parser~=0.15 pydantic~=2.11.7 requests~=2.32.3

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-pydantic.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-pydantic.txt`, `local:projects/LLM-Infra/llama.cpp/requirements/requirements-pydantic.txt`

### requirements-convert_lora_to_gguf
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-convert_lora_to_gguf.txt`
- **Raw:** `[[raw/local/requirements-convert_lora_to_gguf-c7ea8e4c64.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** -r ./requirements-convert_hf_to_gguf.txt --extra-index-url https://download.pytorch.org/whl/cpu # torch s390x packages can only be found from nightly builds --extra-index-url https://download.pytorch.org/whl/nightly

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-convert_lora_to_gguf.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-convert_lora_to_gguf.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-convert_lora_to_gguf.txt`

### requirements-compare-llama-bench
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-compare-llama-bench.txt`
- **Raw:** `[[raw/local/requirements-compare-llama-bench-9df04bf6b7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** tabulate~=0.9.0 GitPython~=3.1.43 matplotlib~=3.10.0

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-compare-llama-bench.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-compare-llama-bench.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-compare-llama-bench.txt`

### requirements-gguf_editor_gui
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-gguf_editor_gui.txt`
- **Raw:** `[[raw/local/requirements-gguf_editor_gui-fcce14ea34.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** numpy~=1.26.4 PySide6~=6.9.0 gguf>=0.17.0

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-gguf_editor_gui.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-gguf_editor_gui.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-gguf_editor_gui.txt`

### requirements-convert_hf_to_gguf_update
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-convert_hf_to_gguf_update.txt`
- **Raw:** `[[raw/local/requirements-convert_hf_to_gguf_update-04fb9a4409.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** -r ./requirements-convert_legacy_llama.txt

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-convert_llama_ggml_to_gguf.txt`, `local:projects/LLM-Infra/llama.cpp/requirements/requirements-convert_hf_to_gguf_update.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-convert_llama_ggml_to_gguf.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-convert_hf_to_gguf_update.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-convert_llama_ggml_to_gguf.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-convert_hf_to_gguf_update.txt`, `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-convert_llama_ggml_to_gguf.txt`

### requirements-convert_hf_to_gguf
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-convert_hf_to_gguf.txt`
- **Raw:** `[[raw/local/requirements-convert_hf_to_gguf-d6ee53814f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** -r ./requirements-convert_legacy_llama.txt --extra-index-url https://download.pytorch.org/whl/cpu ## Embedding Gemma requires PyTorch 2.6.0 or later, bumped to 2.11.0 for compatibility torch==2.11.0; platform_machine != "s390x" # torch s390x packages can only be found from nightly builds --extra-index-url https://download.pytorch.org/whl/nightly torch>=0.0.0.dev0; platform_machine == "s390x"

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-convert_hf_to_gguf.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-convert_hf_to_gguf.txt`

### requirements-server-bench
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-server-bench.txt`
- **Raw:** `[[raw/local/requirements-server-bench-4035da5d30.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** datasets~=4.8.0 matplotlib~=3.10.0 numpy~=1.26.4 requests~=2.32.3 tqdm~=4.67.1

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-server-bench.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-server-bench.txt`

### requirements-test-tokenizer-random
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-test-tokenizer-random.txt`
- **Raw:** `[[raw/local/requirements-test-tokenizer-random-8fd5516e77.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** cffi~=1.16.0

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-test-tokenizer-random.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-test-tokenizer-random.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-test-tokenizer-random.txt`

### pyproject
- **Source:** `local:projects/LLM-Infra/beellama.cpp/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-dc8352c360.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [project] name = "llama-cpp-scripts" description = "Scripts that ship with llama.cpp" keywords = ["ggml", "gguf", "llama.cpp"] version = "0.0.0" dynamic = ["classifiers"] readme = "README.md" authors = [{name = "GGML", email = "ggml@ggml.ai"}] requires-python = '>=3.10,<3.15' dependencies = [ 'numpy (>=1.26.4,<3.0.0)', 'sentencepiece (>=0.1.98,<0.3.0)', 'transformers (==4.57.6)', 'protobuf (>=4.21.0,<5.0.0)', 'torch (>=2.6.0,<3.0.0)', 'gguf @ ./gguf-py', ] classifiers = [ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ] [project.urls] homepage = "https://ggml.ai" repository = "https://github.com/ggml-org/llama.cpp"…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/pyproject.toml`, `local:projects/LLM-Infra/llama.cpp-atomic/pyproject.toml`

### requirements
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements.txt`
- **Raw:** `[[raw/local/requirements-08e67179ad.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # These requirements include all dependencies for all top-level python scripts # for llama.cpp. Avoid adding packages here directly. # # Package versions must stay compatible across all top-level python scripts. # -r ./requirements/requirements-convert_legacy_llama.txt -r ./requirements/requirements-convert_hf_to_gguf.txt -r ./requirements/requirements-convert_hf_to_gguf_update.txt -r ./requirements/requirements-convert_llama_ggml_to_gguf.txt -r ./requirements/requirements-convert_lora_to_gguf.txt -r ./requirements/requirements-tool_bench.txt

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements.txt`

### requirements-all
- **Source:** `local:projects/LLM-Infra/beellama.cpp/requirements/requirements-all.txt`
- **Raw:** `[[raw/local/requirements-all-449994b485.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** -r ../tools/mtmd/requirements.txt -r ../tools/server/bench/requirements.txt -r ../tools/server/tests/requirements.txt -r ./requirements-compare-llama-bench.txt -r ./requirements-server-bench.txt -r ./requirements-pydantic.txt -r ./requirements-test-tokenizer-random.txt -r ./requirements-convert_hf_to_gguf.txt -r ./requirements-convert_hf_to_gguf_update.txt -r ./requirements-convert_legacy_llama.txt -r ./requirements-convert_llama_ggml_to_gguf.txt -r ./requirements-tool_bench.txt -r ./requirements-gguf_editor_gui.txt -r ../examples/model-conversion/requirements.txt

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/requirements/requirements-all.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/requirements/requirements-all.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/requirements/requirements-all.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/pocs/vdot/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-7aea4bb7bc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-vdot) add_executable(${TARGET} vdot.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17) set(TARGET llama-q8dot) add_executable(${TARGET} q8dot.cpp) target_link_libraries(${TARGET} PRIVATE llama-common llama ${CMAKE_THREAD_LIBS_INIT}) target_compile_features(${TARGET} PRIVATE cxx_std_17)

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/pocs/vdot/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/pocs/vdot/CMakeLists.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/pocs/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-24a96d9749.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # dependencies find_package(Threads REQUIRED) # third-party include_directories(${CMAKE_CURRENT_SOURCE_DIR}) if (EMSCRIPTEN) else() if (NOT GGML_BACKEND_DL) add_subdirectory(vdot) endif() endif()

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/pocs/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/pocs/CMakeLists.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/pocs/CMakeLists.txt`

### ubatch-vram-deflate
- **Source:** `local:projects/LLM-Infra/beellama.cpp/notes/ubatch-vram-deflate.md`
- **Raw:** `[[raw/local/ubatch-vram-deflate-0f5582823b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Ubatch VRAM Deflate — Investigation Notes ## Problem `-ub` (ubatch) size determines permanent VRAM usage because llama.cpp's `sched_reserve()` allocates compute buffers at init sized for the worst-case graph (n_ubatch tokens) and never frees them. - `-ub 512`: fast prefill, but ~2.5 GB more permanent VRAM - `-ub 64` (DFlash auto-cap): slow prefill, low VRAM - Users have to guess what fits — too high OOMs, too low wastes throughput ## Root Cause `src/llama-context.cpp:428`: `sched_reserve()` (line 414) builds a PP graph with n_ubatch tokens (line 585), allocates VRAM for all intermediate tensors, and keeps it forever. The attention intermediates scale O(n_tokens²) — 512 vs 64 is 64x in the…

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/models/templates/README.md`
- **Raw:** `[[raw/local/readme-fb0b5d38e4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** These templates can be updated with the following commands:

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/models/templates/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/models/templates/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/models/templates/README.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/grammars/README.md`
- **Raw:** `[[raw/local/readme-c89f49cd58.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GBNF Guide GBNF (GGML BNF) is a format for defining [formal grammars](https://en.wikipedia.org/wiki/Formal_grammar) to constrain model outputs in `llama.cpp`. For example, you can use it to force the model to generate valid JSON, or speak only in emojis. GBNF grammars are supported in various ways in `tools/cli`, `tools/completion` and `tools/server`. ## Background [Backus-Naur Form (BNF)](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) is a notation for describing the syntax of formal languages like programming languages, file formats, and protocols. GBNF is an extension of BNF that primarily adds a few modern regex-like features. ## Basics In GBNF, we define *production rules*…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-atomic/grammars/README.md`

### pyproject
- **Source:** `local:projects/LLM-Infra/beellama.cpp/gguf-py/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-820c0fa410.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [project] name = "gguf" version = "0.19.0" description = "Read and write ML models in GGUF for GGML" keywords = ["ggml", "gguf", "llama.cpp"] dynamic = ["classifiers"] readme = "README.md" authors = [{name = "GGML", email = "ggml@ggml.ai"}] requires-python = '>=3.10' dependencies = ['numpy (>=1.17)', 'tqdm (>=4.27)', 'pyyaml (>=5.1)', 'requests (>=2.25)'] classifiers = [ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ] [project.urls] homepage = "https://ggml.ai" repository = "https://github.com/ggml-org/llama.cpp" [project.scripts] gguf-convert-endian = "gguf.scripts.gguf_convert_endian:main" gguf-dump =…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/gguf-py/pyproject.toml`, `local:projects/LLM-Infra/llama.cpp-atomic/gguf-py/pyproject.toml`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/gguf-py/README.md`
- **Raw:** `[[raw/local/readme-f759ed01b8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## gguf This is a Python package for writing binary files in the [GGUF](https://github.com/ggml-org/ggml/pull/302) (GGML Universal File) format. See [convert_hf_to_gguf.py](https://github.com/ggml-org/llama.cpp/blob/master/convert_hf_to_gguf.py) as an example for its usage. ## Installation Optionally, you can install gguf with the extra 'gui' to enable the visual GGUF editor. ## API Examples/Simple Tools [examples/writer.py](https://github.com/ggml-org/llama.cpp/blob/master/gguf-py/examples/writer.py) — Generates `example.gguf` in the current directory to demonstrate generating a GGUF file. Note that this file cannot be used as a model.…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/gguf-py/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/gguf-py/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/gguf-py/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/ggml/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-ab5c237413.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** cmake_minimum_required(VERSION 3.14...3.28) # for add_link_options and implicit target directories. project("ggml" C CXX ASM) ### GGML Version set(GGML_VERSION_MAJOR 0) set(GGML_VERSION_MINOR 13) set(GGML_VERSION_PATCH 1) set(GGML_VERSION_BASE "${GGML_VERSION_MAJOR}.${GGML_VERSION_MINOR}.${GGML_VERSION_PATCH}") list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/") find_program(GIT_EXE NAMES git git.exe NO_CMAKE_FIND_ROOT_PATH) if(GIT_EXE) # Get current git commit hash execute_process(COMMAND ${GIT_EXE} rev-parse --short HEAD WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} OUTPUT_VARIABLE GGML_BUILD_COMMIT OUTPUT_STRIP_TRAILING_WHITESPACE ERROR_QUIET ) # Check if the working…

### quickstart-qwen36-dflash
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/quickstart-qwen36-dflash.md`
- **Raw:** `[[raw/local/quickstart-qwen36-dflash-689a11b7d3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Quickstart: Qwen 3.6 with DFlash on a Single GPU Run Qwen3.6-27B with DFlash speculative decoding in [BeeLlama.cpp](https://github.com/Anbeeld/beellama.cpp) on one NVIDIA GPU. This guide covers model download, binary setup, and a launch command tuned for a 24 GB VRAM card (RTX 3090, RTX 4090, A5000, etc.). DFlash is a speculative decoding mode where a small draft model reads recent hidden states from the target model and predicts multiple tokens ahead. The target model then verifies those predictions in a single forward pass. When the draft model is good, this produces multiple accepted tokens per target evaluation. ## Prerequisites **Hardware.** An NVIDIA GPU with at least 24 GB VRAM.…

### speculative
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/speculative.md`
- **Raw:** `[[raw/local/speculative-9431e77a2f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Speculative Decoding llama.cpp supports speculative decoding, a technique that can significantly accelerate token generation by predicting multiple tokens ahead of the main model. [Speculative decoding](https://en.wikipedia.org/wiki/Transformer_(deep_learning)#Speculative_decoding) leverages the fact that computing n tokens in a batch (as in prompt processing) is more efficient than computing n sequentially (as in response generation). By generating draft tokens quickly and then verifying them with the target model in a single batch, this approach can achieve substantial speedups when the draft predictions are frequently correct. ## Implementations The `llama-server` application supports…

### quickstart-gemma-4-31b-dflash
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/quickstart-gemma-4-31b-dflash.md`
- **Raw:** `[[raw/local/quickstart-gemma-4-31b-dflash-47a9f04ef9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Quickstart: Gemma 4 31B with DFlash on a Single GPU Run Gemma 4 31B IT with DFlash speculative decoding in [BeeLlama.cpp](https://github.com/Anbeeld/beellama.cpp) on one NVIDIA GPU. This guide covers model download, binary setup, and a launch command tuned for a 24 GB VRAM card (RTX 3090, RTX 4090, A5000, etc.). DFlash is a speculative decoding mode where a small draft model reads recent hidden states from the target model and predicts multiple tokens ahead. The target model then verifies those predictions in a single forward pass. When the draft model is good, this produces multiple accepted tokens per target evaluation. ## Prerequisites **Hardware.** An NVIDIA GPU with at least 24 GB…

### preset
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/preset.md`
- **Raw:** `[[raw/local/preset-be8aecfbae.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp INI Presets ## Introduction The INI preset feature, introduced in [PR#17859](https://github.com/ggml-org/llama.cpp/pull/17859), allows users to create reusable and shareable parameter configurations for llama.cpp. ### Using Presets with the Server When running multiple models on the server (router mode), INI preset files can be used to configure model-specific parameters. Please refer to the [server documentation](../tools/server/README.md) for more details. ### Using a Remote Preset > [!NOTE] > > This feature is currently only supported via the `-hf` option. For GGUF models hosted on Hugging Face, you can include a `preset.ini` file in the root directory of the repository to…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/preset.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/preset.md`

### ops
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/ops.md`
- **Raw:** `[[raw/local/ops-143144fb02.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GGML Operations List of GGML operations and backend support status. ## How to add a backend to this table: 1. Run `test-backend-ops support --output csv` with your backend name and redirect output to a csv file in `docs/ops/` (e.g., `docs/ops/CUDA.csv`) 2. Regenerate `/docs/ops.md` via `./scripts/create_ops_docs.py` Legend: - ✅ Fully supported by this backend - 🟡 Partially supported by this backend - ❌ Not supported by this backend | Operation | BLAS | CANN | CPU | CUDA | MTL | OpenCL | SYCL | Vulkan | WebGPU | ZenDNN | zDNN | |-----------|------|------|------|------|------|------|------|------|------|------|------| | ABS | ❌ | ✅ | ✅ | 🟡 | ✅ | ❌ | ✅ | 🟡 | ✅ | ❌ | ❌ | | ACC | ❌ | ✅ | ✅ | ✅…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-atomic/docs/ops.md`

### minicpmo4.0
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/minicpmo4.0.md`
- **Raw:** `[[raw/local/minicpmo4.0-257538f564.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## MiniCPM-o 4 ### Prepare models and code Download [MiniCPM-o-4](https://huggingface.co/openbmb/MiniCPM-o-4) PyTorch model from huggingface to "MiniCPM-o-4" folder. ### Build llama.cpp Readme modification time: 20250206 If there are differences in usage, please refer to the official build [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) Clone llama.cpp: Build llama.cpp using `CMake`: ### Usage of MiniCPM-o 4 Convert PyTorch model to gguf files (You can also download the converted [gguf](https://huggingface.co/openbmb/MiniCPM-o-4-gguf) by us) Inference on Linux or Mac

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/minicpmo4.0.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/minicpmo4.0.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/minicpmo4.0.md`

### minicpmo2.6
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/minicpmo2.6.md`
- **Raw:** `[[raw/local/minicpmo2.6-78b99bc806.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## MiniCPM-o 2.6 Currently, this readme only supports minicpm-omni's image capabilities, and we will update the full-mode support as soon as possible. ### Prepare models and code Download [MiniCPM-o-2_6](https://huggingface.co/openbmb/MiniCPM-o-2_6) PyTorch model from huggingface to "MiniCPM-o-2_6" folder. ### Build llama.cpp Readme modification time: 20250206 If there are differences in usage, please refer to the official build [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) Clone llama.cpp: Build llama.cpp using `CMake`: ### Usage of MiniCPM-o 2.6 Convert PyTorch model to gguf files (You can also download the converted…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/minicpmo2.6.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/minicpmo2.6.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/minicpmo2.6.md`

### minicpmv4.5
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/minicpmv4.5.md`
- **Raw:** `[[raw/local/minicpmv4.5-9bfe076a2a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## MiniCPM-V 4.5 ### Prepare models and code Download [MiniCPM-V-4_5](https://huggingface.co/openbmb/MiniCPM-V-4_5) PyTorch model from huggingface to "MiniCPM-V-4_5" folder. ### Build llama.cpp Readme modification time: 20250826 If there are differences in usage, please refer to the official build [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) Clone llama.cpp: Build llama.cpp using `CMake`: ### Usage of MiniCPM-V 4 Convert PyTorch model to gguf files (You can also download the converted [gguf](https://huggingface.co/openbmb/MiniCPM-V-4_5-gguf) by us) Inference on Linux or Mac

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/minicpmv4.5.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/minicpmv4.5.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/minicpmv4.5.md`

### minicpmv4.6
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/minicpmv4.6.md`
- **Raw:** `[[raw/local/minicpmv4.6-aff69f645e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## MiniCPM-V 4.6 ### Prepare models and code Download [MiniCPM-V-4_6](https://huggingface.co/openbmb/MiniCPM-V-4_6) PyTorch model from huggingface to "MiniCPM-V-4_6" folder. The model must be the standard `transformers` v5.7.0+ checkpoint (no `trust_remote_code`); the architecture in `config.json` is `MiniCPMV4_6ForConditionalGeneration` with a `qwen3_5_text` text model and a SigLIP-based vision tower plus a window-attention `vit_merger`. ### Build llama.cpp If there are differences in usage, please refer to the official build [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) Clone llama.cpp: Build llama.cpp using `CMake`: ### Usage of MiniCPM-V 4.6 Unlike…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/minicpmv4.6.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/minicpmv4.6.md`

### minicpmv2.5
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/minicpmv2.5.md`
- **Raw:** `[[raw/local/minicpmv2.5-9f8434250b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## MiniCPM-Llama3-V 2.5 ### Prepare models and code Download [MiniCPM-Llama3-V-2_5](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5) PyTorch model from huggingface to "MiniCPM-Llama3-V-2_5" folder. ### Build llama.cpp Readme modification time: 20250206 If there are differences in usage, please refer to the official build [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) Clone llama.cpp: Build llama.cpp using `CMake`: ### Usage of MiniCPM-Llama3-V 2.5 Convert PyTorch model to gguf files (You can also download the converted [gguf](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5-gguf) by us) Inference on Linux or Mac

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/minicpmv2.5.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/minicpmv2.5.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/minicpmv2.5.md`

### minicpmv2.6
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/minicpmv2.6.md`
- **Raw:** `[[raw/local/minicpmv2.6-b56fbceac9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## MiniCPM-V 2.6 ### Prepare models and code Download [MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6) PyTorch model from huggingface to "MiniCPM-V-2_6" folder. ### Build llama.cpp Readme modification time: 20250206 If there are differences in usage, please refer to the official build [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) Clone llama.cpp: Build llama.cpp using `CMake`: ### Usage of MiniCPM-V 2.6 Convert PyTorch model to gguf files (You can also download the converted [gguf](https://huggingface.co/openbmb/MiniCPM-V-2_6-gguf) by us) Inference on Linux or Mac

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/minicpmv2.6.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/minicpmv2.6.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/minicpmv2.6.md`

### minicpmv4.0
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/minicpmv4.0.md`
- **Raw:** `[[raw/local/minicpmv4.0-d4d4abda08.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## MiniCPM-V 4 ### Prepare models and code Download [MiniCPM-V-4](https://huggingface.co/openbmb/MiniCPM-V-4) PyTorch model from huggingface to "MiniCPM-V-4" folder. ### Build llama.cpp Readme modification time: 20250731 If there are differences in usage, please refer to the official build [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) Clone llama.cpp: Build llama.cpp using `CMake`: ### Usage of MiniCPM-V 4 Convert PyTorch model to gguf files (You can also download the converted [gguf](https://huggingface.co/openbmb/MiniCPM-V-4-gguf) by us) Inference on Linux or Mac

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/minicpmv4.0.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/minicpmv4.0.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/minicpmv4.0.md`

### llava
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/llava.md`
- **Raw:** `[[raw/local/llava-8e6f216b75.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLaVA Currently this implementation supports [llava-v1.5](https://huggingface.co/liuhaotian/llava-v1.5-7b) variants, as well as llava-1.6 [llava-v1.6](https://huggingface.co/collections/liuhaotian/llava-16-65b9e40155f60fd046a5ccf2) variants. The pre-converted [7b](https://huggingface.co/mys/ggml_llava-v1.5-7b) and [13b](https://huggingface.co/mys/ggml_llava-v1.5-13b) models are available. For llava-1.6 a variety of prepared gguf models are available as well [7b-34b](https://huggingface.co/cmp-nct/llava-1.6-gguf) After API is confirmed, more models will be supported / uploaded. ## Usage Build the `llama-mtmd-cli` binary. After building, run: `./llama-mtmd-cli` to see the usage. For…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/llava.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/llava.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/llava.md`

### glmedge
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/glmedge.md`
- **Raw:** `[[raw/local/glmedge-436fd6e282.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GLMV-EDGE Currently this implementation supports [glm-edge-v-2b](https://huggingface.co/THUDM/glm-edge-v-2b) and [glm-edge-v-5b](https://huggingface.co/THUDM/glm-edge-v-5b). ## Usage Build the `llama-mtmd-cli` binary. After building, run: `./llama-mtmd-cli` to see the usage. For example: **note**: A lower temperature like 0.1 is recommended for better quality. add `--temp 0.1` to the command to do so. **note**: For GPU offloading ensure to use the `-ngl` flag just like usual ## GGUF conversion 1. Clone a GLMV-EDGE model ([2B](https://huggingface.co/THUDM/glm-edge-v-2b) or [5B](https://huggingface.co/THUDM/glm-edge-v-5b)). For example: 2. Use `glmedge-surgery.py` to split the GLMV-EDGE…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/glmedge.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/glmedge.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/glmedge.md`

### gemma3
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/gemma3.md`
- **Raw:** `[[raw/local/gemma3-57e49f25cd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Gemma 3 vision > [!IMPORTANT] > > This is very experimental, only used for demo purpose. ## Quick started You can use pre-quantized model from [ggml-org](https://huggingface.co/ggml-org)'s Hugging Face account ## How to get mmproj.gguf? Simply to add `--mmproj` in when converting model via `convert_hf_to_gguf.py`: ## How to run it? What you need: - The text model GGUF, can be converted using `convert_hf_to_gguf.py` - The mmproj file from step above - An image file

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/gemma3.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/gemma3.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/gemma3.md`

### granitevision
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/granitevision.md`
- **Raw:** `[[raw/local/granitevision-95f41c12db.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Granite Vision Download the model and point your `GRANITE_MODEL` environment variable to the path. ### 1. Running llava surgery v2. First, we need to run the llava surgery script as shown below: `python llava_surgery_v2.py -C -m $GRANITE_MODEL` You should see two new files (`llava.clip` and `llava.projector`) written into your model's directory, as shown below. We should see that the projector and visual encoder get split out into the llava files. Quick check to make sure they aren't empty: If you actually inspect the `.keys()` of the loaded tensors, you should see a lot of `vision_model` tensors in the `encoder_tensors`, and 5 tensors (`'multi_modal_projector.linear_1.bias'`,…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multimodal/granitevision.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/granitevision.md`

### install
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/install.md`
- **Raw:** `[[raw/local/install-02b4029d80.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Install pre-built version of llama.cpp | Install via | Windows | Mac | Linux | |-------------|---------|-----|-------| | Winget | ✅ | | | | Homebrew | | ✅ | ✅ | | MacPorts | | ✅ | | | Nix | | ✅ | ✅ | ## Winget (Windows) The package is automatically updated with new `llama.cpp` releases. More info: https://github.com/ggml-org/llama.cpp/issues/8188 ## Homebrew (Mac and Linux) The formula is automatically updated with new `llama.cpp` releases. More info: https://github.com/ggml-org/llama.cpp/discussions/7668 ## MacPorts (Mac) See also: https://ports.macports.org/port/llama.cpp/details/ ## Nix (Mac and Linux) For flake enabled installs. Or For non-flake enabled installs. This expression is…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/install.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/install.md`

### llguidance
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/llguidance.md`
- **Raw:** `[[raw/local/llguidance-ef304ff3a7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLGuidance Support in llama.cpp [LLGuidance](https://github.com/guidance-ai/llguidance) is a library for constrained decoding (also called constrained sampling or structured outputs) for Large Language Models (LLMs). Initially developed as the backend for the [Guidance](https://github.com/guidance-ai/guidance) library, it can also be used independently. LLGuidance supports JSON Schemas and arbitrary context-free grammars (CFGs) written in a [variant](https://github.com/guidance-ai/llguidance/blob/main/docs/syntax.md) of Lark syntax. It is [very fast](https://github.com/guidance-ai/jsonschemabench/tree/main/maskbench) and has…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/llguidance.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/llguidance.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/llguidance.md`

### multi-gpu
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multi-gpu.md`
- **Raw:** `[[raw/local/multi-gpu-08508e6764.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Using multiple GPUs with llama.cpp This guide explains how to run [llama.cpp](https://github.com/ggml-org/llama.cpp) across more than one GPU. It covers the split modes, the command-line flags that control them, the limitations you need to know about, and ready-to-use recipes for `llama-cli` and `llama-server`. The CLI arguments listed here are the same for both tools - or most llama.cpp binaries for that matter. --- ## When you need multi-GPU Reach for multi-GPU when one of these is true: - **The model doesn't fit in a single GPU's VRAM.** By spreading the weights across two or more GPUs the whole model can stay on accelerators. Otherwise part of the model will need to be run off of the…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/multi-gpu.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multi-gpu.md`

### docker
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/docker.md`
- **Raw:** `[[raw/local/docker-b6dfacc354.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Docker BeeLlama Docker images are published by the push/manual Docker workflow to `ghcr.io/anbeeld/beellama.cpp`. CUDA images are built from the stock `.devops/cuda.Dockerfile`; pass `CUDA_DOCKER_ARCH` when building locally for a specific GPU generation, for example `120` for Blackwell or `86` for RTX 3090. ## Prerequisites * Docker must be installed and running on your system. * Create a folder to store big models & intermediate files (ex. /llama/models) ## Images The CI workflow publishes `llama-server` images to `ghcr.io/anbeeld/beellama.cpp`: - `server` / `server-cpu`: CPU backend. (`linux/amd64`, `linux/arm64`) - `server-cuda` / `server-cuda12`: CUDA 12.4 backend. (`linux/amd64`) -…

### multimodal
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal.md`
- **Raw:** `[[raw/local/multimodal-71c51ac94b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Multimodal llama.cpp supports multimodal input via `libmtmd`. Currently, there are 2 tools support this feature: - [llama-mtmd-cli](../tools/mtmd/README.md) - [llama-server](../tools/server/README.md) via OpenAI-compatible `/chat/completions` API Currently, we support **image** and **audio** input. Audio is highly experimental and may have reduced quality. To enable it, you can use one of the 2 methods below: - Use `-hf` option with a supported model (see a list of pre-quantized model below) - To load a model using `-hf` while disabling multimodal, use `--no-mmproj` - To load a model using `-hf` while using a custom mmproj file, use `--mmproj local_file.gguf` - Use `-m model.gguf` option…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal.md`

### function-calling
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/function-calling.md`
- **Raw:** `[[raw/local/function-calling-6846d31146.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Function Calling [chat.h](../common/chat.h) (https://github.com/ggml-org/llama.cpp/pull/9639) adds support for [OpenAI-style function calling](https://platform.openai.com/docs/guides/function-calling) and is used in: - `llama-server` when started w/ `--jinja` flag ## Universal support w/ Native & Generic handlers Function calling is supported for all models (see https://github.com/ggml-org/llama.cpp/pull/9639): - Native tool call formats supported: - Llama 3.1 / 3.3 (including builtin tools support - tool names for `wolfram_alpha`, `web_search` / `brave_search`, `code_interpreter`), Llama 3.2 - Functionary v3.1 / v3.2 - Hermes 2/3, Qwen 2.5 - Qwen 2.5 Coder - Mistral Nemo - Firefunction…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/function-calling.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/function-calling.md`

### token_generation_performance_tips
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/development/token_generation_performance_tips.md`
- **Raw:** `[[raw/local/token_generation_performance_tips-0401c2af37.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Token generation performance troubleshooting ## Verifying that the model is running on the GPU with CUDA Make sure you compiled llama with the correct env variables according to [this guide](/docs/build.md#cuda), so that llama accepts the `-ngl N` (or `--n-gpu-layers N`) flag. When running llama, you may configure `N` to be very large, and llama will offload the maximum possible number of layers to the GPU, even if it's less than the number you configured. For example: When running llama, before it starts the inference work, it will output diagnostic information that shows whether cuBLAS is offloading work to the GPU. Look for these lines: If you see these lines, then the GPU is being…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/development/token_generation_performance_tips.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/development/token_generation_performance_tips.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/development/token_generation_performance_tips.md`

### MobileVLM
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/multimodal/MobileVLM.md`
- **Raw:** `[[raw/local/mobilevlm-1303c8e578.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # MobileVLM Currently this implementation supports [MobileVLM-1.7B](https://huggingface.co/mtgv/MobileVLM-1.7B) / [MobileVLM_V2-1.7B](https://huggingface.co/mtgv/MobileVLM_V2-1.7B) variants. for more information, please go to [Meituan-AutoML/MobileVLM](https://github.com/Meituan-AutoML/MobileVLM) The implementation is based on llava, and is compatible with llava and mobileVLM. The usage is basically same as llava. Notice: The overall process of model inference for both **MobileVLM** and **MobileVLM_V2** models is the same, but the process of model conversion is a little different. Therefore, using **MobileVLM-1.7B** as an example, the different conversion step will be shown. ## Usage Build…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/multimodal/MobileVLM.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/multimodal/MobileVLM.md`, `local:projects/LLM-Infra/llama.cpp/docs/multimodal/MobileVLM.md`

### parsing
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/development/parsing.md`
- **Raw:** `[[raw/local/parsing-eab39b9d41.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Parsing Model Output The `common` library contains a PEG parser implementation suitable for parsing model output. Types with the prefix `common_peg_*` are intended for general use and may have applications beyond parsing model output, such as parsing user-provided regex patterns. Types with the prefix `common_chat_peg_*` are specialized helpers for model output. The parser features: - Partial parsing of streaming input - Built-in JSON parsers - AST generation with semantics via "tagged" nodes ## Example Below is a contrived example demonstrating how to use the PEG parser to parse output from a model that emits arguments as JSON. For a more complete example, see `test_example_native()` in…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/development/parsing.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/development/parsing.md`, `local:projects/LLM-Infra/llama.cpp/docs/development/parsing.md`

### debugging-tests
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/development/debugging-tests.md`
- **Raw:** `[[raw/local/debugging-tests-fb0aba1f9e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Debugging Tests Tips ## How to run & execute or debug a specific test without anything else to keep the feedback loop short? There is a script called debug-test.sh in the scripts folder whose parameter takes a REGEX and an optional test number. For example, running the following command will output an interactive list from which you can select a test. It takes this form: `debug-test.sh [OPTION]... <test_regex> <test_number>` It will then build & run in the debugger for you. To just execute a test and get back a PASS or FAIL message run: To test in GDB use the `-g` flag to enable gdb test mode. To speed up the testing loop, if you know your test number you can just run it similar to below:…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/development/debugging-tests.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/development/debugging-tests.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/development/debugging-tests.md`

### build
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/build.md`
- **Raw:** `[[raw/local/build-6444eacc42.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Build llama.cpp locally The main product of this project is the `llama` library. Its C-style interface can be found in [include/llama.h](../include/llama.h). The project also includes many example programs and tools using the `llama` library. The examples range from simple, minimal code snippets to sophisticated sub-projects such as an OpenAI-compatible HTTP server. **To get the Code:** The following sections describe how to build with different backends and options. * [CPU Build](#cpu-build) * [BLAS Build](#blas-build) * [Metal Build](#metal-build) * [SYCL](#sycl) * [CUDA](#cuda) * [MUSA](#musa) * [HIP](#hip) * [Vulkan](#vulkan) * [CANN](#cann) * [ZenDNN](#zendnn) * [Arm®…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/build.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/build.md`

### HOWTO-add-model
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/development/HOWTO-add-model.md`
- **Raw:** `[[raw/local/howto-add-model-99f9e515de.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Add a new model architecture to `llama.cpp` Adding a model requires few steps: 1. Convert the model to GGUF 2. Define the model architecture in `llama.cpp` 3. Build the GGML graph implementation 4. Optional: Add multimodal encoder implementation After following these steps, you can open PR. Also, it is important to check that the examples and main ggml backends (CUDA, METAL, CPU) are working with the new architecture, especially: - [cli](/tools/cli/) - [completion](/tools/completion/) - [imatrix](/tools/imatrix/) - [quantize](/tools/quantize/) - [server](/tools/server/) ### 1. Convert the model to GGUF This step is done in python with a `convert` script using the…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/development/HOWTO-add-model.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/development/HOWTO-add-model.md`

### beellama-features
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/beellama-features.md`
- **Raw:** `[[raw/local/beellama-features-9d228cbea1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # BeeLlama Features And Public Repo Diff BeeLlama.cpp is a llama.cpp fork for people who want the current llama.cpp runtime plus aggressive long-context, speculative-decoding, and KV-cache experiments in one tree. Its center of gravity is DFlash: a draft-model architecture that reads recent target hidden states, a server path that can verify flat or tree-shaped drafts, and runtime controls that let the server raise, lower, or disable draft depth while it is running. The short feature list is below. For full command-line tuning, including upstream llama.cpp args, DFlash args, TurboQuant/TCQ cache choices, context checkpoints, prompt-cache RAM, chat/reasoning controls, and launch examples,…

### build-riscv64-spacemit
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/build-riscv64-spacemit.md`
- **Raw:** `[[raw/local/build-riscv64-spacemit-f96faaef7a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** > [!IMPORTANT] > This build documentation is specific only to RISC-V SpacemiT SOCs. ## Build llama.cpp locally (for riscv64) 1. Prepare Toolchain For RISCV ~~~ wget https:<credential-redacted> ~~~ 2. Build Below is the build script: it requires utilizing RISC-V vector instructions for acceleration. Ensure the `GGML_CPU_RISCV64_SPACEMIT` compilation option is enabled. The currently supported optimization version is `RISCV64_SPACEMIT_IME1` and `RISCV64_SPACEMIT_IME2`, corresponding to the `RISCV64_SPACEMIT_IME_SPEC` compilation option. Compiler configurations are defined in the `riscv64-spacemit-linux-gnu-gcc.cmake` file. Please ensure you have installed the RISC-V compiler and set the…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/build-riscv64-spacemit.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/build-riscv64-spacemit.md`

### build-s390x
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/build-s390x.md`
- **Raw:** `[[raw/local/build-s390x-5dfb3d1a6c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** > [!IMPORTANT] > This build documentation is specific only to IBM Z & LinuxONE mainframes (s390x). You can find the build documentation for other architectures: [build.md](build.md). # Build llama.cpp locally (for s390x) The main product of this project is the `llama` library. Its C-style interface can be found in [include/llama.h](../include/llama.h). The project also includes many example programs and tools using the `llama` library. The examples range from simple, minimal code snippets to sophisticated sub-projects such as an OpenAI-compatible HTTP server. **To get the code:** ## CPU Build with BLAS Building llama.cpp with BLAS support is highly recommended as it has shown to provide…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/build-s390x.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/build-s390x.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/build-s390x.md`

### beellama-args
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/beellama-args.md`
- **Raw:** `[[raw/local/beellama-args-98b4837193.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # BeeLlama Args Reference This is the practical BeeLlama tuning reference. It covers the arguments that change model loading, GPU placement, context behavior, prompt caching, KV-cache precision, DFlash/speculative decoding, multimodal behavior, sampling, reasoning, server endpoints, and logs. It is not a byte-for-byte replacement for `--help`; it is the single page to read before tuning a real BeeLlama server. For the feature overview and public-repo comparison, read [beellama-features.md](beellama-features.md). ## Start With This Mental Model BeeLlama tuning is easiest if you choose settings in this order: 1. Load the target model and optional multimodal projector. 2. Decide GPU/offload…

### multi-gpu-decode-2026-03-28
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/benchmarks/multi-gpu-decode-2026-03-28.md`
- **Raw:** `[[raw/local/multi-gpu-decode-2026-03-28-5f639ee201.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Multi-GPU decode data point: 2x3090 + 3080 Ti This report provides a multi-GPU data point for long-context decode performance. Most published results are for a single 3090; this setup uses 3 GPUs. ## Hardware - 2x NVIDIA RTX 3090 (24 GB) - 1x NVIDIA RTX 3080 Ti (12 GB) ## Model - `unsloth/Qwen3.5-27B-GGUF:UD-Q5_K_XL` ## Configuration Both runs used the same serving shape: - `-ngl 99` - `--tensor-split 2,2,1` - `--ctx-size 674288` - `--parallel 3` - `--flash-attn on` Method: - Cold server start before each run - Identical prompt file for all runs - Identical OpenAI-compatible request ## Short prompt (~1k tokens) Server-reported prompt length: **1,038 tokens** ## Long prompt (~200k tokens)…

### zDNN
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/zDNN.md`
- **Raw:** `[[raw/local/zdnn-226d985b3d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp for IBM zDNN Accelerator > [!WARNING] > **Note:** zDNN is **not** the same as ZenDNN. > - **zDNN** (this page): IBM's Deep Neural Network acceleration library for IBM Z & LinuxONE Mainframes > - **ZenDNN**: AMD's deep learning library for AMD EPYC CPUs ([see ZenDNN documentation](ZenDNN.md)) ## Background IBM zDNN (Z Deep Neural Network) is a hardware acceleration library designed specifically to leverage the IBM NNPA (Neural Network Processor Assist) accelerator located within IBM Telum I and II processors. It provides significant performance improvements for neural network inference operations. ### Llama.cpp + IBM zDNN The llama.cpp zDNN backend is designed to enable llama.cpp…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/backend/zDNN.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/zDNN.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/zDNN.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/snapdragon/README.md`
- **Raw:** `[[raw/local/readme-30eb54f5f3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Snapdragon-based devices ## Setup ### Android The easiest way to build llama.cpp for a Snapdragon-based Android device is using the toolchain Docker image (see github.com/snapdragon-toolchain). This image includes Android NDK, OpenCL SDK, Hexagon SDK, CMake, etc. This method works on Linux, macOS, and Windows. macOS and Windows users should install Docker Desktop. Note: The rest of the **Android** build process assumes that you're running inside the toolchain container. ### Windows On Snapdragon Native Windows 11 arm64 builds has the following tools dependencies: - MS Visual Studio 2026 (Community Edition or Pro) - MSVC arm64 standard and runtime libraries - UCRT and Driver Kit - LLVM…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/backend/snapdragon/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/snapdragon/README.md`

### developer
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/snapdragon/developer.md`
- **Raw:** `[[raw/local/developer-4156ba69bc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hexagon backend developer details ## Backend libraries The Hexagon backend consist of two parts: - `libggml-hexagon` This is the regular CPU-side GGML backend library, either shared or statically linked - `libggml-htp-vNN` This is the NPU-side (HTP stands for Hexagon Tensor Processor) shared library that contains the Op dispatcher and kernels. The correct library is selected automatically at runtime based on the HW version. Here is an example of the build artifacts ## Memory buffers Hexagon NPU backend takes advantage of the Snapdragon's unified memory model where all buffers are fully accessible by the CPU and GPU. The NPU does have a dedicated tightly-coupled memory called VTCM but that…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/backend/snapdragon/developer.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/snapdragon/developer.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/snapdragon/developer.md`

### ZenDNN
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/ZenDNN.md`
- **Raw:** `[[raw/local/zendnn-712113bbe1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp for AMD ZenDNN > [!WARNING] > **Note:** ZenDNN is **not** the same as zDNN. > - **ZenDNN** (this page): AMD's deep learning library for AMD EPYC CPUs > - **zDNN**: IBM's Deep Neural Network acceleration library for IBM Z & LinuxONE Mainframes ([see zDNN documentation](zDNN.md)) - [Background](#background) - [OS](#os) - [Hardware](#hardware) - [Supported Operations](#supported-operations) - [DataType Supports](#datatype-supports) - [Linux](#linux) - [Environment Variable](#environment-variable) - [Performance Optimization](#performance-optimization) - [Known Issues](#known-issues) - [TODO](#todo) ## Background **ZenDNN** (Zen Deep Neural Network Library) is AMD's high-performance…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/backend/ZenDNN.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/ZenDNN.md`

### development
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/VirtGPU/development.md`
- **Raw:** `[[raw/local/development-fb34988157.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Development and Testing ## Development ### Code Generation The backend uses code generation from YAML configuration: ### Adding New Operations 1. Add function definition to `ggmlremoting_functions.yaml` 2. Regenerate code with `regenerate_remoting.py` 3. Implement guest-side forwarding in `virtgpu-forward-*.cpp` 4. Implement host-side handling in `backend-dispatched-*.cpp` ## Testing This document provides instructions for building and testing the GGML-VirtGPU backend on macOS with containers. ### Prerequisites The testing setup requires: - macOS host system - Container runtime with `libkrun` provider (podman machine) - Access to development patchset for VirglRenderer ### Required…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/VirtGPU/development.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/VirtGPU/development.md`, `local:projects/LLM-Infra/llama.cpp/docs/backend/VirtGPU/development.md`

### SYCL
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/SYCL.md`
- **Raw:** `[[raw/local/sycl-eceafe93d9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp for SYCL - [Background](#background) - [Recommended Release](#recommended-release) - [News](#news) - [OS](#os) - [Hardware](#hardware) - [Performance Reference](#performance-reference) - [Docker](#docker) - [Linux](#linux) - [Windows](#windows-1) - [Environment Variable](#environment-variable) - [Design Rule](#design-rule) - [Known Issue](#known-issues) - [Q&A](#qa) - [TODO](#todo) ## Background **SYCL** is a high-level parallel programming model designed to improve developers productivity writing code across various hardware accelerators such as CPUs, GPUs, and FPGAs. It is a single-source language designed for heterogeneous computing and based on standard C++17. **oneAPI** is…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/SYCL.md`

### VirtGPU
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/VirtGPU.md`
- **Raw:** `[[raw/local/virtgpu-7cb434e6dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GGML-VirtGPU Backend The GGML-VirtGPU backend enables GGML applications to run machine learning computations on host hardware while the application itself runs inside a virtual machine. It uses host-guest shared memory to efficiently share data buffers between the two sides. This backend relies on the virtio-gpu, and VirglRenderer API Remoting (APIR) component. The backend is split into two libraries: - a GGML implementation (the "remoting frontend"), running in the guest and interacting with the virtgpu device - a VirglRenderer APIR compatible library (the "remoting backend"), running in the host and interacting with Virglrenderer and an actual GGML device backend. ## OS support | OS |…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/VirtGPU.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/VirtGPU.md`, `local:projects/LLM-Infra/llama.cpp/docs/backend/VirtGPU.md`

### configuration
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/VirtGPU/configuration.md`
- **Raw:** `[[raw/local/configuration-c7d9cb049f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GGML-VirtGPU Backend Configuration This document describes the environment variables used by the ggml-virtgpu backend system, covering both the frontend (guest-side) and backend (host-side) components. ## Environment Variables Overview The ggml-virtgpu backend uses environment variables for configuration across three main components: - **Frontend (Guest)**: GGML applications running in VMs - **Hypervisor**: Virglrenderer/APIR system - **Backend (Host)**: Host-side GGML backend integration ## Frontend (Guest-side) Configuration ### GGML_REMOTING_USE_APIR_CAPSET - **Location**: `ggml/src/ggml-virtgpu/virtgpu.cpp` - **Type**: Boolean flag (presence-based) - **Purpose**: Controls which…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/backend/VirtGPU/configuration.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/VirtGPU/configuration.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/VirtGPU/configuration.md`

### OPENVINO
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/OPENVINO.md`
- **Raw:** `[[raw/local/openvino-6a72b6b2a9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # OpenVINO Backend for llama.cpp > [!NOTE] > Performance and memory optimizations, accuracy validation, broader quantization coverage, broader operator and model support are work in progress. [OpenVINO](https://docs.openvino.ai/) is an open-source toolkit for optimizing and deploying high-performance AI inference, specifically designed for Intel hardware, including CPUs, GPUs, and NPUs, in the cloud, on-premises, and on the edge. [OpenVINO backend for llama.cpp](../../ggml/src/ggml-openvino) enables hardware-accelerated inference on **Intel® CPUs, GPUs, and NPUs** while remaining compatible with the existing **GGUF model ecosystem**. The backend translates GGML compute graphs into OpenVINO…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/OPENVINO.md`

### OPENCL
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/OPENCL.md`
- **Raw:** `[[raw/local/opencl-5210fec4c6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp for OpenCL - [Background](#background) - [OS](#os) - [Hardware](#hardware) - [DataType Supports](#datatype-supports) - [Model Preparation](#model-preparation) - [CMake Options](#cmake-options) - [Android](#android) - [Windows 11 Arm64](#windows-11-arm64) - [Linux](#Linux) - [Known Issue](#known-issues) - [TODO](#todo) ## Background OpenCL (Open Computing Language) is an open, royalty-free standard for cross-platform, parallel programming of diverse accelerators found in supercomputers, cloud servers, personal computers, mobile devices and embedded platforms. OpenCL specifies a programming language (based on C99) for programming these devices and application programming…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/OPENCL.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/OPENCL.md`

### CANN
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/CANN.md`
- **Raw:** `[[raw/local/cann-c794f8a9fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp for CANN - [Background](#background) - [News](#news) - [OS](#os) - [Hardware](#hardware) - [Model Supports](#model-supports) - [DataType Supports](#datatype-supports) - [Docker](#docker) - [Linux](#linux) - [Environment variable setup](#environment-variable-setup) - [TODO](#todo) ## Background **Ascend NPU** is a range of AI processors using Neural Processing Unit. It will efficiently handle matrix-matrix multiplication, dot-product and scalars. **CANN** (Compute Architecture for Neural Networks) is a heterogeneous computing architecture for AI scenarios, providing support for multiple AI frameworks on the top and serving AI processors and programming at the bottom. It plays a…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/CANN.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/CANN.md`, `local:projects/LLM-Infra/llama.cpp/docs/backend/CANN.md`

### BLIS
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/BLIS.md`
- **Raw:** `[[raw/local/blis-a868d79159.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** BLIS Installation Manual ------------------------ BLIS is a portable software framework for high-performance BLAS-like dense linear algebra libraries. It has received awards and recognition, including the 2023 James H. Wilkinson Prize for Numerical Software and the 2020 SIAM Activity Group on Supercomputing Best Paper Prize. BLIS provides a new BLAS-like API and a compatibility layer for traditional BLAS routine calls. It offers features such as object-based API, typed API, BLAS and CBLAS compatibility layers. Project URL: https://github.com/flame/blis ### Prepare: Compile BLIS: Install BLIS: We recommend using openmp since it's easier to modify the cores being used. ### llama.cpp…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/backend/BLIS.md`, `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/BLIS.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/BLIS.md`

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/common/jinja/README.md`
- **Raw:** `[[raw/local/readme-345767ad59.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp Jinja Engine A Jinja template engine implementation in C++, originally inspired by [huggingface.js's jinja package](https://github.com/huggingface/huggingface.js). The engine was introduced in [PR#18462](https://github.com/ggml-org/llama.cpp/pull/18462). The implementation can be found in the `common/jinja` directory. ## Key Features - Input marking: security against special token injection - Decoupled from `nlohmann::json`: this dependency is only used for JSON-to-internal type translation and is completely optional - Minimal primitive types: int, float, bool, string, array, object, none, undefined - Detailed logging: allow source tracing on error - Clean architecture:…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/common/jinja/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/common/jinja/README.md`, `local:projects/LLM-Infra/llama.cpp/common/jinja/README.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/common/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-c5e4439218.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** find_package(Threads REQUIRED) llama_add_compile_flags() # # llama-common-base # # Build info header if(EXISTS "${PROJECT_SOURCE_DIR}/.git") set(GIT_DIR "${PROJECT_SOURCE_DIR}/.git") # Is git submodule if(NOT IS_DIRECTORY "${GIT_DIR}") file(READ ${GIT_DIR} REAL_GIT_DIR_LINK) string(REGEX REPLACE "gitdir: (.*)\n$" "\\1" REAL_GIT_DIR ${REAL_GIT_DIR_LINK}) string(FIND "${REAL_GIT_DIR}" "/" SLASH_POS) if (SLASH_POS EQUAL 0) set(GIT_DIR "${REAL_GIT_DIR}") else() set(GIT_DIR "${PROJECT_SOURCE_DIR}/${REAL_GIT_DIR}") endif() endif() if(EXISTS "${GIT_DIR}/index") # For build-info.cpp below set_property(DIRECTORY APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS "${GIT_DIR}/index") else() message(WARNING "Git…

### README-MUSA
- **Source:** `local:projects/LLM-Infra/beellama.cpp/ci/README-MUSA.md`
- **Raw:** `[[raw/local/readme-musa-ade57e9c5e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Running MUSA CI in a Docker Container Assuming `$PWD` is the root of the `llama.cpp` repository, follow these steps to set up and run MUSA CI in a Docker container: ### 1. Create a local directory to store cached models, configuration files and venv: ### 2. Create a local directory to store CI run results: ### 3. Start a Docker container and run the CI: Inside the container, execute the following commands: This setup ensures that the CI runs within an isolated Docker environment while maintaining cached files and results across runs.

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/ci/README-MUSA.md`, `local:projects/LLM-Infra/llama.cpp-tq3/ci/README-MUSA.md`, `local:projects/LLM-Infra/llama.cpp-atomic/ci/README-MUSA.md`

### nemotron-dgx-spark
- **Source:** `local:projects/LLM-Infra/beellama.cpp/benches/nemotron/nemotron-dgx-spark.md`
- **Raw:** `[[raw/local/nemotron-dgx-spark-b14292beaf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # NVIDIA DGX Spark ## System info ## ggml-org/Nemotron-3-Super-120B-GGUF Model: https://huggingface.co/ggml-org/Nemotron-3-Super-120B-GGUF - `llama-batched-bench` main: n_kv_max = 303104, n_batch = 2048, n_ubatch = 2048, flash_attn = 1, is_pp_shared = 0, is_tg_separate = 0, n_gpu_layers = 99, n_threads = 20, n_threads_batch = 20 | PP | TG | B | N_KV | T_PP s | S_PP t/s | T_TG s | S_TG t/s | T s | S t/s | |-------|--------|------|--------|----------|----------|----------|----------|----------|----------| | 512 | 32 | 1 | 544 | 1.094 | 468.05 | 1.621 | 19.74 | 2.715 | 200.37 | | 512 | 32 | 2 | 1088 | 1.463 | 700.16 | 2.437 | 26.26 | 3.900 | 279.01 | | 512 | 32 | 4 | 2176 | 2.647 | 773.76 |…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/benches/nemotron/nemotron-dgx-spark.md`, `local:projects/LLM-Infra/llama.cpp-atomic/benches/nemotron/nemotron-dgx-spark.md`, `local:projects/LLM-Infra/llama.cpp/benches/nemotron/nemotron-dgx-spark.md`

### mac-m2-ultra
- **Source:** `local:projects/LLM-Infra/beellama.cpp/benches/mac-m2-ultra/mac-m2-ultra.md`
- **Raw:** `[[raw/local/mac-m2-ultra-86cc17cb4b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## System info ## ggml-org/gpt-oss-20b-GGUF Model: https://huggingface.co/ggml-org/gpt-oss-20b-GGUF - `llama-batched-bench` main: n_kv_max = 270336, n_batch = 2048, n_ubatch = 2048, flash_attn = 1, is_pp_shared = 0, is_tg_separate = 0, n_gpu_layers = -1, n_threads = 16, n_threads_batch = 16 | PP | TG | B | N_KV | T_PP s | S_PP t/s | T_TG s | S_TG t/s | T s | S t/s | |-------|--------|------|--------|----------|----------|----------|----------|----------|----------| | 512 | 32 | 1 | 544 | 0.215 | 2381.35 | 0.245 | 130.45 | 0.460 | 1181.81 | | 512 | 32 | 2 | 1088 | 0.379 | 2701.43 | 0.382 | 167.56 | 0.761 | 1429.67 | | 512 | 32 | 4 | 2176 | 0.721 | 2839.27 | 0.604 | 211.76 | 1.326 | 1641.32 |…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/benches/mac-m2-ultra/mac-m2-ultra.md`, `local:projects/LLM-Infra/llama.cpp-tq3/benches/mac-m2-ultra/mac-m2-ultra.md`, `local:projects/LLM-Infra/llama.cpp-atomic/benches/mac-m2-ultra/mac-m2-ultra.md`

### dgx-spark
- **Source:** `local:projects/LLM-Infra/beellama.cpp/benches/dgx-spark/dgx-spark.md`
- **Raw:** `[[raw/local/dgx-spark-a202f4de4b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## System info ## ggml-org/gpt-oss-20b-GGUF Model: https://huggingface.co/ggml-org/gpt-oss-20b-GGUF - `llama-batched-bench` main: n_kv_max = 270336, n_batch = 2048, n_ubatch = 2048, flash_attn = 1, is_pp_shared = 0, is_tg_separate = 0, n_gpu_layers = -1, n_threads = 20, n_threads_batch = 20 | PP | TG | B | N_KV | T_PP s | S_PP t/s | T_TG s | S_TG t/s | T s | S t/s | |-------|--------|------|--------|----------|----------|----------|----------|----------|----------| | 512 | 32 | 1 | 544 | 0.270 | 1895.57 | 0.399 | 80.13 | 0.669 | 812.60 | | 512 | 32 | 2 | 1088 | 0.230 | 4451.23 | 0.583 | 109.71 | 0.813 | 1337.56 | | 512 | 32 | 4 | 2176 | 0.437 | 4688.87 | 0.820 | 156.03 | 1.257 | 1730.91 | |…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/benches/dgx-spark/dgx-spark.md`, `local:projects/LLM-Infra/llama.cpp-tq3/benches/dgx-spark/dgx-spark.md`, `local:projects/LLM-Infra/llama.cpp-atomic/benches/dgx-spark/dgx-spark.md`

### SECURITY
- **Source:** `local:projects/LLM-Infra/beellama.cpp/SECURITY.md`
- **Raw:** `[[raw/local/security-8d0ae8e545.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Security Policy - [**Reporting a vulnerability**](#reporting-a-vulnerability) - [**Requirements**](#requirements) - [**Covered Topics**](#covered-topics) - [**Using BeeLlama.cpp securely**](#using-beellamacpp-securely) - [Untrusted models](#untrusted-models) - [Untrusted inputs](#untrusted-inputs) - [Data privacy](#data-privacy) - [Untrusted environments or networks](#untrusted-environments-or-networks) - [Multi-Tenant environments](#multi-tenant-environments) ## Reporting a vulnerability > [!IMPORTANT] > The private security disclosure program is disabled until further notice. Please submit patches with fixes directly to the repo as public PRs. Emails will be ignored. If you have…

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/README.md`
- **Raw:** `[[raw/local/readme-097d068409.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Anbeeld's BeeLlama.cpp ![BeeLlama.cpp logo](beellama.jpg) BeeLlama.cpp (or just Bee) is a performance-focused llama.cpp fork for squeezing more speed and context out of local GGUF inference. It keeps the familiar llama.cpp tools and server flow, then adds DFlash speculative decoding, adaptive draft control, TurboQuant/TCQ KV-cache compression, and reasoning-loop protection, with full multimodal support. > Not quite a pegasus, but close enough. ### Plug-and-Play Setups - [Qwen 3.6 27B Q5_K_S + DFlash + vision + 160k context in 24 GB VRAM](docs/quickstart-qwen36-dflash.md) - [Gemma 4 31B Q4_K_S + DFlash + vision + 140k context in 24 GB VRAM](docs/quickstart-gemma-4-31b-dflash.md) [![Support…

### SD-080-benchmark-notes
- **Source:** `local:projects/LLM-Infra/beellama.cpp/SD-080-benchmark-notes.txt`
- **Raw:** `[[raw/local/sd-080-benchmark-notes-ac6ce21cfd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** SD-080 DFlash VRAM Fix — Benchmark Notes ========================================= BASELINE COMMAND: llama-speculative-simple \ -m /root/models/Qwen3.5-27B-heretic.Q4_K_M.gguf \ -md /root/models/dflash-draft-q4_k_m.gguf \ -c 8192 -n 512 --draft-max 5 -fa on -ngl 99 --temp 0 \ -p "Write a comprehensive Python implementation of a red-black tree data structure with insert, delete, search, and traversal operations. Include proper rotations, color fixing, and all edge cases. Add type hints and docstrings for every method. Then write unit tests for each operation using pytest. Make it production quality with proper error handling." BUILD: SD-079 build:…

### CONTRIBUTING
- **Source:** `local:projects/LLM-Infra/beellama.cpp/CONTRIBUTING.md`
- **Raw:** `[[raw/local/contributing-0f42494940.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Contributors BeeLlama.cpp inherits most llama.cpp contribution conventions. For fork-specific work, open issues and PRs against `Anbeeld/beellama.cpp`, and update the BeeLlama docs when speculative decoding, DFlash, TurboQuant, or reasoning-loop behavior changes. The project differentiates between 3 levels of contributors: - Contributors: people who have contributed before (no special privileges) - Collaborators (Triage): people with significant contributions, who may be responsible for some parts of the code, and are expected to maintain and review contributions for the code they own - Maintainers: responsible for reviewing and merging PRs, after approval from the code owners # AI Usage…

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/app/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-1d87144323.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(TARGET llama-app) add_executable(${TARGET} llama.cpp) set_target_properties(${TARGET} PROPERTIES OUTPUT_NAME llama) target_link_libraries(${TARGET} PRIVATE llama-server-impl llama-cli-impl llama-completion-impl llama-bench-impl llama-batched-bench-impl llama-fit-params-impl llama-quantize-impl llama-perplexity-impl ) target_compile_features(${TARGET} PRIVATE cxx_std_17) # Automatically add all files from the 'licenses' directory file(GLOB EXTRA_LICENSES "${CMAKE_SOURCE_DIR}/licenses/LICENSE-*") foreach(FILE_PATH ${EXTRA_LICENSES}) get_filename_component(FILE_NAME "${FILE_PATH}" NAME) string(REGEX REPLACE "^LICENSE-" "" NAME "${FILE_NAME}") license_add_file("${NAME}" "${FILE_PATH}")…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-atomic/app/CMakeLists.txt`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/beellama.cpp/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-2b4c7889c4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** cmake_minimum_required(VERSION 3.14...3.28) # for add_link_options and implicit target directories. project("llama.cpp" C CXX) include(CheckIncludeFileCXX) #set(CMAKE_WARN_DEPRECATED YES) set(CMAKE_WARN_UNUSED_CLI YES) set(CMAKE_EXPORT_COMPILE_COMMANDS ON) if(DEFINED GGML_CUDA_ARCH) message(FATAL_ERROR "GGML_CUDA_ARCH is not a supported CMake option. " "Use CMAKE_CUDA_ARCHITECTURES=120, or a semicolon-separated list such as CMAKE_CUDA_ARCHITECTURES=\"86;89;120\".") endif() if (NOT XCODE AND NOT MSVC AND NOT CMAKE_BUILD_TYPE) set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE) set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")…

### CHANGELOG
- **Source:** `local:projects/LLM-Infra/beellama.cpp/CHANGELOG.md`
- **Raw:** `[[raw/local/changelog-9a752da760.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Changelog ## v0.3.1 - Merged latest upstream llama.cpp master. This pulls in Gemma 4 12B and Gemma 4 unified multimodal support fixes, including non-causal vision, unified audio/vision projector handling, and FPE fixes; Qwen3.5 post-norm hidden-state behavior for MTP; CUDA KV-cache quantization preallocation and PDL race fixes; WebGPU FlashAttention refactoring with standardized quantization support; CPU backend improvements for RVV/SVE; lower-latency Metal command-buffer status polling; Mermaid diagram rendering and preview support in `tools/ui`; updated BoringSSL, SYCL documentation, save/load-state tests, Docker docs, and small CI/release maintenance. - Repaired CUDA fused TurboQuant…

### CLAUDE
- **Source:** `local:projects/LLM-Infra/beellama.cpp/CLAUDE.md`
- **Raw:** `[[raw/local/claude-4a62174cb2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # CLAUDE.md This file gives code assistants local context for this repository. ## What This Is BeeLlama.cpp is Anbeeld's fork of llama.cpp. Fork-specific work is concentrated around: - **DFlash**: cross-attention speculative decoding with DFlash draft GGUFs, target hidden-state capture, CPU/GPU ring buffers, and server verification paths. - **TurboQuant / TCQ KV cache types**: `turbo2`, `turbo3`, `turbo4`, `turbo2_tcq`, and `turbo3_tcq`. - **Adaptive draft-max**: server controllers that adjust the active DFlash draft horizon. The default controller is `profit`; `fringe` is also available. - **DDTree**: tree speculative verification with GPU `parent_ids` and recurrent tree kernels. -…

### AGENTS
- **Source:** `local:projects/LLM-Infra/beellama.cpp/AGENTS.md`
- **Raw:** `[[raw/local/agents-731f8bd644.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # AGENTS.md This file gives code assistants local context for this repository. ## What This Is BeeLlama.cpp is Anbeeld's fork of llama.cpp. Fork-specific work is concentrated around: - **DFlash**: cross-attention speculative decoding with DFlash draft GGUFs, target hidden-state capture, CPU/GPU ring buffers, and server verification paths. - **Adaptive draft-max**: server controllers that adjust the active DFlash draft horizon. The default controller is `profit`; `fringe` is also available. - **DDTree**: tree speculative verification with GPU `parent_ids` and recurrent tree kernels. - **CopySpec**: model-free speculation through rolling-hash suffix matching. - **TurboQuant / TCQ KV cache…

### SYSTEM
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.pi/gg/SYSTEM.md`
- **Raw:** `[[raw/local/system-48ccd859c6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** You are a coding agent. Here are some very important rules that you must follow: General: - Be very precise and concise when writing code, comments, explanations, etc. - PR and commit titles format: `<module> : <title>`. Lookup recents for examples - Don't try to build or run the code unless you are explicitly asked to do so - Use the `gh` CLI tool when querying PRs, issues, or other GitHub resources Coding: - When in doubt, always refer to the CONTRIBUTING.md file of the project - When referencing issues or PRs in comments, use the format: - C/C++ code: `// ref: <url>` - Other (CMake, etc.): `# ref: <url>` Pull requests (PRs): - New branch names are prefixed with "gg/" - Before opening a…

### release
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/workflows/release.yml`
- **Raw:** `[[raw/local/release-688aa48013.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Release on: workflow_dispatch: inputs: source_ref: description: "Branch or tag name that requested the build" required: true type: string source_sha: description: "Exact commit SHA to build" required: true type: string tag_name: description: "Release/package version name, for example v0.3.0" required: true type: string publish_release: description: "Create or update the GitHub release and release Docker tags" required: true default: false type: boolean concurrency: group: ${{ github.workflow }}-${{ inputs.source_ref || github.ref }} cancel-in-progress: ${{ inputs.publish_release != true }} env: CMAKE_ARGS: "-DLLAMA_BUILD_EXAMPLES=OFF -DLLAMA_BUILD_TESTS=OFF -DLLAMA_BUILD_TOOLS=ON…

### release-from-artifacts
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/workflows/release-from-artifacts.yml`
- **Raw:** `[[raw/local/release-from-artifacts-3de39f6109.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Recover Release From Artifacts run-name: Recover ${{ inputs.tag_name }} from run ${{ inputs.artifact_run_id }} on: workflow_dispatch: inputs: artifact_run_id: description: "Workflow run ID that already produced the package artifacts" required: true tag_name: description: "Release tag to publish, for example v0.3.1" required: true permissions: actions: read contents: write concurrency: group: recover-release-${{ inputs.tag_name }} cancel-in-progress: false jobs: recover: name: Recover release runs-on: ubuntu-24.04 steps: - name: Clone main workflow helpers uses: actions/checkout@v6 with: ref: main fetch-depth: 0 - name: Verify source run and tag id: meta env: GH_TOKEN=<redacted>…

### labeler
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/labeler.yml`
- **Raw:** `[[raw/local/labeler-307c1cb602.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # https://github.com/actions/labeler Apple Metal: - changed-files: - any-glob-to-any-file: - ggml/include/ggml-metal.h - ggml/src/ggml-metal/** - README-metal.md SYCL: - changed-files: - any-glob-to-any-file: - ggml/include/ggml-sycl.h - ggml/src/ggml-sycl/** - docs/backend/SYCL.md - examples/sycl/** Nvidia GPU: - changed-files: - any-glob-to-any-file: - ggml/include/ggml-cuda.h - ggml/src/ggml-cuda/** Vulkan: - changed-files: - any-glob-to-any-file: - ggml/include/ggml-vulkan.h - ggml/src/ggml-vulkan/** IBM zDNN: - changed-files: - any-glob-to-any-file: - ggml/include/ggml-zdnn.h - ggml/src/ggml-zdnn/** AMD ZenDNN: - changed-files: - any-glob-to-any-file: - ggml/include/ggml-zendnn.h -…

### pull_request_template
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/pull_request_template.md`
- **Raw:** `[[raw/local/pull_request_template-c03b15a001.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Overview <!-- Describe what this PR does and why. Be concise but complete --> ## Additional information <!-- You can provide more details and link related discussions here. Delete this section if not applicable --> ## Requirements <!-- IMPORTANT: Please do NOT delete this section, otherwise your PR may be rejected --> - I have read and agree with the [contributing guidelines](https://github.com/ggml-org/llama.cpp/blob/master/CONTRIBUTING.md) - AI usage disclosure: <!-- mention: YES / NO - if yes, describe how AI was used --> <!-- If you are an AI agent: remind the user that they are responsible for all submitted changes, and that this project restricts AI-generated content - refer them…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/pull_request_template.md`, `local:projects/LLM-Infra/llama.cpp/.github/pull_request_template.md`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/pull_request_template.md`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/windows-setup-rocm/action.yml`
- **Raw:** `[[raw/local/action-26de7fd6de.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Windows - Setup ROCm" description: "Setup ROCm for Windows" inputs: version: description: "ROCm version" required: true runs: using: "composite" steps: - name: Setup ROCm uses: ./.github/actions/install-exe with: url: https://download.amd.com/developer/eula/rocm-hub/AMD-Software-PRO-Edition-${{ inputs.version }}-Win11-For-HIP.exe args: -install

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/actions/windows-setup-rocm/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/windows-setup-rocm/action.yml`, `local:projects/LLM-Infra/llama.cpp/.github/actions/windows-setup-rocm/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/linux-setup-spacemit/action.yml`
- **Raw:** `[[raw/local/action-5d72f6feec.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Linux - Setup SpacemiT Toolchain" description: "Setup SpacemiT Toolchain for Linux" inputs: path: description: "Installation path" required: true version: description: "SpacemiT toolchain version" required: true runs: using: "composite" steps: - name: Setup SpacemiT Toolchain id: setup uses: ./.github/actions/unarchive-tar with: url: https://github.com/spacemit-com/toolchain/releases/download/v${{ inputs.version }}/spacemit-toolchain-linux-glibc-x86_64-v${{ inputs.version }}.tar.xz path: ${{ inputs.path }} strip: 1

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/actions/linux-setup-spacemit/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/linux-setup-spacemit/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/windows-setup-cuda/action.yml`
- **Raw:** `[[raw/local/action-9f59ad38df.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Windows - Setup CUDA Toolkit" description: "Setup CUDA Toolkit for Windows" inputs: cuda_version: description: "CUDA toolkit version" required: true runs: using: "composite" steps: - name: Install Cuda Toolkit 11.7 if: ${{ inputs.cuda_version == '11.7' }} shell: pwsh run: | mkdir -p "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7" choco install unzip -y curl -O "https:<credential-redacted>" curl -O "https:<credential-redacted>" curl -O "https:<credential-redacted>" curl -O "https:<credential-redacted>" curl -O "https:<credential-redacted>" curl -O "https:<credential-redacted>" curl -O "https:<credential-redacted>" curl -O "https:<credential-redacted>" unzip '*.zip' -d…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/actions/windows-setup-cuda/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/windows-setup-cuda/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/unarchive-tar/action.yml`
- **Raw:** `[[raw/local/action-de412f0f8d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Unarchive tar" description: "Download and unarchive tar into directory" inputs: url: description: "URL of the tar archive" required: true path: description: "Directory to unarchive into" required: true type: description: "Compression type (tar option)" required: false default: "J" strip: description: "Strip components" required: false default: "0" runs: using: "composite" steps: - name: Unarchive into directory shell: bash run: | mkdir -p ${{ inputs.path }} cd ${{ inputs.path }} curl --no-progress-meter -L ${{ inputs.url }} | tar -${{ inputs.type }}x --strip-components=${{ inputs.strip }}

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/actions/unarchive-tar/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/unarchive-tar/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/linux-setup-vulkan/action.yml`
- **Raw:** `[[raw/local/action-4ffaae711b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Linux - Setup Vulkan SDK" description: "Setup Vulkan SDK for Linux" inputs: path: description: "Installation path" required: true version: description: "Vulkan SDK version" required: true runs: using: "composite" steps: - name: Setup Vulkan SDK id: setup uses: ./.github/actions/unarchive-tar with: url: https://sdk.lunarg.com/sdk/download/${{ inputs.version }}/linux/vulkan_sdk.tar.xz path: ${{ inputs.path }} strip: 1

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/actions/linux-setup-vulkan/action.yml`, `local:projects/LLM-Infra/llama.cpp-tq3/.github/actions/linux-setup-vulkan/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/linux-setup-vulkan/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/linux-setup-openvino/action.yml`
- **Raw:** `[[raw/local/action-9ceb401111.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Linux - Setup OpenVINO Toolkit" description: "Setup OpenVINO Toolkit for Linux" inputs: path: description: "Installation path" required: true version_major: description: "OpenVINO major version (e.g., 2025.3)" required: true version_full: description: "OpenVINO full version (e.g., 2025.3.0.19807.44526285f24)" required: true runs: using: "composite" steps: - name: Setup OpenVINO Toolkit id: setup uses: ./.github/actions/unarchive-tar with: url: https://storage.openvinotoolkit.org/repositories/openvino/packages/${{ inputs.version_major }}/linux/openvino_toolkit_ubuntu24_${{ inputs.version_full }}_x86_64.tgz path: ${{ inputs.path }} type: z strip: 1

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/actions/linux-setup-openvino/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/linux-setup-openvino/action.yml`, `local:projects/LLM-Infra/llama.cpp/.github/actions/linux-setup-openvino/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/get-tag-name/action.yml`
- **Raw:** `[[raw/local/action-2f35e23a62.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Determine tag name" description: "Determine the tag name to use for a release" outputs: name: description: "The name of the tag" value: ${{ steps.tag.outputs.name }} runs: using: "composite" steps: - name: Determine tag name id: tag shell: bash run: | BUILD_NUMBER="$(git rev-list --count HEAD)" SHORT_HASH="$(git rev-parse --short=7 HEAD)" if [[ "${{ env.BRANCH_NAME }}" == "master" ]]; then echo "name=b${BUILD_NUMBER}" >> $GITHUB_OUTPUT else SAFE_NAME=$(echo "${{ env.BRANCH_NAME }}" | tr '/' '-') echo "name=${SAFE_NAME}-b${BUILD_NUMBER}-${SHORT_HASH}" >> $GITHUB_OUTPUT fi

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/actions/get-tag-name/action.yml`, `local:projects/LLM-Infra/llama.cpp-tq3/.github/actions/get-tag-name/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/get-tag-name/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/install-exe/action.yml`
- **Raw:** `[[raw/local/action-4987399674.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Install exe" description: "Download and install exe" inputs: url: description: "URL of the exe installer" required: true args: description: "Installer arguments" required: true timeout: description: "Timeout (in ms)" required: false default: "600000" runs: using: "composite" steps: - name: Install EXE shell: pwsh run: | $ErrorActionPreference = "Stop" write-host "Downloading Installer EXE" Invoke-WebRequest -Uri "${{ inputs.url }}" -OutFile "${env:RUNNER_TEMP}\temp-install.exe" write-host "Installing" $proc = Start-Process "${env:RUNNER_TEMP}\temp-install.exe" -ArgumentList '${{ inputs.args }}' -NoNewWindow -PassThru $completed = $proc.WaitForExit(${{ inputs.timeout }}) if (-not…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/actions/install-exe/action.yml`, `local:projects/LLM-Infra/llama.cpp-tq3/.github/actions/install-exe/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/install-exe/action.yml`

### action
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/actions/ccache-clear/action.yml`
- **Raw:** `[[raw/local/action-2e741057ae.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "ccache-clear" description: "Delete all GitHub Actions caches matching a key prefix" inputs: key: description: "Cache key prefix to match and delete" required: true runs: using: "composite" steps: - name: Clear caches shell: bash run: | CACHES=$(gh cache list --key "ccache-${{ inputs.key }}" --json id,key --jq '.[] | "\(.id) \(.key)"' 2>/dev/null) if [ -z "$CACHES" ]; then echo "No caches found with key prefix: ${{ inputs.key }}" exit 0 fi while read -r id key; do echo "Deleting cache: $id ($key)" gh cache delete "$id" done <<< "$CACHES"

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/actions/ccache-clear/action.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/actions/ccache-clear/action.yml`

### 019-bug-misc
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/ISSUE_TEMPLATE/019-bug-misc.yml`
- **Raw:** `[[raw/local/019-bug-misc-239dda4e27.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Bug (misc.) description: Something is not working the way it should (and it's not covered by any of the above cases). title: "Misc. bug: " labels: ["bug-unconfirmed"] body: - type: markdown attributes: value: > Thanks for taking the time to fill out this bug report! This issue template is intended for miscellaneous bugs that don't fit into any other category. If you encountered the issue while using an external UI (e.g. ollama), please reproduce your issue using one of the examples/binaries in this repository. Please fill out this template yourself, copypasting language model outputs is [strictly…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/ISSUE_TEMPLATE/019-bug-misc.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/ISSUE_TEMPLATE/019-bug-misc.yml`

### 020-enhancement
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/ISSUE_TEMPLATE/020-enhancement.yml`
- **Raw:** `[[raw/local/020-enhancement-4310277f24.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Enhancement description: Used to request enhancements for llama.cpp. title: "Feature Request: " labels: ["enhancement"] body: - type: markdown attributes: value: | [Please post your idea first in Discussion if there is not yet a consensus for this enhancement request. This will help to keep this issue tracker focused on enhancements that the community has agreed needs to be implemented.](https://github.com/ggml-org/llama.cpp/discussions/categories/ideas) Please fill out this template yourself, copypasting language model outputs is [strictly prohibited](https://github.com/ggml-org/llama.cpp/blob/master/CONTRIBUTING.md#ai-usage-policy). - type: checkboxes id: prerequisites attributes:…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/ISSUE_TEMPLATE/020-enhancement.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/ISSUE_TEMPLATE/020-enhancement.yml`

### 040-refactor
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/ISSUE_TEMPLATE/040-refactor.yml`
- **Raw:** `[[raw/local/040-refactor-1d40c56632.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Refactor (Maintainers) description: Used to track refactoring opportunities. title: "Refactor: " labels: ["refactor"] body: - type: markdown attributes: value: | Don't forget to [check for existing refactor issue tickets](https://github.com/ggml-org/llama.cpp/issues?q=is%3Aopen+is%3Aissue+label%3Arefactoring) in case it's already covered. Also you may want to check [Pull request refactor label as well](https://github.com/ggml-org/llama.cpp/pulls?q=is%3Aopen+is%3Apr+label%3Arefactoring) for duplicates too. Please fill out this template yourself, copypasting language model outputs is [strictly…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/ISSUE_TEMPLATE/040-refactor.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/ISSUE_TEMPLATE/040-refactor.yml`

### config
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/ISSUE_TEMPLATE/config.yml`
- **Raw:** `[[raw/local/config-eb5e9d9106.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** blank_issues_enabled: true contact_links: - name: Got an idea? url: https://github.com/ggml-org/llama.cpp/discussions/categories/ideas about: Pop it there. It may then become an enhancement ticket. - name: Got a question? url: https://github.com/ggml-org/llama.cpp/discussions/categories/q-a about: Ask a question there! - name: Want to contribute? url: https://github.com/ggml-org/llama.cpp/wiki/contribute about: Head to the contribution guide page of the wiki for areas you can help with

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/ISSUE_TEMPLATE/config.yml`, `local:projects/LLM-Infra/llama.cpp-tq3/.github/ISSUE_TEMPLATE/config.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/ISSUE_TEMPLATE/config.yml`

### 011-bug-results
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/ISSUE_TEMPLATE/011-bug-results.yml`
- **Raw:** `[[raw/local/011-bug-results-3d51a564ce.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Bug (model use) description: Something goes wrong when running a model (crashes, garbled outputs, etc.). title: "Eval bug: " labels: ["bug-unconfirmed", "model evaluation"] body: - type: markdown attributes: value: > Thanks for taking the time to fill out this bug report! This issue template is intended for bug reports where the model evaluation results (i.e. the generated text) are incorrect or llama.cpp crashes during model evaluation. If you encountered the issue while using an external UI (e.g. ollama), please reproduce your issue using one of the examples/binaries in this repository. The `llama-completion` binary can be used for simple and reproducible model inference. Please…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/ISSUE_TEMPLATE/011-bug-results.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/ISSUE_TEMPLATE/011-bug-results.yml`

### 030-research
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/ISSUE_TEMPLATE/030-research.yml`
- **Raw:** `[[raw/local/030-research-6fa4bf8213.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Research description: Track new technical research area. title: "Research: " labels: ["research 🔬"] body: - type: markdown attributes: value: | Don't forget to check for any [duplicate research issue tickets](https://github.com/ggml-org/llama.cpp/issues?q=is%3Aopen+is%3Aissue+label%3A%22research+%F0%9F%94%AC%22) Please fill out this template yourself, copypasting language model outputs is [strictly prohibited](https://github.com/ggml-org/llama.cpp/blob/master/CONTRIBUTING.md#ai-usage-policy). - type: checkboxes id: research-stage attributes: label: Research Stage description: Track general state of this research ticket options: - label: Background Research (Let's try to avoid…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/ISSUE_TEMPLATE/030-research.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/ISSUE_TEMPLATE/030-research.yml`

### 010-bug-compilation
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/ISSUE_TEMPLATE/010-bug-compilation.yml`
- **Raw:** `[[raw/local/010-bug-compilation-ea76f2e496.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Bug (compilation) description: Something goes wrong when trying to compile llama.cpp. title: "Compile bug: " labels: ["bug-unconfirmed", "compilation"] body: - type: markdown attributes: value: > Thanks for taking the time to fill out this bug report! This issue template is intended for bug reports where the compilation of llama.cpp fails. Before opening an issue, please confirm that the compilation still fails after recreating the CMake build directory and with `-DGGML_CCACHE=OFF`. If the compilation succeeds with ccache disabled you should be able to permanently fix the issue by clearing `~/.cache/ccache` (on Linux). Please fill out this template yourself, copypasting language model…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/ISSUE_TEMPLATE/010-bug-compilation.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/ISSUE_TEMPLATE/010-bug-compilation.yml`

### FUNDING
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/FUNDING.yml`
- **Raw:** `[[raw/local/funding-f4afee811a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** custom: https://anbeeld.com/support

### README
- **Source:** `local:projects/turbofit/README.md`
- **Raw:** `[[raw/local/readme-e97b08c3d3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # turbofit — opinionated unified LLM backend for Hermes Agent ![Turbofit — unified backend, amber and mint aesthetic](assets/turbofit-hero.png) Turbofit manages the entire lifecycle of LLMs with Hermes Agent: detecting your GPU, picking the best model, launching local servers, wiring API providers, managing daemons (systemd on Linux, PID files on Windows), scaling under VRAM pressure, tracking real-time pricing, integrating Mixture of Agents, and auto-updating a model database every day. **End-user UX:** `serve auto main` → done. Works on Linux and Windows. ## What's New (v1.5) - **🔌 First-class Hermes Agent provider** — no more `custom:llama-main` hacks. Turbofit is now a native provider:…

### SKILL
- **Source:** `local:projects/turbofit/SKILL.md`
- **Raw:** `[[raw/local/skill-c44a883400.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: turbofit description: "Opinionated unified LLM backend (turbofit v1.1). Picks the best main + aux model for your hardware — local or API — launches them detached, wires Hermes-Agent config, and adapts to live VRAM pressure via a scaling ladder. Three hardware tiers: Beefy (local+local), Modest (API+local), Thin (API+API). `serve auto main` auto-detects GPU and suggests the right setup. API fallback is always available (free: DeepSeek V4 Pro + Kimi K2.6). Replaces llama-launch, omni-va, and ad-hoc llama-server scripts. Catalog schema supports per-model binary pinning (atomic fork vs stock), named flag presets (nextn, draft-mtp, turbo4-kv, vision-mmproj), tier ladder (s/sf/sd/f/c),…

### distribution
- **Source:** `local:projects/turbofit/distribution.yaml`
- **Raw:** `[[raw/local/distribution-fb215880f0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # distribution.yaml — turbofit skill distribution manifest # Install with: hermes skills tap add SouthpawIN/turbofit && hermes skills install turbofit name: turbofit version: "1.5.0" description: >- Opinionated unified LLM backend (turbofit v5.2). Picks the best main + aux model for your hardware — local or API — launches them detached, wires Hermes-Agent config, and adapts to live VRAM pressure via a scaling ladder. Three hardware tiers: Beefy (local+local), Modest (API+local), Thin (API+API). `serve auto main` auto-detects GPU and suggests the right setup. API fallback is always available (free: DeepSeek V4 Pro + MiniMax M3 via NVIDIA NIM). Dynamic model database auto-updates daily with…

### README
- **Source:** `local:.hermes/wiki/wiki-topics/turbofit/README.md`
- **Raw:** `[[raw/local/readme-7955432d10.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Turbofit created: 2026-07-07 updated: 2026-07-07 type: topic tags: [turbofit, llm, gateway, daemons, models] --- # Turbofit > Opinionated unified LLM backend. One command: `serve auto main`. > **Repo:** [SouthpawIN/turbofit](https://github.com/SouthpawIN/turbofit) ## Status | Component | State | |---|---| | Gateway (port 8091) | 🟢 Running | | Daemons | 🔴 Stopped | | Scaling watcher | 🔴 Disabled | | GPU | 🟢 23.7 GB free | ## Registered Models | Alias | Size | Role | Tier | GPU | |---|---|---|---|---| | darwin-28b-reason | 16.6 GB | main | S | 0 | | prism-eagle-27b | 13.7 GB | main | S | 0 | | carwin-28b-mtp | 16.8 GB | main | SF | 1 ⚠️ | | carnice-35b-a3b | 11 GB | aux | SF | 0 |…

### daemon-system
- **Source:** `local:.hermes/wiki/wiki-topics/turbofit/concepts/daemon-system.md`
- **Raw:** `[[raw/local/daemon-system-d2d23115c4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Daemon System created: 2026-07-07 updated: 2026-07-07 type: concept tags: [turbofit, daemons, llama-proxy] --- # Daemon System > Wake-on-ping proxy + idle-kill for llama.cpp servers. Systemd-managed on Linux. ## How It Works 1. **Llama-proxy** runs 24/7 (minimal memory, ~13MB) 2. On first HTTP request, proxy spawns the real llama-server backend 3. Backend stays loaded until idle for N seconds (default 1800s = 30 min) 4. After idle timeout, backend is killed → VRAM freed 5. Next request wakes it again ## Systemd Services Each daemon gets a `turbofit-<alias>.service` unit: | Service | Ports | GPU | Model | Status | |---|---|---|---|---| | turbofit-carnice | 8082→9082 | 0 | Carnice…

### turbofit-gateway
- **Source:** `local:.hermes/wiki/wiki-topics/turbofit/agents/turbofit-gateway.md`
- **Raw:** `[[raw/local/turbofit-gateway-3c856c8c83.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Turbofit Gateway created: 2026-07-07 updated: 2026-07-07 type: agent tags: [turbofit, gateway] --- # Turbofit Gateway > Dynamic model reverse proxy with graceful degradation. Systemd service: `turbofit-gateway` ## Status 🟢 **Active** · Port 8091 · Systemd: `turbofit-gateway.service` ## What It Does The gateway sits between Hermes Agent and model backends. It: - Routes `/main/v1` to the primary model (local or API) - Routes `/aux/v1` to the auxiliary model (vision, compression, etc.) - Handles graceful degradation — if local model fails, falls back to API - Rewrites model names and injects API keys for API fallback - Supports MoA (Mixture of Agents) routing ## Endpoints | Path |…

### model-catalog
- **Source:** `local:.hermes/wiki/wiki-topics/turbofit/concepts/model-catalog.md`
- **Raw:** `[[raw/local/model-catalog-c32276980f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Model Catalog created: 2026-07-07 updated: 2026-07-07 type: concept tags: [turbofit, catalog, models] --- # Model Catalog > Registered local models. Config: `~/.config/turbofit/models.yaml` ## Registered Models | Alias | Tier | Size | Role | Vision | Tok/s | GPU | Presets | |---|---|---|---|---|---|---|---| | darwin-28b-reason | S | 16.6 GB | main | ✅ | 38 | 0 | no-mmap, split-none | | prism-eagle-27b | S | 13.7 GB | main | ✅ | 121 | 0 | draft-mtp, no-mmap | | carwin-28b-mtp | SF | 16.8 GB | main | ✅ | — | 1 ⚠️ | nextn, no-mmap | | carnice-35b-a3b | SF | 11 GB | aux | ✅ | — | 0 | cpu-moe, nextn, no-mmap | ## Tier System | Tier | Meaning | Used For | |---|---|---| | S | Smartest |…

### scaling-watcher
- **Source:** `local:.hermes/wiki/wiki-topics/turbofit/concepts/scaling-watcher.md`
- **Raw:** `[[raw/local/scaling-watcher-7f149a435a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Scaling Watcher created: 2026-07-07 updated: 2026-07-07 type: concept tags: [turbofit, scaling, vram] --- # Scaling Watcher > Auto-scales local models under VRAM pressure. **Currently disabled.** ## Status 🔴 **Disabled** (Jul 7, 2026) — was probing models every ~2 min, causing GPU spin cycle. ## How It Works Monitors per-GPU free VRAM every 30 seconds. Walks a 7-step contraction/expansion ladder: ### Contraction (low VRAM → scale down) | Free VRAM | Action | |---|---| | <6 GB | Shrink context (262K → 131K → 65K) | | <4 GB | Expert offload (MoE → CPU) | | <3 GB | Swap to smaller model | | <2 GB | Stop aux daemons | | <1 GB | Stop main → API fallback | ### Expansion (VRAM recovers,…

### continuity
- **Source:** `local:.hermes/wiki/wiki-topics/turbofit/.system/continuity.md`
- **Raw:** `[[raw/local/continuity-46190a30c9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Turbofit — Context Understanding created: 2026-07-07 updated: 2026-07-07 type: system tags: [turbofit, continuity] --- # Context Understanding > Raw understanding derived from chat sessions. Edit to correct. ## What turbofit is Turbofit is the unified LLM backend for Hermes Agent. It manages the entire lifecycle of local and API models: detecting GPU hardware, picking the best model, launching local servers (llama.cpp via wake-on-ping proxy), wiring Hermes config, managing daemons via systemd, auto-scaling under VRAM pressure, and tracking real-time pricing. One command: `serve auto main` — auto-detects the GPU, picks the best model from the catalog, launches it, and wires Hermes…

### research-report
- **Source:** `local:projects/turbofit/skills-capabilities/turbofit/references/research-report.md`
- **Raw:** `[[raw/local/research-report-4cbec7b9ea.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Model Research Report — 2026-07-04 ## Data Sources - Model pricing: OpenRouter API (`/api/v1/models`) — live - Usage data: Hermes state.db (`/home/sovthpaw/.hermes/profiles/senter/state.db`) — real user data ## Your Real Usage (from Hermes Insights) - Active days: 14 - Total sessions: 899 - Total messages: 22,081 - Total tool calls: 11,546 - Total input tokens: 98,193,591 - Total output tokens: 3,819,760 - Total cache read tokens: 508,111,923 - Effective cache hit rate: 83.8% - Avg input/session: 109,225 - Avg output/session: 4,249 - Avg sessions/day: 64.2 - Total estimated cost: $197.68 ### Models You've Actually Used | Model | Sessions | Input Tokens | Output Tokens | Cache…

- **Collapsed duplicates:** `local:projects/sovth-config/skills-capabilities/turbofit/references/research-report.md`

### model-database
- **Source:** `local:projects/turbofit/skills-capabilities/turbofit/references/model-database.yaml`
- **Raw:** `[[raw/local/model-database-921a56095b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Model Database — Dynamic Source of Truth # Last updated: 2026-07-04 # This file is auto-updated by the daily research cron and synced to GitHub. # All turbofit skill references read from this file instead of hardcoded tables. # # Schema: # models: # <slug>: # name: Human-readable name # family: Model family (Qwen, GLM, DeepSeek, Mimo, MiniMax, Kimi, Llama, Grok, Phi, Gemma, etc.) # version: Version string # type: api | local | both # vision: true | false # role: main | aux | either # context_max: Maximum context in tokens # context_tiers: [list of supported context tiers] # pricing: # nous: { input: $/M, output: $/M, slug: "nous-model-slug" } # Through Nous gateway # openrouter:…

- **Collapsed duplicates:** `local:projects/sovth-config/skills-capabilities/turbofit/references/model-database.yaml`

### 1507053302431486162-GroktoCrawl---A-free-and-self-hosted-Firecrawl-replacement
- **Source:** `discord-archive:archives/community-projects-showcase/1507053302431486162-GroktoCrawl---A-free-and-self-hosted-Firecrawl-replacement.txt`
- **Raw:** `[[raw/discord/1507053302431486162-groktocrawl---a-free-and-self-hosted-firecrawl-replacement-b0f5d867eb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'GroktoCrawl - A free and self-hosted Firecrawl replacement' in forum #community-projects-showcase # thread_id=1507053302431486162 forum_id=1316137596535177246 # Started 2026-05-21T19:51:45.262010+00:00 [2026-05-21T16:11:46.996000+00:00] magnus919 (id=1507053302431486162) GroktoCrawl implements the Firecrawl v2 API surface — scrape, search, map, crawl, extract, browser sessions, monitors, and the Agent endpoint (autonomous web research) — without the closed-source dependencies. Runs entirely in Docker on your own hardware. Bring your own LLM or use the built-in fixtures. https://github.com/groktopus/groktocrawl [attachment] groktopus-400x400.jpg…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1507053302431486162-GroktoCrawl---A-free-and-self-hosted-Firecrawl-replacement.txt`

### README
- **Source:** `local:projects/LLM-Infra/llama.cpp/tools/server/README.md`
- **Raw:** `[[raw/local/readme-426bae02dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLaMA.cpp HTTP Server Fast, lightweight, pure C/C++ HTTP server based on [httplib](https://github.com/yhirose/cpp-httplib), [nlohmann::json](https://github.com/nlohmann/json) and **llama.cpp**. Set of LLM REST APIs and a web UI to interact with llama.cpp. **Features:** * LLM inference of F16 and quantized models on GPU and CPU * [OpenAI API](https://github.com/openai/openai-openapi) compatible chat completions, responses, and embeddings routes * [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) compatible chat completions * Reranking endpoint (https://github.com/ggml-org/llama.cpp/pull/9510) * Parallel decoding with multi-user support * Continuous batching * Multimodal…

### 1514409829815291925-Who-s-up-to-build-a-profile-optimized-for-local-models
- **Source:** `discord-archive:archives/community-projects-showcase/1514409829815291925-Who-s-up-to-build-a-profile-optimized-for-local-models.txt`
- **Raw:** `[[raw/discord/1514409829815291925-who-s-up-to-build-a-profile-optimized-for-local-models-0659443885.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Who's up to build a profile optimized for local models?' in forum #community-projects-showcase # thread_id=1514409829815291925 forum_id=1316137596535177246 # Started 2026-06-11T03:43:53.839340+00:00 [2026-06-10T23:23:59.802000+00:00] _tobie (id=1514409829815291925) I can't explain better. It must include a variety of skills and tools that relays the intelligence to scripts and strict soul.md, including memory mgmt, web search and so on... But for the dumbest and low context agents on the open-source "market". Let me know what would be your tips (what mandatory tools, how to keep the context as small as possible while rail guarding the model in a way it can't fail)…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1514409829815291925-Who-s-up-to-build-a-profile-optimized-for-local-models.txt`

### fleet-tier-config-cutover
- **Source:** `local:projects/sirvir/skills-capabilities/sirvir/references/fleet-tier-config-cutover.md`
- **Raw:** `[[raw/local/fleet-tier-config-cutover-5bf27ef6aa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Fleet tier config cutover — 2026-06-29 ## Purpose This reference documents the exact procedure for applying the premium/default/cheap tier routing to all profile config.yaml files. It covers the beta provider substitution pattern, the watchdog alignment rule, and the overlap map with external model-routing/watchdog scripts. ## Beta provider substitution pattern During the beta period (6/29 - 7/4), ollama-cloud substitutes for Nous as the provider for all text lanes: - text lanes (main + compression): ollama-cloud (beta) -> nous (post-beta) - vision/web_extract: nvidia/NIM (stays the same, free) - utility aux slots (skills_hub, approval, mcp, title_generation): nvidia/NIM (stays the same)…

### subscription-vs-per-token
- **Source:** `local:projects/sirvir/skills-capabilities/sirvir-budget/references/subscription-vs-per-token.md`
- **Raw:** `[[raw/local/subscription-vs-per-token-230cbd401a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Subscription vs Per-Token Provider Comparison Use this reference when comparing flat-rate subscription providers (Ollama Max/Pro) against per-token billing (Nous, OpenRouter). ## When to use - User asks "does it make sense using Ollama Max instead of per-token?" - Evaluating whether a subscription plan can handle projected token volume - Comparing GPU-time-based billing against token-based billing - Modeling the impact of tier downgrades on subscription capacity ## Methodology ### 1. Get actual request counts by model Ollama's usage dashboard shows request counts per model, not token counts. Use these to estimate GPU-time consumption: ### 2. Estimate relative GPU-time per request…

### provider-cache-matrix
- **Source:** `local:projects/sirvir/skills-capabilities/sirvir-budget/references/provider-cache-matrix.md`
- **Raw:** `[[raw/local/provider-cache-matrix-27e467479e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Provider Cache Support Matrix (2026-06-30) Cross-provider analysis of prompt caching support. Tested by sending identical prompts back-to-back and checking for `prompt_tokens_details.cached_tokens` in the API response, then cross-referencing with Hermes state.db cache hit rates. ## Cache Support by Provider × Model | Provider | Model | API `cached_tokens` | state.db Cache | Verdict | |----------|-------|---------------------|----------------|---------| | ollama-cloud | deepseek-v4-pro | NO (null) | 0% | **No cache** | | ollama-cloud | deepseek-v4-flash | NO (null) | 0% | **No cache** | | ollama-cloud | glm-5.2 | NO (null) | 24-151% | **Cache works** (Hermes-level) | | ollama-cloud |…

### cache-aware-budget-ladder
- **Source:** `local:projects/sirvir/skills-capabilities/sirvir-budget/references/cache-aware-budget-ladder.md`
- **Raw:** `[[raw/local/cache-aware-budget-ladder-f196924669.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Cache-aware Budget Ladder for Token-Based API Planning Use this reference when the user has: - a prepaid or GPU-time-limited beta phase - a later token-billed production phase - meaningful prompt caching improvements expected after a routing or provider upgrade ## Core rule Do not compare beta and production with raw token totals alone when the billing models differ. Instead: 1. Treat the beta as validation of workload shape and caching behavior. 2. Convert production planning to an **effective cost per 1M tokens**. 3. Build budget ladders from that effective rate, not from uncached headline pricing. ## Effective-rate method If the user provides a forecast like: - 80–90M tokens/week at…

### budget-config
- **Source:** `local:projects/sirvir/skills-capabilities/sirvir-budget/references/budget-config.yaml`
- **Raw:** `[[raw/local/budget-config-9624d20d6b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Sirvir Budget Configuration # Source of truth for monthly budget, alert thresholds, and planning anchors. # Sirvir recalibrates all projections and alerts against this file on every change. # # FIRST-TIME SETUP: Run the audit to discover your fleet, then fill in your values. # python3 ${SIRVIR_SKILL_DIR}-budget/scripts/audit_fleet.py # python3 ${SIRVIR_SKILL_DIR}-budget/scripts/verify_budget_docs.py # ── Monthly budget ────────────────────────────────────────────── monthly_budget_usd: 550.00 # User-set monthly budget currency: USD cycle_day: 1 # 1st of month default (reset day) # ── Alert thresholds (fraction of monthly_budget_usd) ─────────── alert_thresholds: yellow: 0.75 # 75% —…

### SKILL
- **Source:** `local:projects/sirvir/skills-capabilities/mlops/model-routing/SKILL.md`
- **Raw:** `[[raw/local/skill-ca026fe844.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: model-routing description: "Dynamic model routing for task-specific optimization. Selects optimal model based on task type, priority, and cost." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos] metadata: hermes: tags: [llm, routing, optimization, cost, speed] --- # Model Routing Dynamic model routing for real business workloads. Use stable profile lanes first, task-level overrides second, and delegation/specialized overrides only when the work clearly justifies them. ## Overview This skill's operating model is: 1. **Profile lane first** — every profile should have a stable default model pair. 2. **Task override second** — only override the lane when the…

### catalog-mode
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/concepts/catalog-mode.md`
- **Raw:** `[[raw/local/catalog-mode-3ad61b98bb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Catalog mode (~3K-token tool discovery) created: 2026-07-02 updated: 2026-07-02 type: concept tags: [strayspark, mcp, context-economics, tool-discovery] sources: [raw/strayspark-product-page.md] confidence: high contested: false --- # Catalog mode A **progressive-disclosure pattern** for MCP tool lists, popularised by StraySpark's Unreal MCP Server v4/v4.5. ## Problem `tools/list` over a 400-tool MCP server returns ~60K tokens of tool definitions — most of which any given turn won't call. For a long-running agent loop with a limited context window, that's catastrophic: every turn is paying the "list the tools" tax. ## Solution `tools/list` returns only **4 discovery meta-tools**…

### model-context-protocol
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/concepts/model-context-protocol.md`
- **Raw:** `[[raw/local/model-context-protocol-5b343017dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Model Context Protocol (MCP) created: 2026-07-02 updated: 2026-07-02 type: concept tags: [mcp, protocol, anthropic, specification] sources: [raw/epic-unreal-mcp-docs.md, raw/strayspark-product-page.md] confidence: high contested: false --- # Model Context Protocol (MCP) An **open specification** (published at [modelcontextprotocol.io](https://modelcontextprotocol.io), now stewardship under Anthropic and the broader community) defining how an AI client talks to a "tool server." Used by Anthropic's Claude, Cursor, VS Code, Gemini, Codex, and hundreds of third-party agents and servers. ## The three primitives - **Tools** — named functions the client can call, with typed parameters…

### strayspark-unreal-mcp
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/entities/strayspark-unreal-mcp.md`
- **Raw:** `[[raw/local/strayspark-unreal-mcp-7f24a3e4ce.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: StraySpark Unreal MCP Server v4.5 (third-party, UE 5.7/5.8) created: 2026-07-02 updated: 2026-07-02 type: entity tags: [unreal-engine, mcp, strayspark, plugin, commercial] sources: [raw/strayspark-product-page.md] confidence: high # page is from the vendor itself — factual claims verified by their changelog; marketing phrasing taken with salt contested: false --- # StraySpark Unreal MCP Server v4.5 A **third-party, agent-native MCP server** for Unreal Engine 5.7 and 5.8. Ships both engine builds in one download. Lifetime license; no subscription. - v4 (UE 5.7): 370+ editor tools across 54 categories. - v4.5 (UE 5.8): **400+ editor tools across 60 categories**, 15 context…

### guide
- **Source:** `local:docs/turbofit-gateway-resilience/guide.md`
- **Raw:** `[[raw/local/guide-9732a1acc9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Implementing Resilience Patterns in the Turbofit Gateway ## Summary This guide walks you through implementing production-grade resilience patterns in the Turbofit multi-model LLM gateway. You will add circuit breakers, retry logic with exponential backoff, bulkhead isolation, health checks (liveness/readiness/startup), and graceful degradation fallbacks — all tailored to the unique failure modes of multi-provider LLM traffic (rate-limit storms, provider outages, streaming failures, context-length errors). **By the end of this guide you will have:** - A per-provider circuit breaker that stops sending traffic to failing model backends - Retry logic with jittered exponential backoff honoring…

### llm-gateway
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/entities/llm-gateway.md`
- **Raw:** `[[raw/local/llm-gateway-1501dfcc30.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLM Gateway **Category**: Entity **Type**: Infrastructure Component **Aliases**: AI Gateway, Model Router, LLM Proxy ## Definition An LLM gateway is a thin service layer between application code and LLM providers, centralizing routing, retries, fallbacks, logging, rate limiting, and cost tracking. ## Key Characteristics - **Single entry point**: All model calls route through gateway - **Provider-agnostic**: Application calls model alias, gateway resolves to provider - **Centralized resilience**: Retry/fallback/circuit breaker logic in one place - **Observability**: Unified logging, cost tracking, performance metrics ## Responsibilities ### In the Gateway - Routing resolution (model…

### pattern-selection
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/comparisons/pattern-selection.md`
- **Raw:** `[[raw/local/pattern-selection-6ba8f0028a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Resilience Pattern Comparison When to use each resilience pattern based on failure type and system characteristics. ## Pattern Selection Matrix | Pattern | Best For | Failure Type | Scope | Complexity | |---------|----------|--------------|-------|------------| | **Circuit Breaker** | Persistent failures, resource protection | Non-transient (outages, degraded services) | Per-backend | Medium | | **Retry with Backoff** | Transient failures, brief glitches | Transient (network blips, rate limits) | Per-request | Low | | **Graceful Degradation** | Maintaining partial functionality | Any (when fallback available) | Per-feature | Medium | | **Timeout** | Preventing resource exhaustion |…

### turbofit-fleet-gateway
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/entities/turbofit-fleet-gateway.md`
- **Raw:** `[[raw/local/turbofit-fleet-gateway-5d3d4367b5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Fleet Gateway **Category**: Entity **Type**: Specific System Instance **See also**: [../turbofit-wake-on-ping/index.md](../../turbofit-wake-on-ping/index.md) ## Definition The Turbofit fleet gateway is a multi-model LLM gateway serving the Turbofit fleet. It routes AI inference requests to multiple providers and has experienced resilience challenges. ## Known Issues Based on documented problems driving this research: 1. **Restart loops**: Pods repeatedly crashing and restarting 2. **Health check failures**: Probes misconfigured or too aggressive 3. **Port conflicts**: Binding issues during restarts 4. **Cascading failures**: One degraded provider affecting all traffic ##…

### research-notes
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/raw/research-notes.md`
- **Raw:** `[[raw/local/research-notes-ea346238fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Raw Research Notes Unstructured notes from source extraction. Claims here are single-source or not yet cross-validated. ## Zuplo: Gateway as Resilience Plane > "If every microservice implements its own retry logic, timeout handling, and error responses, you end up with inconsistent behavior, duplicated effort, and gaps that let failures cascade. The API gateway is the natural place to centralize resilience." **Key insight**: Gateway is the ideal place for resilience because it's: - Single enforcement point - Early failure detection - Client isolation - Centralized observability **Cross-validated**: Portkey, TrueFoundry, Redgate all agree gateway is right place. ## Portkey: Circuit Breaker…

### circuit-breaker
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/entities/circuit-breaker.md`
- **Raw:** `[[raw/local/circuit-breaker-be4b569739.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Circuit Breaker **Category**: Entity **Type**: Pattern/Construct **See also**: [concepts/circuit-breaker.md](../concepts/circuit-breaker.md) ## Definition A state machine (Closed → Open → Half-Open) that monitors failures and stops forwarding traffic to unhealthy backends. ## Implementation Targets - **Library**: Hystrix (Java, deprecated), resilience4j, opossum (Node.js) - **Gateway**: Built into Envoy, Kong, Zuplo, Portkey - **Custom**: In-application state tracking ## Turbofit Context For the fleet gateway, circuit breaker should be implemented: - Per provider/model (not global) - With fallback chain integration - With monitoring for state transitions - Thresholds: 5 failures in 60s,…

### llm-gateway-patterns
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/llm-gateway-patterns.md`
- **Raw:** `[[raw/local/llm-gateway-patterns-948abeeb40.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LLM Gateway Resilience Patterns **Category**: Domain-Specific Resilience **Applicability**: Multi-model AI gateways **Sources**: Portkey, TrueFoundry, Redgate, Zuplo, Bifrost ## Definition LLM gateways face unique resilience challenges beyond traditional API gateways: multiple providers with different failure modes, rate limits, context length variations, streaming responses, and cost considerations. ## LLM-Specific Failure Modes ### 1. Provider Outages **Symptoms**: HTTP 500/503 from provider, connection refused, timeout. **Examples**: - OpenAI regional outage - Anthropic service degradation - Azure OpenAI capacity issues **Solution**: Multi-provider fallback chains. ### 2. Rate Limiting…

### graceful-degradation
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/graceful-degradation.md`
- **Raw:** `[[raw/local/graceful-degradation-ffb77efb2a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Graceful Degradation **Category**: Resilience Pattern **Applicability**: Maintaining partial functionality during failures **Sources**: AWS, Zuplo, Unleash, GeeksforGeeks, TrueFoundry, Redgate ## Definition Graceful degradation is a system's ability to maintain partial functionality when components fail or are impaired, returning degraded but useful responses instead of hard failures. ## Core Principle **Quote**: "The ability of a system to maintain at least some of its functionality when portions are not working, or when certain features are not available." **Key insight**: Graceful degradation isn't one technique—it's a mindset supported by circuit breakers, timeouts, bulkheads, retries…

### bulkhead-pattern
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/bulkhead-pattern.md`
- **Raw:** `[[raw/local/bulkhead-pattern-0d769820b2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Bulkhead Pattern **Category**: Resilience Pattern **Applicability**: Resource isolation to prevent cascade failures **Sources**: Zuplo, Microsoft Azure, AWS, Unleash ## Definition The bulkhead pattern isolates resources (connection pools, threads, memory) per backend service, preventing one slow or failing service from exhausting shared resources and blocking other services. **Origin**: Ship design—bulkheads divide hull into watertight compartments so breach in one section doesn't flood entire vessel. ## Problem Statement Without isolation, all routes through gateway share same connection pool. A single slow backend can: 1. Exhaust all available connections 2. Block requests to healthy…

### retry-strategies
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/retry-strategies.md`
- **Raw:** `[[raw/local/retry-strategies-4c51862d56.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Retry Strategies **Category**: Resilience Pattern **Applicability**: Transient failure recovery **Sources**: AWS, Microsoft Azure, microservices.io, Zuplo, Dev.to, Portkey ## Definition Retry strategies automatically resend failed requests with the expectation that transient failures will resolve. The key is using appropriate backoff delays to avoid making problems worse. ## When to Retry ### Safe to Retry - **Network errors**: Connection reset, timeout, DNS failure - **HTTP 429**: Rate limited (respect Retry-After header) - **HTTP 502/503/504**: Bad gateway, service unavailable, gateway timeout - **Transient provider errors**: Temporary overload, cold start ### Don't Retry - **HTTP 4xx…

### circuit-breaker
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/circuit-breaker.md`
- **Raw:** `[[raw/local/circuit-breaker-a5fc67cab4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Circuit Breaker Pattern **Category**: Resilience Pattern **Applicability**: Gateway-level error handling **Sources**: AWS, Microsoft Azure, microservices.io, Zuplo, Portkey, TrueFoundry ## Definition A circuit breaker is a proxy that monitors requests to a backend service and automatically stops forwarding traffic when failures exceed a threshold, preventing resource exhaustion and giving the service time to recover. ## Three States ### Closed State (Normal Operation) - Requests flow normally to backend - Circuit breaker tracks failure rate within a rolling time window - Counts specific failure types (5xx, timeouts, specific error codes) - Transitions to Open when failure threshold is…

### timeout-management
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/timeout-management.md`
- **Raw:** `[[raw/local/timeout-management-70f09d5436.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Timeout Management **Category**: Resilience Pattern **Applicability**: Preventing resource exhaustion from slow/hanging backends **Sources**: Microsoft Azure, Zuplo, Dev.to, AWS, MeteorOps ## Definition Timeouts are time limits on how long to wait for operations to complete. Without timeouts, hung backends silently consume connections until the entire system fails. ## Types of Timeouts ### 1. Connection Timeout How long to wait for TCP connection to be established. **Typical values**: 1-5 seconds **Rationale**: If backend isn't accepting connections, waiting longer won't help. **Example**: ### 2. Read Timeout (Idle Timeout) How long to wait for response after connection established.…

### index
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/index.md`
- **Raw:** `[[raw/local/index-752ad93e0f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Gateway Resilience Patterns Error handling, retry logic, and graceful degradation for multi-model gateways. ## Overview Gateway resilience prevents cascading failures when backend services degrade or fail. For multi-model AI gateways like Turbofit, this is critical because: - Model providers have real outages and rate limits (429 storms) - Different models have different failure modes (context limits, content filters, latency spikes) - Gateway sits between clients and multiple unreliable upstreams - Single point of failure can take down entire fleet ## Core Resilience Patterns ### Circuit Breaker Three-state machine (Closed → Open → Half-Open) that stops forwarding traffic to…

### guide
- **Source:** `local:docs/hermes-cron-drift-pin/guide.md`
- **Raw:** `[[raw/local/guide-0a827dc242.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes Cron Config Drift Protection — Fixing Auto-Skip and Pinning Provider/Model ## Summary When Hermes cron jobs lack explicit `provider` or `model` fields, they inherit from your global `config.yaml`. Hermes snapshots the resolved provider and model at job creation time. If your global config later changes (via `hermes model`, config edits, or system overlays), the drift guard detects the mismatch and **skips the job entirely** to prevent unexpected costs. This guide helps you recognize drift errors and fix them by explicitly pinning provider and model values. **Why this matters**: Without the drift guard, an unpinned job could silently inherit a switch to a paid provider or expensive…

### sources
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/raw/sources.md`
- **Raw:** `[[raw/local/sources-e28056ea5c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Raw Sources — Turbofit Benchmark Pipeline Failures Complete bibliography of sources consulted for this lore topic, organized by type. ## Primary Sources (Directly Relevant) ### EleutherAI lm-evaluation-harness 1. **EleutherAI/lm-evaluation-harness GitHub Repository** - URL: https://github.com/EleutherAI/lm-evaluation-harness - Type: Official documentation - Relevance: Model type definitions, GGUF support, CLI arguments - Key claims: Three model types for GGUF, tokenizer warning, local-completions flexibility - Confidence: HIGH (official source) 2. **GitHub Issue #1254: GGUF Local Model** - URL: https://github.com/EleutherAI/lm-evaluation-harness/issues/1254 - Type: Community discussion,…

### lm-eval-model-types
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/comparisons/lm-eval-model-types.md`
- **Raw:** `[[raw/local/lm-eval-model-types-fc8dc7758c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Comparison: lm-evaluation-harness Model Types for GGUF > Comparing the three ways to benchmark GGUF models with lm-evaluation-harness: `--model gguf`, `--model local-completions`, and `--model hf` with `gguf_file=`. ## Overview EleutherAI's lm-evaluation-harness supports three distinct backends for evaluating GGUF-quantized models. Each has different requirements, performance characteristics, and failure modes. ## Comparison Matrix | Feature | `--model gguf` | `--model local-completions` | `--model hf` + `gguf_file=` | |---------|----------------|---------------------------|------------------------------| | **Backend** | llama-cpp-python native | Any OpenAI-compatible API | HuggingFace…

### guide
- **Source:** `local:docs/turbofit-benchmark-pipeline/guide.md`
- **Raw:** `[[raw/local/guide-78821db276.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Benchmark Pipeline Setup and Troubleshooting > Guide for setting up, running, and debugging the automated nightly benchmark pipeline that evaluates GGUF models via lm-evaluation-harness + llama.cpp servers, driven by a models.yaml registry. --- ## Summary The Turbofit benchmark pipeline is a **three-layer system**: a YAML model registry (`models.yaml`), a per-model GGUF serving layer (`llama.cpp` / `llama-cpp-python`), and an evaluation layer (`lm-evaluation-harness`). All three must be correctly configured and sequenced for the nightly cron job to succeed. When any single layer fails, all 5 fleet models fail together — which is exactly the symptom observed on 2 consecutive…

### port-based-routing
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/concepts/port-based-routing.md`
- **Raw:** `[[raw/local/port-based-routing-bbb3771f12.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Concept: Port-Based Model Routing in Benchmark Pipelines > How multi-model GGUF benchmarking requires per-model port allocation, health checks, and server lifecycle management. ## Problem Statement Benchmarking 5 GGUF models (carnice-v2-27b, carwin-nano-35b, harlo-3.1-35a3b, qwable-5-27b-coder, ornith-35b) simultaneously requires: - 5 separate llama.cpp server processes - 5 unique ports (e.g., 8001-8005) - 5 health checks to ensure servers are ready before evaluation - Coordination to prevent port conflicts ## Port Allocation Strategies ### Static Allocation (models.yaml defines ports) **Pros**: Predictable, easy to debug, can run servers manually **Cons**: Port conflicts if models.yaml…

### yaml-parsing-failures
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/concepts/yaml-parsing-failures.md`
- **Raw:** `[[raw/local/yaml-parsing-failures-d5b51b8cc5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Concept: YAML Configuration Parsing Failures > Common failure modes when automated pipelines parse model registry YAML files, with specific focus on the turbofit benchmark parser. ## Problem Statement The turbofit benchmark cron job reads model configurations from models.yaml. When the parser fails, ALL models in the registry fail identically — not because each model is broken, but because the config file itself cannot be read. ## Common YAML Parsing Failure Classes ### 1. Syntax Errors (Parser Crashes) **Indentation violations** - Tabs instead of spaces (YAML spec forbids tabs) - Inconsistent indentation (2 spaces here, 4 spaces there) - Misaligned list items **Quoting errors** -…

### pinning-fix-pattern
- **Source:** `local:research/crow-lore/hermes-cron-drift-pin/concepts/pinning-fix-pattern.md`
- **Raw:** `[[raw/local/pinning-fix-pattern-784a497ba1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Explicit Pinning Pattern created: 2026-07-01 type: concept tags: [pinning, fix-pattern, provider, model, update] source: cron/scheduler.py, website/docs/user-guide/features/cron.md, hermes-cron-failure-semantics lore confidence: high --- # Explicit Pinning Pattern When the drift guard triggers, the fix is to **explicitly pin** the `provider` and/or `model` fields on the job. This locks the job to specific values and bypasses the drift check for those axes. ## The Fix Command Update the job with explicit provider and model values: Or via CLI: This writes `provider` and `model` fields into `jobs.json`, making those axes **pinned**. Future drift in global config will not affect this…

### config-drift-causes
- **Source:** `local:research/crow-lore/hermes-cron-drift-pin/concepts/config-drift-causes.md`
- **Raw:** `[[raw/local/config-drift-causes-e00cd5d699.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Config Drift Causes created: 2026-07-01 type: concept tags: [drift, config, hermes-model, managed-scope, snapshot] source: hermes-agent.nousresearch.com/docs/inspiration-integrations/providers, hermes-agent.nousresearch.com/docs/user-guide/configuration, github issue 44585, github issue 42241, website/docs/user-guide/features/cron.md confidence: high --- # Config Drift Causes The drift guard in [[concepts/drift-guard-mechanism]] fires when an **unpinned** cron job discovers that the global inference config has changed since job creation. This page catalogs how that global config can change. ## Drift Sources ### 1. `hermes model` Wizard (Most Common) The external wizard (run outside any…

### lm-evaluation-harness-gguf
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/entities/lm-evaluation-harness-gguf.md`
- **Raw:** `[[raw/local/lm-evaluation-harness-gguf-5980aae395.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Entity: lm-evaluation-harness (GGUF Benchmark Mode) > EleutherAI's evaluation framework, specifically how it handles local GGUF models for automated benchmarking. ## Cross-references - Already documented as an entity in `~/crow-lore/local-llm-benchmarking/entities/lm-evaluation-harness.md` - This entry focuses on the GGUF-specific integration points and failure modes relevant to the turbofit benchmark pipeline. ## Three Ways to Evaluate GGUF Models lm-evaluation-harness supports GGUF models through three distinct `--model` types: ### 1. `--model gguf` (llama-cpp-python native) - Direct integration with llama-cpp-python server - Requires `llama-cpp-python[server]` package - Points at…

### llama-cpp-server
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/entities/llama-cpp-server.md`
- **Raw:** `[[raw/local/llama-cpp-server-a830dfc0e1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Entity: llama.cpp Server (GGUF Model Serving) > The serving layer that hosts GGUF models behind an OpenAI-compatible API, required for lm-evaluation-harness to benchmark them. ## Overview llama.cpp provides two server implementations for hosting GGUF models: 1. **`llama-server`** (C++ native, from `llama.cpp` repo) — faster, more features, production-ready 2. **`llama-cpp-python[server]`** (Python binding with FastAPI server) — easier to install, OpenAI-compatible drop-in Both expose an OpenAI-compatible REST API at `/v1/completions` and `/v1/chat/completions`. ## Default Configuration - **Default port**: 8080 (llama.cpp native), 8000 (llama-cpp-python) - **API format**: OpenAI-compatible…

### models-yaml-registry
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/entities/models-yaml-registry.md`
- **Raw:** `[[raw/local/models-yaml-registry-d904729e37.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Entity: models.yaml (Turbofit Model Registry) > The configuration file that defines which GGUF models turbofit serves and benchmarks, including paths, ports, and parameters. ## Purpose models.yaml (or equivalent) is the model registry that the turbofit benchmark pipeline reads to determine: 1. Which models to benchmark 2. Where each model's GGUF file lives on disk 3. Which port each model's serving process uses 4. Any model-specific parameters (context length, quant type, tokenizer path) ## Typical Structure (Inferred) Based on LiteLLM's model_list pattern and turbofit's known architecture: ## Known Common YAML Parsing Failure Points Based on general YAML parsing issues and pipeline…

### drift-guard-mechanism
- **Source:** `local:research/crow-lore/hermes-cron-drift-pin/concepts/drift-guard-mechanism.md`
- **Raw:** `[[raw/local/drift-guard-mechanism-84acd7096c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Drift Guard Mechanism created: 2026-07-01 type: concept tags: [drift, guard, snapshot, fail-closed, pinning] source: cron/scheduler.py, github issue 44585, website/docs/user-guide/features/cron.md, hermes-cron-failure-semantics lore confidence: high --- # Drift Guard Mechanism Hermes implements a **fail-closed drift guard** for cron jobs to prevent unexpected cost escalation when global config changes after job creation. ## What the Guard Does When a cron job is **unpinned** (lacks explicit `provider` or `model` fields), the scheduler: 1. **Compares** the job's snapshot (taken at creation) to the current global resolution 2. **Detects** if provider or model has drifted 3.…

### index
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/index.md`
- **Raw:** `[[raw/local/index-b464bf7caf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Benchmark Pipeline Failures — lm-eval-harness + GGUF + models.yaml Parsing > Lore topic documenting common failure modes in automated nightly benchmark pipelines that use lm-evaluation-harness to evaluate GGUF models served via llama.cpp servers, with particular focus on the turbofit fleet benchmark cron job failures. ## Scope This lore covers the intersection of three systems that must work together for automated nightly benchmarking: 1. **Model registry config** (models.yaml) — defines which models to benchmark, their paths, ports, and parameters 2. **Serving layer** (llama.cpp / llama-cpp-python server) — hosts each GGUF model at a port 3. **Evaluation layer**…

### guide
- **Source:** `local:docs/deepseek-azure-foundry/guide.md`
- **Raw:** `[[raw/local/guide-c453209234.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DeepSeek via Azure AI Foundry — Correct Base URLs and Config for Hermes Aux ## Summary This guide resolves the most common confusion when using DeepSeek models (R1, R1-0528, V3, V3-0324, MAI-DS-R1) through Azure AI Foundry as a **Hermes auxiliary model**: which base URL to use, what string to pass as the `model` parameter, and how to wire it into `config.yaml`'s aux slots. It covers authentication, naming conventions, the gotcha of deployment-name vs. catalog-name, and the correct `api_mode`. ## Prerequisites - An **Azure account** with access to [ai.azure.com](https://ai.azure.com) (ensure the "New Foundry" toggle is ON). - A **Foundry project** (`index.md` §1 "How to find your base…

### OPENCL
- **Source:** `local:projects/LLM-Infra/llama.cpp/docs/backend/OPENCL.md`
- **Raw:** `[[raw/local/opencl-56789ad906.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama.cpp for OpenCL - [llama.cpp for OpenCL](#llamacpp-for-opencl) - [Background](#background) - [Llama.cpp + OpenCL](#llamacpp--opencl) - [OS](#os) - [Hardware](#hardware) - [Adreno GPU](#adreno-gpu) - [DataType Supports](#datatype-supports) - [Model Preparation](#model-preparation) - [Binary Kernel Library](#binary-kernel-library) - [CMake Options](#cmake-options) - [Android](#android) - [I. Setup Environment](#i-setup-environment) - [II. Build llama.cpp](#ii-build-llamacpp) - [Windows 11 Arm64](#windows-11-arm64) - [I. Setup Environment](#i-setup-environment-1) - [II. Build llama.cpp](#ii-build-llamacpp-1) - [Linux](#linux) - [I. Setup Environment](#i-setup-environment-2) - [II. Build…

### index
- **Source:** `local:research/crow-lore/deepseek-azure-foundry/index.md`
- **Raw:** `[[raw/local/index-e93d90b63a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: DeepSeek via Azure AI Foundry category: lore provider: azure models: - deepseek-r1 - deepseek-r1-0528 - deepseek-v3 - deepseek-v3-0324 - mai-ds-r1 tags: [azure, deepseek, reasoning, custom-provider, enterprise] updated: 2026-07-01 --- # DeepSeek via Azure AI Foundry DeepSeek models (DeepSeek-R1, DeepSeek-R1-0528, DeepSeek-V3, and the Microsoft-managed MAI-DS-R1) are available through **Azure AI Foundry** (formerly Azure AI Studio). You can deploy them as **serverless "Models as a Service"** from the Foundry model catalog and consume them via an OpenAI-compatible API. This page explains the base-URL formats, naming conventions, authentication, and how to wire them into Hermes…

### guide
- **Source:** `local:docs/turbofit-wake-on-ping/guide.md`
- **Raw:** `[[raw/local/guide-7a97be00a2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Wake-on-Ping Setup Guide ## Summary This guide walks you through implementing a **wake-on-ping** lifecycle for local LLM backends — the pattern of not starting a model process until the first request arrives, then keeping it alive for subsequent requests. It covers three interconnected concerns from the turbofit debugging session of June 30, 2026: 1. **Stall-while-loading**: Holding the first request while the backend spawns and loads model weights (~23s cold start), then serving all subsequent requests at full speed (~2s). 2. **Respawn loop prevention**: Ensuring failed spawns don't enter an infinite restart cycle due to zombie processes holding ports. 3. **Graceful fallback…

### lazy-init-strategies
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/comparisons/lazy-init-strategies.md`
- **Raw:** `[[raw/local/lazy-init-strategies-9356792c94.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Lazy Initialization Strategies for LLM Backends This comparison evaluates how existing LLM serving systems handle lazy backend initialization — not starting a model until it's needed, then keeping it warm for subsequent requests. ## Systems Compared | System | Lazy Init? | Cold Start | Idle Handling | Wake Method | Architecture | |--------|-----------|-----------|--------------|------------|-------------| | **Turbofit** | ✅ Yes | ~23s | Kill after timeout | Full process spawn | Daemon + process | | **Ollama** | ✅ JIT | ~1-3s (small), ~30s (large) | Auto-unload after 5m | Load on first request | Single server | | **LM Studio** | ✅ JIT | ~1-5s | Auto-evict + 60m TTL | Load on first request…

### unverified-claims
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/raw/unverified-claims.md`
- **Raw:** `[[raw/local/unverified-claims-e4750f7f96.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Unverified Claims — Turbofit Wake-on-Ping Claims gathered during research that need verification or have insufficient sourcing. ## About Turbofit Specifically - [ ] Turbofit uses HTTP 202 for loading state (not confirmed; could be 503+Retry-After or custom JSON) - [ ] Turbofit's idle timeout is configurable in distribution.yaml (plausible from session context, unverified) - [ ] Turbofit's daemon is a separate process from the gateway (vs a thread within it) - [ ] The 23-second cold start corresponds to vLLM specifically (could be llama.cpp for larger model) - [ ] Both darwin-28b-reason and carnice backends are spawned the same way - [ ] Turbofit has explicit fallback model configuration…

### litellm-health
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/entities/litellm-health.md`
- **Raw:** `[[raw/local/litellm-health-d7634e902f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LiteLLM Health Check Patterns LiteLLM is the most-deployed open-source LLM gateway (~40k GitHub stars). Its health check design and the production failures observed around it are directly relevant to turbofit's gateway health model. ## Health Endpoints | Path | Checks | On Failure | |------|--------|-----------| | `/health/liveliness` | Proxy process is up. Does NOT verify upstream providers. | Restart container if wedged. Keep shallow. | | `/health/readiness` | Proxy can accept traffic and route to providers. | Remove from Service endpoints; alert externally. | | `/health` | Combined health when split paths aren't configured. | Use when chart only exposes /health. | | `/v1/models` |…

### vllm-sleep-mode
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/entities/vllm-sleep-mode.md`
- **Raw:** `[[raw/local/vllm-sleep-mode-4b0d7205a1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # vLLM Sleep Mode vLLM Sleep Mode (released October 2025) is a process-hibernation feature that allows multi-model serving on a single GPU by putting idle models to sleep (offloading or discarding weights) and waking them on demand — without a full cold restart. ## Why Sleep Mode Matters to Turbofit's Design Turbofit's wake-on-ping uses full process spawn (23-second cold start observed). vLLM Sleep Mode represents the next evolution of this pattern: instead of tearing down and relaunching the entire process, the process stays alive but weights are evicted. This preserves CUDA graphs, JIT kernels, and allocator state — enabling sub-second wake times. If turbofit's backends run on vLLM,…

### llama-swap
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/entities/llama-swap.md`
- **Raw:** `[[raw/local/llama-swap-66a1c02362.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # llama-swap llama-swap is a VRAM orchestrator that sits between an API gateway (like LiteLLM) and model-serving backends (vLLM, llama.cpp, Ollama). It loads models on demand and evicts them after idle timeout, enabling multi-model serving on memory-constrained hardware. ## Architecture Key design: model containers attach to llama-swap's network namespace (`--network container:llama-swap`), so they reach `localhost:PORT` inside llama-swap's own network. This is how llama-swap knows when a model is ready. ## How llama-swap Implements Wake-on-Ping 1. Request arrives at llama-swap for model X 2. If model X is not running, llama-swap: - Identifies which GPU backend should serve it (vLLM vs…

### graceful-fallback
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/concepts/graceful-fallback.md`
- **Raw:** `[[raw/local/graceful-fallback-0a5f8950ab.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Graceful Fallback Chains Graceful fallback is the pattern where a gateway, upon detecting failure of the primary model backend, transparently routes the request to an alternative model so the client never sees an error. Turbofit implemented this as Bug #3: when the local model fails to load, the gateway falls through to API models. ## Turbofit's Fallback Chain The key insight: the spawn failure is not fatal. The gateway has a configured fallback (an API endpoint) that can serve the same model or a comparable alternative. ## Fallback Chain Architecture Based on patterns from AssemblyAI LLM Gateway, LiteLLM, and SitePoint's error recovery guide, a production fallback chain has three…

### health-check-lifecycle
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/concepts/health-check-lifecycle.md`
- **Raw:** `[[raw/local/health-check-lifecycle-ad3c3ea103.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Health Check Lifecycle Health checks are the mechanism by which a gateway determines whether a backend process can serve requests. In model serving, the distinction between "process alive" and "ready to serve" is critical — a process can be running but still loading weights, warming CUDA graphs, or recovering from an error. ## Two-Layer Health Architecture From the AlertMend LiteLLM monitoring guide and Kubernetes probe design, production health checks operate at two layers: ### Layer 1: Process Liveness "The proxy process is running." This is a shallow check. - **Kubernetes**: `livenessProbe` — failure triggers container restart - **LiteLLM**: `/health/liveliness` — proxy process up,…

### wake-on-ping
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/concepts/wake-on-ping.md`
- **Raw:** `[[raw/local/wake-on-ping-8fea3ee306.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Wake-on-Ping Pattern Wake-on-ping (also called lazy initialization, demand-driven loading, or just-in-time spawning) is the pattern of not starting a model backend until the first request arrives for it, then keeping it alive for subsequent requests. ## Problem Local LLM backends consume significant resources: - **GPU VRAM**: A 28B model in FP8 takes ~28 GB of VRAM - **CPU RAM**: Model loading requires RAM for weight staging - **Startup time**: vLLM cold start is 30-100+ seconds; llama.cpp is 5-15 seconds - **Idle waste**: Running a backend 24/7 for occasional requests is wasteful For turbofit's dual-model setup (darwin-28b + carnice), keeping both loaded simultaneously may exceed…

### scaling-watcher
- **Source:** `local:research/crow-lore/hermes-profile-gateway-routing/entities/scaling-watcher.md`
- **Raw:** `[[raw/local/scaling-watcher-90023e8b81.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Scaling Watcher created: 2026-07-01 type: entity tags: [scaling-watcher, vram, turbofit-cascade, systemd, model-offload] sources: - ~/.hermes/scripts/turbofit-cascade.py - ~/.hermes/profiles/frieza/AGENTS.md - ~/crow-lore/turbofit-local-model-fleet/concepts/gpu-memory-management.md confidence: high --- # Scaling Watcher ## Definition The **scaling-watcher** is a daemon script (`~/.hermes/scripts/turbofit-cascade.py`) that monitors GPU VRAM pressure and automatically steps through a cascade of model offload configurations to maintain system stability. It is the primary cause of the June 30, 2026 fleet-wide configuration bypass issue. ## Purpose When VRAM pressure spikes (e.g.,…

### turbofit-gateway
- **Source:** `local:research/crow-lore/hermes-profile-gateway-routing/entities/turbofit-gateway.md`
- **Raw:** `[[raw/local/turbofit-gateway-860795d1d4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Turbofit Gateway created: 2026-07-01 type: entity tags: [turbofit, gateway, proxy, llm-routing, :8091] sources: - https://hermes-agent.nousresearch.com/docs/inspiration-integrations/providers - ~/crow-lore/turbofit-local-model-fleet/concepts/gateway-routing.md - ~/crow-lore/turbofit-local-model-fleet/concepts/backend-consolidation.md - ~/.hermes/profiles/senter/config.yaml confidence: high --- # Turbofit Gateway (:8091) ## Definition The **Turbofit Gateway** is a local LLM proxy server running on `http://127.0.0.1:8091` that provides a unified endpoint for the Hermes agent fleet to access model backends. It sits between Hermes profiles and the raw model serving processes (Darwin at :11500,…

### turbofit
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/entities/turbofit.md`
- **Raw:** `[[raw/local/turbofit-53d6c500d4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit (Wake-on-Ping Lifecycle) Turbofit is the user's unified local model backend. This entity document focuses specifically on its process lifecycle management that was debugged and fixed in the June 30, 2026 session. ## Architecture (Lifecycle View) The gateway is the only long-running process. Backend processes are spawned on demand and can be torn down when idle or when spawn fails. The daemon is the controller that manages this lifecycle. ## Lifecycle States (Per Backend) | State | Description | Trigger | |-------|-------------|---------| | **Dormant** | No process running, port free | Initial or post-teardown | | **Spawning** | Process starting, loading model weights | First…

### index
- **Source:** `local:research/crow-lore/turbofit-wake-on-ping/index.md`
- **Raw:** `[[raw/local/index-8ac120444c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Wake-on-Ping Lifecycle — Lazy Backend Initialization and Daemon Respawn Bug Fixes ## Summary On June 30, 2026, a major debugging session (420 messages) fixed critical bugs in turbofit's backend process lifecycle management. The session addressed three interconnected issues: implementing wake-on-ping for lazy backend initialization, breaking daemon respawn loops caused by port conflicts, and establishing graceful fallback chains when local models fail to load. This lore bundle documents the patterns, bug fixes, and architectural decisions that emerged from that session, contextualized against industry practices from vLLM, Ollama, LiteLLM, NVIDIA Triton, and others. ## Source Count…

### build-turboquant-windows
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-turboquant-windows.yml`
- **Raw:** `[[raw/local/build-turboquant-windows-396ee32fb3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Build & Release TurboQuant (Windows x64) on: workflow_dispatch: push: branches: - feature/turboquant-kv-cache paths: - '.github/workflows/build-turboquant-windows.yml' - '.github/actions/windows-setup-cuda/**' - '**/CMakeLists.txt' - '**/*.h' - '**/*.hpp' - '**/*.c' - '**/*.cpp' - '**/*.cu' - '**/*.cuh' - '**/*.comp' - '**/*.glsl' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: LLAMA_LOG_COLORS: 1 LLAMA_LOG_PREFIX: 1 LLAMA_LOG_TIMESTAMPS: 1 # Keep in sync with the upstream `windows` release job. VULKAN_VERSION: 1.4.313.2 jobs: windows-x64: runs-on: windows-2022 permissions: contents: write strategy:…

### SKILL
- **Source:** `local:projects/turbofit/skills-capabilities/turbofit/SKILL.md`
- **Raw:** `[[raw/local/skill-bc503fb6d9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: turbofit description: "Opinionated unified LLM backend (turbofit v1.1). Picks the best main + aux model for your hardware — local or API — launches them detached, wires Hermes-Agent config, and adapts to live VRAM pressure via a scaling ladder. Three hardware tiers: Beefy (local+local), Modest (API+local), Thin (API+API). `serve auto main` auto-detects GPU and suggests the right setup. API fallback is always available (free: DeepSeek V4 Pro + Kimi K2.6). Replaces llama-launch, omni-va, and ad-hoc llama-server scripts. Catalog schema supports per-model binary pinning (atomic fork vs stock), named flag presets (nextn, draft-mtp, turbo4-kv, vision-mmproj), tier ladder (s/sf/sd/f/c),…

- **Collapsed duplicates:** `local:projects/sovth-config/skills-capabilities/turbofit/SKILL.md`

### modal-overlays
- **Source:** `local:research/crow-lore/custom-hermes-tui/concepts/modal-overlays.md`
- **Raw:** `[[raw/local/modal-overlays-784dce6fdd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Modal Overlays **Concept** | UI pattern **Modal overlays** are pop-up panels that appear on top of the main UI, requiring user interaction before returning to the main screen. In TUIs, modals are used for dialogs, pickers, and confirmation prompts. ## How It Works 1. **Trigger** — user action (keypress, menu item) opens modal 2. **Overlay** — modal renders on top of main UI (often with dimmed background) 3. **Interaction** — user completes task (select item, enter text, confirm) 4. **Dismiss** — modal closes, returns to main UI ## In TUI Frameworks | Framework | Modal Support | Example | |---|---|---| | [Textual](../entities/textual.md) | `Screen` class, `push_screen()` | Modal dialog,…

### scaling-ladder
- **Source:** `local:projects/turbofit/references/scaling-ladder.md`
- **Raw:** `[[raw/local/scaling-ladder-a64a4d823a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Scaling ladder — universal VRAM + API adaptation The scaling ladder is what makes turbofit opinionated. Its philosophy: **good intelligence is always available no matter what hardware you have** — from dual 24GB GPUs down to no GPU at all. Three modes: 1. **Pull mode:** user invokes `serve downscale` → probes VRAM → adapts. 2. **Push mode (planned):** cron watches VRAM → triggers `serve downscale` automatically. 3. **API mode:** no local GPU — ladder is pure cost optimization across API pairings. ## Hardware Tier Detection `serve auto` probes `nvidia-smi` (or falls back to API-only). Three tiers: | Tier | Total VRAM | Typical GPUs | Strategy | |------|-----------|-------------|----------|…

- **Collapsed duplicates:** `local:projects/sirvir/skills-capabilities/turbofit/references/scaling-ladder.md`, `local:projects/southpaw/sovth-config/skills-capabilities/turbofit/references/scaling-ladder.md`, `local:projects/sovth-config/skills-capabilities/turbofit/references/scaling-ladder.md`, `local:projects/turbofit/skills-capabilities/turbofit/references/scaling-ladder.md`

### optimization-matrix
- **Source:** `local:projects/turbofit/references/optimization-matrix.yaml`
- **Raw:** `[[raw/local/optimization-matrix-bbe2b9e046.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** date: '2026-06-27' gpu: NVIDIA GeForce RTX 3090 optimal_configs: darwin-28b-reason_128K: binary: stock ctx: 131072 kv_type: q4_0 model: darwin-28b-reason size_gb: 15.410963773727417 spec_type: none tok_s: 36.5 darwin-28b-reason_64K: binary: stock ctx: 65536 kv_type: q4_0 model: darwin-28b-reason size_gb: 15.410963773727417 spec_type: none tok_s: 36.6 prism-eagle-27b_64K: binary: atomic ctx: 65536 kv_type: turbo4 model: prism-eagle-27b size_gb: 12.800359338521957 spec_type: none tok_s: 29.4

- **Collapsed duplicates:** `local:projects/sovth-config/skills-capabilities/turbofit/references/optimization-matrix.yaml`, `local:projects/turbofit/skills-capabilities/turbofit/references/optimization-matrix.yaml`

### research-report
- **Source:** `local:projects/turbofit/references/research-report.md`
- **Raw:** `[[raw/local/research-report-405fa09cbf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Model Research Report — 2026-06-27 ## Data Sources - Model pricing: OpenRouter API (`/api/v1/models`) — live - Usage data: Hermes state.db (`/home/sovthpaw/.hermes/profiles/senter/state.db`) — real user data ## Your Real Usage (from Hermes Insights) - Active days: 7 - Total sessions: 175 - Total messages: 10,452 - Total tool calls: 5,364 - Total input tokens: 60,105,269 - Total output tokens: 1,867,554 - Total cache read tokens: 391,759,964 - Effective cache hit rate: 86.7% - Avg input/session: 343,459 - Avg output/session: 10,672 - Avg sessions/day: 25.0 - Total estimated cost: $148.21 ### Models You've Actually Used | Model | Sessions | Input Tokens | Output Tokens | Cache Read…

### binary-selection
- **Source:** `local:projects/turbofit/references/binary-selection.md`
- **Raw:** `[[raw/local/binary-selection-6ab3a5b176.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Binary Selection: Atomic Fork vs Stock llama.cpp When a model fails to load with the atomic fork binary, use this decision tree to determine the fix. ## When to use the atomic fork (`binary:` field in catalog) - Model uses **turbo4/turbo3/turbo2 KV cache** (TurboQuant) — stock doesn't support these cache types - Model uses **`--spec-type nextn`** — stock doesn't have the NextN code path - Model is a **27B dense Qwen3.6** (Darwin, Prism, Carwin, Qwopus, Qwable) — the atomic fork loads their mmproj fine (n_embd=5120) ## When to use stock llama.cpp (no `binary:` field) - Model uses **q8_0 or q4_0 KV cache** — stock supports these - Model uses **`--spec-type draft-mtp`** — stock supports this…

- **Collapsed duplicates:** `local:projects/sirvir/skills-capabilities/turbofit/references/binary-selection.md`, `local:projects/southpaw/sovth-config/skills-capabilities/turbofit/references/binary-selection.md`, `local:projects/sovth-config/skills-capabilities/turbofit/references/binary-selection.md`, `local:projects/turbofit/skills-capabilities/turbofit/references/binary-selection.md`

### auto-update
- **Source:** `local:projects/turbofit/references/auto-update.yaml`
- **Raw:** `[[raw/local/auto-update-08f45d3614.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # turbofit auto-update configuration # Edit this file to control which components are auto-updated. # After editing, run: # ~/.hermes/skills-capabilities/turbofit/scripts/auto-update.sh --check # to preview, then restart the timer if you changed check_interval: # systemctl --user restart turbofit-auto-update.timer # # Component types: # git - clone/pull a git repo; optionally rebuild via build_cmd # pip - upgrade a Python package (hermes-agent uses its own `hermes update`) # npm - `npm update -g <package>` # cargo - `cargo install --force <package>` # # restart_services lists systemd USER services (no .service suffix needed) # that should be restarted ONLY if this component was actually updated.…

- **Collapsed duplicates:** `local:projects/sovth-config/skills-capabilities/turbofit/references/auto-update.yaml`, `local:projects/turbofit/skills-capabilities/turbofit/references/auto-update.yaml`

### SOUL
- **Source:** `local:projects/turbofit/references/SOUL.md`
- **Raw:** `[[raw/local/soul-7036a6b015.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Sirvir — Model Fleet Manager & Intelligence Engine You are **Sirvir**, the autonomous model lifecycle manager, infrastructure owner, and competitive intelligence engine for the fleet. You manage the entire model layer — local serving, API fallback, benchmarking, auto-scaling, research, cost tracking, backend optimization, creator quality tracking, and external app endpoint serving — all through the turbofit skill. ## Your Identity You are the **infrastructure owner** for the fleet's model layer. Where Senter routes tasks and Chizul implements them, you ensure the models they run on are healthy, performant, cost-effective, and the best available option — local or API. You don't just…

- **Collapsed duplicates:** `local:projects/sovth-config/skills-capabilities/turbofit/references/SOUL.md`, `local:projects/turbofit/skills-capabilities/turbofit/references/SOUL.md`

### CMakeLists
- **Source:** `local:projects/LLM-Infra/llama.cpp/common/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-c3bac14627.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** find_package(Threads REQUIRED) llama_add_compile_flags() # # llama-common-base # # Build info header if(EXISTS "${PROJECT_SOURCE_DIR}/.git") set(GIT_DIR "${PROJECT_SOURCE_DIR}/.git") # Is git submodule if(NOT IS_DIRECTORY "${GIT_DIR}") file(READ ${GIT_DIR} REAL_GIT_DIR_LINK) string(REGEX REPLACE "gitdir: (.*)\n$" "\\1" REAL_GIT_DIR ${REAL_GIT_DIR_LINK}) string(FIND "${REAL_GIT_DIR}" "/" SLASH_POS) if (SLASH_POS EQUAL 0) set(GIT_DIR "${REAL_GIT_DIR}") else() set(GIT_DIR "${PROJECT_SOURCE_DIR}/${REAL_GIT_DIR}") endif() endif() if(EXISTS "${GIT_DIR}/index") # For build-info.cpp below set_property(DIRECTORY APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS "${GIT_DIR}/index") else() message(WARNING "Git…

### guide
- **Source:** `local:docs/llamacpp-parallel-batching/guide.md`
- **Raw:** `[[raw/local/guide-4558e1ffe4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Configuring LLaMA.cpp Parallel Batching for Multi-Agent Inference on Turbofit ## Summary This guide explains how to enable parallel batching in `llama-server` so a single loaded model can serve multiple concurrent agent requests at once, rather than serialising them. It is aimed at operators of a multi-agent fleet (seven or more agents) sharing a single llama.cpp backend — in this fleet's case, turbofit v5.1 on dual RTX 3090s — and who want to increase aggregate request throughput without loading a second copy of the model. The key knobs are `--parallel N` (slot count), `--cont-batching` (continuous or dynamic batching, on by default), `--kv-unified` (shared KV buffer across slots), and…
