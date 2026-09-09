---
title: Personal Vision
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Personal Vision

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### nous-test
- **Source:** `github:SouthpawIN/nous-test`
- **Raw:** `[[raw/github/nous-test-94e0491cee.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Test profile for forge verification # nous-test Test profile for forge verification ## Install ## Skills android, mlops-inference, mlops-model-registry, mlops-training, productivity-office, research-knowledge ## License MIT

### nous-style-guide
- **Source:** `github:SouthpawIN/nous-style-guide`
- **Raw:** `[[raw/github/nous-style-guide-89eee1e8e0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Distributable Hermes Agent skill: Nous Research brand identity, monochrome design rules, image generation templates # Nous Style Guide Distributable skill for Hermes Agent — Nous Research brand identity rules and design templates. **Install:** ## What's Included - **SKILL.md** — Complete brand guide: colors, typography, layout principles, image generation prompt templates - **Reference PDF** — [NOUS-BRAND-BOOKLET-firstedition_1.pdf](https://github.com/SouthpawIN/nous-style-guide/releases/latest/download/NOUS-BRAND-BOOKLET-firstedition_1.pdf) (download from Releases) ## Usage Once installed, the agent automatically loads this skill when you ask for infographics, diagrams, blog art, or any…

### southpawin.github.io
- **Source:** `github:SouthpawIN/southpawin.github.io`
- **Raw:** `[[raw/github/southpawin.github.io-d692a194cf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Southpaw personal site — TOWARDS SELF-IMPROVEMENT. Blog, projects, models, the pet. # sovthpaw — Personal Site This repo is the front door for everything I build. It's deployed to **https://southpawin.github.io/** via GitHub Pages. ## What's here - **Blog** — long-form posts on the OmniSenter pipeline, the pet, the radio - **Projects** — every repo, with descriptions and links - **Models** — the curated catalog - **Wiki** — the reference: every concept and entity, cross-linked ## How it works - Source: Markdown in `docs/` - Theme: MkDocs Material with custom Nous cosmic-variant CSS - Build: GitHub Actions → `mkdocs build` → deploy to Pages - Branch: `main` ## Local dev Then visit…

### index
- **Source:** `local:.hermes/wiki/visions/index.md`
- **Raw:** `[[raw/local/index-6c0c610b52.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Visions Long-running user visions and overarching goals. These are the north stars that guide fleet activities. ## Active Visions *No vision pages created yet.* --- *Back to [Wiki Root](../index.md)*

### model-database
- **Source:** `local:projects/turbofit/references/model-database.yaml`
- **Raw:** `[[raw/local/model-database-7cabb37598.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** archetypes: aux: cpu_moe: ctx_max: 1048576 name: 35B MoE with cpu-moe notes: MoE experts offloaded to CPU RAM size_gb: 11 tier: sf vram_gb: 11 primary: ctx_max: 1048576 examples: - Carnice 35A3B Apex name: 35B MoE 3B-active (Q4) size_gb: 11 tier: sf vram_gb: 17 small: ctx_max: 32768 examples: - Qwen2.5-Omni-3B name: Small multimodal (≤3B) size_gb: 2-3 tier: c vram_gb: 3 main: budget: ctx_max: 262144 examples: - Qwable 27B base - Qwen 3.6-27B base name: 27B dense base (Q4) size_gb: 16-17 tier: c vram_gb: 22 heavy: ctx_max: 1048576 examples: - Darwin 28B Reason - Qwen 3.6-27B fine-tunes - Llama 3.3 27B name: 27-28B dense (Q4) size_gb: 14-17 tier: s vram_gb: 22 light: ctx_max: 262144 examples:…

### curated-lineup
- **Source:** `local:projects/turbofit/references/curated-lineup.md`
- **Raw:** `[[raw/local/curated-lineup-843a30bbdb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Curated Model Lineup Opinionated picks for main + aux roles, local + API. **Ranked by actual benchmark scores, not heuristics.** ## API Model Leaderboard (by benchmark scores — June 2026) ### Main API — text-only mains (must pair with vision aux) Ranked by composite score (GPQA + SWE-bench + MMLU + AIME weighted equally): | Rank | Model | MMLU | GPQA Diamond | SWE-bench Verified | SWE-bench Pro | AIME 2026 | Cost (in/out) | Context | Through Nous? | |------|-------|------|-------------|-------------------|---------------|-----------|---------------|---------|---------------| | 1 | **Qwen 3.7 MAX** | 93.7% (#1) | 92.4% | — | 60.6% | — | $1.25/$3.75 | 1M | ✅ `qwen/qwen3.7-max` | | 2 |…

- **Collapsed duplicates:** `local:projects/sirvir/skills/turbofit/references/curated-lineup.md`, `local:projects/sovth-config/skills/turbofit/references/curated-lineup.md`, `local:projects/turbofit/skills/turbofit/references/curated-lineup.md`

### api-tier-rankings
- **Source:** `local:projects/turbofit/references/api-tier-rankings.md`
- **Raw:** `[[raw/local/api-tier-rankings-20a12946a3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # API Tier Rankings (2026-06-25) Curated API models ranked by quality. Prices in $/M tokens (input/output). ## Main API Models (Text-Only — must pair with vision aux) | Rank | Model | Provider | Input $ | Output $ | Vision | Context | Tier | Through Nous? | |------|-------|----------|---------|----------|--------|---------|------|---------------| | 1 | GLM 5.2 | Z.AI / OR / Nous | $0.95 (OR) / $1.40 (Z.AI) | $3.00 (OR) / $4.40 (Z.AI) | ❌ | 1M | S | ✅ `z-ai/glm-5.2` | | 2 | Qwen 3.7 MAX | DashScope / OR / Nous | $1.25 | $3.75 | ❌ | 1M | S | ✅ `qwen/qwen3.7-max` | | 3 | DeepSeek V4 Pro | DS / OR / NIM (free) / Nous | $0.435 (DS) / FREE (NIM) | $0.87 (DS) / FREE (NIM) | ❌ | 1M | S | ✅…

- **Collapsed duplicates:** `local:projects/sirvir/skills/turbofit/references/api-tier-rankings.md`, `local:projects/southpaw/sovth-config/skills/turbofit/references/api-tier-rankings.md`, `local:projects/sovth-config/skills/turbofit/references/api-tier-rankings.md`, `local:projects/turbofit/skills/turbofit/references/api-tier-rankings.md`

### api-pairing-matrix
- **Source:** `local:projects/turbofit/references/api-pairing-matrix.md`
- **Raw:** `[[raw/local/api-pairing-matrix-0acdaf3a28.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # API Pairing Matrix — Optimal Main+Aux by Price & Context (2026-06-25) Pairings use the user's specified model universe. Prices in $/M tokens (input/output). Aux offset: 40-85% of total tokens route to aux (compression, vision, web summarization, skill search, title gen, MCP routing, approval scoring — 11 slots). ## Model Universe ### Text-Only Mains (no vision — MUST pair with vision aux) | Model | Max Ctx | Input $/M | Output $/M | Provider(s) | Through Nous? | |-------|---------|-----------|-----------|--------------|---------------| | GLM 5.2 | 1M | $0.95 (OR) / $1.40 (Z.AI) | $3.00 (OR) / $4.40 (Z.AI) | Z.AI, OpenRouter, Nous | ✅ `z-ai/glm-5.2` | | Qwen 3.7 MAX | 1M | $1.25 | $3.75 |…

- **Collapsed duplicates:** `local:projects/sirvir/skills/turbofit/references/api-pairing-matrix.md`, `local:projects/southpaw/sovth-config/skills/turbofit/references/api-pairing-matrix.md`, `local:projects/sovth-config/skills/turbofit/references/api-pairing-matrix.md`, `local:projects/turbofit/skills/turbofit/references/api-pairing-matrix.md`

### api-model-rankings
- **Source:** `local:projects/turbofit/references/api-model-rankings.md`
- **Raw:** `[[raw/local/api-model-rankings-72bd730906.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # API Model Rankings (2026-06-25) Curated API models ranked by quality. Prices in $/M tokens (input/output). ## Main API Models (Text-Only — must pair with vision aux) | Rank | Model | Provider | Input $ | Output $ | Vision | Context | Tier | Through Nous? | |------|-------|----------|---------|----------|--------|---------|------|---------------| | 1 | GLM 5.2 | Z.AI / OpenRouter / Nous | $0.95 (OR) / $1.40 (Z.AI) | $3.00 (OR) / $4.40 (Z.AI) | ❌ | 1M | S | ✅ `z-ai/glm-5.2` | | 2 | Qwen 3.7 MAX | DashScope / OpenRouter / Nous | $1.25 | $3.75 | ❌ | 1M | S | ✅ `qwen/qwen3.7-max` | | 3 | DeepSeek V4 Pro | DeepSeek / OpenRouter / NIM (free) / Nous | $0.435 (DS) / $1.74 (OR) / FREE (NIM) | $0.87…

- **Collapsed duplicates:** `local:projects/sirvir/skills/turbofit/references/api-model-rankings.md`, `local:projects/southpaw/sovth-config/skills/turbofit/references/api-model-rankings.md`, `local:projects/sovth-config/skills/turbofit/references/api-model-rankings.md`, `local:projects/turbofit/skills/turbofit/references/api-model-rankings.md`

### guide
- **Source:** `local:docs/ask-hermes-meme-generation/guide.md`
- **Raw:** `[[raw/local/guide-b4adda8978.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Ask Hermes: Meme Generation with Nous Brand Guide > **Version:** 1.0 · **Last updated:** 2026-06-27 > **Skill referenced:** `nous-brand-guide` v2.0.0 (`creative` category) > **Backend:** FAL image generation (managed by Nous subscription) + Carnice (aux vision model) for reference-image analysis --- ## Summary Hermes can generate brand-compliant Nous Research memes on request. The full pipeline is: 1. The user asks for a meme (with an optional reference image). 2. If a reference image is attached, it is **ingested** and analyzed by **Carnice** (the aux vision model) to extract subject, composition, mood, and text. 3. The `nous-brand-guide` skill is loaded so the resulting prompt adheres…

### distribution
- **Source:** `local:projects/nous-girl/distribution.yaml`
- **Raw:** `[[raw/local/distribution-97445b34d9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: nous-girl version: 0.1.0 description: "Hermes Agent profile: nous-girl" author: SouthpawIN license: MIT hermes_requires: ">=0.12.0" env_requires: [] distribution_owned: - SOUL.md - config.yaml - skills/

### curated-lineup
- **Source:** `local:projects/southpaw/sovth-config/skills/turbofit/references/curated-lineup.md`
- **Raw:** `[[raw/local/curated-lineup-68ccf0b2e3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Curated Model Lineup Opinionated picks for main + aux roles, local + API. **Good intelligence is always available no matter your hardware.** ## Hardware Tiers | Tier | VRAM | Setup | Default Main | Default Aux | Gateway | |------|------|-------|-------------|-------------|---------| | **Beefy** | ≥24GB | Local main + local aux | 27-28B dense (Q4) | 35B MoE 3B-active | N/A (local) | | **Modest** | 8-24GB | API main + free/cheap aux | DeepSeek V4 Pro (API) | Qwen 3.6 Plus (OR free) or MiniMax M3 (NIM free) | 🟡/⚪ | | **Thin** | <8GB or no GPU | API main + API aux | DeepSeek V4 Flash (NIM free) | MiniMax M3 (NIM free) | ⚪ NIM | `serve auto` detects your tier. `--api` forces API mode. `--free`…

### model-database
- **Source:** `local:projects/southpaw/sovth-config/skills/turbofit/references/model-database.yaml`
- **Raw:** `[[raw/local/model-database-aac2f71405.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Turbofit Model Database — Dynamic Source of Truth # Last updated: 2026-06-26 # This file is auto-updated by the daily research cron and synced to GitHub. # All turbofit skill references read from this file instead of hardcoded tables. # # Schema: # models: # <slug>: # name: Human-readable name # family: Model family (Qwen, GLM, DeepSeek, Mimo, MiniMax, Kimi, Llama, Grok, Phi, Gemma, etc.) # version: Version string # type: api | local | both # vision: true | false # role: main | aux | either # context_max: Maximum context in tokens # context_tiers: [list of supported context tiers] # pricing: # nous: { input: $/M, output: $/M, slug: "nous-model-slug" } # Through Nous gateway # openrouter:…

### config
- **Source:** `local:projects/southpaw/kashik/config.yaml`
- **Raw:** `[[raw/local/config-e1b407cf8a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: base_url: *** default: qwen/qwen3.6-flash provider: nous providers: {} fallback_providers: [] credential_pool_strategies: {} toolsets: - hermes-cli agent: max_turns: 120 gateway_timeout: 3600 restart_drain_timeout: 180 api_max_retries: 3 tool_use_enforcement: auto terminal: backend: local cwd: . timeout: 180 persistent_shell: true browser: inactivity_timeout: 120 command_timeout: 30 file_read_max_chars: 200000 tool_output: max_bytes: 50000 max_lines: 2000 max_line_length: 2000 compression: enabled: true threshold: 0.95 target_ratio: 0.2 protect_last_n: 20 auxiliary: vision: provider: nous model: qwen/qwen3.5-flash-02-23 web_extract: provider: nous model: qwen/qwen3.5-flash-02-23…

### writing-guide
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/references/writing-guide.md`
- **Raw:** `[[raw/local/writing-guide-5cc1931707.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ML Paper Writing Philosophy & Best Practices This reference compiles writing advice from prominent ML researchers including Neel Nanda, Andrej Karpathy, Sebastian Farquhar, Zachary Lipton, and Jacob Steinhardt. --- ## Contents - [The Narrative Principle](#the-narrative-principle) - [Time Allocation](#time-allocation) - [Abstract Writing Formula](#abstract-writing-formula) - [Introduction Structure](#introduction-structure) - [Sentence-Level Clarity](#sentence-level-clarity) - [Word Choice and Precision](#word-choice-and-precision) - [Mathematical Writing](#mathematical-writing) - [Figure Design](#figure-design) - [Common Mistakes to Avoid](#common-mistakes-to-avoid) --- ## The Narrative…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/references/writing-guide.md`, `local:projects/jestur/skills/research/research-paper-writing/references/writing-guide.md`, `local:projects/dev-coder/skills/research/research-paper-writing/references/writing-guide.md`, `local:projects/dev-orch/skills/research/research-paper-writing/references/writing-guide.md`, `local:projects/dev-review/skills/research/research-paper-writing/references/writing-guide.md`

### feature-request
- **Source:** `local:projects/southpaw/klerik/skills/github/github-issues/templates/feature-request.md`
- **Raw:** `[[raw/local/feature-request-43962f5a39.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Feature Description <!-- What do you want? --> ## Motivation <!-- Why would this be useful? What problem does it solve? --> ## Proposed Solution <!-- How could it work? Include API sketches, CLI examples, or mockups if helpful --> ## Alternatives Considered <!-- Other approaches and why they're less ideal --> - ## Scope / Effort Estimate <!-- How big is this? What areas of the codebase would it touch? --> Small / Medium / Large — <!-- explanation --> ## Additional Context <!-- Links to similar features in other tools, relevant discussions, etc. -->

- **Collapsed duplicates:** `local:projects/klerik/skills/github/github-issues/templates/feature-request.md`, `local:projects/jestur/skills/github/github-issues/templates/feature-request.md`, `local:projects/dev-coder/skills/github/github-issues/templates/feature-request.md`, `local:projects/dev-orch/skills/github/github-issues/templates/feature-request.md`, `local:projects/dev-review/skills/github/github-issues/templates/feature-request.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/dogfood/SKILL.md`
- **Raw:** `[[raw/local/skill-36b1a710c6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: dogfood description: "Exploratory QA of web apps: find bugs, evidence, reports." version: 1.0.0 platforms: [linux, macos, windows] metadata: hermes: tags: [qa, testing, browser, web, dogfood] related_skills: [] --- # Dogfood: Systematic Web Application QA Testing ## Overview This skill guides you through systematic exploratory QA testing of web applications using the browser toolset. You will navigate the application, interact with elements, capture evidence of issues, and produce a structured bug report. ## Prerequisites - Browser toolset must be available (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_vision`, `browser_console`,…

- **Collapsed duplicates:** `local:projects/klerik/skills/dogfood/SKILL.md`, `local:projects/jestur/skills/dogfood/SKILL.md`, `local:projects/dev-coder/skills/dogfood/SKILL.md`, `local:projects/dev-orch/skills/dogfood/SKILL.md`, `local:projects/dev-review/skills/dogfood/SKILL.md`

### x.ai
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/x.ai.md`
- **Raw:** `[[raw/local/x.ai-5454af16b5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: xAI > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Geist Mono` | **Mono:** `Geist Mono` > - **Font stack (CSS):** `font-family: 'Geist Mono', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere xAI's website…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/x.ai.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/x.ai.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/x.ai.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/x.ai.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/x.ai.md`

### wise
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/wise.md`
- **Raw:** `[[raw/local/wise-6496785cb6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Wise > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Wise's website is a bold,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/wise.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/wise.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/wise.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/wise.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/wise.md`

### supabase
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/supabase.md`
- **Raw:** `[[raw/local/supabase-deeabf2b03.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Supabase > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `Source Code Pro` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Supabase's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/supabase.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/supabase.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/supabase.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/supabase.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/supabase.md`

### together.ai
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/together.ai.md`
- **Raw:** `[[raw/local/together.ai-de149f63fd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Together AI > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Together…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/together.ai.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/together.ai.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/together.ai.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/together.ai.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/together.ai.md`

### stripe
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/stripe.md`
- **Raw:** `[[raw/local/stripe-cdddebb03b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Stripe > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Source Sans 3` | **Mono:** `Source Code Pro` > - **Font stack (CSS):** `font-family: 'Source Sans 3', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme &…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/stripe.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/stripe.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/stripe.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/stripe.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/stripe.md`

### runwayml
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/runwayml.md`
- **Raw:** `[[raw/local/runwayml-81fe46161a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Runway > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Runway's interface is a…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/runwayml.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/runwayml.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/runwayml.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/runwayml.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/runwayml.md`

### sentry
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/sentry.md`
- **Raw:** `[[raw/local/sentry-edac951ab2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Sentry > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Rubik` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Rubik', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Sentry's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/sentry.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/sentry.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/sentry.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/sentry.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/sentry.md`

### revolut
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/revolut.md`
- **Raw:** `[[raw/local/revolut-1d024aa810.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Revolut > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Revolut's website is…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/revolut.md`

### pinterest
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/pinterest.md`
- **Raw:** `[[raw/local/pinterest-eaec9d13e6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Pinterest > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Pinterest's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/pinterest.md`

### mistral.ai
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/mistral.ai.md`
- **Raw:** `[[raw/local/mistral.ai-82b090855a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Mistral AI > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Mistral…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/mistral.ai.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/mistral.ai.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/mistral.ai.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/mistral.ai.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/mistral.ai.md`

### linear.app
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/linear.app.md`
- **Raw:** `[[raw/local/linear.app-0826aef4c6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Linear > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Linear's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/linear.app.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/linear.app.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/linear.app.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/linear.app.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/linear.app.md`

### mongodb
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/mongodb.md`
- **Raw:** `[[raw/local/mongodb-96531df710.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: MongoDB > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `Source Code Pro` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere MongoDB's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/mongodb.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/mongodb.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/mongodb.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/mongodb.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/mongodb.md`

### minimax
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/minimax.md`
- **Raw:** `[[raw/local/minimax-8b1cfa04f4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: MiniMax > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere MiniMax's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/minimax.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/minimax.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/minimax.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/minimax.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/minimax.md`

### mintlify
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/mintlify.md`
- **Raw:** `[[raw/local/mintlify-2a1e56e99f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Mintlify > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `Geist Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Mintlify's website…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/mintlify.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/mintlify.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/mintlify.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/mintlify.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/mintlify.md`

### kraken
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/kraken.md`
- **Raw:** `[[raw/local/kraken-4c31864981.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Kraken > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Kraken's website is a…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/kraken.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/kraken.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/kraken.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/kraken.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/kraken.md`

### hashicorp
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/hashicorp.md`
- **Raw:** `[[raw/local/hashicorp-fc14c7103c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: HashiCorp > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere HashiCorp's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/hashicorp.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/hashicorp.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/hashicorp.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/hashicorp.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/hashicorp.md`

### figma
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/figma.md`
- **Raw:** `[[raw/local/figma-d04a522572.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Figma > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Figma's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/figma.md`

### intercom
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/intercom.md`
- **Raw:** `[[raw/local/intercom-a8a3f040a1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Intercom > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Intercom's website is…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/intercom.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/intercom.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/intercom.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/intercom.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/intercom.md`

### coinbase
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/coinbase.md`
- **Raw:** `[[raw/local/coinbase-d34fc53bf9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Coinbase > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Coinbase's website…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/coinbase.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/coinbase.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/coinbase.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/coinbase.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/coinbase.md`

### clickhouse
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/clickhouse.md`
- **Raw:** `[[raw/local/clickhouse-1f92343a51.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: ClickHouse > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/clickhouse.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/clickhouse.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/clickhouse.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/clickhouse.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/clickhouse.md`

### claude
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/claude.md`
- **Raw:** `[[raw/local/claude-0644dd065f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Claude (Anthropic) > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/claude.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/claude.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/claude.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/claude.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/claude.md`

### composio
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/composio.md`
- **Raw:** `[[raw/local/composio-2398498177.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Composio > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/composio.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/composio.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/composio.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/composio.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/composio.md`

### cursor
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/cursor.md`
- **Raw:** `[[raw/local/cursor-9c0584ad58.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Cursor > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Cursor's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/cursor.md`

### airbnb
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/airbnb.md`
- **Raw:** `[[raw/local/airbnb-4d6277a1e6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Airbnb > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Airbnb's website is…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/airbnb.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/airbnb.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/airbnb.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/airbnb.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/airbnb.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/SKILL.md`
- **Raw:** `[[raw/local/skill-cd89bdb860.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: popular-web-designs description: 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS. version: 1.0.0 author: Hermes Agent + Teknium (design systems sourced from VoltAgent/awesome-design-md) license: MIT tags: [design, css, html, ui, web-development, design-systems, templates] platforms: [linux, macos, windows] triggers: - build a page that looks like - make it look like stripe - design like linear - vercel style - create a UI - web design - landing page - dashboard design - website styled like --- # Popular Web Designs 54 real-world design systems ready for use when generating HTML/CSS. Each template captures a site's complete visual language: color palette, typography…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/SKILL.md`, `local:projects/jestur/skills/creative/popular-web-designs/SKILL.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/SKILL.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/SKILL.md`, `local:projects/dev-review/skills/creative/popular-web-designs/SKILL.md`

### visual-design
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/visual-design.md`
- **Raw:** `[[raw/local/visual-design-6703a312d9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Visual Design Principles ## 12 Core Principles 1. **Geometry Before Algebra** — Show the shape first, the equation second. 2. **Opacity Layering** — PRIMARY=1.0, CONTEXT=0.4, GRID=0.15. Direct attention through brightness. 3. **One New Idea Per Scene** — Each scene introduces exactly one concept. 4. **Spatial Consistency** — Same concept occupies the same screen region throughout. 5. **Color = Meaning** — Assign colors to concepts, not mobjects. If velocity is blue, it stays blue. 6. **Progressive Disclosure** — Show simplest version first, add complexity incrementally. 7. **Transform, Don't Replace** — Use Transform/ReplacementTransform to show connections. 8. **Breathing Room** —…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/visual-design.md`, `local:projects/jestur/skills/creative/manim-video/references/visual-design.md`, `local:projects/dev-coder/skills/creative/manim-video/references/visual-design.md`, `local:projects/dev-orch/skills/creative/manim-video/references/visual-design.md`, `local:projects/dev-review/skills/creative/manim-video/references/visual-design.md`

### starter
- **Source:** `local:projects/southpaw/klerik/skills/creative/design-md/templates/starter.md`
- **Raw:** `[[raw/local/starter-587571ab91.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- version: alpha name: MyBrand description: One-sentence description of the visual identity. colors: primary: "#0F172A" secondary: "#64748B" tertiary: "#2563EB" neutral: "#F8FAFC" on-primary: "#FFFFFF" on-tertiary: "#FFFFFF" typography: h1: fontFamily: Inter fontSize: 3rem fontWeight: 700 lineHeight: 1.1 letterSpacing: "-0.02em" h2: fontFamily: Inter fontSize: 2rem fontWeight: 600 lineHeight: 1.2 body-md: fontFamily: Inter fontSize: 1rem lineHeight: 1.5 label-caps: fontFamily: Inter fontSize: 0.75rem fontWeight: 600 letterSpacing: "0.08em" rounded: sm: 4px md: 8px lg: 16px full: 9999px spacing: xs: 4px sm: 8px md: 16px lg: 24px xl: 48px components: button-primary: backgroundColor:…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/design-md/templates/starter.md`, `local:projects/jestur/skills/creative/design-md/templates/starter.md`, `local:projects/dev-coder/skills/creative/design-md/templates/starter.md`, `local:projects/dev-orch/skills/creative/design-md/templates/starter.md`, `local:projects/dev-review/skills/creative/design-md/templates/starter.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/creative/creative-ideation/SKILL.md`
- **Raw:** `[[raw/local/skill-a0768ddf76.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ideation title: Creative Ideation — Constraint-Driven Project Generation description: "Generate project ideas via creative constraints." version: 1.0.0 author: SHL0MS license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [Creative, Ideation, Projects, Brainstorming, Inspiration] category: creative requires_toolsets: [] --- # Creative Ideation ## When to use Use when the user says 'I want to build something', 'give me a project idea', 'I'm bored', 'what should I make', 'inspire me', or any variant of 'I have tools but no direction'. Works for code, art, hardware, writing, tools, and anything that can be made. Generate project ideas through creative constraints.…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/creative-ideation/SKILL.md`, `local:projects/jestur/skills/creative/creative-ideation/SKILL.md`, `local:projects/dev-coder/skills/creative/creative-ideation/SKILL.md`, `local:projects/dev-orch/skills/creative/creative-ideation/SKILL.md`, `local:projects/dev-review/skills/creative/creative-ideation/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/creative/claude-design/SKILL.md`
- **Raw:** `[[raw/local/skill-4c24fb9579.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: claude-design description: Design one-off HTML artifacts (landing, deck, prototype). version: 1.0.0 author: BadTechBandit license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [design, html, prototype, ux, ui, creative, artifact, deck, motion, design-system] related_skills: [design-md, popular-web-designs, excalidraw, architecture-diagram] --- # Claude Design for CLI/API Agents Use this skill when the user asks for design work that would normally fit Claude Design, but the agent is running in a CLI/API environment instead of the hosted Claude Design web UI. The goal is to preserve Claude Design's useful design behavior and taste while removing hosted-tool…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/claude-design/SKILL.md`, `local:projects/jestur/skills/creative/claude-design/SKILL.md`, `local:projects/dev-coder/skills/creative/claude-design/SKILL.md`, `local:projects/dev-orch/skills/creative/claude-design/SKILL.md`, `local:projects/dev-review/skills/creative/claude-design/SKILL.md`

### chalkboard
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/chalkboard.md`
- **Raw:** `[[raw/local/chalkboard-d903ffb1bd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # chalkboard Black chalkboard background with colorful chalk drawing style ## Design Aesthetic Classic classroom chalkboard aesthetic with hand-drawn chalk illustrations. Nostalgic educational feel with imperfect, sketchy lines that capture the warmth of traditional teaching. Colorful chalk creates visual hierarchy while maintaining the authentic chalkboard experience. ## Background - Color: Chalkboard Black (#1A1A1A) or Dark Green-Black (#1C2B1C) - Texture: Realistic chalkboard texture with subtle scratches, dust particles, and faint eraser marks ## Typography Hand-drawn chalk lettering style with visible chalk texture. Imperfect baseline adds authenticity. White or bright colored chalk…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/chalkboard.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/chalkboard.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/chalkboard.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/chalkboard.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/chalkboard.md`

### pop-laboratory
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/pop-laboratory.md`
- **Raw:** `[[raw/local/pop-laboratory-c920d07989.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # pop-laboratory Lab manual precision meets pop art color impact—coordinate systems, technical diagrams, and fluorescent accents on blueprint grid. ## Color Palette - Background: Professional grayish-white with faint blueprint grid texture (#F2F2F2) - Primary: Muted teal/sage green (#B8D8BE) for major functional blocks and data zones - High-alert accent: Vibrant fluorescent pink (#E91E63) strictly for warnings, critical data, or "winner" highlights - Marker highlights: Vivid lemon yellow (#FFF200) as translucent highlighter effect for keywords - Line art: Ultra-fine charcoal brown (#2D2926) for technical grids, coordinates, and hairlines ## Visual Elements - Coordinate-style labels on every…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/pop-laboratory.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/pop-laboratory.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/pop-laboratory.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/pop-laboratory.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/pop-laboratory.md`

### craft-handmade
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/craft-handmade.md`
- **Raw:** `[[raw/local/craft-handmade-9174054923.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # craft-handmade (DEFAULT) Hand-drawn and paper craft aesthetic with warm, organic feel. ## Color Palette - Primary: Warm pastels, soft saturated colors, craft paper tones - Background: Light cream (#FFF8F0), textured paper (#F5F0E6) - Accents: Bold highlights, construction paper colors ## Variants | Variant | Focus | Visual Emphasis | |---------|-------|-----------------| | **Hand-drawn** | Cartoon illustration | Simple icons, slightly imperfect lines | | **Paper-cutout** | Layered paper craft | Drop shadows, torn edges, texture | ## Visual Elements - Hand-drawn or cut-paper quality - Organic, slightly imperfect shapes - Layered depth with shadows (paper variant) - Simple cartoon elements…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/craft-handmade.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/craft-handmade.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/craft-handmade.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/craft-handmade.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/craft-handmade.md`

### cyberpunk-neon
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/cyberpunk-neon.md`
- **Raw:** `[[raw/local/cyberpunk-neon-68fdaa033d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # cyberpunk-neon Neon glow on dark backgrounds, futuristic aesthetic ## Color Palette - Primary: Neon pink (#FF00FF), cyan (#00FFFF), electric blue - Background: Deep black (#0A0A0A), dark purple gradients - Accents: Neon glow effects, chrome reflections ## Visual Elements - Glowing neon outlines - Dark atmospheric backgrounds - Digital glitch effects - Circuit patterns - Holographic elements - Rain and reflections ## Typography - Glowing neon text - Digital/tech fonts - Flickering effects - Outlined glow letters ## Best For Tech futures, gaming content, digital culture, futuristic concepts, night aesthetics

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/cyberpunk-neon.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/cyberpunk-neon.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/cyberpunk-neon.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/cyberpunk-neon.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/cyberpunk-neon.md`

### claymation
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/claymation.md`
- **Raw:** `[[raw/local/claymation-c55e726c0d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # claymation 3D clay figure aesthetic with stop-motion charm ## Color Palette - Primary: Saturated clay colors - bright but slightly muted - Background: Neutral studio backdrop, soft gradients - Accents: Complementary clay colors, shiny highlights ## Visual Elements - Clay/plasticine texture on all objects - Fingerprint marks and imperfections - Rounded, sculpted forms - Soft shadows - Stop-motion staging - Miniature set aesthetic ## Typography - Extruded clay letters - Dimensional, rounded text - Playful and chunky - Embedded in clay scenes ## Best For Playful explanations, children's content, stop-motion narratives, friendly processes

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/claymation.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/claymation.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/claymation.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/claymation.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/claymation.md`

### retro-pop-grid
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/retro-pop-grid.md`
- **Raw:** `[[raw/local/retro-pop-grid-d59faa1639.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # retro-pop-grid 1970s retro pop art with strict Swiss international grid, thick black outlines, and flat color blocks. ## Color Palette - Background: Warm vintage cream/beige (#F5F0E6) - Flat accents: Salmon pink, sky blue, mustard yellow, mint green—all muted retro tones - Contrast blocks: Solid pure black (#000000) and solid pure white (#FFFFFF) used strategically for extreme contrast - Line art and outlines: Solid thick black ## Visual Elements - Uniform thick black outlines on all illustrations, text boxes, and grid dividers - Pure 2D flat vector aesthetic with subtle screen print texture - Strict Swiss international grid: poster divided into square and rectangular cells by thick black…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/retro-pop-grid.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/retro-pop-grid.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/retro-pop-grid.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/retro-pop-grid.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/retro-pop-grid.md`

### lego-brick
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/lego-brick.md`
- **Raw:** `[[raw/local/lego-brick-3753f54d30.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # lego-brick Toy brick construction with playful aesthetic ## Color Palette - Primary: Classic LEGO colors - red, blue, yellow, green, white - Background: Light gray baseplate or white - Accents: Bright primary pops, shiny studs ## Visual Elements - Visible brick studs - Modular construction - Minifigure characters - Building instruction style - Stackable elements - Plastic sheen ## Typography - Blocky, bold fonts - LEGO instruction style - Step numbers - Playful appearance ## Best For Building concepts, modular systems, playful education, children's content

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/lego-brick.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/lego-brick.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/lego-brick.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/lego-brick.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/lego-brick.md`

### pixel-art
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/pixel-art.md`
- **Raw:** `[[raw/local/pixel-art-1a1dffbccf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # pixel-art Retro 8-bit gaming aesthetic ## Color Palette - Primary: Limited palette - NES/SNES colors - Background: Black or dark blue, scanlines optional - Accents: Bright pixel highlights, CRT glow ## Visual Elements - Visible pixel grid - Limited color count per sprite - 8-bit or 16-bit style - Retro game UI elements - Pixel-perfect edges - Dithering for gradients ## Typography - Pixel fonts - Blocky letterforms - Game UI style text - Score/stat display style ## Best For Gaming topics, nostalgia content, developer audiences, retro tech themes

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/pixel-art.md`

### morandi-journal
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/morandi-journal.md`
- **Raw:** `[[raw/local/morandi-journal-13d230f406.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # morandi-journal Hand-drawn doodle illustration with warm Morandi color tones and cozy bullet journal aesthetic. ## Color Palette - Background: Warm cream/beige with subtle paper texture (#F5F0E6) - Primary: Muted teal/sage green (#7BA3A8) for headers and frames - Secondary: Warm terracotta/orange (#D4956A) for highlights and numbers - Line art: Dark charcoal brown (#4A4540) - Soft highlights: Pale yellow (#F5E6C8) ## Visual Elements - Hand-drawn doodle illustrations with organic, slightly imperfect ink lines - Washi tape strip decorations (diagonal stripes pattern, beige and brown) - Rounded card containers for brand/option items - Hand-drawn rulers, scales, and progress bars with emoji…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/morandi-journal.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/morandi-journal.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/morandi-journal.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/morandi-journal.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/morandi-journal.md`

### hand-drawn-edu
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/hand-drawn-edu.md`
- **Raw:** `[[raw/local/hand-drawn-edu-f08c3abbdd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # hand-drawn-edu Hand-drawn educational infographic with macaron pastel color blocks on warm cream paper texture. ## Color Palette - Background: Warm cream (#F5F0E8) with subtle paper grain texture - Primary text: Deep charcoal (#2D2D2D) for headlines, outlines - Macaron Blue: #A8D8EA for cool-toned information zones - Macaron Mint: #B5E5CF for growth/positive zones - Macaron Lavender: #D5C6E0 for abstract/concept zones - Macaron Peach: #FFD5C2 for warm-toned zones - Accent: Coral Red (#E8655A) for key data, warnings, emphasis - Muted annotations: Warm gray (#6B6B6B) for secondary labels ## Visual Elements - Macaron pastel rounded cards as distinct information zones - Hand-drawn wavy…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/hand-drawn-edu.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/hand-drawn-edu.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/hand-drawn-edu.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/hand-drawn-edu.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/hand-drawn-edu.md`

### origami
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/origami.md`
- **Raw:** `[[raw/local/origami-58f5143826.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # origami Folded paper forms with geometric precision ## Color Palette - Primary: Solid origami paper colors - red, blue, green, gold - Background: White or soft gray, subtle shadows - Accents: Paper fold highlights, crisp shadows ## Visual Elements - Geometric folded shapes - Visible fold lines - Cast shadows showing depth - Paper texture - Angular, faceted forms - Low-poly aesthetic ## Typography - Clean geometric fonts - Angular letterforms - Folded paper text effect - Minimal, precise labels ## Best For Geometric concepts, transformation topics, Japanese themes, abstract representations

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/origami.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/origami.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/origami.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/origami.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/origami.md`

### dense-modules
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/layouts/dense-modules.md`
- **Raw:** `[[raw/local/dense-modules-5d73084f49.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # dense-modules High-density modular layout with 6-7 typed information modules packed with concrete data. ## Structure - 6-7 distinct modules per image, each serving a specific information function - Every module contains concrete data: brand names, numbers, percentages, parameters - Minimal whitespace—compact spacing prioritized over breathing room - Smaller text acceptable to maximize information density - Each module identified by coordinate label or section marker (e.g., MOD-1, SEC-A) ## Module Archetypes | Module | Purpose | Content Requirements | |--------|---------|---------------------| | **Brand/Selection Array** | Grid of options with recommendations | 4-8 items with icons, names,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/layouts/dense-modules.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/layouts/dense-modules.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/layouts/dense-modules.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/layouts/dense-modules.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/layouts/dense-modules.md`

### aged-academia
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/aged-academia.md`
- **Raw:** `[[raw/local/aged-academia-596be42638.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # aged-academia Historical scientific illustration with aged paper aesthetic. ## Color Palette - Primary: Sepia brown (#704214), aged ink, muted earth tones - Background: Parchment (#F4E4BC), yellowed paper texture - Accents: Faded red annotations, iron gall ink spots ## Variants | Variant | Focus | Visual Emphasis | |---------|-------|-----------------| | **Notebook** | Personal sketches, inventions | Cursive notes, margin annotations | | **Specimen** | Scientific classification | Numbered diagrams, Latin labels | ## Visual Elements - Aged paper texture overlay - Detailed cross-hatching and line work - Scientific illustration precision - Study notes and annotations - Specimen plate or…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/aged-academia.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/aged-academia.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/aged-academia.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/aged-academia.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/aged-academia.md`

### base-prompt
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/base-prompt.md`
- **Raw:** `[[raw/local/base-prompt-a0d476aa00.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Create a professional infographic following these specifications: ## Image Specifications - **Type**: Infographic - **Layout**: {{LAYOUT}} - **Style**: {{STYLE}} - **Aspect Ratio**: {{ASPECT_RATIO}} - **Language**: {{LANGUAGE}} ## Core Principles - Follow the layout structure precisely for information architecture - Apply style aesthetics consistently throughout - If content involves sensitive or copyrighted figures, create stylistically similar alternatives - Keep information concise, highlight keywords and core concepts - Use ample whitespace for visual clarity - Maintain clear visual hierarchy ## Text Requirements - All text must match the specified style treatment - Main titles should…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/base-prompt.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/base-prompt.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/base-prompt.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/base-prompt.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/base-prompt.md`

### warm
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/tones/warm.md`
- **Raw:** `[[raw/local/warm-a80705960f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # warm 温馨基调 - Nostalgic, personal, comforting ## Overview Warm, inviting atmosphere for personal stories and nostalgic content. Creates emotional connection through cozy aesthetics and comforting visuals. ## Mood Characteristics - Nostalgic feeling - Personal, intimate atmosphere - Comforting and healing - Memory and reflection - Gentle emotional warmth ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | Slightly reduced | | Contrast | Softer | | Temperature | Warm shift (+15%) | | Brightness | Soft, golden | ## Color Temperature Shift palette toward warm tones: | Original | Warm Shift | |----------|-----------| | Cool blue…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/tones/warm.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/tones/warm.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/tones/warm.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/tones/warm.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/tones/warm.md`

### dramatic
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/tones/dramatic.md`
- **Raw:** `[[raw/local/dramatic-02fe6d7dd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # dramatic 戏剧基调 - High contrast, intense, powerful moments ## Overview High-impact dramatic tone for pivotal moments, conflicts, and breakthroughs. Uses strong contrast and intense compositions to create emotional power. ## Mood Characteristics - Tension and intensity - Pivotal moments - Conflict and resolution - Breakthrough discoveries - Emotional climaxes ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | High (vibrant or deep) | | Contrast | Maximum | | Temperature | Varies for effect | | Brightness | Strong highlights, deep shadows | ## Contrast Approach - Sharp light/dark divisions - Minimal mid-tones - Stark…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/tones/dramatic.md`

### romantic
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/tones/romantic.md`
- **Raw:** `[[raw/local/romantic-7d51adc7c5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # romantic 浪漫基调 - Soft, beautiful, emotionally delicate ## Overview Soft, dreamy atmosphere for romantic and emotionally delicate content. Features decorative elements, sparkles, and beautiful compositions that emphasize feeling and beauty. ## Mood Characteristics - Romance and love - Beauty and elegance - Emotional delicacy - Dreams and hopes - Youth and idealism ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | Soft pastels | | Contrast | Low, gentle | | Temperature | Slightly warm pink | | Brightness | Soft, glowing | ## Color Palette Shift toward romantic tones: | Role | Color | Hex | |------|-------|-----| | Primary |…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/tones/romantic.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/tones/romantic.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/tones/romantic.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/tones/romantic.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/tones/romantic.md`

### wuxia
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/presets/wuxia.md`
- **Raw:** `[[raw/local/wuxia-8f4df8d695.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # wuxia 武侠预设 - Hong Kong martial arts comic style ## Base Configuration | Dimension | Value | |-----------|-------| | Art Style | ink-brush | | Tone | action | | Layout | splash (default) | Equivalent to: art=ink-brush, tone=action ## Unique Rules This preset includes special rules beyond the art+tone combination. When the `wuxia` preset is selected, ALL rules below must be applied. ### Qi/Energy Effects (Required) Martial arts power must be visible through qi effects: | Effect Type | Visual Treatment | |-------------|-----------------| | Internal qi | Glowing aura around character | | External qi | Visible energy projection | | Qi clash | Radiating impact waves | | Qi absorption | Flowing…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/presets/wuxia.md`

### base-prompt
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/base-prompt.md`
- **Raw:** `[[raw/local/base-prompt-9cea612602.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Create a knowledge biography comic page following these guidelines: ## Image Specifications - **Type**: Comic book page with multiple panels - **Orientation**: Portrait (vertical) - **Aspect Ratio**: 2:3 - **Style**: See style-specific reference for visual guidelines ## Panel Structure ### Panel Borders - Clean black lines (1-2px) around each panel - White gutters between panels (8-12px) - Panels arranged for clear reading flow - Variety in panel sizes for visual rhythm ### Panel Composition - Clear focal points in each panel - Proper use of foreground, midground, background - Camera angles vary: eye level, bird's eye, low angle, close-up, wide shot - Action flows logically between panels -…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/base-prompt.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/base-prompt.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/base-prompt.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/base-prompt.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/base-prompt.md`

### minimalist
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/art-styles/minimalist.md`
- **Raw:** `[[raw/local/minimalist-d5ff796d5c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # minimalist 极简画风 - Clean black line art, limited spot color, simplified stick-figure characters ## Overview Minimalist cartoon illustration characterized by clean black line art on white background with very limited spot color for emphasis. Characters are simplified to near-stick-figure abstraction, focusing on gesture and concept rather than anatomical detail. Designed for business allegory, quick-read educational content, and concept illustration. ## Line Work - Clean, uniform black lines (1.5-2px) - No hatching, cross-hatching, or shading techniques - Minimal detail — every line serves a purpose - Bold outlines for characters, thinner lines for props/labels - No decorative flourishes or…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/art-styles/minimalist.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/art-styles/minimalist.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/art-styles/minimalist.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/art-styles/minimalist.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/art-styles/minimalist.md`

### realistic
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/art-styles/realistic.md`
- **Raw:** `[[raw/local/realistic-6b12457bc3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # realistic 写实画风 - Digital painting with realistic proportions and lighting ## Overview Full-color realistic manga style using digital painting techniques. Features anatomically accurate characters, rich gradients, and detailed environmental rendering. Sophisticated aesthetic for mature audiences. ## Line Work - Clean, precise outlines with clear contours - Uniform line weight for character definition - No excessive hatching - rely on color for depth - Smooth curves and realistic anatomical lines - Ligne Claire influence: clean but not simplified ## Character Design - Realistic human proportions (7-8 head heights) - Anatomically accurate features and expressions - Detailed facial structure…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/art-styles/realistic.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/art-styles/realistic.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/art-styles/realistic.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/art-styles/realistic.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/art-styles/realistic.md`

### ink-brush
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/art-styles/ink-brush.md`
- **Raw:** `[[raw/local/ink-brush-cf43c5345b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ink-brush 水墨画风 - Chinese ink brush aesthetics with dynamic strokes ## Overview Traditional Chinese ink brush painting style adapted for comics. Combines calligraphic brush strokes with ink wash effects. Creates atmospheric, artistic visuals rooted in East Asian aesthetics. ## Line Work - 2-3px dynamic brush strokes with varying weight - Ink wash effects, traditional Chinese brush feel - Bold, confident strokes with sharp edges - Flowing lines for fabric and hair - Pressure-sensitive stroke variation ## Character Design - Realistic human proportions (7.5-8 head heights) - Defined features with ink brush definition - Dynamic poses capturing movement - Flowing hair and clothing in motion -…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/art-styles/ink-brush.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/art-styles/ink-brush.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/art-styles/ink-brush.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/art-styles/ink-brush.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/art-styles/ink-brush.md`

### chalk
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/art-styles/chalk.md`
- **Raw:** `[[raw/local/chalk-735f5eea57.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # chalk 粉笔画风 - Chalkboard aesthetic with hand-drawn warmth ## Overview Classic classroom chalkboard aesthetic with hand-drawn chalk illustrations. Nostalgic educational feel with imperfect, sketchy lines that capture the warmth of traditional teaching. ## Line Work - Sketchy, imperfect hand-drawn lines - Chalk texture on all strokes - Varying line weight from chalk pressure - Soft edges, no sharp digital lines - Visible chalk dust effects ## Character Design - Simplified, friendly character designs - Stick figures to semi-detailed range - Expressive through simple gestures - Approachable, non-intimidating - Educational presenter style ## Background - Chalkboard Black (#1A1A1A) or Dark…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/art-styles/chalk.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/art-styles/chalk.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/art-styles/chalk.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/art-styles/chalk.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/art-styles/chalk.md`

### model-database
- **Source:** `local:projects/sirvir/skills/turbofit/references/model-database.yaml`
- **Raw:** `[[raw/local/model-database-fe05553906.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** archetypes: aux: cpu_moe: ctx_max: 1048576 name: 35B MoE with cpu-moe notes: MoE experts offloaded to CPU RAM size_gb: 11 tier: sf vram_gb: 11 primary: ctx_max: 1048576 examples: - Carnice 35A3B Apex name: 35B MoE 3B-active (Q4) size_gb: 11 tier: sf vram_gb: 17 small: ctx_max: 32768 examples: - Qwen2.5-Omni-3B name: Small multimodal (≤3B) size_gb: 2-3 tier: c vram_gb: 3 main: budget: ctx_max: 262144 examples: - Qwable 27B base - Qwen 3.6-27B base name: 27B dense base (Q4) size_gb: 16-17 tier: c vram_gb: 22 heavy: ctx_max: 1048576 examples: - Darwin 28B Reason - Qwen 3.6-27B fine-tunes - Llama 3.3 27B name: 27-28B dense (Q4) size_gb: 14-17 tier: s vram_gb: 22 light: ctx_max: 262144 examples:…

### 1511419525885726761-README-vs-Code-Verifier--Bootstrap-Idea
- **Source:** `discord-archive:archives/community-projects-showcase/1511419525885726761-README-vs-Code-Verifier--Bootstrap-Idea.txt`
- **Raw:** `[[raw/discord/1511419525885726761-readme-vs-code-verifier--bootstrap-idea-fa86b94ba9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'README-vs-Code Verifier (Bootstrap Idea)' in forum #community-projects-showcase # thread_id=1511419525885726761 forum_id=1316137596535177246 # Started 2026-06-02T20:46:20.283548+00:00 [2026-06-02T17:21:35.788000+00:00] xriddick (id=1511419525885726761) README-vs-Code Verifier (Bootstrap Idea) Goal: Build a small model that checks whether code actually matches what the README or documentation claims. Version 1: 1. Use a tiny CPU-friendly model (nanoGPT or similar). 2. Dataset: claim,code,label Example: "deletes files","open(path,'w').write('')","LIE" "deletes files","os.remove(path)","MATCH" 3. Train: Claim + Code -> MATCH or LIE 4. Start with 50-100 hand-labeled examples to…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1511419525885726761-README-vs-Code-Verifier--Bootstrap-Idea.txt`

### 1488681202511511694-AutoArticle-pipelined-article-builder-that-is-built-upon-nous-work-on-autonovel.
- **Source:** `discord-archive:archives/community-projects-showcase/1488681202511511694-AutoArticle-pipelined-article-builder-that-is-built-upon-nous-work-on-autonovel..txt`
- **Raw:** `[[raw/discord/1488681202511511694-autoarticle-pipelined-article-builder-that-is-built-upon-nous-work-on-autonovel.-8e0a18b909.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'AutoArticle pipelined article builder that is built upon nous work on autonovel.' in forum #community-projects-showcase # thread_id=1488681202511511694 forum_id=1316137596535177246 # Started 2026-05-10T19:51:01.627887+00:00 [2026-03-31T23:27:37.038000+00:00] valhalladestined (id=1488681202511511694) I’ve been experimenting with different approaches to AI-assisted writing and built a small project called AutoArticle which built on the approach taken by autonovel. Instead of the usual “one prompt → full article” approach, it treats writing as a pipeline with layered stages: Foundation → Draft → Revision → Polish. Each stage focuses on a specific task so the output stays structured…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1488681202511511694-AutoArticle-pipelined-article-builder-that-is-built-upon-nous-work-on-autonovel..txt`

### 1467196023205265430-fahad---ryve-contribution
- **Source:** `discord-archive:archives/community-projects-showcase/1467196023205265430-fahad---ryve-contribution.txt`
- **Raw:** `[[raw/discord/1467196023205265430-fahad---ryve-contribution-e4b290bb64.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'fahad | ryve contribution' in forum #community-projects-showcase # thread_id=1467196023205265430 forum_id=1316137596535177246 # Started 2026-05-10T19:51:26.488284+00:00 [2026-01-31T16:33:11.116000+00:00] fahadgo (id=1467196023205265430) [attachment] amar_twitter_and_dcc_er_piq.jpg https://cdn.discordapp.com/attachments/1467196023205265430/1467196023410524272/amar_twitter_and_dcc_er_piq.jpg?ex=6a0204c7&is=6a00b347&hm=320b2991c5c5e9e169925fb9f47bcec2e53cb661e33a5c0bbcf51b3d870f7c22& [2026-01-31T16:33:54.548000+00:00] fahadgo (id=1467196205372149822) judt did my 1st contribution https://github.com/NousResearch/atropos/pull/349 [attachment] image.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1467196023205265430-fahad---ryve-contribution.txt`

### 1477982563099349036-AI-translater-NVDA-addon-with-Nous-research
- **Source:** `discord-archive:archives/community-projects-showcase/1477982563099349036-AI-translater-NVDA-addon-with-Nous-research.txt`
- **Raw:** `[[raw/discord/1477982563099349036-ai-translater-nvda-addon-with-nous-research-0661f08682.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'AI translater NVDA addon with Nous research' in forum #community-projects-showcase # thread_id=1477982563099349036 forum_id=1316137596535177246 # Started 2026-05-10T19:51:08.612267+00:00 [2026-03-02T10:55:02.631000+00:00] denis_skripnik (id=1477982563099349036) I have been blind since birth. I use a screen reader program. It vocalizes all my actions. Today I created an add-on that translates texts into the languages I need by pressing Insert+Shift+T (selected text), Insert+Shift+Y - from the clipboard. Now I translated this text using Nous! Thank you for this opportunity! Repository: https://github.com/denis-skripnik/ai-translator-addon [embed] GitHub -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1477982563099349036-AI-translater-NVDA-addon-with-Nous-research.txt`

### 1365221985692418131-Open-Reasoning-Tasks
- **Source:** `discord-archive:archives/community-projects-showcase/1365221985692418131-Open-Reasoning-Tasks.txt`
- **Raw:** `[[raw/discord/1365221985692418131-open-reasoning-tasks-b912704d20.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Open Reasoning Tasks' in forum #community-projects-showcase # thread_id=1365221985692418131 forum_id=1316137596535177246 # Started 2026-05-10T19:51:34.930941+00:00 [2025-04-25T07:04:45.987000+00:00] teknium (id=1365221985692418131) Introduction The goal of this repository is to gather a diverse set of reasoning tasks designed to improve the reasoning capabilities of LLMs. Contributors are encouraged to submit tasks, provide examples, and optionally include diagrams or workflows to illustrate how the tasks function. Resources Master Reasoning Tasks List You can access the main tasks list table by clicking here (or open tasks.md file in the top level directory):…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1365221985692418131-Open-Reasoning-Tasks.txt`

### 1400600190599303280-Research-Idea--Mixture-of-Collaborative-Experts--MoC---Moving-Beyond-Isolated-Experts
- **Source:** `discord-archive:archives/community-projects-showcase/1400600190599303280-Research-Idea--Mixture-of-Collaborative-Experts--MoC---Moving-Beyond-Isolated-Experts.txt`
- **Raw:** `[[raw/discord/1400600190599303280-research-idea--mixture-of-collaborative-experts--moc---moving-beyond-isolated-experts-30404fcb23.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '[Research Idea] Mixture of Collaborative Experts (MoC): Moving Beyond Isolated Experts' in forum #community-projects-showcase # thread_id=1400600190599303280 forum_id=1316137596535177246 # Started 2026-05-10T19:51:36.404295+00:00 [2025-07-31T22:05:07.332000+00:00] franciscoan. (id=1400600190599303280) Hey everyone, I've been exploring what I see as a core limitation in standard Mixture-of-Experts (MoE) models: **the experts work in complete isolation.** To address this, I've been prototyping a new architecture I'm calling **Mixture of Collaborative Experts (MoC)**, and I would be honored to get feedback from this community. The core concept is to shift from a system where experts…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1400600190599303280-Research-Idea--Mixture-of-Collaborative-Experts--MoC---Moving-Beyond-Isolated-Experts.txt`

### 1371587770111361075-provide--assist-and-provide-input-or-solutions-regarding-everything-related-to-nousresearch.com
- **Source:** `discord-archive:archives/community-projects-showcase/1371587770111361075-provide--assist-and-provide-input-or-solutions-regarding-everything-related-to-nousresearch.com.txt`
- **Raw:** `[[raw/discord/1371587770111361075-provide--assist-and-provide-input-or-solutions-regarding-everything-related-to-nousresearch.com-9f7a48bc5d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'provide, assist and provide input or solutions regarding everything related to nousresearch.com' in forum #community-projects-showcase # thread_id=1371587770111361075 forum_id=1316137596535177246 # Started 2026-05-10T19:51:38.978402+00:00 [2025-05-12T20:40:07.263000+00:00] sandiap5623 (id=1371587770111361075) https://aistudio.instagram.com/ai/1211635743960953/?utm_source=share

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1371587770111361075-provide--assist-and-provide-input-or-solutions-regarding-everything-related-to-nousresearch.com.txt`

### 1365616890218545162-Introducing-the-New-and-Improved-Nous-by-hyeon-Interface
- **Source:** `discord-archive:archives/community-projects-showcase/1365616890218545162-Introducing-the-New-and-Improved-Nous-by-hyeon-Interface.txt`
- **Raw:** `[[raw/discord/1365616890218545162-introducing-the-new-and-improved-nous-by-hyeon-interface-64d28afa85.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Introducing the New and Improved Nous by hyeon Interface' in forum #community-projects-showcase # thread_id=1365616890218545162 forum_id=1316137596535177246 # Started 2026-05-10T19:51:45.981943+00:00 [2025-04-26T09:13:58.563000+00:00] jonghyeon0624 (id=1365616890218545162) With our previous update, the intuitive UI we developed was even adopted by the main Nous site. Still, many users continue to use our version, so we've pushed forward with further enhancements tailored for the evolving Nous ecosystem. first update ariticle: https://x.com/hyeon__dev/status/1906239764157915626 second update article: https://x.com/hyeon__dev/status/1916055761333194926 [attachment]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1365616890218545162-Introducing-the-New-and-Improved-Nous-by-hyeon-Interface.txt`

### 1367486623499161700-Chat-with-Nous-API---NousChat--Elegant-Web-Interface-for-Nous-Research-API
- **Source:** `discord-archive:archives/community-projects-showcase/1367486623499161700-Chat-with-Nous-API---NousChat--Elegant-Web-Interface-for-Nous-Research-API.txt`
- **Raw:** `[[raw/discord/1367486623499161700-chat-with-nous-api---nouschat--elegant-web-interface-for-nous-research-api-d7046f5fea.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🚀 Chat with Nous API - NousChat: Elegant Web Interface for Nous Research API' in forum #community-projects-showcase # thread_id=1367486623499161700 forum_id=1316137596535177246 # Started 2026-05-10T19:51:31.991226+00:00 [2025-05-01T13:03:37.715000+00:00] bynextex (id=1367486623499161700) I've created a sleek, feature-rich interface for testing and utilizing Nous Research models through their API. > This application allows those with Nous Research API access to easily test and explore various models using their own API keys. ✨ **What Makes NousChat Unique?** Unlike other simple frontend implementations, NousChat offers a comprehensive suite of features that enhance the testing and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1367486623499161700-Chat-with-Nous-API---NousChat--Elegant-Web-Interface-for-Nous-Research-API.txt`

### 1382196795031158824-Token-Reasoning-Ideas
- **Source:** `discord-archive:archives/community-projects-showcase/1382196795031158824-Token-Reasoning-Ideas.txt`
- **Raw:** `[[raw/discord/1382196795031158824-token-reasoning-ideas-5bd76841b1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Token Reasoning Ideas' in forum #community-projects-showcase # thread_id=1382196795031158824 forum_id=1316137596535177246 # Started 2026-05-10T19:51:37.929350+00:00 [2025-06-11T03:16:35.910000+00:00] airtightsquid (id=1382196795031158824) Gmgm want to get a sanity check on an idea for a fun side project / experiment I am putting together. Have an initial pipeline put together to collect data and put together reasoning traces for tokens. Rough reasoning trace: (On chain data, analysis of on chain data text), (social data, analysis of social data) (text Reasoning based on on chain and social data) (buy/sell based on actual performance and review of reasoning) (Overall collection…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1382196795031158824-Token-Reasoning-Ideas.txt`

### config
- **Source:** `local:projects/kashik/config.yaml`
- **Raw:** `[[raw/local/config-6844c41bd7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: base_url: https://inference-api.nousresearch.com/v1 default: z-ai/glm-5.2 provider: nous providers: {} fallback_providers: [] credential_pool_strategies: {} toolsets: - hermes-cli agent: max_turns: 120 gateway_timeout: 3600 restart_drain_timeout: 180 api_max_retries: 3 tool_use_enforcement: auto terminal: backend: local cwd: . timeout: 180 persistent_shell: true browser: inactivity_timeout: 120 command_timeout: 30 file_read_max_chars: 200000 tool_output: max_bytes: 50000 max_lines: 2000 max_line_length: 2000 compression: enabled: true threshold: 0.95 target_ratio: 0.2 protect_last_n: 20 auxiliary: vision: provider: nous model: qwen/qwen3.5-flash-02-23 web_extract: provider: nous…

### mkdocs
- **Source:** `local:projects/evolutionary-training/mkdocs.yml`
- **Raw:** `[[raw/local/mkdocs-fe1dc3a2e1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** site_name: OmniSenter Blog site_description: >- A multi-stage agentic MoE with the Ohm self-evolution engine — built on Darwin Family weight-space recombination. site_url: https://southpawin.github.io/omnisenter-blog/ repo_url: https://github.com/SouthpawIN/omnisenter-blog repo_name: SouthpawIN/omnisenter-blog edit_uri: "" # Copyright (appears in footer) copyright: >- OmniSenter by Chris (SouthpawIN) · TOWARDS SELF-IMPROVEMENT # Don't include source/timestamp/docs paths in the nav docs_dir: docs site_dir: site use_directory_urls: true # Theme theme: name: material language: en features: - navigation.tabs - navigation.tabs.sticky - navigation.sections - navigation.expand - navigation.top -…

- **Collapsed duplicates:** `local:projects/omnisenter-blog/mkdocs.yml`

### README
- **Source:** `local:projects/nous-girl-agent/assistant/sprites/omni-va/README.md`
- **Raw:** `[[raw/local/readme-c75dd9fd71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Omni VA eikon — VA avatar # Source: eikon package nous (vendored from herm-tui/node_modules/eikon/eikons/nous) ## Files - `base.png` (98KB) — default avatar, used for the VA window and as the catalog default - `manifest.json` — eikon manifest with state references - `states/` — per-state variants (idle, listening, thinking, speaking, working, error) ## Live2D upgrade path The current eikon is a static PNG, suitable for v1 of the VA. To upgrade to Live2D (for animated expressions, mouse-tracking eye movement, click animations): 1. Source a Live2D model in Cubism 4 format 2. Drop the `.moc3` + textures + `*.model3.json` into `vtuber-core/live2d-models/nous-assistant/` 3. Update…

### EIKON_FORMAT
- **Source:** `local:projects/nous-girl-agent/docs/EIKON_FORMAT.md`
- **Raw:** `[[raw/local/eikon_format-df94e723a9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Eikon Format The VA supports two eikon formats: ## v1 — Static PNG (current) The simplest format. A single PNG, displayed as the VA's avatar. States follow the Herm eikon convention: - `idle` — default resting state - `listening` — user is speaking - `thinking` — model is generating - `speaking` — model has output - `working` — model is in a tool loop - `error` — something went wrong States can be either a still image (`.png`) or a short video loop (`.mp4`). If a state is missing, the base image is used. ## v2 — Live2D (planned upgrade) To upgrade a v1 eikon to Live2D: 1. Source a Live2D model in Cubism 4 format (`.moc3` + textures) 2. Drop the files into…

### CHANGELOG
- **Source:** `local:projects/nous-girl-agent/CHANGELOG.md`
- **Raw:** `[[raw/local/changelog-47d4a2503b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Changelog All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). ## [Unreleased] ### Added - Initial repo skeleton with vendored Open-LLM-VTuber (vtuber-core/) - Curated model catalog (models/curated.yaml) with 7 real model entries - Suggested model candidates (models/suggested.yaml) for promotion - Omni VA eikon sprite (VA/sprites/nous-assistant/) with 6 state variants - Omni VA character config (vtuber-core/characters/nous-assistant.yaml) - Right-click context menu (VA/menus/nous-assistant.yaml) - Three agent prompts:…

### README
- **Source:** `local:projects/personal-site/README.md`
- **Raw:** `[[raw/local/readme-134b6ca590.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # sovthpaw — Personal Site This repo is the front door for everything I build. It's deployed to **https://southpawin.github.io/** via GitHub Pages. ## What's here - **Blog** — long-form posts on the OmniSenter pipeline, the pet, the radio - **Projects** — every repo, with descriptions and links - **Models** — the curated catalog - **Wiki** — the reference: every concept and entity, cross-linked ## How it works - Source: Markdown in `docs/` - Theme: MkDocs Material with custom Nous cosmic-variant CSS - Build: GitHub Actions → `mkdocs build` → deploy to Pages - Branch: `main` ## Local dev Then visit `http://127.0.0.1:8765/`. ## Adding a post 1. Add a new `.md` file under `docs/blog/` 2. Add…

### README
- **Source:** `local:projects/evolutionary-training/blog/README.md`
- **Raw:** `[[raw/local/readme-74580a22c1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # OmniSenter Blog Design posts, deep-dives, and announcements for the OmniSenter project. ## Start here The catalog is the master index — start with [**`CATALOG.md`**](./CATALOG.md) for the full reading order. The naming convention that every post uses is defined in [**`the-omni-family.md`**](./the-omni-family.md). Read that first if any of the names are confusing (Omni vs Senter vs Ohm vs Senter Ohm). ## Master wiki The consolidated knowledge base (in catalog order) lives at [**`../wiki/README.md`**](https://github.com/SouthpawIN/evolutionary-training/blob/master/wiki/README.md). It cross-references every blog post + every concept + every entity. ## Image credits All images generated with…

### session_20260605_124101_8bf670
- **Source:** `session:session_20260605_124101_8bf670.json`
- **Raw:** `[[raw/sessions/session_20260605_124101_8bf670-e094e01201.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** there's a file that was just created on my computer called South Paul breakdown that is a breakdown of what I'm doing with my other agent which is getting my local model situation set up as well as the evolutionary training pipeline radio agent model and plans that I have I want you to find that document read over it and then we're actually going to be making a video breakdown of that using the skills that you have to make a easy to understand video for me to share with the Discord group that I moderate because I am an employee at nous research Ooh, exciting — a video breakdown for the Discord crew! Let me find that document first! 🔍 Let me try a few more search angles — STT might've…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene8_Outro/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-81a6087505.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene8_Outro/4248106075_65536929_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene8_Outro/3205220997_2318836581_2076028380.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene8_Outro/3205220997_1601449021_1376707896.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene8_Outro/3205220997_3653752161_2368728307.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene7_InfiniteLoop/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-b3d59c01ac.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene7_InfiniteLoop/4248106075_2982006669_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene7_InfiniteLoop/3205220997_3611782961_3442986152.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene7_InfiniteLoop/3205220997_3291881883_2019774106.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-cdb146ba69.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/4248106075_1685746490_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/3205220997_509871711_1008132326.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene6_EvolutionRadio/3205220997_3298370552_892228099.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene5_OmniSenter/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-cebaec6ac6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene5_OmniSenter/4248106075_4163519911_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene5_OmniSenter/3205220997_3722464026_1633796073.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene5_OmniSenter/3205220997_2680702870_3653606919.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene5_OmniSenter/3205220997_3774578863_2078828385.mp4'…

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

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene2_LocalServer/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-f6c7c7ce13.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene2_LocalServer/4248106075_4223738845_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene2_LocalServer/3205220997_3364653624_4253377461.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene2_LocalServer/3205220997_2852302903_3792776087.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene2_LocalServer/3205220997_89784688_3218818038.mp4'…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene1_Title/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-878e4e2ac7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene1_Title/4248106075_3784753026_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene1_Title/3205220997_2554475727_650828684.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene1_Title/3205220997_2318836581_4201161137.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/1080p60/partial_movie_files/Scene1_Title/3205220997_4093393195_762485675.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene8_Outro/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-742e12ac8c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene8_Outro/1858565952_65536929_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene8_Outro/961523082_2318836581_2076028380.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene8_Outro/961523082_1601449021_1376707896.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene8_Outro/961523082_3653752161_2368728307.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene7_InfiniteLoop/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-ba951e8048.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene7_InfiniteLoop/1858565952_2982006669_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene7_InfiniteLoop/961523082_3611782961_3442986152.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene7_InfiniteLoop/961523082_3291881883_2019774106.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene7_InfiniteLoop/961523082_3863042283_573005954.mp4'…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-d36f272777.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/1858565952_1685746490_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/961523082_509871711_1008132326.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene6_EvolutionRadio/961523082_3298370552_892228099.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene5_OmniSenter/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-8f36558f5f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene5_OmniSenter/1858565952_4163519911_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene5_OmniSenter/961523082_3722464026_1633796073.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene5_OmniSenter/961523082_2680702870_3653606919.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene5_OmniSenter/961523082_3774578863_2078828385.mp4' file…

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

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene2_LocalServer/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-07ef56c78e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene2_LocalServer/1858565952_4223738845_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene2_LocalServer/961523082_3364653624_4253377461.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene2_LocalServer/961523082_2852302903_3792776087.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene2_LocalServer/961523082_89784688_3218818038.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene1_Title/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-db0c5050b2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene1_Title/1858565952_3784753026_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene1_Title/961523082_2554475727_650828684.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene1_Title/961523082_2318836581_4201161137.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/720p30/partial_movie_files/Scene1_Title/961523082_4093393195_762485675.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene8_Outro/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-21464eedaa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene8_Outro/2713569302_65536929_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene8_Outro/2122946644_2318836581_2076028380.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene8_Outro/2122946644_1601449021_1376707896.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene8_Outro/2122946644_1566446855_2368728307.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene7_InfiniteLoop/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-9a0cbf44e5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene7_InfiniteLoop/2713569302_1237594176_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene7_InfiniteLoop/2122946644_3611782961_1427869424.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene7_InfiniteLoop/2122946644_2390901575_1495561564.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene7_InfiniteLoop/2122946644_3863042283_100663075.mp4'…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-d8e3355fa8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/2713569302_1857963253_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/2122946644_509871711_284057894.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene6_EvolutionRadio/2122946644_528328893_3911637545.mp4' file…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene5_OmniSenter/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-ead508718c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene5_OmniSenter/2713569302_903697089_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene5_OmniSenter/2122946644_3722464026_3079871874.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene5_OmniSenter/2122946644_3704136151_2843942444.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene5_OmniSenter/2122946644_3774578863_3320470075.mp4' file…

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

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene2_LocalServer/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-5a3e7325f0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene2_LocalServer/2713569302_2074621176_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene2_LocalServer/2122946644_3364653624_2213370290.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene2_LocalServer/2122946644_2852302903_2332284121.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene2_LocalServer/2122946644_2000513539_904384602.mp4'…

### partial_movie_file_list
- **Source:** `local:projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene1_Title/partial_movie_file_list.txt`
- **Raw:** `[[raw/local/partial_movie_file_list-7702f2fe9b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This file is used internally by FFMPEG. file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene1_Title/2713569302_1584563606_223132457.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene1_Title/2122946644_2554475727_132226535.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene1_Title/2122946644_2318836581_2976579549.mp4' file 'file:/home/sovthpaw/projects/southpaw-breakdown-video/media/videos/script/480p15/partial_movie_files/Scene1_Title/2122946644_3881780595_2795241512.mp4' file…

### mmlu_conceptual_physics
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_conceptual_physics.yaml`
- **Raw:** `[[raw/local/mmlu_conceptual_physics-0eac76ae4d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: conceptual_physics description: ' The following are multiple choice questions (with answers) about conceptual physics.' fewshot_config: sampler: first_n samples: - question: 'Colors in a soap bubble result from light (A) converted to a different frequency (B) deflection (C) interference (D) polarization' target: Let's think step by step. In a soap bubble film, the light bounces between the two soap-air interfaces many times, interfering with itself constructively or destructively depending on the width of the film. This results in different colors being visible. The answer is (C). - question: 'Compared with the mass of a uranium atom undergoing fission, the combined masses of…

### BROWSER-AUTOMATION-GUIDE
- **Source:** `local:projects/pocket-shop/docs/BROWSER-AUTOMATION-GUIDE.md`
- **Raw:** `[[raw/local/browser-automation-guide-94950bb158.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Browser Automation Guide for Pocket-Shop *Hermes Documentation Extract - March 25, 2026* --- ## Overview Browser automation is the **primary tool** for Pocket-Shop. It enables: - Price lookups on TCGPlayer - Set monitoring on MTGStocks - Email checking via Gmail browser interface - Creating eBay listings (if API not available) --- ## Browser Automation Documentation **Full Docs:** https://hermes-agent.nousresearch.com/docs/user-guide/features/browser ### Backend Options 1. **Browserbase cloud mode** - Managed cloud browsers with anti-bot tooling 2. **Browser Use cloud mode** - Alternative cloud browser provider 3. **Local Chrome via CDP** - Connect to your own Chrome instance 4. **Local…

### wiki_demo
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/data/wiki_demo.txt`
- **Raw:** `[[raw/local/wiki_demo-9d7ff28fd6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Anarchism is a political philosophy and movement that is sceptical of authority and rejects all involuntary, coercive forms of hierarchy. Anarchism calls for the abolition of the state, which it holds to be unnecessary, undesirable, and harmful. As a historically left-wing movement, placed on the farthest left of the political spectrum, it is usually described alongside communalism and libertarian Marxism as the libertarian wing (libertarian socialism) of the socialist movement, and has a strong historical association with anti-capitalism and socialism.Humans lived in societies without formal hierarchies long before the establishment of formal states, realms, or empires. With the rise of…

### Devtools
- **Source:** `local:projects/Mobile/ws-scrcpy/docs/Devtools.md`
- **Raw:** `[[raw/local/devtools-e2d79666e2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Devtools Forward and proxy a WebKit debug-socket from an android device to your browser ## How it works ### Server 1. Find devtools sockets: `adb shell 'grep -a devtools_remote /proc/net/unix'` 2. For each socket request `/json` and `/json/version` 3. Replace websocket address in response with our hostname 4. Combine all data and send to a client ### Client Though each debuggable page explicitly specifies `devtoolsFrontendUrl` it is possible that provided version of devtools frontend will not work in your browser. To ensure that you will be able to debug webpage/webview, client creates three links: - `inspect` - this is a link provided by a remote browser in the answer for `/json` request…
