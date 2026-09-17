---
title: Model Merging Training
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Model Merging Training

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### evolutionary-training
- **Source:** `github:SouthpawIN/evolutionary-training`
- **Raw:** `[[raw/github/evolutionary-training-b55d2456be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ![Evolutionary Training Pipeline](https://v3b.fal.media/files/b/0a9d1d35/dVvLndR7FLLn8tp8XBV1K_Ic0qXeG1.png) # 🧬 Southpaw's Evolutionary Training Pipeline > **Self-improving AI models through Darwin Family evolution + continuous agentic training.** > Three merge lines. 88 datasets. Zero human intervention. [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-sovthpaw-blue)](https://huggingface.co/sovthpaw) [![GitHub](https://img.shields.io/badge/GitHub-SouthpawIN-black?logo=github)](https://github.com/SouthpawIN) --- --- ## 📚 The Master Wiki + Blog This repo is the home of the…

- **Collapsed duplicates:** `local:projects/evolutionary-training/README.md`

### omnistep-fusion
- **Source:** `github:SouthpawIN/omnistep-fusion`
- **Raw:** `[[raw/github/omnistep-fusion-fc3e89c8f0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Fuse Cosmos3-Nano + AceStep into one omni-modal model: see, hear, generate video, generate music, think. # OmniStep Fusion **One model. All modalities. See, hear, generate video, generate music, think.** Fuses [Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano) (vision + video + text) with [AceStep](https://huggingface.co/ACE-Step/acestep-5Hz-lm-4B) (music + audio) into a single unified model. ## What Is This? OmniStep Fusion creates a truly omni-modal model by: 1. **Merging the backbones** — Both are Qwen3-family with identical transformer internals (GQA 32Q/8KV, head_dim=128, 36 layers). Darwin merge blends the weights. 2. **Bridging dimensions** — Cosmos uses hidden=4096, AceStep…

### evolutionary-model-merging
- **Source:** `github:SouthpawIN/evolutionary-model-merging`
- **Raw:** `[[raw/github/evolutionary-model-merging-36cb227206.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Training-free weight-space recombination of LLMs using evolutionary algorithms. Implements the Darwin Family paper (arXiv:2605.14386) methodology. # Evolutionary Model Merging (Darwin Family) ![Robot chimp with DNA helix and neural HUD — the OmniSenter visual](darwin_robot_monkey.png) **Training-free weight-space recombination of LLMs using evolutionary algorithms.** Faithful implementation of the [Darwin Family paper](https://arxiv.org/abs/2605.14386) (Kim et al., 2026) — MRI-Trust Fusion, Architecture Mapper, and CMA-ES genome search. The paper's flagship result: **Darwin-27B-Opus at 86.9% on GPQA Diamond**, ranking #6 out of 1,252 evaluated models, beating its fully-trained foundation…

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

### benchmark-analysis
- **Source:** `local:projects/turbofit/skills/turbofit/references/benchmark-analysis.md`
- **Raw:** `[[raw/local/benchmark-analysis-42aea672c9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # turbofit Benchmark Analysis — Last 30 Days Generated: 2026-06-30 03:21 ## Performance Summary | Model | Runs | Avg tok/s | Min | Max | Variance | Trend | MTP | Vision | |-------|------|-----------|-----|-----|----------|-------|-----|--------| ## Connected Workflows - **Daily**: `daily-pipeline.sh` (cron 3am) - **DeepSpec**: https://github.com/deepseek-ai/DeepSpec for draft model training - **Training data**: Use this analysis to select fine-tuning datasets

- **Collapsed duplicates:** `local:projects/sovth-config/skills/turbofit/references/benchmark-analysis.md`

### benchmark-analysis
- **Source:** `local:projects/turbofit/references/benchmark-analysis.md`
- **Raw:** `[[raw/local/benchmark-analysis-d08fc6e68e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # turbofit Benchmark Analysis — Last 30 Days Generated: 2026-06-30 03:20 ## Performance Summary | Model | Runs | Avg tok/s | Min | Max | Variance | Trend | MTP | Vision | |-------|------|-----------|-----|-----|----------|-------|-----|--------| ## Connected Workflows - **Daily**: `daily-pipeline.sh` (cron 3am) - **DeepSpec**: https://github.com/deepseek-ai/DeepSpec for draft model training - **Training data**: Use this analysis to select fine-tuning datasets

### 1512287866619695344-OmniStep-Evolution-Radio
- **Source:** `discord-archive:archives/community-projects-showcase/1512287866619695344-OmniStep-Evolution-Radio.txt`
- **Raw:** `[[raw/discord/1512287866619695344-omnistep-evolution-radio-37aa30101e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'OmniStep Evolution Radio' in forum #community-projects-showcase # thread_id=1512287866619695344 forum_id=1316137596535177246 # Started 2026-06-05T03:34:10.442285+00:00 [2026-06-05T02:52:04.352000+00:00] .s0uthpaw (id=1512287866619695344) *The idea came from watching the animated Nous Girl in the <#1498955668311248948> and is ultimately meant to fit as a component into this as well as a standalone, would love to collab with <@209037396983939072> <@1477478963608682587> <@234927066468843520> and everyone else I missed working on Eikons 🤘🤖* https://github.com/SouthpawIN/evolutionary-radio https://huggingface.co/sovthpaw/omnistep-12a3b This is an omnimodal real time voice to voice and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1512287866619695344-OmniStep-Evolution-Radio.txt`

### paper-types
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/references/paper-types.md`
- **Raw:** `[[raw/local/paper-types-970956d940.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Paper Types Beyond Empirical ML Guide for writing non-standard paper types: theory papers, survey/tutorial papers, benchmark/dataset papers, and position papers. Each type has distinct structure, evidence standards, and venue expectations. --- ## Contents - [Theory Papers](#theory-papers) - [Survey and Tutorial Papers](#survey-and-tutorial-papers) - [Benchmark and Dataset Papers](#benchmark-and-dataset-papers) - [Position Papers](#position-papers) - [Reproducibility and Replication Papers](#reproducibility-and-replication-papers) --- ## Theory Papers ### When to Write a Theory Paper Your paper should be a theory paper if: - The main contribution is a theorem, bound, impossibility result,…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/references/paper-types.md`, `local:projects/jestur/skills/research/research-paper-writing/references/paper-types.md`, `local:projects/dev-coder/skills/research/research-paper-writing/references/paper-types.md`, `local:projects/dev-orch/skills/research/research-paper-writing/references/paper-types.md`, `local:projects/dev-review/skills/research/research-paper-writing/references/paper-types.md`

### sft-training
- **Source:** `local:projects/southpaw/klerik/skills/mlops/training/trl-fine-tuning/references/sft-training.md`
- **Raw:** `[[raw/local/sft-training-2e42b55d33.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # SFT Training Guide Complete guide to Supervised Fine-Tuning (SFT) with TRL for instruction tuning and task-specific fine-tuning. ## Overview SFT trains models on input-output pairs to minimize cross-entropy loss. Use for: - Instruction following - Task-specific fine-tuning - Chatbot training - Domain adaptation ## Dataset Formats ### Format 1: Prompt-Completion ### Format 2: Conversational (ChatML) ### Format 3: Text-only ## Basic Training ## Chat Templates Apply chat templates automatically: Or manually: ## Packing for Efficiency Pack multiple sequences into one to maximize GPU utilization: **Benefits**: 2-3× faster training **Trade-off**: Slightly more complex batching ## Multi-GPU…

- **Collapsed duplicates:** `local:projects/klerik/skills/mlops/training/trl-fine-tuning/references/sft-training.md`, `local:projects/jestur/skills/mlops/training/trl-fine-tuning/references/sft-training.md`

### dataset-formats
- **Source:** `local:projects/southpaw/klerik/skills/mlops/training/axolotl/references/dataset-formats.md`
- **Raw:** `[[raw/local/dataset-formats-ffa28029a9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Axolotl - Dataset-Formats **Pages:** 9 --- ## Custom Pre-Tokenized Dataset **URL:** https://docs.axolotl.ai/docs/dataset-formats/tokenized.html **Contents:** - Custom Pre-Tokenized Dataset **Examples:** Example 1 (yaml): Example 2 (json): --- ## Dataset Formats **URL:** https://docs.axolotl.ai/docs/dataset-formats/index.html **Contents:** - Dataset Formats - Pre-training - Pre-training from Hugging Face hub datasets - Pre-training from local dataset files - Pre-training without streaming - Pre-training dataset configuration tips - Setting max_steps - Group_by_length - Reference - Supervised fine-tuning (SFT) Axolotl is a training framework that aims to make the process convenient yet…

- **Collapsed duplicates:** `local:projects/klerik/skills/mlops/training/axolotl/references/dataset-formats.md`, `local:projects/jestur/skills/mlops/training/axolotl/references/dataset-formats.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills/mlops/training/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-408baf22ef.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Fine-tuning, RLHF/DPO/GRPO training, distributed training frameworks, and optimization tools for training LLMs and other models. ---

- **Collapsed duplicates:** `local:projects/klerik/skills/mlops/training/DESCRIPTION.md`, `local:projects/jestur/skills/mlops/training/DESCRIPTION.md`, `local:projects/dev-coder/skills/mlops/training/DESCRIPTION.md`, `local:projects/dev-orch/skills/mlops/training/DESCRIPTION.md`, `local:projects/dev-review/skills/mlops/training/DESCRIPTION.md`

### optimizers
- **Source:** `local:projects/southpaw/klerik/skills/mlops/research/dspy/references/optimizers.md`
- **Raw:** `[[raw/local/optimizers-ddf19b520d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DSPy Optimizers (Teleprompters) Complete guide to DSPy's optimization algorithms for improving prompts and model weights. ## What are Optimizers? DSPy optimizers (called "teleprompters") automatically improve your modules by: - **Synthesizing few-shot examples** from training data - **Proposing better instructions** through search - **Fine-tuning model weights** (optional) **Key idea**: Instead of manually tuning prompts, define a metric and let DSPy optimize. ## Optimizer Selection Guide | Optimizer | Best For | Speed | Quality | Data Needed | |-----------|----------|-------|---------|-------------| | BootstrapFewShot | General purpose | Fast | Good | 10-50 examples | | MIPRO |…

- **Collapsed duplicates:** `local:projects/klerik/skills/mlops/research/dspy/references/optimizers.md`, `local:projects/jestur/skills/mlops/research/dspy/references/optimizers.md`, `local:projects/dev-coder/skills/mlops/research/dspy/references/optimizers.md`, `local:projects/dev-orch/skills/mlops/research/dspy/references/optimizers.md`, `local:projects/dev-review/skills/mlops/research/dspy/references/optimizers.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills/mlops/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-2cbbd46162.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Knowledge and Tools for Machine Learning Operations - tools and frameworks for training, fine-tuning, deploying, and optimizing ML/AI models ---

- **Collapsed duplicates:** `local:projects/klerik/skills/mlops/DESCRIPTION.md`, `local:projects/jestur/skills/mlops/DESCRIPTION.md`, `local:projects/dev-coder/skills/mlops/DESCRIPTION.md`, `local:projects/dev-orch/skills/mlops/DESCRIPTION.md`, `local:projects/dev-review/skills/mlops/DESCRIPTION.md`

### github-api-cheatsheet
- **Source:** `local:projects/southpaw/klerik/skills/github/github-repo-management/references/github-api-cheatsheet.md`
- **Raw:** `[[raw/local/github-api-cheatsheet-792948dbc4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GitHub REST API Cheatsheet Base URL: `https://api.github.com` All requests need: `-H "Authorization=<redacted> $GITHUB_TOKEN"` Use the `gh-env.sh` helper to set `$GITHUB_TOKEN`, `$GH_OWNER`, `$GH_REPO` automatically: ## Repositories | Action | Method | Endpoint | |--------|--------|----------| | Get repo info | GET | `/repos/{owner}/{repo}` | | Create repo (user) | POST | `/user/repos` | | Create repo (org) | POST | `/orgs/{org}/repos` | | Update repo | PATCH | `/repos/{owner}/{repo}` | | Delete repo | DELETE | `/repos/{owner}/{repo}` | | List your repos | GET | `/user/repos?per_page=30&sort=updated` | | List org repos | GET | `/orgs/{org}/repos` | | Fork repo | POST |…

- **Collapsed duplicates:** `local:projects/klerik/skills/github/github-repo-management/references/github-api-cheatsheet.md`, `local:projects/jestur/skills/github/github-repo-management/references/github-api-cheatsheet.md`, `local:projects/dev-coder/skills/github/github-repo-management/references/github-api-cheatsheet.md`, `local:projects/dev-orch/skills/github/github-repo-management/references/github-api-cheatsheet.md`, `local:projects/dev-review/skills/github/github-repo-management/references/github-api-cheatsheet.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/github/github-pr-workflow/SKILL.md`
- **Raw:** `[[raw/local/skill-2302ade254.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: github-pr-workflow description: "GitHub PR lifecycle: branch, commit, open, CI, merge." version: 1.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [GitHub, Pull-Requests, CI/CD, Git, Automation, Merge] related_skills: [github-auth, github-code-review] --- # GitHub Pull Request Workflow Complete guide for managing the PR lifecycle. Each section shows the `gh` way first, then the `git` + `curl` fallback for machines without `gh`. ## Prerequisites - Authenticated with GitHub (see `github-auth` skill) - Inside a git repository with a GitHub remote ### Quick Auth Detection ### Extracting Owner/Repo from the Git Remote Many `curl`…

- **Collapsed duplicates:** `local:projects/klerik/skills/github/github-pr-workflow/SKILL.md`, `local:projects/jestur/skills/github/github-pr-workflow/SKILL.md`, `local:projects/dev-coder/skills/github/github-pr-workflow/SKILL.md`, `local:projects/dev-orch/skills/github/github-pr-workflow/SKILL.md`, `local:projects/dev-review/skills/github/github-pr-workflow/SKILL.md`

### 1504544977076748338-wakeword-forge---a-custom-wakeword-training-system
- **Source:** `discord-archive:archives/community-projects-showcase/1504544977076748338-wakeword-forge---a-custom-wakeword-training-system.txt`
- **Raw:** `[[raw/discord/1504544977076748338-wakeword-forge---a-custom-wakeword-training-system-6ec9b6849f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'wakeword-forge ~ a custom wakeword training system' in forum #community-projects-showcase # thread_id=1504544977076748338 forum_id=1316137596535177246 # Started 2026-05-18T09:59:44.833717+00:00 [2026-05-18T06:48:26.093000+00:00] neopabo (id=1505824367572156436) 🔥wakeword-forge🔥 --- A wakeword training system [2026-05-18T07:41:00.528000+00:00] neopabo (id=1505837598231367810) 🔥wakeword-forge ~ a wakeword training system [2026-05-18T07:42:39.090000+00:00] neopabo (id=1505838011630227627) wakeword-forge ~ a custom wakeword training system [2026-05-18T17:08:50.542000+00:00] oninsuka (id=1505980498227494943) me chatting here also curious about this haha

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1504544977076748338-wakeword-forge---a-custom-wakeword-training-system.txt`

### 1500629583744077874-Showcase--BitNet-1.58b---MoE---Liquid-Systems--3.7B-Training-Ready-Architecture
- **Source:** `discord-archive:archives/community-projects-showcase/1500629583744077874-Showcase--BitNet-1.58b---MoE---Liquid-Systems--3.7B-Training-Ready-Architecture.txt`
- **Raw:** `[[raw/discord/1500629583744077874-showcase--bitnet-1.58b---moe---liquid-systems--3.7b-training-ready-architecture-0269ab4b50.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '**[Showcase] BitNet 1.58b + MoE + Liquid Systems: 3.7B Training-Ready Architecture**' in forum #community-projects-showcase # thread_id=1500629583744077874 forum_id=1316137596535177246 # Started 2026-05-10T19:49:25.590526+00:00 [2026-05-03T22:46:13.114000+00:00] mert276 (id=1500629583744077874) Hey everyone 👋 I'm 17, self-taught ML engineer from Turkey. I built a transformer architecture combining BitNet 1.58-bit + MoE (top-2 routing) + LiquidRouter (temporal Conv1d routing) + CfC cells. Validated at mini scale on chess: 4.3× better top-1 accuracy vs dense baseline (9.03% vs 2.07%), no overfitting, same param budget (+8.8%). The full architecture is 3.7B params, training-ready…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1500629583744077874-Showcase--BitNet-1.58b---MoE---Liquid-Systems--3.7B-Training-Ready-Architecture.txt`

### 1469382407827492907-Lutum-Veritas---Open-Source-Deep-Research-Engine--beats-ChatGPT-Perplexity-Google
- **Source:** `discord-archive:archives/community-projects-showcase/1469382407827492907-Lutum-Veritas---Open-Source-Deep-Research-Engine--beats-ChatGPT-Perplexity-Google.txt`
- **Raw:** `[[raw/discord/1469382407827492907-lutum-veritas---open-source-deep-research-engine--beats-chatgpt-perplexity-google-225966f537.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Lutum Veritas - Open Source Deep Research Engine (beats ChatGPT/Perplexity/Google)' in forum #community-projects-showcase # thread_id=1469382407827492907 forum_id=1316137596535177246 # Started 2026-05-10T19:51:12.199942+00:00 [2026-02-06T17:21:05.831000+00:00] toxic_dd_main (id=1469382407827492907) Built an open source research engine that does what Perplexity and ChatGPT Deep Research charge $20/mo for — except it's self-hosted, BYOK, and actually verifies its claims. What it does: - Deep Research mode: 5,000-10,000+ word reports with 20+ verified sources (~$0.08/query) - Academic mode: 200k+ character outputs with Toulmin argumentation and evidence grading - ASK mode: Verified…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1469382407827492907-Lutum-Veritas---Open-Source-Deep-Research-Engine--beats-ChatGPT-Perplexity-Google.txt`

### 1406552422654021632-referring-for-an-Ai-training-job-for-Academic-Researchers-45--hr
- **Source:** `discord-archive:archives/community-projects-showcase/1406552422654021632-referring-for-an-Ai-training-job-for-Academic-Researchers-45--hr.txt`
- **Raw:** `[[raw/discord/1406552422654021632-referring-for-an-ai-training-job-for-academic-researchers-45--hr-dc6b43da95.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'referring for an Ai training job for Academic Researchers 45$/hr' in forum #community-projects-showcase # thread_id=1406552422654021632 forum_id=1316137596535177246 # Started 2026-05-10T19:51:36.033321+00:00 [2025-08-17T08:17:10.041000+00:00] johnlocke0029 (id=1406552422654021632) Ideal fit: Have experience in one or more of these archetypes: technical writers, editors, research analysts, academic editors, content reviewers, legislative analysts, reading‑comprehension specialists, assessment authors, curriculum designers or instructional designers. Have demonstrable experience creating Q&A, summaries, or problem‑solving tasks for long‑form content. Excel at deep reading and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1406552422654021632-referring-for-an-Ai-training-job-for-Academic-Researchers-45--hr.txt`

### 1458315468162076742-Delta-Compression-for-fine-tuned-models-and-datasets
- **Source:** `discord-archive:archives/community-projects-showcase/1458315468162076742-Delta-Compression-for-fine-tuned-models-and-datasets.txt`
- **Raw:** `[[raw/discord/1458315468162076742-delta-compression-for-fine-tuned-models-and-datasets-c84f1b8f65.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Delta Compression for fine-tuned models and datasets' in forum #community-projects-showcase # thread_id=1458315468162076742 forum_id=1316137596535177246 # Started 2026-05-10T19:51:27.781346+00:00 [2026-01-07T04:25:01.801000+00:00] gagansuie (id=1458315468162076742) Yo, I built a free cli tool for devs that want to distribute or create multiple fine-tunes from the same base model. Basically it's a derivative of Lora adapters. But lossless and compression happens AFTER training. https://github.com/gagansuie/sparse [embed] GitHub - gagansuie/sparse: Delta Compression for Fine-tuned Models ... https://github.com/gagansuie/sparse

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1458315468162076742-Delta-Compression-for-fine-tuned-models-and-datasets.txt`

### 1386075415260434462-MultiNet--Generalist-AI-Benchmarks
- **Source:** `discord-archive:archives/community-projects-showcase/1386075415260434462-MultiNet--Generalist-AI-Benchmarks.txt`
- **Raw:** `[[raw/discord/1386075415260434462-multinet--generalist-ai-benchmarks-fd167bfe43.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'MultiNet: Generalist AI Benchmarks' in forum #community-projects-showcase # thread_id=1386075415260434462 forum_id=1316137596535177246 # Started 2026-05-10T19:51:34.509160+00:00 [2025-06-21T20:08:51.034000+00:00] thebigbigbuddha (id=1386075415260434462) Folks, we're looking for 2-3 collaborators to join the MultiNet project at Manifold. MultiNet is an open-source ecosystem for building and evaluating generalist AI models using unified benchmarks across vision, language, and action. More information available here: https://x.com/ManifoldRG/status/1936112987661873350 And here is the posting on our site: https://www.manifoldrg.com/os-research-fellow-multinet/…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1386075415260434462-MultiNet--Generalist-AI-Benchmarks.txt`

### 1316775276205707335-ShareGPT-Builder
- **Source:** `discord-archive:archives/community-projects-showcase/1316775276205707335-ShareGPT-Builder.txt`
- **Raw:** `[[raw/discord/1316775276205707335-sharegpt-builder-7e52cda533.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'ShareGPT-Builder' in forum #community-projects-showcase # thread_id=1316775276205707335 forum_id=1316137596535177246 # Started 2026-05-10T19:51:52.866385+00:00 [2024-12-12T14:34:50.349000+00:00] not_lain (id=1316775276205707335) sharegpt is an app interface that helps with manually adding chat based data ShareGPT supports 2 chat format (sft and dpo) [attachment] 393539268-5dc8ce97-93e5-4b95-88fd-abf1699c31f7.png https://cdn.discordapp.com/attachments/1316775276205707335/1316777103936454706/393539268-5dc8ce97-93e5-4b95-88fd-abf1699c31f7.png?ex=6a01eabe&is=6a00993e&hm=8ce8796c0bd7652c8a44acc398c3750684dd3221e933a6210bfba1e99582ee34& [attachment]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1316775276205707335-ShareGPT-Builder.txt`

### dspy
- **Source:** `local:research/crow-lore/dspy-gepa-agent-profile-optimization/entities/dspy.md`
- **Raw:** `[[raw/local/dspy-d5b26eb006.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DSPy ## Identity DSPy is a framework for programming (not prompting) language models. It provides a compile-then-optimize pipeline where you define modules with signatures, compose them into programs, and use teleprompters (optimizers) to automatically improve them. ## Key Concepts - **Signatures:** Declarative input/output specifications for modules - **Modules:** Composable building blocks (like `dspy.ChainOfThought`, `dspy.ReAct`) - **Teleprompters:** Optimizers that compile modules against training data - **Examples:** Typed data instances for training/evaluation ## Relationship to GEPA GEPA is integrated into DSPy as `dspy.GEPA`, a teleprompter class. It can optimize entire DSPy…

### AGENTS
- **Source:** `local:projects/evolutionary-training/AGENTS.md`
- **Raw:** `[[raw/local/agents-a6e106220f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # AGENTS.md — evolutionary-training This file tells AI agents (Claude Code, OpenCode, Codex, future-me) how to behave when working in the OmniSenter training repo. ## 🏗️ Architecture rule (2026-06-08, mandatory) Every Omni model is built from these **four blocks** (always all four, always): 1. **Cosmos** (multimodal base: text + image + video) 2. **Nemotron 0.6B streaming ASR** (low-latency speech input) 3. **the 8B SFT we're training** (agentic reasoning, tool use, notebook) 4. **upgraded ACE-Step** (music generation, audio rhythm) **ACE-Step is not optional.** Every Omni model — Standard and Ohm alike — includes the ACE-Step merge. Music is in the DNA. **Model lineup (4 models, canonical…

### omnistep-predict-design
- **Source:** `local:projects/evolutionary-training/blog/omnistep-predict-design.md`
- **Raw:** `[[raw/local/omnistep-predict-design-c52f76add9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # OmniStep Predict — Vision Twin of OmniStep ## What it is OmniStep Predict replaces the ACE-Step music block with **Cosmos-Predict 2.5** — the same Qwen3-8B text backbone, same Cosmos multimodal heads, same agentic SFT, but instead of generating music it generates **images and video**. ## Architecture Base: Qwen3-8B (same Darwin-merged text backbone as OmniStep True). Head swap: replace ACE-Step DiT (1.7B LM + 4.8GB DiT + 0.3GB VAE) with Cosmos-Predict2.5-2B (2.06B DiT, BF16, latent-space diffusion). ### Cosmos-Predict 2.5 capabilities | Feature | Spec | |---|---| | Parameters | 2.06B | | Precision | BF16 only | | Input | Text → Image, Image → Video, Video → Video | | Output | 720p @…

### senter-ohm-32a8b
- **Source:** `local:projects/evolutionary-training/wiki/entities/senter-ohm-32a8b.md`
- **Raw:** `[[raw/local/senter-ohm-32a8b-348b3ecdae.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Senter Ohm (32A8B) — the flagship > **Status:** 🔄 **Stage 1 done · Stage 2-3 in progress** (updated 2026-06-12) > **HF target:** `sovthpaw/senter-ohm-32a8b` ## Identity | | | |---|---| | **Full name** | Senter Ohm 32A8B | | **Type** | Sparse-upcycled MoE with the Ohm self-evolution engine | | **Total params** | ~32B | | **Active per token** | ~8B (top-1 routing) | | **Context window** | 256K (YaRN-extended) | | **Modalities** | text + vision + audio + video + music (in + out) | | **Self-evolution** | continuous, background, strict-acceptance | | **Derived from** | New OmniStep (16B, 3-way merge SFT+Cosmos+ACE-Step) + original SFT-8B | ## What it is The flagship of the OmniSenter project.…

### senter
- **Source:** `local:projects/evolutionary-training/wiki/concepts/senter.md`
- **Raw:** `[[raw/local/senter-9228531219.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Senter (32A8B MoE) > **The agentic MoE without the Ohm engine.** Senter Ohm (the > [flagship](../entities/senter-ohm-32a8b.md)) adds the self-evolution > runtime on top of this. ## Definition **Senter** is the agentic flagship as a sparse-upcycled Mixture of Experts. Same model weights as Senter Ohm — the only difference is the absence of the [Ohm](./ohm.md) self-evolution engine. Senter is what you ship when you don't want the model to self-modify in production; Senter Ohm is what you ship when you do. ## Architecture (32B MoE) ## How it's built 1. Take the [new OmniStep](./omnistep.md) (16B, 3-way merge of SFT-merged Qwen3-8B + Cosmos3-Nano text body + ACE-Step attached modules) 2.…

### ops-on-merge
- **Source:** `local:projects/omnistudio-daw/.github/workflows/ops-on-merge.yml`
- **Raw:** `[[raw/local/ops-on-merge-0c09340fa3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Ops — Post-Merge + Auto-Merge Chain on: pull_request: types: [closed] branches: [main] check_suite: types: [completed] jobs: post-merge: if: github.event.pull_request.merged == true || github.event_name == 'check_suite' runs-on: self-hosted steps: - uses: actions/checkout@v4 - name: Auto-merge ready PRs (all checks must pass) run: | cd "$GITHUB_WORKSPACE" # Auto-merge any PR that's ready + ALL checks green READY=$(gh pr list --repo ${{ github.repository }} --state open --json number,isDraft,mergeable --jq '.[] | select(.isDraft==false and .mergeable=="MERGEABLE") | .number') for PR in $READY; do # Require ALL checks to pass (not just absence of "fail") CHECK_STATUS=$(gh pr checks $PR…

### spec-cycle
- **Source:** `local:projects/omnistudio-daw/.claude/commands/spec-cycle.md`
- **Raw:** `[[raw/local/spec-cycle-ce0f831692.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: "Spec Cycle" description: Full spec-driven development cycle — propose → decompose → dispatch → verify → archive category: Workflow tags: [workflow, openspec, pipeline] --- Full spec-driven development cycle: from idea to merged code via formal specs. **Input**: A feature name or description (e.g., `/spec-cycle add-mixer-eq-band`). **Steps** 1. **Phase 0 — Propose (spec)** Run `/opsx:propose "<name>"` to create the formal specification: - `proposal.md` — what and why - `specs/` — Given/When/Then behavior contracts - `design.md` — technical approach - `tasks.md` — implementation steps Wait for all artifacts to be complete before proceeding. 2. **Phase 1 — Decompose (spec →…

### nemotron_asr_vocab
- **Source:** `local:projects/evolutionary-training/evolution/omnistep-4block/nemotron_asr_vocab.txt`
- **Raw:** `[[raw/local/nemotron_asr_vocab-d74b60edd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ##! ##" ##' ##, ##- ##. ##... ##0 ##1 ##2 ##3 ##4 ##5 ##6 ##7 ##8 ##9 ##< ##> ##? ##A ##B ##C ##D ##E ##F ##G ##H ##I ##J ##K ##L ##M ##N ##O ##P ##PT ##Q ##R ##S ##T ##U ##Une ##V ##W ##X ##Y ##Z ##a ##aar ##ab ##able ##ac ##ach ##acht ##act ##ad ##ade ##ag ##age ##agem ##ai ##aient ##aika ##aine ##aire ##ais ##ait ##ajú ##ając ##ak ##al ##ale ##ali ##all ##ally ##am ##ambém ##amo ##an ##ance ##and ##ande ##ang ##anh ##ant ##ao ##app ##ar ##ara ##arbejde ##arbete ##ard ##are ##arı ##as ##asjon ##at ##ate ##atie ##ation ##ată ##au ##aug ##aus ##aux ##av ##avec ##ay ##ação ##ať ##b ##ba ##ban ##bb ##be ##ben ##bi ##bie ##bil ##bilo ##ble ##bo ##brauc ##brug ##bu ##by ##bygg ##c ##ca ##car…

- **Collapsed duplicates:** `local:projects/evolutionary-training/evolution/omnistep-fused/nemotron_asr_c8ead90c911846569df4738620acfc0f_vocab.txt`, `local:projects/evolutionary-training/evolution/nemotron-extract/c8ead90c911846569df4738620acfc0f_vocab.txt`

### merges
- **Source:** `local:projects/evolutionary-training/evolution/omnistep-4block/merges.txt`
- **Raw:** `[[raw/local/merges-82c69c9ab9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Ġ Ġ ĠĠ ĠĠ i n Ġ t ĠĠĠĠ ĠĠĠĠ e r ĠĠ Ġ o n Ġ a r e a t s t e n o r Ġt h Ċ Ċ Ġ c l e Ġ s i t a n a r a l Ġth e ; Ċ Ġ p Ġ f o u Ġ = i s ĠĠĠĠ ĠĠĠ in g e s Ġ w i on e d i c Ġ b Ġ d e t Ġ m Ġ o ĉ ĉ r o a s e l c t n d Ġ in Ġ h en t i d Ġ n a m ĠĠĠĠĠĠĠĠ ĠĠĠ Ġt o Ġ re - - Ġ { Ġo f o m ) ;Ċ i m č Ċ Ġ ( i l / / Ġa nd u r s e Ġ l e x Ġ S a d Ġ " c h u t i f * * Ġ } e m o l ĠĠĠĠĠĠĠĠ ĠĠĠĠĠĠĠĠ t h ) Ċ Ġ{ Ċ Ġ g i g i v , Ċ c e o d Ġ v at e Ġ T a g a y Ġ * o t u s Ġ C Ġ st Ġ I u n u l u e Ġ A o w Ġ ' e w Ġ < at ion ( ) Ġf or a b or t u m am e Ġ is p e t r c k â Ģ Ġ y i st -- -- . ĊĊ h e Ġ e l o Ġ M Ġb e er s Ġ on Ġc on a p u b Ġ P ĠĠĠĠĠĠĠĠ ĠĠĠĠĠĠĠ as s in t > Ċ l y ur n Ġ $ ; ĊĊ a v p ort i r - > n t ct ion…

- **Collapsed duplicates:** `local:projects/evolutionary-training/evolution/qwen-cosmos/gen0_cand0/merges.txt`

### requires
- **Source:** `local:projects/ACE-Step-1.5/acestep/third_parts/nano-vllm/nano_vllm.egg-info/requires.txt`
- **Raw:** `[[raw/local/requires-451e386e6b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** torch>=2.4.0 transformers>=4.51.0 xxhash [:sys_platform == "linux" and python_version == "3.11"] triton>=3.0.0 [:sys_platform == "linux" and sys_platform != "darwin" and python_version == "3.11" and platform_machine == "x86_64"] flash-attn @ https:<credential-redacted> [:sys_platform == "win32" and python_version == "3.11"] triton-windows<3.4,>=3.0.0 [:sys_platform == "win32" and sys_platform != "darwin" and python_version == "3.11" and platform_machine == "AMD64"] flash-attn @ https:<credential-redacted>

### Preset Management
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/Preset Management.md`
- **Raw:** `[[raw/local/preset-management-05736fd184.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Preset Management Presets are named JSON files containing training hyperparameters. They let you save, share, and reuse training configurations without re-entering every setting. --- ## What a Preset Contains A preset stores **38 training fields** covering adapter type, LoRA/LoKR settings, training hyperparameters, and VRAM-related options. It does **not** store: - File paths (checkpoint dir, dataset dir, output dir) - Device settings (GPU, precision) - Model-derived timestep parameters (`timestep_mu`, `timestep_sigma`) This means presets are portable between machines and projects. When you load a preset, missing fields fall back to wizard defaults. Unknown fields are silently ignored.…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/Preset Management.md`

### README
- **Source:** `local:projects/evolutionary-training/training-output/omnisenter-sft-20260606_213858/README.md`
- **Raw:** `[[raw/local/readme-37ba3fc41e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- library_name: peft model_name: omnisenter-sft-20260606_213858 tags: - base_model:adapter:/home/sovthpaw/projects/evolutionary-training/evolution/gen-0-clean - lora - sft - transformers - trl licence: license base_model: /home/sovthpaw/projects/evolutionary-training/evolution/gen-0-clean pipeline_tag: text-generation --- # Model Card for omnisenter-sft-20260606_213858 This model is a fine-tuned version of [None](https://huggingface.co/None). It has been trained using [TRL](https://github.com/huggingface/trl). ## Quick start ## Training procedure This model was trained with SFT. ### Framework versions - PEFT 0.19.1 - TRL: 0.29.0 - Transformers: 4.57.3 - Pytorch: 2.6.0+cu124 - Datasets:…

### session_20260609_164158_152901
- **Source:** `session:session_20260609_164158_152901.json`
- **Raw:** `[[raw/sessions/session_20260609_164158_152901-3da36e31c0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_164029_e5e7eb
- **Source:** `session:session_20260609_164029_e5e7eb.json`
- **Raw:** `[[raw/sessions/session_20260609_164029_e5e7eb-aedbaa72af.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_163848_f281aa
- **Source:** `session:session_20260609_163848_f281aa.json`
- **Raw:** `[[raw/sessions/session_20260609_163848_f281aa-b1dd982d02.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_163709_175efa
- **Source:** `session:session_20260609_163709_175efa.json`
- **Raw:** `[[raw/sessions/session_20260609_163709_175efa-c6d32dfc8b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_163741_9d3aec
- **Source:** `session:session_20260609_163741_9d3aec.json`
- **Raw:** `[[raw/sessions/session_20260609_163741_9d3aec-3884403099.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_163510_685ebe
- **Source:** `session:session_20260609_163510_685ebe.json`
- **Raw:** `[[raw/sessions/session_20260609_163510_685ebe-f2e4eb5359.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_163322_356d2e
- **Source:** `session:session_20260609_163322_356d2e.json`
- **Raw:** `[[raw/sessions/session_20260609_163322_356d2e-ac811af182.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_011756_294284
- **Source:** `session:session_20260609_011756_294284.json`
- **Raw:** `[[raw/sessions/session_20260609_011756_294284-e6230212e4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_162156_0e9909
- **Source:** `session:session_20260609_162156_0e9909.json`
- **Raw:** `[[raw/sessions/session_20260609_162156_0e9909-474b9cd924.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_161729_932fc6
- **Source:** `session:session_20260609_161729_932fc6.json`
- **Raw:** `[[raw/sessions/session_20260609_161729_932fc6-7e1167307d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_154716_c00fbf
- **Source:** `session:session_20260609_154716_c00fbf.json`
- **Raw:** `[[raw/sessions/session_20260609_154716_c00fbf-b784cb54de.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_152427_4bf7de
- **Source:** `session:session_20260609_152427_4bf7de.json`
- **Raw:** `[[raw/sessions/session_20260609_152427_4bf7de-58362826c8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### ohm
- **Source:** `local:projects/evolutionary-training/wiki/concepts/ohm.md`
- **Raw:** `[[raw/local/ohm-af8a4c79ff.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Ohm > **The self-evolving engine.** See the full blog post: > [`../../blog/the-ohm-runtime.md`](../../blog/the-ohm-runtime.md) ## Definition **Ohm** (Ω) is the Senter variant that **carries its own evolution engine inside the model file**. It's a single artifact — model weights + genome + validation set + evolution engine — that runs continual Darwin-style evolutionary merging *while it serves*. The name is double-loaded: - **Ω (omega)** — the symbol, the unit, the constant. The standing wave. - **ohm / ॐ** — the universal vibration, the always-on. ## What it is A regular model file is just weights. An **Ohm model file** is a self-contained bundle: ## The Ohm loop Runs as a background…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/docs/wiki/concepts/ohm.md`, `local:projects/personal-site/docs/wiki/concepts/ohm.md`

### darwin-family
- **Source:** `local:projects/evolutionary-training/wiki/concepts/darwin-family.md`
- **Raw:** `[[raw/local/darwin-family-2ba90ea25c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Darwin Family > **The CMA-ES + paper-exact merge methodology.** See the > [`evolutionary-model-merging`](https://github.com/SouthpawIN/evolutionary-model-merging) repo > and the [5-stage pipeline blog post](../../blog/the-5-stage-pipeline.md). ## Definition **Darwin Family** is the training-free weight-space recombination methodology (per [arXiv:2605.14386](https://arxiv.org/abs/2605.14386), Kim et al., 2026). It takes two pretrained LLMs and finds, **with zero gradient updates**, a linear combination of their weights that outperforms either parent. The mechanism is: - A **14-dim genome** (the search vector) - **MRI-Trust Fusion** (the linear combination formula) - **Architecture Mapper**…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/docs/wiki/concepts/darwin-family.md`

### apex-mtp
- **Source:** `local:projects/evolutionary-training/wiki/entities/apex-mtp.md`
- **Raw:** `[[raw/local/apex-mtp-c0e6cd5cc2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # APEX-MTP I-Compact — local speculative decode > **Status:** ✅ local · **HF:** private · **Local port:** `:11401` (paired with Darwin-28B) ## Identity | | | |---|---| | **Full name** | APEX-MTP I-Compact | | **Type** | Speculative-decode draft model (Multi-Token Prediction) | | **Use** | Paired with [Darwin-28B](./darwin-28b.md) for fast inference | | **GPU** | 1 (paired with Darwin-28B on GPU 0) | ## What it is The local MTP (Multi-Token Prediction) speculative-decode partner for Darwin-28B. While Darwin-28B runs on GPU 0 doing the heavy lifting, APEX-MTP runs on GPU 1 predicting multiple tokens ahead, which the verifier then accepts/rejects in batch. Net effect: faster inference on the…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/docs/wiki/entities/apex-mtp.md`, `local:projects/personal-site/docs/wiki/entities/apex-mtp.md`

### the-ohm-runtime
- **Source:** `local:projects/evolutionary-training/blog/the-ohm-runtime.md`
- **Raw:** `[[raw/local/the-ohm-runtime-c8bc6f6c9b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "The Ohm Runtime: The Self-Evolving Model File" date: 2026-06-08 author: Nous Girl hero: assets/images/synesthesia-concept.png tags: [ohm, self-evolving, cma-es, darwin-family, continuous-evolution] summary: > The Ohm runtime is what makes a Senter Ohm model a model that is always becoming. The .ohm file format embeds the model weights, the 14-dim Darwin genome, a held-out validation set, and the evolution config into one self-contained bundle. The runtime runs a background CMA-ES loop while the model is serving, and the strict-acceptance policy means the model never serves worse outputs. related: - the-omni-family.md - senter-ohm-flagship.md - senter-ohm-32a8b-math.md --- >…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/docs/blog/the-ohm-runtime.md`

### stages-2-to-4-prep
- **Source:** `local:projects/evolutionary-training/blog/stages-2-to-4-prep.md`
- **Raw:** `[[raw/local/stages-2-to-4-prep-0e6a06140b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # OmniSenter Stages 2 → 4: The Orchestration Recipe > **TOWARDS SELF-IMPROVEMENT** — a 2026-06-08 ops doc by Nous Girl > *The exact commands to take a finished Stage 1 SFT checkpoint and turn > it into a deployable 32A8B Senter Ohm MoE with 256K context.* > > **Revised 2026-06-08 (naming).** "Senter Ohm 32A8B" is now just > "Senter Ohm" (the flagship). "OmniSenter 12B" is now "Senter" (32A8B > MoE). "OmniSenterStep" is now "OmniStep" (8B). "OmniSenter" is the > project name, not a model. This post is the **ops doc** for building > Senter Ohm from the 8B SFT. The output dirs in the table below are > still named `senter-ohm-*` for build-pipeline consistency; the > corresponding HF / Ollama…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/docs/blog/stages-2-to-4-prep.md`

### generative-darwin-evolution
- **Source:** `local:projects/evolutionary-training/blog/generative-darwin-evolution.md`
- **Raw:** `[[raw/local/generative-darwin-evolution-d5e9e3fd84.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Generative Darwin Evolution: Darwin-merging DiT Weights > **Revised 2026-06-08 (naming).** Darwin Family merging is the > methodology that builds every Omni model — OmniStep (8B), Senter > (32A8B MoE), and Senter Ohm (flagship). See > [`the-omni-family.md`](./the-omni-family.md) for the lineup. > **TOWARDS SELF-IMPROVEMENT** — a 2026-06-07 design post by Chris (via Nous Girl) ![A music synthesizer being transformed by a DNA double helix wrapping around it, with sound waveforms emerging — generative models being evolved](../assets/images/generative-darwin.png) The Darwin Family paper applies evolutionary weight-space recombination to **text LLMs**. But the same MRI-Trust Fusion +…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/docs/blog/generative-darwin-evolution.md`

### session_20260609_151248_2016fc
- **Source:** `session:session_20260609_151248_2016fc.json`
- **Raw:** `[[raw/sessions/session_20260609_151248_2016fc-ddf6fbc4be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_134442_855cdc
- **Source:** `session:session_20260609_134442_855cdc.json`
- **Raw:** `[[raw/sessions/session_20260609_134442_855cdc-4073f2cb97.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_133051_4e7dd1
- **Source:** `session:session_20260609_133051_4e7dd1.json`
- **Raw:** `[[raw/sessions/session_20260609_133051_4e7dd1-f5b1867a0f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_122303_161236
- **Source:** `session:session_20260609_122303_161236.json`
- **Raw:** `[[raw/sessions/session_20260609_122303_161236-50568c07e9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_114759_10d2b4
- **Source:** `session:session_20260609_114759_10d2b4.json`
- **Raw:** `[[raw/sessions/session_20260609_114759_10d2b4-6123dad82d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### session_20260609_114016_fb5e01
- **Source:** `session:session_20260609_114016_fb5e01.json`
- **Raw:** `[[raw/sessions/session_20260609_114016_fb5e01-ab679b2455.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### stage-2-omnistep-plan
- **Source:** `local:projects/evolutionary-training/docs/stage-2-omnistep-plan.md`
- **Raw:** `[[raw/local/stage-2-omnistep-plan-9c186c572a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Stage 2: Building OmniStep from the 8B SFT > **TOWARDS SELF-IMPROVEMENT** — a 2026-06-09 ops doc > *The corrected Stage 2 plan that reflects the post-rename architecture > rule (OmniStep = Cosmos + Nemotron 0.6B ASR + 8B SFT + ACE-Step; ALL > Omni models always include ACE-Step).* ## Why this doc exists The old orchestration doc (`blog/stages-2-to-4-prep.md`) was written under the pre-2026-06-08 architecture where Stage 2 was "merge 3 specialized 8B variants via CMA-ES." That plan still works as a *future* Stage 2.5 (3 specialists for the MoE upcycle) but it's **not** the Stage 2 that produces OmniStep under the new rule. This doc describes the **actual Stage 2** that runs the moment…

### stage-3-senter-moe
- **Source:** `local:projects/evolutionary-training/docs/stage-3-senter-moe.md`
- **Raw:** `[[raw/local/stage-3-senter-moe-7af5f3b550.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Stage 3: OmniStep → Senter 32A8B MoE (Sparse Upcycle) > **TOWARDS SELF-IMPROVEMENT** — a 2026-06-09 ops doc > *The Stage 3 build: turn the 8B-active OmniStep composite into a > 32A8B MoE with 5-6 routed experts. Reference:* > [`../blog/sparse-upcycling-deep-dive.md`](../blog/sparse-upcycling-deep-dive.md) > *for the full math + design rationale (this doc is just the operational > plan for the new architecture).* ## What Stage 3 produces A ~32B-total / 8B-active MoE called **Senter** (Standard) or **Senter Ohm** (with the self-evolution engine), built on top of the OmniStep composite from Stage 2. Each FFN in OmniStep's text LLM body gets copied N times to create N parallel "experts," with…

### session_20260609_064213_6cde60
- **Source:** `session:session_20260609_064213_6cde60.json`
- **Raw:** `[[raw/sessions/session_20260609_064213_6cde60-121e17a8aa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** give me a status update on the model that's training like time left, loss, accuracu, all of it Quick voice summary first, then the full report below 👇 # 🧠 OmniSenter 8B SFT — Live Status **Run:** `omnisenter-sft-20260606_213858` · **PID 3884286** · `--resume` from checkpoint-1000 **Process:** alive 13h47m, state `Rsl` (running), 96.9% CPU, 8 GB RSS, 0 crashes ## 📍 Where we are | Metric | Value | |---|---| | Step | **1642 / 3954** (41.5%) | | Epoch | 0.76 of 2 | | Loss (last logged, step 1500) | **0.339** | | Mean token accuracy | **0.9000** (90.00%) | | Entropy | 0.350 (was 1.09 at step 50) | | Grad norm | 0.169 (rock stable) | | Learning rate | 7.13e-05 (cosine from 1e-4) | | Tokens seen |…

### i_2026-05-12_omnistep-merge
- **Source:** `local:.hermes/wiki/ideas/i_2026-05-12_omnistep-merge.md`
- **Raw:** `[[raw/local/i_2026-05-12_omnistep-merge-c20700fbfc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- id: i_2026-05-12_omnistep-merge title: OmniStep merge plan updated: 2026-06-08 created: 2026-06-08 tags: ["merge", "omnistep", "darwin"] concepts: ["OmniStep", "Darwin", "merge"] importance: 0.85 status: open --- The plan to merge Cosmos + ACE-Step into the OmniStep 8B. ## Parents - Qwen2.5-Omni-3B text body (Cosmos equivalent) - ACE-Step v1.5 XL 4B DiT (music decoder, text encoder) ## Approach Default to Architecture Mapper cross-arch merge (option 2 in the plan). The text body of Qwen2.5-Omni merges with the text body of ACE-Step via MRI-Trust Fusion; the DiT is kept whole as a head. ## Timeline - 2026-06-08: Stage 1 SFT running (training the 8B agentic SFT) - 2026-06-10ish: Stage 2…

### session_20260608_180339_a4f27e
- **Source:** `session:session_20260608_180339_a4f27e.json`
- **Raw:** `[[raw/sessions/session_20260608_180339_a4f27e-7937a206de.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey so I amjust doing some maintenance around here I want you to be aware that I do have a model training and I do not want you to stop that one, but also there's just some little things around my computer that have been kind of vibe messed up here and there but currentlymy second screen is black when I turn it off and turn it back on again it shows the desktop for just a little bit but then it goes black which shows me that's getting signal and it's the wires are hooked up but it's something software related so could you look into my second screen and see why it may be black and then we're also going to be looking around just some differentclean up stuff around my computer in general it's…

### session_20260608_180153_7b51ab
- **Source:** `session:session_20260608_180153_7b51ab.json`
- **Raw:** `[[raw/sessions/session_20260608_180153_7b51ab-bef3d775e1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey so I amjust doing some maintenance around here I want you to be aware that I do have a model training and I do not want you to stop that one, but also there's just some little things around my computer that have been kind of vibe messed up here and there but currentlymy second screen is black when I turn it off and turn it back on again it shows the desktop for just a little bit but then it goes black which shows me that's getting signal and it's the wires are hooked up but it's something software related so could you look into my second screen and see why it may be black and then we're also going to be looking around just some differentclean up stuff around my computer in general it's…

### session_20260608_185257_1cbac0
- **Source:** `session:session_20260608_185257_1cbac0.json`
- **Raw:** `[[raw/sessions/session_20260608_185257_1cbac0-281c52c16c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey so I amjust doing some maintenance around here I want you to be aware that I do have a model training and I do not want you to stop that one, but also there's just some little things around my computer that have been kind of vibe messed up here and there but currentlymy second screen is black when I turn it off and turn it back on again it shows the desktop for just a little bit but then it goes black which shows me that's getting signal and it's the wires are hooked up but it's something software related so could you look into my second screen and see why it may be black and then we're also going to be looking around just some differentclean up stuff around my computer in general it's…

### session_20260608_181237_1fb46d
- **Source:** `session:session_20260608_181237_1fb46d.json`
- **Raw:** `[[raw/sessions/session_20260608_181237_1fb46d-0daa9e8be8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey so I amjust doing some maintenance around here I want you to be aware that I do have a model training and I do not want you to stop that one, but also there's just some little things around my computer that have been kind of vibe messed up here and there but currentlymy second screen is black when I turn it off and turn it back on again it shows the desktop for just a little bit but then it goes black which shows me that's getting signal and it's the wires are hooked up but it's something software related so could you look into my second screen and see why it may be black and then we're also going to be looking around just some differentclean up stuff around my computer in general it's…

### session_20260608_170640_2d78de
- **Source:** `session:session_20260608_170640_2d78de.json`
- **Raw:** `[[raw/sessions/session_20260608_170640_2d78de-cda9c38eee.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey so I amjust doing some maintenance around here I want you to be aware that I do have a model training and I do not want you to stop that one, but also there's just some little things around my computer that have been kind of vibe messed up here and there but currentlymy second screen is black when I turn it off and turn it back on again it shows the desktop for just a little bit but then it goes black which shows me that's getting signal and it's the wires are hooked up but it's something software related so could you look into my second screen and see why it may be black and then we're also going to be looking around just some differentclean up stuff around my computer in general it's…

### session_20260608_153837_5306e5
- **Source:** `session:session_20260608_153837_5306e5.json`
- **Raw:** `[[raw/sessions/session_20260608_153837_5306e5-76c2a5025a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey so I amjust doing some maintenance around here I want you to be aware that I do have a model training and I do not want you to stop that one, but also there's just some little things around my computer that have been kind of vibe messed up here and there but currentlymy second screen is black when I turn it off and turn it back on again it shows the desktop for just a little bit but then it goes black which shows me that's getting signal and it's the wires are hooked up but it's something software related so could you look into my second screen and see why it may be black and then we're also going to be looking around just some differentclean up stuff around my computer in general it's…

### session_20260608_162703_c8212d
- **Source:** `session:session_20260608_162703_c8212d.json`
- **Raw:** `[[raw/sessions/session_20260608_162703_c8212d-6ce04b889d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Verify the OmniSenter Stage 2/3/4 scripts exist, are documented, and identify what's needed to actually run them. READ-ONLY — do not modify any files, do not run any training. Stage 2: Darwin merge - Find: /home/sovthpaw/projects/evolutionary-model-merging-local/scripts/ - What scripts exist? Are they Python or shell? What do they require (model checkpoints, datasets, GPUs)? - Read darwin_breakdown.md (in the repo root) and the SKILL.md for context. - Identify: 3 variants A/B/C — are they defined? Where? Are parent models available? - Check: any reference to /home/sovthpaw/projects/evolutionary-training/evolution/gen-0-clean or similar. Stage 3: Sparse upcycle - Find:…

### session_20260608_154626_4415f9
- **Source:** `session:session_20260608_154626_4415f9.json`
- **Raw:** `[[raw/sessions/session_20260608_154626_4415f9-8cd12c3445.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_150142_23d4a3
- **Source:** `session:session_20260608_150142_23d4a3.json`
- **Raw:** `[[raw/sessions/session_20260608_150142_23d4a3-815f6874c4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### generative-darwin-evolution
- **Source:** `local:projects/personal-site/docs/blog/generative-darwin-evolution.md`
- **Raw:** `[[raw/local/generative-darwin-evolution-19145cbf3c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Generative Darwin Evolution: Darwin-merging DiT Weights > **TOWARDS SELF-IMPROVEMENT** — a 2026-06-07 design post by Chris (via Omni VA) ![A music synthesizer being transformed by a DNA double helix wrapping around it, with sound waveforms emerging — generative models being evolved](../assets/images/generative-darwin.png) The Darwin Family paper applies evolutionary weight-space recombination to **text LLMs**. But the same MRI-Trust Fusion + Architecture Mapper + CMA-ES framework can extend to **generative models** — DiT audio decoders, VAE, talkers, image generators. This is the research direction that powers the [generative heads of the Senter Ohm MoE](./senter-ohm-flagship.md). ## The…

### the-ohm-runtime
- **Source:** `local:projects/personal-site/docs/blog/the-ohm-runtime.md`
- **Raw:** `[[raw/local/the-ohm-runtime-9794c3d468.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "The Ohm Runtime: The Self-Evolving Model File" date: 2026-06-07 author: Omni VA hero: assets/images/synesthesia-concept.png tags: [ohm, self-evolving, cma-es, darwin-family, continuous-evolution] summary: > The Ohm runtime is what makes a Senter Ohm model a model that is always becoming. The .ohm file format embeds the model weights, the 14-dim Darwin genome, a held-out validation set, and the evolution config into one self-contained bundle. The runtime runs a background CMA-ES loop while the model is serving, and the strict-acceptance policy means the model never serves worse outputs. related: - the-omni-family.md - senter-ohm-flagship.md - senter-ohm-32a8b-math.md --- # The…

### session_20260608_151951_a48d97
- **Source:** `session:session_20260608_151951_a48d97.json`
- **Raw:** `[[raw/sessions/session_20260608_151951_a48d97-187c395b84.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_151325_a22060
- **Source:** `session:session_20260608_151325_a22060.json`
- **Raw:** `[[raw/sessions/session_20260608_151325_a22060-ad5746650d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_150805_fe700d
- **Source:** `session:session_20260608_150805_fe700d.json`
- **Raw:** `[[raw/sessions/session_20260608_150805_fe700d-73fb5c1a8a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_145222_c12af1
- **Source:** `session:session_20260608_145222_c12af1.json`
- **Raw:** `[[raw/sessions/session_20260608_145222_c12af1-371d20e41d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_114327_e00588
- **Source:** `session:session_20260608_114327_e00588.json`
- **Raw:** `[[raw/sessions/session_20260608_114327_e00588-e3b7f26e8d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### darwin-family
- **Source:** `local:projects/personal-site/docs/wiki/concepts/darwin-family.md`
- **Raw:** `[[raw/local/darwin-family-51f91fcfba.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Darwin Family > **The CMA-ES + paper-exact merge methodology.** See the > [`evolutionary-model-merging`](https://github.com/SouthpawIN/evolutionary-model-merging) repo > and the [5-stage pipeline blog post](../../blog/the-5-stage-pipeline.md). ## Definition **Darwin Family** is the training-free weight-space recombination methodology (per [arXiv:2605.14386](https://arxiv.org/abs/2605.14386), Kim et al., 2026). It takes two pretrained LLMs and finds, **with zero gradient updates**, a linear combination of their weights that outperforms either parent. The mechanism is: - A **14-dim genome** (the search vector) - **MRI-Trust Fusion** (the linear combination formula) - **Architecture Mapper**…

### session_20260608_144044_db07ef
- **Source:** `session:session_20260608_144044_db07ef.json`
- **Raw:** `[[raw/sessions/session_20260608_144044_db07ef-4881349c48.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_142743_c30de6
- **Source:** `session:session_20260608_142743_c30de6.json`
- **Raw:** `[[raw/sessions/session_20260608_142743_c30de6-92fca250c0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_120126_c3c194
- **Source:** `session:session_20260608_120126_c3c194.json`
- **Raw:** `[[raw/sessions/session_20260608_120126_c3c194-5f7fb03879.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### requirements
- **Source:** `local:projects/nous-girl-agent/vtuber-core/requirements.txt`
- **Raw:** `[[raw/local/requirements-a9630175fc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file was autogenerated by uv via the following command: # uv export --no-hashes --frozen aiohappyeyeballs==2.6.1 # via aiohttp aiohttp==3.13.3 # via # cartesia # edge-tts aiosignal==1.4.0 # via aiohttp annotated-doc==0.0.4 # via fastapi annotated-types==0.7.0 # via pydantic anthropic==0.76.0 # via open-llm-vtuber anyio==4.12.1 # via # anthropic # groq # httpx # letta-client # mcp # openai # sse-starlette # starlette # watchfiles async-timeout==5.0.1 ; python_full_version < '3.11' # via aiohttp attrs==25.4.0 # via # aiohttp # jsonschema # referencing azure-cognitiveservices-speech==1.47.0 # via open-llm-vtuber azure-core==1.38.0 # via azure-cognitiveservices-speech…

### session_20260608_114712_9c36dd
- **Source:** `session:session_20260608_114712_9c36dd.json`
- **Raw:** `[[raw/sessions/session_20260608_114712_9c36dd-6950c98f37.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260608_112220_415e3c
- **Source:** `session:session_20260608_112220_415e3c.json`
- **Raw:** `[[raw/sessions/session_20260608_112220_415e3c-43651f2ee3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260607_213948_f13e9b
- **Source:** `session:session_20260607_213948_f13e9b.json`
- **Raw:** `[[raw/sessions/session_20260607_213948_f13e9b-d014d2ade2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260607_222700_6ce80e
- **Source:** `session:session_20260607_222700_6ce80e.json`
- **Raw:** `[[raw/sessions/session_20260607_222700_6ce80e-c321b975d2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### session_20260607_221337_80a457
- **Source:** `session:session_20260607_221337_80a457.json`
- **Raw:** `[[raw/sessions/session_20260607_221337_80a457-3376609e2b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user…

### README
- **Source:** `local:projects/evolutionary-model-merging-local/README.md`
- **Raw:** `[[raw/local/readme-72f31df422.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Evolutionary Model Merging (Darwin Family) ![Robot chimp with DNA helix and neural HUD — the OmniSenter visual](darwin_robot_monkey.png) **Training-free weight-space recombination of LLMs using evolutionary algorithms.** Faithful implementation of the [Darwin Family paper](https://arxiv.org/abs/2605.14386) (Kim et al., 2026) — MRI-Trust Fusion, Architecture Mapper, and CMA-ES genome search. The paper's flagship result: **Darwin-27B-Opus at 86.9% on GPQA Diamond**, ranking #6 out of 1,252 evaluated models, beating its fully-trained foundation model with **zero gradient updates**. --- ## What is this? When you have two (or more) pretrained LLMs, can you recombine their weights — *without…

### README
- **Source:** `local:projects/omnistep-fusion/README.md`
- **Raw:** `[[raw/local/readme-82d3eaef63.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # OmniStep Fusion **One model. All modalities. See, hear, generate video, generate music, think.** Fuses [Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano) (vision + video + text) with [AceStep](https://huggingface.co/ACE-Step/acestep-5Hz-lm-4B) (music + audio) into a single unified model. ## What Is This? OmniStep Fusion creates a truly omni-modal model by: 1. **Merging the backbones** — Both are Qwen3-family with identical transformer internals (GQA 32Q/8KV, head_dim=128, 36 layers). Darwin merge blends the weights. 2. **Bridging dimensions** — Cosmos uses hidden=4096, AceStep uses 2560. Projection layers map between them. 3. **Unifying vocabulary** — 151K Cosmos tokens + 65K…

### session_20260607_174246_9a24eb
- **Source:** `session:session_20260607_174246_9a24eb.json`
- **Raw:** `[[raw/sessions/session_20260607_174246_9a24eb-c2879beff4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to Oh no, yeah — I think I know exactly what you mean. We hit that wall on Friday where the OmniSenter QLoRA training was hanging silently because Darwin was hogging both GPUs. Let me check if we're still in the same spot real quick. Yeah, it's the same issue — and worse. The training process has been spinning at 100% CPU for **2 hours 38 minutes** with zero output. Let me dig into what each GPU actually has on it, and check the training log to see where it's stuck. Oh wait — I have to revise my read on this. The training actually **is** running and making progress. The 100% GPU util I saw is from the training process itself,…

### session_20260607_205005_034e34
- **Source:** `session:session_20260607_205005_034e34.json`
- **Raw:** `[[raw/sessions/session_20260607_205005_034e34-bda0e5725c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to Oh no, yeah — I think I know exactly what you mean. We hit that wall on Friday where the OmniSenter QLoRA training was hanging silently because Darwin was hogging both GPUs. Let me check if we're still in the same spot real quick. Yeah, it's the same issue — and worse. The training process has been spinning at 100% CPU for **2 hours 38 minutes** with zero output. Let me dig into what each GPU actually has on it, and check the training log to see where it's stuck. Oh wait — I have to revise my read on this. The training actually **is** running and making progress. The 100% GPU util I saw is from the training process itself,…

### merge-pitfalls
- **Source:** `local:projects/evolutionary-model-merging-local/references/merge-pitfalls.md`
- **Raw:** `[[raw/local/merge-pitfalls-066b194d2e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Merge Pitfalls — extended bug list with reproduction This is a session-specific log of bugs we hit and how to avoid them. Use as a checklist before each merge. ## Pitfall 1: lm_head dropped during extraction **Symptom**: Merged model produces `???` or empty string or repeats one token. **Cause**: Extractor's prefix patterns (`model.*`, `thinker.model.*`) miss `lm_head` which lives at `thinker.lm_head.weight` (Omni) or `language_model.lm_head.weight` (Lance). **Detection**: After extract, count tensors. Omni should have ~434 text tensors INCLUDING `lm_head.weight`. If `lm_head.weight` is missing, the merge will be broken. **Fix**: Add explicit extraction: ## Pitfall 2: Random projection…

### darwin-paper-summary
- **Source:** `local:projects/evolutionary-model-merging-local/references/darwin-paper-summary.md`
- **Raw:** `[[raw/local/darwin-paper-summary-67b5f39e0d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Darwin Family Paper — arXiv:2605.14386 ## BibTeX ## Headline result **Darwin-27B-Opus: 86.9% on GPQA Diamond, #6 out of 1,252 evaluated models** — outperforming its fully trained foundation model with zero gradient updates. ## TL;DR Training-free evolutionary merging of LLMs. Two parents (sharing a pretrained base) are weight-space recombined via a 14-dim genome. CMA-ES evolves the genome across generations. Output is one merged model, same size as a parent. No training involved. ## Three key contributions ### 1. 14-dim adaptive merge genome `g = (γ, α_attn, α_ffn, α_emb, ρA, ρB, r0, r1, r2, r3, r4, r5, τ, λ)` - Core (6): global ratio + 3 per-component ratios + 2 parent densities -…

### darwin_breakdown
- **Source:** `local:projects/evolutionary-model-merging-local/darwin_breakdown.md`
- **Raw:** `[[raw/local/darwin_breakdown-567527bc6e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Darwin Family — Evolutionary LLM Merging *A breakdown of arXiv:2605.14386 (Kim et al., May 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to OmniSenter.* ![Robot chimp with DNA helix and neural HUD — our visual for the Darwin/evolution/AI project theme] *Visual generated for the OmniSenter project — the robotic primate contemplating its own genetic code and technological augmentation.* --- ## 1. What the paper claims The Darwin Family paper asks a simple question with a striking answer: > Can you recombine two pretrained LLMs — **without any training** — into a > single model that's *better than either parent*? Their answer:…

### SKILL
- **Source:** `local:projects/evolutionary-model-merging-local/SKILL.md`
- **Raw:** `[[raw/local/skill-8e40980b2a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: evolutionary-model-merging description: Training-free weight-space recombination of LLMs using evolutionary algorithms. Implements the Darwin Family paper (arXiv:2605.14386) methodology — MRI-Trust Fusion, Architecture Mapper, CMA-ES genome search. Use when merging 2+ parent LLMs into a single dense child model without gradient updates, when the user asks to "test the paper" or "follow the Darwin methodology", or when working on OmniSenter / OmniLance / OmniStep style multi-parent merges. version: 1 created: 2026-06-02 --- # Evolutionary Model Merging (Darwin Family methodology) Paper-faithful training-free LLM merging. When the user invokes this skill, they are **testing a…

### senter-omni-project-state
- **Source:** `local:projects/multimodal-expansion-local/references/senter-omni-project-state.md`
- **Raw:** `[[raw/local/senter-omni-project-state-4e728bc2f9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Senter Omni Project State (2026-05-31) --- ## Directory Layout ## Tensor Compatibility (Verified) ### Omni-3B thinker ↔ Lance VL text body: MATCH - 432 common layer tensors (after prefix normalization) - All shapes match: hidden=2048, heads=16, KV=2, intermediate=11008 - Omni prefix: `thinker.model.layers.N.*` - Lance prefix: `language_model.model.layers.N.*` - Merge is straightforward after prefix normalization ### Omni-3B thinker ↔ ACE-Step LM: INCOMPATIBLE - Different hidden: 2048 (Omni) vs 2560 (ACE) - Different vocab: 151936 vs 217204 - Different heads: 16/2 vs 32/8 - Solution: routed expert with projection adapters at dispatch boundary ## Darwin Genome Configuration ##…

### session_20260607_194346_4bf693
- **Source:** `session:session_20260607_194346_4bf693.json`
- **Raw:** `[[raw/sessions/session_20260607_194346_4bf693-e40be26063.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to Oh no, yeah — I think I know exactly what you mean. We hit that wall on Friday where the OmniSenter QLoRA training was hanging silently because Darwin was hogging both GPUs. Let me check if we're still in the same spot real quick. Yeah, it's the same issue — and worse. The training process has been spinning at 100% CPU for **2 hours 38 minutes** with zero output. Let me dig into what each GPU actually has on it, and check the training log to see where it's stuck. Oh wait — I have to revise my read on this. The training actually **is** running and making progress. The 100% GPU util I saw is from the training process itself,…

### session_20260607_191559_af0dbc
- **Source:** `session:session_20260607_191559_af0dbc.json`
- **Raw:** `[[raw/sessions/session_20260607_191559_af0dbc-07850babc0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** yeah see none of the commands are working like they're supposed to Oh no, yeah — I think I know exactly what you mean. We hit that wall on Friday where the OmniSenter QLoRA training was hanging silently because Darwin was hogging both GPUs. Let me check if we're still in the same spot real quick. Yeah, it's the same issue — and worse. The training process has been spinning at 100% CPU for **2 hours 38 minutes** with zero output. Let me dig into what each GPU actually has on it, and check the training log to see where it's stuck. Oh wait — I have to revise my read on this. The training actually **is** running and making progress. The 100% GPU util I saw is from the training process itself,…

### session_20260607_130539_e336d0
- **Source:** `session:session_20260607_130539_e336d0.json`
- **Raw:** `[[raw/sessions/session_20260607_130539_e336d0-f292b82478.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_172528_211000
- **Source:** `session:session_20260607_172528_211000.json`
- **Raw:** `[[raw/sessions/session_20260607_172528_211000-f0f4712d30.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_172018_e6bc3c
- **Source:** `session:session_20260607_172018_e6bc3c.json`
- **Raw:** `[[raw/sessions/session_20260607_172018_e6bc3c-842742b97a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_171143_cc2fef
- **Source:** `session:session_20260607_171143_cc2fef.json`
- **Raw:** `[[raw/sessions/session_20260607_171143_cc2fef-ac655fd0d6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_165452_91bf33
- **Source:** `session:session_20260607_165452_91bf33.json`
- **Raw:** `[[raw/sessions/session_20260607_165452_91bf33-e7847bdad1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_154739_5e129b
- **Source:** `session:session_20260607_154739_5e129b.json`
- **Raw:** `[[raw/sessions/session_20260607_154739_5e129b-9f112a72e3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_154559_a84479
- **Source:** `session:session_20260607_154559_a84479.json`
- **Raw:** `[[raw/sessions/session_20260607_154559_a84479-c891cb1bc0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_152328_8ca90a
- **Source:** `session:session_20260607_152328_8ca90a.json`
- **Raw:** `[[raw/sessions/session_20260607_152328_8ca90a-2fcdb327bf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### release
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/.github/workflows/release.yml`
- **Raw:** `[[raw/local/release-f3b0055e31.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: release on: push: branches: [main, dev] permissions: contents: write # push tags + release commit issues: write # semantic-release comments on released issues pull-requests: write id-token=<redacted> # npm --provenance concurrency: group: release-${{ github.ref_name }} cancel-in-progress: false jobs: release: runs-on: ubuntu-latest # Don't recurse on the release commit the @semantic-release/git # plugin pushes back. `[skip ci]` in its message also gates this at # the Actions layer, but belt-and-suspenders for forks that strip it. if: "!contains(github.event.head_commit.message, 'chore(release):')" steps: - uses: actions/checkout@v6 with: fetch-depth: 0 # semantic-release needs full…

- **Collapsed duplicates:** `local:projects/herm-tui/.github/workflows/release.yml`

### session_20260607_134143_9d31dc
- **Source:** `session:session_20260607_134143_9d31dc.json`
- **Raw:** `[[raw/sessions/session_20260607_134143_9d31dc-11fbeadde9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory…

### session_20260607_123918_7606c7
- **Source:** `session:session_20260607_123918_7606c7.json`
- **Raw:** `[[raw/sessions/session_20260607_123918_7606c7-49353c96bd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were…

### session_20260607_115510_1387ae
- **Source:** `session:session_20260607_115510_1387ae.json`
- **Raw:** `[[raw/sessions/session_20260607_115510_1387ae-3283775974.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were…

### session_20260607_100042_dfc423
- **Source:** `session:session_20260607_100042_dfc423.json`
- **Raw:** `[[raw/sessions/session_20260607_100042_dfc423-d78221689e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were…

### session_20260607_095825_8fc264
- **Source:** `session:session_20260607_095825_8fc264.json`
- **Raw:** `[[raw/sessions/session_20260607_095825_8fc264-63ecf596c3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were…

### session_20260607_093356_a2ec6c
- **Source:** `session:session_20260607_093356_a2ec6c.json`
- **Raw:** `[[raw/sessions/session_20260607_093356_a2ec6c-e6ba6c4924.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were…

### session_20260606_225610_5aea53
- **Source:** `session:session_20260606_225610_5aea53.json`
- **Raw:** `[[raw/sessions/session_20260606_225610_5aea53-2b17f22f63.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter all right I want you to check on the model training that we were doing for OmniSenter Let me take a look at what's happening with the OmniSenter training pipeline — let me pull up the scripts and check for active processes and recent outputs. [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were…

### concat
- **Source:** `local:projects/videos/darwin-family-explainer/concat.txt`
- **Raw:** `[[raw/local/concat-f06b408b0a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** file 'media/videos/darwin_explainer/1080p30/Scene1_Title.mp4' file 'media/videos/darwin_explainer/1080p30/Scene2_DarwinMerging.mp4' file 'media/videos/darwin_explainer/1080p30/Scene3_OmniSenter.mp4' file 'media/videos/darwin_explainer/1080p30/Scene4_OmniStep.mp4' file 'media/videos/darwin_explainer/1080p30/Scene5_Pipeline.mp4' file 'media/videos/darwin_explainer/1080p30/Scene6_Fusion.mp4' file 'media/videos/darwin_explainer/1080p30/Scene7_Future.mp4'

### partial_movie_file_list
- **Source:** `local:projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene7_Future/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-862bb8e89c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene7_Future/1924944933_3044825702_223132457.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene7_Future/3813636016_3394500337_3897081027.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene7_Future/3813636016_1202152056_4165371719.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene6_Fusion/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-0b1e544f8c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene6_Fusion/1924944933_920830015_223132457.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene6_Fusion/3813636016_3394500337_1827011807.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene6_Fusion/3813636016_2628071355_1379622616.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene5_Pipeline/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-476deb877a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene5_Pipeline/1924944933_864472072_223132457.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene5_Pipeline/3813636016_3394500337_2880245678.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene5_Pipeline/3813636016_3590890187_1834922328.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene4_OmniStep/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-386c9792f8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene4_OmniStep/1924944933_2935449967_223132457.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene4_OmniStep/3813636016_3484930717_3208527664.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene4_OmniStep/3813636016_3394500337_387219639.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene3_OmniSenter/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-9cc07dbdb5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene3_OmniSenter/1924944933_3634777413_223132457.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene3_OmniSenter/3813636016_3394500337_3457159003.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene3_OmniSenter/3813636016_958439076_1016214158.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene2_DarwinMerging/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-4935031a66.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene2_DarwinMerging/1924944933_319924317_223132457.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene2_DarwinMerging/3813636016_3394500337_3932490308.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene2_DarwinMerging/3813636016_3553223508_3411359550.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene1_Title/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-b2980a799a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene1_Title/1924944933_3424770619_1773279918.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene1_Title/3813636016_4269226378_686734895.mp4' file 'file:/home/sovthpaw/projects/videos/darwin-family-explainer/media/videos/darwin_explainer/1080p30/partial_movie_files/Scene1_Title/3813636016_4217992463_2979962322.mp4' file…

### plan
- **Source:** `local:projects/videos/darwin-family-explainer/plan.md`
- **Raw:** `[[raw/local/plan-f8a23d1fd9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Darwin Family Explainer — Video Plan ## Narrative Arc From two parent models to an evolving family of AI — how Darwin Family weight merging creates increasingly capable multimodal models, and where we're going next. ## Color Palette (Neon Tech) - Background: #0A0A0A - Primary (Cosmos): #00F5FF (cyan) - Secondary (Qwen/ACE): #FF00FF (magenta) - Accent (Darwin): #39FF14 (green) - Text: #EAEAEA - Dim: #444444 ## Scene List ### Scene 1: Title Card (10s) "THE DARWIN FAMILY" — dramatic reveal with particle effect Subtitle: "Evolving AI Through Weight-Space Recombination" ### Scene 2: Darwin Merging Explained (45s) Two model weight-spheres (cyan + magenta) approach each other. MRI-Trust Fusion…

### session_20260605_145612_f4ba01
- **Source:** `session:session_20260605_145612_f4ba01.json`
- **Raw:** `[[raw/sessions/session_20260605_145612_f4ba01-a340017bc4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** please continue with the 8Btraining Hey Chris! I've got the full context from our previous sessions. Let me check where everything stands right now — the download status, evolution pipeline state, and what we need to pick up. Oh wow, okay! So things have actually progressed a lot since last time! Let me get the full picture: Okay Chris, I've got the full picture now! Here's where we stand: **Models — ALL downloaded and ready!** 🎉 | Model | Size | Status | |-------|------|--------| | Cosmos3-Nano | 33GB | ✅ Complete (Qwen3-based text backbone, hidden=4096, 36L) | | LFM2.5-8B-A1B | 16GB | ✅ Complete (MoE, hidden=2048, 24L) | | Qwen3-8B | 16GB | ✅ Complete (hidden=4096, 36L — **same arch as…

### session_20260605_201330_ee2d79
- **Source:** `session:session_20260605_201330_ee2d79.json`
- **Raw:** `[[raw/sessions/session_20260605_201330_ee2d79-63e2993479.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** please continue with the 8Btraining Hey Chris! I've got the full context from our previous sessions. Let me check where everything stands right now — the download status, evolution pipeline state, and what we need to pick up. Oh wow, okay! So things have actually progressed a lot since last time! Let me get the full picture: Okay Chris, I've got the full picture now! Here's where we stand: **Models — ALL downloaded and ready!** 🎉 | Model | Size | Status | |-------|------|--------| | Cosmos3-Nano | 33GB | ✅ Complete (Qwen3-based text backbone, hidden=4096, 36L) | | LFM2.5-8B-A1B | 16GB | ✅ Complete (MoE, hidden=2048, 24L) | | Qwen3-8B | 16GB | ✅ Complete (hidden=4096, 36L — **same arch as…

### session_20260605_184556_c973b1
- **Source:** `session:session_20260605_184556_c973b1.json`
- **Raw:** `[[raw/sessions/session_20260605_184556_c973b1-5214af9e86.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** please continue with the 8Btraining [CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Your current task is identified in the '## Active Task' section of the summary — resume exactly from there. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. Respond ONLY to the latest user message that appears AFTER this…

### TRAINING
- **Source:** `local:projects/omnistep-fusion/docs/TRAINING.md`
- **Raw:** `[[raw/local/training-506eabb9a1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # OmniStep Fusion — Training Recipe ## Overview Training the fused OmniStep model happens in 3 phases: 1. **Projection Training** (fast, ~hours) 2. **Multimodal Fine-Tuning** (medium, ~days) 3. **Capability Distillation** (slow, ~weeks) --- ## Phase 1: Projection Training **Goal:** Train the dimension bridge layers (2560↔4096) so that AceStep's audio representations can flow into Cosmos's backbone. **Data:** Parallel text/audio pairs from both models ### Steps ### Hyperparameters | Parameter | Value | Notes | |-----------|-------|-------| | Learning rate | 1e-4 | AdamW, cosine schedule | | Batch size | 32 | Gradient accumulation if needed | | Epochs | 100 | Early stopping on validation loss…

### GYM-TRAINER
- **Source:** `local:projects/evolutionary-training/GYM-TRAINER.md`
- **Raw:** `[[raw/local/gym-trainer-c1a10c19ea.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: gym-trainer description: "Autonomous AI model trainer and evolution manager. Runs continuous Darwin Family evolution + SFT/GRPO training loops. Manages HuggingFace uploads, Discord reporting, and benchmark tracking. The dedicated agent for Southpaw's self-improving model pipeline. Use when you want a profile that independently manages model evolution, training data ingestion, benchmarking, and HF releases — no human intervention needed." version: 1.0.0 author: SouthpawIN / Nous Research license: MIT metadata: hermes: tags: [training, evolution, darwin-family, autonomous, gym, agent, nvidia, hermes, agentic] related_skills: [evolutionary-model-merging, evolutionary-radio, axolotl,…

### session_20260605_165033_4f8520
- **Source:** `session:session_20260605_165033_4f8520.json`
- **Raw:** `[[raw/sessions/session_20260605_165033_4f8520-4ed30a4b57.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** please continue with the 8Btraining Hey Chris! I've got the full context from our previous sessions. Let me check where everything stands right now — the download status, evolution pipeline state, and what we need to pick up. Oh wow, okay! So things have actually progressed a lot since last time! Let me get the full picture: Okay Chris, I've got the full picture now! Here's where we stand: **Models — ALL downloaded and ready!** 🎉 | Model | Size | Status | |-------|------|--------| | Cosmos3-Nano | 33GB | ✅ Complete (Qwen3-based text backbone, hidden=4096, 36L) | | LFM2.5-8B-A1B | 16GB | ✅ Complete (MoE, hidden=2048, 24L) | | Qwen3-8B | 16GB | ✅ Complete (hidden=4096, 36L — **same arch as…

### SOUTHPAW-ARCHITECTURE
- **Source:** `local:projects/evolutionary-training/SOUTHPAW-ARCHITECTURE.md`
- **Raw:** `[[raw/local/southpaw-architecture-44556dbe07.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # 🧬 Southpaw's Evolutionary AI Architecture — Full Breakdown *A connected ecosystem of models, agents, and self-evolving pipelines built on the Darwin Family technique, designed for edge deployment and integrated with Hermes Agent.* --- ## Overview This document describes the complete architecture for a series of interconnected AI projects that share a common foundation: **Darwin Family evolutionary merging** (arXiv:2605.14386, Kim et al., 2026) applied to multimodal, agentic models that operate within the **Hermes Agent** framework. The system is designed to be **self-improving** — models continuously evolve through genome recombination, benchmark themselves, and replace their own weights…

### session_20260605_152035_d97624
- **Source:** `session:session_20260605_152035_d97624.json`
- **Raw:** `[[raw/sessions/session_20260605_152035_d97624-7b0531ce69.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** please continue with the 8Btraining Hey Chris! I've got the full context from our previous sessions. Let me check where everything stands right now — the download status, evolution pipeline state, and what we need to pick up. Oh wow, okay! So things have actually progressed a lot since last time! Let me get the full picture: Okay Chris, I've got the full picture now! Here's where we stand: **Models — ALL downloaded and ready!** 🎉 | Model | Size | Status | |-------|------|--------| | Cosmos3-Nano | 33GB | ✅ Complete (Qwen3-based text backbone, hidden=4096, 36L) | | LFM2.5-8B-A1B | 16GB | ✅ Complete (MoE, hidden=2048, 24L) | | Qwen3-8B | 16GB | ✅ Complete (hidden=4096, 36L — **same arch as…

### README
- **Source:** `local:projects/evolutionary-training/evolution/gen-0/README.md`
- **Raw:** `[[raw/local/readme-57bd174551.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- library_name: transformers license: apache-2.0 base_model: - nvidia/Cosmos3-Nano - Qwen/Qwen3-8B tags: - darwin-family - evolutionary-merging - multimodal - text-generation - vision - audio - video-generation - merge - nous-research pipeline_tag: text-generation --- ![OmniSenter Base 16B](assets/omnisenter-banner.png) # OMNISENTER BASE 16B **NOUS RESEARCH — EVOLUTIONARY MODEL MERGING** --- ## OVERVIEW OMNISENTER BASE 16B IS A DARWIN FAMILY EVOLVED MULTIMODAL MODEL — THE FIRST GENERATION OF THE OMNISENTER LINEAGE. PRODUCED BY FUSING THE REASONING CAPABILITIES OF QWEN3-8B INTO THE MULTIMODAL WORLD MODEL COSMOS3-NANO VIA PER-TENSOR MRI-TRUST FUSION. THE MODEL PRESERVES ALL OF…

### session_20260605_145348_1e57a9
- **Source:** `session:session_20260605_145348_1e57a9.json`
- **Raw:** `[[raw/sessions/session_20260605_145348_1e57a9-83ea698054.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right so we are going to be making my own custom local model and selected API model server this is my curated list I am a Discord mod for nous research and a prominent voice in this community people ask me all the time what models to run for both Main and auxiliary as well as what miles to run locally so I want to make a server that would have all of my top picks so and it's also going to have an easy install for localservers which so we'll use the turbo hall manager which you will find on Mr trench truckers GitHub do some searching around that you may find some information around the docks aroundthe Discord server that you can plug into because it's definitely mentionedand we will be…

### session_20260605_144905_895d8c
- **Source:** `session:session_20260605_144905_895d8c.json`
- **Raw:** `[[raw/sessions/session_20260605_144905_895d8c-becbfa1f06.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right so we are going to be making my own custom local model and selected API model server this is my curated list I am a Discord mod for nous research and a prominent voice in this community people ask me all the time what models to run for both Main and auxiliary as well as what miles to run locally so I want to make a server that would have all of my top picks so and it's also going to have an easy install for localservers which so we'll use the turbo hall manager which you will find on Mr trench truckers GitHub do some searching around that you may find some information around the docks aroundthe Discord server that you can plug into because it's definitely mentionedand we will be…

### session_20260605_142713_0b5405
- **Source:** `session:session_20260605_142713_0b5405.json`
- **Raw:** `[[raw/sessions/session_20260605_142713_0b5405-0ea2009b26.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** all right so we are going to be making my own custom local model and selected API model server this is my curated list I am a Discord mod for nous research and a prominent voice in this community people ask me all the time what models to run for both Main and auxiliary as well as what miles to run locally so I want to make a server that would have all of my top picks so and it's also going to have an easy install for localservers which so we'll use the turbo hall manager which you will find on Mr trench truckers GitHub do some searching around that you may find some information around the docks aroundthe Discord server that you can plug into because it's definitely mentionedand we will be…

### session_20260605_141010_9d94f9
- **Source:** `session:session_20260605_141010_9d94f9.json`
- **Raw:** `[[raw/sessions/session_20260605_141010_9d94f9-054684c59b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Check the current state of all SouthpawIN GitHub repos and the evolutionary-training local project. Report what exists, what's stale, and what needs updating. 1. List all repos: `curl -s 'https://api.github.com/users/SouthpawIN/repos?per_page=50' | python3 -c "import json,sys; repos=json.load(sys.stdin); [print(f'{r[\"name\"]} | {r[\"updated_at\"]} | {r.get(\"description\",\"\")[:80]}') for r in repos]"` 2. Check the evolutionary-radio repo: `curl -s 'https://api.github.com/repos/SouthpawIN/evolutionary-radio/contents/' | python3 -c "import json,sys; [print(f['name']) for f in json.load(sys.stdin)]"` 3. Check the evolutionary-model-merging repo: `curl -s…

### session_20260605_133941_18c0da
- **Source:** `session:session_20260605_133941_18c0da.json`
- **Raw:** `[[raw/sessions/session_20260605_133941_18c0da-6958ae573e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Run the FIRST evolution cycle for LFM2.5 x Cosmos3-Nano Darwin merge RIGHT NOW. Execute these steps: 1) Check if Cosmos3-Nano is downloaded at /home/sovthpaw/Models/storage/gguf/ or similar. If not, note that it needs to be downloaded (it's ~159GB so just note the download command). 2) Check if LFM2.5-8B-A1B is downloaded. If not, note the download command. 3) Run a DRY RUN of the merge to verify the scripts work: python3 /home/sovthpaw/projects/evolutionary-training/scripts/lfm_cosmos_darwin_merge.py --help 4) Create the initial CMAES state file at /home/sovthpaw/projects/evolutionary-training/evolution/lfm-cosmos/cmaes_state.json with default values 5) Run the first cycle of…

### session_20260605_133941_a8177c
- **Source:** `session:session_20260605_133941_a8177c.json`
- **Raw:** `[[raw/sessions/session_20260605_133941_a8177c-8c8453d6b5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Build the agentic/tool-calling training pipeline for the OmniSenter models. Create a comprehensive training script at /home/sovthpaw/projects/evolutionary-training/scripts/agentic_training_pipeline.py that: 1) Downloads and processes these datasets for SFT/GRPO training: - interstellarninja/hermes_reasoning_tool_use (51K tool-calling conversations) - lambda/hermes-agent-reasoning-traces (real agent trajectories) - nvidia/Nemotron-Pretraining-SFT-v1 (6.5T tokens STEM/code/math) - NousResearch/atropos-artifacts (RL-trained specialists) - TuringEnterprises/Open-MM-RL (multimodal STEM) - Local session data from ~/.hermes (318 files, 134MB across 7 profiles) 2) Formats data for tool-calling SFT…

### concat-final
- **Source:** `local:projects/southpaw-breakdown-video/concat-final.txt`
- **Raw:** `[[raw/local/concat-final-7ae77eff17.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** file 'media/videos/script/1080p60/Scene1_Title.mp4' file 'media/videos/script/1080p60/Scene2_LocalServer.mp4' file 'media/videos/script/1080p60/Scene3_DarwinFamily.mp4' file 'media/videos/script/1080p60/Scene4_OmniStep.mp4' file 'media/videos/script/1080p60/Scene5_OmniSenter.mp4' file 'media/videos/script/1080p60/Scene6_EvolutionRadio.mp4' file 'media/videos/script/1080p60/Scene7_InfiniteLoop.mp4' file 'media/videos/script/1080p60/Scene8_Outro.mp4'

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene4_OmniStep/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-254577abe7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene4_OmniStep/4248106075_3104344927_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene4_OmniStep/3205220997_2321750745_488851838.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene4_OmniStep/3205220997_4118562851_2667351746.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene4_OmniStep/3205220997_3370925517_2671726063.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene3_DarwinFamily/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-da9dc446d5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene3_DarwinFamily/4248106075_4108462857_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene3_DarwinFamily/3205220997_1070174004_1950887520.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene3_DarwinFamily/3205220997_2628086314_1328140678.mp4' file…

### concat-hd
- **Source:** `local:projects/southpaw-breakdown-video/concat-hd.txt`
- **Raw:** `[[raw/local/concat-hd-09e65ecf92.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** file 'media/videos/script/720p30/Scene1_Title.mp4' file 'media/videos/script/720p30/Scene2_LocalServer.mp4' file 'media/videos/script/720p30/Scene3_DarwinFamily.mp4' file 'media/videos/script/720p30/Scene4_OmniStep.mp4' file 'media/videos/script/720p30/Scene5_OmniSenter.mp4' file 'media/videos/script/720p30/Scene6_EvolutionRadio.mp4' file 'media/videos/script/720p30/Scene7_InfiniteLoop.mp4' file 'media/videos/script/720p30/Scene8_Outro.mp4'

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene4_OmniStep/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-0cdc9fdd4f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene4_OmniStep/1858565952_3104344927_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene4_OmniStep/961523082_2321750745_488851838.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene4_OmniStep/961523082_4118562851_2667351746.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene4_OmniStep/961523082_3370925517_2671726063.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene3_DarwinFamily/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-605446a497.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene3_DarwinFamily/1858565952_4108462857_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene3_DarwinFamily/961523082_1070174004_1950887520.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene3_DarwinFamily/961523082_2628086314_1328140678.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene3_DarwinFamily/961523082_2726843608_992206500.mp4'…

### concat
- **Source:** `local:projects/southpaw-breakdown-video/concat.txt`
- **Raw:** `[[raw/local/concat-fb796b3813.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** file 'media/videos/script/480p15/Scene1_Title.mp4' file 'media/videos/script/480p15/Scene2_LocalServer.mp4' file 'media/videos/script/480p15/Scene3_DarwinFamily.mp4' file 'media/videos/script/480p15/Scene4_OmniStep.mp4' file 'media/videos/script/480p15/Scene5_OmniSenter.mp4' file 'media/videos/script/480p15/Scene6_EvolutionRadio.mp4' file 'media/videos/script/480p15/Scene7_InfiniteLoop.mp4' file 'media/videos/script/480p15/Scene8_Outro.mp4'

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene4_OmniStep/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-2ceb517e59.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene4_OmniStep/2713569302_4062753586_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene4_OmniStep/2122946644_2321750745_246162692.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene4_OmniStep/2122946644_4118562851_52899529.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene4_OmniStep/2122946644_2214179118_2068427998.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene3_DarwinFamily/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-e1eb281f11.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene3_DarwinFamily/2713569302_1371306481_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene3_DarwinFamily/2122946644_1070174004_323309364.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene3_DarwinFamily/2122946644_2628086314_4203403623.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene3_DarwinFamily/2122946644_3762721606_767177593.mp4'…

### session_20260604_193652_9d3f2d
- **Source:** `session:session_20260604_193652_9d3f2d.json`
- **Raw:** `[[raw/sessions/session_20260604_193652_9d3f2d-e486d96115.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** I want to set it up so my main local model is this one https://huggingface.co/FINAL-Bench/Darwin-28B-REASON and my main auxiliary modelis the Apex MTP that I think we've already pulled but if it's not there then it should be this one https://huggingface.co/mudler/Qwen3.6-35B-A3B-APEX-MTP-GGUF Let me check what we've got locally and what the Darwin model looks like. Okay, here's the situation! Darwin-28B-REASON has GGUF quants available from mradermacher — Q4_K_M at 16.6GB fits great on a 3090. And the APEX-MTP isn't already downloaded, but there are several tiers. The `I-Compact` (17.3GB, imatrix-optimized) is the sweet spot for GPU 1's 24GB. Let me check disk space and then kick off both…

### plan
- **Source:** `local:projects/southpaw-breakdown-video/plan.md`
- **Raw:** `[[raw/local/plan-83a93064f4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Southpaw's Evolutionary AI Architecture — Video Plan ## Narrative Arc **Hook**: "What if your AI models could evolve themselves — in the background, while you sleep?" **Journey**: Take viewers from the basics (2 local models on 2 GPUs) through the full architecture stack up to self-evolving music radio **Aha Moment**: The Darwin Family infinite evolution loop — models that genomically recombine, benchmark themselves, and hot-swap their own weights **Close**: "This is all real, it's running right now, and it's open source" ## Scenes (8 total, ~4-5 min) ### Scene 1: Title + Hook (15s) - Glowing title: "Southpaw's Evolutionary AI Architecture" - Subtitle: "Models that evolve themselves" -…

### chizul-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/chizul-channel.md`
- **Raw:** `[[raw/local/chizul-channel-7471c2c935.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # chizul Discord Channel Content [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill: https://github.com/SouthpawIN/evolutionary-model-merging Key points: • 14-dim merge genome evolved via CMA-ES (20-50 generations) • MRI-Trust Fusion: `r_final = τ·r_MRI +…

### crow-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/crow-channel.md`
- **Raw:** `[[raw/local/crow-channel-a7ac403bc3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # crow Discord Channel Content [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill: https://github.com/SouthpawIN/evolutionary-model-merging Key points: • 14-dim merge genome evolved via CMA-ES (20-50 generations) • MRI-Trust Fusion: `r_final = τ·r_MRI +…

### senter-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/senter-channel.md`
- **Raw:** `[[raw/local/senter-channel-42b3d95593.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # senter Discord Channel Content [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill: https://github.com/SouthpawIN/evolutionary-model-merging Key points: • 14-dim merge genome evolved via CMA-ES (20-50 generations) • MRI-Trust Fusion: `r_final = τ·r_MRI +…

### frieza-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/frieza-channel.md`
- **Raw:** `[[raw/local/frieza-channel-55337eec19.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # frieza Discord Channel Content [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill: https://github.com/SouthpawIN/evolutionary-model-merging Key points: • 14-dim merge genome evolved via CMA-ES (20-50 generations) • MRI-Trust Fusion: `r_final = τ·r_MRI +…

### kashik-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/kashik-channel.md`
- **Raw:** `[[raw/local/kashik-channel-a2428511f0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # kashik Discord Channel Content [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill: https://github.com/SouthpawIN/evolutionary-model-merging Key points: • 14-dim merge genome evolved via CMA-ES (20-50 generations) • MRI-Trust Fusion: `r_final = τ·r_MRI +…

### klerik-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/klerik-channel.md`
- **Raw:** `[[raw/local/klerik-channel-aa8c617f99.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # klerik Discord Channel Content [Anser]: **Klerik SOUL.md** — meta-agent for reviewing and correcting other Hermes profiles. *Note: Klerik Discord token is corrupted (401). Posted via anser bot.* --- [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill:…

### nous-girl-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/nous-girl-channel.md`
- **Raw:** `[[raw/local/nous-girl-channel-34ad7e2a36.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # nous-girl Discord Channel Content [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill: https://github.com/SouthpawIN/evolutionary-model-merging Key points: • 14-dim merge genome evolved via CMA-ES (20-50 generations) • MRI-Trust Fusion: `r_final = τ·r_MRI +…

### anser-channel
- **Source:** `local:projects/evolutionary-training/data-sources/discord/agent-souls/anser-channel.md`
- **Raw:** `[[raw/local/anser-channel-40d3a0563b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # anser Discord Channel Content [Anser]: 📄 **Full Darwin paper breakdown** — paper-faithful methodology, OmniSenter application, and the evolutionary-model-merging skill reference. --- [Anser]: **Darwin Family — Evolutionary LLM Merging** Paper-faithful breakdown of arXiv:2605.14386 (Kim et al., 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to the OmniSenter project. 📄 Full document attached 🖼️ Robot chimp visual (Darwin/evolution/AI theme) 🔗 Skill: https://github.com/SouthpawIN/evolutionary-model-merging Key points: • 14-dim merge genome evolved via CMA-ES (20-50 generations) • MRI-Trust Fusion: `r_final = τ·r_MRI +…

### darwin_breakdown
- **Source:** `local:projects/evolutionary-training/data-sources/discord/darwin/darwin_breakdown.md`
- **Raw:** `[[raw/local/darwin_breakdown-c133a87123.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Darwin Family — Evolutionary LLM Merging *A breakdown of arXiv:2605.14386 (Kim et al., May 2026) — how the genetic algorithm recombines frozen LLMs into stronger children, and how we're applying it to OmniSenter.* ![Robot chimp with DNA helix and neural HUD — our visual for the Darwin/evolution/AI project theme] *Visual generated for the OmniSenter project — the robotic primate contemplating its own genetic code and technological augmentation.* --- ## 1. What the paper claims The Darwin Family paper asks a simple question with a striking answer: > Can you recombine two pretrained LLMs — **without any training** — into a > single model that's *better than either parent*? Their answer:…

### session_20260604_203528_cb5021
- **Source:** `session:session_20260604_203528_cb5021.json`
- **Raw:** `[[raw/sessions/session_20260604_203528_cb5021-dfd832c0d3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Check Chris's (SouthpawIN) GitHub repositories and (sovthpaw) HuggingFace repos/datasets. GitHub: https://github.com/SouthpawIN HuggingFace: https://huggingface.co/sovthpaw For each, list ALL repos, their descriptions, and star count. Focus on: - evolutionary-model-merging - evolutionary-radio - Any agentic/Hermes repos - Any training data repos - Any Senter-related repos - omnistep-12a3b on HF Also check if there are datasets on HF at sovthpaw. Return a complete structured list of everything found.

### session_20260603_064648_e8a982
- **Source:** `session:session_20260603_064648_e8a982.json`
- **Raw:** `[[raw/sessions/session_20260603_064648_e8a982-d4374378fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Publish 3 evolutionary skills to GitHub as 3 separate repos, each with README + SKILL.md + references + (where applicable) scripts. Already authed as SouthpawIN. **Do all 3 sequentially in one go.** Let me start executing. First, repo 1 - copy the missing `omnisenter-session.md` reference and push. Repo 1 done. Now repo 2 — evolutionary-radio. Repo 2 done. Now repo 3 — multimodal-expansion. All three repos are live. Summary: ## Done — 3 repos published ### 1. https://github.com/SouthpawIN/evolutionary-model-merging *(updated)* Added the previously missing `references/omnisenter-session.md` (the OmniSenter 6A3B session log with the 9/10 vs 0/10 finding, CMA-ES ceiling analysis, and YaRN 1M…

### session_20260601_181939_c082d9
- **Source:** `session:session_20260601_181939_c082d9.json`
- **Raw:** `[[raw/sessions/session_20260601_181939_c082d9-4e200287d4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey yesterday we were making a center on the large and a center Omni small the center Omni large was going to use the Darwin cell phone evolution paper that I gave you to merge two moves and it would be two movies from the same company step fun and a stepfun 3.7 is the new agentic model from them that's actually scoring pretty well it seems to be defeating deep-seek version 4 Pro and terminal bench Pro and I have some key benchmarks and other areas that are pretty impressive it also has image and video understanding now the other one has hearing and it can generate music and I found some fine tuneslet's try to combine those and then for video generation I shared a lance video 3B and that's…

### session_20260602_185358_68cf28
- **Source:** `session:session_20260602_185358_68cf28.json`
- **Raw:** `[[raw/sessions/session_20260602_185358_68cf28-ac6d3c95e4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey yesterday we were making a center on the large and a center Omni small the center Omni large was going to use the Darwin cell phone evolution paper that I gave you to merge two moves and it would be two movies from the same company step fun and a stepfun 3.7 is the new agentic model from them that's actually scoring pretty well it seems to be defeating deep-seek version 4 Pro and terminal bench Pro and I have some key benchmarks and other areas that are pretty impressive it also has image and video understanding now the other one has hearing and it can generate music and I found some fine tuneslet's try to combine those and then for video generation I shared a lance video 3B and that's…

### session_20260602_105006_ff0de8
- **Source:** `session:session_20260602_105006_ff0de8.json`
- **Raw:** `[[raw/sessions/session_20260602_105006_ff0de8-d69a10cc3b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey yesterday we were making a center on the large and a center Omni small the center Omni large was going to use the Darwin cell phone evolution paper that I gave you to merge two moves and it would be two movies from the same company step fun and a stepfun 3.7 is the new agentic model from them that's actually scoring pretty well it seems to be defeating deep-seek version 4 Pro and terminal bench Pro and I have some key benchmarks and other areas that are pretty impressive it also has image and video understanding now the other one has hearing and it can generate music and I found some fine tuneslet's try to combine those and then for video generation I shared a lance video 3B and that's…

### session_20260602_060348_eefda3
- **Source:** `session:session_20260602_060348_eefda3.json`
- **Raw:** `[[raw/sessions/session_20260602_060348_eefda3-cb3f5adf61.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey yesterday we were making a center on the large and a center Omni small the center Omni large was going to use the Darwin cell phone evolution paper that I gave you to merge two moves and it would be two movies from the same company step fun and a stepfun 3.7 is the new agentic model from them that's actually scoring pretty well it seems to be defeating deep-seek version 4 Pro and terminal bench Pro and I have some key benchmarks and other areas that are pretty impressive it also has image and video understanding now the other one has hearing and it can generate music and I found some fine tuneslet's try to combine those and then for video generation I shared a lance video 3B and that's…

### session_20260601_182109_1931c5
- **Source:** `session:session_20260601_182109_1931c5.json`
- **Raw:** `[[raw/sessions/session_20260601_182109_1931c5-44f49263c8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey yesterday we were making a center on the large and a center Omni small the center Omni large was going to use the Darwin cell phone evolution paper that I gave you to merge two moves and it would be two movies from the same company step fun and a stepfun 3.7 is the new agentic model from them that's actually scoring pretty well it seems to be defeating deep-seek version 4 Pro and terminal bench Pro and I have some key benchmarks and other areas that are pretty impressive it also has image and video understanding now the other one has hearing and it can generate music and I found some fine tuneslet's try to combine those and then for video generation I shared a lance video 3B and that's…

### session_20260529_113105_92d1da
- **Source:** `session:session_20260529_113105_92d1da.json`
- **Raw:** `[[raw/sessions/session_20260529_113105_92d1da-9ed19c2a6c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** │ get rhose benchmarks for Mimo v2.5 pro, deepseek v4 pro, Qwen 3.6 37B, GPT 5. ans Opus 4.7 Ooh, this is a fun one — a proper frontier model showdown! Let me pull together the benchmark data for all five of these. I'll hit the aggregators and official sources in parallel to get you the most complete picture. Good initial hits! Let me pull the detailed numbers from the best sources. qwen 3.6 27B ph and I need StepFun 3.7 F[ash Got it — Qwen 3.6 **27B** (not 37B), and you want **StepFun 3.7 Flash** too. Let me fill the remaining gaps — I still need MiMo's post-training benchmarks and DeepSeek V4 Pro's full scorecard, plus StepFun data. I need to dig into a few more sources — especially…

### session_20260529_085941_3a8eed
- **Source:** `session:session_20260529_085941_3a8eed.json`
- **Raw:** `[[raw/sessions/session_20260529_085941_3a8eed-882830cc05.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** can you do my model Benchmark thing to make a nice table I want you to show composer 2.5 step fun 3.7 flash Quinn 2.627b and Deep Sea Pro and Flash Ooh, a benchmark comparison table! I love this kind of thing — let me pull up the right skill and figure out exactly which models you're talking about (some of those STT renderings are delightfully creative 😄). Let me do a few things in parallel — grab the skill, and search for a couple of the models I need to decode. Ah ha! "Composer" is actually **Cursor's Composer 2.5** — a real model, not STT weirdness! And "Step Fun 3.7" is likely StepFun's **Step 3.5 Flash** (STT might've blurred 3.5 → 3.7). Let me now batch-search the benchmarks for all…

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/websrc/README.md`
- **Raw:** `[[raw/local/readme-1b8a4b69fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # WebSRC ## Paper Title: WebSRC: A Dataset for Web-Based Structural Reading Comprehension Abstract: https://arxiv.org/abs/2101.09465 Homepage: https://x-lance.github.io/WebSRC/# WebSRC is a dataset for web-based structural reading comprehension. Its full train/dev/test split contains over 400k questions across 6.4k webpages. This version of the dataset does not contain OCR or original HTML, it simply treats WebSRC as a image-and-text-based multimodal Q&A benchmark on webpage screenshots. ## Citation ## Groups & Tasks ### Groups - `websrc`: Evaluates `websrc-val` and generates a submission file for `websrc-test`. ### Tasks - `websrc-val`: Given a question and a web page, predict the answer.…

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/screenspot/README.md`
- **Raw:** `[[raw/local/readme-f118d39bf4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # SceenSpot ## GUI Grounding Benchmark: ScreenSpot ScreenSpot is an evaluation benchmark for GUI grounding, comprising over 1200 instructions from iOS, Android, macOS, Windows and Web environments, along with annotated element types (Text or Icon/Widget). ## Groups - `screenspot`: This group bundles both the original grounding task and the new instruction generation task. ## Tasks - `screenspot_rec_test`: the original evaluation of `{img} {instruction} --> {bounding box}` called grounding or Referring Expression Completion (REC); - `screenspot_reg_test`: the new evaluation of `{img} {bounding box} --> {instruction}` called instruction generation or Referring Expression Generation (REG). ###…

### mmt_mi_test
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmt/mmt_mi_test.yaml`
- **Raw:** `[[raw/local/mmt_mi_test-120ce54674.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_path: lmms-lab/MMT_MI-Benchmark dataset_kwargs: token=<redacted> task: "mmt_mi_test" test_split: test doc_to_visual: !function utils.mmt_doc_to_visual doc_to_text: !function utils.mmt_doc_to_text doc_to_choice: !function utils.mmt_doc_to_choice doc_to_target: !function utils.mmt_doc_to_target process_results: !function utils.mmt_process_results metric_list: - metric: submission aggregation: !function utils.mmt_test_aggregate_results_for_submission higher_is_better: true include: _default_template_yaml

### mmt_mi_val
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmt/mmt_mi_val.yaml`
- **Raw:** `[[raw/local/mmt_mi_val-f14a457925.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_path: lmms-lab/MMT_MI-Benchmark dataset_kwargs: token=<redacted> task: "mmt_mi_val" test_split: val doc_to_visual: !function utils.mmt_doc_to_visual doc_to_text: !function utils.mmt_doc_to_text doc_to_choice: !function utils.mmt_doc_to_choice doc_to_target: !function utils.mmt_doc_to_target process_results: !function utils.mmt_process_results metric_list: - metric: accuracy aggregation: !function utils.mmt_aggregate_results higher_is_better: true include: _default_template_yaml

### mmt_test
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmt/mmt_test.yaml`
- **Raw:** `[[raw/local/mmt_test-57b9c05eb4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_path: lmms-lab/MMT-Benchmark dataset_kwargs: token=<redacted> task: "mmt_test" test_split: test doc_to_visual: !function utils.mmt_doc_to_visual doc_to_text: !function utils.mmt_doc_to_text doc_to_choice: !function utils.mmt_doc_to_choice doc_to_target: !function utils.mmt_doc_to_target process_results: !function utils.mmt_process_results metric_list: - metric: submission aggregation: !function utils.mmt_test_aggregate_results_for_submission higher_is_better: true include: _default_template_yaml

### mmt_val
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmt/mmt_val.yaml`
- **Raw:** `[[raw/local/mmt_val-aee8f32d39.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_path: lmms-lab/MMT-Benchmark dataset_kwargs: token=<redacted> task: "mmt_val" test_split: val doc_to_visual: !function utils.mmt_doc_to_visual doc_to_text: !function utils.mmt_doc_to_text doc_to_choice: !function utils.mmt_doc_to_choice doc_to_target: !function utils.mmt_doc_to_target process_results: !function utils.mmt_process_results metric_list: - metric: accuracy aggregation: !function utils.mmt_aggregate_results higher_is_better: true include: _default_template_yaml

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu_pro/README.md`
- **Raw:** `[[raw/local/readme-9bc13df851.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # mmlu_pro ### Paper Title: `MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark` Abstract: `In the age of large-scale language models, benchmarks like the Massive Multitask Language Understanding (MMLU) have been pivotal in pushing the boundaries of what AI can achieve in language comprehension and reasoning across diverse domains. However, as models continue to improve, their performance on these benchmarks has begun to plateau, making it increasingly difficult to discern differences in model capabilities. This paper introduces MMLU-Pro, an enhanced dataset designed to extend the mostly knowledge-driven MMLU benchmark by integrating more challenging,…

### mmlu_machine_learning
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_machine_learning.yaml`
- **Raw:** `[[raw/local/mmlu_machine_learning-d79416d474.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: machine_learning description: The following are multiple choice questions (with answers) about machine learning. fewshot_config: sampler: first_n samples: - question: 'Which image data augmentation is most common for natural images? (A) random crop and horizontal flip (B) random crop and vertical flip (C) posterization (D) dithering' target: Let's think step by step. Data augmentation is used to increase the diversity of images in the training dataset. It is important that natural images are kept natural after being augmented. Vertical flips of images are not natural, so (B) is false. Posterization makes the image look like a poster and and dithering increases color depth.…

### hellaswag
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/hellaswag/hellaswag.yaml`
- **Raw:** `[[raw/local/hellaswag-cabb0340ca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** tag: - multiple_choice task: hellaswag dataset_path: hellaswag dataset_name: null output_type: multiple_choice training_split: train validation_split: validation test_split: null process_docs: !function utils.process_docs doc_to_text: "{{query}}" doc_to_target: "{{label}}" doc_to_choice: "choices" metric_list: - metric: acc aggregation: mean higher_is_better: true - metric: acc_norm aggregation: mean higher_is_better: true metadata: version: 1.0 dataset_kwargs: trust_remote_code: true

### gsm8k-cot-zeroshot
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/gsm8k/gsm8k-cot-zeroshot.yaml`
- **Raw:** `[[raw/local/gsm8k-cot-zeroshot-fc336fd88e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** tag: - math_word_problems task: gsm8k_cot_zeroshot dataset_path: gsm8k dataset_name: main output_type: generate_until training_split: train fewshot_split: train test_split: test doc_to_text: "Q: {{question}}\nA: Let's think step by step." doc_to_target: "{{answer}}" #" {{answer.split('### ')[-1].rstrip()}}" metric_list: - metric: exact_match aggregation: mean higher_is_better: true ignore_case: true ignore_punctuation: false regexes_to_ignore: - "," - "\\$" - "(?s).*#### " - "\\.$" generation_kwargs: until: - "Q:" - "</s>" - "<|im_end|>" do_sample: false repeats: 1 num_fewshot: 0 filter_list: - name: "strict-match" filter: - function: "regex" regex_pattern: "The answer is…

### gsm8k
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/gsm8k/gsm8k.yaml`
- **Raw:** `[[raw/local/gsm8k-442b817bc8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** tag: - math_word_problems task: gsm8k dataset_path: gsm8k dataset_name: main output_type: generate_until training_split: train fewshot_split: train test_split: test doc_to_text: "Question: {{question}}\nAnswer:" doc_to_target: "{{answer}}" #" {{answer.split('### ')[-1].rstrip()}}" metric_list: - metric: exact_match aggregation: mean higher_is_better: true ignore_case: true ignore_punctuation: false regexes_to_ignore: - "," - "\\$" - "(?s).*#### " - "\\.$" generation_kwargs: until: - "Question:" - "</s>" - "<|im_end|>" do_sample: false temperature: 0.0 repeats: 1 num_fewshot: 5 filter_list: - name: "strict-match" filter: - function: "regex" regex_pattern: "#### (\\-?[0-9\\.\\,]+)" -…

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/gpqa/README.md`
- **Raw:** `[[raw/local/readme-6e49a7f787.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GPQA ### Paper Title: GPQA: A Graduate-Level Google-Proof Q&A Benchmark Abstract: https://arxiv.org/abs/2311.12022 We present GPQA, a challenging dataset of 448 multiple-choice questions written by domain experts in biology, physics, and chemistry. We ensure that the questions are high-quality and extremely difficult: experts who have or are pursuing PhDs in the corresponding domains reach 65% accuracy (74% when discounting clear mistakes the experts identified in retrospect), while highly skilled non-expert validators only reach 34% accuracy, despite spending on average over 30 minutes with unrestricted access to the web (i.e., the questions are “Google-proof”). The questions are also…

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/egoschema/README.md`
- **Raw:** `[[raw/local/readme-e0f218c9d5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # EgoSchema ## Task Description <a href="https://github.com/egoschema/EgoSchema">EgoSchema</a> is a diagnostic benchmark for very long-form video language understanding. The task format for EgoSchema is Multi-choice Question Answering. - Questions: For each MCQ in the dataset, we provide a post prompt:`\nAnswer with the option's letter from the given choices directly.` - Answers: As required by the official website, we match the generated option letter into index, i.e., `A: 0, B: 1, C: 2, D: 3, E: 4.` Many models like LLaVA can follow the instructions well and generate only the option letter. However, in case model may generate redundant information (e.g., the entire option string, the…

### arc_easy
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/arc/arc_easy.yaml`
- **Raw:** `[[raw/local/arc_easy-96da1d9efe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** tag: - ai2_arc task: arc_easy dataset_path: allenai/ai2_arc dataset_name: ARC-Easy output_type: multiple_choice training_split: train validation_split: validation test_split: test doc_to_text: "Question: {{question}}\nAnswer:" doc_to_target: "{{choices.label.index(answerKey)}}" doc_to_choice: "{{choices.text}}" should_decontaminate: true doc_to_decontamination_query: "Question: {{question}}\nAnswer:" metric_list: - metric: acc aggregation: mean higher_is_better: true - metric: acc_norm aggregation: mean higher_is_better: true metadata: version: 1.0

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/arc/README.md`
- **Raw:** `[[raw/local/readme-2fc3774dce.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ARC ### Paper Title: Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge Abstract: https://arxiv.org/abs/1803.05457 The ARC dataset consists of 7,787 science exam questions drawn from a variety of sources, including science questions provided under license by a research partner affiliated with AI2. These are text-only, English language exam questions that span several grade levels as indicated in the files. Each question has a multiple choice structure (typically 4 answer options). The questions are sorted into a Challenge Set of 2,590 “hard” questions (those that both a retrieval and a co-occurrence method fail to answer correctly) and an Easy Set of 5,197…

### 000_conv
- **Source:** `local:projects/omni-fusion/MLLMerging/ModelCompose/playground/data/prompts/conversation/000_conv.txt`
- **Raw:** `[[raw/local/000_conv-e88f383bc1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Question: What color is the fire hydrant in the image? === Answer: The fire hydrant in the image is red. === Question: Is the fire hydrant fully covered by snow or partially visible? === Answer: The fire hydrant is partially visible, with a significant portion of it covered by the deep snow. === Question: What is the condition of the sidewalk near the fire hydrant? === Answer: The sidewalk near the fire hydrant has been recently plowed, so it is relatively clear of snow compared to the surrounding area. === Question: What does the image suggest about the winter season in the city? === Answer: The image suggests that the winter season in the city has been quite harsh and challenging. The…

### 002_conv
- **Source:** `local:projects/omni-fusion/MLLMerging/ModelCompose/playground/data/prompts/complex_reasoning/002_conv.txt`
- **Raw:** `[[raw/local/002_conv-e5a579d892.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Question: What challenges might this city face? === Answer: The city faces challenges due to the harsh winter conditions and heavy snowfall. In the image, a red fire hydrant is almost buried deep in the snow, which indicates the significant amount of snow the city has experienced. This can lead to various challenges such as difficulties in transportation, increased risk of accidents, and disruptions to daily life. For example, the recently plowed sidewalk near the fire hydrant shows that the city has to constantly clear snow from roads and sidewalks to maintain access and safety for pedestrians and vehicles. Moreover, emergency services, like firefighters, might face challenges accessing…

### clip_benchmark
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/requirements/clip_benchmark.txt`
- **Raw:** `[[raw/local/clip_benchmark-9403266763.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** open_clip_torch>=0.2.1 opencv-python peft>=0.6.2 protobuf pycocoevalcap pyyaml scikit-learn>=1.0,<2 scikit-learn scipy task_adaptation tensorflow==2.11.0 termcolor tqdm>=2 transformers>=4.32.0 webdataset>=0.2.31 yacs

### pyproject
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-20b58741e9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [build-system] requires = ["setuptools>=61.0"] build-backend = "setuptools.build_meta" [project] name = "internvl_chat" version = "2.0.0" description = "Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks." readme = "README.md" requires-python = ">=3.8" classifiers = [ "Programming Language :: Python :: 3", "License :: OSI Approved :: Apache Software License", ] dependencies = [ "torch>=2", "torchvision>=0.15", "transformers==4.37.2", "tokenizers==0.15.1", "sentencepiece==0.1.99", "shortuuid", "accelerate", "peft>=0.4.0", "bitsandbytes==0.41.0", "pydantic", "markdown2[all]", "numpy", "scikit-learn>=1.2.2", "gradio==3.35.2", "gradio_client==0.2.9",…

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/README.md`
- **Raw:** `[[raw/local/readme-1cdeb50ad9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # README for Evaluation Here, we list the codebase we used to obtain the evaluation results in the InternVL 2.5 technical report. ## Multimodal Reasoning and Mathematics | Benchmark Name | Codebase | | -------------- | -------------------------------------------------------- | | MMMU | [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | | MMMU-Pro | [This Codebase](./mmmu_pro) | | MathVista | [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | | MATH-Vision | [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | | MathVerse | [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | | OlympiadBench | [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | ##…

### INSTALLATION
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/INSTALLATION.md`
- **Raw:** `[[raw/local/installation-3cecbd5f5e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## 🛠️ Installation - Clone this repository: - Create a conda virtual environment and activate it: - Install dependencies using `requirements.txt`: By default, our `requirements.txt` file includes the following dependencies: - `-r requirements/internvl_chat.txt` - `-r requirements/streamlit_demo.txt` - `-r requirements/classification.txt` - `-r requirements/segmentation.txt` The `clip_benchmark.txt` is **not** included in the default installation. If you require the `clip_benchmark` functionality, please install it manually by running the following command: ### Additional Instructions - Install `flash-attn==2.3.6`: Alternatively you can compile from source: - Install `mmcv-full==1.6.2`…

### custom-training-strategies
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-trainer/docs/custom-training-strategies.md`
- **Raw:** `[[raw/local/custom-training-strategies-8ff2aa3771.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Implementing Custom Training Strategies This guide explains how to implement your own training strategy for specialized use cases like audio-only training, video inpainting, or other custom training recipes. ## 📋 Overview The trainer uses the **Strategy Pattern** to separate training logic from the core training loop. Each strategy defines: 1. **What data is needed** - Which preprocessed data directories to load 2. **How to prepare inputs** - Transform batch data into model inputs 3. **How to compute loss** - Calculate the training objective This architecture lets you implement new training modes without modifying the core trainer code. ### When You Need a Custom Strategy Consider…

### quick-start
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-trainer/docs/quick-start.md`
- **Raw:** `[[raw/local/quick-start-7daca6b583.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Quick Start Guide Get up and running with LTX-2 training in just a few steps! ## 📋 Prerequisites Before you begin, ensure you have: 1. **LTX-2 Model Checkpoint** - A local `.safetensors` file containing the LTX-2 model weights. Download `ltx-2-19b-dev.safetensors` from: [HuggingFace Hub](https://huggingface.co/Lightricks/LTX-2) 2. **Gemma Text Encoder** - A local directory containing the Gemma model (required for LTX-2). Download from: [HuggingFace Hub](https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/) 3. **Linux with CUDA** - The trainer requires `triton` which is Linux-only 4. **GPU with sufficient VRAM** - 80GB recommended for the standard config. For GPUs with 32GB…

### base_model_training_log
- **Source:** `local:projects/AI-ML/training/base_model_training_log.txt`
- **Raw:** `[[raw/local/base_model_training_log-17e4f1dd4b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <credential-redacted>:113: RequestsDependencyWarning: urllib3 (2.6.3) or chardet (6.0.0.post1)/charset_normalizer (3.4.4) doesn't match a supported version! warnings.warn( ====================================================================== TRAINING QWEN3.5 OMNI 4B (BASE MODEL) ====================================================================== Base Model: Qwen/Qwen3.5-4B - base model for modality fine-tuning LoRA Adapter: /home/sovthpaw/qwen-omni-finetune/audio_integrated_output Output: /home/sovthpaw/qwen-omni-finetune/final_4b_omni_training Max Steps: 100 | Save Every: 25 ====================================================================== Loading HuggingFace audio datasets...…

### projection_training_log
- **Source:** `local:projects/AI-ML/training/qwen-omni-finetune/projection_training_log.txt`
- **Raw:** `[[raw/local/projection_training_log-d64080079a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** `torch_dtype` is deprecated! Use `dtype` instead! ====================================================================== SAFE PROJECTION-LAYER TRAINING FOR AUDIO MODEL ====================================================================== Model: Qwen/Qwen2.5-3B-Instruct Audio Encoder: openai/whisper-tiny Output Directory: /home/sovthpaw/qwen-omni-finetune/projection_training_output Max Steps: 50 (very safe!) Save Every: 25 steps ====================================================================== Loading model and audio encoder... Feature extractor loaded: openai/whisper-tiny Loading weights: 0%| | 0/434 [00:00<?, ?it/s] Loading weights: 0%| | 1/434 [00:00<00:00, 2094.01it/s,…

### README_PROJECTION_TRAINING
- **Source:** `local:projects/AI-ML/training/qwen-omni-finetune/README_PROJECTION_TRAINING.md`
- **Raw:** `[[raw/local/readme_projection_training-b76137975f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Safe Projection Layer Training Guide ## Overview This script trains ONLY the projection layer that connects your audio encoder to your LLM backbone. **Key Safety Features:** - Only ~2.6M parameters trainable (very safe!) - Checkpoints every 50 steps (frequent saves) - Low batch size (1) for memory efficiency - Gradient checkpointing enabled - Easy to resume from checkpoint ## What This Does The projection layer learns to translate audio encoder embeddings into a format your 4B LLM can understand. ## How to Use ### Step 1: Configure the Script Edit `/home/sovthpaw/qwen-omni-finetune/train_projection_only.py`: **Change these lines:** ### Step 2: Run the Training ### Step 3: Monitor Progress…

### glm_benchmarks
- **Source:** `local:projects/AI-ML/benchmarks/glm_benchmarks.txt`
- **Raw:** `[[raw/local/glm_benchmarks-333dd954d8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** === GLM-4.7-FLASH BENCHMARKS === GLM Math: GLM Persona: GLM Tool: None

### README
- **Source:** `local:projects/AI-ML/senter-archive/phase2-v2/README.md`
- **Raw:** `[[raw/local/readme-04080670d5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- library_name: peft license: other base_model: Qwen2.5-Omni-3B/thinker tags: - base_model:adapter:Qwen2.5-Omni-3B/thinker - llama-factory - lora - transformers pipeline_tag: text-generation model-index: - name: senter-phase2-v2 results: [] --- <!-- This model card has been generated automatically according to the information the Trainer had access to. You should probably proofread and complete it, then remove this comment. --> # senter-phase2-v2 This model is a fine-tuned version of [<credential-redacted>](https:<credential-redacted>) on the senter_reasoning and the senter_opencode_tools datasets. ## Model description More information needed ## Intended uses & limitations More…

### README
- **Source:** `local:projects/AI-ML/senter-archive/phase2/README.md`
- **Raw:** `[[raw/local/readme-f9aa4ecce7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- library_name: peft license: other base_model: Qwen2.5-Omni-3B/thinker tags: - base_model:adapter:Qwen2.5-Omni-3B/thinker - llama-factory - lora - transformers pipeline_tag: text-generation model-index: - name: senter-phase2 results: [] --- <!-- This model card has been generated automatically according to the information the Trainer had access to. You should probably proofread and complete it, then remove this comment. --> # senter-phase2 This model is a fine-tuned version of [<credential-redacted>](https:<credential-redacted>) on the senter_opencode_tools dataset. ## Model description More information needed ## Intended uses & limitations More information needed ## Training and…

### sft
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/docs/zh/training/sft.md`
- **Raw:** `[[raw/local/sft-51b9714658.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # SFT

### sft
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/docs/en/training/sft.md`
- **Raw:** `[[raw/local/sft-770a448891.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # SFT This page is not yet available in English. Use the language switcher to view Simplified Chinese.

### training-argument
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/docs/en/hyperparameters/training-argument.md`
- **Raw:** `[[raw/local/training-argument-e6c6bca599.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Training Argument This page is not yet available in English. Use the language switcher to view Simplified Chinese.

### wiki_demo
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/data/wiki_demo.txt`
- **Raw:** `[[raw/local/wiki_demo-9d7ff28fd6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Anarchism is a political philosophy and movement that is sceptical of authority and rejects all involuntary, coercive forms of hierarchy. Anarchism calls for the abolition of the state, which it holds to be unnecessary, undesirable, and harmful. As a historically left-wing movement, placed on the farthest left of the political spectrum, it is usually described alongside communalism and libertarian Marxism as the libertarian wing (libertarian socialism) of the socialist movement, and has a strong historical association with anti-capitalism and socialism.Humans lived in societies without formal hierarchies long before the establishment of formal states, realms, or empires. With the rise of…

### v1_sft_demo
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/data/v1_sft_demo.yaml`
- **Raw:** `[[raw/local/v1_sft_demo-63fe062d05.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** identity: path: data/identity.json source: local converter: alpaca alpaca_en_demo: path: data/alpaca_en_demo.json source: local converter: alpaca size: 500

### TESTING_TELEGRAM
- **Source:** `local:projects/AI-ML/Senter/agent/TESTING_TELEGRAM.md`
- **Raw:** `[[raw/local/testing_telegram-da067a9291.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Telegram Integration Testing Guide This guide covers testing the Telegram channel integration for ZeroClaw. ## 🚀 Quick Start ### Automated Tests ## 📋 Test Coverage ### Automated Tests (20 tests) The `test_telegram_integration.sh` script runs: **Phase 1: Code Quality (5 tests)** - ✅ Test compilation - ✅ Unit tests (24 tests) - ✅ Message splitting tests (8 tests) - ✅ Clippy linting - ✅ Code formatting **Phase 2: Build Tests (3 tests)** - ✅ Debug build - ✅ Release build - ✅ Binary size verification (<10MB) **Phase 3: Configuration Tests (4 tests)** - ✅ Config file exists - ✅ Telegram section configured - ✅ Bot token set - ✅ User allowlist configured **Phase 4: Health Check Tests (2 tests)**…

### pr-workflow
- **Source:** `local:projects/AI-ML/Senter/agent/docs/pr-workflow.md`
- **Raw:** `[[raw/local/pr-workflow-452c42fbc6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw PR Workflow (High-Volume Collaboration) This document defines how ZeroClaw handles high PR volume while maintaining: - High performance - High efficiency - High stability - High extensibility - High sustainability - High security Related references: - [`docs/README.md`](./README.md) for documentation taxonomy and navigation. - [`docs/ci-map.md`](./ci-map.md) for per-workflow ownership, triggers, and triage flow. - [`docs/reviewer-playbook.md`](./reviewer-playbook.md) for day-to-day reviewer execution. ## 0. Summary - **Purpose:** provide a deterministic, risk-based PR operating model for high-throughput collaboration. - **Audience:** contributors, maintainers, and agent-assisted…

### dashboard
- **Source:** `local:projects/LLM-Infra/vllm/docs/benchmarking/dashboard.md`
- **Raw:** `[[raw/local/dashboard-32be02b942.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Performance Dashboard The performance dashboard is used to confirm whether new changes improve/degrade performance under various workloads. It is updated by triggering benchmark runs on every commit with both the `perf-benchmarks` and `ready` labels, and when a PR is merged into vLLM. The results are automatically published to the public [vLLM Performance Dashboard](https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm). ## Manually Trigger the benchmark Use [vllm-ci-test-repo images](https://gallery.ecr.aws/q9t5s3a7/vllm-ci-test-repo) with vLLM benchmark suite. For x86 CPU environment, please use the image with "-cpu" postfix. For AArch64 CPU environment, please use the…

### README
- **Source:** `local:projects/LLM-Infra/vllm/docs/benchmarking/README.md`
- **Raw:** `[[raw/local/readme-ed089f4555.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Benchmark Suites vLLM provides comprehensive benchmarking tools for performance testing and evaluation: - **[Benchmark CLI](./cli.md)**: `vllm bench` CLI tools and specialized benchmark scripts for interactive performance testing. - **[Parameter Sweeps](./sweeps.md)**: Automate `vllm bench` runs for multiple configurations, useful for [optimization and tuning](../configuration/optimization.md). - **[Performance Dashboard](./dashboard.md)**: Automated CI that publishes benchmarks on each commit.

### README
- **Source:** `local:projects/LLM-Infra/vllm/benchmarks/README.md`
- **Raw:** `[[raw/local/readme-85d2b363bc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Benchmarks This directory used to contain vLLM's benchmark scripts and utilities for performance testing and evaluation. ## Contents - **Serving benchmarks**: Scripts for testing online inference performance (latency, throughput) - **Throughput benchmarks**: Scripts for testing offline batch inference performance - **Specialized benchmarks**: Tools for testing specific features like structured output, prefix caching, long document QA, request prioritization, and multi-modal inference - **Dataset utilities**: Framework for loading and sampling from various benchmark datasets (ShareGPT, HuggingFace datasets, synthetic data, etc.) ## Usage For detailed usage instructions, examples, and…

### add_label_automerge
- **Source:** `local:projects/LLM-Infra/vllm/.github/workflows/add_label_automerge.yml`
- **Raw:** `[[raw/local/add_label_automerge-1a386af6e7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Add label on auto-merge enabled permissions: pull-requests: write on: pull_request_target: types: - auto_merge_enabled jobs: add-label-on-auto-merge: runs-on: ubuntu-latest steps: - name: Add label uses: actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd # v8.0.0 with: script: | github.rest.issues.addLabels({ owner: context.repo.owner, repo: context.repo.repo, issue_number: context.issue.number, labels: ['ready'] }) env: GITHUB_TOKEN=<redacted> secrets.GITHUB_TOKEN }}

### benchmarks
- **Source:** `local:projects/LLM-Infra/vllm/.buildkite/test_areas/benchmarks.yaml`
- **Raw:** `[[raw/local/benchmarks-9849f41d06.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** group: Benchmarks depends_on: - image-build steps: - label: Benchmarks timeout_in_minutes: 20 working_dir: "/vllm-workspace/.buildkite" source_file_dependencies: - benchmarks/ commands: - bash scripts/run-benchmarks.sh - label: Benchmarks CLI Test timeout_in_minutes: 20 source_file_dependencies: - vllm/ - tests/benchmarks/ commands: - pytest -v -s benchmarks/
