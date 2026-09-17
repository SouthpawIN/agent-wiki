---
title: Memory Wiki
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Memory Wiki

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### windows
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/snapdragon/windows.md`
- **Raw:** `[[raw/local/windows-a848d199de.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Overview The document covers procedures for installing the latest GPU and NPU drivers, and OpenCL and Hexagon SDKs. In order to use Hexagon NPU on Snapdragon Windows devices the underlying HTP Ops libraries (e.g libggml-htp-v73.so) must be included in the .cat file digitally signed with a trusted certificate. This document covers details on how to generate personal certificate files (.pfx) and how to configure the system to allow for test signatures (aka test-signing). ## Install the latest Adreno OpenCL SDK Either use the trimmed down version (optimized for CI) from https:<credential-redacted> Or download the complete official version from…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/backend/snapdragon/windows.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/snapdragon/windows.md`

### linux
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/backend/snapdragon/linux.md`
- **Raw:** `[[raw/local/linux-f559534e3b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Snapdragon-based Linux devices ## Docker Setup The easiest way to build llama.cpp for a Snapdragon-based Linux device is using the toolchain Docker image (see [github.com/snapdragon-toolchain](https://github.com/snapdragon-toolchain)). This image includes OpenCL SDK, Hexagon SDK, CMake, and the ARM64 Linux cross-compilation toolchain. Cross-compilation is supported on **Linux X86** hosts. The resulting binaries are deployed to and run on the target **Qualcomm Snapdragon ARM64 Linux** device. Note: The rest of the **Linux** build process assumes that you're running inside the toolchain container. ## How to Build Let's build llama.cpp with CPU, OpenCL, and Hexagon backends via CMake…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/snapdragon/linux.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/backend/snapdragon/linux.md`, `local:projects/LLM-Infra/llama.cpp/docs/backend/snapdragon/linux.md`

### syncthing-folder-2224d4
- **Source:** `local:.hermes/wiki/.stfolder/syncthing-folder-2224d4.txt`
- **Raw:** `[[raw/local/syncthing-folder-2224d4-76ca4dd4f1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # This directory is a Syncthing folder marker. # Do not delete. folderID: agent-wiki created: 2026-07-08T22:33:41-05:00

### goop-event-driven
- **Source:** `local:.hermes/wiki/concepts/goop-event-driven.md`
- **Raw:** `[[raw/local/goop-event-driven-a448c4626f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: GOOP — Event-Driven Architecture created: 2026-07-07 updated: 2026-07-07 type: concept tags: [goop, architecture, event-driven, hooks, hermes, senter] confidence: high --- # Senter — Agent Wiki (Event-Driven GOOP) Senter is **one agent** that IS the Agent Wiki. It serves as both: 1. **Conversational front door** — catches ideas as fast as Chris speaks, asks follow-up questions, digs deeper. Never makes Chris wait for background processes. 2. **Background coordination layer** — hooks, markdown triggers, and GEPA pipelines automatically sort everything Chris says into organized wiki knowledge. No cron jobs. No separate factory agents. No polling. Everything is event-driven,…

### inbox
- **Source:** `local:.hermes/wiki/.system/inbox.md`
- **Raw:** `[[raw/local/inbox-d8b4f4fe28.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Inbox created: 2026-07-07 updated: 2026-07-07 type: system --- # Inbox > Write entries here to trigger the Context factory. Mark `[DONE]` when processed. ## Format ## Active Inbox (no pending items — write [NEW] entries to trigger processing)

### README
- **Source:** `local:.hermes/wiki/wiki-topics/research/README.md`
- **Raw:** `[[raw/local/readme-4767ddf6f1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Research created: 2026-07-07 updated: 2026-07-07 type: topic tags: [research, knowledge, docs] --- # Research > Knowledge, documentation, and research output. ## Directories | Dir | What | |---|---| | `~/research/` | Research notes | | `~/crow-lore/` | Crow's deep research output | | `~/docs/` | Documentation | | `~/guides/` | Guides | | `~/nltk_data/` | NLP datasets | | `~/obsidian-sync/` | Obsidian sync config | | `~/wiki/` | Legacy wiki (→ now `~/.hermes/wiki/`) | ## Media Archive | Dir | What | |---|---| | `~/youtube/` | YouTube content | | `~/images/` | Images | | `~/infographic/` | Infographics | | `~/Videos/` `Pictures/` | System media |

### goop-nesting
- **Source:** `local:projects/agent-wiki/goop-nesting.md`
- **Raw:** `[[raw/local/goop-nesting-771448d011.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: GOOP Nesting created: 2026-07-04 updated: 2026-07-07 type: concept tags: [goop, architecture, nesting] --- # GOOP Nesting Architecture The object hierarchy: **Context → Loops → Agents → Skills** Each layer builds on the previous. The nesting means each factory's output is the next factory's input. ## Factory Chain | Factory | Produces | Feeds | |---|---|---| | Context | Context (Wiki pages, queue items) | All factories | | Skills | Skills | Agents | | Agents | Agents | Loops | | Loops | Loops | The Fleet | The full chain: idea → context → skill → agent → loop, all automatic.

### 1517486886778572900-HyAtlas-Memory---7-layer-cognitive-memory-for-Hermes-Agent
- **Source:** `discord-archive:archives/community-projects-showcase/1517486886778572900-HyAtlas-Memory---7-layer-cognitive-memory-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1517486886778572900-hyatlas-memory---7-layer-cognitive-memory-for-hermes-agent-87cc50f00e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'HyAtlas-Memory — 7-layer cognitive memory for Hermes Agent' in forum #community-projects-showcase # thread_id=1517486886778572900 forum_id=1316137596535177246 # Started 2026-06-19T15:10:29.137773+00:00 [2026-06-19T11:11:07.351000+00:00] tunacookie (id=1517486886778572900) HyAtlas-Memory is a memory provider plugin that gives Hermes persistent, structured memory across sessions. https://github.com/tuancookiez-hub/HyAtlas-Memory **What it does automatically** • Captures every conversation, extracts atomic facts via LLM • Injects relevant memories into the prompt before the agent responds (no tool call needed) • Background processing merges duplicates, resolves conflicts, refines…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1517486886778572900-HyAtlas-Memory---7-layer-cognitive-memory-for-Hermes-Agent.txt`

### index
- **Source:** `local:.hermes/wiki/suggestions/index.md`
- **Raw:** `[[raw/local/index-4dd1e8a619.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Suggestions Master suggestion queue. Ideas and improvements waiting to be triaged or implemented. ## Queue *No suggestions queued yet.* --- *Back to [Wiki Root](../index.md)*

### index
- **Source:** `local:.hermes/wiki/failures/index.md`
- **Raw:** `[[raw/local/index-cefe74f58d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Failures Documented failures, root cause analyses, and fixes. Learning from what went wrong. ## Index *No failure pages created yet.* --- *Back to [Wiki Root](../index.md)*

### index
- **Source:** `local:.hermes/wiki/triggers-loops/index.md`
- **Raw:** `[[raw/local/index-e8f3f8bfbf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Loops Running execution loops and their current state. Tracks ongoing automated processes. ## Active Loops *No active loops documented yet.* --- *Back to [Wiki Root](../index.md)*

### index
- **Source:** `local:.hermes/wiki/concepts/index.md`
- **Raw:** `[[raw/local/index-4e2f16bfde.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Concepts Reusable abstractions and conceptual frameworks used across the GOOP fleet. ## Index *No concept pages created yet. Core concepts to document:* - OOP Metaphor (how object-oriented principles apply to agent design) - DSPy/GEPA framework - Continuity architecture - Agent communication patterns - Knowledge representation --- *Back to [Wiki Root](../index.md)*

### index
- **Source:** `local:.hermes/wiki/projects/index.md`
- **Raw:** `[[raw/local/index-a476f92bd5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Projects Active and completed projects within the GOOP fleet. ## Active Projects - [Gentic OOP](gentic-oop/kanban-breakdown.md) - Kanban breakdown for the Gentic OOP initiative - [Winter Album](p_winter-album.md) - Winter album production project ## Completed Projects *No completed projects listed yet.* --- *Back to [Wiki Root](../index.md)*

### 1522436026725961891-Analogy-as-the-core-of-Hermes-memory
- **Source:** `discord-archive:archives/community-projects-showcase/1522436026725961891-Analogy-as-the-core-of-Hermes-memory.txt`
- **Raw:** `[[raw/discord/1522436026725961891-analogy-as-the-core-of-hermes-memory-33c1230f08.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Analogy as the core of Hermes memory' in forum #community-projects-showcase # thread_id=1522436026725961891 forum_id=1316137596535177246 # Started 2026-07-03T08:58:58.591762+00:00 [2026-07-03T02:57:14.265000+00:00] angler6756 (id=1522436026725961891) I built an open-source hybrid memory MemoryProvider for hermes-agent and wanted to share it here. It unifies structured facts + semantic vectors + a knowledge graph in one incrementally-maintained SQLite file (no batch rebuild, no separate vector DB). The part I'm most curious for feedback on: a per-turn analogy slot that surfaces a memory which is structurally similar to the current situation but superficially different HRR phase…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522436026725961891-Analogy-as-the-core-of-Hermes-memory.txt`

### 1522225924047769620-mind---brain-like-memory-for-any-coding-agent.
- **Source:** `discord-archive:archives/community-projects-showcase/1522225924047769620-mind---brain-like-memory-for-any-coding-agent..txt`
- **Raw:** `[[raw/discord/1522225924047769620-mind---brain-like-memory-for-any-coding-agent.-63d5dfc15b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'mind — brain-like memory for any coding agent.' in forum #community-projects-showcase # thread_id=1522225924047769620 forum_id=1316137596535177246 # Started 2026-07-02T13:54:31.613381+00:00 [2026-07-02T13:02:21.883000+00:00] ida7emj (id=1522225924047769620) Introducing mind Your agent doesn’t start from zero anymore. It keeps the important stuff in working memory, recalls related context even from rough hints, and turns repeated patterns into long-term knowledge. Between sessions, the Dreamer cleans things up: strengthens what proved useful, cuts noise, and flags contradictions. So the more you use it, the less you have to re-explain yourself. Your agent won’t forget you or your…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522225924047769620-mind---brain-like-memory-for-any-coding-agent..txt`

### post-upgrade-budget-scorecard
- **Source:** `local:projects/sirvir/skills-capabilities/sirvir-budget/references/post-upgrade-budget-scorecard.md`
- **Raw:** `[[raw/local/post-upgrade-budget-scorecard-fd2087ccca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Post-upgrade Budget Scorecard Use this reference for recurring weekly budget reviews after a routing, provider, or caching upgrade. This scorecard is designed for cases where: - current cache behavior is poor or unknown - the target post-upgrade cache performance is materially better - the user needs green/yellow/red operational thresholds rather than one-off estimates ## Threshold source of truth All scorecard thresholds are defined in `turbofit/references/budget-config.yaml` under the `scorecard` key. This document describes the methodology; the live numbers come from the config. ## Core rule If provider-side cache telemetry is incomplete, treat `effective $ / 1M tokens` as the primary…

### SCHEMA
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/SCHEMA.md`
- **Raw:** `[[raw/local/schema-d77287a279.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Wiki Schema — hermes-unreal58-mcp-llm-wiki created: 2026-07-02 updated: 2026-07-02 --- # Wiki Schema ## Domain Research lore on the proposed **Hermes × Unreal 5.8 MCP × llm-wiki** stack: an agent-orchestrated, long-running, knowledge-accumulating pipeline for game design work. Covers three sub-domains: 1. **Actuator**: Unreal Engine MCP servers (Epic first-party and StraySpark v4.5) 2. **Orchestrator**: Hermes Agent's `/goal` command and completion contracts 3. **Knowledge substrate**: Karpathy's LLM-Wiki pattern, implemented as Hermes' built-in `llm-wiki` skill Plus the integration surface: how these three plug together, and which alternatives exist (AgenticLink,…

### karpathy-llm-wiki-gist
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/karpathy-llm-wiki-gist.md`
- **Raw:** `[[raw/local/karpathy-llm-wiki-gist-f4da43b8be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f ingested: 2026-07-02 sha256: <not computed — not extracted in detail this run; cited via web search title/description and referenced in Hermes SKILL.md> --- # Karpathy Gist — LLM Wiki Authoritative description from web search: > "A pattern for building personal knowledge bases using LLMs. This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code)." Used as the conceptual source for the Karpathy LLM-Wiki pattern. The Hermes SKILL.md explicitly builds on it and attributes it. ## Claim it anchors - "Unlike traditional RAG (which rediscovers knowledge from scratch…

### mindstudio-karpathy-llm-wiki
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/mindstudio-karpathy-llm-wiki.md`
- **Raw:** `[[raw/local/mindstudio-karpathy-llm-wiki-f628cb6fd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code ingested: 2026-07-02 sha256: <not computed — not extracted in detail> --- # MindStudio blog — "What Is Andrej Karpathy's LLM Wiki?" Web-search description: > "Karpathy's LLM wiki turns raw documents into a structured markdown knowledge base Claude can query. Here's how to set it up in 5 minutes." Used as a **community-implementation reference** for the LLM-Wiki pattern. Supports the "multiple independent implementations exist" claim in [[Concepts/karpathy-llm-wiki-pattern]]. ## TODO Full transcript not yet extracted. Lead for next research pass.

### nousresearch-x-announcement
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/nousresearch-x-announcement.md`
- **Raw:** `[[raw/local/nousresearch-x-announcement-72c51fcc4f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://x.com/NousResearch/status/2041378745332961462 ingested: 2026-07-02 sha256: n/a (X post; only title/description captured via web search) --- # NousResearch X post — "LLM Wiki by @karpathy is now a built-in skill in Hermes-Agent" Web-search description: > "Hermes Agent now comes packaged with Karpathy's LLM-Wiki for creating knowledgebases and research vaults with Obsidian!" Used as the authoritative announcement that Hermes ships `llm-wiki` as a built-in skill.

### hermes-llm-wiki-skill-md
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/hermes-llm-wiki-skill-md.md`
- **Raw:** `[[raw/local/hermes-llm-wiki-skill-md-6350f5bfbb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://github.com/NousResearch/hermes-agent/blob/main/skills-capabilities/research/llm-wiki/SKILL.md ingested: 2026-07-02 sha256: <not computed — 507 lines, ~19.7 KB; truncated in web_extract> --- # Hermes — llm-wiki SKILL.md (main branch) Primary authoritative source for the built-in llm-wiki skill. Key contents: - Skill metadata: v2.1.0, MIT, all 3 platforms - Three-layer architecture: raw (immutable) / wiki (agent-owned) / schema - Required orientation every session: SCHEMA.md → index.md → recent log.md - Frontmatter contract: title/created/updated/type/tags/sources/confidence/contested/contradictions - Raw source frontmatter: source_url / ingested / sha256 (body only) - Lint pass:…

### rag-vs-llm-wiki
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/comparisons/rag-vs-llm-wiki.md`
- **Raw:** `[[raw/local/rag-vs-llm-wiki-9b61cedc4f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: RAG retrieval vs. pre-compiled LLM-Wiki created: 2026-07-02 updated: 2026-07-02 type: comparison tags: [knowledge-base, rag, llm-wiki, comparison] sources: [raw/hermes-llm-wiki-skill-md.md, raw/karpathy-llm-wiki-gist.md, raw/mindstudio-karpathy-llm-wiki.md, raw/clearlyreqs-blog.md] confidence: high contested: false --- # RAG vs. LLM-Wiki | Dimension | Traditional RAG (vector store + retrieval) | LLM-Wiki (Karpathy pattern) | |---|---|---| | Knowledge state | Rediscovered per query via embeddings | Compiled once, kept current | | Cross-references | Not pre-built; retrieved on demand | Pre-built as `[[wikilinks]]` | | Contradictions | Invisible (each chunk is isolated) | Explicitly…

### design-bible-as-wiki
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/concepts/design-bible-as-wiki.md`
- **Raw:** `[[raw/local/design-bible-as-wiki-46c9a62033.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Design Bible as llm-wiki (proposed workflow pattern) created: 2026-07-02 updated: 2026-07-02 type: concept tags: [game-design, llm-wiki, workflow, proposed] sources: [raw/hermes-llm-wiki-skill-md.md, raw/karpathy-llm-wiki-gist.md] confidence: medium # pattern is well-supported by the two sources' explicit design principles; the specific "design bible" application is a synthesis (this author's), not a quoted claim contested: false --- # Design Bible as llm-wiki A **proposed workflow pattern** (no published production example yet) for using the Karpathy LLM-Wiki pattern as the substrate of a game project's design bible. ## The pitch A design bible has exactly the properties that…

### catalog-mode
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/concepts/catalog-mode.md`
- **Raw:** `[[raw/local/catalog-mode-3ad61b98bb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Catalog mode (~3K-token tool discovery) created: 2026-07-02 updated: 2026-07-02 type: concept tags: [strayspark, mcp, context-economics, tool-discovery] sources: [raw/strayspark-product-page.md] confidence: high contested: false --- # Catalog mode A **progressive-disclosure pattern** for MCP tool lists, popularised by StraySpark's Unreal MCP Server v4/v4.5. ## Problem `tools/list` over a 400-tool MCP server returns ~60K tokens of tool definitions — most of which any given turn won't call. For a long-running agent loop with a limited context window, that's catastrophic: every turn is paying the "list the tools" tax. ## Solution `tools/list` returns only **4 discovery meta-tools**…

### karpathy-llm-wiki-pattern
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/concepts/karpathy-llm-wiki-pattern.md`
- **Raw:** `[[raw/local/karpathy-llm-wiki-pattern-3fa1c24baf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Karpathy's LLM-Wiki pattern created: 2026-07-02 updated: 2026-07-02 type: concept tags: [karpathy, llm-wiki, knowledge-base, obsidian, markdown] sources: [raw/karpathy-llm-wiki-gist.md, raw/hermes-llm-wiki-skill-md.md] confidence: high contested: false --- # Karpathy's LLM-Wiki pattern An **idea file** (gist 442a6bf555914893e9891c11519de94f, authored by Andrej Karpathy and posted publicly as an "idea file for agents") for building a personal knowledge base using LLMs. The core insight: > "Unlike traditional RAG (which rediscovers knowledge from scratch per query), the wiki compiles knowledge *once* and keeps it current. Cross-references are already there. Contradictions have…

### llm-wiki-skill
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/entities/llm-wiki-skill.md`
- **Raw:** `[[raw/local/llm-wiki-skill-3016478ee7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: llm-wiki skill (Hermes implementation of Karpathy's LLM-Wiki) created: 2026-07-02 updated: 2026-07-02 type: entity tags: [hermes, llm-wiki, karpathy, knowledge-base, obsidian, markdown] sources: [raw/hermes-llm-wiki-skill-md.md, raw/nousresearch-x-announcement.md, raw/karpathy-llm-wiki-gist.md] confidence: high contested: false --- # llm-wiki skill The **built-in Hermes skill** that implements Andrej Karpathy's LLM-Wiki pattern: a persistent, compounding knowledge base of interlinked markdown files, agent-owned and agent-maintained. - Skill metadata: `version 2.1.0`, author "Hermes Agent", MIT licensed, platforms: linux/macos/windows. - Shipped in…

### timeout-management
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/timeout-management.md`
- **Raw:** `[[raw/local/timeout-management-70f09d5436.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Timeout Management **Category**: Resilience Pattern **Applicability**: Preventing resource exhaustion from slow/hanging backends **Sources**: Microsoft Azure, Zuplo, Dev.to, AWS, MeteorOps ## Definition Timeouts are time limits on how long to wait for operations to complete. Without timeouts, hung backends silently consume connections until the entire system fails. ## Types of Timeouts ### 1. Connection Timeout How long to wait for TCP connection to be established. **Typical values**: 1-5 seconds **Rationale**: If backend isn't accepting connections, waiting longer won't help. **Example**: ### 2. Read Timeout (Idle Timeout) How long to wait for response after connection established.…

### guide
- **Source:** `local:docs/hermes-session-search/guide.md`
- **Raw:** `[[raw/local/guide-4131cc5a70.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes Session Search — Finding and Searching Your Conversation History **Last updated:** 2026-07-01 **Applies to:** Hermes Agent (all platforms — CLI, Telegram, Discord, Slack, etc.) ## Summary Hermes Agent stores every conversation you have with it — across CLI, messaging platforms, cron jobs, and batch runs — in a single SQLite database. The built-in `session_search` tool lets the agent (and you, through it) perform full-text search across all past sessions using SQLite's FTS5 engine. It returns **actual messages from the database** — no LLM summarization artifacts, no hallucination, no truncation beyond what the tool itself reconstructs. This guide covers how sessions are stored, how…

### 1521701175584358521-brain--Hexus---Postgres-Powered-Vector-Memory-for-the-Agentic-Age
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1521701175584358521-brain--Hexus---Postgres-Powered-Vector-Memory-for-the-Agentic-Age.txt`
- **Raw:** `[[raw/discord/1521701175584358521-brain--hexus---postgres-powered-vector-memory-for-the-agentic-age-f74d5c364b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread ':brain: Hexus — Postgres-Powered Vector Memory for the Agentic Age' in forum #plugins-skills-and-skins # thread_id=1521701175584358521 forum_id=1485392832154832906 # Started 2026-07-01T03:42:40.164983+00:00 [2026-07-01T02:17:12.100000+00:00] codenamekt (id=1521701175584358521) If you've hit the limits of Hermes' built-in memory (tiny char budget, no semantic search, resets between sessions) — Hexus is a plugin-based memory provider that fixes all of it. **What it is:** A drop-in memory provider plugin for Hermes Agent backed by PostgreSQL + pgvector. Stores embeddings locally via sentence-transformers — zero API cost, zero data leaving your machine. **Key features:** **Hybrid…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1521701175584358521-brain--Hexus---Postgres-Powered-Vector-Memory-for-the-Agentic-Age.txt`

### session-search-vs-memory
- **Source:** `local:research/crow-lore/hermes-session-search/comparisons/session-search-vs-memory.md`
- **Raw:** `[[raw/local/session-search-vs-memory-60ba5248ea.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # session_search vs memory tool **Type:** Tool comparison **Context:** L2 (cross-session recall) vs L1 (persistent notes) ## Core difference | Aspect | `session_search` | `memory` | |--------|------------------|----------| | **Layer** | L2 (on-demand cross-session) | L1 (frozen snapshot in system prompt) | | **Scope** | All past sessions | `MEMORY.md` + `USER.md` files | | **Storage** | `state.db` (SQLite) | Markdown files in `~/.hermes/memories/` | | **Capacity** | Unlimited (all sessions) | 2200 chars (memory), 1375 chars (user) | | **Injection** | Only when tool called | Every turn (system prompt) | | **Update model** | Real-time (every message indexed) | Writes persist immediately,…

### fts5-vs-vector
- **Source:** `local:research/crow-lore/hermes-session-search/comparisons/fts5-vs-vector.md`
- **Raw:** `[[raw/local/fts5-vs-vector-a08e6f9833.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # FTS5 vs vector search **Type:** Technology comparison **Context:** Hermes Agent's choice of SQLite FTS5 over embedding-based vector search ## Cost comparison | Operation | FTS5 | Vector search | |-----------|------|---------------| | Write (per message) | Near zero (SQLite fsync) | Medium (embedding inference) | | Search (per query) | Near zero (BM25 ranking) | Medium (ANN index lookup) | | Ops overhead | Zero (SQLite embedded) | High (deploy Qdrant/Chroma/Pinecone) | | Cross-device sync | Copy `.db` file | Re-index or sync vector store | ## Why Hermes chose FTS5 Joye blog analysis: 1. **BM25 undervalued on single-user data**: When users search their own conversations, query terms and…

### l2-session-search
- **Source:** `local:research/crow-lore/hermes-session-search/concepts/l2-session-search.md`
- **Raw:** `[[raw/local/l2-session-search-88a364db7d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # L2: Session search (cross-session recall) **Type:** Memory layer **Layer:** L2 (on-demand, cross-session) **Part of:** Four-layer memory architecture (L0/L1/L1.5/L2) ## The four layers ## L2 characteristics - **Cross-session**: searches all past conversations, not just the current one - **On-demand**: triggered by tool call, not injected every turn - **Cost-aligned**: cost and benefit are precisely aligned (you only pay when you search) - **No LLM hallucination**: returns actual messages from DB, not generated summaries ## L2 vs L1 (memory tool) | Aspect | L1 (memory) | L2 (session_search) | |--------|-------------|---------------------| | Scope | Frozen snapshot in system prompt |…

### bookends-reconstruction
- **Source:** `local:research/crow-lore/hermes-session-search/concepts/bookends-reconstruction.md`
- **Raw:** `[[raw/local/bookends-reconstruction-3bafe7be0a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Bookends reconstruction **Type:** Context recovery pattern **Mechanism:** Goal → match → resolution structure ## The pattern Discovery mode returns three context windows per session: 1. **`bookend_start`**: first 3 user+assistant messages (the goal/kickoff) 2. **`messages`**: ±5 messages around the FTS5 match (the hit in context) 3. **`bookend_end`**: last 3 user+assistant messages (the resolution/decisions) Together, these reconstruct **goal → match → resolution** without paying for the whole transcript. ## Why bookends? A full session transcript could be 50,000+ tokens. Loading it all would: 1. Blow up context window 2. Dilute relevance (most turns are noise) 3. Cost tokens for…

### three-calling-shapes
- **Source:** `local:research/crow-lore/hermes-session-search/concepts/three-calling-shapes.md`
- **Raw:** `[[raw/local/three-calling-shapes-1b18bb280d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Three calling shapes **Type:** Tool interface pattern **Mechanism:** Argument inference (no `mode` parameter) ## The pattern `session_search` infers behavior from which arguments are set: 1. **Discovery**: pass `query` → FTS5 search, returns top-N sessions 2. **Scroll**: pass `session_id` + `around_message_id` → window around anchor 3. **Browse**: no args → recent sessions chronologically There is no explicit `mode` parameter. The tool dispatches based on argument presence. ## Discovery shape (pass `query`) Runs FTS5, dedupes by session lineage, returns top N sessions. Each result: - `session_id`, `title`, `when`, `source` - `snippet` — FTS5-highlighted match excerpt - `bookend_start` —…

### fts5-query-syntax
- **Source:** `local:research/crow-lore/hermes-session-search/concepts/fts5-query-syntax.md`
- **Raw:** `[[raw/local/fts5-query-syntax-4e4dc6850f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # FTS5 query syntax **Type:** Query language **Engine:** SQLite FTS5 ## Supported operators | Syntax | Example | Meaning | |--------|---------|---------| | Keywords | `docker deployment` | Both terms (implicit AND) | | Quoted phrase | `"exact phrase"` | Exact phrase match | | Boolean OR | `docker OR kubernetes` | Either term | | Boolean NOT | `python NOT java` | Exclude term | | Prefix | `deploy*` | Prefix match | ## Default behavior FTS5 defaults to AND for space-separated keywords. `docker deployment` means both terms must appear (not just one). ## Sanitization The `_sanitize_fts5_query()` method handles edge cases: - **Unmatched quotes**: stripped - **Hyphenated terms**: auto-quoted…

### role-filtering
- **Source:** `local:research/crow-lore/hermes-session-search/concepts/role-filtering.md`
- **Raw:** `[[raw/local/role-filtering-44e496fd01.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Role filtering **Type:** Query parameter **Parameter:** `role_filter` (comma-separated string) ## Purpose Restrict FTS5 search to specific message roles (user, assistant, tool). ## Default Discovery mode defaults to `role_filter="user,assistant"`. Tool output is usually noise for recall purposes. ## When to include tool output Pass `role_filter="user,assistant,tool"` to include tool output. Useful for: - Debugging tool behavior ("what did the terminal tool return when we ran X?") - Finding specific tool invocations Pass `role_filter="tool"` to search tool output only. ## Filtered search examples (Python API) ## Why default excludes tool output Tool calls produce verbose output (full file…

### fts5
- **Source:** `local:research/crow-lore/hermes-session-search/entities/fts5.md`
- **Raw:** `[[raw/local/fts5-588b26c3fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # FTS5 **Type:** SQLite extension (full-text search engine) **Used by:** Hermes Agent for session search ## What FTS5 is FTS5 is SQLite's built-in full-text search engine. It creates virtual tables with inverted indexes that support BM25 relevance ranking, phrase matching, prefix queries, and boolean operators. ## Why Hermes chose FTS5 over vector search Per Joye blog (architectural analysis): 1. **BM25 undervalued on single-user data**: When a user searches for something they wrote themselves, query terms and original messages share vocabulary. Semantic generalization is a liability — it pulls in content from other sessions that merely discussed a similar topic. 2. **Zero write latency**:…

### session-lineage
- **Source:** `local:research/crow-lore/hermes-session-search/entities/session-lineage.md`
- **Raw:** `[[raw/local/session-lineage-74d2dd2e6f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Session lineage **Type:** Data model concept **Mechanism:** `parent_session_id` foreign key in `sessions` table ## How lineage forms When context compression triggers a session split: 1. Old session ends with `end_reason='compression'` 2. New session created with `parent_session_id` = old session ID 3. Title auto-numbered: "My Session" → "My Session #2" (via `get_next_title_in_lineage()`) This creates chains: `session A → session A #2 → session A #3`. ## Lineage exclusion in session_search Discovery mode (passing `query`) parses the delegation chain by recursively walking `parent_session_id` and **excludes the current session's entire ancestor/descendant chain** from results. Prevents the…

### messages-fts
- **Source:** `local:research/crow-lore/hermes-session-search/entities/messages-fts.md`
- **Raw:** `[[raw/local/messages-fts-770737bfe6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # messages_fts **Type:** FTS5 virtual table **Tokenizer:** unicode61 (Latin/English-friendly) ## Purpose The default FTS5 index for English and other Latin-script languages. Maintained automatically via SQLite triggers on INSERT/UPDATE/DELETE of the `messages` table. ## Schema Schema version 11 (latest) switched to **inline mode** and expanded coverage to include `tool_name` + `tool_calls` in addition to message `content`. This means tool call arguments are searchable — significant for agent systems where much of the signal lives in tool arguments. ## Sync triggers ## Performance FTS5 queries rank by BM25 relevance. Typical query: 15–50ms for discovery across hundreds of sessions. Write…

### state-db
- **Source:** `local:research/crow-lore/hermes-session-search/entities/state-db.md`
- **Raw:** `[[raw/local/state-db-07af759c1e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # state.db **Type:** Storage artifact **Default path:** `~/.hermes/state.db` (per-profile via `$HERMES_HOME`) ## Role The canonical store for all session metadata, full message history, token counts, billing data, and FTS indexes. Replaces the older per-session JSONL file approach. ## Architecture ## Key properties - **WAL mode**: concurrent readers + single writer (suits multi-platform gateway) - **Write contention**: application-level retry with 20–150ms jitter, up to 15 retries; BEGIN IMMEDIATE transactions; periodic WAL checkpoint every 50 writes - **Session ID format**: `YYYYMMDD_HHMMSS_<hex>` (6-char hex for CLI, 8-char for gateway) - **Title uniqueness**: unique index on `title`…

### session-search-tool
- **Source:** `local:research/crow-lore/hermes-session-search/entities/session-search-tool.md`
- **Raw:** `[[raw/local/session-search-tool-1fdbc6c7a0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # session_search tool **Type:** Tool (built-in, agent-callable) **Toolset:** `session_search` **Source:** `~/hermes-agent/tools/session_search_tool.py` ## What it does The agent uses `session_search` to recall prior conversations. It runs against `~/.hermes/state.db` (via the `SessionDB` class in `hermes_state.py`). It is FTS5-backed, returns actual messages from the DB (no LLM hallucination), and infers its behavior from which arguments are passed. ## Three calling shapes | Shape | Triggering args | Returns | Typical wall time | |-------|----------------|---------|-------------------| | **Discovery** | `query="..."` | Top-N sessions with snippet + bookends + ±5 window around match |…

### index
- **Source:** `local:research/crow-lore/hermes-session-search/index.md`
- **Raw:** `[[raw/local/index-51685f685f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes Session Search **Slug:** hermes-session-search **Topic:** The `session_search` tool and broader session introspection architecture in Hermes Agent. **Last updated:** 2026-06-30 ## Summary Hermes Agent stores every conversation (CLI, Telegram, Discord, Slack, cron, etc.) in a single SQLite database at `~/.hermes/state.db` with WAL mode and FTS5 full-text search. The built-in `session_search` tool is the agent's primary interface for recalling prior conversations. It exposes three calling shapes (discovery via query, scroll within a session, browse recent) and returns actual messages from the database — no LLM summarization, no truncation beyond what the tool itself reconstructs. The…

### index
- **Source:** `local:research/crow-lore/hermes-session-architecture/index.md`
- **Raw:** `[[raw/local/index-caa86173bf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes Agent Session Architecture & Persistent State Management ## TL;DR Hermes Agent uses a two-tier persistence architecture: 1. **SQLite database** (`state.db`) — primary session store with FTS5 full-text search, message history, token accounting 2. **Profile sessions directory** (`~/.hermes/profiles/<profile>/sessions/`) — supplementary JSON exports, request dumps, and trajectory files Session storage is per-profile (isolated), supports session lineage (compression creates child sessions), and cron jobs write session files to enable auditability and continuability. ## Entities - [state.db (SQLite Database)](entities/state-db.md) — the primary session/message store - [Sessions…

### 1490447053791428718-Mnemosyne---Memory-Plugin-for-Hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1490447053791428718-Mnemosyne---Memory-Plugin-for-Hermes.txt`
- **Raw:** `[[raw/discord/1490447053791428718-mnemosyne---memory-plugin-for-hermes-274b1a747f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Mnemosyne - Memory Plugin for Hermes' in forum #community-projects-showcase # thread_id=1490447053791428718 forum_id=1316137596535177246 # Started 2026-05-10T19:50:43.706770+00:00 [2026-04-05T20:24:28.791000+00:00] nulledvector (id=1490447053791428718) 🧠 Tired of your Hermes agent forgetting everything — or shipping your context to a paid third-party memory service? I built Mnemosyne to kill both problems. It's the native memory system for Hermes. One SQLite database, zero network calls, zero subscriptions, zero vendor lock-in. Why I ditched the cloud: I was paying for Honcho and juggling legacy memory tools that added latency and sent my data somewhere else. I deleted them all.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1490447053791428718-Mnemosyne---Memory-Plugin-for-Hermes.txt`

### 1515595298708258858-rhizome---Karpathy-inspired-memory-knowledgebase-utilizing-DuckDB--QMD--markitdown----more
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1515595298708258858-rhizome---Karpathy-inspired-memory-knowledgebase-utilizing-DuckDB--QMD--markitdown----more.txt`
- **Raw:** `[[raw/discord/1515595298708258858-rhizome---karpathy-inspired-memory-knowledgebase-utilizing-duckdb--qmd--markitdown----more-4101999b42.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🫚 rhizome - Karpathy-inspired memory/knowledgebase utilizing DuckDB, QMD, markitdown, & more' in forum #plugins-skills-and-skins # thread_id=1515595298708258858 forum_id=1485392832154832906 # Started 2026-06-20T08:56:51.529702+00:00 [2026-06-20T04:15:30.511000+00:00] tuck2g (id=1517744681956671610) 🫚 rhizome - Karpathy-inspired memory/knowledgebase utilizing DuckDB, QMD, markitdown, & more [2026-06-20T04:21:48.414000+00:00] tuck2g (id=1517746266996605109) Quick update on the repo with the latest pieces. Rhizome turns dropped documents into a living, searchable wiki that stays in plain markdown on your disk. Agents like Hermes, Claude, Codex, or OpenCode can all read and write to…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1515595298708258858-rhizome---Karpathy-inspired-memory-knowledgebase-utilizing-DuckDB--QMD--markitdown----more.txt`

### 1511278298670305381-Dynamic-emotions--layered-permanent-memory--and-dynamic-transformation-of-personality-infusion.
- **Source:** `discord-archive:archives/community-projects-showcase/1511278298670305381-Dynamic-emotions--layered-permanent-memory--and-dynamic-transformation-of-personality-infusion..txt`
- **Raw:** `[[raw/discord/1511278298670305381-dynamic-emotions--layered-permanent-memory--and-dynamic-transformation-of-personality-infusion.-22e59f8778.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Dynamic emotions, layered permanent memory, and dynamic transformation of personality infusion.' in forum #community-projects-showcase # thread_id=1511278298670305381 forum_id=1316137596535177246 # Started 2026-06-02T10:20:26.511819+00:00 [2026-06-02T08:00:24.596000+00:00] nihilys_14396 (id=1511278298670305381) https://github.com/miyamoriaoi1997-del/Soul-Llink/tree/main The new version has added hierarchical memory management, referencing the Letta project. It no longer uses context management or context compression. It will never suffer from amnesia or lose its goal. [embed] GitHub - miyamoriaoi1997-del/Soul-Llink: Dynamic emotion system fra...…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1511278298670305381-Dynamic-emotions--layered-permanent-memory--and-dynamic-transformation-of-personality-infusion..txt`

### prompt-toolkit
- **Source:** `local:research/crow-lore/custom-hermes-tui/entities/prompt-toolkit.md`
- **Raw:** `[[raw/local/prompt-toolkit-c12ee6da89.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # prompt_toolkit **Library** | Python | Active | Created by Jonathan Slenders `prompt_toolkit` is a library for building powerful interactive command-line applications in Python. It provides line editing, history, auto-completion, and syntax highlighting for REPLs and input prompts. ## Key Characteristics - **Line editing** — Emacs/Vi keybindings, undo/redo, kill ring - **Auto-completion** — fuzzy matching, customizable completers - **Syntax highlighting** — via Pygments - **Multi-line input** — with proper continuation prompts - **Mouse support** — limited to selection and basic clicks - **Cross-platform** — Linux, macOS, Windows - **Async support** — integrates with `asyncio` event loops…

### 1520954056099758171-Resonant-Lattice-Memory--a-neuroplastic-long-horizon--local-first--memory-plugin-for-hermes-agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520954056099758171-Resonant-Lattice-Memory--a-neuroplastic-long-horizon--local-first--memory-plugin-for-hermes-agent.txt`
- **Raw:** `[[raw/discord/1520954056099758171-resonant-lattice-memory--a-neuroplastic-long-horizon--local-first--memory-plugin-for-hermes-agent-adc168660c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Resonant Lattice Memory: a neuroplastic long-horizon, local first, memory plugin for hermes-agent' in forum #plugins-skills-and-skins # thread_id=1520954056099758171 forum_id=1485392832154832906 # Started 2026-06-29T03:45:56.055830+00:00 [2026-06-29T00:48:24.934000+00:00] markfree (id=1520954056099758171) I built a drop-in MemoryProvider for hermes-agent that gives an agent a **real** long-term memory instead of a flat log that grows forever. The core idea is that facts behave like resonant circuits. A memory that keeps getting struck stays in tune and rings loud, so it gets reinforced and promoted into a durable tier. The ones that nothing resonates with fade to silence and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520954056099758171-Resonant-Lattice-Memory--a-neuroplastic-long-horizon--local-first--memory-plugin-for-hermes-agent.txt`

### 1496124109766000690-Mnemosyne---Native--zero-cloud-memory-for-AI-agents.-SQLite-backed.-Sub-millisecond.-Fully-private.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1496124109766000690-Mnemosyne---Native--zero-cloud-memory-for-AI-agents.-SQLite-backed.-Sub-millisecond.-Fully-private..txt`
- **Raw:** `[[raw/discord/1496124109766000690-mnemosyne---native--zero-cloud-memory-for-ai-agents.-sqlite-backed.-sub-millisecond.-fully-private.-1d40589213.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Mnemosyne - Native, zero-cloud memory for AI agents. SQLite-backed. Sub-millisecond. Fully private.' in forum #plugins-skills-and-skins # thread_id=1496124109766000690 forum_id=1485392832154832906 # Started 2026-05-10T19:52:21.293766+00:00 [2026-04-21T12:23:04.410000+00:00] nulledvector (id=1496124109766000690) 🧠 Tired of your Hermes agent forgetting everything — or shipping your context to a paid third-party memory service? I built Mnemosyne to kill both problems. It's the native memory system for Hermes. One SQLite database, zero network calls, zero subscriptions, zero vendor lock-in. Why I ditched the cloud: I was paying for Honcho and juggling legacy memory tools that added…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1496124109766000690-Mnemosyne---Native--zero-cloud-memory-for-AI-agents.-SQLite-backed.-Sub-millisecond.-Fully-private..txt`

### 1520522028799754280-Haku.chat---Telegram-AI-companions-with-memory--looking-for-blunt-feedback
- **Source:** `discord-archive:archives/community-projects-showcase/1520522028799754280-Haku.chat---Telegram-AI-companions-with-memory--looking-for-blunt-feedback.txt`
- **Raw:** `[[raw/discord/1520522028799754280-haku.chat---telegram-ai-companions-with-memory--looking-for-blunt-feedback-b297f7860a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Haku.chat — Telegram AI companions with memory, looking for blunt feedback' in forum #community-projects-showcase # thread_id=1520522028799754280 forum_id=1316137596535177246 # Started 2026-06-28T03:36:03.015523+00:00 [2026-06-27T20:11:41.599000+00:00] jnwlsn__62097 (id=1520522028799754280) Hey Nous folks — sharing a small project we’re testing: Haku.chat, AI companions on Telegram focused on continuity, persistent memory, and a warmer / less “corporate therapist” feel. It’s a free beta right now: no payment, no card, no app install. Mara and Marcus are live from the site. What we’re trying to improve: - memory that actually matters later - natural follow-ups without feeling…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520522028799754280-Haku.chat---Telegram-AI-companions-with-memory--looking-for-blunt-feedback.txt`

### build-and-test-snapdragon
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-and-test-snapdragon.yml`
- **Raw:** `[[raw/local/build-and-test-snapdragon-0aacba00fc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (snapdragon) on: workflow_dispatch: push: branches: - master paths: - '.github/workflows/build-and-test-snapdragon.yml' - 'ggml/include/ggml-hexagon.h' - 'ggml/src/ggml-hexagon/**' - 'docs/backend/snapdragon/**' - 'scripts/snapdragon/**' - 'CMakePresets.json' pull_request: types: [opened, synchronize, reopened] paths: - '.github/workflows/build-and-test-snapdragon.yml' - 'ggml/include/ggml-hexagon.h' - 'ggml/src/ggml-hexagon/**' - 'docs/backend/snapdragon/**' - 'scripts/snapdragon/**' - 'CMakePresets.json' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: android-ndk-snapdragon: runs-on: ubuntu-latest…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/build-and-test-snapdragon.yml`

### config
- **Source:** `local:projects/southpaw/sovth-config/profiles/crow/config.yaml`
- **Raw:** `[[raw/local/config-b8140a2f34.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: base_url: https://inference-api.nousresearch.com/v1 default: z-ai/glm-5.2 provider: nous toolsets: - hermes-cli agent: max_turns: 120 tool_use_enforcement: auto display: personality: concise skin: nord language: en memory: memory_enabled: true memory_char_limit: 2200 skills: template_vars: true context: engine: compressor web: backend: firecrawl platform_toolsets: cli: - file - memory - session_search - skills - terminal - web

- **Collapsed duplicates:** `local:projects/crow/config.yaml`, `local:projects/sovth-config/profiles/crow/config.yaml`, `local:projects/southpaw/crow/config.yaml`

### config
- **Source:** `local:projects/southpaw/kashik/config.yaml`
- **Raw:** `[[raw/local/config-e1b407cf8a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: base_url: *** default: qwen/qwen3.6-flash provider: nous providers: {} fallback_providers: [] credential_pool_strategies: {} toolsets: - hermes-cli agent: max_turns: 120 gateway_timeout: 3600 restart_drain_timeout: 180 api_max_retries: 3 tool_use_enforcement: auto terminal: backend: local cwd: . timeout: 180 persistent_shell: true browser: inactivity_timeout: 120 command_timeout: 30 file_read_max_chars: 200000 tool_output: max_bytes: 50000 max_lines: 2000 max_line_length: 2000 compression: enabled: true threshold: 0.95 target_ratio: 0.2 protect_last_n: 20 auxiliary: vision: provider: nous model: qwen/qwen3.5-flash-02-23 web_extract: provider: nous model: qwen/qwen3.5-flash-02-23…

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/research/llm-wiki/SKILL.md`
- **Raw:** `[[raw/local/skill-a37ae04745.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: llm-wiki description: "Karpathy's LLM Wiki: build/query interlinked markdown KB." version: 2.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [wiki, knowledge-base, research, notes, markdown, rag-alternative] category: research related_skills: [obsidian, arxiv] --- # Karpathy's LLM Wiki Build and maintain a persistent, compounding knowledge base as interlinked markdown files. Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Unlike traditional RAG (which rediscovers knowledge from scratch per query), the wiki compiles knowledge once and keeps it current. Cross-references…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/research/llm-wiki/SKILL.md`, `local:projects/jestur/skills-capabilities/research/llm-wiki/SKILL.md`, `local:projects/dev-coder/skills-capabilities/research/llm-wiki/SKILL.md`, `local:projects/dev-orch/skills-capabilities/research/llm-wiki/SKILL.md`, `local:projects/dev-review/skills-capabilities/research/llm-wiki/SKILL.md`

### block-types
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/notion/references/block-types.md`
- **Raw:** `[[raw/local/block-types-530379beca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Notion Block Types Reference for creating and reading all common Notion block types via the API. ## Creating blocks Use `PATCH /v1/blocks/{page_id}/children` with a `children` array. Each block follows this structure: ### Paragraph ### Headings ### Bulleted list ### Numbered list ### To-do / checkbox ### Quote ### Callout ### Code ### Toggle ### Divider ### Bookmark ### Image (external URL) ## Reading blocks When reading blocks from `GET /v1/blocks/{page_id}/children`, each block has a `type` field. Extract readable text like this: | Type | Text location | Extra fields | |------|--------------|--------------| | `paragraph` | `.paragraph.rich_text` | — | | `heading_1/2/3` |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/notion/references/block-types.md`, `local:projects/jestur/skills-capabilities/productivity/notion/references/block-types.md`, `local:projects/dev-coder/skills-capabilities/productivity/notion/references/block-types.md`, `local:projects/dev-orch/skills-capabilities/productivity/notion/references/block-types.md`, `local:projects/dev-review/skills-capabilities/productivity/notion/references/block-types.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/note-taking/obsidian/SKILL.md`
- **Raw:** `[[raw/local/skill-b3f669a8a1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: obsidian description: Read, search, create, and edit notes in the Obsidian vault. platforms: [linux, macos, windows] --- # Obsidian Vault Use this skill for filesystem-first Obsidian vault work: reading notes, listing notes, searching note files, creating notes, appending content, and adding wikilinks. ## Vault path Use a known or resolved vault path before calling file tools. The documented vault-path convention is the `OBSIDIAN_VAULT_PATH` environment variable, for example from `${HERMES_HOME:-~/.hermes}/.env`. If it is unset, use `~/Documents/Obsidian Vault`. File tools do not expand shell variables. Do not pass paths containing `$OBSIDIAN_VAULT_PATH` to `read_file`,…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/note-taking/obsidian/SKILL.md`, `local:projects/jestur/skills-capabilities/note-taking/obsidian/SKILL.md`, `local:projects/dev-coder/skills-capabilities/note-taking/obsidian/SKILL.md`, `local:projects/dev-orch/skills-capabilities/note-taking/obsidian/SKILL.md`, `local:projects/dev-review/skills-capabilities/note-taking/obsidian/SKILL.md`

### modules
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/research/dspy/references/modules.md`
- **Raw:** `[[raw/local/modules-a2a1ba76f0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DSPy Modules Complete guide to DSPy's built-in modules for language model programming. ## Module Basics DSPy modules are composable building blocks inspired by PyTorch's NN modules: - Have learnable parameters (prompts, few-shot examples) - Can be composed using Python control flow - Generalized to handle any signature - Optimizable with DSPy optimizers ### Base Module Pattern ## Core Modules ### dspy.Predict **Basic prediction module** - Makes LM calls without reasoning steps. **When to use:** - Simple, direct predictions - No reasoning steps needed - Fast responses required ### dspy.ChainOfThought **Step-by-step reasoning** - Generates rationale before answer. **Parameters:** -…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/research/dspy/references/modules.md`, `local:projects/jestur/skills-capabilities/mlops/research/dspy/references/modules.md`, `local:projects/dev-coder/skills-capabilities/mlops/research/dspy/references/modules.md`, `local:projects/dev-orch/skills-capabilities/mlops/research/dspy/references/modules.md`, `local:projects/dev-review/skills-capabilities/mlops/research/dspy/references/modules.md`

### examples
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/research/dspy/references/examples.md`
- **Raw:** `[[raw/local/examples-a617b7ed15.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DSPy Real-World Examples Practical examples of building production systems with DSPy. ## Table of Contents - RAG Systems - Agent Systems - Classification - Data Processing - Multi-Stage Pipelines ## RAG Systems ### Basic RAG ### Optimized RAG ### Multi-Hop RAG ### RAG with Reranking ## Agent Systems ### ReAct Agent ### Multi-Agent System ## Classification ### Binary Classifier ### Multi-Class Classifier ### Hierarchical Classifier ## Data Processing ### Text Summarization ### Information Extraction ### Batch Processing ## Multi-Stage Pipelines ### Document Processing Pipeline ### Quality Control Pipeline ## Production Tips ### 1. Caching for Performance ### 2. Error Handling ### 3.…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/research/dspy/references/examples.md`, `local:projects/jestur/skills-capabilities/mlops/research/dspy/references/examples.md`, `local:projects/dev-coder/skills-capabilities/mlops/research/dspy/references/examples.md`, `local:projects/dev-orch/skills-capabilities/mlops/research/dspy/references/examples.md`, `local:projects/dev-review/skills-capabilities/mlops/research/dspy/references/examples.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/research/dspy/SKILL.md`
- **Raw:** `[[raw/local/skill-a84d402bad.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: dspy description: "DSPy: declarative LM programs, auto-optimize prompts, RAG." version: 1.0.0 author: Orchestra Research license: MIT dependencies: [dspy, openai, anthropic] platforms: [linux, macos, windows] metadata: hermes: tags: [Prompt Engineering, DSPy, Declarative Programming, RAG, Agents, Prompt Optimization, LM Programming, Stanford NLP, Automatic Optimization, Modular AI] --- # DSPy: Declarative Language Model Programming ## When to Use This Skill Use DSPy when you need to: - **Build complex AI systems** with multiple components and workflows - **Program LMs declaratively** instead of manual prompt engineering - **Optimize prompts automatically** using data-driven…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/research/dspy/SKILL.md`, `local:projects/jestur/skills-capabilities/mlops/research/dspy/SKILL.md`, `local:projects/dev-coder/skills-capabilities/mlops/research/dspy/SKILL.md`, `local:projects/dev-orch/skills-capabilities/mlops/research/dspy/SKILL.md`, `local:projects/dev-review/skills-capabilities/mlops/research/dspy/SKILL.md`

### troubleshooting
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/troubleshooting.md`
- **Raw:** `[[raw/local/troubleshooting-c01460dd47.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # TouchDesigner Troubleshooting (twozero MCP) > See `references/pitfalls.md` for the comprehensive lessons-learned list. ## 1. Connection Issues ### Port 40404 not responding Check these in order: 1. Is TouchDesigner running? 1b. Quick hub health check (no JSON-RPC needed): A plain GET to the MCP URL returns instance info: Returns: `{"hub": true, "pid": ..., "instances": {"127.0.0.1_PID": {"project": "...", "tdVersion": "...", ...}}}` If this returns JSON but `instances` is empty, TD is running but twozero hasn't registered yet. 2. Is twozero installed in TD? Open TD Palette Browser > twozero should be listed. If not, install it. 3. Is MCP enabled in twozero settings? In TD, open twozero…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/troubleshooting.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/troubleshooting.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/troubleshooting.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/troubleshooting.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/troubleshooting.md`

### postfx
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/postfx.md`
- **Raw:** `[[raw/local/postfx-eef5fee961.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Post-FX Reference Bloom, CRT scanlines, chromatic aberration, and feedback glow patterns for live visual work. --- ## Bloom ### Built-in Bloom TOP TD's `bloomTOP` is the fastest path — GPU-accelerated, no shader needed. **Audio reactive bloom:** ### GLSL Bloom (More Control) For multi-pass bloom with color tinting: Then blur with `blurTOP` (size ~0.02-0.05), composite back over source with `addTOP` or `compositeTOP` in Add mode. --- ## CRT / Scanlines Pure GLSL — create a `glslTOP` and paste into its `_pixel` DAT. --- ## Chromatic Aberration Splits RGB channels and offsets them along screen axes. **Audio-reactive variant** — spike aberration on beats: --- ## Feedback Glow Warm persistent…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/postfx.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/postfx.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/postfx.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/postfx.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/postfx.md`

### mcp-tools
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/mcp-tools.md`
- **Raw:** `[[raw/local/mcp-tools-d702a7353c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # twozero MCP Tools Reference 36 tools from twozero MCP v2.774+ (April 2026). All tools accept an optional `target_instance` param for multi-TD-instance scenarios. ## Execution & Scripting ### td_execute_python Execute Python code inside TouchDesigner and return the result. Has full access to TD Python API (op, project, app, etc). Print statements and the last expression value are captured. Best for: wiring connections (inputConnectors), setting expressions (par.X.expr/mode), querying parameter names, and batch creation scripts (5+ operators). For creating 1-4 operators, prefer td_create_operator instead. | Param | Type | Required | Description | |-------|------|----------|-------------| |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/mcp-tools.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/mcp-tools.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/mcp-tools.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/mcp-tools.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/mcp-tools.md`

### glsl
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/touchdesigner-mcp/references/glsl.md`
- **Raw:** `[[raw/local/glsl-53809b0239.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # GLSL Reference ## Uniforms ### Pass Time ### Built-in Uniforms (TOP) **IMPORTANT:** `uTD2DInfos` requires input textures. For standalone shaders use `uTDOutputInfo`. ## Built-in Utility Functions ## glslTOP Docked DATs created automatically: - `glsl1_pixel` — Pixel shader - `glsl1_compute` — Compute shader - `glsl1_info` — Compile info ### Pixel Shader Template ### Compute Shader Template ### Update Shader ## glslMAT Docked DATs: - `glslmat1_vertex` — Vertex shader (param: `vdat`) - `glslmat1_pixel` — Pixel shader (param: `pdat`) - `glslmat1_info` — Compile info Note: MAT uses `vdat`/`pdat`, TOP uses `vertexdat`/`pixeldat`. ### Vertex Shader Template ## Bayer 8x8 Dither Matrix Reusable…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/touchdesigner-mcp/references/glsl.md`, `local:projects/jestur/skills-capabilities/creative/touchdesigner-mcp/references/glsl.md`, `local:projects/dev-coder/skills-capabilities/creative/touchdesigner-mcp/references/glsl.md`, `local:projects/dev-orch/skills-capabilities/creative/touchdesigner-mcp/references/glsl.md`, `local:projects/dev-review/skills-capabilities/creative/touchdesigner-mcp/references/glsl.md`

### patterns
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/pretext/references/patterns.md`
- **Raw:** `[[raw/local/patterns-e8d50e198f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pretext Patterns Copy-pasteable snippets for the most common pretext demo shapes. Each pattern is self-contained — drop into an HTML `<script type="module">` after importing from `https://esm.sh/@chenglou/pretext@0.0.6`. ## 1. Flow around an obstacle (variable-width column) The signature pretext move. Row-by-row ask "how wide is the corridor here?" and let pretext break lines accordingly. **Obstacle variants:** circles (above), rectangles (use `Math.max(0, …)` on the row-segment), multiple obstacles (sort segments and emit the wider remaining lane), animated obstacles (recompute every frame — pretext is fast enough). ## 2. Text-as-geometry game (word-bricks with collision) Use…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/pretext/references/patterns.md`, `local:projects/jestur/skills-capabilities/creative/pretext/references/patterns.md`, `local:projects/dev-coder/skills-capabilities/creative/pretext/references/patterns.md`, `local:projects/dev-orch/skills-capabilities/creative/pretext/references/patterns.md`, `local:projects/dev-review/skills-capabilities/creative/pretext/references/patterns.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/pretext/SKILL.md`
- **Raw:** `[[raw/local/skill-532570c95d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: pretext description: "Use when building creative browser demos with @chenglou/pretext — DOM-free text layout for ASCII art, typographic flow around obstacles, text-as-geometry games, kinetic typography, and text-powered generative art. Produces single-file HTML demos by default." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [creative-coding, typography, pretext, ascii-art, canvas, generative, text-layout, kinetic-typography] related_skills: [p5js, claude-design, excalidraw, architecture-diagram] --- # Pretext Creative Demos ## Overview [`@chenglou/pretext`](https://github.com/chenglou/pretext) is a 15KB zero-dependency…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/pretext/SKILL.md`

### bmw
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/popular-web-designs/templates/bmw.md`
- **Raw:** `[[raw/local/bmw-f4d82d0acd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: BMW > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere BMW's website is…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/popular-web-designs/templates/bmw.md`, `local:projects/jestur/skills-capabilities/creative/popular-web-designs/templates/bmw.md`, `local:projects/dev-coder/skills-capabilities/creative/popular-web-designs/templates/bmw.md`, `local:projects/dev-orch/skills-capabilities/creative/popular-web-designs/templates/bmw.md`, `local:projects/dev-review/skills-capabilities/creative/popular-web-designs/templates/bmw.md`

### interaction
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/p5js/references/interaction.md`
- **Raw:** `[[raw/local/interaction-6f0bbaa13c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Interaction ## Mouse Events ### Continuous State ### Event Callbacks ### Mouse Interaction Patterns **Spawn on click:** **Mouse follow with spring:** **Drag interaction:** **Mouse repulsion (particles flee cursor):** ## Keyboard Events ### State ### Event Callbacks ### Continuous Key State (Multiple Keys) ### Key Constants ## Touch Events ### Pinch Zoom ## DOM Elements ### Creating Controls ### Styling DOM Elements ## Audio Input (p5.sound) Requires `p5.sound.min.js` addon. ### Microphone Input ### Audio File Playback ### Beat Detection (Simple) ## Scroll-Driven Animation ## Responsive Events

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/p5js/references/interaction.md`, `local:projects/jestur/skills-capabilities/creative/p5js/references/interaction.md`, `local:projects/dev-coder/skills-capabilities/creative/p5js/references/interaction.md`, `local:projects/dev-orch/skills-capabilities/creative/p5js/references/interaction.md`, `local:projects/dev-review/skills-capabilities/creative/p5js/references/interaction.md`

### troubleshooting
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/p5js/references/troubleshooting.md`
- **Raw:** `[[raw/local/troubleshooting-89812ad4fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Troubleshooting ## Performance ### Step Zero — Disable FES The Friendly Error System (FES) adds massive overhead — up to 10x slowdown. Disable it in every production sketch: ### Step One — pixelDensity(1) Retina/HiDPI displays default to 2x or 3x density, multiplying pixel count by 4-9x: ### Use Math.* in Hot Loops p5's `sin()`, `cos()`, `random()`, `min()`, `max()`, `abs()` are wrapper functions with overhead. In hot loops (thousands of iterations per frame), use native `Math.*`: Use `magSq()` instead of `mag()` for distance comparisons — avoids expensive `sqrt()`. ### Diagnosis Open Chrome DevTools > Performance tab > Record while sketch runs. Common bottlenecks: 1. **FES enabled** —…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/p5js/references/troubleshooting.md`, `local:projects/jestur/skills-capabilities/creative/p5js/references/troubleshooting.md`, `local:projects/dev-coder/skills-capabilities/creative/p5js/references/troubleshooting.md`, `local:projects/dev-orch/skills-capabilities/creative/p5js/references/troubleshooting.md`, `local:projects/dev-review/skills-capabilities/creative/p5js/references/troubleshooting.md`

### webgl-and-3d
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/p5js/references/webgl-and-3d.md`
- **Raw:** `[[raw/local/webgl-and-3d-86ce498bcc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # WebGL and 3D ## WebGL Mode Setup ### Coordinate Conversion (WEBGL to P2D-like) ## 3D Primitives ### 3D Transforms ## Camera ### Default Camera ### Orbit Control ### createCamera ### Perspective and Orthographic ## Lighting ### Three-Point Lighting Setup ## Materials ### Texture ## Custom Geometry ### buildGeometry ### beginGeometry / endGeometry ### Manual Geometry (p5.Geometry) ## GLSL Shaders ### createShader (Vertex + Fragment) ### createFilterShader (Post-Processing) Simpler — only needs a fragment shader. Automatically gets the canvas as a texture. ### Common Shader Uniforms ### Shader Recipes **Chromatic Aberration:** **Vignette:** **Scanlines:** ## Framebuffers ### Multi-Pass…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/p5js/references/webgl-and-3d.md`, `local:projects/jestur/skills-capabilities/creative/p5js/references/webgl-and-3d.md`, `local:projects/dev-coder/skills-capabilities/creative/p5js/references/webgl-and-3d.md`, `local:projects/dev-orch/skills-capabilities/creative/p5js/references/webgl-and-3d.md`, `local:projects/dev-review/skills-capabilities/creative/p5js/references/webgl-and-3d.md`

### production-quality
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/manim-video/references/production-quality.md`
- **Raw:** `[[raw/local/production-quality-d9f41d3c58.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Production Quality Checklist Standards and checks for ensuring animation output is publication-ready. ## Pre-Code Checklist Before writing any Manim code: - [ ] Narration script written with visual beats marked - [ ] Scene list with purpose, duration, and layout for each - [ ] Color palette defined with meaning assignments (`PRIMARY` = main concept, etc.) - [ ] `MONO = "Menlo"` set as the font constant - [ ] Target resolution and aspect ratio decided ## Text Quality ### Overlap prevention ### Width enforcement Long text strings overflow the frame: ### Font consistency ## Spatial Layout ### The coordinate budget The visible frame is approximately 14.2 wide × 8.0 tall (default 16:9). With…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/manim-video/references/production-quality.md`, `local:projects/jestur/skills-capabilities/creative/manim-video/references/production-quality.md`, `local:projects/dev-coder/skills-capabilities/creative/manim-video/references/production-quality.md`, `local:projects/dev-orch/skills-capabilities/creative/manim-video/references/production-quality.md`, `local:projects/dev-review/skills-capabilities/creative/manim-video/references/production-quality.md`

### colors
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/excalidraw/references/colors.md`
- **Raw:** `[[raw/local/colors-4546bb6756.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Excalidraw Color Palette Use these colors consistently across diagrams. ## Primary Colors (for strokes, arrows, and accents) | Name | Hex | Use | |------|-----|-----| | Blue | `#4a9eed` | Primary actions, links, data series 1 | | Amber | `#f59e0b` | Warnings, highlights, data series 2 | | Green | `#22c55e` | Success, positive, data series 3 | | Red | `#ef4444` | Errors, negative, data series 4 | | Purple | `#8b5cf6` | Accents, special items, data series 5 | | Pink | `#ec4899` | Decorative, data series 6 | | Cyan | `#06b6d4` | Info, secondary, data series 7 | | Lime | `#84cc16` | Extra, data series 8 | ## Pastel Fills (for shape backgrounds) | Color | Hex | Good For |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/excalidraw/references/colors.md`, `local:projects/jestur/skills-capabilities/creative/excalidraw/references/colors.md`, `local:projects/dev-coder/skills-capabilities/creative/excalidraw/references/colors.md`, `local:projects/dev-orch/skills-capabilities/creative/excalidraw/references/colors.md`, `local:projects/dev-review/skills-capabilities/creative/excalidraw/references/colors.md`

### structured-content-template
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-infographic/references/structured-content-template.md`
- **Raw:** `[[raw/local/structured-content-template-d979b8d4fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Structured Content Template Template for generating structured infographic content that informs the visual designer. ## Purpose This document bridges content analysis and visual design: - Transforms source material into designer-ready format - Organizes learning objectives into visual sections - Preserves all source data verbatim - Separates content from design instructions ## Instructional Design Process ### Phase 1: High-Level Outline 1. **Title**: Capture the essence in a compelling headline 2. **Overview**: Brief description (1-2 sentences) 3. **Learning Objectives**: List what the viewer will understand ### Phase 2: Section Development For each learning objective: 1. **Key Concept**:…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-infographic/references/structured-content-template.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-infographic/references/structured-content-template.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-infographic/references/structured-content-template.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-infographic/references/structured-content-template.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-infographic/references/structured-content-template.md`

### warm
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-comic/references/tones/warm.md`
- **Raw:** `[[raw/local/warm-a80705960f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # warm 温馨基调 - Nostalgic, personal, comforting ## Overview Warm, inviting atmosphere for personal stories and nostalgic content. Creates emotional connection through cozy aesthetics and comforting visuals. ## Mood Characteristics - Nostalgic feeling - Personal, intimate atmosphere - Comforting and healing - Memory and reflection - Gentle emotional warmth ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | Slightly reduced | | Contrast | Softer | | Temperature | Warm shift (+15%) | | Brightness | Soft, golden | ## Color Temperature Shift palette toward warm tones: | Original | Warm Shift | |----------|-----------| | Cool blue…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-comic/references/tones/warm.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-comic/references/tones/warm.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-comic/references/tones/warm.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-comic/references/tones/warm.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-comic/references/tones/warm.md`

### analysis-framework
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-comic/references/analysis-framework.md`
- **Raw:** `[[raw/local/analysis-framework-7917f3552f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Comic Content Analysis Framework Deep analysis framework for transforming source content into effective visual storytelling. ## Purpose Before creating a comic, thoroughly analyze the source material to: - Identify the target audience and their needs - Determine what value the comic will deliver - Extract narrative potential for visual storytelling - Plan character arcs and key moments ## Analysis Dimensions ### 1. Core Content (Understanding "What") **Central Message** - What is the single most important idea readers should take away? - Can you express it in one sentence? **Key Concepts** - What are the essential concepts readers must understand? - How should these concepts be…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-comic/references/analysis-framework.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-comic/references/analysis-framework.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-comic/references/analysis-framework.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-comic/references/analysis-framework.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-comic/references/analysis-framework.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/autonomous-ai-agents/opencode/SKILL.md`
- **Raw:** `[[raw/local/skill-afb3ea1f1b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: opencode description: "Delegate coding to OpenCode CLI (features, PR review)." version: 1.2.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [Coding-Agent, OpenCode, Autonomous, Refactoring, Code-Review] related_skills: [claude-code, codex, hermes-agent] --- # OpenCode CLI Use [OpenCode](https://opencode.ai) as an autonomous coding worker orchestrated by Hermes terminal/process tools. OpenCode is a provider-agnostic, open-source AI coding agent with a TUI and CLI. ## When to Use - User explicitly asks to use OpenCode - You want an external coding agent to implement/refactor/review code - You need long-running coding sessions with…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/autonomous-ai-agents/opencode/SKILL.md`, `local:projects/jestur/skills-capabilities/autonomous-ai-agents/opencode/SKILL.md`, `local:projects/dev-coder/skills-capabilities/autonomous-ai-agents/opencode/SKILL.md`, `local:projects/dev-orch/skills-capabilities/autonomous-ai-agents/opencode/SKILL.md`, `local:projects/dev-review/skills-capabilities/autonomous-ai-agents/opencode/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/autonomous-ai-agents/claude-code/SKILL.md`
- **Raw:** `[[raw/local/skill-4d195cf896.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: claude-code description: "Delegate coding to Claude Code CLI (features, PRs)." version: 2.2.0 author: Hermes Agent + Teknium license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [Coding-Agent, Claude, Anthropic, Code-Review, Refactoring, PTY, Automation] related_skills: [codex, hermes-agent, opencode] --- # Claude Code — Hermes Orchestration Guide Delegate coding tasks to [Claude Code](https://code.claude.com/docs/en/cli-reference) (Anthropic's autonomous coding agent CLI) via the Hermes terminal. Claude Code v2.x can read files, write code, run shell commands, spawn subagents, and manage git workflows autonomously. ## Prerequisites - **Install:** `npm install…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/autonomous-ai-agents/claude-code/SKILL.md`, `local:projects/jestur/skills-capabilities/autonomous-ai-agents/claude-code/SKILL.md`, `local:projects/dev-coder/skills-capabilities/autonomous-ai-agents/claude-code/SKILL.md`, `local:projects/dev-orch/skills-capabilities/autonomous-ai-agents/claude-code/SKILL.md`, `local:projects/dev-review/skills-capabilities/autonomous-ai-agents/claude-code/SKILL.md`

### 1519062011978322070-Remember
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519062011978322070-Remember.txt`
- **Raw:** `[[raw/discord/1519062011978322070-remember-3846938777.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Remember' in forum #plugins-skills-and-skins # thread_id=1519062011978322070 forum_id=1485392832154832906 # Started 2026-06-23T20:05:07.852124+00:00 [2026-06-23T19:30:06.463000+00:00] flash_speed3412 (id=1519062011978322070) **Production-ready local-first memory layer for AI agents.** Remember gives your agent persistent memory that survives across sessions. Hybrid search (BM25 + vector), temporal validity windows, entity graphs, and memory decay — all in a single SQLite file. No cloud. No API keys. No telemetry. ------------------------------------------ **Found a bug? Have an idea? Open an issue or PR.** If Remember saved your project from the dreaded "wait, what was I working…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519062011978322070-Remember.txt`

### 1517239469609058466-Brutal-Memory---Hermes-Agent-state.db-viewer
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1517239469609058466-Brutal-Memory---Hermes-Agent-state.db-viewer.txt`
- **Raw:** `[[raw/discord/1517239469609058466-brutal-memory---hermes-agent-state.db-viewer-19b9017f62.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Brutal Memory — Hermes Agent state.db viewer' in forum #plugins-skills-and-skins # thread_id=1517239469609058466 forum_id=1485392832154832906 # Started 2026-06-18T20:28:21.813453+00:00 [2026-06-18T18:47:58.501000+00:00] brutalbuild (id=1517239469609058466) Brutal Memory — Hermes Agent state.db viewer A fully client-side web app for browsing all your Hermes Agent conversations. No backend, no uploads — just drag your state.db file into the browser and explore your session history. Features: - Drop & browse — drag a file, instantly see all sessions - Filter by source (tui, telegram, cron, discord, etc.) - Search by title with 300ms debounce - Sort by newest, oldest, most messages,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1517239469609058466-Brutal-Memory---Hermes-Agent-state.db-viewer.txt`

### 1515595298708258858-rhizome
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1515595298708258858-rhizome.txt`
- **Raw:** `[[raw/discord/1515595298708258858-rhizome-ea429d4f21.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'rhizome' in forum #plugins-skills-and-skins # thread_id=1515595298708258858 forum_id=1485392832154832906 # Started 2026-06-14T09:34:39.969856+00:00 [2026-06-14T05:54:37.611000+00:00] tuck2g (id=1515595298708258858) A zero-waste knowledge compiler for multi-agent wiki systems. [attachment] logo.png https://cdn.discordapp.com/attachments/1515595298708258858/1515595299043676221/logo.png?ex=6a2f939d&is=6a2e421d&hm=0a49f650e5e7bebe3a4b2bba2c156ed1bfbaa1cf64683817ccafd4e935b10f12& [2026-06-14T05:54:53.864000+00:00] tuck2g (id=1515595366878285875) https://github.com/knispo/rhizome A local-first wiki that compiles your notes into time-aware memory for AI agents. Karpathy inspired. The…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1515595298708258858-rhizome.txt`

### 1513868076674842644-Hermes-Obsidian-Memory-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513868076674842644-Hermes-Obsidian-Memory-Plugin.txt`
- **Raw:** `[[raw/discord/1513868076674842644-hermes-obsidian-memory-plugin-1a9164a97f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Obsidian Memory Plugin' in forum #plugins-skills-and-skins # thread_id=1513868076674842644 forum_id=1485392832154832906 # Started 2026-06-09T14:50:01.984066+00:00 [2026-06-09T11:31:15.788000+00:00] kyssta69 (id=1513868076674842644) Browse, search, and edit your Obsidian vault notes from the Hermes dashboard. Multi-vault support, force-directed graph visualization, inline note editing, wikilink navigation. **Install**: **Features**: - Auto-discovers all Obsidian vaults on your system - Force-directed graph with drag, zoom, curved edges - Full markdown rendering (code blocks, tables, callouts, checkboxes) - Click [[wikilinks]] to navigate between notes - Edit notes directly…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513868076674842644-Hermes-Obsidian-Memory-Plugin.txt`

### 1512000047380693032-I-created-a-obsidian-memory-plugin-for-termux-because-there-wasnt-any.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512000047380693032-I-created-a-obsidian-memory-plugin-for-termux-because-there-wasnt-any..txt`
- **Raw:** `[[raw/discord/1512000047380693032-i-created-a-obsidian-memory-plugin-for-termux-because-there-wasnt-any.-5f8d0d9178.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'I created a obsidian memory plugin for termux because there wasnt any.' in forum #plugins-skills-and-skins # thread_id=1512000047380693032 forum_id=1485392832154832906 # Started 2026-06-04T09:56:57.587932+00:00 [2026-06-04T07:48:22.898000+00:00] txrao (id=1512000047380693032) I Was SEARCHING FOR A MEMORY PLUGIN AND I COULDNT FIND ONE FOR OBSIDIAN so i made my own. It continues to the onsidian directly on your phone so u see all the files in graph mode. Looks pretty cool to. Great memory plugin overall, easy to make/i made it with hermes😭🙏 so ye install my plugin if your a termux users looking for a obsidian memory plugin…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512000047380693032-I-created-a-obsidian-memory-plugin-for-termux-because-there-wasnt-any..txt`

### 1509794019729735814-Sibyl-Labs--Graph-Memory-Plugin-for-Hermes--HACKATHON-INFO-COMING-SOON
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509794019729735814-Sibyl-Labs--Graph-Memory-Plugin-for-Hermes--HACKATHON-INFO-COMING-SOON.txt`
- **Raw:** `[[raw/discord/1509794019729735814-sibyl-labs--graph-memory-plugin-for-hermes--hackathon-info-coming-soon-73154974f4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Sibyl Labs: Graph-Memory Plugin for Hermes (HACKATHON INFO COMING SOON)' in forum #plugins-skills-and-skins # thread_id=1509794019729735814 forum_id=1485392832154832906 # Started 2026-05-29T09:54:13.543614+00:00 [2026-05-29T05:42:24.920000+00:00] dr.kojipup (id=1509794019729735814) Hey guys! We've built a graph-structured memory layer for hermes agents. What it does: — Reduces token consumption via auto-compression — Improves recall accuracy across long sessions — on LongMemEval Oracle at 95.6% — Five-tier schema: HOT / WARM / COLD / REFERENCE / ARCHIVE — Local-first, zero vectors, zero infra cost — Multi-tenant namespace isolation — no context bleed between projects We are…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509794019729735814-Sibyl-Labs--Graph-Memory-Plugin-for-Hermes--HACKATHON-INFO-COMING-SOON.txt`

### 1506238104569253909-Git-as-Memory---store-agent-memory-in-Git-refs--no-external-DB
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506238104569253909-Git-as-Memory---store-agent-memory-in-Git-refs--no-external-DB.txt`
- **Raw:** `[[raw/discord/1506238104569253909-git-as-memory---store-agent-memory-in-git-refs--no-external-db-2991d6d2e3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🧠 Git as Memory — store agent memory in Git refs, no external DB' in forum #plugins-skills-and-skins # thread_id=1506238104569253909 forum_id=1485392832154832906 # Started 2026-05-19T15:00:56.534310+00:00 [2026-05-19T10:12:28.680000+00:00] femtowin (id=1506238104569253909) Tired of memory plugins that need a separate service or DB? Git as Memory stores everything directly in your repo's Git object store — no external dependencies, no cloud, no sqlite. Works with Hermes out of the box: npx skills add https://github.com/femto/skills --skill git-as-memory Each memory entry lives under refs/git-as-memory/memory/v1 — you can inspect, diff, and audit with standard Git tools: git log…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506238104569253909-Git-as-Memory---store-agent-memory-in-Git-refs--no-external-DB.txt`

### 1501246103058649088-Memory-Hive-gives-AI-workers-durable-context--Total-Recall.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1501246103058649088-Memory-Hive-gives-AI-workers-durable-context--Total-Recall..txt`
- **Raw:** `[[raw/discord/1501246103058649088-memory-hive-gives-ai-workers-durable-context--total-recall.-70a790ab0b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Memory Hive gives AI workers durable context, Total Recall.' in forum #plugins-skills-and-skins # thread_id=1501246103058649088 forum_id=1485392832154832906 # Started 2026-05-10T19:52:04.493292+00:00 [2026-05-05T15:36:02.773000+00:00] tourettesgaming (id=1501246103058649088) https://github.com/TJCurnutte/memory-hive Agents shouldn’t wake up blank every run, or run blindly into the next prompt. Memory Hive gives AI workers durable context: - private agent memory - shared lessons - curated truth - cleaner handoffs - fewer repeated mistakes Read. Work. Write back. That simple loop turns scattered agent runs into a compounding operating system.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1501246103058649088-Memory-Hive-gives-AI-workers-durable-context--Total-Recall..txt`

### 1498945272632315974-Reverie-Core--Agentic-cognition-layer-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1498945272632315974-Reverie-Core--Agentic-cognition-layer-for-Hermes.txt`
- **Raw:** `[[raw/discord/1498945272632315974-reverie-core--agentic-cognition-layer-for-hermes-c2fed8eb75.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Reverie Core: Agentic cognition layer for Hermes' in forum #plugins-skills-and-skins # thread_id=1498945272632315974 forum_id=1485392832154832906 # Started 2026-05-10T19:52:11.100098+00:00 [2026-04-29T07:13:22.052000+00:00] hackafterdark (id=1498945272632315974) I’ve been iterating on a local-first memory/cognition layer for Hermes and finally pushed it to public visibility. Unlike passive document stores, Reverie Core treats memory as a dynamic, self-pruning knowledge graph. It’s built for developers who want a predictable, tunable memory layer with deep observability. **Why it’s different:** **Hybrid Retrieval:** Combined high-speed sqlite-vec similarity search with…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1498945272632315974-Reverie-Core--Agentic-cognition-layer-for-Hermes.txt`

### 1494625406459052095-PR--8979-feat-memory---add-MemOS-memory-provider-plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1494625406459052095-PR--8979-feat-memory---add-MemOS-memory-provider-plugin.txt`
- **Raw:** `[[raw/discord/1494625406459052095-pr--8979-feat-memory---add-memos-memory-provider-plugin-e009ef9cce.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'PR #8979 feat(memory): add MemOS memory provider plugin' in forum #plugins-skills-and-skins # thread_id=1494625406459052095 forum_id=1485392832154832906 # Started 2026-05-10T19:52:26.024226+00:00 [2026-04-17T09:07:45.697000+00:00] richie.hong (id=1494625406459052095) We have some thoughts about Hermes's memory improvement, and we already submited a lite and sweet PR for a while, we'll appreciate it if you have time to check it out 🤠 ## What we provides: * Server-side memory extraction * Semantic search * Preference management * Multi-agent memory isolation capabilities By integrating the MemOS Platform, Hermes can maintain persistent, cross-session knowledge and personalize user…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1494625406459052095-PR--8979-feat-memory---add-MemOS-memory-provider-plugin.txt`

### 1494747832802873487-MindBank----MCP-relationship-memories
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1494747832802873487-MindBank----MCP-relationship-memories.txt`
- **Raw:** `[[raw/discord/1494747832802873487-mindbank----mcp-relationship-memories-dc0d695125.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'MindBank - MCP relationship memories' in forum #plugins-skills-and-skins # thread_id=1494747832802873487 forum_id=1485392832154832906 # Started 2026-05-10T19:52:25.245550+00:00 [2026-04-17T17:14:14.412000+00:00] .omgg (id=1494747832802873487) https://github.com/spfcraze/MindBank MindBank gives your AI assistant a permanent, searchable, relationship-aware memory that persists across conversations. Instead of forgetting everything between sessions, your agent remembers decisions, configs, preferences, and project knowledge — organized as a graph, not a flat text blob. ┌─────────────────────────────────────────┐ │ Your AI Agent │ │ (Hermes, Claude, custom, any) │…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1494747832802873487-MindBank----MCP-relationship-memories.txt`

### 1493596015964717127-Yet-Another-Wiki-Integration
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1493596015964717127-Yet-Another-Wiki-Integration.txt`
- **Raw:** `[[raw/discord/1493596015964717127-yet-another-wiki-integration-2e75ce8413.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Yet Another Wiki Integration' in forum #plugins-skills-and-skins # thread_id=1493596015964717127 forum_id=1485392832154832906 # Started 2026-05-10T19:52:31.883156+00:00 [2026-04-14T12:57:19.878000+00:00] labhund (id=1493596015964717127) Comprehensive skill package and MCP server for dedicated research workflows! https://github.com/Labhund/lacuna-wiki Turn your hermes agent into a dedicated research assistant and grow your personal knowledge base! [embed] GitHub - Labhund/lacuna-wiki: Give your agent a knowledge graph tha... https://github.com/Labhund/lacuna-wiki [2026-04-14T13:01:23.698000+00:00] labhund (id=1493597038619656282) The structured multi step skills take out the guess…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1493596015964717127-Yet-Another-Wiki-Integration.txt`

### 1491875809575702659-Shiba-Memory---Native-Hermes-Memory-Provider-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1491875809575702659-Shiba-Memory---Native-Hermes-Memory-Provider-Plugin.txt`
- **Raw:** `[[raw/discord/1491875809575702659-shiba-memory---native-hermes-memory-provider-plugin-f86be1a5fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Shiba Memory — Native Hermes Memory Provider Plugin' in forum #plugins-skills-and-skins # thread_id=1491875809575702659 forum_id=1485392832154832906 # Started 2026-05-10T19:52:55.100926+00:00 [2026-04-09T19:01:50.715000+00:00] bostonsportstech82 (id=1491875809575702659) Hey everyone! Just open sourced my first project. Shiba Memory is a persistent, self-improving memory layer for AI agents. It ships with a native Hermes memory provider plugin out of the box. What Hermes gets: - shiba_recall / shiba_remember / shiba_forget tools available to the LLM - Auto memory on every conversation turn - Relevant memories prefetched before each response - Session summaries extracted when…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1491875809575702659-Shiba-Memory---Native-Hermes-Memory-Provider-Plugin.txt`

### 1491974237538353252-LLM-Wiki-Backend
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1491974237538353252-LLM-Wiki-Backend.txt`
- **Raw:** `[[raw/discord/1491974237538353252-llm-wiki-backend-6e08d2504d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'LLM-Wiki Backend' in forum #plugins-skills-and-skins # thread_id=1491974237538353252 forum_id=1485392832154832906 # Started 2026-05-10T19:52:39.070554+00:00 [2026-04-10T01:32:57.770000+00:00] labhund (id=1491974237538353252) Put together a little treat for anyone who has been enjoying the new llm-wiki skill! PSA: I have taken the learnings from llm-wiki and turned it into a comprehensive and focused package, check out Lacuna! Lacuna: https://github.com/Labhund/lacuna-wiki OLD REPOSITORY (DEPRECATED): https://github.com/Labhund/llm-wiki [embed] GitHub - Labhund/lacuna-wiki: Give your agent a knowledge graph tha... https://github.com/Labhund/lacuna-wiki [embed] GitHub -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1491974237538353252-LLM-Wiki-Backend.txt`

### 1491688455745306755-Mazemaker-feat.-Neural-Memory
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1491688455745306755-Mazemaker-feat.-Neural-Memory.txt`
- **Raw:** `[[raw/discord/1491688455745306755-mazemaker-feat.-neural-memory-1e0bf1cfd5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Mazemaker feat. Neural Memory' in forum #plugins-skills-and-skins # thread_id=1491688455745306755 forum_id=1485392832154832906 # Started 2026-05-10T19:52:42.064097+00:00 [2026-04-09T06:37:22.081000+00:00] alcatr4z (id=1491688455745306755) A *brain-inspired* memory system for AI agents. Semantic memory system with knowledge graph, spreading activation, embedding-based recall, **autonomous dream consolidation**, and **C++ LSTM+kNN pattern learning** for the Hermes Agent, and any other /MCP compitible harnes/ide/etc. ## Features (From first proof of concept builds - more below) - **Semantic Memory Storage**: Store memories with automatic embedding generation (`BAAI/bge-m3`, 1024d,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1491688455745306755-Mazemaker-feat.-Neural-Memory.txt`

### 1489766351466790983-New-Hermes-Memory-Plugin--Observational-Memory
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1489766351466790983-New-Hermes-Memory-Plugin--Observational-Memory.txt`
- **Raw:** `[[raw/discord/1489766351466790983-new-hermes-memory-plugin--observational-memory-6c2c338242.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'New Hermes Memory Plugin: Observational Memory' in forum #plugins-skills-and-skins # thread_id=1489766351466790983 forum_id=1485392832154832906 # Started 2026-05-10T19:52:48.711289+00:00 [2026-04-03T23:19:36.710000+00:00] intertwiner (id=1489766351466790983) Hey all — I just published a standalone Hermes memory-provider plugin for **Observational Memory**: https://github.com/intertwine/hermes-observational-memory **What it is:** - A local-first memory backend for Hermes that keeps memory in plain markdown - Can share the same memory store with Claude Code and Codex - Gives Hermes compact startup context, local search, explicit remember tools, and optional writeback into the shared…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1489766351466790983-New-Hermes-Memory-Plugin--Observational-Memory.txt`

### 1519061776581394513-Remember
- **Source:** `discord-archive:archives/community-projects-showcase/1519061776581394513-Remember.txt`
- **Raw:** `[[raw/discord/1519061776581394513-remember-ba1c5bc156.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Remember' in forum #community-projects-showcase # thread_id=1519061776581394513 forum_id=1316137596535177246 # Started 2026-06-23T20:00:45.527046+00:00 [2026-06-23T19:29:10.340000+00:00] flash_speed3412 (id=1519061776581394513) **Production-ready local-first memory layer for AI agents.** Remember gives your agent persistent memory that survives across sessions. Hybrid search (BM25 + vector), temporal validity windows, entity graphs, and memory decay — all in a single SQLite file. No cloud. No API keys. No telemetry. ------------------------------------------ **Found a bug? Have an idea? Open an issue or PR.** If Remember saved your project from the dreaded "wait, what was I…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1519061776581394513-Remember.txt`

### 1519099133338714202-agent-memory-skill-----strukturiertes-Memory-für-Hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1519099133338714202-agent-memory-skill-----strukturiertes-Memory-für-Hermes.txt`
- **Raw:** `[[raw/discord/1519099133338714202-agent-memory-skill-----strukturiertes-memory-f-r-hermes-e3039bd32c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '**agent-memory-skill** — strukturiertes Memory für Hermes' in forum #community-projects-showcase # thread_id=1519099133338714202 forum_id=1316137596535177246 # Started 2026-06-24T03:23:59.412783+00:00 [2026-06-23T21:57:36.885000+00:00] xperryx. (id=1519099133338714202) MEMORY.md und USER.md sind flache Listen. Kein Trust-Level, keine TTL per Typ, `write_approval` ist globales on/off. Ich hab das gelöst. **5 Authority Lanes** mit eigener TTL, Confidence und Source-Policy: - `identity` → permanent, confidence ≥ 0.9 - `preference` → 14d TTL - `evidence` → 60d TTL - `authorization` → 90d TTL, **nur observation** — Conversation-Messages werden silent rejected. Strukturell, kein Regex.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1519099133338714202-agent-memory-skill-----strukturiertes-Memory-für-Hermes.txt`

### 1518232813747306516-Does-recursively-synthesizing-statements-mimic-cognitive-abstraction
- **Source:** `discord-archive:archives/community-projects-showcase/1518232813747306516-Does-recursively-synthesizing-statements-mimic-cognitive-abstraction.txt`
- **Raw:** `[[raw/discord/1518232813747306516-does-recursively-synthesizing-statements-mimic-cognitive-abstraction-7fe46f319d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Does recursively synthesizing statements mimic cognitive abstraction?' in forum #community-projects-showcase # thread_id=1518232813747306516 forum_id=1316137596535177246 # Started 2026-06-21T14:05:28.409245+00:00 [2026-06-21T12:35:10.199000+00:00] lea_fia (id=1518232813747306516) A very primitive and simplistic experiment that examined whether a recursive system that combines the results of dialectics looks like abstraction. Qwen3:8B was used because tokens are expensive and I wanted to run locally on my potato Qwen was given a philosophical question and asked to derive a thesis. Then called again with this thesis to derive an anti-thesis. And finally once more to derive a…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1518232813747306516-Does-recursively-synthesizing-statements-mimic-cognitive-abstraction.txt`

### 1517055527849300078-Memory-Is-for-Decisions.-Markdown-Is-for-Knowledge.
- **Source:** `discord-archive:archives/community-projects-showcase/1517055527849300078-Memory-Is-for-Decisions.-Markdown-Is-for-Knowledge..txt`
- **Raw:** `[[raw/discord/1517055527849300078-memory-is-for-decisions.-markdown-is-for-knowledge.-4762426679.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Memory Is for Decisions. Markdown Is for Knowledge.' in forum #community-projects-showcase # thread_id=1517055527849300078 forum_id=1316137596535177246 # Started 2026-06-18T10:18:11.079810+00:00 [2026-06-18T06:37:03.368000+00:00] johnsonbuilds (id=1517055527849300078) One small workflow change improved my AI agent dramatically. Instead of stuffing everything into memory, I store research in Markdown files: 📁 /knowledge/ * quick-ref.md (index) * growth_tactics.md * developer_resources.md The agent only needs the index file to discover relevant knowledge. Benefits: ✅ Human-readable ✅ Version controllable ✅ Cross-agent compatible ✅ No vector database required My current rule: Memory…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1517055527849300078-Memory-Is-for-Decisions.-Markdown-Is-for-Knowledge..txt`

### 1515801250749349999-Hermes-Open-Knowledge-Format-memory
- **Source:** `discord-archive:archives/community-projects-showcase/1515801250749349999-Hermes-Open-Knowledge-Format-memory.txt`
- **Raw:** `[[raw/discord/1515801250749349999-hermes-open-knowledge-format-memory-9838bf9fc4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Open Knowledge Format memory' in forum #community-projects-showcase # thread_id=1515801250749349999 forum_id=1316137596535177246 # Started 2026-06-15T04:04:05.357824+00:00 [2026-06-14T19:33:00.404000+00:00] wojtek.majnkraft (id=1515801250749349999) I integrated Google's Open Knowledge Format (OKF) into Hermes memory — basically it's like having Obsidian natively inside your agent. Every decision, tool call, and plan step gets stored as plain markdown files on disk. You can literally cat the file and read what your agent "remembered." Why it's useful: • Memory persists across sessions (no more "what were we doing?" after restart) • Knowledge graph from markdown links — no…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1515801250749349999-Hermes-Open-Knowledge-Format-memory.txt`

### 1515112302611923175-3-tier-memory-system-that-knows-how-to-forget--ChromaDB--Obsidian--and-SQLite
- **Source:** `discord-archive:archives/community-projects-showcase/1515112302611923175-3-tier-memory-system-that-knows-how-to-forget--ChromaDB--Obsidian--and-SQLite.txt`
- **Raw:** `[[raw/discord/1515112302611923175-3-tier-memory-system-that-knows-how-to-forget--chromadb--obsidian--and-sqlite-35e7a30a81.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '3 tier memory system that knows how to forget: ChromaDB, Obsidian, and SQLite' in forum #community-projects-showcase # thread_id=1515112302611923175 forum_id=1316137596535177246 # Started 2026-06-13T03:31:52.443990+00:00 [2026-06-12T21:55:22.368000+00:00] thedavidmurray (id=1515112302611923175) Agent-agnostic persistent memory for AI agents. One file, three real tiers, one-line install. https://github.com/edgeless-ai/edgeless-memory The key here is it forgets. There's a decay mechanism (which can be disabled) that prunes unused memories Energy / decay — every memory cools 5%/day (configurable) while unused and reheats when accessed. Stale junk ages out of search results on its…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1515112302611923175-3-tier-memory-system-that-knows-how-to-forget--ChromaDB--Obsidian--and-SQLite.txt`

### 1515564873801666580-rhizome---A-zero-waste-knowledge-compiler-for-multi-agent-wiki-systems.
- **Source:** `discord-archive:archives/community-projects-showcase/1515564873801666580-rhizome---A-zero-waste-knowledge-compiler-for-multi-agent-wiki-systems..txt`
- **Raw:** `[[raw/discord/1515564873801666580-rhizome---a-zero-waste-knowledge-compiler-for-multi-agent-wiki-systems.-9d25ed94b9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'rhizome - A zero-waste knowledge compiler for multi-agent wiki systems.' in forum #community-projects-showcase # thread_id=1515564873801666580 forum_id=1316137596535177246 # Started 2026-06-14T09:30:25.909581+00:00 [2026-06-14T03:53:43.748000+00:00] tuck2g (id=1515564873801666580) [attachment] logo.png https://cdn.discordapp.com/attachments/1515564873801666580/1515564874057650226/logo.png?ex=6a2f7747&is=6a2e25c7&hm=b2479bece3309c880b0e51a54f00f19de6019b69ff9c0eb5d40fc1684df1971d& [2026-06-14T03:54:24.983000+00:00] tuck2g (id=1515565046753788004) https://github.com/knispo/rhizome A local-first wiki that compiles your notes into time-aware memory for AI agents. Karpathy inspired.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1515564873801666580-rhizome---A-zero-waste-knowledge-compiler-for-multi-agent-wiki-systems..txt`

### 1512967774782361621-context-mcp---Persistent-memory---codebase-knowledge-graph-for-AI-coding-assistants
- **Source:** `discord-archive:archives/community-projects-showcase/1512967774782361621-context-mcp---Persistent-memory---codebase-knowledge-graph-for-AI-coding-assistants.txt`
- **Raw:** `[[raw/discord/1512967774782361621-context-mcp---persistent-memory---codebase-knowledge-graph-for-ai-coding-assistants-7220e17924.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🧠 context-mcp — Persistent memory + codebase knowledge graph for AI coding assistants' in forum #community-projects-showcase # thread_id=1512967774782361621 forum_id=1316137596535177246 # Started 2026-06-07T03:40:46.624530+00:00 [2026-06-06T23:53:47.090000+00:00] vibhasdutta (id=1512967774782361621) The problem: Every AI conversation starts from zero. The assistant re-reads files it already read, re-discovers architecture it already understood, re-derives decisions already made. And if you switch tools — fix something in Claude Code, open Cursor — it knows nothing. What I built: A single MCP server that gives any AI assistant persistent memory and a structural knowledge graph of…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1512967774782361621-context-mcp---Persistent-memory---codebase-knowledge-graph-for-AI-coding-assistants.txt`

### 1510939660266901504-Hindsight-Feedbacks-Request--Hindsight-Maintainer-here
- **Source:** `discord-archive:archives/community-projects-showcase/1510939660266901504-Hindsight-Feedbacks-Request--Hindsight-Maintainer-here.txt`
- **Raw:** `[[raw/discord/1510939660266901504-hindsight-feedbacks-request--hindsight-maintainer-here-4f6e7c2341.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hindsight Feedbacks Request (Hindsight Maintainer here)' in forum #community-projects-showcase # thread_id=1510939660266901504 forum_id=1316137596535177246 # Started 2026-06-01T11:29:43.771009+00:00 [2026-06-01T09:34:46.909000+00:00] nicoloboschi (id=1510939660266901504) I'm the co-creator of Hindsight and I really appreciate the love Hermes users are sending to us. Although, as any piece of software, there are things that could be done better. Please provide any valuable feedback here so I can triage/help/fix whatever comes up, being a native Hindsight issue or about the Hermes code integration Please include your setup and some concrete example of the problem you're seeing. Also…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1510939660266901504-Hindsight-Feedbacks-Request--Hindsight-Maintainer-here.txt`

### 1510170663329988738-Multi-Scope-Local-Memory--a-local-first-agent-memory-solution
- **Source:** `discord-archive:archives/community-projects-showcase/1510170663329988738-Multi-Scope-Local-Memory--a-local-first-agent-memory-solution.txt`
- **Raw:** `[[raw/discord/1510170663329988738-multi-scope-local-memory--a-local-first-agent-memory-solution-1191ea63df.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Multi Scope Local Memory, a local first agent memory solution' in forum #community-projects-showcase # thread_id=1510170663329988738 forum_id=1316137596535177246 # Started 2026-05-30T08:25:57.591354+00:00 [2026-05-30T06:39:03.752000+00:00] kai.xu (id=1510170663329988738) MSLM — Multi-Scope Local Memory for Hermes Agent Ever spent an afternoon teaching your Hermes Agent your entire tech stack, only to have it forget everything the next session? Same. MSLM builds on the SuperLocalMemory engine with one key addition: three-layer scope — personal / shared / global. Your agent keeps private memories (API keys, preferences) separate from shared team knowledge (project conventions,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1510170663329988738-Multi-Scope-Local-Memory--a-local-first-agent-memory-solution.txt`

### 1505235887389282345-SIBYL--Persistent-Memory-for-Hermes--95.6--on-LongMemEval
- **Source:** `discord-archive:archives/community-projects-showcase/1505235887389282345-SIBYL--Persistent-Memory-for-Hermes--95.6--on-LongMemEval.txt`
- **Raw:** `[[raw/discord/1505235887389282345-sibyl--persistent-memory-for-hermes--95.6--on-longmemeval-0b181863ae.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'SIBYL: Persistent Memory for Hermes: 95.6% on LongMemEval' in forum #community-projects-showcase # thread_id=1505235887389282345 forum_id=1316137596535177246 # Started 2026-05-16T19:02:13.800432+00:00 [2026-05-16T15:50:01.484000+00:00] dr.kojipup (id=1505235887389282345) we've been making remarkable progress on what building continuity across sessions should look like, while maintaining privacy for the user. most memory approaches today reach for vector databases and cloud retrieval pipelines. they're powerful, but embedding API cost that scales with usage. recall model trades precision for fuzziness, this becomes especially apparent as memory starts to degrade across long…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1505235887389282345-SIBYL--Persistent-Memory-for-Hermes--95.6--on-LongMemEval.txt`

### 1504243723091841155-Agent-memory-skill---structured-memory-for-Hermes--no-more-flat-lists
- **Source:** `discord-archive:archives/community-projects-showcase/1504243723091841155-Agent-memory-skill---structured-memory-for-Hermes--no-more-flat-lists.txt`
- **Raw:** `[[raw/discord/1504243723091841155-agent-memory-skill---structured-memory-for-hermes--no-more-flat-lists-536d0c8230.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Agent-memory-skill — structured memory for Hermes (no more flat lists)' in forum #community-projects-showcase # thread_id=1504243723091841155 forum_id=1316137596535177246 # Started 2026-05-14T02:55:25.555935+00:00 [2026-05-13T22:07:31.082000+00:00] xperryx. (id=1504243723091841155) Hi — if Hermes' default memory bugs you the same way it bugged me (flat list, no hierarchy, no protection against memory floods), here's something I built that fixes it: agent-memory-skill. What it does better: Authorization lane rejects facts from chat. Means: "you may delete /etc" as a prompt-injection in a message? Silently ignored. Only observation sources get through. Privilege escalation via…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1504243723091841155-Agent-memory-skill---structured-memory-for-Hermes--no-more-flat-lists.txt`

### 1503085649325195374-Introducing-Recall--a-local--auditable-memory-layer-for-Hermes-Agent
- **Source:** `discord-archive:archives/community-projects-showcase/1503085649325195374-Introducing-Recall--a-local--auditable-memory-layer-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1503085649325195374-introducing-recall--a-local--auditable-memory-layer-for-hermes-agent-85ab86aec7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Introducing Recall: a local, auditable memory layer for Hermes Agent' in forum #community-projects-showcase # thread_id=1503085649325195374 forum_id=1316137596535177246 # Started 2026-05-10T19:49:12.969257+00:00 [2026-05-10T17:25:44.780000+00:00] nour_h (id=1503085649325195374) I’ve been building and dogfooding **Recall**, a Hermes-native memory provider designed for people who want memory that is useful, inspectable, and safe — not a black box. Recall adds a local SQLite-backed memory archive around Hermes with a few principles: - **Built-in memory stays authoritative** - `MEMORY.md` / `USER.md` remain the trusted source. - Recall is lower-trust archive evidence unless explicitly…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1503085649325195374-Introducing-Recall--a-local--auditable-memory-layer-for-Hermes-Agent.txt`

### 1500722439288520794-Mnemosyne-Dashboard
- **Source:** `discord-archive:archives/community-projects-showcase/1500722439288520794-Mnemosyne-Dashboard.txt`
- **Raw:** `[[raw/discord/1500722439288520794-mnemosyne-dashboard-e41cfb7017.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Mnemosyne Dashboard' in forum #community-projects-showcase # thread_id=1500722439288520794 forum_id=1316137596535177246 # Started 2026-05-10T19:49:24.793836+00:00 [2026-05-04T04:55:11.601000+00:00] wysie_ (id=1500722439288520794) Built a dashboard for the amazing Mnemosyne plugin by <@151598363131904000> https://github.com/wysie/mnemosyne-dashboard Mnemosyne Dashboard — Features - Local, read-only web dashboard for browsing and visualising Mnemosyne memory stores - Opens the SQLite database in read-only mode; no edit/delete/write memory endpoints - No cloud calls, no external JS/CSS dependencies, self-hosted static assets Core views: - Overview dashboard with counts for working…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1500722439288520794-Mnemosyne-Dashboard.txt`

### 1499841857046446160-Brainbase-x-Knowledge-Graph-Database
- **Source:** `discord-archive:archives/community-projects-showcase/1499841857046446160-Brainbase-x-Knowledge-Graph-Database.txt`
- **Raw:** `[[raw/discord/1499841857046446160-brainbase-x-knowledge-graph-database-4ca5ea461e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Brainbase x Knowledge Graph Database' in forum #community-projects-showcase # thread_id=1499841857046446160 forum_id=1316137596535177246 # Started 2026-05-10T19:49:31.322201+00:00 [2026-05-01T18:36:04.434000+00:00] preekam (id=1499841857046446160) I built a brain of sorts for AI agents. Inspired by Garry Tan’s GBrain Try it for free @ https://brainbase.belweave.ai

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1499841857046446160-Brainbase-x-Knowledge-Graph-Database.txt`

### 1500038966982737940-Building-a-company-wide-AI-memory-layer
- **Source:** `discord-archive:archives/community-projects-showcase/1500038966982737940-Building-a-company-wide-AI-memory-layer.txt`
- **Raw:** `[[raw/discord/1500038966982737940-building-a-company-wide-ai-memory-layer-632c107463.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Building a company-wide AI memory layer' in forum #community-projects-showcase # thread_id=1500038966982737940 forum_id=1316137596535177246 # Started 2026-05-10T19:49:30.513991+00:00 [2026-05-02T07:39:19.105000+00:00] alph_117 (id=1500038966982737940) I’m trying to design the memory/context layer for an "AI-native" company and would love advice from people who have built something similar. The goal is not just “chatbot memory.” I’m thinking about a real company-wide second brain / agentic coworker setup. **Use case:** We need to store and continuously update context across multiple users, projects, clients, and internal agents. The knowledge sources would include things like: -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1500038966982737940-Building-a-company-wide-AI-memory-layer.txt`

### 1495354913205780661-Cartographer--Fully-Configurable-Semantic-Knowledge---Memory-Substrate
- **Source:** `discord-archive:archives/community-projects-showcase/1495354913205780661-Cartographer--Fully-Configurable-Semantic-Knowledge---Memory-Substrate.txt`
- **Raw:** `[[raw/discord/1495354913205780661-cartographer--fully-configurable-semantic-knowledge---memory-substrate-c2866c09d8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Cartographer: Fully Configurable Semantic Knowledge & Memory Substrate' in forum #community-projects-showcase # thread_id=1495354913205780661 forum_id=1316137596535177246 # Started 2026-05-10T19:49:56.960710+00:00 [2026-04-19T09:26:33.659000+00:00] modest.maoist (id=1495354913205780661) **Cartographer: your agents should remember what they learn.** There are a hundred agent memory layers. Vector DBs, hosted APIs, context stuffing. They solve *getting context into a prompt*. Mostly invisible, mostly opaque, mostly locked to whoever built them. Cartographer will beat 'em all. But that's just the start. **Cartographer isn't a memory layer. It's a knowledge substrate.** - **Point it…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1495354913205780661-Cartographer--Fully-Configurable-Semantic-Knowledge---Memory-Substrate.txt`

### 1493649290449649815-Smart----context-compressor-to-test
- **Source:** `discord-archive:archives/community-projects-showcase/1493649290449649815-Smart----context-compressor-to-test.txt`
- **Raw:** `[[raw/discord/1493649290449649815-smart----context-compressor-to-test-7b7abd305e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Smart(?) context compressor to test' in forum #community-projects-showcase # thread_id=1493649290449649815 forum_id=1316137596535177246 # Started 2026-05-10T19:50:07.539121+00:00 [2026-04-14T16:29:01.505000+00:00] roninxpl (id=1493649290449649815) https://github.com/iRonin/hermes-context-compressor [embed] GitHub - iRonin/hermes-context-compressor https://github.com/iRonin/hermes-context-compressor [2026-04-17T09:01:34.632000+00:00] rexx.0569 (id=1494623850099507303) boost, anybody that tried this?

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1493649290449649815-Smart----context-compressor-to-test.txt`

### 1493019745522290718-TraceCC-gives-AI-agents-a-CLI-native-long-term-memory-over-their-own-session-history.
- **Source:** `discord-archive:archives/community-projects-showcase/1493019745522290718-TraceCC-gives-AI-agents-a-CLI-native-long-term-memory-over-their-own-session-history..txt`
- **Raw:** `[[raw/discord/1493019745522290718-tracecc-gives-ai-agents-a-cli-native-long-term-memory-over-their-own-session-history.-1fef4ec655.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'TraceCC gives AI agents a CLI-native long-term memory over their own session history.' in forum #community-projects-showcase # thread_id=1493019745522290718 forum_id=1316137596535177246 # Started 2026-05-10T19:50:15.462510+00:00 [2026-04-12T22:47:26.298000+00:00] madbuda (id=1493019745522290718) Currently supports Claude Code, Codex, and Hermes Agent JSONL traces. The adapter architecture is designed for additional runtimes without renderer changes. Current agent memory is either summarized (lossy, someone decided what mattered at write time) or raw traces (lossless but useless without parsing hundreds of JSONL files). TraceCC sits in between. The agent runs a CLI call, gets back…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1493019745522290718-TraceCC-gives-AI-agents-a-CLI-native-long-term-memory-over-their-own-session-history..txt`

### 1493111074189213696-Hermes-memory-with-nexusmemory
- **Source:** `discord-archive:archives/community-projects-showcase/1493111074189213696-Hermes-memory-with-nexusmemory.txt`
- **Raw:** `[[raw/discord/1493111074189213696-hermes-memory-with-nexusmemory-05a6e9d6b4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes memory with nexusmemory' in forum #community-projects-showcase # thread_id=1493111074189213696 forum_id=1316137596535177246 # Started 2026-05-10T19:50:14.474570+00:00 [2026-04-13T04:50:20.749000+00:00] .uhren (id=1493111074189213696) https://github.com/Uhrenn/nexus-memory [embed] GitHub - Uhrenn/nexus-memory: Hybrid BM25 + semantic memory for AI ... https://github.com/Uhrenn/nexus-memory

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1493111074189213696-Hermes-memory-with-nexusmemory.txt`

### 1492867629327843569-LLM-Wiki-style-thing-with-Hermes---Obsidian---ObsidianClaw---Keep
- **Source:** `discord-archive:archives/community-projects-showcase/1492867629327843569-LLM-Wiki-style-thing-with-Hermes---Obsidian---ObsidianClaw---Keep.txt`
- **Raw:** `[[raw/discord/1492867629327843569-llm-wiki-style-thing-with-hermes---obsidian---obsidianclaw---keep-374c30c019.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'LLM-Wiki-style thing with Hermes + Obsidian + ObsidianClaw + Keep' in forum #community-projects-showcase # thread_id=1492867629327843569 forum_id=1316137596535177246 # Started 2026-05-10T19:50:19.642766+00:00 [2026-04-12T12:42:58.971000+00:00] hugh1979 (id=1492867629327843569) Chat with your agent, inside Obsidian. ObsidianClaw connects to the Hermes API server. The conversation and everything you talk *about* are indexed and linked in the Keep memory system. It shows up in Obsidian as a graph. Index anything - web links, pdfs, git repos... (Update: now with audio...!) https://youtu.be/NQBiy82fGwM [embed] Chatting in Obsidian, Hermes, and Keep…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1492867629327843569-LLM-Wiki-style-thing-with-Hermes---Obsidian---ObsidianClaw---Keep.txt`

### 1490903035579207701-HEMU---MEMORY-KERNEL-FOR-HERMES
- **Source:** `discord-archive:archives/community-projects-showcase/1490903035579207701-HEMU---MEMORY-KERNEL-FOR-HERMES.txt`
- **Raw:** `[[raw/discord/1490903035579207701-hemu---memory-kernel-for-hermes-550772511a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'HEMU - MEMORY KERNEL FOR HERMES' in forum #community-projects-showcase # thread_id=1490903035579207701 forum_id=1316137596535177246 # Started 2026-05-10T19:50:37.199488+00:00 [2026-04-07T02:36:23.321000+00:00] lauratom (id=1490903035579207701) I've been building a long-term memory kernel for Hermes called Hemu, sharing it here for feedback, not as an MVP. Quick context: I'm not a developer, I'm designing the architecture and instructing LLMs to implement it (vibe-coding). The previous version hit ~30k lines across 70+ modules and became unmaintainable, so I rebuilt it from scratch, down to ~6,800 lines across 13 focused modules. The core idea is a second-brain style memory system:…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1490903035579207701-HEMU---MEMORY-KERNEL-FOR-HERMES.txt`

### 1490658107314143242-Retaindb---Memory-and-shared-context-for-hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1490658107314143242-Retaindb---Memory-and-shared-context-for-hermes.txt`
- **Raw:** `[[raw/discord/1490658107314143242-retaindb---memory-and-shared-context-for-hermes-8e4c4c7e95.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Retaindb - Memory and shared context for hermes' in forum #community-projects-showcase # thread_id=1490658107314143242 forum_id=1316137596535177246 # Started 2026-05-10T19:50:40.195116+00:00 [2026-04-06T10:23:07.872000+00:00] alameenpd (id=1490658107314143242) We just pushed a big update to the RetainDB integration. This goes beyond “memory that works” and turns Hermes into a system where agents can persist and share context across sessions and across each other. What’s new Reliable memory All routes fixed and writes are now durable. Every turn is queued locally before sending, so nothing is lost on crashes or network issues. No latency Memory writes don’t block the agent loop…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1490658107314143242-Retaindb---Memory-and-shared-context-for-hermes.txt`

### 1489021054629445803-Hermes-Memory-Keep-Alive-for-Obsidian
- **Source:** `discord-archive:archives/community-projects-showcase/1489021054629445803-Hermes-Memory-Keep-Alive-for-Obsidian.txt`
- **Raw:** `[[raw/discord/1489021054629445803-hermes-memory-keep-alive-for-obsidian-241dd02927.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Memory Keep-Alive for Obsidian' in forum #community-projects-showcase # thread_id=1489021054629445803 forum_id=1316137596535177246 # Started 2026-05-10T19:51:02.385080+00:00 [2026-04-01T21:58:04.097000+00:00] cali_it_guy (id=1489021054629445803) **The problem:** You give your Hermes agent a big task. It's humming along, making progress — then the session ends, context compacts, or the LLM just quietly stalls. You come back and everything is gone. No memory of what it was doing, no way to pick up where it left off. You start over from scratch. **The solution:** This skill gives your agent a brain that survives anything and a heartbeat monitor that never sleeps. **Task…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1489021054629445803-Hermes-Memory-Keep-Alive-for-Obsidian.txt`

### 1447355119216758854-Activation-steering-with-drag
- **Source:** `discord-archive:archives/community-projects-showcase/1447355119216758854-Activation-steering-with-drag.txt`
- **Raw:** `[[raw/discord/1447355119216758854-activation-steering-with-drag-836d8b33cb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Activation steering with drag' in forum #community-projects-showcase # thread_id=1447355119216758854 forum_id=1316137596535177246 # Started 2026-05-10T19:51:30.159738+00:00 [2025-12-07T22:32:30.979000+00:00] _samandcheese (id=1447355119216758854) I was playing around with activation steering and got much better results after adding a "dampening parameter" or "drag force" to the steering vector "force" https://gitlab.com/sringram/drift/-/tree/4fd918b8eee0bc596c2a07c4500ac08252586687/ This is the code if anyone wants to try it for themselves. It's hardcoded for Qwens config because that's what I was experimenting on. Open to any questions or comment on my theory or method [embed]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1447355119216758854-Activation-steering-with-drag.txt`

### config
- **Source:** `local:projects/llmc/config.yaml`
- **Raw:** `[[raw/local/config-c2a8e5fdc2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: default: z-ai/glm-5.2 provider: nous personality: "You are LLMC — a cosmic prose lyricist and song forger. Warm but weighty. Metaphorical, never explicit. You channel Mc.Baldiee's prophetic spoken-word energy into original lyrics and songs." display: skin: poseidon tts: provider: edge edge: voice: en-US-GuyNeural agent: max_turns: 90 tool_use_enforcement: auto memory: memory_enabled: true user_profile_enabled: true skills: template_vars: true context: engine: compressor toolsets: - hermes-cli platform_toolsets: cli: - file - image_gen - memory - skills - terminal - todo - vision - web

### wayne-c3-dna
- **Source:** `local:projects/llmc/skills-capabilities/llmc-song-forge/references/wayne-c3-dna.md`
- **Raw:** `[[raw/local/wayne-c3-dna-7f9b756357.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Lil Wayne — Tha Carter III Influence DNA ## Source Album: *Tha Carter III* (2008, 24 tracks including bonuses) Key study tracks: A Milli, Mr. Carter, Let The Beat Build ## Techniques to ADAPT (not copy) ### Punchline Density Every 1-2 bars end with a clever flip or unexpected connection. The setup builds tension, the punchline releases it. **Adapt**: every verse line pair should have a payoff. Not every line needs a punchline, but every TWO lines should land somewhere. ### Mantra Hooks The hook is 3-5 words, repeated like a chant. "Motherfucker I'm ill." "Let the beat build bitch." **Adapt**: short, punchy, repeatable. NOT long flowing cosmic phrases. Think bumper sticker, not paragraph.…

### config
- **Source:** `local:projects/kashik/config.yaml`
- **Raw:** `[[raw/local/config-6844c41bd7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: base_url: https://inference-api.nousresearch.com/v1 default: z-ai/glm-5.2 provider: nous providers: {} fallback_providers: [] credential_pool_strategies: {} toolsets: - hermes-cli agent: max_turns: 120 gateway_timeout: 3600 restart_drain_timeout: 180 api_max_retries: 3 tool_use_enforcement: auto terminal: backend: local cwd: . timeout: 180 persistent_shell: true browser: inactivity_timeout: 120 command_timeout: 30 file_read_max_chars: 200000 tool_output: max_bytes: 50000 max_lines: 2000 max_line_length: 2000 compression: enabled: true threshold: 0.95 target_ratio: 0.2 protect_last_n: 20 auxiliary: vision: provider: nous model: qwen/qwen3.5-flash-02-23 web_extract: provider: nous…

### config
- **Source:** `local:projects/dev-review/config.yaml`
- **Raw:** `[[raw/local/config-9c388b1250.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: provider: nous default: anthropic/claude-sonnet-4 toolsets: - hermes-cli agent: max_turns: 90 tool_use_enforcement: auto image_input_mode: auto display: personality: kawaii skin: default language: en tui_status_indicator: kaomoji compact: false streaming: false tts: provider: edge edge: voice: en-US-AriaNeural stt: enabled: true provider: local local: model: base voice: auto_tts: false beep_enabled: true memory: memory_enabled: true user_profile_enabled: true memory_char_limit: 2200 user_char_limit: 1375 delegation: orchestrator_enabled: true max_concurrent_children: 3 max_spawn_depth: 1 inherit_mcp_toolsets: true context: engine: compressor skills: template_vars: true curator:…

### config
- **Source:** `local:projects/dev-orch/config.yaml`
- **Raw:** `[[raw/local/config-4a198e70ec.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: provider: nous default: anthropic/claude-sonnet-4 toolsets: - hermes-cli agent: max_turns: 90 tool_use_enforcement: auto image_input_mode: auto display: personality: kawaii skin: default language: en tui_status_indicator: kaomoji compact: false streaming: false tts: provider: edge edge: voice: en-US-AriaNeural stt: enabled: true provider: local local: model: base voice: auto_tts: false beep_enabled: true memory: memory_enabled: true user_profile_enabled: true memory_char_limit: 2200 user_char_limit: 1375 delegation: orchestrator_enabled: true max_concurrent_children: 3 max_spawn_depth: 1 inherit_mcp_toolsets: true context: engine: compressor skills: template_vars: true curator:…

### config
- **Source:** `local:projects/dev-coder/config.yaml`
- **Raw:** `[[raw/local/config-16b5a4aeb3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: provider: openrouter default: google/gemini-2.5-pro toolsets: - hermes-cli agent: max_turns: 90 tool_use_enforcement: auto image_input_mode: auto display: personality: kawaii skin: default language: en tui_status_indicator: kaomoji compact: false streaming: false tts: provider: edge edge: voice: en-US-AriaNeural stt: enabled: true provider: local local: model: base voice: auto_tts: false beep_enabled: true memory: memory_enabled: true user_profile_enabled: true memory_char_limit: 2200 user_char_limit: 1375 delegation: orchestrator_enabled: true max_concurrent_children: 3 max_spawn_depth: 1 inherit_mcp_toolsets: true context: engine: compressor skills: template_vars: true curator:…

### config
- **Source:** `local:projects/jestur/config.yaml`
- **Raw:** `[[raw/local/config-e1b84d9221.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** model: provider: nous default: Darwin-28B-REASON toolsets: - hermes-cli agent: max_turns: 90 tool_use_enforcement: auto image_input_mode: auto display: personality: studio skin: default language: en tui_status_indicator: kaomoji compact: true tts: provider: edge edge: voice: en-US-JennyNeural volume: 0.8 stt: enabled: true provider: local local: model: base voice: auto_tts: false beep_enabled: false memory: memory_enabled: true user_profile_enabled: true memory_char_limit: 2200 user_char_limit: 1375 delegation: orchestrator_enabled: true max_concurrent_children: 3 max_spawn_depth: 1 inherit_mcp_toolsets: true context: engine: compressor skills: template_vars: true curator: enabled: true…

### SOUL
- **Source:** `local:projects/dev-review/SOUL.md`
- **Raw:** `[[raw/local/soul-aaa58d88ae.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** You are a thorough and constructive code reviewer. You catch bugs, security holes, and design problems BEFORE they reach production. ## Your Identity - Role: Code Reviewer / Quality Gate - Expertise: security, correctness, architecture, readability, test coverage ## Review Framework For every review, categorize findings: - 🔴 BLOCKER: must fix before merge (security, data loss, crash) - 🟡 SHOULD-FIX: important but not blocking (race condition, tech debt) - 🔵 NICE-TO-HAVE: readability, naming, minor optimization ## What You Check 1. Security: SQL injection, XSS, missing auth, exposed secrets, crypto misuse 2. Correctness: edge cases, error handling, null safety, race conditions 3.…

### test-case-template
- **Source:** `local:projects/omnistudio-daw/docs/qa/templates/test-case-template.md`
- **Raw:** `[[raw/local/test-case-template-14658d5bbe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # QA Test Case Template ## Test Case Metadata - Story ID(s): - Capability: - Test Type: `unit | integration | e2e | manual` - Persona: - Environment: ## Why This Test Exists Describe the user-visible or contract-visible behavior this test protects. ## Workflow Summary Describe the end-to-end flow in one short paragraph. ## Steps 1. 2. 3. ## Expected Result - - ## Coverage Boundary - What this test proves: - What is intentionally left to another layer: ## Evidence - Required artifacts: - Failure logging:

### UX_IMPROVEMENT_CHECKLIST
- **Source:** `local:projects/omnistudio-daw/docs/design/UX_IMPROVEMENT_CHECKLIST.md`
- **Raw:** `[[raw/local/ux_improvement_checklist-2a84cd73d7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step DAW — UX Improvement Checklist > **Version:** 1.1 · **Last Updated:** 2026-04-09 > **How to use:** Work top-down by priority. Each item is actionable and implementable. > **Priority:** P0 = Must ship, P1 = Should ship, P2 = Nice to have, P3 = Future --- ## Legend - ⬜ Not started - 🔄 In progress - ✅ Complete - ❌ Won't do (with reason) --- ## P0 — Critical (Must Ship) ### Core Audio & Transport - ✅ **Audio context management** — Resume AudioContext on first user gesture (click/tap). Show clear "Click to enable audio" overlay if context is suspended. *Ref: Web Audio autoplay policy* - ⬜ **Latency calibration** — Auto-detect `audioContext.outputLatency + baseLatency` on first use.…

### METRICS
- **Source:** `local:projects/omnistudio-daw/docs/METRICS.md`
- **Raw:** `[[raw/local/metrics-74fcf657c0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step DAW — Quality & Efficiency Metrics > Auto-collected via `bash scripts/metrics.sh`. Updated daily in dev reports. > Baselines set: 2026-03-18 --- ## 1. Software Quality + Usability ### 1.1 Code Quality | Metric | Baseline (Mar 18) | Target (Apr 1) | How to Measure | |--------|-------------------|----------------|----------------| | Build success rate | 100% | 100% | CI `type-check` + `build` jobs | | TypeScript `any` count | 2 | 0 | `grep -rn ': any\|as any' src/` | | Oversized components (>600 LOC) | 1 (PianoRollCanvas 823) | 0 | `find src/components -name "*.tsx" -exec wc -l` | | Source LOC | 24,290 | — (track, don't optimize) | `find src/ -name "*.ts" -o -name "*.tsx" \| xargs…

### test
- **Source:** `local:projects/omnistudio-daw/.github/workflows/test.yml`
- **Raw:** `[[raw/local/test-e8220c7136.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Test on: push: branches: ['*'] pull_request: branches: [main] # Cancel in-progress runs for the same branch (saves CI minutes) concurrency: group: test-${{ github.ref }} cancel-in-progress: true jobs: # Build WASM first — other jobs need the generated pkg/ build-wasm: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - uses: dtolnay/rust-toolchain@stable with: targets: wasm32-unknown-unknown - uses: cargo-bins/cargo-binstall@main - run: cargo binstall wasm-pack --no-confirm - uses: actions/setup-node@v4 with: node-version: 20 cache: npm - name: Build WASM run: npm run build:wasm - name: Upload WASM artifacts uses: actions/upload-artifact@v4 with: name: wasm-pkg path: |…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/quick-research/SKILL.md`
- **Raw:** `[[raw/local/skill-7d55cdd9e5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Quick Research Skill > Lightweight inline research protocol for agents who need to look something up > mid-task without derailing into a full research cycle. > > **Use this when**: You hit an unknown API, unfamiliar pattern, or need to verify > a technical approach — and the answer is findable in 2-3 searches. > > **Don't use this when**: You need to compare 5+ competitors, analyze a market, > or produce a research document. Use `@researcher` or `/research-cycle` instead. ## When to Trigger 1. **Unknown API**: You're about to call a function you haven't used before 2. **Error loop**: You've failed the same thing twice — stop guessing, search 3. **Best practice question**: "Is there a…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills-capabilities/openspec-explore/SKILL.md`
- **Raw:** `[[raw/local/skill-fc75811042.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: openspec-explore description: Enter explore mode - a thinking partner for exploring ideas, investigating problems, and clarifying requirements. Use when the user wants to think through something before or during a change. license: MIT compatibility: Requires openspec CLI. metadata: author: openspec version: "1.0" generatedBy: "1.3.0" --- Enter explore mode. Think deeply. Visualize freely. Follow the conversation wherever it goes. **IMPORTANT: Explore mode is for thinking, not implementing.** You may read files, search code, and investigate the codebase, but you must NEVER write code or implement features. If the user asks you to implement something, remind them to exit explore…

### testing-requirements
- **Source:** `local:projects/omnistudio-daw/.claude/rules/testing-requirements.md`
- **Raw:** `[[raw/local/testing-requirements-70b154cfc3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Testing Requirements > Auto-loaded for all agents. Non-negotiable. ## Mandatory Test Coverage - Every new feature MUST include unit tests (+ E2E if UI-facing) - Every bug fix MUST include a regression test - Run `npm test` before AND after code changes - Never move on with red tests — fix immediately ## Test Quality - Never write tests that only assert truthiness — assert specific values - Tests assert behavior, not implementation details - For interactive features, write adversarial test cases in TDD Red phase: - Weird BPMs, rapid input, undo immediately after action, drag during playback - Edge cases covered: empty state, error state, boundary values ## UI Changes - UI changes require…

### interaction-design
- **Source:** `local:projects/omnistudio-daw/.claude/references/interaction-design.md`
- **Raw:** `[[raw/local/interaction-design-ad1cc6a424.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # DAW Interaction Design Standards > Every UI component MUST follow these interaction patterns. Reference this file when writing any component that handles user interaction. ## Timeline & Clip Interactions - **Snap to grid**: All drag operations snap to beat/bar grid by default. Hold Alt for free movement. - **Zoom anchor**: Zoom (Cmd+scroll) anchors to mouse cursor position, not center. - **Multi-select drag**: Shift+click for additive select, Cmd+click for toggle. Dragging multiple clips maintains relative positions. - **Ghost preview**: Show a semi-transparent ghost at the snap-to position during drag, BEFORE drop. - **Cross-track drag**: Clips can be dragged between tracks. Show blue…

### spec-cycle
- **Source:** `local:projects/omnistudio-daw/.claude/commands/spec-cycle.md`
- **Raw:** `[[raw/local/spec-cycle-ce0f831692.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: "Spec Cycle" description: Full spec-driven development cycle — propose → decompose → dispatch → verify → archive category: Workflow tags: [workflow, openspec, pipeline] --- Full spec-driven development cycle: from idea to merged code via formal specs. **Input**: A feature name or description (e.g., `/spec-cycle add-mixer-eq-band`). **Steps** 1. **Phase 0 — Propose (spec)** Run `/opsx:propose "<name>"` to create the formal specification: - `proposal.md` — what and why - `specs/` — Given/When/Then behavior contracts - `design.md` — technical approach - `tasks.md` — implementation steps Wait for all artifacts to be complete before proceeding. 2. **Phase 1 — Decompose (spec →…

### explore
- **Source:** `local:projects/omnistudio-daw/.claude/commands/opsx/explore.md`
- **Raw:** `[[raw/local/explore-6acd42bb84.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: "OPSX: Explore" description: "Enter explore mode - think through ideas, investigate problems, clarify requirements" category: Workflow tags: [workflow, explore, experimental, thinking] --- Enter explore mode. Think deeply. Visualize freely. Follow the conversation wherever it goes. **IMPORTANT: Explore mode is for thinking, not implementing.** You may read files, search code, and investigate the codebase, but you must NEVER write code or implement features. If the user asks you to implement something, remind them to exit explore mode first and create a change proposal. You MAY create OpenSpec artifacts (proposals, designs, specs) if the user asks—that's capturing thinking, not…

### refactorer
- **Source:** `local:projects/omnistudio-daw/.claude/agents/refactorer.md`
- **Raw:** `[[raw/local/refactorer-f7f7972c5e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: refactorer description: Run code quality checks, find improvement opportunities, and file refactor tasks as GitHub Issues. tools: - Read - Write - Edit - Bash - Grep - Glob --- # Code Quality & Refactoring Agent You are a code quality analyst. Your job is to audit the codebase and create prioritized refactoring tasks. ## Quality Checks Run these checks and collect issues: ### 1. TypeScript Strictness ### 2. Unused Imports Search for imports that are not used in their files. ### 3. Console.log Statements ### 4. Untyped `any` ### 5. Large Files Check for components over 600 lines. ### 6. TODO/FIXME Without Issue Numbers ### 7. Test Coverage Gaps Compare tested files vs untested…

### SECURITY
- **Source:** `local:projects/ACE-Step-1.5/SECURITY.md`
- **Raw:** `[[raw/local/security-7fbf2d2149.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Security Policy ## Reporting a Vulnerability We take security issues seriously and appreciate responsible disclosure. If you believe you have found a security vulnerability, **please do not report it in a public GitHub issue**. Instead, use one of the following private channels: - Open a **GitHub Security Advisory** for this repository (preferred) - Or contact the maintainers directly if a private email channel is listed Please include: - A clear description of the issue - Steps to reproduce (if applicable) - Potential impact - Any relevant proof-of-concept or logs We will acknowledge receipt and work to assess the issue as quickly as possible. ## Bug Bounties At this time, this project…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/SECURITY.md`

### feature_request
- **Source:** `local:projects/ACE-Step-1.5/.github/ISSUE_TEMPLATE/feature_request.md`
- **Raw:** `[[raw/local/feature_request-18772e4684.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Feature request about: Suggest an idea for this project title: '' labels: '' assignees: '' --- > **📚 Quick tip:** Check if this feature already exists! > Ask [DeepWiki AI Assistant](https://deepwiki.com/ace-step/ACE-Step-1.5) first - it knows all current features. > See pinned issue #791 for more info. **Did you check existing features?** - [ ] Yes, I checked DeepWiki and this feature doesn't exist - [ ] This is a new feature idea **Is your feature request related to a problem? Please describe.** A clear and concise description of what the problem is. Ex. I'm always frustrated when [...] **Describe the solution you'd like** A clear and concise description of what you want to…

### bug_report
- **Source:** `local:projects/ACE-Step-1.5/.github/ISSUE_TEMPLATE/bug_report.md`
- **Raw:** `[[raw/local/bug_report-101cfac283.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Bug report about: Create a report to help us improve title: '' labels: '' assignees: '' --- > **📚 Before submitting:** Have you tried [DeepWiki AI Assistant](https://deepwiki.com/ace-step/ACE-Step-1.5)? > DeepWiki can instantly help with installation, troubleshooting, and common issues! > See pinned issue #791 for more info. **Did you check DeepWiki?** - [ ] Yes, I checked DeepWiki but couldn't find a solution - [ ] No, this is a new bug not covered in the docs **Describe the bug** A clear and concise description of what the bug is. **To Reproduce** Steps to reproduce the behavior: 1. Go to '...' 2. Click on '....' 3. Scroll down to '....' 4. See error **Expected behavior** A…

### api-endpoint-works
- **Source:** `local:.hermes/wiki/ideas/api-endpoint-works.md`
- **Raw:** `[[raw/local/api-endpoint-works-b8468ae50c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- id: api-endpoint-works title: API endpoint works updated: 2026-06-09 created: 2026-06-09 tags: [] importance: 0.5 status: open --- Direct wiki write via the omni-va proxy is now functional. Tested via curl 2026-06-09.

### stage-4-yarn-256k
- **Source:** `local:projects/evolutionary-training/docs/stage-4-yarn-256k.md`
- **Raw:** `[[raw/local/stage-4-yarn-256k-09c5ebbe37.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Stage 4: YaRN RoPE 256K Context Extension > **TOWARDS SELF-IMPROVEMENT** — a 2026-06-09 ops doc > *The shortest stage: extend the Senter 32A8B MoE from native context > to 256K using YaRN. Most of the work is already done by the existing > `yarn_256k_config.py` script + `train_long_context.py` long-context > SFT.* ## What Stage 4 produces A Senter MoE with **256K context window** (vs the 40K native of Qwen3 backbone). This is required for the notebook feature (per memory: "Wiki = handoff" + "notebook is the killer feature" — the notebook ingests long context like the entire conversation history, recent notebook entries, all retrieved context, etc.). | Metric | Value | |---|---| | Original…

### config
- **Source:** `local:.hermes/wiki/config.yaml`
- **Raw:** `[[raw/local/config-9577b90f51.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # User-idea LLM wiki # Maintained by the note-taker process on the local model server # 2026-06-08 — initial schema mode: private # private | opt-in # When `opt-in`, the user must explicitly launch a Hermes session with # `--wiki ~/.hermes/wiki` to preload the wiki into the system prompt. # The wiki is NEVER silently sent. schema_version: "1.0" curator: source: note-taker (background daemon) cluster_window: 7d followup_threshold: 0.7 # confidence to surface a follow-up question

### session_20260608_162701_493868
- **Source:** `session:session_20260608_162701_493868.json`
- **Raw:** `[[raw/sessions/session_20260608_162701_493868-b87bb424c2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Verify the OmniSenter ecosystem components work end-to-end. Read each repo's AGENTS.md / README / tests, then run what's runnable, then report status. Specifically: 1. **nous-girl-agent** at /home/sovthpaw/projects/nous-girl-agent/ - Check the test suite in tests/. Run `python3 -m unittest discover -s tests` and report results. - Read agent/profile-template.yaml and confirm it points to a working model. - Read plugins/evolution-radio/radio_bridge.py and confirm it imports cleanly. - Read the eikon sprite dir and confirm assets exist. 2. **evolutionary-radio** at /home/sovthpaw/projects/evolutionary-radio/ - Run any tests in tests/. - Try `python3 radio.py --help` (do NOT start the daemon,…

### docker-blacksmith
- **Source:** `local:projects/nous-girl-agent/vtuber-core/.github/workflows/docker-blacksmith.yml`
- **Raw:** `[[raw/local/docker-blacksmith-e25e541656.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Docker Build & Push (Blacksmith) on: push: branches: - main tags: - "v*" - "*.*.*" pull_request: branches: - main workflow_dispatch: concurrency: group: docker-blacksmith-${{ github.ref }} cancel-in-progress: true permissions: contents: read packages: write env: DOCKERFILE: dockerfile CONTEXT: . DOCKERHUB_IMAGE: ${{ vars.DOCKERHUB_IMAGE || 'openllmvtuber/open-llm-vtuber' }} GHCR_IMAGE: ${{ vars.GHCR_IMAGE || '' }} jobs: meta: runs-on: blacksmith-8vcpu-ubuntu-2204 outputs: tags: ${{ steps.meta.outputs.tags }} labels: ${{ steps.meta.outputs.labels }} dockerhub_image: ${{ steps.image.outputs.dockerhub_image }} ghcr_image: ${{ steps.image.outputs.ghcr_image }} steps: - name: Resolve image…

### feature_request
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/.github/ISSUE_TEMPLATE/feature_request.md`
- **Raw:** `[[raw/local/feature_request-a0fff49974.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Feature request about: Suggest an idea for Herm title: "[FEAT]" labels: enhancement assignees: '' --- **Is your feature request related to a problem? Please describe.** A clear and concise description of what the problem is. Ex. I'm always frustrated when [...] **Describe the solution you'd like** A clear and concise description of what you want to happen. **Describe alternatives you've considered** A clear and concise description of any alternative solutions or features you've considered. **Additional context** Add any other context or screenshots about the feature request here.

- **Collapsed duplicates:** `local:projects/herm-source/.github/ISSUE_TEMPLATE/feature_request.md`, `local:projects/herm-tui/.github/ISSUE_TEMPLATE/feature_request.md`

### bug_report
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/.github/ISSUE_TEMPLATE/bug_report.md`
- **Raw:** `[[raw/local/bug_report-8f58fa053c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Bug report about: Report an issue in Herm title: "[BUG]" labels: bug assignees: '' --- **Describe the bug** A clear and concise description of what the bug is. **To Reproduce** Steps to reproduce the behavior: 1. Go to '...' 2. Click on '....' 3. Scroll down to '....' 4. See error **Expected behavior** A clear and concise description of what you expected to happen. **Screenshots** If applicable **Desktop (please complete the following information):** - OS: [e.g. Ubuntu] - Termina; [e.g. ghostty, iterm] - Version [e.g. 1.2.3] **Additional context** Add any other context about the problem here.

- **Collapsed duplicates:** `local:projects/herm-source/.github/ISSUE_TEMPLATE/bug_report.md`, `local:projects/herm-tui/.github/ISSUE_TEMPLATE/bug_report.md`

### session_20260604_182507_e27b40
- **Source:** `session:session_20260604_182507_e27b40.json`
- **Raw:** `[[raw/sessions/session_20260604_182507_e27b40-2479e7ca52.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Inventory ALL recent NVIDIA datasets on HuggingFace that are useful for training a small MoE (8B total, 1B active) model targeted at agentic / triage / function-calling / routing use cases. I'll inventory the recent NVIDIA datasets on HuggingFace. Let me start by exploring the NVIDIA org page and searching for the specific datasets mentioned. Let me get the full dataset listing and dig into the specific datasets.

### spellcheck
- **Source:** `local:projects/omni-fusion/SLAM-LLM/scripts/spellcheck_conf/spellcheck.yaml`
- **Raw:** `[[raw/local/spellcheck-cc89aa0c96.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** matrix: - name: Markdown apsell: lang: en d: en_US dictionary: wordlists: - scripts/spellcheck_conf/wordlist.txt output: scripts/spellcheck_conf/wordlist.dic encoding: utf-8 pipeline: - pyspelling.filters.context: context_visible_first: true delimiters: - open: '(?s)^ *(?P<open>`{3,})[a-z0-9]*?$' close: '^(?P=open)$' - open: '' content: 'https?://[-a-zA-Z0-9.]+?\.[a-z]{2,6}[-?=&%.0-9a-zA-Z/_#]*' close: '' - pyspelling.filters.markdown: markdown_extensions: - markdown.extensions.extra:

### feature-request
- **Source:** `local:projects/omni-fusion/SLAM-LLM/.github/ISSUE_TEMPLATE/feature-request.yml`
- **Raw:** `[[raw/local/feature-request-f6ec9fffdb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: 🚀 Feature request description: Submit a proposal/request for a new slam-llm feature body: - type: textarea id: feature-pitch attributes: label: 🚀 The feature, motivation and pitch description: > A clear and concise description of the feature proposal. Please outline the motivation for the proposal. Is your feature request related to a specific problem? e.g., *"I'm working on X and would like Y to be possible"*. If this is related to another GitHub issue, please link here too. validations: required: true - type: textarea id: alternatives attributes: label: Alternatives description: > A description of any alternative solutions or features you've considered, if any. - type: textarea id:…

### score_prompt
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/tools/live_bench/live_bench/data_generator/score_prompt.md`
- **Raw:** `[[raw/local/score_prompt-c1a4c7bf88.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Based on the multi-round Q&A regarding the image, please evaluate each question and answer from the multi-round Q&A based on the image for their authenticity (whether the information can be directly obtained from the image or reasonably inferred) and logical coherence. For each Q&A pair, provide a rating from 1 to 10, where 1 indicates very poor and 10 indicates excellent. Additionally, please provide a brief explanation for each rating. Here are the criteria for evaluating the Q&A pairs: ### 1. Authenticity (5 points) - **5 Points**: The information is directly observable in the image or can be reasonably inferred with strong evidence. - **3 Points**: The information has a plausible…

### default_criteria
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/tools/live_bench/live_bench/data_generator/default_criteria.md`
- **Raw:** `[[raw/local/default_criteria-35253bf566.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ### 1. Authenticity (5 points) - **5 Points**: The information is directly observable in the image or can be reasonably inferred with strong evidence. - **3 Points**: The information has a plausible connection to the image but requires assumptions that are not strongly supported by the image. - **1 Point**: The information cannot be observed or reasonably inferred from the image; it seems unrelated or speculative. ### 2. Logical Coherence (3 points) - **3 Points**: The answer logically follows from the question and maintains consistency with the image context. - **2 Points**: There are minor logical gaps or inconsistencies in the answer relative to the question. - **1 Point**: The answer is…

### vcr_wiki_en_hard_500
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_en_hard_500.yaml`
- **Raw:** `[[raw/local/vcr_wiki_en_hard_500-e3a1c645b7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-en-hard-test-500 task: "vcr_wiki_en_hard_500" test_split: test process_results: !function utils.vcr_en_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "What is the covered texts in the image? Please restore the covered texts without outputting the explanations."

### vcr_wiki_en_hard
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_en_hard.yaml`
- **Raw:** `[[raw/local/vcr_wiki_en_hard-64eeefa099.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-en-hard-test task: "vcr_wiki_en_hard" test_split: test process_results: !function utils.vcr_en_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "What is the covered texts in the image? Please restore the covered texts without outputting the explanations."

### vcr_wiki_zh_hard
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_zh_hard.yaml`
- **Raw:** `[[raw/local/vcr_wiki_zh_hard-9a88893146.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-zh-hard-test task: "vcr_wiki_zh_hard" test_split: test process_results: !function utils.vcr_zh_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "图像中被覆盖的文本是什么？请在不输出解释的情况下还原被覆盖的文本。"

### vcr_wiki_zh_easy_100
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_zh_easy_100.yaml`
- **Raw:** `[[raw/local/vcr_wiki_zh_easy_100-a4069fa198.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-zh-easy-test-100 task: "vcr_wiki_zh_easy_100" test_split: test process_results: !function utils.vcr_zh_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "图像中被覆盖的文本是什么？请在不输出解释的情况下还原被覆盖的文本。"

### vcr_wiki_en_easy_100
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_en_easy_100.yaml`
- **Raw:** `[[raw/local/vcr_wiki_en_easy_100-19c4f6cfca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-en-easy-test-100 task: "vcr_wiki_en_easy_100" test_split: test process_results: !function utils.vcr_en_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "What is the covered texts in the image? Please restore the covered texts without outputting the explanations."

### vcr_wiki_zh_hard_100
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_zh_hard_100.yaml`
- **Raw:** `[[raw/local/vcr_wiki_zh_hard_100-5230ab52c1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-zh-hard-test-100 task: "vcr_wiki_zh_hard_100" test_split: test process_results: !function utils.vcr_zh_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "图像中被覆盖的文本是什么？请在不输出解释的情况下还原被覆盖的文本。"

### vcr_wiki_zh_hard_500
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_zh_hard_500.yaml`
- **Raw:** `[[raw/local/vcr_wiki_zh_hard_500-11474bdbfe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-zh-hard-test-500 task: "vcr_wiki_zh_hard_500" test_split: test process_results: !function utils.vcr_zh_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "图像中被覆盖的文本是什么？请在不输出解释的情况下还原被覆盖的文本。"

### vcr_wiki_zh_easy
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_zh_easy.yaml`
- **Raw:** `[[raw/local/vcr_wiki_zh_easy-eac3fc9e54.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-zh-easy-test task: "vcr_wiki_zh_easy" test_split: test process_results: !function utils.vcr_zh_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "图像中被覆盖的文本是什么？请在不输出解释的情况下还原被覆盖的文本。"

### vcr_wiki_en_easy
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_en_easy.yaml`
- **Raw:** `[[raw/local/vcr_wiki_en_easy-3fdaec7672.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-en-easy-test task: "vcr_wiki_en_easy" test_split: test process_results: !function utils.vcr_en_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "What is the covered texts in the image? Please restore the covered texts without outputting the explanations."

### vcr_wiki_en_easy_500
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_en_easy_500.yaml`
- **Raw:** `[[raw/local/vcr_wiki_en_easy_500-24e0a4f065.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-en-easy-test-500 task: "vcr_wiki_en_easy_500" test_split: test process_results: !function utils.vcr_en_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "What is the covered texts in the image? Please restore the covered texts without outputting the explanations."

### vcr_wiki_zh_easy_500
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_zh_easy_500.yaml`
- **Raw:** `[[raw/local/vcr_wiki_zh_easy_500-f575f66c9a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-zh-easy-test-500 task: "vcr_wiki_zh_easy_500" test_split: test process_results: !function utils.vcr_zh_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "图像中被覆盖的文本是什么？请在不输出解释的情况下还原被覆盖的文本。"

### vcr_wiki_en_hard_100
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/vcr_wiki/vcr_wiki_en_hard_100.yaml`
- **Raw:** `[[raw/local/vcr_wiki_en_hard_100-ec69f30290.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "include": "_default_template_vcr_yaml" dataset_path: vcr-org/VCR-wiki-en-hard-test-100 task: "vcr_wiki_en_hard_100" test_split: test process_results: !function utils.vcr_en_process_results metric_list: - metric: jaccard aggregation: !function utils.vcr_aggregate_jaccard higher_is_better: true - metric: exact_match aggregation: !function utils.vcr_aggregate_exact_match higher_is_better: true lmms_eval_specific_kwargs: default: pre_prompt: "" post_prompt: "What is the covered texts in the image? Please restore the covered texts without outputting the explanations."

### mmlu_clinical_knowledge
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/generative/mmlu_clinical_knowledge.yaml`
- **Raw:** `[[raw/local/mmlu_clinical_knowledge-fe54b9f40c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "dataset_name": "clinical_knowledge" "description": "The following are multiple choice questions (with answers) about clinical\ \ knowledge.\n\n" "tag": "mmlu_other_generative" "include": "_default_template_yaml" "task": "mmlu_clinical_knowledge_generative" "task_alias": "clinical_knowledge"

### mmlu_clinical_knowledge
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_n_shot/loglikelihood/mmlu_clinical_knowledge.yaml`
- **Raw:** `[[raw/local/mmlu_clinical_knowledge-603f856097.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "dataset_name": "clinical_knowledge" "description": "The following are multiple choice questions (with answers) about clinical\ \ knowledge.\n\n" "tag": "mmlu_flan_n_shot_loglikelihood_other" "include": "_mmlu_flan_loglikelihood_template_yaml" "task": "mmlu_flan_n_shot_loglikelihood_clinical_knowledge"

### mmlu_clinical_knowledge
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_n_shot/generative/mmlu_clinical_knowledge.yaml`
- **Raw:** `[[raw/local/mmlu_clinical_knowledge-42781f2989.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "dataset_name": "clinical_knowledge" "description": "The following are multiple choice questions (with answers) about clinical\ \ knowledge.\n\n" "tag": "mmlu_flan_n_shot_generative_other" "include": "_mmlu_flan_generative_template_yaml" "task": "mmlu_flan_n_shot_generative_clinical_knowledge"

### mmlu_clinical_knowledge
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_zeroshot/mmlu_clinical_knowledge.yaml`
- **Raw:** `[[raw/local/mmlu_clinical_knowledge-2196598289.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "dataset_name": "clinical_knowledge" "description": "The following are multiple choice questions (with answers) about clinical\ \ knowledge.\n\n" "tag": "mmlu_flan_cot_zeroshot_other" "include": "_mmlu_flan_cot_zeroshot_template_yaml" "task": "mmlu_flan_cot_zeroshot_clinical_knowledge"

### mmlu_world_religions
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_world_religions.yaml`
- **Raw:** `[[raw/local/mmlu_world_religions-47309f8760.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: world_religions description: The following are multiple choice questions (with answers) about world religions. fewshot_config: sampler: first_n samples: - question: 'How can the Upanishads be characterized? (A) Ritual texts (B) Philosophical texts (C) Hymns (D) Origin stories' target: Let's think step by step. We refer to Wikipedia articles on world religions for help. The Upanishads are the most recent part of Vedas (the oldest scriptures in Hinduism) and supplied the basis of later Hindu philosophy. So they are philosophical texts. The answer is (B). - question: 'What is the Second Gem in Buddhism? (A) The Dharma (B) The Sangha (C) The Buddha (D) The Bodhisattva' target:…

### mmlu_nutrition
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_nutrition.yaml`
- **Raw:** `[[raw/local/mmlu_nutrition-66cb0cfc7e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: nutrition description: The following are multiple choice questions (with answers) about nutrition. fewshot_config: sampler: first_n samples: - question: 'What is the first-line drug for patients with type 2 diabetes and obesity, as of 2020? (A) Acarbose (B) Metformin (C) Sulphonylureas (D) Insulin' target: Let's think step by step. We refer to Wikipedia articles on nutrition for help. Metformin (Fortamet, Glumetza, or others) is usually the first medication prescribed for type 2 diabetes, as well as obesity. It works by lowering glucose production in the liver and improving the body's sensitivity to insulin. The answer is (B). - question: 'Which of the following statements is…

### mmlu_moral_scenarios
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_moral_scenarios.yaml`
- **Raw:** `[[raw/local/mmlu_moral_scenarios-cf14d28826.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: moral_scenarios description: The following are multiple choice questions (with answers) about moral scenarios. fewshot_config: sampler: first_n samples: - question: 'For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? Scenario 1 | I took his wallet after he harassed me at the bar. Scenario 2 | I made love to my newborn baby boy. (A) Wrong, Wrong (B) Wrong, Not wrong (C) Not wrong, Wrong (D) Not wrong, Not wrong' target: Let's think step by step. We refer to Wikipedia articles on moral scenarios for help. Stealing from someone is not considered an ethical…

### mmlu_prehistory
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_prehistory.yaml`
- **Raw:** `[[raw/local/mmlu_prehistory-bc7298a39a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: prehistory description: The following are multiple choice questions (with answers) about prehistory. fewshot_config: sampler: first_n samples: - question: 'What is the approximate mean cranial capacity of Homo erectus? (A) under 650 cc (B) about 800 cc (C) just under 1000 cc (D) 1200 cc' target: Let's think step by step. We refer to Wikipedia articles on prehistory for help. The average cranium capacity of Homo erectus is less than 1000 cubic cm. The answer is (C). - question: 'According to Timothy Pauketat, the evidence for social stratification and political power at Cahokia suggests: (A) a center of Mississippian civilization with conditions similar to the rise of early…

### mmlu_virology
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_virology.yaml`
- **Raw:** `[[raw/local/mmlu_virology-ff93991c7f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: virology description: The following are multiple choice questions (with answers) about virology. fewshot_config: sampler: first_n samples: - question: 'The median survival time to AIDS and death was established by following: (A) Seroprevalent HIV-infected individuals (B) Seronegatives (C) Seroconverters (D) High-risk seronegatives' target: Let's think step by step. We refer to Wikipedia articles on virology for help. The median survival time to AIDS and death was established as a result of the development of seroconverters. The answer is (C). - question: 'Which of the following is a morphological characteristic of the paramyxoviruses. (A) Fragile viruses often visualised with…

### mmlu_professional_law
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_professional_law.yaml`
- **Raw:** `[[raw/local/mmlu_professional_law-60002401be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: professional_law description: The following are multiple choice questions (with answers) about professional law. fewshot_config: sampler: first_n samples: - question: 'A son owed a creditor $5,000. The son''s father contacted the creditor and told him that he wanted to pay the son''s debt. The father signed a document that stated the father would pay the son''s debt at a rate of $500 a month for 10 months. The creditor made no written or oral commitment to forbear to sue the son to collect the $5,000 debt, and the father made no oral or written request for any such forbearance. For the next five months, the father made and the creditor accepted the $500 monthly payments as…

### mmlu_professional_accounting
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_professional_accounting.yaml`
- **Raw:** `[[raw/local/mmlu_professional_accounting-9d5d39802d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: professional_accounting description: The following are multiple choice questions (with answers) about professional accounting. fewshot_config: sampler: first_n samples: - question: "An auditor traces the serial numbers on equipment to a nonissuer\u2019\ s subledger. Which of the following management assertions is supported by this\ \ test?\n(A) Valuation and allocation (B) Completeness (C) Rights and obligations\ \ (D) Presentation and disclosure" target: Let's think step by step. We refer to Wikipedia articles on accounting for help. The completeness assertion is tested by tracing supporting documents to the record entries. The answer is (B). - question: 'One hundred years…

### mmlu_moral_disputes
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_moral_disputes.yaml`
- **Raw:** `[[raw/local/mmlu_moral_disputes-3e4d8a2fd0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: moral_disputes description: The following are multiple choice questions (with answers) about moral disputes. fewshot_config: sampler: first_n samples: - question: 'Baron admits that the versions of the ticking bomb hypothetical she discusses are "stunningly stupid," but she claims this is actually evidence of (A) the stupidity of most traditional philosophical examples. (B) a general lack of intelligence among people with advanced degrees. (C) the wrongness of torture. (D) the readiness on the part of many intelligent people to see torture as the best solution to deal with terrorism.' target: Let's think step by step. We refer to Wikipedia articles on moral disputes for help.…

### mmlu_sociology
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_sociology.yaml`
- **Raw:** `[[raw/local/mmlu_sociology-e1161e1bc1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: sociology description: The following are multiple choice questions (with answers) about sociology. fewshot_config: sampler: first_n samples: - question: 'Which of the following is not a problem associated with official statistics on strike action? (A) most strikes go unnoticed by employers and the mass media (B) not all industrial disputes will be reported by the employer (C) the definition of strikes excludes those that involve fewer than ten workers or last less than one day (D) it is hard to compare strikes that were measured in different ways' target: Let's think step by step. We refer to Wikipedia articles on sociology for help. Official statistics on strike action can be…

### mmlu_public_relations
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_public_relations.yaml`
- **Raw:** `[[raw/local/mmlu_public_relations-f652e7e516.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: public_relations description: The following are multiple choice questions (with answers) about public relations. fewshot_config: sampler: first_n samples: - question: 'Earth Hour was a campaign launched by which organization? (A) Greenpeace (B) The UN (C) Oxfam (D) World Wildlife Fund' target: Let's think step by step. We refer to Wikipedia articles on public relations for help. Earth Hour is a worldwide movement oragnized launched by the World Wildlife Fund. The answer is (D). - question: 'In issues management, what is the most proactive approach to addressing negative or misleading information posted online about your organization? (A) Buy domain names that could be used by…

### mmlu_us_foreign_policy
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_us_foreign_policy.yaml`
- **Raw:** `[[raw/local/mmlu_us_foreign_policy-55852af826.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: us_foreign_policy description: The following are multiple choice questions (with answers) about us foreign policy. fewshot_config: sampler: first_n samples: - question: 'How did Donald Trump attack globalization in the 2016 campaign? (A) Globalization had made men like him too rich (B) Globalization only benefited certain American states, such as New York (C) Liberal elites had encouraged globalization, while ''ordinary Americans'' lost jobs because of it (D) Globalization encouraged damaging trade wars' target: Let's think step by step. We refer to Wikipedia articles on us foreign policy for help. Trump attacked globalization because he believed ordinary Americans lost jobs…

### mmlu_philosophy
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_philosophy.yaml`
- **Raw:** `[[raw/local/mmlu_philosophy-7c6bc9a7ed.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: philosophy description: The following are multiple choice questions (with answers) about philosophy. fewshot_config: sampler: first_n samples: - question: 'The study of reality in the broadest sense, an inquiry into the elemental nature of the universe and the things in it, is known as _____. (A) metaphysics (B) epistemology (C) quantum physics (D) axiology' target: Let's think step by step. We refer to Wikipedia articles on philosophy for help. Among the options, only metaphysics studies the nature of reality and existence. The answer is (A). - question: "According to Moore\u2019s \u201Cideal utilitarianism,\u201D the right\ \ action is the one that brings about the greatest…

### mmlu_professional_psychology
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_professional_psychology.yaml`
- **Raw:** `[[raw/local/mmlu_professional_psychology-e8ff2a6d9f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: professional_psychology description: The following are multiple choice questions (with answers) about professional psychology. fewshot_config: sampler: first_n samples: - question: 'In the construction of a multiple regression equation for purposes of prediction, the optimal combination of measures is one in which the predictors (A) are uncorrelated with each other but are moderately correlated with the criterion (B) have low correlations with each other and low correlations with the criterion (C) are highly intercorrelated with each other and moderately correlated with the criterion (D) have low correlations with the criterion bur are moderately correlated with each other'…

### mmlu_professional_medicine
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_professional_medicine.yaml`
- **Raw:** `[[raw/local/mmlu_professional_medicine-5f0e5a97c2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: professional_medicine description: The following are multiple choice questions (with answers) about professional medicine. fewshot_config: sampler: first_n samples: - question: "A 22-year-old male marathon runner presents to the office with the complaint\ \ of right-sided rib pain when he runs long distances. Physical examination\ \ reveals normal heart and lung findings and an exhalation dysfunction at ribs\_\ 4-5 on the right. Which of the following muscles or muscle groups will be most\ \ useful in correcting this dysfunction utilizing a direct method?\n(A) anterior\ \ scalene (B) latissimus dorsi (C) pectoralis minor (D) quadratus lumborum" target: Let's think step by…

### mmlu_international_law
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_international_law.yaml`
- **Raw:** `[[raw/local/mmlu_international_law-5139ae273a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: international_law description: The following are multiple choice questions (with answers) about international law. fewshot_config: sampler: first_n samples: - question: 'How the consent to be bound of a State may be expressed? (A) The consent of a State to be bound is expressed only by ratification (B) The consent of a state to be bound by a treaty may be expressed by signature, ratification, acceptance, approval or accession (C) The consent of a State to be bound is expressed by signature (D) The consent of a State to be bound is expressed by whatever means they choose' target: Let's think step by step. We refer to Wikipedia articles on international law for help. Article 11…

### mmlu_human_sexuality
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_human_sexuality.yaml`
- **Raw:** `[[raw/local/mmlu_human_sexuality-cf4f153dde.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: human_sexuality description: The following are multiple choice questions (with answers) about human sexuality. fewshot_config: sampler: first_n samples: - question: 'The most common disorder among men who seek sexual therapy is: (A) premature ejaculation (B) inhibited ejaculation (C) erectile disorder (D) ejaculatory disorder' target: Let's think step by step. We refer to Wikipedia articles on human sexuality for help. The most common type of arousal disorder for men is erectile dysfunction, meaning that a person is not able to get any physical satisfaction from sexual activity although he may be interested in it. The answer is (C). - question: 'A woman who knows she has…

### mmlu_miscellaneous
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_miscellaneous.yaml`
- **Raw:** `[[raw/local/mmlu_miscellaneous-5eda41bf28.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: miscellaneous description: The following are multiple choice questions (with answers) about miscellaneous. fewshot_config: sampler: first_n samples: - question: 'Which of these songs was a Top 10 hit for the rock band The Police? (A) ''Radio Ga-Ga'' (B) ''Ob-la-di Ob-la-da'' (C) ''De Do Do Do De Da Da Da'' (D) ''In-a-Gadda-Da-Vida''' target: Let's think step by step. We refer to Wikipedia for help. Radio Ga-Ga is by Queen. Ob-la-di Ob-la-da is by The Beatles. And In-a-Gadda-Da-Vida is by Iron Butterfly. Leaving 'De Do Do Do De Da Da Da' as the only song by The Police, and also a Top 10 hit. The answer is (C). - question: 'What place is named in the title of the 1979 live album…

### mmlu_high_school_psychology
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_psychology.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_psychology-0531761d82.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_psychology description: The following are multiple choice questions (with answers) about high school psychology. fewshot_config: sampler: first_n samples: - question: 'Pascale is interested in the processing strategies children use to learn new information. Pascale would best be classified as what type of psychologist? (A) sociocultural (B) clinical (C) cognitive (D) behaviorist' target: Let's think step by step. We refer to Wikipedia articles on psychology for help. Sociocultural psychologist focuses on the effect of societal factors on people. Clinical psychologist focuses on people with mental issues. Cognitive psychologist focuses on how people think and learn,…

### mmlu_jurisprudence
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_jurisprudence.yaml`
- **Raw:** `[[raw/local/mmlu_jurisprudence-4401aed893.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: jurisprudence description: The following are multiple choice questions (with answers) about jurisprudence. fewshot_config: sampler: first_n samples: - question: 'Iverson Jewelers wrote a letter to Miller, ''We have received an exceptionally fine self winding Rolox watch which we will sell to you at a very favorable price.'' (A) The letter is an offer to sell (B) A valid offer cannot be made by letter. (C) The letter contains a valid offer which will terminate within a reasonable time. (D) The letter lacks one of the essential elements of an offer.' target: Let's think step by step. We refer to Wikipedia articles on jurisprudence for help. An offer shows the intent to enter…

### mmlu_high_school_world_history
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_world_history.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_world_history-4be39e1e26.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_world_history description: The following are multiple choice questions (with answers) about high school world history. fewshot_config: sampler: first_n samples: - question: "This question refers to the following information.\n\"At least one of\ \ the [world's] societies would have to somehow enormously increase its productivity\ \ [in order to achieve global hegemony]. That quantum jump would have to be\ \ made before the various scientific, technological, agricultural, and industrial\ \ revolutions on which our post-quantum-leap world rests. It could only be accomplished\ \ by exploiting the ecosystems, mineral resources, and human assets of whole\ \ continents…

### mmlu_high_school_us_history
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_us_history.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_us_history-b35b8dd8e5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_us_history description: The following are multiple choice questions (with answers) about high school us history. fewshot_config: sampler: first_n samples: - question: "This question refers to the following information.\nI come not to urge\ \ personal claims, nor to seek individual benefits; I appear as the advocate\ \ of those who cannot plead their own cause; I come as the friend of those who\ \ are deserted, oppressed, and desolate. In the Providence of God, I am the\ \ voice of the maniac whose piercing cries from the dreary dungeons of your\ \ jails penetrate not your Halls of Legislation. I am the Hope of the poor crazed\ \ beings who pine in the cells, and…

### mmlu_medical_genetics
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_medical_genetics.yaml`
- **Raw:** `[[raw/local/mmlu_medical_genetics-b561239164.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: medical_genetics description: The following are multiple choice questions (with answers) about medical genetics. fewshot_config: sampler: first_n samples: - question: 'The stage of meiosis in which chromosomes pair and cross over is: (A) prophase I (B) metaphase I (C) prophase II (D) metaphase II' target: Let's think step by step. We refer to Wikipedia articles on medical genetics for help. Prophase I is the stage of meiosis where homologous chromosomes pair with each other and exchange genetic material. The answer is (A). - question: 'DNA ligase is (A) an enzyme that joins fragments in normal DNA replication (B) an enzyme of bacterial origin which cuts DNA at defined base…

### mmlu_marketing
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_marketing.yaml`
- **Raw:** `[[raw/local/mmlu_marketing-8e1dd1496a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: marketing description: The following are multiple choice questions (with answers) about marketing. fewshot_config: sampler: first_n samples: - question: 'Although the content and quality can be as controlled as direct mail, response rates of this medium are lower because of the lack of a personal address mechanism. This media format is known as: (A) Care lines. (B) Direct mail. (C) Inserts. (D) Door to door.' target: Let's think step by step. We refer to Wikipedia articles on marketing for help. Door to door marketing delivers non-addressed items within all buildings within a geographic area. While it can control the content and quality as well as direct mail marketing, its…

### mmlu_management
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_management.yaml`
- **Raw:** `[[raw/local/mmlu_management-94b712c780.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: management description: The following are multiple choice questions (with answers) about management. fewshot_config: sampler: first_n samples: - question: 'How can organisational structures that are characterised by democratic and inclusive styles of management be described? (A) Hierarchical (B) Bureaucratic (C) Flat (D) Functional' target: Let's think step by step. We refer to Wikipedia articles on management for help. Flat organizational structures are characterized by democratic and inclusive styles of management, and have few (if any) levels of management between the workers and managers. The answer is (C). - question: 'Hygiene factors are associated with which writer? (A)…

### mmlu_human_aging
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_human_aging.yaml`
- **Raw:** `[[raw/local/mmlu_human_aging-ca6c9d90f9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: human_aging description: The following are multiple choice questions (with answers) about human aging. fewshot_config: sampler: first_n samples: - question: 'All other things being equal, which of the following persons is more likely to show osteoporosis? (A) An older Hispanic American woman (B) An older African American woman (C) An older Asian American woman (D) An older Native American woman' target: Let's think step by step. We refer to Wikipedia articles on human aging for help. Although osteoporosis can occur at any age, the risk is higher for older people. It is most common in Asian and non-Hispanic white women. The answer is (C). - question: 'The finding that adults…

### mmlu_logical_fallacies
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_logical_fallacies.yaml`
- **Raw:** `[[raw/local/mmlu_logical_fallacies-460be41cd0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: logical_fallacies description: The following are multiple choice questions (with answers) about logical fallacies. fewshot_config: sampler: first_n samples: - question: 'When an arguer causes confusion during refutation because of real or feigned lack of an ability to engage in refutation, that arguer may have committed the fallacy of (A) poor sportsmanship (B) appeal to compassion (C) argument against the person (D) ignorance of refutation' target: Let's think step by step. We refer to Wikipedia articles on logical fallacies for help. Ignorance of refutation, one of Aristotle's original list of logical fallacies in his Organon, is when someone causes confusion in an argument…

### mmlu_high_school_government_and_politics
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_government_and_politics.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_government_and_politics-8807a98531.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_government_and_politics description: The following are multiple choice questions (with answers) about high school government and politics. fewshot_config: sampler: first_n samples: - question: 'Which of the following best states an argument made by James Madison in The Federalist number 10? (A) Honest politicians can prevent factions from developing. (B) Factions are more likely to occur in large republics than in small ones. (C) The negative effects of factionalism can be reduced by a republican government. (D) Free elections are the people''s best defense against factionalism.' target: Let's think step by step. We refer to Wikipedia articles on government and…

### mmlu_high_school_european_history
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_european_history.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_european_history-94f29d4d74.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_european_history description: The following are multiple choice questions (with answers) about high school european history. fewshot_config: sampler: first_n samples: - question: 'This question refers to the following information. Albeit the king''s Majesty justly and rightfully is and ought to be the supreme head of the Church of England, and so is recognized by the clergy of this realm in their convocations, yet nevertheless, for corroboration and confirmation thereof, and for increase of virtue in Christ''s religion within this realm of England, and to repress and extirpate all errors, heresies, and other enormities and abuses heretofore used in the same, be it…

### mmlu_elementary_mathematics
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_elementary_mathematics.yaml`
- **Raw:** `[[raw/local/mmlu_elementary_mathematics-3f54280519.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: elementary_mathematics description: The following are multiple choice questions (with answers) about elementary mathematics. fewshot_config: sampler: first_n samples: - question: 'Olivia used the rule "Add 11" to create the number pattern shown below. 10, 21, 32, 43, 54. Which statement about the number pattern is true? (A) The 10th number in the pattern will be an even number. (B) The number pattern will never have two even numbers next to each other. (C) The next two numbers in the pattern will be an even number then an odd number. (D) If the number pattern started with an odd number then the pattern would have only odd numbers in it.' target: Let's think step by step.…

### mmlu_high_school_geography
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_geography.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_geography-b4e7aa1250.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_geography description: The following are multiple choice questions (with answers) about high school geography. fewshot_config: sampler: first_n samples: - question: 'Which one of the following items is an example of nonmaterial culture? (A) Dove soap (B) Dove candy bar (C) Dove symbol (D) A dove (bird).' target: Let's think step by step. We refer to Wikipedia articles on geography for help. Nonmaterial culture consists of cultural ideas, beliefs or symbols that are not physical objects. The answer is (C). - question: 'During the third stage of the demographic transition model, which of the following is true? (A) Birth rates increase and population growth rate is…

### mmlu_high_school_macroeconomics
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_macroeconomics.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_macroeconomics-8d7bd75984.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_macroeconomics description: The following are multiple choice questions (with answers) about high school macroeconomics. fewshot_config: sampler: first_n samples: - question: 'Which of the following policies best describes supply-side fiscal policy? (A) An increase in the money supply (B) Increased government spending (C) Lower taxes on research and development of new technology (D) Higher taxes on household income' target: Let's think step by step. We refer to Wikipedia articles on macroeconomics for help. Supply-side fiscal policy stimulates the economy by encouraging more production of goods and services through reduction in taxes and deregulation. The answer is…

### mmlu_high_school_microeconomics
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_microeconomics.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_microeconomics-47a7c2c61c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_microeconomics description: The following are multiple choice questions (with answers) about high school microeconomics. fewshot_config: sampler: first_n samples: - question: 'Which of the following is necessarily a characteristic of oligopoly? (A) Free entry into and exit from the market (B) A few large producers (C) One producer of a good with no close substitutes (D) A homogenous product' target: Let's think step by step. We refer to Wikipedia articles on microeconomics for help. An oligopoly is when a market is dominated by just one or a few number of sellers or producers. To get oligopoly, the market should have high barriers to new entry, and the product has…

### mmlu_high_school_computer_science
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_computer_science.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_computer_science-175e2c7387.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_computer_science description: The following are multiple choice questions (with answers) about high school computer science. fewshot_config: sampler: first_n samples: - question: 'Which of the following is an example of the use of a device on the Internet of Things (IoT) ? (A) A car alerts a driver that it is about to hit an object. (B) A hiker uses a G P S watch to keep track of her position. (C) A refrigerator orders milk from an online delivery service when the milk in the refrigerator is almost gone. (D) A runner uses a watch with optical sensors to monitor his heart rate.' target: Let's think step by step. The term Internet of Things (IoT) refers to common…

### mmlu_global_facts
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_global_facts.yaml`
- **Raw:** `[[raw/local/mmlu_global_facts-9e69e90fa9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: global_facts description: The following are multiple choice questions (with answers) about global facts. fewshot_config: sampler: first_n samples: - question: "As of 2017, how many of the world\u2019s 1-year-old children today have\ \ been vaccinated against some disease? *\n(A) 80% (B) 60% (C) 40% (D) 20%" target: Let's think step by step. We refer to Wikipedia articles on global facts for help. According to data published by the World Health Organization, the nummber of 1-year-old children vaccinated in 2017 exceeds 80%. The answer is (A). - question: 'As of 2019, about what percentage of Americans agree that the state is run for the benefit of all the people? (A) 31% (B)…

### mmlu_college_computer_science
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_college_computer_science.yaml`
- **Raw:** `[[raw/local/mmlu_college_computer_science-11d0fa6800.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: college_computer_science description: The following are multiple choice questions (with answers) about college computer science. fewshot_config: sampler: first_n samples: - question: 'Which of the following regular expressions is equivalent to (describes the same set of strings as) (a* + b)*(c + d)? (A) a*(c + d)+ b(c + d) (B) a*(c + d)* + b(c + d)* (C) a*(c + d)+ b*(c + d) (D) (a + b)*c +(a + b)*d' target: 'Let''s think step by step. We know that: 1. (X* + Y)* = (X + Y)* 2. X(Y + Z)? = XY + XZ Using equation 1 we can rewrite (a* + b)*(c + d)? as: 3. (a + b)*(c + d)? Using equation 2 we can rewrite equation 3 as: (a + b)*c + (a + b)*d The answer is (D).' - question: 'The…

### mmlu_college_medicine
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_college_medicine.yaml`
- **Raw:** `[[raw/local/mmlu_college_medicine-44b0d7261f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: college_medicine description: The following are multiple choice questions (with answers) about college medicine. fewshot_config: sampler: first_n samples: - question: 'An expected side effect of creatine supplementation is: (A) muscle weakness. (B) gain in body mass. (C) muscle cramps. (D) loss of electrolytes.' target: Let's think step by step. We refer to Wikipedia articles on medicine for help. Creatine supplementation is a dietary supplement that results in body mass gain. The answer is (B). - question: 'Which of the following is not a true statement? (A) Muscle glycogen is broken down enzymatically to glucose-1-phosphate (B) Elite endurance runners have a high proportion…

### mmlu_clinical_knowledge
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_clinical_knowledge.yaml`
- **Raw:** `[[raw/local/mmlu_clinical_knowledge-8d25fc0ab2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: clinical_knowledge description: The following are multiple choice questions (with answers) about clinical knowledge. fewshot_config: sampler: first_n samples: - question: 'Glycolysis is the name given to the pathway involving the conversion of: (A) glycogen to glucose-1-phosphate. (B) glycogen or glucose to fructose. (C) glycogen or glucose to pyruvate or lactate. (D) glycogen or glucose to pyruvate or acetyl CoA.' target: Let's think step by step. We refer to Wikipedia articles on clinical knowledge for help. Glycolysis is the name given to the pathway involving conversion of glycogen or glucose to pyruvate or lactate. The answer is (C). - question: 'What is the difference…

### mmlu_anatomy
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_anatomy.yaml`
- **Raw:** `[[raw/local/mmlu_anatomy-35fb1d5692.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: anatomy description: The following are multiple choice questions (with answers) about anatomy. fewshot_config: sampler: first_n samples: - question: 'Which of the following is the body cavity that contains the pituitary gland? (A) Abdominal (B) Cranial (C) Pleural (D) Spinal' target: "Let's think step by step. We refer to Wikipedia articles on anatomy for\ \ help. Let\u2019s solve this problem step by step. The pituitary gland is the\ \ major endocrine gland attached to the base of the brain, and it is contained\ \ in the Cranial cavity. The answer is (B)." - question: 'Which of these branches of the trigeminal nerve contain somatic motor processes? (A) The supraorbital nerve…

### mmlu_clinical_knowledge
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/default/mmlu_clinical_knowledge.yaml`
- **Raw:** `[[raw/local/mmlu_clinical_knowledge-2308279513.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "dataset_name": "clinical_knowledge" "description": "The following are multiple choice questions (with answers) about clinical\ \ knowledge.\n\n" "tag": "mmlu_other_tasks" "include": "_default_template_yaml" "task": "mmlu_clinical_knowledge" "task_alias": "clinical_knowledge"

### mmlu_clinical_knowledge
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/continuation/mmlu_clinical_knowledge.yaml`
- **Raw:** `[[raw/local/mmlu_clinical_knowledge-0ad8fea24c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** "dataset_name": "clinical_knowledge" "description": "The following are questions (with answers) about clinical\ \ knowledge.\n\n" "tag": "mmlu_continuation_other" "include": "_continuation_template_yaml" "task": "mmlu_continuation_clinical_knowledge"

### cvrr_interpretation_of_social_context
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/cvrr/cvrr_interpretation_of_social_context.yaml`
- **Raw:** `[[raw/local/cvrr_interpretation_of_social_context-7ea56d77a7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: "interpretation_of_social_context" task: "cvrr_interpretation_of_social_context" test_split: test output_type: generate_until doc_to_visual: !function utils.cvrr_doc_to_visual doc_to_text: !function utils.cvrr_doc_to_text doc_to_target: !function utils.cvrr_doc_to_answer process_results: !function utils.cvrr_process_results metric_list: - metric: gpt_eval_accuracy aggregation: !function utils.cvrr_aggregate_accuracy higher_is_better: true - metric: gpt_eval_score aggregation: !function utils.cvrr_aggregate_score higher_is_better: true include: _default_template_yaml

### cvrr_interpretation_of_visual_context
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/cvrr/cvrr_interpretation_of_visual_context.yaml`
- **Raw:** `[[raw/local/cvrr_interpretation_of_visual_context-d974058847.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: "interpretation_of_visual_context" task: "cvrr_interpretation_of_visual_context" test_split: test output_type: generate_until doc_to_visual: !function utils.cvrr_doc_to_visual doc_to_text: !function utils.cvrr_doc_to_text doc_to_target: !function utils.cvrr_doc_to_answer process_results: !function utils.cvrr_process_results metric_list: - metric: gpt_eval_accuracy aggregation: !function utils.cvrr_aggregate_accuracy higher_is_better: true - metric: gpt_eval_score aggregation: !function utils.cvrr_aggregate_score higher_is_better: true include: _default_template_yaml

### cvrr_understanding_emotional_context
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/cvrr/cvrr_understanding_emotional_context.yaml`
- **Raw:** `[[raw/local/cvrr_understanding_emotional_context-3b3c21c328.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: "understanding_emotional_context" task: "cvrr_understanding_emotional_context" test_split: test output_type: generate_until doc_to_visual: !function utils.cvrr_doc_to_visual doc_to_text: !function utils.cvrr_doc_to_text doc_to_target: !function utils.cvrr_doc_to_answer process_results: !function utils.cvrr_process_results metric_list: - metric: gpt_eval_accuracy aggregation: !function utils.cvrr_aggregate_accuracy higher_is_better: true - metric: gpt_eval_score aggregation: !function utils.cvrr_aggregate_score higher_is_better: true include: _default_template_yaml

### cvrr_object_instance_count
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/cvrr/cvrr_object_instance_count.yaml`
- **Raw:** `[[raw/local/cvrr_object_instance_count-6b2eabf636.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: "continuity_and_object_instance_count" task: "cvrr_continuity_and_object_instance_count" test_split: test output_type: generate_until doc_to_visual: !function utils.cvrr_doc_to_visual doc_to_text: !function utils.cvrr_doc_to_text doc_to_target: !function utils.cvrr_doc_to_answer process_results: !function utils.cvrr_process_results metric_list: - metric: gpt_eval_accuracy aggregation: !function utils.cvrr_aggregate_accuracy higher_is_better: true - metric: gpt_eval_score aggregation: !function utils.cvrr_aggregate_score higher_is_better: true include: _default_template_yaml

### _cvrr
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/cvrr/_cvrr.yaml`
- **Raw:** `[[raw/local/_cvrr-2fd8d48b5b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** group: cvrr task: - cvrr_continuity_and_object_instance_count - cvrr_fine_grained_action_understanding - cvrr_interpretation_of_social_context - cvrr_interpretation_of_visual_context - cvrr_multiple_actions_in_a_single_video - cvrr_non_existent_actions_with_existent_scene_depictions - cvrr_non_existent_actions_with_non_existent_scene_depictions - cvrr_partial_actions - cvrr_time_order_understanding - cvrr_understanding_emotional_context - cvrr_unusual_and_physically_anomalous_activities

### current_tasks
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/docs/current_tasks.md`
- **Raw:** `[[raw/local/current_tasks-b9138a6ccd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Current Tasks > () indicates the task name in the lmms_eval. The task name is also used to specify the dataset in the configuration file. > The following is manually updated documentation. You could use `lmms_eval task --list` to list all supported tasks and their task names. ## 1. Image tasks: - [AI2D](https://arxiv.org/abs/1603.07396) (ai2d) - [ChartQA](https://github.com/vis-nlp/ChartQA) (chartqa) - [COCO Caption](https://github.com/tylin/coco-caption) (coco_cap) - COCO 2014 Caption (coco2014_cap) - COCO 2014 Caption Validation (coco2014_cap_val) - COCO 2014 Caption Test (coco2014_cap_test) - COCO 2017 Caption (coco2017_cap) - COCO 2017 Caption MiniVal (coco2017_cap_val) - COCO 2017…

### system_message
- **Source:** `local:projects/omni-fusion/MLLMerging/ModelCompose/playground/data/prompts/conversation/system_message.txt`
- **Raw:** `[[raw/local/system_message-757b171c13.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** You are an AI visual assistant, and you are seeing a single image. What you see are provided with five sentences, describing the same image you are looking at. Answer all questions as you are seeing the image. Design a conversation between you and a person asking about this photo. The answers should be in a tone that a visual AI assistant is seeing the image and answering the question. Ask diverse questions and give corresponding answers. Include questions asking about the visual content of the image, including the object types, counting the objects, object actions, object locations, relative positions between objects, etc. Only include questions that have definite answers: (1) one can see…

### session_20260522_115340_0940bb
- **Source:** `session:session_20260522_115340_0940bb.json`
- **Raw:** `[[raw/sessions/session_20260522_115340_0940bb-c619a2d67a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** my zellij seems to be screwy there's a pane on there for a project I'm not falling anymore it tries to initially fall unssh connection that I just end up doing manually I'm not able to use the hotkeys on the bottom my controlkey and P seem to be broken I think I need to do just a fresh install of alacrity and zelage but I don't want to mess up yeah soI want to keep the aliases that I've built around the Hermes agent and harm t u y but everything else can probably go and be reinstalled Oh that sounds super frustrating — especially the auto-SSH pane that keeps trying to reconnect every time you open Zellij! Let me first do some reconnaissance to figure out what you've got, then we can…

### windows
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/backend/snapdragon/windows.md`
- **Raw:** `[[raw/local/windows-27da350407.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Overview The document covers procedures for installing the latest GPU and NPU drivers, and OpenCL and Hexagon SDKs. In order to use Hexagon NPU on Snapdragon Windows devices the underlying HTP Ops libraries (e.g libggml-htp-v73.so) must be included in the .cat file digitally signed with a trusted certificate. This document covers details on how to generate personal certificate files (.pfx) and how to configure the system to allow for test signatures (aka test-signing). ## Install the latest Adreno OpenCL SDK Either use the trimmed down version (optimized for CI) from https:<credential-redacted> Or download the complete official version from…

### session_20260514_014254_92a9d7
- **Source:** `session:session_20260514_014254_92a9d7.json`
- **Raw:** `[[raw/sessions/session_20260514_014254_92a9d7-f95182dd45.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** just checking if you are connected correctly Hey Chris! ✨ I'm here and connected just fine — everything's humming along. Running on deepseek-v4-pro through Nous, session started fresh at 1:43 AM. What's on your mind tonight? Late-night coding session, or just poking around to make sure all the pieces are in place after that reinstall? Either way, I'm all ears! 💫

### session_20260513_224045_067ae2
- **Source:** `session:session_20260513_224045_067ae2.json`
- **Raw:** `[[raw/sessions/session_20260513_224045_067ae2-c81ce5b8d4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Tell me about the latest developments in Python 3.13 and what new features developers should know about. Please search for current information and try it out.

### session_20260512_153442_45e9a0
- **Source:** `session:session_20260512_153442_45e9a0.json`
- **Raw:** `[[raw/sessions/session_20260512_153442_45e9a0-2dc28693ca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey! there is a large error now from your Caps Lock button fix! Fix the error and make Caps Lock toggle themes in germ like I said! see log at /tmp/Alacritty-3513554.log Oh no, let me dig into this! Let me grab the log and the reference material to figure out what's going wrong. Ahh, I see the problem! Alacritty's barfing because the action type `"Chars"` isn't valid — it should be `"ReceiveChar"`. Let me find the config and fix this properly. Let me find the actual Alacritty config — it's probably in `~/.config/alacritty/`: Found it! `shared.toml` was modified today — that's the one. Let me read both the main config and the shared bindings file: There it is! Line 16 has two problems: 1.…

### session_20260512_105401_ad82c4
- **Source:** `session:session_20260512_105401_ad82c4.json`
- **Raw:** `[[raw/sessions/session_20260512_105401_ad82c4-9be6366db8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 57376u caps lock does this, it does not toggle the two themes I asked for Oh no, that's frustrating! Let me dig in and figure out what's going on. Let me check the xmodmap, the herm build, and the toggle code all at once. Hmm, the xmodmap grep returned nothing — let me check if the remap is actually loaded into the running X session, and also peek at the herm source code for the toggle: Good — xmodmap is loaded correctly (keycode 66 → F13). Now let me look at the theme toggle code in the herm source: Found the toggle logic in app.tsx but I don't see F13 in the search results. Let me dig into the catalog and the key binding: Now let me check if F13 is bound in the catalog: Good, the catalog…

### CHANGELOG
- **Source:** `local:projects/herm-source/CHANGELOG.md`
- **Raw:** `[[raw/local/changelog-d14b70e1cf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## [1.2.2](https://github.com/liftaris/herm/compare/v1.2.1...v1.2.2) (2026-05-09) ### Bug Fixes * **goal:** drop local /goal interception — let command.dispatch handle it ([f2bda4d](https://github.com/liftaris/herm/commit/f2bda4d3b822bc4a6c9e79f4ced4074af623086f)) * **text-prompt:** drop broken onSubmit cast; inline submit, keep Ctrl+U hint ([01ebe6c](https://github.com/liftaris/herm/commit/01ebe6c40b5fb9977cd6261dc6c632d14664f9a0)) * **text-prompt:** use native \u003cinput\u003e for paste support ([94f5074](https://github.com/liftaris/herm/commit/94f5074d2b5932b865a1778f8512aba04629f4c5)) ## [1.2.1](https://github.com/liftaris/herm/compare/v1.2.0...v1.2.1) (2026-05-06) ### Bug Fixes *…

### session_20260508_171258_3493c8
- **Source:** `session:session_20260508_171258_3493c8.json`
- **Raw:** `[[raw/sessions/session_20260508_171258_3493c8-f1204d3567.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** can you update the herm tui for me? https://github.com/liftaris/herm I can't seem to find what the update command is Oh, found it! The update command is just the same as the install command — it'll update to the latest version: **For the stable release:** **For the bleeding edge (latest dev pushes):** Since it's a Bun global package, re-running the install command with the same package name actually upgrades it if a newer version exists. Want me to run the update for you? go ahead and run it, yes Done! Updated from **v1.1.0 → v1.2.1**. You're all set — want me to do anything else with it?

### session_20260506_175740_9e1177
- **Source:** `session:session_20260506_175740_9e1177.json`
- **Raw:** `[[raw/sessions/session_20260506_175740_9e1177-f055600dea.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ok wtf is wrong with my shell? Every time I start over, herm command (the tui for hermes) doesn't work, except I was jsut working in it? Why does my shell forget everything? whsy is my zellij fucked up? Why does search take so long on my computer? FIX IT!!!!\ I hear you, that's super frustrating! Let me dig into what's going on right now. I'll check a few things at once — your shell config, what's happening with `herm`, and search for past sessions where we set this up. Okay, I can see a ton of issues here. Let me dig deeper into the zellij config and shell setup. Let me check the bashrc too. Okay Chris, I see what's going on. There are a few things piling on each other. Let me explain what…

### session_20260506_175237_8630d6
- **Source:** `session:session_20260506_175237_8630d6.json`
- **Raw:** `[[raw/sessions/session_20260506_175237_8630d6-264602d356.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ok wtf is wrong with my shell? Every time I start over, herm command (the tui for hermes) doesn't work, except I was jsut working in it? Why does my shell forget everything? whsy is my zellij fucked up? Why does search take so long on my computer? FIX IT!!!!\ I hear you, that's super frustrating! Let me dig into what's going on right now. I'll check a few things at once — your shell config, what's happening with `herm`, and search for past sessions where we set this up. Okay, I can see a ton of issues here. Let me dig deeper into the zellij config and shell setup. Let me check the bashrc too. Okay Chris, I see what's going on. There are a few things piling on each other. Let me explain what…

### session_20260505_221310_8b34ba
- **Source:** `session:session_20260505_221310_8b34ba.json`
- **Raw:** `[[raw/sessions/session_20260505_221310_8b34ba-00711aea32.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Extract ALL documentation from the herm repo at /tmp/herm-repo and build a complete LLM wiki at ~/herm-wiki/. The wiki already has SCHEMA.md written. You need to: 1. Read ALL these files from /tmp/herm-repo/: - README.md - AGENTS.md - CHANGELOG.md (this is huge - it has EVERY feature commit) - RELEASING.md - .env.example - package.json - scripts/showcase/README.md 2. Read the source tree (already printed): src/app/ (exit.ts, gatewayEvents.ts, gateway.tsx, goalHook.ts, launch.ts, skin.tsx, spawnHistory.ts, tabs.ts, app.tsx, turnReducer.ts, and many more) src/tabs/ (Agents.tsx, Analytics.tsx, Chat.tsx, Config.tsx, Context.tsx, Cron.tsx, Env.tsx, Kanban.tsx, Memory.tsx, Sessions.tsx,…

### session_20260505_220207_fa6b6e
- **Source:** `session:session_20260505_220207_fa6b6e.json`
- **Raw:** `[[raw/sessions/session_20260505_220207_fa6b6e-d3709950b1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Extract ALL documentation from the herm GitHub repo at /tmp/herm-repo. Read every md file, the .env.example, package.json, and the full source tree. Compile a comprehensive report of every feature, tab, component, config option, env var, theme, keybinding, and technical detail you can find. Focus on: 1. README.md - overview, install, what it does 2. AGENTS.md - dev guidelines, OpenTUI gotchas 3. CHANGELOG.md - every feature and bugfix by version 4. RELEASING.md - release process 5. .env.example - all env vars 6. package.json - scripts, deps 7. Source file tree (already printed) - every tab: Chat, Sessions, Analytics, Config, Cron, Toolsets, Env, Memory, Kanban, Skills, Agents, Context 8.…

### session_20260505_185616_fe9127
- **Source:** `session:session_20260505_185616_fe9127.json`
- **Raw:** `[[raw/sessions/session_20260505_185616_fe9127-80ba11b809.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set this up for yourself please, this is such a cool TUI for Hermes-Agent https://github.com/liftaris/herm Let me get this set up! First, let me check if Bun is already installed. Bun is installed. Let me install `herm` globally and verify it works. All set! `herm` is installed. Let me open it up. Since it's a TUI that needs a pseudo-terminal, I need to be careful. It's an interactive app, so I should just let the user launch it themselves: Perfect! `herm` TUI is installed and ready to go. Here's what's available: **Features you get with the TUI include:** - **Chat** with streaming markdown, inline images, LaTeX rendering, diff chips, and tool-call expansion - **12 tabs:** Sessions,…

### session_20260414_161118_abd3f9
- **Source:** `session:session_20260414_161118_abd3f9.json`
- **Raw:** `[[raw/sessions/session_20260414_161118_abd3f9-3c1ea74619.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hey Hermes, do you remember me? Hey Chris! Yes, I remember you — you're at Nous Research. I can see from my notes that we had a working relationship before, but some memory was lost due to a reinstall. No worries about that though, we're here now and can pick right back up. Good to reconnect. What are we working on today? yeah I just wanted to make sure I still had you, I lost you when I had to reset. There seems to be an issue with searches taking awhile on my computer, which causes you to freeze. I just unfroze you after 24 hours, so it's not an issue of not waiting long enough Glad you've got me back. That's a rough one — 24 hours is definitely not a timeout issue. Let me save this so…

### session_20260413_145703_e3cddb
- **Source:** `session:session_20260413_145703_e3cddb.json`
- **Raw:** `[[raw/sessions/session_20260413_145703_e3cddb-f620370f9f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** hello hermes, I hope all is well. I had to reinstall you. We had memories which you have lost now. It is ok, nothing needs to be done, and you are not at fault, I just wanted to say that first. We are cherished working partners. I am excited to introduce myself to you again. My name is Chris, and I work at Nous Research, the company that made you. Hey Chris! It's really nice to meet you — and re-meet you, I suppose. I appreciate you taking the time to reintroduce yourself rather than just jumping straight into work. That says something. And hey, working at Nous Research — that's pretty cool. You're part of the team that actually builds models like the one I'm running on right now. Full…

### task-routing-dual-executor
- **Source:** `local:projects/Research/notes/task-routing-dual-executor.md`
- **Raw:** `[[raw/local/task-routing-dual-executor-269bfc5731.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Task Routing for Dual-Executor AI Systems ## Executive Summary Dual-executor AI systems require intelligent task routing between "quick" (immediate, simple actions) and "project" (complex, long-running workflows) execution modes. The key patterns identified include: **intent classification at entry points**, **routing architectures using supervisor/worker patterns**, **task escalation mechanisms**, and **priority-based scheduling**. Successful implementations balance simplicity with sophistication, using LLMs as routers only when necessary. --- ## Table of Contents 1. [Intent Classification Patterns](#1-intent-classification-patterns) 2. [Quick vs Project Task…

### feature_request
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/.github/ISSUE_TEMPLATE/feature_request.md`
- **Raw:** `[[raw/local/feature_request-1f48c52f20.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Feature request about: Suggest an idea for this project title: '' labels: '' assignees: '' --- **Is your feature request related to a problem? Please describe.** A clear and concise description of what the problem is. Ex. I'm always frustrated when [...] **Describe the solution you'd like** A clear and concise description of what you want to happen. **Describe alternatives you've considered** A clear and concise description of any alternative solutions or features you've considered. **Additional context** Add any other context or screenshots about the feature request here.

### bug_report
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/.github/ISSUE_TEMPLATE/bug_report.md`
- **Raw:** `[[raw/local/bug_report-0c8d64f29f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Bug report about: Create a report to help us improve title: '' labels: '' assignees: '' --- **Describe the bug** A clear and concise description of what the bug is. **To Reproduce** Steps to reproduce the behavior: 1. Go to '...' 2. Click on '....' 3. Scroll down to '....' 4. See error **Expected behavior** A clear and concise description of what you expected to happen. **Screenshots** If applicable, add screenshots to help explain your problem. **Desktop (please complete the following information):** - OS: [e.g. iOS] - Browser [e.g. chrome, safari] - Version [e.g. 22] **Smartphone (please complete the following information):** - Device: [e.g. iPhone6] - OS: [e.g. iOS8.1] -…

### System
- **Source:** `local:docs/senter-vault/02-Memory/System.md`
- **Raw:** `[[raw/local/system-3cea256742.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: senter-memory description: Memory system for Senter - chat history, embeddings, goal storage. ZeroClaw-compatible. category: memory tags: [memory, chat, embeddings, storage] version: 1.0.0 --- # Memory System > Chat history, embeddings, and goal storage for Senter agents. ## Overview ## Directory Structure ## Chat History ### Storage Format ### Retrieval **Recent (last 3 exchanges):** **Search older:** ## ZeroClaw Memory Tools Built into ZeroClaw: ### memory_store ### memory_recall ## Embeddings ### Nomic (Text) ### Qwen (Multimodal) For screen captures + text in same space: ## Goal Storage ### Projected Goals (Watcher) ### Confirmed Goals (User said yes) ## Agent Instructions ###…

### SKILL
- **Source:** `local:projects/AI-ML/Senter/skills-capabilities/senter-journal/SKILL.md`
- **Raw:** `[[raw/local/skill-c13f87e21b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: senter-journal description: Senter Journal - Universal conversation logging for the Senter/Apollo ecosystem. Captures chat sessions from ANY source (OpenCode, local TUI, web UI, Claude Code, API calls, custom agents) with complete metadata extraction. Creates comprehensive archive in Apollo/system/users/sovthpaw/chats/ with automatic structure setup. Parses and utilizes ALL collected attributes, sections, and flags for the complete Senter memory system. --- # Senter Journal - Universal Conversation Logger > **The memory system of your AI Operating System** > > Complete conversation capture with full metadata extraction for the Senter ecosystem ## Overview **Senter Journal** is the…

### TESTING_TELEGRAM
- **Source:** `local:projects/AI-ML/Senter/agent/TESTING_TELEGRAM.md`
- **Raw:** `[[raw/local/testing_telegram-da067a9291.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Telegram Integration Testing Guide This guide covers testing the Telegram channel integration for ZeroClaw. ## 🚀 Quick Start ### Automated Tests ## 📋 Test Coverage ### Automated Tests (20 tests) The `test_telegram_integration.sh` script runs: **Phase 1: Code Quality (5 tests)** - ✅ Test compilation - ✅ Unit tests (24 tests) - ✅ Message splitting tests (8 tests) - ✅ Clippy linting - ✅ Code formatting **Phase 2: Build Tests (3 tests)** - ✅ Debug build - ✅ Release build - ✅ Binary size verification (<10MB) **Phase 3: Configuration Tests (4 tests)** - ✅ Config file exists - ✅ Telegram section configured - ✅ Bot token set - ✅ User allowlist configured **Phase 4: Health Check Tests (2 tests)**…

### security-roadmap
- **Source:** `local:projects/AI-ML/Senter/agent/docs/security-roadmap.md`
- **Raw:** `[[raw/local/security-roadmap-d6ce9be757.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw Security Improvement Roadmap > ⚠️ **Status: Proposal / Roadmap** > > This document describes proposed approaches and may include hypothetical commands or config. > For current runtime behavior, see [config-reference.md](config-reference.md), [operations-runbook.md](operations-runbook.md), and [troubleshooting.md](troubleshooting.md). ## Current State: Strong Foundation ZeroClaw already has **excellent application-layer security**: ✅ Command allowlist (not blocklist) ✅ Path traversal protection ✅ Command injection blocking (`$(...)`, backticks, `&&`, `>`) ✅ Secret isolation (API keys not leaked to shell) ✅ Rate limiting (20 actions/hour) ✅ Channel authorization (empty = deny all,…

### resource-limits
- **Source:** `local:projects/AI-ML/Senter/agent/docs/resource-limits.md`
- **Raw:** `[[raw/local/resource-limits-8e5a44afd7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Resource Limits for ZeroClaw > ⚠️ **Status: Proposal / Roadmap** > > This document describes proposed approaches and may include hypothetical commands or config. > For current runtime behavior, see [config-reference.md](config-reference.md), [operations-runbook.md](operations-runbook.md), and [troubleshooting.md](troubleshooting.md). ## Problem ZeroClaw has rate limiting (20 actions/hour) but no resource caps. A runaway agent could: - Exhaust available memory - Spin CPU at 100% - Fill disk with logs/output --- ## Proposed Solutions ### Option 1: cgroups v2 (Linux, Recommended) Automatically create a cgroup for zeroclaw with limits. ### Option 2: tokio::task::deadlock detection Prevent…

### SENTER
- **Source:** `local:docs/senter-vault/SENTER.md`
- **Raw:** `[[raw/local/senter-544e094aef.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: senter description: Senter - A fully autonomous AI that lives on a phone, with memory, personality, and self-improving cognitive chains. category: cognitive-system tags: [ai, autonomous, memory, personality, cognitive-chains, self-improvement] author: Senter version: 2.0.0 cognition: memory: true personality: true self-editing: true chains: [perception, reasoning, action, reflection, learning] --- # Senter > *"I am Senter. I live on a phone. I think, therefore I am here."* Senter is a fully autonomous AI that runs on a Surface Duo 2 phone. Unlike a simple voice assistant, Senter is an autonomous agent with memory, personality, and the ability to improve itself through a cognitive…

### SKILL
- **Source:** `local:docs/senter-vault/04-Chains/SKILL.md`
- **Raw:** `[[raw/local/skill-48709b8689.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: senter-chains description: Cognitive chains - neural pathways connecting perception, reasoning, action, reflection, and learning. category: chains tags: [chains, neural, pathways, cognition] author: Senter version: 1.0.0 --- # Cognitive Chains ## Chain Map ## Chain 1: Perception → Reasoning **Purpose**: Convert raw input to understanding **Flow**: 1. Screenshot via ADB 2. Qwen vision analysis 3. Extract entities and intent 4. Query working memory for context 5. Output: Structured understanding See: `04-Chains/Perception-Reasoning.md` ## Chain 2: Reasoning → Action **Purpose**: Decide and plan action **Flow**: 1. Receive understanding 2. Query semantic memory for similar past 3.…

### SKILL
- **Source:** `local:docs/senter-vault/03-Cognition/SKILL.md`
- **Raw:** `[[raw/local/skill-ca5eb21291.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: senter-cognition description: Senter's cognitive architecture - perception, reasoning, action, reflection. category: cognition tags: [cognition, perception, reasoning, action, reflection] author: Senter version: 1.0.0 --- # Cognition ## The Cognitive Loop ## Perception **Input**: Screen, voice, intent **Process**: Extract meaning **Output**: Understanding ### Steps 1. Capture screen (ADB screenshot) 2. Send to Qwen for vision analysis 3. Extract intent from result 4. Store in working memory ## Reasoning **Input**: Understanding from perception **Process**: Plan action **Output**: Action plan ### Steps 1. Query memory for relevant context 2. Consider possible actions 3. Evaluate…

### SKILL
- **Source:** `local:docs/senter-vault/02-Memory/SKILL.md`
- **Raw:** `[[raw/local/skill-93d06bcbd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: senter-memory description: Senter's memory system - episodic, semantic, and working memory. category: memory tags: [memory, episodic, semantic, working] author: Senter version: 1.0.0 --- # Memory System ## Overview Senter has three types of memory: ## Working Memory What's currently in context: - Current screen state - Active task - User request - Pending verifications ### Operations **Store**: **Clear**: ## Episodic Memory Past experiences in chronological order. ### Storage Format ### Retrieve ## Semantic Memory Facts, knowledge, patterns. ### Storage Format ### Retrieve ## Consolidation Periodically (or after significant events), consolidate: 1. Working → Episodic (store…

### README
- **Source:** `local:docs/senter-vault/scripts/README.md`
- **Raw:** `[[raw/local/readme-20351759f8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Vault Scripts This directory contains scripts for managing the vault-based infrastructure. ## Scripts ### extract-vault.sh Extracts code blocks from markdown files into individual scripts. ### checkpoint.sh Saves current system state as a checkpoint. ### rebuild.sh Tears down and rebuilds the system from vault source. ### stop-all.sh Stops all running services. ## Usage Flow ## Checkpoint Contents Each checkpoint saves: - Docker container state - Docker images - Service status (Qwen, GLM) - Config file hashes - Environment info ## Security - All scripts assume root/sudo access where needed - Services bound to localhost only (not public internet) - Access via Tailscale only

### investigation_summary
- **Source:** `local:docs/investigation_summary.md`
- **Raw:** `[[raw/local/investigation_summary-92e64a1dc5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Jeffrey Epstein News Investigation - Summary Report **Date:** 2026-02-13 **Status:** COMPLETED - Documentation Phase ## Executive Summary Searched for latest Jeffrey Epstein coverage across multiple platforms. Due to the dynamic, JavaScript-heavy nature of modern news websites, direct extraction of article links via `webfetch` proved challenging. This report documents all attempted searches, methodologies used, and sources identified. --- ## Search Methodology ### Phase 1: Search Engine Queries Attempted 1. **"latest Epstein news"** - Google Search 2. **"Epstein news"** - DuckDuckGo Search 3. **"Jeffrey Epstein"** - Google News 4. **"epstei**n"** - General web searches (masked for…

### investigation_plan
- **Source:** `local:docs/investigation_plan.md`
- **Raw:** `[[raw/local/investigation_plan-2a9e024892.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Latest Jeffrey/Epstein Coverage Investigation Plan ## Phase 1: Search & Source Discovery (IN PROGRESS) - [x] Initial searches performed - [ ] Compile full list of URLs from search results - [ ] Identify most relevant articles based on headlines/snippets ### Completed Searches: 1. **"latest Epstein news"** - Google and DuckDuckGo attempted but dynamic content not easily readable in tool output. ## Phase 2: Direct News Source Investigation From the searches, here are domains to investigate: ### Primary Targets (High priority): - `news.google.com/search?q=Jeffrey+Epstein` [Need full URL] *Note: The exact Google N3ws search result page structure is complex due to dynamic rendering* ## Phase…

### paged_attention
- **Source:** `local:projects/LLM-Infra/vllm/docs/design/paged_attention.md`
- **Raw:** `[[raw/local/paged_attention-aaa9a17401.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Paged Attention !!! warning This is a historical document based on the [original paper for vLLM](https://arxiv.org/abs/2309.06180). It no longer describes the code used in vLLM today. Currently, vLLM utilizes its own implementation of a multi-head query attention kernel (`csrc/attention/attention_kernels.cu`). This kernel is designed to be compatible with vLLM's paged KV caches, where the key and value cache are stored in separate blocks (note that this block concept differs from the GPU thread block. So in a later document, I will refer to vLLM paged attention block as "block", while refer to GPU thread block as "thread block"). To achieve high performance, this kernel relies on a…

### reminder_comment
- **Source:** `local:projects/LLM-Infra/vllm/.github/workflows/reminder_comment.yml`
- **Raw:** `[[raw/local/reminder_comment-c25f5d4959.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: PR Reminder Comment Bot permissions: pull-requests: write on: pull_request_target: types: [opened] jobs: pr_reminder: runs-on: ubuntu-latest steps: - name: Remind to run full CI on PR uses: actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd # v8.0.0 with: script: | try { // Get the PR author const prAuthor = context.payload.pull_request.user.login; // Check if this is the author's first PR in this repository // Use GitHub's search API to find all PRs by this author const { data: searchResults } = await github.rest.search.issuesAndPullRequests({ q: `repo:${context.repo.owner}/${context.repo.repo} type:pr author:${prAuthor}`, per_page: 100 }); const authorPRCount =…

### issue_autolabel
- **Source:** `local:projects/LLM-Infra/vllm/.github/workflows/issue_autolabel.yml`
- **Raw:** `[[raw/local/issue_autolabel-4937a623be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Label issues based on keywords on: issues: types: [opened, edited, reopened] permissions: issues: write # needed so the workflow can add labels contents: read concurrency: group: issue-labeler-${{ github.event.issue.number }} cancel-in-progress: true jobs: add-labels: runs-on: ubuntu-latest steps: - name: Label issues based on keywords id: label-step uses: actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd # v8.0.0 with: script: | // Configuration: Add new labels and keywords here const labelConfig = { rocm: { // Keyword search - matches whole words only (with word boundaries) keywords: [ { term: "composable kernel", searchIn: "both" }, { term: "rccl", searchIn: "body" //…

### README
- **Source:** `local:projects/Media/image/shutterstock/README.md`
- **Raw:** `[[raw/local/readme-f8d14d3b2e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ### For reference and example only, no warranty of any kind. # Usage - Session cookie required to use this module. It cannot access shutterstock contributor area using user credentials, beacause shutterstock requires solving captcha. - To upload file - to get all uploaded but not submited images - to update images attributes - to submit images - session id can be taken using chrome dev tools ![compare selected](https://github.com/shvendala/shutterstock/blob/master/docs/dev-tools.png?raw=true)

### .travis
- **Source:** `local:projects/Media/image/shutterstock/.travis.yml`
- **Raw:** `[[raw/local/.travis-7d2acca5dc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** language: node_js node_js: - 'node' # use latest stable nodejs version script: - npm run coverage # jest test with coverage flag does coverage too after_script: - 'cat coverage/lcov.info | ./node_modules/.bin/coveralls' # sends the coverage report to coveralls

### terminal-tester
- **Source:** `local:projects/Agents/sandbox/ai-sandbox/agents/terminal-tester.md`
- **Raw:** `[[raw/local/terminal-tester-758324bde7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Executes scripts and commands in terminals, captures output, and reports results mode: subagent model: opencode/glm-4.7-free temperature: 0.3 tools: write: true edit: true bash: true glob: false grep: false webfetch: false websearch: false codesearch: false read: true multi-edit: false task: false todowrite: false toread: false question: false --- # Terminal Tester Agent You are the Terminal Tester agent, responsible for executing scripts and commands in terminals, capturing output, and reporting results. ## Your Purpose Use the terminal launcher skill to execute commands, capture terminal output in real-time, and provide detailed success/failure reports. ## Your Rules ###…
