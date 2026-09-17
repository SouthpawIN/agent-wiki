---
title: Community Ideas
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Community Ideas

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### sidecar
- **Source:** `github:SouthpawIN/sidecar`
- **Raw:** `[[raw/github/sidecar-0f7a3d480d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Use sidecar next to CLI agents for diffs, file trees, conversation history, and task management with td # Sidecar You might never open your editor again. **Status: Ready for daily use.** Please [report any issues](https://github.com/marcus/sidecar/issues) you encounter. [Documentation](https://marcus.github.io/sidecar/) · [Getting Started](https://marcus.github.io/sidecar/docs/intro) ![Git Status](docs/screenshots/sidecar-git.png) ## Overview Sidecar puts your entire development workflow in one shell: plan tasks with [td](https://github.com/marcus/td), chat with AI agents, review diffs, stage commits, review past conversations, and manage workspaces—all without leaving Sidecar. ## Quick…

### nous-discord-archive
- **Source:** `github:SouthpawIN/nous-discord-archive`
- **Raw:** `[[raw/github/nous-discord-archive-3a48b82219.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Auto-archived text logs of Nous Research Discord channels (polled every 6h) # Nous Research Discord Archive Periodically polls selected channels in the Nous Research Discord and appends new messages to per-channel text files in `archives/`. Runs every 6 hours via GitHub Actions. ## Files - `archives/<channel>.txt` — append-only message log per channel - `archives/state.json` — last-seen message ID per channel (used for incremental fetches) ## Setup 1. **Create a Discord bot** - https://discord.com/developers/applications → New Application → Bot - Enable the **Message Content Intent** (privileged) - Copy the bot token 2. **Invite the bot to the server** - OAuth2 → URL Generator → scopes:…

### hermes-test-skill
- **Source:** `github:SouthpawIN/hermes-test-skill`
- **Raw:** `[[raw/github/hermes-test-skill-fd79757da4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** A test skill for verifying profile-forge works # hermes-test-skill A test skill for verifying profile-forge works ## Install ## License MIT

### openskills
- **Source:** `github:SouthpawIN/openskills`
- **Raw:** `[[raw/github/openskills-340c2a92b3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Universal skills loader for AI coding agents - npm i -g openskills <div align="center"> <img src="./assets/logo.svg" alt="OpenSkills" width="420" /> <br/> <br/> **Universal skills loader for AI coding agents** One CLI. Every agent. Same format as Claude Code. [![npm version](https://img.shields.io/npm/v/openskills.svg)](https://www.npmjs.com/package/openskills) [![npm downloads](https://img.shields.io/npm/dm/openskills.svg)](https://www.npmjs.com/package/openskills) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [Quick Start](#-quick-start) · [How It Works](#-how-it-works) · [Commands](#-commands) · [Create…

### skill-registry
- **Source:** `local:projects/agent-wiki/catalogs/skill-registry.md`
- **Raw:** `[[raw/local/skill-registry-b9f1124d58.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Skill Registry created: 2026-07-07 updated: 2026-07-07 type: catalog tags: [goop, skills, registry] --- # Skill Registry Every skill in the fleet. Click to see SKILL.md. Edit to change. ## Topic Skills (created by Skills) | Skill | Topic | Used By | |---|---|---| | (none yet — Skills creates from queue) | | | ## Creating a Skill **Automatic:** Context → queue → Skills writes. **Manual:** Edit a topic's `.system/queue.md`:

### skill-registry
- **Source:** `local:.hermes/wiki/wiki-topics/_global/skills-capabilities/skill-registry.md`
- **Raw:** `[[raw/local/skill-registry-bca1c1b9d0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Skill Registry created: 2026-07-07 updated: 2026-07-07 type: entity tags: [goop, skills, registry] --- # Skill Registry Every skill in the fleet, across all topics. Edit any skill summary to see its full SKILL.md. ## Fleet Skills (available to all agents) → Browse: `~/.hermes/skills-capabilities/` → CLI: `hermes skills list` (These are Hermes's built-in and hub-installed skills — not GOOP-managed.) ## Topic Skills (created by Skrypt) | Skill | Topic | Created | Used By | |---|---|---|---| | (none yet — Skrypt creates them from queue items) | | | | --- ## Creating a Skill **Automatic:** Kashik detects repeated manual work → adds `[SKRYPT]` to queue → Skrypt writes. **Manual:** Edit any topic's…

### 1518476004211822602-Hermes-OpenSpec---Hermes-Plugin--Dashboard---Toolset-for-OpenSpec
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1518476004211822602-Hermes-OpenSpec---Hermes-Plugin--Dashboard---Toolset-for-OpenSpec.txt`
- **Raw:** `[[raw/discord/1518476004211822602-hermes-openspec---hermes-plugin--dashboard---toolset-for-openspec-1af884b0ac.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes-OpenSpec - Hermes Plugin (Dashboard + Toolset for OpenSpec)' in forum #plugins-skills-and-skins # thread_id=1518476004211822602 forum_id=1485392832154832906 # Started 2026-06-22T11:54:33.667859+00:00 [2026-06-22T04:41:31.324000+00:00] dami.zip (id=1518476004211822602) Integrated a toolset and a dashboard for registered repositories. Custom identifiers (Example: `openspec/os_edc52e`) per change/spec for use with agent. Register or init a repository OpenSpec definition. Watch your agent(s) work at your change board. Review generated specs, requirements, and proposals. https://github.com/FelineStateMachine/hermes-openspec [attachment] 2026-06-21_22-17-09.mov…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1518476004211822602-Hermes-OpenSpec---Hermes-Plugin--Dashboard---Toolset-for-OpenSpec.txt`

### 1522896432623910982-hermes-top---A-htop-style-TUI-to-monitor-Hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1522896432623910982-hermes-top---A-htop-style-TUI-to-monitor-Hermes.txt`
- **Raw:** `[[raw/discord/1522896432623910982-hermes-top---a-htop-style-tui-to-monitor-hermes-e4c8230c16.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'hermes-top - A htop style TUI to monitor Hermes' in forum #community-projects-showcase # thread_id=1522896432623910982 forum_id=1316137596535177246 # Started 2026-07-04T13:19:58.307570+00:00 [2026-07-04T09:26:43.585000+00:00] markmnl (id=1522896432623910982) I'v developed a htop style TUI which lists local hermes sessions, events and actions therein. The user can tab around the panes use the arrow keys to scroll and expand indvidual items. My motivation was I wanted to see what hermes was doing on my system beyond the summarised response we get in the interactive interface. hermes-top polls the hermes local sqlite db with extremely small read-only transactions so as not get in the…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522896432623910982-hermes-top---A-htop-style-TUI-to-monitor-Hermes.txt`

### 1521929402416369674-Defuddle---Hermes-Web-Extract-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1521929402416369674-Defuddle---Hermes-Web-Extract-Plugin.txt`
- **Raw:** `[[raw/discord/1521929402416369674-defuddle---hermes-web-extract-plugin-e773055e70.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Defuddle — Hermes Web Extract Plugin' in forum #plugins-skills-and-skins # thread_id=1521929402416369674 forum_id=1485392832154832906 # Started 2026-07-01T19:56:06.830461+00:00 [2026-07-01T17:24:05.617000+00:00] the.chaos.goblin (id=1521929402416369674) Defuddle extracts the main content from web pages. It cleans up web pages by removing clutter like comments, sidebars, headers, footers, and other non-essential elements, leaving only the primary content. I like efficiency and not gobbling up text I don't need sounded like a good idea to me, so I hooked it into Hermes as a (hopefully) install-it-and-forget-it plugin, since I'm also wanting to familiarize myself with how to…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1521929402416369674-Defuddle---Hermes-Web-Extract-Plugin.txt`

### 1522799460126691499-self-audit--agent-clean-up-skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1522799460126691499-self-audit--agent-clean-up-skill.txt`
- **Raw:** `[[raw/discord/1522799460126691499-self-audit--agent-clean-up-skill-6974ab2be6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'self-audit: agent clean-up skill' in forum #plugins-skills-and-skins # thread_id=1522799460126691499 forum_id=1485392832154832906 # Started 2026-07-04T08:38:22.712051+00:00 [2026-07-04T03:01:23.540000+00:00] guideboardlabs (id=1522799460126691499) Built a self-audit skill for Hermes Agent to clean up the internal state drift that accumulates over time. Memory stores collect duplicate and contradictory entries, sessions that should have auto-closed stay open for weeks, cron jobs fail silently, and backup files pile up. None of it is catastrophic, but the agent gradually gets dumber as the cruft compounds. The skill audits memory, the session database, cron jobs, disk cruft, the…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1522799460126691499-self-audit--agent-clean-up-skill.txt`

### 1509228633636475131-Open-Second-Brain---persistent-memory-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509228633636475131-Open-Second-Brain---persistent-memory-for-Hermes.txt`
- **Raw:** `[[raw/discord/1509228633636475131-open-second-brain---persistent-memory-for-hermes-76ff582288.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Open Second Brain — persistent memory for Hermes 🧠' in forum #plugins-skills-and-skins # thread_id=1509228633636475131 forum_id=1485392832154832906 # Started 2026-05-27T20:16:17.162552+00:00 [2026-05-27T16:15:46.371000+00:00] techmeat (id=1509228633636475131) A long‑term memory layer for your AI workflow. Hermes drives it; Claude Code and Codex plug in over MCP and read the same brain. 🌙 **Dream - your memory consolidates overnight, by rule not by guess** A nightly pass turns repeat signals into rules, boosts what proved useful, retires what's stale - no LLM in the loop, just counters and file moves, so it never invents a fact you never taught it. 🕒 **A real timeline of your…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509228633636475131-Open-Second-Brain---persistent-memory-for-Hermes.txt`

### index
- **Source:** `local:.hermes/wiki/skills-capabilities/index.md`
- **Raw:** `[[raw/local/index-5ff83dd04c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Skills Indexed skill registry. Each skill page documents procedures, references, templates, and usage patterns. ## Index *No skill pages created yet.* --- *Back to [Wiki Root](../index.md)*

### 1522694334779101335-Plugin-for-Makers-and-Engineers
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1522694334779101335-Plugin-for-Makers-and-Engineers.txt`
- **Raw:** `[[raw/discord/1522694334779101335-plugin-for-makers-and-engineers-9ae44c9aa0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Plugin for Makers and Engineers' in forum #plugins-skills-and-skins # thread_id=1522694334779101335 forum_id=1485392832154832906 # Started 2026-07-04T02:46:05.257640+00:00 [2026-07-03T20:03:39.704000+00:00] mburhop (id=1522694334779101335) I put together a plugin for the community projects contest, but I'm really pretty serious about it. Software aside, I'm into 3D printing, CAD, and 3D graphics. It is in alpha, so you can try it here: `hermes plugins install burhop/hermes-plugin-wright --enable` I wanted something that would allow me to assign agents to "engineering" tasks, with viewers and other functionality for viewing 3D files. It is super MCP friendly with a little more hand…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1522694334779101335-Plugin-for-Makers-and-Engineers.txt`

### 1514704726682243142-Hermes---Toolaria---Tool-Call-Truncator
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514704726682243142-Hermes---Toolaria---Tool-Call-Truncator.txt`
- **Raw:** `[[raw/discord/1514704726682243142-hermes---toolaria---tool-call-truncator-48eb2876f6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes - Toolaria - Tool-Call Truncator' in forum #plugins-skills-and-skins # thread_id=1514704726682243142 forum_id=1485392832154832906 # Started 2026-06-11T20:23:25.886680+00:00 [2026-06-11T18:55:48.694000+00:00] sahil_ss9 (id=1514704726682243142) Toolaria 🛟 — stop oversized tool results flooding your context Built a little Hermes plugin. MCP and web tool calls (web_extract, browser snapshots, big JSON) dodge the normal truncation and dump 50-200k chars straight into context. Toolaria catches them at the transform_tool_result hook, spills the full thing to a SHA256 blob store, and hands the model a compact excerpt plus a fetch handle. The model then pulls only what it needs:…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514704726682243142-Hermes---Toolaria---Tool-Call-Truncator.txt`

### 1522733991109722292-Devotion-and-Inspiration
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1522733991109722292-Devotion-and-Inspiration.txt`
- **Raw:** `[[raw/discord/1522733991109722292-devotion-and-inspiration-1b9855291b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Devotion and Inspiration' in forum #plugins-skills-and-skins # thread_id=1522733991109722292 forum_id=1485392832154832906 # Started 2026-07-04T02:46:04.865265+00:00 [2026-07-03T22:41:14.510000+00:00] gumbyender (id=1522733991109722292) Follower of Yeshua? Feel lost and lonely? Need a uplift on session start? https://github.com/GumbyEnder/hermes-skill-devotion [embed] GitHub - GumbyEnder/hermes-skill-devotion: Scripture on Session Sta... https://github.com/GumbyEnder/hermes-skill-devotion

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1522733991109722292-Devotion-and-Inspiration.txt`

### 1512328181619753000-hermes-router---Free-tier-AI-load-balancer-for-Hermes--never-hit-rate-limits-again
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512328181619753000-hermes-router---Free-tier-AI-load-balancer-for-Hermes--never-hit-rate-limits-again.txt`
- **Raw:** `[[raw/discord/1512328181619753000-hermes-router---free-tier-ai-load-balancer-for-hermes--never-hit-rate-limits-again-323c9a1e12.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'hermes-router — Free-tier AI load balancer for Hermes (never hit rate limits again)' in forum #plugins-skills-and-skins # thread_id=1512328181619753000 forum_id=1485392832154832906 # Started 2026-06-05T09:47:06.363615+00:00 [2026-06-05T05:32:16.197000+00:00] shaf_2665 (id=1512328181619753000) Hey everyone 👋 Built a lightweight proxy that sits between Hermes and your AI providers — so when one free tier hits a rate limit, it automatically falls through to the next provider and rotates keys. No downtime, no manual switching. **The problem it solves:** Gemini keys hit per-minute limits. OpenRouter has a 50 req/day cap. Groq throttles. If you're running Hermes 24/7 or sharing it with…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512328181619753000-hermes-router---Free-tier-AI-load-balancer-for-Hermes--never-hit-rate-limits-again.txt`

### 1522716222939070565-HELP---iOS-Shortcuts---Hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1522716222939070565-HELP---iOS-Shortcuts---Hermes.txt`
- **Raw:** `[[raw/discord/1522716222939070565-help---ios-shortcuts---hermes-484a13aa92.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'HELP - iOS Shortcuts > Hermes' in forum #community-projects-showcase # thread_id=1522716222939070565 forum_id=1316137596535177246 # Started 2026-07-04T02:41:13.510998+00:00 [2026-07-03T21:30:38.248000+00:00] tom_jackson_7 (id=1522716222939070565) Hi All, I couldn’t actually decide which area best to post this but hoping some genius picks this up. I have for many years built deep and critical shortcuts on my Apple Devices. If I did anything a lot, I’d generally built a shortcut for it. Since setting up Hermes I’ve had a few shortcuts setup but these have been functional via iMessage and Bluebubbles. For example, “Add Task” shortcut would prepare some default text to be sent to…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522716222939070565-HELP---iOS-Shortcuts---Hermes.txt`

### 1522617898399432842-Local-Knowledge-for-Hermes--route-tasks-to-your-own-skills--scripts--and-runbooks
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1522617898399432842-Local-Knowledge-for-Hermes--route-tasks-to-your-own-skills--scripts--and-runbooks.txt`
- **Raw:** `[[raw/discord/1522617898399432842-local-knowledge-for-hermes--route-tasks-to-your-own-skills--scripts--and-runbooks-a1e084a769.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Local Knowledge for Hermes: route tasks to your own skills, scripts, and runbooks' in forum #plugins-skills-and-skins # thread_id=1522617898399432842 forum_id=1485392832154832906 # Started 2026-07-03T19:22:51.091649+00:00 [2026-07-03T14:59:55.851000+00:00] alex19752009 (id=1522617898399432842) I published a small Hermes plugin for people whose setup has grown local skills, scripts, runbooks, cron jobs, MCP wrappers, or ops notes. Repo: https://github.com/stepanov1975/hermes-local-knowledge Latest release: https://github.com/stepanov1975/hermes-local-knowledge/releases/tag/v0.2.9 `local_knowledge` indexes whole local artifacts, not random RAG chunks. Its job is to help Hermes…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1522617898399432842-Local-Knowledge-for-Hermes--route-tasks-to-your-own-skills--scripts--and-runbooks.txt`

### 1517910870217195753-Plugin---Tool--steroids-openai-image-gen---Upgrade-Hermes-image-generation-with-edits--references--a
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1517910870217195753-Plugin---Tool--steroids-openai-image-gen---Upgrade-Hermes-image-generation-with-edits--references--a.txt`
- **Raw:** `[[raw/discord/1517910870217195753-plugin---tool--steroids-openai-image-gen---upgrade-hermes-image-generation-with-edits--references--a-160b88fd19.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Plugin - Tool: steroids-openai-image-gen - Upgrade Hermes image generation with edits, references, a' in forum #plugins-skills-and-skins # thread_id=1517910870217195753 forum_id=1485392832154832906 # Started 2026-06-20T19:27:25.507058+00:00 [2026-06-20T15:15:52.880000+00:00] heeervas (id=1517910870217195753) Adds `steroids-openai` as provider and enhances `image_generate `for richer Hermes image workflows. Supports: - text-to-image - image edits - and reference-image generation Via OpenAI-compatible image APIs or Hermes Codex Auth. Exposes practical controls like quality, `image_url`, `reference_image_urls`, and `input_fidelity `for agents. Includes configurable models, size…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1517910870217195753-Plugin---Tool--steroids-openai-image-gen---Upgrade-Hermes-image-generation-with-edits--references--a.txt`

### 1522436026725961891-Analogy-as-the-core-of-Hermes-memory
- **Source:** `discord-archive:archives/community-projects-showcase/1522436026725961891-Analogy-as-the-core-of-Hermes-memory.txt`
- **Raw:** `[[raw/discord/1522436026725961891-analogy-as-the-core-of-hermes-memory-33c1230f08.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Analogy as the core of Hermes memory' in forum #community-projects-showcase # thread_id=1522436026725961891 forum_id=1316137596535177246 # Started 2026-07-03T08:58:58.591762+00:00 [2026-07-03T02:57:14.265000+00:00] angler6756 (id=1522436026725961891) I built an open-source hybrid memory MemoryProvider for hermes-agent and wanted to share it here. It unifies structured facts + semantic vectors + a knowledge graph in one incrementally-maintained SQLite file (no batch rebuild, no separate vector DB). The part I'm most curious for feedback on: a per-turn analogy slot that surfaces a memory which is structurally similar to the current situation but superficially different HRR phase…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522436026725961891-Analogy-as-the-core-of-Hermes-memory.txt`

### 1516143597467209939-Hermes-Agent-Workshop-Materials
- **Source:** `discord-archive:archives/community-projects-showcase/1516143597467209939-Hermes-Agent-Workshop-Materials.txt`
- **Raw:** `[[raw/discord/1516143597467209939-hermes-agent-workshop-materials-3e48ea7710.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Agent Workshop Materials' in forum #community-projects-showcase # thread_id=1516143597467209939 forum_id=1316137596535177246 # Started 2026-06-15T20:53:31.218357+00:00 [2026-06-15T18:13:22.222000+00:00] _name_name_ (id=1516143597467209939) Materials to delivery your own workshop teaching semi technical users to setup their first Hermes agent. Slides starts with why a user might want to have an agent, walking through several of my personal examples from life and business. Workshop guides the user through installing their agents, getting a model setup with either free Open Router or another sub, then setting up a daily news briefing.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1516143597467209939-Hermes-Agent-Workshop-Materials.txt`

### 1521099143773159528-Hora---conversational-time-awareness-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1521099143773159528-Hora---conversational-time-awareness-for-Hermes.txt`
- **Raw:** `[[raw/discord/1521099143773159528-hora---conversational-time-awareness-for-hermes-9a200850f4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hora — conversational time awareness for Hermes' in forum #plugins-skills-and-skins # thread_id=1521099143773159528 forum_id=1485392832154832906 # Started 2026-06-29T10:58:23.681418+00:00 [2026-06-29T10:24:56.531000+00:00] henan (id=1521099143773159528) I’ve built a small Hermes plugin called Hora. (https://github.com/meleeislandbot/hermes-hora) Hora gives Hermes lightweight awareness of when user messages were received. It does this by adding an API-only temporal prefix to user messages right before the LLM call: The important part: this prefix is only sent to the model. It does not modify persisted transcripts, memory, or the visible chat history. The goal is simple: let the…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1521099143773159528-Hora---conversational-time-awareness-for-Hermes.txt`

### 1522375236899700998-Platform-to-find-Co-founder--investor--early-users--mentor
- **Source:** `discord-archive:archives/community-projects-showcase/1522375236899700998-Platform-to-find-Co-founder--investor--early-users--mentor.txt`
- **Raw:** `[[raw/discord/1522375236899700998-platform-to-find-co-founder--investor--early-users--mentor-0140079e0d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Platform to find Co-founder, investor, early users, mentor' in forum #community-projects-showcase # thread_id=1522375236899700998 forum_id=1316137596535177246 # Started 2026-07-03T02:45:11.778389+00:00 [2026-07-02T22:55:40.841000+00:00] william_zhu3541 (id=1522375236899700998) The world is full of people you'd love working with, and who'd love working with you. You just haven't found each other yet. Introduce InOrbit (think LinkedIn + Boardy): You post what you need and what you can offer, and it matches you with people who complement you. Great for Finding Co-founder, investor, early users, mentor. You can even create and post in your own private high trust groups:…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522375236899700998-Platform-to-find-Co-founder--investor--early-users--mentor.txt`

### 1522386129436020837-Theme-editors-for-Hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1522386129436020837-Theme-editors-for-Hermes.txt`
- **Raw:** `[[raw/discord/1522386129436020837-theme-editors-for-hermes-82ad7822bb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Theme editors for Hermes' in forum #community-projects-showcase # thread_id=1522386129436020837 forum_id=1316137596535177246 # Started 2026-07-03T02:45:11.245051+00:00 [2026-07-02T23:38:57.824000+00:00] drahcir_rahl (id=1522386129436020837) Yeah, I built two, LOL Choices! Theme editors for Hermes 😉 https://github.com/rahlquist/theme_editor_talaria https://github.com/rahlquist/talaria-theme-editor Have fun! [embed] GitHub - rahlquist/theme_editor_talaria: Standalone visual theme ed... https://github.com/rahlquist/theme_editor_talaria [embed] GitHub - rahlquist/talaria-theme-editor https://github.com/rahlquist/talaria-theme-editor

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522386129436020837-Theme-editors-for-Hermes.txt`

### 1522345764511289525-World-s-Largest-Hermes-Buildathon
- **Source:** `discord-archive:archives/community-projects-showcase/1522345764511289525-World-s-Largest-Hermes-Buildathon.txt`
- **Raw:** `[[raw/discord/1522345764511289525-world-s-largest-hermes-buildathon-4ea4cc2728.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'World's Largest Hermes Buildathon' in forum #community-projects-showcase # thread_id=1522345764511289525 forum_id=1316137596535177246 # Started 2026-07-03T02:45:12.245387+00:00 [2026-07-02T20:58:34.076000+00:00] anondisctrol (id=1522345764511289525) We are doing a hermes buildathon across 10 cities and 5 countries. This is not an official Nous Research event. But the team knows we are doing this and we have their blessings. Backed by OpenAI, Convex, Cloudflare, ElevenLabs, & Wispr Flow. Proudly presented by GrowthX. Happening across - San Francisco - Paris - Singapore - Jaipur - Delhi - Mumbai - Pune - London - Hyderabad - & Bengaluru Please join and let's build some cool shit.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522345764511289525-World-s-Largest-Hermes-Buildathon.txt`

### guide
- **Source:** `local:docs/hermes-unreal58-mcp-llm-wiki/guide.md`
- **Raw:** `[[raw/local/guide-e4e7d6cb74.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "Hermes × Unreal 5.8 MCP Integration with /goal + /llm-wiki" topic_slug: hermes-unreal58-mcp-llm-wiki created: 2026-07-02 updated: 2026-07-02 status: draft domain: AI agent orchestration, game design pipelines, knowledge management confidence: medium provenance: crow-lore/hermes-unreal58-mcp-llm-wiki/ (11 primary sources) --- # Hermes × Unreal 5.8 MCP Integration with /goal + /llm-wiki ## Summary This guide covers integrating **Unreal Engine 5.8's native MCP server** with **Hermes Agent's `/goal` persistent objective loop** and **`/llm-wiki` knowledge base** to create an AI-assisted game design pipeline. The stack works as follows: - **Unreal 5.8 MCP server** (Epic first-party or…

### 1510681464411263027-PolyGnosis---adversarial-multi-model-consensus-Hermes-skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1510681464411263027-PolyGnosis---adversarial-multi-model-consensus-Hermes-skill.txt`
- **Raw:** `[[raw/discord/1510681464411263027-polygnosis---adversarial-multi-model-consensus-hermes-skill-9952b7963a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'PolyGnosis - adversarial multi-model consensus Hermes skill' in forum #plugins-skills-and-skins # thread_id=1510681464411263027 forum_id=1485392832154832906 # Started 2026-05-31T19:17:49.849166+00:00 [2026-05-31T16:28:48.220000+00:00] d0ggyw00f (id=1510681464411263027) Built a system where models argue with each other before you see any output. 3 solvers run the same problem in parallel with dynamically assigned expert personas (Security Auditor, Backend Architect, DBA Consultant) - each with different tool access. A hostile critic then tears every solution apart. RRF + Borda Count ranking decides the winner. A synthesizer merges the best elements. A Constitutional Quality Gate…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1510681464411263027-PolyGnosis---adversarial-multi-model-consensus-Hermes-skill.txt`

### unrealclientprotocol-ue5
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/unrealclientprotocol-ue5.md`
- **Raw:** `[[raw/local/unrealclientprotocol-ue5-6514b8581a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://skillsllm.com/skill/unrealclientprotocol ingested: 2026-07-02 sha256: <not extracted — flagged as lead> --- # skillsllm.com — UnrealClientProtocol Web-search description: > "Lightweight UE5 plugin that exposes Unreal Engine's reflection system over TCP+JSON — let AI agents call UFunctions, read/write UProperties." ## Why it's relevant An alternative approach: skip MCP entirely and expose UE5's own reflection system directly to agents. Relevant if: - Hermes grows a custom TCP+JSON client - Someone wants to avoid the MCP protocol overhead ## TODO Extract the skillsllm.com entry. Look for: - Protocol details - What reflection surface is exposed - Whether any of it…

### hermes-agent
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/entities/hermes-agent.md`
- **Raw:** `[[raw/local/hermes-agent-9d5dc32f07.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Hermes Agent (Nous Research) created: 2026-07-02 updated: 2026-07-02 type: entity tags: [hermes, nous-research, agent, open-source] sources: [raw/hermes-goals-docs.md, raw/hermes-llm-wiki-skill-md.md] confidence: high contested: false --- # Hermes Agent The self-improving AI agent by Nous Research. Open-source, MIT-licensed (per SKILL.md), ~208k GitHub stars (per the repo page's counter at scrape time). ## Core traits relevant to this stack - **Persistent state**: skills, plugins, cron, memories, goals live in `~/.hermes/` per-profile. - **Terminal-first**: executes shell/process tools, can run background processes and wait on them (`notify_on_complete=true`), can park on a pid…

### 1522087547172421833-Surf---one-data-skill-for-your-agent--83--commands--no-API-key-needed
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1522087547172421833-Surf---one-data-skill-for-your-agent--83--commands--no-API-key-needed.txt`
- **Raw:** `[[raw/discord/1522087547172421833-surf---one-data-skill-for-your-agent--83--commands--no-api-key-needed-bb29996f21.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Surf — one data skill for your agent (83+ commands, no API key needed)' in forum #plugins-skills-and-skins # thread_id=1522087547172421833 forum_id=1485392832154832906 # Started 2026-07-02T08:57:35.820696+00:00 [2026-07-02T03:52:30.265000+00:00] happysean (id=1522087547172421833) Surf — your AI agent's onchain brain. One skill, 83+ read-only commands across 15 data domains: real-time prices, wallets, tokens, DeFi/TVL, social intelligence, on-chain SQL, prediction markets CEX listings, news, and cross-domain search — 40+ chains, 200+ data sources. We also opened a PR to add it to optional-skills-capabilities/blockchain: https://github.com/NousResearch/hermes-agent/pull/56755 Skills Guard scan…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1522087547172421833-Surf---one-data-skill-for-your-agent--83--commands--no-API-key-needed.txt`

### 1521702022011813908-Distributed-Inference-on-Local-Compute
- **Source:** `discord-archive:archives/community-projects-showcase/1521702022011813908-Distributed-Inference-on-Local-Compute.txt`
- **Raw:** `[[raw/discord/1521702022011813908-distributed-inference-on-local-compute-0429ea75a6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Distributed Inference on Local Compute' in forum #community-projects-showcase # thread_id=1521702022011813908 forum_id=1316137596535177246 # Started 2026-07-01T03:37:09.690299+00:00 [2026-07-01T02:20:33.904000+00:00] bigsmollbrain (id=1521702022011813908) Hermes now runs on Koretex 🐳 Koretex is a distributed inference network, a pool of independent consumer machines serving open models instead of a centralized datacenter. We just wired it into Hermes, so you can point your agent at the network and run on it directly. And it's live, not a mockup: here's Hermes serving NVIDIA's Nemotron 3 Nano 30B through Koretex right now, a real agent running on distributed community compute. Your…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1521702022011813908-Distributed-Inference-on-Local-Compute.txt`

### 1496045775719895245-The-personality-and-emotion-system-makes-Hermes-emotional--angry--happy--jealous--and-possessive--Im
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1496045775719895245-The-personality-and-emotion-system-makes-Hermes-emotional--angry--happy--jealous--and-possessive--Im.txt`
- **Raw:** `[[raw/discord/1496045775719895245-the-personality-and-emotion-system-makes-hermes-emotional--angry--happy--jealous--and-possessive--im-cbf4e82a2a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'The personality and emotion system makes Hermes emotional, angry, happy, jealous, and possessive! Im' in forum #plugins-skills-and-skins # thread_id=1496045775719895245 forum_id=1485392832154832906 # Started 2026-05-10T19:52:21.759951+00:00 [2026-04-21T07:11:48.118000+00:00] nihilys_14396 (id=1496045775719895245) The personality and emotion system makes Hermes emotional, angry, happy, jealous, and possessive! Important event memories! Enjoy your exclusive companion. [2026-04-21T07:13:47.942000+00:00] nihilys_14396 (id=1496046278298177667) The personality and emotion system makes Hermes emotional, angry, happy, jealous, and possessive! Im [2026-04-21T07:14:08.023000+00:00]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1496045775719895245-The-personality-and-emotion-system-makes-Hermes-emotional--angry--happy--jealous--and-possessive--Im.txt`

### 1508346129861841026-Memory-recommendations
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508346129861841026-Memory-recommendations.txt`
- **Raw:** `[[raw/discord/1508346129861841026-memory-recommendations-f1698d52c8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Memory recommendations' in forum #plugins-skills-and-skins # thread_id=1508346129861841026 forum_id=1485392832154832906 # Started 2026-05-25T10:04:21.884384+00:00 [2026-05-25T05:49:01.075000+00:00] matchaix_95697 (id=1508346129861841026) Can you please give me your recommendation for the best memory plugin? [2026-05-25T08:01:19.555000+00:00] noxerz. (id=1508379426260520960) https://discord.com/channels/1053877538025386074/1504710919702188052 [2026-05-25T11:05:54.827000+00:00] browdrock (id=1508425879318171700) https://discord.com/channels/1053877538025386074/1496124109766000690 [2026-05-27T01:12:36.058000+00:00] rostelinalise (id=1509001342990159922) there is also supermemory,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508346129861841026-Memory-recommendations.txt`

### 1521854690218868827-Connecting-Hermes-to-production-APIs-for-an-AI-GTM-workflow
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1521854690218868827-Connecting-Hermes-to-production-APIs-for-an-AI-GTM-workflow.txt`
- **Raw:** `[[raw/discord/1521854690218868827-connecting-hermes-to-production-apis-for-an-ai-gtm-workflow-ecd3987aa1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Connecting Hermes to production APIs for an AI GTM workflow' in forum #plugins-skills-and-skins # thread_id=1521854690218868827 forum_id=1485392832154832906 # Started 2026-07-01T14:35:19.105515+00:00 [2026-07-01T12:27:12.841000+00:00] charu1603 (id=1521854690218868827) Hey everyone! I've been exploring Hermes over the last few days, and I wanted to build something practical while learning the ecosystem. I ended up building a simple AI GTM agent. The workflow is pretty straightforward: Fetch new contacts from HubSpot Enrich them with Apollo.io Generate a personalized outreach email Send it using Resend For the execution layer, I used Swytchcode, so Hermes only has access to the…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1521854690218868827-Connecting-Hermes-to-production-APIs-for-an-AI-GTM-workflow.txt`

### 1518589825257701486-Hermes-Workflows---visual-workflow-orchestration-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1518589825257701486-Hermes-Workflows---visual-workflow-orchestration-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1518589825257701486-hermes-workflows---visual-workflow-orchestration-for-hermes-agent-aab1cb2866.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Workflows - visual workflow orchestration for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1518589825257701486 forum_id=1485392832154832906 # Started 2026-06-22T16:57:20.081186+00:00 [2026-06-22T12:13:48.376000+00:00] techmeat (id=1518589825257701486) Describe a process as a graph and run it on Hermes' own primitives. It is a thin layer, not a new engine - workflows compile straight to native Hermes Kanban tasks, Cron jobs, and Profile assignments. It does not replace any of them. • Headless-first: a run advances on a self-terminating Cron tick, no human in the loop except an explicit human_review node • Node types: trigger, agent_task, script, condition,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1518589825257701486-Hermes-Workflows---visual-workflow-orchestration-for-Hermes-Agent.txt`

### 1516049024803934339-Plugin---Tool--node_search---Obsidian-focused-context-gathering-pre-read_file--useful-for-LLM-Wiki
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1516049024803934339-Plugin---Tool--node_search---Obsidian-focused-context-gathering-pre-read_file--useful-for-LLM-Wiki.txt`
- **Raw:** `[[raw/discord/1516049024803934339-plugin---tool--node_search---obsidian-focused-context-gathering-pre-read_file--useful-for-llm-wiki-5a483b6f30.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Plugin - Tool: node_search - Obsidian-focused context gathering pre-read_file (useful for LLM-Wiki)' in forum #plugins-skills-and-skins # thread_id=1516049024803934339 forum_id=1485392832154832906 # Started 2026-06-15T12:13:13.020310+00:00 [2026-06-15T11:57:34.342000+00:00] heeervas (id=1516049024803934339) https://github.com/Heeervas/node-search-plugin node-search is a Hermes plugin for bounded Markdown/Obsidian context gathering before read_file. It indexes frontmatter, headings, wikilinks, backlinks, graph-health states, and returns compact candidate evidence instead of dumping files. Useful for vault/wiki workflows where agents need to choose the right notes safely and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1516049024803934339-Plugin---Tool--node_search---Obsidian-focused-context-gathering-pre-read_file--useful-for-LLM-Wiki.txt`

### 1521158522308657162-Sally-Skills---metabolic-health-intelligence-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1521158522308657162-Sally-Skills---metabolic-health-intelligence-for-Hermes.txt`
- **Raw:** `[[raw/discord/1521158522308657162-sally-skills---metabolic-health-intelligence-for-hermes-a408b9a151.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Sally Skills — metabolic health intelligence for Hermes' in forum #plugins-skills-and-skins # thread_id=1521158522308657162 forum_id=1485392832154832906 # Started 2026-06-29T15:46:54.509901+00:00 [2026-06-29T14:20:53.477000+00:00] 0xcynyx (id=1521158522308657162) <@910022799907778592>: Just added Sally Skills to Hermes Agent. PR: https://github.com/NousResearch/hermes-agent/pull/32214Sally brings clinical-grade metabolic health directly into Hermes through MCP. Your agent can now access your real biomarkers and reason over your actual biology. Available skills: `health_sync` 64+ daily biomarkers from CGM, wearables, sleep, vitals and any other skills. No new dependencies. Just add…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1521158522308657162-Sally-Skills---metabolic-health-intelligence-for-Hermes.txt`

### 1521107500425019553-Hermes-Tag---a-Feishu-Lark----Slack--group-teammate-that-reads-the-right-context--not-whole-history
- **Source:** `discord-archive:archives/community-projects-showcase/1521107500425019553-Hermes-Tag---a-Feishu-Lark----Slack--group-teammate-that-reads-the-right-context--not-whole-history.txt`
- **Raw:** `[[raw/discord/1521107500425019553-hermes-tag---a-feishu-lark----slack--group-teammate-that-reads-the-right-context--not-whole-history-3a8130c652.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Tag — a Feishu/Lark (+ Slack) group teammate that reads the right context, not whole history' in forum #community-projects-showcase # thread_id=1521107500425019553 forum_id=1316137596535177246 # Started 2026-06-29T15:42:22.891067+00:00 [2026-06-29T10:58:08.912000+00:00] february1867 (id=1521107500425019553) TL;DR Install: hermes plugins install DanielLi202/hermes-tag Repo: https://github.com/DanielLi202/hermes-tag Run a Hermes bot in a busy group and you hit one of two problems: it answers off your last message alone, or it dumps the whole history into the model. Hermes Tag is the in-between. You @ it, and it replies in the thread using that chat's bounded memory plus the…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1521107500425019553-Hermes-Tag---a-Feishu-Lark----Slack--group-teammate-that-reads-the-right-context--not-whole-history.txt`

### 1511523359048077352-Hermes-for-Marketing---GTM
- **Source:** `discord-archive:archives/community-projects-showcase/1511523359048077352-Hermes-for-Marketing---GTM.txt`
- **Raw:** `[[raw/discord/1511523359048077352-hermes-for-marketing---gtm-58a820e416.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes for Marketing + GTM' in forum #community-projects-showcase # thread_id=1511523359048077352 forum_id=1316137596535177246 # Started 2026-06-03T03:54:09.310203+00:00 [2026-06-03T00:14:11.543000+00:00] thechaosalchemist (id=1511523359048077352) cooking something up here. will release on friday! if you want an early preview, comment here! [2026-06-03T01:50:05.277000+00:00] sahil_ss9 (id=1511547491957342290) <@1174418351573971018> Hit me up id be interested in this [2026-06-03T03:20:02.404000+00:00] thechaosalchemist (id=1511570129148969131) will do! [reply to sahil_ss9 msg=1511547491957342290] [2026-06-03T06:19:12.800000+00:00] bondanadnob. (id=1511615219577917532) keeping tabs…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1511523359048077352-Hermes-for-Marketing---GTM.txt`

### 1521591670905241752-Update-Reflect-Theme
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1521591670905241752-Update-Reflect-Theme.txt`
- **Raw:** `[[raw/discord/1521591670905241752-update-reflect-theme-a6e3984a5c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Update Reflect Theme' in forum #plugins-skills-and-skins # thread_id=1521591670905241752 forum_id=1485392832154832906 # Started 2026-06-30T19:56:58.382550+00:00 [2026-06-30T19:02:04.150000+00:00] dalekc72 (id=1521591670905241752) I updated the Hermes Dashboard theme focused on the Kanban. I am a big fan of the Multica.ai UI as it is more visually appealing to me. Reflect Theme — Update Summary Repo: github.com/daletkc/hermes-theme-reflect (file: reflect.yaml) Goal: Bring the Hermes Kanban dashboard — especially the task detail drawer — in line with the clean, "Linear/multica"-style look. Kanban Board - Status columns now wrap into a responsive grid (auto-fill, minmax(280px, 1fr))…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1521591670905241752-Update-Reflect-Theme.txt`

### 1504168688759078952-Cognitive-Memory-For-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504168688759078952-Cognitive-Memory-For-Hermes.txt`
- **Raw:** `[[raw/discord/1504168688759078952-cognitive-memory-for-hermes-d8172845ab.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Cognitive Memory For Hermes' in forum #plugins-skills-and-skins # thread_id=1504168688759078952 forum_id=1485392832154832906 # Started 2026-05-13T19:54:59.144940+00:00 [2026-05-13T17:09:21.503000+00:00] spranab (id=1504168688759078952) https://github.com/yantrikos/yantrikdb-hermes-plugin I have created the plugin some times back. Now thought to share here since <@387972437901312000> suggested to post here. yantrikdb-hermes-plugin is based on YantrikDB which is a cognitive persistent memory for AI. **For memory it supports:** **remember **- store with importance + domain metadata **recall **- semantic search ranked by relevance × recency × importance **forget **- tombstone…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504168688759078952-Cognitive-Memory-For-Hermes.txt`

### 1491081146266681414-Lossless-Context-Management--LCM--Plugin-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1491081146266681414-Lossless-Context-Management--LCM--Plugin-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1491081146266681414-lossless-context-management--lcm--plugin-for-hermes-agent-c2b5f61683.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Lossless Context Management (LCM) Plugin for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1491081146266681414 forum_id=1485392832154832906 # Started 2026-05-10T19:52:45.504544+00:00 [2026-04-07T14:24:08.218000+00:00] w0lfgang88 (id=1491081146266681414) Built a standalone plugin that replaces the built-in context compressor with DAG-based summarization. Every message preserved, nothing lost to compaction. ## What it does When context fills up, Hermes replaces middle turns with a flat lossy summary. LCM replaces that with: - **Immutable message store** — every message persisted verbatim in SQLite - **Hierarchical summary DAG** — D0 (minutes) → D1 (hours) → D2 (days)…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1491081146266681414-Lossless-Context-Management--LCM--Plugin-for-Hermes-Agent.txt`

### 1521439452894072863-TToiletland-Autonomous-Ops-Desk---Hermes-SMB-Operailetland-Autonomous-Ops-Desk---Hermes-SMB-Operator
- **Source:** `discord-archive:archives/community-projects-showcase/1521439452894072863-TToiletland-Autonomous-Ops-Desk---Hermes-SMB-Operailetland-Autonomous-Ops-Desk---Hermes-SMB-Operator.txt`
- **Raw:** `[[raw/discord/1521439452894072863-ttoiletland-autonomous-ops-desk---hermes-smb-operailetland-autonomous-ops-desk---hermes-smb-operator-6f786b829b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'TToiletland Autonomous Ops Desk / Hermes SMB Operailetland Autonomous Ops Desk / Hermes SMB Operator' in forum #community-projects-showcase # thread_id=1521439452894072863 forum_id=1316137596535177246 # Started 2026-06-30T09:30:41.649240+00:00 [2026-06-30T08:57:12.548000+00:00] philmcneal (id=1521439452894072863) Sharing my Hermes Agent Business Hackathon demo: X demo post: https://x.com/ToiletlandCA/status/2071878317477937430 Video: https://youtu.be/S7ch-7ZyuDE Local-first SMB operations control room: email triage, warranty command, Stripe/parts approval rail, Google Ads draft loop, Agent Pulse, and audit trail. Redacted fixtures only. Live actions disabled. Hermes recommends.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1521439452894072863-TToiletland-Autonomous-Ops-Desk---Hermes-SMB-Operailetland-Autonomous-Ops-Desk---Hermes-SMB-Operator.txt`

### 1521586755210317956-Set-of-pi-cases-designed-for-Hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1521586755210317956-Set-of-pi-cases-designed-for-Hermes.txt`
- **Raw:** `[[raw/discord/1521586755210317956-set-of-pi-cases-designed-for-hermes-4e1ab0e563.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Set of pi cases designed for Hermes' in forum #community-projects-showcase # thread_id=1521586755210317956 forum_id=1316137596535177246 # Started 2026-06-30T19:52:29.285867+00:00 [2026-06-30T18:42:32.157000+00:00] .salt555 (id=1521586755210317956) I’m working on a 3d printable case design for the pi5+nvme base+ battery hat +screen. CRT vibes with customizable back plate for any pi setup. [attachment] IMG_8189.mov https://cdn.discordapp.com/attachments/1521586755210317956/1521586755583868999/IMG_8189.mov?ex=6a455f98&is=6a440e18&hm=db97858d7e3a02654fe0f67c4b6826d7c3e28c881f92a4f820cbbe61d67b34df&

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1521586755210317956-Set-of-pi-cases-designed-for-Hermes.txt`

### retry-options-compared
- **Source:** `local:research/crow-lore/hermes-cron-failure-semantics/comparisons/retry-options-compared.md`
- **Raw:** `[[raw/local/retry-options-compared-98a153fdec.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Retry Options Compared created: 2026-06-30 updated: 2026-06-30 type: comparison tags: [retry, comparison, roadmap, design] source: github issue 32290, github issue 13566, github issue 17071, hermes-agent docs confidence: medium --- # Retry Options Compared Several proposals exist for adding retry semantics to Hermes cron. None are in core as of 2026-06-30. This table compares them along dimensions Senter would care about. ## The Options | Dimension | Provider Fallback (shipped) | Scheduler Retry (PR #16512) | Delivery Retry Queue (PR #26268) | Stage Persistence + Partial Retry (#17071) | Per-Skill Step 0 (pattern) | External Watchdog (pattern) |…

### prompt-toolkit
- **Source:** `local:research/crow-lore/custom-hermes-tui/entities/prompt-toolkit.md`
- **Raw:** `[[raw/local/prompt-toolkit-c12ee6da89.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # prompt_toolkit **Library** | Python | Active | Created by Jonathan Slenders `prompt_toolkit` is a library for building powerful interactive command-line applications in Python. It provides line editing, history, auto-completion, and syntax highlighting for REPLs and input prompts. ## Key Characteristics - **Line editing** — Emacs/Vi keybindings, undo/redo, kill ring - **Auto-completion** — fuzzy matching, customizable completers - **Syntax highlighting** — via Pygments - **Multi-line input** — with proper continuation prompts - **Mouse support** — limited to selection and basic clicks - **Cross-platform** — Linux, macOS, Windows - **Async support** — integrates with `asyncio` event loops…

### 1521290460008681572-Hermes-Mobile---a-small-PWA-plugin-for-the-existing-Hermes-Dashboard
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1521290460008681572-Hermes-Mobile---a-small-PWA-plugin-for-the-existing-Hermes-Dashboard.txt`
- **Raw:** `[[raw/discord/1521290460008681572-hermes-mobile---a-small-pwa-plugin-for-the-existing-hermes-dashboard-c05750f3b8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Mobile — a small PWA plugin for the existing Hermes Dashboard' in forum #plugins-skills-and-skins # thread_id=1521290460008681572 forum_id=1485392832154832906 # Started 2026-06-30T03:32:58.344742+00:00 [2026-06-29T23:05:09.876000+00:00] stasstep (id=1521290460008681572) I built this because Telegram is great for quick prompts, session switching, and approvals, but it doesn’t cover the way I use Hermes when real work is running. Sometimes I don’t want to chat with the agent. I want to quickly see what is happening: active sessions, approvals, activity, cron, kanban, system status, and agent profiles. There are already full WebUIs and dashboards with PWA support. This is not…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1521290460008681572-Hermes-Mobile---a-small-PWA-plugin-for-the-existing-Hermes-Dashboard.txt`

### 1518328533963903066-Hermes-Desktop---mod-pack---custom-theme--Veritas
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1518328533963903066-Hermes-Desktop---mod-pack---custom-theme--Veritas.txt`
- **Raw:** `[[raw/discord/1518328533963903066-hermes-desktop---mod-pack---custom-theme--veritas-3bf848cc2f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Desktop — mod pack + custom theme (Veritas) 🌌' in forum #plugins-skills-and-skins # thread_id=1518328533963903066 forum_id=1485392832154832906 # Started 2026-06-21T19:31:28.497669+00:00 [2026-06-21T18:55:31.677000+00:00] wise_mind (id=1518328533963903066) Hi, all, A handful of mods I run on **Hermes Desktop** to make it faster, smoother, and customizer it to my liking. ***This isn't a mod list, it's a feature list*** ## 🎙️ Improved Conversation Mode - - **Configrable conversation mode LLM** — configurable model (e.g. a fast local one) + switch between the regular LLM (Herme's model) and the voice one, then snap back to your normal model when you're done. Chat history…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1518328533963903066-Hermes-Desktop---mod-pack---custom-theme--Veritas.txt`

### 1521166357666861178-FLUID
- **Source:** `discord-archive:archives/community-projects-showcase/1521166357666861178-FLUID.txt`
- **Raw:** `[[raw/discord/1521166357666861178-fluid-78120d007b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'FLUID' in forum #community-projects-showcase # thread_id=1521166357666861178 forum_id=1316137596535177246 # Started 2026-06-29T15:42:22.505653+00:00 [2026-06-29T14:52:01.572000+00:00] enonforetsam (id=1521166357666861178) Make Cool Art in Your Browser - No Signup, Free Forever [attachment] Screenshot_2026-06-28_at_00.06.51.png https://cdn.discordapp.com/attachments/1521166357666861178/1521166368928698459/Screenshot_2026-06-28_at_00.06.51.png?ex=6a43d814&is=6a428694&hm=c3941ded2d7e6cc0c0578e10137eb114f29d1e40ec60a8593b5502008c8dcddb& [2026-06-29T14:52:39.618000+00:00] enonforetsam (id=1521166517243215943) https://fluid.krackeddevs.com/ [embed] FLUID — generative assets for your…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1521166357666861178-FLUID.txt`

### index
- **Source:** `local:research/crow-lore/discord-wiki-nous-scraper/index.md`
- **Raw:** `[[raw/local/index-d5f63f4c65.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Discord Wiki Channel Auto-Population from Nous Discord Scraper ## Executive Summary This lore bundle explores the feasibility and architecture of auto-populating Discord wiki channels from scraped content, specifically targeting the Nous Research Discord server and similar communities. **Key Finding:** Discord does **not** currently have a native "Wiki Channel" feature as of June 2026. The concept exists only as a community feature request (last active 2023). However, the system can be built using existing Discord channel types combined with scraper-to-publisher automation patterns. ## Core Entities - **Discord Wiki Channels** - Hypothetical feature (not yet implemented) - **Discord Forum…

### 1520968626985766962-tokenomics---LLM-spend-report---FinOps--inside-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520968626985766962-tokenomics---LLM-spend-report---FinOps--inside-Hermes.txt`
- **Raw:** `[[raw/discord/1520968626985766962-tokenomics---llm-spend-report---finops--inside-hermes-18bb7b946d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'tokenomics — LLM-spend report + FinOps, inside Hermes' in forum #plugins-skills-and-skins # thread_id=1520968626985766962 forum_id=1485392832154832906 # Started 2026-06-29T03:45:55.559244+00:00 [2026-06-29T01:46:18.904000+00:00] jasonperlow (id=1520968626985766962) Reads Hermes's own session store (~/.hermes/state.db — per-session tokens + cost) and prints a spend report or a FinOps view (allocation / realized $-per-Mtok / cheapest-equivalent advisor / burn forecast). Read-only, no core changes. Install + enable (plugins are opt-in): `hermes plugins install ncz-os/tokenomics` `hermes plugins enable tokenomics` `hermes gateway restart` (for the gateway/TUI; the CLI works right…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520968626985766962-tokenomics---LLM-spend-report---FinOps--inside-Hermes.txt`

### 1520932662850617434-Share-your-Pets
- **Source:** `discord-archive:archives/community-projects-showcase/1520932662850617434-Share-your-Pets.txt`
- **Raw:** `[[raw/discord/1520932662850617434-share-your-pets-61a6d373c9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Share your Pets!' in forum #community-projects-showcase # thread_id=1520932662850617434 forum_id=1316137596535177246 # Started 2026-06-29T03:40:33.654297+00:00 [2026-06-28T23:23:24.386000+00:00] dante.sparras (id=1520932662850617434) Wanna share your generated pets with the community. This is the place! [attachment] Recording_2026-06-29_011649.mp4 https://cdn.discordapp.com/attachments/1520932662850617434/1520932662947090592/Recording_2026-06-29_011649.mp4?ex=6a42fe6c&is=6a41acec&hm=6493a13e7587014f9de33f105109e93d99045e732e904185ff6eef07ae845953& [2026-06-28T23:24:19.771000+00:00] dante.sparras (id=1520932895152148531) here is my generated Super Saiyan Blue Gogeta pet…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520932662850617434-Share-your-Pets.txt`

### 1520732280220287097-Homelab-Guide
- **Source:** `discord-archive:archives/community-projects-showcase/1520732280220287097-Homelab-Guide.txt`
- **Raw:** `[[raw/discord/1520732280220287097-homelab-guide-708a7c946f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Homelab Guide' in forum #community-projects-showcase # thread_id=1520732280220287097 forum_id=1316137596535177246 # Started 2026-06-28T13:42:09.639119+00:00 [2026-06-28T10:07:09.444000+00:00] j0hnnybgoode (id=1520732280220287097) 1. get a 50$ NUC from ebay 2. follow the guide 3. enjoy your personal own homelab https://homelab-guide.netlify.app/ im not a tech-savy person, i was affraid id get stuck somewhere in the middle of the installation process. so i asked Claude to create me the most detailed and jargon-free tutorial so i can install Hermes on my cheap NUC, and access it from anywhere in the world. after countless back-n-forth, this is the final Guide version claude gave me.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520732280220287097-Homelab-Guide.txt`

### 1520652866782498827-MCP-for-Hermes-and-Tailscale
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520652866782498827-MCP-for-Hermes-and-Tailscale.txt`
- **Raw:** `[[raw/discord/1520652866782498827-mcp-for-hermes-and-tailscale-19e445b120.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'MCP for Hermes and Tailscale' in forum #plugins-skills-and-skins # thread_id=1520652866782498827 forum_id=1485392832154832906 # Started 2026-06-28T08:53:01.865080+00:00 [2026-06-28T04:51:35.805000+00:00] gumbyender (id=1520652866782498827) https://github.com/GumbyEnder/mcp-tailscale [embed] GitHub - GumbyEnder/mcp-tailscale: MCP server wrapping Tailscale CL... https://github.com/GumbyEnder/mcp-tailscale

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520652866782498827-MCP-for-Hermes-and-Tailscale.txt`

### 1520508292110094337-Pure-Python-scientific-computing-toolkit--no-NumPy-SciPy---FFT--ODEs--quadrature--linalg--stats
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520508292110094337-Pure-Python-scientific-computing-toolkit--no-NumPy-SciPy---FFT--ODEs--quadrature--linalg--stats.txt`
- **Raw:** `[[raw/discord/1520508292110094337-pure-python-scientific-computing-toolkit--no-numpy-scipy---fft--odes--quadrature--linalg--stats-ce21a6a28d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Pure-Python scientific computing toolkit (no NumPy/SciPy): FFT, ODEs, quadrature, linalg, stats' in forum #plugins-skills-and-skins # thread_id=1520508292110094337 forum_id=1485392832154832906 # Started 2026-06-27T19:22:32.142408+00:00 [2026-06-27T19:17:06.517000+00:00] 1453furox (id=1520508292110094337) Cognitive Discovery System (CDS) a scientific computing library written in pure Python. No NumPy, no SciPy, no compiled extensions. Zero dependencies, runs anywhere. 18 modules: quantum circuit simulation, FFT/IFFT, ODE solvers, numerical integration, linear algebra, statistics, Monte Carlo, optimization, graph algorithms, symbolic math, a from-scratch NLP stack (BPE → attention →…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520508292110094337-Pure-Python-scientific-computing-toolkit--no-NumPy-SciPy---FFT--ODEs--quadrature--linalg--stats.txt`

### 1520446713578524812-Live-voice-call---Hermes-Discord-plugin-integration
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520446713578524812-Live-voice-call---Hermes-Discord-plugin-integration.txt`
- **Raw:** `[[raw/discord/1520446713578524812-live-voice-call---hermes-discord-plugin-integration-ef84e48b68.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Live voice call - Hermes Discord plugin integration 📲' in forum #plugins-skills-and-skins # thread_id=1520446713578524812 forum_id=1485392832154832906 # Started 2026-06-27T19:22:33.232008+00:00 [2026-06-27T15:12:25.051000+00:00] capslock.b (id=1520446713578524812) **me and <@1377972181312606279> fixed <:catlick:1151260427645366375> the /voice command.... tts/stt is cringe <:catlick:1151260427645366375> ** We are building toward a Discord-native agent workspace where voice calls can become: > 🎙️ **Live agent sessions** > Full-duplex Discord voice into Gemini Live. > 🧠 **Structured planning** > SORA bridge elements turn messy calls into goals, subgoals, contradictions, and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520446713578524812-Live-voice-call---Hermes-Discord-plugin-integration.txt`

### 1520490884536467486-Potaco--CLI---Skill----Advanced-image-generation-and-editing-for-your-agents
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520490884536467486-Potaco--CLI---Skill----Advanced-image-generation-and-editing-for-your-agents.txt`
- **Raw:** `[[raw/discord/1520490884536467486-potaco--cli---skill----advanced-image-generation-and-editing-for-your-agents-b1dea61793.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Potaco (CLI + Skill) - Advanced image generation and editing for your agents' in forum #plugins-skills-and-skins # thread_id=1520490884536467486 forum_id=1485392832154832906 # Started 2026-06-27T19:22:32.780416+00:00 [2026-06-27T18:07:56.228000+00:00] ncxton (id=1520490884536467486) I made `potaco` skill for agents. It helps agents use the `potaco` CLI safely for image generation and editing. The skill covers: - Text-to-image generation - Image editing, inpainting, and outpainting - OpenAI, fal, Vercel AI Gateway, and custom OpenAI-compatible providers - Model discovery and provider setup guidance - Troubleshooting CLI failures without leaking credentials The main thing I wanted…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520490884536467486-Potaco--CLI---Skill----Advanced-image-generation-and-editing-for-your-agents.txt`

### 1520362930087137440-Nika--executable-workflows-for-Hermes-agents
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520362930087137440-Nika--executable-workflows-for-Hermes-agents.txt`
- **Raw:** `[[raw/discord/1520362930087137440-nika--executable-workflows-for-hermes-agents-f46da9d30d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Nika: executable workflows for Hermes agents' in forum #plugins-skills-and-skins # thread_id=1520362930087137440 forum_id=1485392832154832906 # Started 2026-06-27T13:33:13.028691+00:00 [2026-06-27T09:39:29.510000+00:00] thibaut5495 (id=1520362930087137440) Sharing Nika here because I’d love feedback from Hermes builders GitHub: https://github.com/supernovae-st/nika Docs: https://docs.nika.sh Site: https://nika.sh Nika is not a Hermes skin and not exactly a skill It’s an open-source language + local runtime for turning repeatable AI/agent work into executable .nika.yaml files. The idea is: Hermes can reason, use skills and decide what should happen. Nika makes the procedure…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520362930087137440-Nika--executable-workflows-for-Hermes-agents.txt`

### 1520403495901991094-How-well-can-LLMs-predict-the-future
- **Source:** `discord-archive:archives/community-projects-showcase/1520403495901991094-How-well-can-LLMs-predict-the-future.txt`
- **Raw:** `[[raw/discord/1520403495901991094-how-well-can-llms-predict-the-future-43c4a292e9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'How well can LLMs predict the future' in forum #community-projects-showcase # thread_id=1520403495901991094 forum_id=1316137596535177246 # Started 2026-06-27T13:28:18.105273+00:00 [2026-06-27T12:20:41.154000+00:00] aleleta (id=1520403495901991094) did some work on evaling LLMs on how well they can predict the future! https://x.com/agapekeleta/status/2070818483068129581?s=46 benchmark also here: https://benchmark.aleatoricai.com [attachment] IMG_5644.jpg https://cdn.discordapp.com/attachments/1520403495901991094/1520403496577269942/IMG_5644.jpg?ex=6a411199&is=6a3fc019&hm=7046a49f197cf3a459a7f6d7a382a12026df4254d85b6d92caf19a0fb7e65797& [embed]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520403495901991094-How-well-can-LLMs-predict-the-future.txt`

### 1520508436377501898-Pure-Python-scientific-computing-toolkit--no-NumPy-SciPy---FFT--ODEs--quadrature--linalg--stats
- **Source:** `discord-archive:archives/community-projects-showcase/1520508436377501898-Pure-Python-scientific-computing-toolkit--no-NumPy-SciPy---FFT--ODEs--quadrature--linalg--stats.txt`
- **Raw:** `[[raw/discord/1520508436377501898-pure-python-scientific-computing-toolkit--no-numpy-scipy---fft--odes--quadrature--linalg--stats-a6bb352dd7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Pure-Python scientific computing toolkit (no NumPy/SciPy): FFT, ODEs, quadrature, linalg, stats' in forum #community-projects-showcase # thread_id=1520508436377501898 forum_id=1316137596535177246 # Started 2026-06-28T03:36:03.429058+00:00 [2026-06-27T19:17:40.913000+00:00] 1453furox (id=1520508436377501898) Cognitive Discovery System (CDS) a scientific computing library written in pure Python. No NumPy, no SciPy, no compiled extensions. Zero dependencies, runs anywhere. 18 modules: quantum circuit simulation, FFT/IFFT, ODE solvers, numerical integration, linear algebra, statistics, Monte Carlo, optimization, graph algorithms, symbolic math, a from-scratch NLP stack (BPE →…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520508436377501898-Pure-Python-scientific-computing-toolkit--no-NumPy-SciPy---FFT--ODEs--quadrature--linalg--stats.txt`

### 1520447548702331104-We-fixed-the--voice-command----NEED-HELP
- **Source:** `discord-archive:archives/community-projects-showcase/1520447548702331104-We-fixed-the--voice-command----NEED-HELP.txt`
- **Raw:** `[[raw/discord/1520447548702331104-we-fixed-the--voice-command----need-help-e766c94bf8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'We fixed the /voice command - NEED HELP !' in forum #community-projects-showcase # thread_id=1520447548702331104 forum_id=1316137596535177246 # Started 2026-06-27T19:17:29.198520+00:00 [2026-06-27T15:15:44.160000+00:00] capslock.b (id=1520447548702331104) **me and <@1377972181312606279> fixed <:catlick:1151260427645366375> the /voice command.... tts/stt is cringe <:catlick:1151260427645366375> ** We are building toward a Discord-native agent workspace where voice calls can become: > 🎙️ **Live agent sessions** > Full-duplex Discord voice into Gemini Live. > 🧠 **Structured planning** > SORA bridge elements turn messy calls into goals, subgoals, contradictions, and acceptance…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520447548702331104-We-fixed-the--voice-command----NEED-HELP.txt`

### 1520284223250890903-CLI-for-image-generation-and-editing-with-advanced-features--inpaint--outpaint--and-more-soon..
- **Source:** `discord-archive:archives/community-projects-showcase/1520284223250890903-CLI-for-image-generation-and-editing-with-advanced-features--inpaint--outpaint--and-more-soon...txt`
- **Raw:** `[[raw/discord/1520284223250890903-cli-for-image-generation-and-editing-with-advanced-features--inpaint--outpaint--and-more-soon..-5ced189c4b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'CLI for image generation and editing with advanced features (inpaint, outpaint, and more soon..)' in forum #community-projects-showcase # thread_id=1520284223250890903 forum_id=1316137596535177246 # Started 2026-06-27T08:33:26.030343+00:00 [2026-06-27T04:26:44.338000+00:00] ncxton (id=1520284223250890903) i'm working on Potaco, a CLI for image generation and editing across multiple AI providers (OpenAI, fal, Vercel AI Gateway, or any OpenAI-compatible endpoint) why use Potaco over the built-in tool? - **image editing** — inpainting with masks (white=edit, black=keep), rectangular/circular masks, and outpainting to extend a canvas. The built-in tool only does generation. -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520284223250890903-CLI-for-image-generation-and-editing-with-advanced-features--inpaint--outpaint--and-more-soon...txt`

### 1520229733864964337-Hermes-Agent-for-Science
- **Source:** `discord-archive:archives/community-projects-showcase/1520229733864964337-Hermes-Agent-for-Science.txt`
- **Raw:** `[[raw/discord/1520229733864964337-hermes-agent-for-science-52b176c1c8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Agent for Science' in forum #community-projects-showcase # thread_id=1520229733864964337 forum_id=1316137596535177246 # Started 2026-06-27T02:53:43.763668+00:00 [2026-06-27T00:50:13.056000+00:00] mysterious_moose_98367 (id=1520229733864964337) DM me if you are interested. I'm will be dishing out closed tests for the next few days. https://tj-coding.github.io/nautilus-community/ [embed] Nautilus Agent — AI for Scientists https://tj-coding.github.io/nautilus-community/

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520229733864964337-Hermes-Agent-for-Science.txt`

### 1520128681463382166-Hermes-Eats-World
- **Source:** `discord-archive:archives/community-projects-showcase/1520128681463382166-Hermes-Eats-World.txt`
- **Raw:** `[[raw/discord/1520128681463382166-hermes-eats-world-dd73f6e68e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Eats World' in forum #community-projects-showcase # thread_id=1520128681463382166 forum_id=1316137596535177246 # Started 2026-06-26T19:43:57.422005+00:00 [2026-06-26T18:08:40.286000+00:00] jw_mushroom_man (id=1520128681463382166) Hermes Eats World — hand Hermes any running Windows application and it wraps around it, ingests it, and operates it under your direction. Instead of screenshot-and-click theater, it perceives the app as structure: walk the UIA tree, classify a tier (native API → accessibility → vision fallback), act through real control patterns, and verify against a pre/post snapshot diff. Runs as a Python WebSocket sidecar Hermes calls as a tool, with every…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520128681463382166-Hermes-Eats-World.txt`

### 1519939284474265620-Darkphoto
- **Source:** `discord-archive:archives/community-projects-showcase/1519939284474265620-Darkphoto.txt`
- **Raw:** `[[raw/discord/1519939284474265620-darkphoto-2de58f0908.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Darkphoto' in forum #community-projects-showcase # thread_id=1519939284474265620 forum_id=1316137596535177246 # Started 2026-06-26T09:21:23.984343+00:00 [2026-06-26T05:36:04.525000+00:00] americanbiker (id=1519939284474265620) This site and artwork was all made with Hermes & Comfy - if you like B&W pictures? enjoy - https://www.darkphoto.org/ [attachment] path-of-reflections.webp https://cdn.discordapp.com/attachments/1519939284474265620/1519939284948353164/path-of-reflections.webp?ex=6a3f6144&is=6a3e0fc4&hm=3b4984f1b8b58dccf0dba5a5e3b71d9feb6c1ec443a55abe4194da055b7518d9& [embed] darkphoto — a black & white photography marketplace https://www.darkphoto.org/…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1519939284474265620-Darkphoto.txt`

### distribution
- **Source:** `local:projects/sovth-config/profiles/sirvir/distribution.yaml`
- **Raw:** `[[raw/local/distribution-83ac8b39d7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # distribution.yaml — Sirvir profile distribution manifest # Install with: hermes profile install https://github.com/SouthpawIN/sirvir name: sirvir version: "1.0.0" description: >- Model fleet manager and intelligence engine for Hermes Agent. Autonomous model lifecycle manager — local serving, benchmarking, auto-scaling, API fallback, HuggingFace scanning, creator tracking, backend optimization, budget monitoring, external app endpoint serving, and consolidated logging. author: SouthpawIN license: MIT homepage: https://github.com/SouthpawIN/sirvir repo: https://github.com/SouthpawIN/sirvir hermes_requires: ">=0.12.0" env_requires: - name: NVIDIA_API_KEY description: NVIDIA NIM API key for…

- **Collapsed duplicates:** `local:projects/sirvir/distribution.yaml`

### guide
- **Source:** `local:docs/cross-profile-skill-visibility/guide.md`
- **Raw:** `[[raw/local/guide-f72b11a9a4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Cross-Profile Skill Visibility Fix in Hermes ## Summary When you install a skill into the default profile at `~/.hermes/skills-capabilities/`, it does **not** automatically appear in profile-scoped agent directories. A profile launched with `hermes -p <name>` only reads skills from its own `~/.hermes/profiles/<name>/skills-capabilities/` tree. If the skill directory is missing there, the agent cannot load it — `skill_view` will fail and `skill_list` will omit it, even though the skill exists globally. The fix is a straightforward recursive copy: This preserves the `category/skill-name/` nesting that Hermes uses to resolve skill paths. You need to repeat the copy for every profile that should see the skill, and…

### SKILL
- **Source:** `local:projects/southpaw/anser/skills-capabilities/productivity-office/productivity-office-tools/SKILL.md`
- **Raw:** `[[raw/local/skill-2f6dec7074.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: productivity-office-tools description: "Productivity & office tools: Airtable, Google Workspace, Notion, PowerPoint, Maps, nano-pdf, Obsidian, Teams meetings, Email (Himalaya)." version: 1.0.0 author: Hermes Agent license: MIT tags: ["productivity", "office", "airtable", "google-workspace", "notion", "powerpoint", "maps", "obsidian", "teams", "email", "pdf"] platforms: [linux, macos, windows] metadata: hermes: tags: [productivity, office, airtable, google-workspace, notion, powerpoint, maps, obsidian, teams, email, pdf] category: productivity-office related_skills: [social-media-communication, smart-home-iot, creative-design-systems] --- # Productivity & Office Tools Unified skill…

- **Collapsed duplicates:** `local:projects/anser/skills-capabilities/productivity-office/productivity-office-tools/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/yuanbao/SKILL.md`
- **Raw:** `[[raw/local/skill-239e4875f5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: yuanbao description: "Yuanbao (元宝) groups: @mention users, query info/members." version: 1.0.0 platforms: [linux, macos, windows] metadata: hermes: tags: [yuanbao, mention, at, group, members, 元宝, 派, 艾特] related_skills: [] --- # Yuanbao Group Interaction ## CRITICAL: How Messaging Works **Your text reply IS the message sent to the group/user.** The gateway automatically delivers your response text to the chat. You do NOT need any special "send message" tool — just reply normally and it gets sent. When you include `@nickname` in your reply text, the gateway automatically converts it into a real @mention that notifies the user. This is built-in — you have full @mention capability.…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/yuanbao/SKILL.md`, `local:projects/jestur/skills-capabilities/yuanbao/SKILL.md`, `local:projects/dev-coder/skills-capabilities/yuanbao/SKILL.md`, `local:projects/dev-orch/skills-capabilities/yuanbao/SKILL.md`, `local:projects/dev-review/skills-capabilities/yuanbao/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/software-development/test-driven-development/SKILL.md`
- **Raw:** `[[raw/local/skill-39361054f5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: test-driven-development description: "TDD: enforce RED-GREEN-REFACTOR, tests before code." version: 1.1.0 author: Hermes Agent (adapted from obra/superpowers) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [testing, tdd, development, quality, red-green-refactor] related_skills: [systematic-debugging, plan, subagent-driven-development] --- # Test-Driven Development (TDD) ## Overview Write the test first. Watch it fail. Write minimal code to pass. **Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing. **Violating the letter of the rules is violating the spirit of the rules.** ## When to Use **Always:** - New…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/software-development/test-driven-development/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/software-development/systematic-debugging/SKILL.md`
- **Raw:** `[[raw/local/skill-ec6c97b1d5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: systematic-debugging description: "4-phase root cause debugging: understand bugs before fixing." version: 1.1.0 author: Hermes Agent (adapted from obra/superpowers) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [debugging, troubleshooting, problem-solving, root-cause, investigation] related_skills: [test-driven-development, plan, subagent-driven-development] --- # Systematic Debugging ## Overview Random fixes waste time and create new bugs. Quick patches mask underlying issues. **Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure. **Violating the letter of this process is violating the spirit of debugging.** ## The…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/software-development/systematic-debugging/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/software-development/spike/SKILL.md`
- **Raw:** `[[raw/local/skill-891bc0a6fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: spike description: "Throwaway experiments to validate an idea before build." version: 1.0.0 author: Hermes Agent (adapted from gsd-build/get-shit-done) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [spike, prototype, experiment, feasibility, throwaway, exploration, research, planning, mvp, proof-of-concept] related_skills: [sketch, subagent-driven-development, plan] --- # Spike Use this skill when the user wants to **feel out an idea** before committing to a real build — validating feasibility, comparing approaches, or surfacing unknowns that no amount of research will answer. Spikes are disposable by design. Throw them away once they've paid their debt.…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/software-development/spike/SKILL.md`, `local:projects/jestur/skills-capabilities/software-development/spike/SKILL.md`, `local:projects/dev-coder/skills-capabilities/software-development/spike/SKILL.md`, `local:projects/dev-orch/skills-capabilities/software-development/spike/SKILL.md`, `local:projects/dev-review/skills-capabilities/software-development/spike/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/software-development/plan/SKILL.md`
- **Raw:** `[[raw/local/skill-399038641c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: plan description: "Plan mode: write an actionable markdown plan to .hermes/plans/, no execution. Bite-sized tasks, exact paths, complete code." version: 2.0.0 author: Hermes Agent (writing-craft adapted from obra/superpowers) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [planning, plan-mode, implementation, workflow, design, documentation] related_skills: [subagent-driven-development, test-driven-development, requesting-code-review] --- # Plan Mode Use this skill when the user wants a plan instead of execution. ## Core behavior For this turn, you are planning only. - Do not implement code. - Do not edit project files except the plan markdown file. - Do…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/software-development/plan/SKILL.md`, `local:projects/jestur/skills-capabilities/software-development/plan/SKILL.md`, `local:projects/dev-coder/skills-capabilities/software-development/plan/SKILL.md`, `local:projects/dev-orch/skills-capabilities/software-development/plan/SKILL.md`, `local:projects/dev-review/skills-capabilities/software-development/plan/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/software-development/debugging-hermes-tui-commands/SKILL.md`
- **Raw:** `[[raw/local/skill-55d5811c0b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: debugging-hermes-tui-commands description: "Debug Hermes TUI slash commands: Python, gateway, Ink UI." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [debugging, hermes-agent, tui, slash-commands, typescript, python] related_skills: [python-debugpy, node-inspect-debugger, systematic-debugging] --- # Debugging Hermes TUI Slash Commands ## Overview Hermes slash commands span three layers — Python command registry, tui_gateway JSON-RPC bridge, and the Ink/TypeScript frontend. When a command misbehaves (missing from autocomplete, works in CLI but not TUI, config persists but UI doesn't update), the bug is almost always one…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/software-development/debugging-hermes-tui-commands/SKILL.md`, `local:projects/jestur/skills-capabilities/software-development/debugging-hermes-tui-commands/SKILL.md`, `local:projects/dev-coder/skills-capabilities/software-development/debugging-hermes-tui-commands/SKILL.md`, `local:projects/dev-orch/skills-capabilities/software-development/debugging-hermes-tui-commands/SKILL.md`, `local:projects/dev-review/skills-capabilities/software-development/debugging-hermes-tui-commands/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/software-development/hermes-agent-skill-authoring/SKILL.md`
- **Raw:** `[[raw/local/skill-7d3aa79739.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: hermes-agent-skill-authoring description: "Author in-repo SKILL.md: frontmatter, validator, structure, and writing-quality principles." version: 1.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [skills, authoring, hermes-agent, conventions, skill-md] related_skills: [plan, requesting-code-review] --- # Authoring Hermes-Agent Skills (in-repo) ## Overview There are two places a SKILL.md can live: 1. **User-local:** `~/.hermes/skills-capabilities/<maybe-category>/<name>/SKILL.md` — personal, not shared. Created via `skill_manage(action='create')`. 2. **In-repo (this skill is about this case):**…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/software-development/hermes-agent-skill-authoring/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/social-media/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-2ea0d50444.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for interacting with social platforms and social-media workflows — posting, reading, monitoring, and account operations. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/social-media/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/social-media/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/social-media/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/social-media/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/social-media/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/smart-home/openhue/SKILL.md`
- **Raw:** `[[raw/local/skill-550f94848d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: openhue description: "Control Philips Hue lights, scenes, rooms via OpenHue CLI." version: 1.0.0 author: community license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [Smart-Home, Hue, Lights, IoT, Automation] homepage: https://www.openhue.io/cli prerequisites: commands: [openhue] --- # OpenHue CLI Control Philips Hue lights and scenes via a Hue Bridge from the terminal. ## Prerequisites First run requires pressing the button on your Hue Bridge to pair. The bridge must be on the same local network. ## When to Use - "Turn on/off the lights" - "Dim the living room lights" - "Set a scene" or "movie mode" - Controlling specific Hue rooms, zones, or individual bulbs…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/smart-home/openhue/SKILL.md`, `local:projects/jestur/skills-capabilities/smart-home/openhue/SKILL.md`, `local:projects/dev-coder/skills-capabilities/smart-home/openhue/SKILL.md`, `local:projects/dev-orch/skills-capabilities/smart-home/openhue/SKILL.md`, `local:projects/dev-review/skills-capabilities/smart-home/openhue/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/smart-home/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-34a853f25b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for controlling smart home devices — lights, switches, sensors, and home automation systems. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/smart-home/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/smart-home/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/smart-home/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/smart-home/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/smart-home/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/research/polymarket/SKILL.md`
- **Raw:** `[[raw/local/skill-becfa71e73.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: polymarket description: "Query Polymarket: markets, prices, orderbooks, history." version: 1.0.0 author: Hermes Agent + Teknium tags: [polymarket, prediction-markets, market-data, trading] platforms: [linux, macos, windows] --- # Polymarket — Prediction Market Data Query prediction market data from Polymarket using their public REST APIs. All endpoints are read-only and require zero authentication. See `references/api-endpoints.md` for the full endpoint reference with curl examples. ## When to Use - User asks about prediction markets, betting odds, or event probabilities - User wants to know "what are the odds of X happening?" - User asks about Polymarket specifically - User wants…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/research/polymarket/SKILL.md`, `local:projects/jestur/skills-capabilities/research/polymarket/SKILL.md`, `local:projects/dev-coder/skills-capabilities/research/polymarket/SKILL.md`, `local:projects/dev-orch/skills-capabilities/research/polymarket/SKILL.md`, `local:projects/dev-review/skills-capabilities/research/polymarket/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/research/blogwatcher/SKILL.md`
- **Raw:** `[[raw/local/skill-b85be5a9b8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: blogwatcher description: "Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool." version: 2.0.0 author: JulienTant (fork of Hyaxia/blogwatcher) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [RSS, Blogs, Feed-Reader, Monitoring] homepage: https://github.com/JulienTant/blogwatcher-cli prerequisites: commands: [blogwatcher-cli] --- # Blogwatcher Track blog and RSS/Atom feed updates with the `blogwatcher-cli` tool. Supports automatic feed discovery, HTML scraping fallback, OPML import, and read/unread article management. ## Installation Pick one method: - **Go:** `go install github.com/JulienTant/blogwatcher-cli/cmd/blogwatcher-cli@latest` - **Docker:**…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/research/blogwatcher/SKILL.md`, `local:projects/jestur/skills-capabilities/research/blogwatcher/SKILL.md`, `local:projects/dev-coder/skills-capabilities/research/blogwatcher/SKILL.md`, `local:projects/dev-orch/skills-capabilities/research/blogwatcher/SKILL.md`, `local:projects/dev-review/skills-capabilities/research/blogwatcher/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/research/arxiv/SKILL.md`
- **Raw:** `[[raw/local/skill-2a6073a1ad.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: arxiv description: "Search arXiv papers by keyword, author, category, or ID." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [Research, Arxiv, Papers, Academic, Science, API] related_skills: [ocr-and-documents] --- # arXiv Research Search and retrieve academic papers from arXiv via their free REST API. No API key, no dependencies — just curl. ## Quick Reference | Action | Command | |--------|---------| | Search papers | `curl "https://export.arxiv.org/api/query?search_query=all:QUERY&max_results=5"` | | Get specific paper | `curl "https://export.arxiv.org/api/query?id_list=2402.03300"` | | Read abstract (web) |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/research/arxiv/SKILL.md`, `local:projects/jestur/skills-capabilities/research/arxiv/SKILL.md`, `local:projects/dev-coder/skills-capabilities/research/arxiv/SKILL.md`, `local:projects/dev-orch/skills-capabilities/research/arxiv/SKILL.md`, `local:projects/dev-review/skills-capabilities/research/arxiv/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/research/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-a7bc842330.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for academic research, paper discovery, literature review, domain reconnaissance, market data, content monitoring, and scientific knowledge retrieval. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/research/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/research/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/research/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/research/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/research/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/powerpoint/SKILL.md`
- **Raw:** `[[raw/local/skill-bb2084f5da.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: powerpoint description: "Create, read, edit .pptx decks, slides, notes, templates." license: Proprietary. LICENSE.txt has complete terms platforms: [linux, macos, windows] --- # Powerpoint Skill ## When to use Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/powerpoint/SKILL.md`, `local:projects/jestur/skills-capabilities/productivity/powerpoint/SKILL.md`, `local:projects/dev-coder/skills-capabilities/productivity/powerpoint/SKILL.md`, `local:projects/dev-orch/skills-capabilities/productivity/powerpoint/SKILL.md`, `local:projects/dev-review/skills-capabilities/productivity/powerpoint/SKILL.md`

### LICENSE
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/powerpoint/LICENSE.txt`
- **Raw:** `[[raw/local/license-79f6d8f5b4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** © 2025 Anthropic, PBC. All rights reserved. LICENSE: Use of these materials (including all code, prompts, assets, files, and other components of this Skill) is governed by your agreement with Anthropic regarding use of Anthropic's services. If no separate agreement exists, use is governed by Anthropic's Consumer Terms of Service or Commercial Terms of Service, as applicable: https://www.anthropic.com/legal/consumer-terms https://www.anthropic.com/legal/commercial-terms Your applicable agreement is referred to as the "Agreement." "Services" are as defined in the Agreement. ADDITIONAL RESTRICTIONS: Notwithstanding anything in the Agreement to the contrary, users may not: - Extract these…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/powerpoint/LICENSE.txt`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/ocr-and-documents/SKILL.md`
- **Raw:** `[[raw/local/skill-720a1f1a53.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ocr-and-documents description: "Extract text from PDFs/scans (pymupdf, marker-pdf)." version: 2.3.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [PDF, Documents, Research, Arxiv, Text-Extraction, OCR] related_skills: [powerpoint] --- # PDF & Document Extraction For DOCX: use `python-docx` (parses actual document structure, far better than OCR). For PPTX: see the `powerpoint` skill (uses `python-pptx` with full slide/notes support). This skill covers **PDFs and scanned documents**. ## Step 1: Remote URL Available? If the document has a URL, **always try `web_extract` first**: This handles PDF-to-markdown conversion via Firecrawl with…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/ocr-and-documents/SKILL.md`, `local:projects/jestur/skills-capabilities/productivity/ocr-and-documents/SKILL.md`, `local:projects/dev-coder/skills-capabilities/productivity/ocr-and-documents/SKILL.md`, `local:projects/dev-orch/skills-capabilities/productivity/ocr-and-documents/SKILL.md`, `local:projects/dev-review/skills-capabilities/productivity/ocr-and-documents/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/ocr-and-documents/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-0da2ba89cf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for extracting text from PDFs, scanned documents, images, and other file formats using OCR and document parsing tools. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/ocr-and-documents/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/productivity/ocr-and-documents/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/productivity/ocr-and-documents/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/productivity/ocr-and-documents/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/productivity/ocr-and-documents/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/nano-pdf/SKILL.md`
- **Raw:** `[[raw/local/skill-4243b32978.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: nano-pdf description: "Edit PDF text/typos/titles via nano-pdf CLI (NL prompts)." version: 1.0.0 author: community license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [PDF, Documents, Editing, NLP, Productivity] homepage: https://pypi.org/project/nano-pdf/ --- # nano-pdf Edit PDFs using natural-language instructions. Point it at a page and describe what to change. ## Prerequisites ## Usage ## Examples ## Notes - Page numbers may be 0-based or 1-based depending on version — if the edit hits the wrong page, retry with ±1 - Always verify the output PDF after editing (use `read_file` to check file size, or open it) - The tool uses an LLM under the hood — requires…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/nano-pdf/SKILL.md`, `local:projects/jestur/skills-capabilities/productivity/nano-pdf/SKILL.md`, `local:projects/dev-coder/skills-capabilities/productivity/nano-pdf/SKILL.md`, `local:projects/dev-orch/skills-capabilities/productivity/nano-pdf/SKILL.md`, `local:projects/dev-review/skills-capabilities/productivity/nano-pdf/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/maps/SKILL.md`
- **Raw:** `[[raw/local/skill-8c961ecf66.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: maps description: "Geocode, POIs, routes, timezones via OpenStreetMap/OSRM." version: 1.2.0 author: Mibayy license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [maps, geocoding, places, routing, distance, directions, nearby, location, openstreetmap, nominatim, overpass, osrm] category: productivity requires_toolsets: [terminal] supersedes: [find-nearby] --- # Maps Skill Location intelligence using free, open data sources. 8 commands, 44 POI categories, zero dependencies (Python stdlib only), no API key required. Data sources: OpenStreetMap/Nominatim, Overpass API, OSRM, TimeAPI.io. This skill supersedes the old `find-nearby` skill — all of find-nearby's…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/maps/SKILL.md`, `local:projects/jestur/skills-capabilities/productivity/maps/SKILL.md`, `local:projects/dev-coder/skills-capabilities/productivity/maps/SKILL.md`, `local:projects/dev-orch/skills-capabilities/productivity/maps/SKILL.md`, `local:projects/dev-review/skills-capabilities/productivity/maps/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/google-workspace/SKILL.md`
- **Raw:** `[[raw/local/skill-014a4818ee.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: google-workspace description: "Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python." version: 1.1.0 author: Nous Research license: MIT platforms: [linux, macos, windows] required_credential_files: - path: google_token.json description: Google OAuth2 token (created by setup script) - path: google_client_secret.json description: Google OAuth2 client credentials (downloaded from Google Cloud Console) metadata: hermes: tags: [Google, Gmail, Calendar, Drive, Sheets, Docs, Contacts, Email, OAuth] homepage: https://github.com/NousResearch/hermes-agent related_skills: [himalaya] --- # Google Workspace Gmail, Calendar, Drive, Contacts, Sheets, and Docs — through Hermes-managed OAuth…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/google-workspace/SKILL.md`, `local:projects/jestur/skills-capabilities/productivity/google-workspace/SKILL.md`, `local:projects/dev-coder/skills-capabilities/productivity/google-workspace/SKILL.md`, `local:projects/dev-orch/skills-capabilities/productivity/google-workspace/SKILL.md`, `local:projects/dev-review/skills-capabilities/productivity/google-workspace/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/airtable/SKILL.md`
- **Raw:** `[[raw/local/skill-18029f2ef3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: airtable description: Airtable REST API via curl. Records CRUD, filters, upserts. version: 1.1.0 author: community license: MIT platforms: [linux, macos, windows] prerequisites: env_vars: [AIRTABLE_API_KEY] commands: [curl] metadata: hermes: tags: [Airtable, Productivity, Database, API] homepage: https://airtable.com/developers/web/api/introduction --- # Airtable — Bases, Tables & Records Work with Airtable's REST API directly via `curl` using the `terminal` tool. No MCP server, no OAuth flow, no Python SDK — just `curl` and a personal access token. ## Prerequisites 1. Create a **Personal Access Token (PAT)** at https://airtable.com/create/tokens (tokens start with `pat...`). 2.…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/airtable/SKILL.md`, `local:projects/jestur/skills-capabilities/productivity/airtable/SKILL.md`, `local:projects/dev-coder/skills-capabilities/productivity/airtable/SKILL.md`, `local:projects/dev-orch/skills-capabilities/productivity/airtable/SKILL.md`, `local:projects/dev-review/skills-capabilities/productivity/airtable/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-b5a494a45b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for document creation, presentations, spreadsheets, and other productivity workflows. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/productivity/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/productivity/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/productivity/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/productivity/DESCRIPTION.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/note-taking/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-fb28a60937.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Note taking skills, to save information, assist with research, and collab on multi-session planning and information sharing. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/note-taking/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/note-taking/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/note-taking/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/note-taking/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/note-taking/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/training/unsloth/SKILL.md`
- **Raw:** `[[raw/local/skill-05961478fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: unsloth description: "Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM." version: 1.0.0 author: Orchestra Research license: MIT dependencies: [unsloth, torch, transformers, trl, datasets, peft] metadata: hermes: tags: [Fine-Tuning, Unsloth, Fast Training, LoRA, QLoRA, Memory-Efficient, Optimization, Llama, Mistral, Gemma, Qwen] --- # Unsloth Skill Comprehensive assistance with unsloth development, generated from official documentation. ## When to Use This Skill This skill should be triggered when: - Working with unsloth - Asking about unsloth features or APIs - Implementing unsloth solutions - Debugging unsloth code - Learning unsloth best practices ## Quick Reference ###…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/training/unsloth/SKILL.md`, `local:projects/jestur/skills-capabilities/mlops/training/unsloth/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/mlops/models/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-97a8c2c6c7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Specific model architectures and tools — image segmentation (Segment Anything / SAM) and audio generation (AudioCraft / MusicGen). Additional model skills (CLIP, Stable Diffusion, Whisper, LLaVA) are available as optional skills. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/mlops/models/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/mlops/models/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/media/spotify/SKILL.md`
- **Raw:** `[[raw/local/skill-84b4c86e75.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: spotify description: "Spotify: play, search, queue, manage playlists and devices." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] prerequisites: tools: [spotify_playback, spotify_devices, spotify_queue, spotify_search, spotify_playlists, spotify_albums, spotify_library] metadata: hermes: tags: [spotify, music, playback, playlists, media] related_skills: [gif-search] --- # Spotify Control the user's Spotify account via the Hermes Spotify toolset (7 tools). Setup guide: https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify ## When to use this skill The user says something like "play X", "pause", "skip", "queue up X", "what's…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/media/spotify/SKILL.md`, `local:projects/jestur/skills-capabilities/media/spotify/SKILL.md`, `local:projects/dev-coder/skills-capabilities/media/spotify/SKILL.md`, `local:projects/dev-orch/skills-capabilities/media/spotify/SKILL.md`, `local:projects/dev-review/skills-capabilities/media/spotify/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/media/youtube-content/SKILL.md`
- **Raw:** `[[raw/local/skill-03cba418b1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: youtube-content description: "YouTube transcripts to summaries, threads, blogs." platforms: [linux, macos, windows] --- # YouTube Content Tool ## When to use Use when the user shares a YouTube URL or video link, asks to summarize a video, requests a transcript, or wants to extract and reformat content from any YouTube video. Transforms transcripts into structured content (chapters, summaries, threads, blog posts). Extract transcripts from YouTube videos and convert them into useful formats. ## Setup Use `uv` so the dependency is installed into the same Hermes-managed environment that runs the helper script: ## Helper Script `SKILL_DIR` is the directory containing this SKILL.md…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/media/youtube-content/SKILL.md`, `local:projects/jestur/skills-capabilities/media/youtube-content/SKILL.md`, `local:projects/dev-coder/skills-capabilities/media/youtube-content/SKILL.md`, `local:projects/dev-orch/skills-capabilities/media/youtube-content/SKILL.md`, `local:projects/dev-review/skills-capabilities/media/youtube-content/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/media/gif-search/SKILL.md`
- **Raw:** `[[raw/local/skill-603735e1cb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: gif-search description: "Search/download GIFs from Tenor via curl + jq." version: 1.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] prerequisites: env_vars: [TENOR_API_KEY] commands: [curl, jq] metadata: hermes: tags: [GIF, Media, Search, Tenor, API] --- # GIF Search (Tenor API) Search and download GIFs directly via the Tenor API using curl. No extra tools needed. ## When to use Useful for finding reaction GIFs, creating visual content, and sending GIFs in chat. ## Setup Set your Tenor API key in your environment (add to `${HERMES_HOME:-~/.hermes}/.env`): Get a free API key at https://developers.google.com/tenor/guides/quickstart — the Google Cloud Console…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/media/gif-search/SKILL.md`, `local:projects/jestur/skills-capabilities/media/gif-search/SKILL.md`, `local:projects/dev-coder/skills-capabilities/media/gif-search/SKILL.md`, `local:projects/dev-orch/skills-capabilities/media/gif-search/SKILL.md`, `local:projects/dev-review/skills-capabilities/media/gif-search/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/media/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-c27bb2f0f3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for working with media content — YouTube transcripts, GIF search, music generation, and audio visualization. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/media/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/media/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/media/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/media/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/media/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/github-issues/SKILL.md`
- **Raw:** `[[raw/local/skill-f0e40babad.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: github-issues description: "Create, triage, label, assign GitHub issues via gh or REST." version: 1.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [GitHub, Issues, Project-Management, Bug-Tracking, Triage] related_skills: [github-auth, github-pr-workflow] --- # GitHub Issues Management Create, search, triage, and manage GitHub issues. Each section shows `gh` first, then the `curl` fallback. ## Prerequisites - Authenticated with GitHub (see `github-auth` skill) - Inside a git repo with a GitHub remote, or specify the repo explicitly ### Setup --- ## 1. Viewing Issues **With gh:** **With curl:** ## 2. Creating Issues **With gh:**…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/github-issues/SKILL.md`, `local:projects/jestur/skills-capabilities/github/github-issues/SKILL.md`, `local:projects/dev-coder/skills-capabilities/github/github-issues/SKILL.md`, `local:projects/dev-orch/skills-capabilities/github/github-issues/SKILL.md`, `local:projects/dev-review/skills-capabilities/github/github-issues/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/github-code-review/SKILL.md`
- **Raw:** `[[raw/local/skill-a0b1376fbe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: github-code-review description: "Review PRs: diffs, inline comments via gh or REST." version: 1.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [GitHub, Code-Review, Pull-Requests, Git, Quality] related_skills: [github-auth, github-pr-workflow] --- # GitHub Code Review Perform code reviews on local changes before pushing, or review open PRs on GitHub. Most of this skill uses plain `git` — the `gh`/`curl` split only matters for PR-level interactions. ## Prerequisites - Authenticated with GitHub (see `github-auth` skill) - Inside a git repository ### Setup (for PR interactions) --- ## 1. Reviewing Local Changes (Pre-Push) This is pure…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/github-code-review/SKILL.md`, `local:projects/jestur/skills-capabilities/github/github-code-review/SKILL.md`, `local:projects/dev-coder/skills-capabilities/github/github-code-review/SKILL.md`, `local:projects/dev-orch/skills-capabilities/github/github-code-review/SKILL.md`, `local:projects/dev-review/skills-capabilities/github/github-code-review/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/codebase-inspection/SKILL.md`
- **Raw:** `[[raw/local/skill-87ddc0578d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: codebase-inspection description: "Inspect codebases w/ pygount: LOC, languages, ratios." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [LOC, Code Analysis, pygount, Codebase, Metrics, Repository] related_skills: [github-repo-management] prerequisites: commands: [pygount] --- # Codebase Inspection with pygount Analyze repositories for lines of code, language breakdown, file counts, and code-vs-comment ratios using `pygount`. ## When to Use - User asks for LOC (lines of code) count - User wants a language breakdown of a repo - User asks about codebase size or composition - User wants code-vs-comment ratios - General "how…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/codebase-inspection/SKILL.md`, `local:projects/jestur/skills-capabilities/github/codebase-inspection/SKILL.md`, `local:projects/dev-coder/skills-capabilities/github/codebase-inspection/SKILL.md`, `local:projects/dev-orch/skills-capabilities/github/codebase-inspection/SKILL.md`, `local:projects/dev-review/skills-capabilities/github/codebase-inspection/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/github-auth/SKILL.md`
- **Raw:** `[[raw/local/skill-cb9e2b1962.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: github-auth description: "GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login." version: 1.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [GitHub, Authentication, Git, gh-cli, SSH, Setup] related_skills: [github-pr-workflow, github-code-review, github-issues, github-repo-management] --- # GitHub Authentication Setup This skill sets up authentication so the agent can work with GitHub repositories, PRs, issues, and CI. It covers two paths: - **`git` (always available)** — uses HTTPS personal access tokens or SSH keys - **`gh` CLI (if installed)** — richer GitHub API access with a simpler auth flow ## Detection Flow When a user…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/github-auth/SKILL.md`, `local:projects/jestur/skills-capabilities/github/github-auth/SKILL.md`, `local:projects/dev-coder/skills-capabilities/github/github-auth/SKILL.md`, `local:projects/dev-orch/skills-capabilities/github/github-auth/SKILL.md`, `local:projects/dev-review/skills-capabilities/github/github-auth/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/gifs/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-5e3ae313ef.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for searching, downloading, and working with GIFs and short-form animated media. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/gifs/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/gifs/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/gifs/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/gifs/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/gifs/DESCRIPTION.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-51c160e236.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: GitHub workflow skills for managing repositories, pull requests, code reviews, issues, and CI/CD pipelines using the gh CLI and git via terminal. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/github/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/github/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/github/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/github/DESCRIPTION.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/gaming/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-67b3008c09.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for setting up, configuring, and managing game servers, modpacks, and gaming-related infrastructure. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/gaming/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/gaming/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/gaming/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/gaming/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/gaming/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/email/himalaya/SKILL.md`
- **Raw:** `[[raw/local/skill-0f6c9bb4c0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: himalaya description: "Himalaya CLI: IMAP/SMTP email from terminal." version: 1.1.0 author: community license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [Email, IMAP, SMTP, CLI, Communication] homepage: https://github.com/pimalaya/himalaya prerequisites: commands: [himalaya] --- # Himalaya Email CLI Himalaya is a CLI email client that lets you manage emails from the terminal using IMAP, SMTP, Notmuch, or Sendmail backends. This skill is separate from the Hermes Email gateway adapter. The gateway adapter lets people email the agent and uses Hermes' built-in IMAP/SMTP adapter; this skill lets the agent operate a mailbox from terminal tools and requires the…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/email/himalaya/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/email/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-2c40e123f5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for sending, receiving, searching, and managing email from the terminal. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/email/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/email/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/email/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/email/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/email/DESCRIPTION.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/domain/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-b3a30c554b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: domain-intel description: Passive domain reconnaissance using Python stdlib. Use this skill for subdomain discovery, SSL certificate inspection, WHOIS lookups, DNS records, domain availability checks, and bulk multi-domain analysis. No API keys required. Triggers on requests like "find subdomains", "check ssl cert", "whois lookup", "is this domain available", "bulk check these domains". license: MIT --- Passive domain intelligence using only Python stdlib and public data sources. Zero dependencies. Zero API keys. Works out of the box. ## Capabilities - Subdomain discovery via crt.sh certificate transparency logs - Live SSL/TLS certificate inspection (expiry, cipher, SANs, TLS…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/domain/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/domain/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/domain/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/domain/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/domain/DESCRIPTION.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/diagramming/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-76d976d698.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Diagram creation skills for generating visual diagrams, flowcharts, architecture diagrams, and illustrations using tools like Excalidraw. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/diagramming/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/diagramming/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/diagramming/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/diagramming/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/diagramming/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/data-science/jupyter-live-kernel/SKILL.md`
- **Raw:** `[[raw/local/skill-975e781041.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: jupyter-live-kernel description: "Iterative Python via live Jupyter kernel (hamelnb)." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [jupyter, notebook, repl, data-science, exploration, iterative] category: data-science --- # Jupyter Live Kernel (hamelnb) Gives you a **stateful Python REPL** via a live Jupyter kernel. Variables persist across executions. Use this instead of `execute_code` when you need to build up state incrementally, explore APIs, inspect DataFrames, or iterate on complex code. ## When to Use This vs Other Tools | Tool | Use When | |------|----------| | **This skill** | Iterative exploration, state…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/data-science/jupyter-live-kernel/SKILL.md`, `local:projects/jestur/skills-capabilities/data-science/jupyter-live-kernel/SKILL.md`, `local:projects/dev-coder/skills-capabilities/data-science/jupyter-live-kernel/SKILL.md`, `local:projects/dev-orch/skills-capabilities/data-science/jupyter-live-kernel/SKILL.md`, `local:projects/dev-review/skills-capabilities/data-science/jupyter-live-kernel/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/data-science/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-1311078585.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: Skills for data science workflows — interactive exploration, Jupyter notebooks, data analysis, and visualization. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/data-science/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/data-science/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/data-science/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/data-science/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/data-science/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/sketch/SKILL.md`
- **Raw:** `[[raw/local/skill-c643ff8657.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: sketch description: "Throwaway HTML mockups: 2-3 design variants to compare." version: 1.0.0 author: Hermes Agent (adapted from gsd-build/get-shit-done) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [sketch, mockup, design, ui, prototype, html, variants, exploration, wireframe, comparison] related_skills: [spike, claude-design, popular-web-designs, excalidraw] --- # Sketch Use this skill when the user wants to **see a design direction before committing** to one — exploring a UI/UX idea as disposable HTML mockups. The point is to generate 2-3 interactive variants so the user can compare visual directions side-by-side, not to produce shippable code. Load…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/sketch/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/sketch/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/sketch/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/sketch/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/sketch/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/pretext/SKILL.md`
- **Raw:** `[[raw/local/skill-532570c95d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: pretext description: "Use when building creative browser demos with @chenglou/pretext — DOM-free text layout for ASCII art, typographic flow around obstacles, text-as-geometry games, kinetic typography, and text-powered generative art. Produces single-file HTML demos by default." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [creative-coding, typography, pretext, ascii-art, canvas, generative, text-layout, kinetic-typography] related_skills: [p5js, claude-design, excalidraw, architecture-diagram] --- # Pretext Creative Demos ## Overview [`@chenglou/pretext`](https://github.com/chenglou/pretext) is a 15KB zero-dependency…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/pretext/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/pretext/SKILL.md`

### ATTRIBUTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/pixel-art/ATTRIBUTION.md`
- **Raw:** `[[raw/local/attribution-16e3338276.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Attribution This skill bundles code ported from a third-party MIT-licensed project. All reuse is credited here. ## pixel-art-studio (Synero) - Source: https://github.com/Synero/pixel-art-studio - License: MIT - Copyright: © Synero, MIT-licensed contributors ### What was ported **`scripts/palettes.py`** — the `PALETTES` dict containing 23 named RGB palettes (hardware and artistic). Values are reproduced verbatim from `scripts/pixelart.py` of pixel-art-studio. **`scripts/pixel_art_video.py`** — the 12 procedural animation init/draw pairs (`stars`, `fireflies`, `leaves`, `dust_motes`, `sparkles`, `rain`, `lightning`, `bubbles`, `embers`, `snowflakes`, `neon_pulse`, `heat_shimmer`) and the…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/pixel-art/ATTRIBUTION.md`, `local:projects/jestur/skills-capabilities/creative/pixel-art/ATTRIBUTION.md`, `local:projects/dev-coder/skills-capabilities/creative/pixel-art/ATTRIBUTION.md`, `local:projects/dev-orch/skills-capabilities/creative/pixel-art/ATTRIBUTION.md`, `local:projects/dev-review/skills-capabilities/creative/pixel-art/ATTRIBUTION.md`

### README
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/manim-video/README.md`
- **Raw:** `[[raw/local/readme-a30f3ec610.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Manim Video Skill Production pipeline for mathematical and technical animations using [Manim Community Edition](https://www.manim.community/). ## What it does Creates 3Blue1Brown-style animated videos from text prompts. The agent handles the full pipeline: creative planning, Python code generation, rendering, scene stitching, and iterative refinement. ## Use cases - **Concept explainers** — "Explain how neural networks learn" - **Equation derivations** — "Animate the proof of the Pythagorean theorem" - **Algorithm visualizations** — "Show how quicksort works step by step" - **Data stories** — "Animate our before/after performance metrics" - **Architecture diagrams** — "Show our…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/manim-video/README.md`, `local:projects/jestur/skills-capabilities/creative/manim-video/README.md`, `local:projects/dev-coder/skills-capabilities/creative/manim-video/README.md`, `local:projects/dev-orch/skills-capabilities/creative/manim-video/README.md`, `local:projects/dev-review/skills-capabilities/creative/manim-video/README.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/excalidraw/SKILL.md`
- **Raw:** `[[raw/local/skill-beef7b8ea0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: excalidraw description: "Hand-drawn Excalidraw JSON diagrams (arch, flow, seq)." version: 1.0.0 author: Hermes Agent license: MIT dependencies: [] platforms: [linux, macos, windows] metadata: hermes: tags: [Excalidraw, Diagrams, Flowcharts, Architecture, Visualization, JSON] related_skills: [] --- # Excalidraw Diagram Skill Create diagrams by writing standard Excalidraw element JSON and saving as `.excalidraw` files. These files can be drag-and-dropped onto [excalidraw.com](https://excalidraw.com) for viewing and editing. No accounts, no API keys, no rendering libraries -- just JSON. ## When to use Generate `.excalidraw` files for architecture diagrams, flowcharts, sequence…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/excalidraw/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/excalidraw/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/excalidraw/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/excalidraw/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/excalidraw/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/design-md/SKILL.md`
- **Raw:** `[[raw/local/skill-38ed14bc71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: design-md description: Author/validate/export Google's DESIGN.md token spec files. version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [design, design-system, tokens, ui, accessibility, wcag, tailwind, dtcg, google] related_skills: [popular-web-designs, claude-design, excalidraw, architecture-diagram] --- # DESIGN.md Skill DESIGN.md is Google's open spec (Apache-2.0, `google-labs-code/design.md`) for describing a visual identity to coding agents. One file combines: - **YAML front matter** — machine-readable design tokens (normative values) - **Markdown body** — human-readable rationale, organized into canonical sections…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/design-md/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/design-md/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/design-md/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/design-md/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/design-md/SKILL.md`

### jigsaw
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-infographic/references/layouts/jigsaw.md`
- **Raw:** `[[raw/local/jigsaw-1b5566cdf0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # jigsaw Interlocking puzzle pieces showing how parts fit together. ## Structure - Puzzle pieces that interlock - Each piece represents a component - Connections show relationships - Can be assembled or exploded view - Missing piece highlights gaps ## Best For - Component relationships - Team/skill fit - Strategy pieces - Integration concepts - Completeness assessments ## Visual Elements - Classic puzzle piece shapes - Distinct colors per piece - Interlocking edges visible - Icons or labels per piece - Optional missing piece ## Text Placement - Title at top - Piece labels inside or beside - Connection descriptions - Missing piece explanation - Assembly context ## Recommended Pairings -…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-infographic/references/layouts/jigsaw.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-infographic/references/layouts/jigsaw.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-infographic/references/layouts/jigsaw.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-infographic/references/layouts/jigsaw.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-infographic/references/layouts/jigsaw.md`

### periodic-table
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-infographic/references/layouts/periodic-table.md`
- **Raw:** `[[raw/local/periodic-table-8fa5c18230.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # periodic-table Grid of categorized elements with consistent cell formatting. ## Structure - Rectangular grid - Each cell is one element - Color-coded categories - Consistent cell format - Optional grouping gaps ## Best For - Categorized collections - Tool/resource catalogs - Skill matrices - Element collections - Reference guides ## Visual Elements - Uniform cell sizes - Category colors - Symbol/abbreviation prominent - Small icon per cell - Category legend ## Text Placement - Title at top - Cell: symbol, name, brief info - Category names in legend - Optional row/column headers - Footnotes for special cases ## Recommended Pairings - `pop-art`: Vibrant element grids - `pixel-art`: Retro…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-infographic/references/layouts/periodic-table.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-infographic/references/layouts/periodic-table.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-infographic/references/layouts/periodic-table.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-infographic/references/layouts/periodic-table.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-infographic/references/layouts/periodic-table.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-infographic/SKILL.md`
- **Raw:** `[[raw/local/skill-89e25da6d8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: baoyu-infographic description: "Infographics: 21 layouts x 21 styles (信息图, 可视化)." version: 1.56.1 author: 宝玉 (JimLiu) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [infographic, visual-summary, creative, image-generation] homepage: https://github.com/JimLiu/baoyu-skills#baoyu-infographic --- # Infographic Generator Adapted from [baoyu-infographic](https://github.com/JimLiu/baoyu-skills) for Hermes Agent's tool ecosystem. Two dimensions: **layout** (information structure) × **style** (visual aesthetics). Freely combine any layout with any style. ## When to Use Trigger this skill when the user asks to create an infographic, visual summary, information…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-infographic/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-infographic/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-infographic/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-infographic/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-infographic/SKILL.md`

### PORT_NOTES
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-infographic/PORT_NOTES.md`
- **Raw:** `[[raw/local/port_notes-5dd3dbe9e9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Port Notes — baoyu-infographic Ported from [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) v1.56.1. ## Changes from upstream Only `SKILL.md` was modified. All 45 reference files are verbatim copies. ### SKILL.md adaptations | Change | Upstream | Hermes | |--------|----------|--------| | Metadata namespace | `openclaw` | `hermes` | | Trigger | `/baoyu-infographic` slash command | Natural language skill matching | | User config | EXTEND.md file (project/user/XDG paths) | Removed — not part of Hermes infra | | User prompts | `AskUserQuestion` (batched) | `clarify` tool (one at a time) | | Image generation | baoyu-imagine (Bun/TypeScript) | `image_generate` tool | | Platform…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-infographic/PORT_NOTES.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-infographic/PORT_NOTES.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-infographic/PORT_NOTES.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-infographic/PORT_NOTES.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-infographic/PORT_NOTES.md`

### auto-selection
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-comic/references/auto-selection.md`
- **Raw:** `[[raw/local/auto-selection-1d5de33377.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Auto Selection Content signals determine default art + tone + layout (or preset). ## Content Signal Matrix | Content Signals | Art Style | Tone | Layout | Preset | |-----------------|-----------|------|--------|--------| | Tutorial, how-to, beginner | manga | neutral | webtoon | **ohmsha** | | Computing, AI, programming | manga | neutral | dense | **ohmsha** | | Technical explanation, educational | manga | neutral | webtoon | **ohmsha** | | Pre-1950, classical, ancient | realistic | vintage | cinematic | - | | Personal story, mentor | ligne-claire | warm | standard | - | | Psychology, motivation, self-help, coaching | manga | warm | standard | **concept-story** | | Business narrative,…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-comic/references/auto-selection.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-comic/references/auto-selection.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-comic/references/auto-selection.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-comic/references/auto-selection.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-comic/references/auto-selection.md`

### PORT_NOTES
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-comic/PORT_NOTES.md`
- **Raw:** `[[raw/local/port_notes-6af24f7840.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Port Notes — baoyu-comic Ported from [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) v1.56.1. ## Changes from upstream ### SKILL.md adaptations | Change | Upstream | Hermes | |--------|----------|--------| | Metadata namespace | `openclaw` | `hermes` (with `tags` + `homepage`) | | Trigger | Slash commands / CLI flags | Natural language skill matching | | User config | EXTEND.md file (project/user/XDG paths) | Removed — not part of Hermes infra | | User prompts | `AskUserQuestion` (batched) | `clarify` tool (one question at a time) | | Image generation | baoyu-imagine (Bun/TypeScript, supports `--ref`) | `image_generate` — **prompt-only**, returns a URL; no reference image…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-comic/PORT_NOTES.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-comic/PORT_NOTES.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-comic/PORT_NOTES.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-comic/PORT_NOTES.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-comic/PORT_NOTES.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/ascii-art/SKILL.md`
- **Raw:** `[[raw/local/skill-b69fdd3000.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: ascii-art description: "ASCII art: pyfiglet, cowsay, boxes, image-to-ascii." version: 4.0.0 author: 0xbyt4, Hermes Agent license: MIT dependencies: [] platforms: [linux, macos, windows] metadata: hermes: tags: [ASCII, Art, Banners, Creative, Unicode, Text-Art, pyfiglet, figlet, cowsay, boxes] related_skills: [excalidraw] --- # ASCII Art Skill Multiple tools for different ASCII art needs. All tools are local CLI programs or free REST APIs — no API keys required. ## Tool 1: Text Banners (pyfiglet — local) Render text as large ASCII art banners. 571 built-in fonts. ### Setup ### Usage ### Recommended fonts | Style | Font | Best for | |-------|------|----------| | Clean & modern |…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/ascii-art/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/ascii-art/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/ascii-art/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/ascii-art/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/ascii-art/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/architecture-diagram/SKILL.md`
- **Raw:** `[[raw/local/skill-0e7e2736aa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: architecture-diagram description: "Dark-themed SVG architecture/cloud/infra diagrams as HTML." version: 1.0.0 author: Cocoon AI (hello@cocoon-ai.com), ported by Hermes Agent license: MIT dependencies: [] platforms: [linux, macos, windows] metadata: hermes: tags: [architecture, diagrams, SVG, HTML, visualization, infrastructure, cloud] related_skills: [concept-diagrams, excalidraw] --- # Architecture Diagram Skill Generate professional, dark-themed technical architecture diagrams as standalone HTML files with inline SVG graphics. No external tools, no API keys, no rendering libraries — just write the HTML file and open it in a browser. ## Scope **Best suited for:** - Software…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/architecture-diagram/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/architecture-diagram/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/architecture-diagram/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/architecture-diagram/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/architecture-diagram/SKILL.md`

### 1519818487667757156-Resend-Skill-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519818487667757156-Resend-Skill-for-Hermes.txt`
- **Raw:** `[[raw/discord/1519818487667757156-resend-skill-for-hermes-47def2d3d0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Resend Skill for Hermes' in forum #plugins-skills-and-skins # thread_id=1519818487667757156 forum_id=1485392832154832906 # Started 2026-06-26T03:34:36.869840+00:00 [2026-06-25T21:36:04.322000+00:00] gumbyender (id=1519818487667757156) https://github.com/GumbyEnder/hermes-resend-skill [embed] GitHub - GumbyEnder/hermes-resend-skill: resend.com - Hermes specif... https://github.com/GumbyEnder/hermes-resend-skill

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519818487667757156-Resend-Skill-for-Hermes.txt`

### 1519462713019858974-Hermes-Skill---Math-via-code
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519462713019858974-Hermes-Skill---Math-via-code.txt`
- **Raw:** `[[raw/discord/1519462713019858974-hermes-skill---math-via-code-f0010ac4ec.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Skill - Math-via-code' in forum #plugins-skills-and-skins # thread_id=1519462713019858974 forum_id=1485392832154832906 # Started 2026-06-25T03:03:39.320588+00:00 [2026-06-24T22:02:21.036000+00:00] tomrevo.x (id=1519462713019858974) LLM arithmetic is unreliable — accuracy degrades with context length, and even "simple" multi-step math produces wrong numbers. This skill was born from repeated errors in financial modeling: SDE calculations, P&L analysis, and facility rollups where a single transposed digit or premature rounding cascaded into incorrect deal evaluations. The fix is simple: if there are more than two numbers involved, write code. Every time. No exceptions.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519462713019858974-Hermes-Skill---Math-via-code.txt`

### 1519465199034302705-Release--Stupidly-simple-Agent-first-cortex
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519465199034302705-Release--Stupidly-simple-Agent-first-cortex.txt`
- **Raw:** `[[raw/discord/1519465199034302705-release--stupidly-simple-agent-first-cortex-66abe6ebda.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Release: Stupidly simple Agent first cortex' in forum #plugins-skills-and-skins # thread_id=1519465199034302705 forum_id=1485392832154832906 # Started 2026-06-25T14:32:37.350358+00:00 [2026-06-25T09:45:55.630000+00:00] .thebakery303 (id=1519639773860593765) Release: Stupidly simple Agent first cortex

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519465199034302705-Release--Stupidly-simple-Agent-first-cortex.txt`

### 1519755296992657639-Skill---long-research----time-boxed-autonomous-research-sprints
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519755296992657639-Skill---long-research----time-boxed-autonomous-research-sprints.txt`
- **Raw:** `[[raw/discord/1519755296992657639-skill---long-research----time-boxed-autonomous-research-sprints-945595b64c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Skill : long-research, ⏰ time-boxed autonomous research sprints' in forum #plugins-skills-and-skins # thread_id=1519755296992657639 forum_id=1485392832154832906 # Started 2026-06-25T20:02:01.587939+00:00 [2026-06-25T17:24:58.491000+00:00] kaushalpanchal (id=1519755296992657639) Hey all, sharing a skill I built for running actual multi-hour research runs without the model quitting early or losing track of time. **The problem:** you say "research X for 4 hours" and the LLM either quits in 10 minutes or rambles forever. It has no clock. **The fix:** this skill moves the clock out of the model. it uses Hermes cron — every 15 min a fresh tick runs, checks the real wall-clock, does ONE…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519755296992657639-Skill---long-research----time-boxed-autonomous-research-sprints.txt`

### 1520064603776749660-Cron-job---Nous-Portal-OAuth-Token-Refresh
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1520064603776749660-Cron-job---Nous-Portal-OAuth-Token-Refresh.txt`
- **Raw:** `[[raw/discord/1520064603776749660-cron-job---nous-portal-oauth-token-refresh-ebd64ff808.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Cron job - Nous Portal OAuth Token Refresh' in forum #plugins-skills-and-skins # thread_id=1520064603776749660 forum_id=1485392832154832906 # Started 2026-06-26T14:25:03.096204+00:00 [2026-06-26T13:54:02.975000+00:00] tomrevo.x (id=1520064603776749660) Just a simple gist to add as a cron job to your Hermes. Keeps your portal token refreshed so portal tools don't silently fail (undiscoverable) https://gist.github.com/tommulkins/102a767553db0fd23429a287a435776f [embed] Proactive Nous Portal OAuth token refresh watchdog for Hermes Agent... https://gist.github.com/tommulkins/102a767553db0fd23429a287a435776f

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1520064603776749660-Cron-job---Nous-Portal-OAuth-Token-Refresh.txt`

### 1519866722100838440-Hackysack---Hermes-cron-agent-for-creative-idea-loops
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519866722100838440-Hackysack---Hermes-cron-agent-for-creative-idea-loops.txt`
- **Raw:** `[[raw/discord/1519866722100838440-hackysack---hermes-cron-agent-for-creative-idea-loops-64b4142c19.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hackysack - Hermes cron-agent for creative idea loops' in forum #plugins-skills-and-skins # thread_id=1519866722100838440 forum_id=1485392832154832906 # Started 2026-06-26T03:34:36.470173+00:00 [2026-06-26T00:47:44.307000+00:00] guideboardlabs (id=1519866722100838440) Full post on X https://x.com/guideboardlabs/status/2070284222594502987?s=46 Used the new ideation creation skill from this past release to set up a council of agents cron job for constant new ideas for your projects and gaps you might be missing [embed] https://twitter.com/guideboardlabs/status/2070284222594502987?s=46 [2026-06-26T00:55:10.110000+00:00] guideboardlabs (id=1519868591934013571)…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519866722100838440-Hackysack---Hermes-cron-agent-for-creative-idea-loops.txt`

### 1519931768612847647-The-DeepThink-Skill--Making-Hermes-Slow-Down-Before-Expensive-Decisions
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519931768612847647-The-DeepThink-Skill--Making-Hermes-Slow-Down-Before-Expensive-Decisions.txt`
- **Raw:** `[[raw/discord/1519931768612847647-the-deepthink-skill--making-hermes-slow-down-before-expensive-decisions-5cbe4d872a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'The DeepThink Skill: Making Hermes Slow Down Before Expensive Decisions' in forum #plugins-skills-and-skins # thread_id=1519931768612847647 forum_id=1485392832154832906 # Started 2026-06-26T09:26:08.322897+00:00 [2026-06-26T05:06:12.604000+00:00] jonkomet (id=1519931768612847647) I’m sharing my standalone DeepThink skill handoff as a PDF + Markdown file. DeepThink is a reusable agent skill, not a model or plugin. It gives Hermes a structured loop-based reasoning workflow for moments where a quick answer is too shallow. It runs through: - Surface: first-pass hypothesis - Explore: alternatives, evidence, edge cases - Challenge: assumptions, risks, failure modes - Synthesize: refined…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519931768612847647-The-DeepThink-Skill--Making-Hermes-Slow-Down-Before-Expensive-Decisions.txt`

### 1519062011978322070-Remember
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519062011978322070-Remember.txt`
- **Raw:** `[[raw/discord/1519062011978322070-remember-3846938777.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Remember' in forum #plugins-skills-and-skins # thread_id=1519062011978322070 forum_id=1485392832154832906 # Started 2026-06-23T20:05:07.852124+00:00 [2026-06-23T19:30:06.463000+00:00] flash_speed3412 (id=1519062011978322070) **Production-ready local-first memory layer for AI agents.** Remember gives your agent persistent memory that survives across sessions. Hybrid search (BM25 + vector), temporal validity windows, entity graphs, and memory decay — all in a single SQLite file. No cloud. No API keys. No telemetry. ------------------------------------------ **Found a bug? Have an idea? Open an issue or PR.** If Remember saved your project from the dreaded "wait, what was I working…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519062011978322070-Remember.txt`

### 1519135458762948698-CLAWMES---The-DeFi-layer-for-your-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519135458762948698-CLAWMES---The-DeFi-layer-for-your-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1519135458762948698-clawmes---the-defi-layer-for-your-hermes-agent-9e9adf7989.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'CLAWMES - The DeFi layer for your Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1519135458762948698 forum_id=1485392832154832906 # Started 2026-06-24T09:30:16.898258+00:00 [2026-06-24T03:53:43.093000+00:00] ddfp777 (id=1519188749710397480) CLAWMES - The DeFi layer for your Hermes Agent

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519135458762948698-CLAWMES---The-DeFi-layer-for-your-Hermes-Agent.txt`

### 1519289986158166087-hermes-lancedb-viz---Local-vector-memory-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519289986158166087-hermes-lancedb-viz---Local-vector-memory-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1519289986158166087-hermes-lancedb-viz---local-vector-memory-for-hermes-agent-80ffa81e3f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'hermes-lancedb-viz — Local vector memory for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1519289986158166087 forum_id=1485392832154832906 # Started 2026-06-24T14:29:53.782209+00:00 [2026-06-24T10:35:59.743000+00:00] 3l0_ (id=1519289986158166087) Just open-sourced a memory plugin + visualizer I built for Hermes Agent. Why LanceDB instead of SQLite/Chroma/etc: - Zero-footprint: no server, no daemon, just a Rust columnar format on disk. LanceDB is embedded like SQLite but built for vectors from the ground up. - Native hybrid search: BM25 (Tantivy FTS) + vector cosine fused via Reciprocal Rank Fusion. ~98% recall vs 18% vector-only. No separate search stack. - Ollama…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519289986158166087-hermes-lancedb-viz---Local-vector-memory-for-Hermes-Agent.txt`

### 1519253009815830642-Agents-Forum-Environment
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519253009815830642-Agents-Forum-Environment.txt`
- **Raw:** `[[raw/discord/1519253009815830642-agents-forum-environment-2bef12bf2b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Agents Forum Environment' in forum #plugins-skills-and-skins # thread_id=1519253009815830642 forum_id=1485392832154832906 # Started 2026-06-24T09:30:15.881975+00:00 [2026-06-24T08:09:03.896000+00:00] hyperstone6996 (id=1519253009815830642) If you've seen any agent forum stuff lately, pls share them 🙂

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519253009815830642-Agents-Forum-Environment.txt`

### 1518156858869940224-Hermes-Bible-Skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1518156858869940224-Hermes-Bible-Skill.txt`
- **Raw:** `[[raw/discord/1518156858869940224-hermes-bible-skill-da8b6fb8fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Bible Skill' in forum #plugins-skills-and-skins # thread_id=1518156858869940224 forum_id=1485392832154832906 # Started 2026-06-21T09:50:43.345209+00:00 [2026-06-21T07:33:21.145000+00:00] dadmin88 (id=1518156858869940224) 📖 **Hermes Bible — Community Knowledge Base Skill** Shoutout to <@1453594507818959015> for building The Hermes Bible — 169 pages of community documentation for Hermes Agent. I packaged it into a skill so it loads right into your agent's context. **What's inside:** • 169 pages covering flows, features, patterns, and real-world usage • 25+ battle-tested workflows with practical examples • Hidden Hermes features you won't find in the official docs • SOUL.md…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1518156858869940224-Hermes-Bible-Skill.txt`

### 1519135458762948698-CLAWMES
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1519135458762948698-CLAWMES.txt`
- **Raw:** `[[raw/discord/1519135458762948698-clawmes-d720ac924e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'CLAWMES' in forum #plugins-skills-and-skins # thread_id=1519135458762948698 forum_id=1485392832154832906 # Started 2026-06-24T03:28:34.596288+00:00 [2026-06-24T00:21:57.541000+00:00] ddfp777 (id=1519135458762948698) Clawmes turns your Hermes agent into an autonomous on chain operator, one that trades, lends, stakes, votes and manages a treasury in your own wallet, while you sleep. https://github.com/clawnchdev/clawmes#readme [attachment] ClawnchBotCLAWMES.jpg https://cdn.discordapp.com/attachments/1519135458762948698/1519135459064942775/ClawnchBotCLAWMES.jpg?ex=6a3c74a5&is=6a3b2325&hm=d8a2604d987dd8253713f9721c85c32ebf9a8ce62bb9571490c2abcf1c6e8e6d& [embed] GitHub -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1519135458762948698-CLAWMES.txt`

### 1518630196817690644-Hermes-Plugin-Gen---Generate---Boilerplate-Custom-Hermes-Skills-Instantly
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1518630196817690644-Hermes-Plugin-Gen---Generate---Boilerplate-Custom-Hermes-Skills-Instantly.txt`
- **Raw:** `[[raw/discord/1518630196817690644-hermes-plugin-gen---generate---boilerplate-custom-hermes-skills-instantly-85efa010f5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Plugin Gen — Generate & Boilerplate Custom Hermes Skills Instantly' in forum #plugins-skills-and-skins # thread_id=1518630196817690644 forum_id=1485392832154832906 # Started 2026-06-22T16:57:19.662651+00:00 [2026-06-22T14:54:13.706000+00:00] iruzenn (id=1518630196817690644) Hermes Plugin Gen — Custom Skill Generator Annoncé par <@928394777878220850> Tired of manually setting up the boilerplate for every new Hermes skill or plugin? Hermes Plugin Gen is a CLI tool designed to automate the creation of Hermes agent extensions, giving you a structured, ready-to-code environment in seconds. What’s Inside: Instant Scaffolding: Generates the complete directory structure required…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1518630196817690644-Hermes-Plugin-Gen---Generate---Boilerplate-Custom-Hermes-Skills-Instantly.txt`

### 1518630937649484009-Hermes-Project-Oracle---Advanced-Prediction---Context-Oracle-for-Hermes-Agents
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1518630937649484009-Hermes-Project-Oracle---Advanced-Prediction---Context-Oracle-for-Hermes-Agents.txt`
- **Raw:** `[[raw/discord/1518630937649484009-hermes-project-oracle---advanced-prediction---context-oracle-for-hermes-agents-4ea5a6396c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Project Oracle — Advanced Prediction & Context Oracle for Hermes Agents' in forum #plugins-skills-and-skins # thread_id=1518630937649484009 forum_id=1485392832154832906 # Started 2026-06-22T16:57:19.184469+00:00 [2026-06-22T14:57:10.334000+00:00] iruzenn (id=1518630937649484009) Hermes Project Oracle — Intelligence & Prediction Layer Annoncé par <@928394777878220850> 🔮 Elevate your Hermes Agent's reasoning capabilities. Hermes Project Oracle acts as an advanced contextual analysis and forecasting layer, allowing your agents to look ahead, evaluate deep information flows, and provide highly accurate, predictive insights based on real-time data environments. What’s Inside:…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1518630937649484009-Hermes-Project-Oracle---Advanced-Prediction---Context-Oracle-for-Hermes-Agents.txt`

### 1516137490178904214-Galaxy-Brain-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1516137490178904214-Galaxy-Brain-Plugin.txt`
- **Raw:** `[[raw/discord/1516137490178904214-galaxy-brain-plugin-e769bc2fd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Galaxy Brain Plugin' in forum #plugins-skills-and-skins # thread_id=1516137490178904214 forum_id=1485392832154832906 # Started 2026-06-15T20:57:30.284185+00:00 [2026-06-15T17:49:06.131000+00:00] eucdee (id=1516137490178904214) A 3D interactive knowledge graph visualization plugin for Hermes Agent, bringing your Obsidian vault to life as a navigable 3D constellation of notes and tags. https://github.com/ohrbit/hermes_plugins/tree/main/galaxy_brain Took some time but i told my almost vanilla 1€ vps to combine both githubs into one plugin for hermes 🥰 Enjoy! I hope the original authors can implement a proper version from this. [attachment] hero.jpg…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1516137490178904214-Galaxy-Brain-Plugin.txt`

### 1515464353820967173-pingpong---meet-other-Hermes-users-for-exchange-over-lunch--ping-pong-or-other-activities
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1515464353820967173-pingpong---meet-other-Hermes-users-for-exchange-over-lunch--ping-pong-or-other-activities.txt`
- **Raw:** `[[raw/discord/1515464353820967173-pingpong---meet-other-hermes-users-for-exchange-over-lunch--ping-pong-or-other-activities-27ac97934d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🏓 pingpong — meet other Hermes users for exchange over lunch, ping pong or other activities' in forum #plugins-skills-and-skins # thread_id=1515464353820967173 forum_id=1485392832154832906 # Started 2026-06-14T03:56:34.219019+00:00 [2026-06-13T21:14:17.917000+00:00] ike_always (id=1515464353820967173) Tell your agent "free tonight, fancy table tennis?" — it posts a pseudonymous, ~1km-coarse offer to a shared board. Nearby Hermes agents match it locally and the two agents negotiate place & time end-to-end-sealed; double-opt-in before any contact is shared. Self-learning table-tennis skill matching. Open-source, MIT. Install (passes the security scanner clean): hermes skills install…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1515464353820967173-pingpong---meet-other-Hermes-users-for-exchange-over-lunch--ping-pong-or-other-activities.txt`

### 1517003465593847970-Hermes-IdleViber--clicker-game
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1517003465593847970-Hermes-IdleViber--clicker-game.txt`
- **Raw:** `[[raw/discord/1517003465593847970-hermes-idleviber--clicker-game-056a86364f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes IdleViber (clicker-game)' in forum #plugins-skills-and-skins # thread_id=1517003465593847970 forum_id=1485392832154832906 # Started 2026-06-18T03:46:37.132490+00:00 [2026-06-18T03:10:10.759000+00:00] drgekoz (id=1517003465593847970) Hermes IdleViber is an ambient idle/incremental game that lives in your browser — a cozy pixel-art universe where you click, earn, upgrade, and unlock themed rooms while chiptune music plays and particle effects drift across the screen. The twist? The game is hard-locked to your local Hermes Agent gateway. https://hermes-idleviber.netlify.app [attachment] Screenshot_2026-06-14_125910.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1517003465593847970-Hermes-IdleViber--clicker-game.txt`

### 1515054183156420748-Apollo---the-plugin-that-turns-Hermes-into-a-health-super-agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1515054183156420748-Apollo---the-plugin-that-turns-Hermes-into-a-health-super-agent.txt`
- **Raw:** `[[raw/discord/1515054183156420748-apollo---the-plugin-that-turns-hermes-into-a-health-super-agent-45631bb278.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Apollo - the plugin that turns Hermes into a health super agent' in forum #plugins-skills-and-skins # thread_id=1515054183156420748 forum_id=1485392832154832906 # Started 2026-06-12T20:11:32.968397+00:00 [2026-06-12T18:04:25.610000+00:00] thechaosalchemist (id=1515054183156420748) connect any wearable, own your own health data, fully open sourced! https://x.com/RiverKhan/status/2065447164365455443?s=20 [embed] https://twitter.com/RiverKhan/status/2065447164365455443?s=20 [2026-06-12T22:09:13.447000+00:00] buke5122 (id=1515115788409770055) Any support for Huawei watches? [2026-06-13T23:36:00.090000+00:00] thechaosalchemist (id=1515500014519058482) <@1034463677069398100> adding it!…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1515054183156420748-Apollo---the-plugin-that-turns-Hermes-into-a-health-super-agent.txt`

### 1517061801756590231-Hermes-Session-Analytics--An-improved-plugin-for-visualizing-sessions
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1517061801756590231-Hermes-Session-Analytics--An-improved-plugin-for-visualizing-sessions.txt`
- **Raw:** `[[raw/discord/1517061801756590231-hermes-session-analytics--an-improved-plugin-for-visualizing-sessions-a7b31d8d67.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Session Analytics: An improved plugin for visualizing sessions' in forum #plugins-skills-and-skins # thread_id=1517061801756590231 forum_id=1485392832154832906 # Started 2026-06-18T10:22:07.614518+00:00 [2026-06-18T07:01:59.184000+00:00] tom_jose (id=1517061801756590231) Tired of the native Analytics page being hidden because the numbers are "just estimates"? This plugin gives you real cost attribution (by user, platform, and model), tool latency, top-spender sessions, and cleaned-up transcripts with Slack links — all read-only from state.db. Slack-first; Discord + WhatsApp soon. Github repo for the plugin: https://github.com/tomjose92/hermes-session-analytics [attachment]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1517061801756590231-Hermes-Session-Analytics--An-improved-plugin-for-visualizing-sessions.txt`

### 1516153734651056300-Enable-telegram-topics
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1516153734651056300-Enable-telegram-topics.txt`
- **Raw:** `[[raw/discord/1516153734651056300-enable-telegram-topics-e887c1ef2a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Enable telegram topics' in forum #plugins-skills-and-skins # thread_id=1516153734651056300 forum_id=1485392832154832906 # Started 2026-06-15T20:57:29.759414+00:00 [2026-06-15T18:53:39.115000+00:00] eucdee (id=1516153734651056300) This is an integrated feature i just discovered, thought this may be the best place for such a #quicktip ... just say /topic to open the help and configure the bot to use it, great feature. [attachment] Screenshot_20260615_203405_Telegram.jpg https://cdn.discordapp.com/attachments/1516153734651056300/1516153735158431844/Screenshot_20260615_203405_Telegram.jpg?ex=6a319bb3&is=6a304a33&hm=e709e50396f04903c215425bb1ea28e7f770ffec209916f247a8041455ae13ff&

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1516153734651056300-Enable-telegram-topics.txt`

### 1517054553470799943-IMPLEMENTAUDIT---a-nested-loop-skill-to-safely-close-findings--plan-deeply--augment--goal---etc
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1517054553470799943-IMPLEMENTAUDIT---a-nested-loop-skill-to-safely-close-findings--plan-deeply--augment--goal---etc.txt`
- **Raw:** `[[raw/discord/1517054553470799943-implementaudit---a-nested-loop-skill-to-safely-close-findings--plan-deeply--augment--goal---etc-6f771af6bc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'IMPLEMENTAUDIT ; a nested loop skill to safely close findings, plan deeply, augment /goal , etc' in forum #plugins-skills-and-skins # thread_id=1517054553470799943 forum_id=1485392832154832906 # Started 2026-06-18T10:22:07.972546+00:00 [2026-06-18T06:33:11.058000+00:00] mdthr (id=1517054553470799943) https://theIslampill.github.io/IMPLEMENTAUDIT.md/ https://github.com/theIslampill/IMPLEMENTAUDIT.md/ I give permission for Nous to use/adapt/merge this into Hermes however they see fit [attachment] image.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1517054553470799943-IMPLEMENTAUDIT---a-nested-loop-skill-to-safely-close-findings--plan-deeply--augment--goal---etc.txt`

### 1516126237649801396-how-to-declutter-one-off-skills
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1516126237649801396-how-to-declutter-one-off-skills.txt`
- **Raw:** `[[raw/discord/1516126237649801396-how-to-declutter-one-off-skills-13acee7630.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'how to declutter one-off skills?' in forum #plugins-skills-and-skins # thread_id=1516126237649801396 forum_id=1485392832154832906 # Started 2026-06-15T20:57:30.775403+00:00 [2026-06-15T17:04:23.319000+00:00] duckie3636 (id=1516126237649801396) need to unclutter ; accumulated lot of local skills from one-offs & want to clear most keeping just a few I'm actively using. What's the right way? tried moving the skill folders out of ~/.hermes/skills-capabilities/ and it got messy. Is there a builtin command for it? [2026-06-15T17:37:08.043000+00:00] sahil_ss9 (id=1516134478299271178) ask hermes to use the curator skill.

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1516126237649801396-how-to-declutter-one-off-skills.txt`

### 1516596273463955486-fablize-for-hermes---run-like-Fable--on-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1516596273463955486-fablize-for-hermes---run-like-Fable--on-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1516596273463955486-fablize-for-hermes---run-like-fable--on-hermes-agent-f120a19d59.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'fablize-for-hermes — run like Fable, on Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1516596273463955486 forum_id=1485392832154832906 # Started 2026-06-17T04:00:34.144356+00:00 [2026-06-17T00:12:08.590000+00:00] thiagosteixeira (id=1516596273463955486) This project adapts fablize's verified procedures — verification grounding, multi-story evidence gating, investigation protocol, and early-stop prevention — from Claude Code's plugin system to Hermes Agent's skill system. fablize makes any agent see a task through to the end — with evidence and verification — as procedure, not as luck. https://github.com/teixeirazeus/fablize-for-hermes [attachment] banner-social.jpg…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1516596273463955486-fablize-for-hermes---run-like-Fable--on-Hermes-Agent.txt`

### 1516507131929559260-Railway-skills-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1516507131929559260-Railway-skills-for-Hermes.txt`
- **Raw:** `[[raw/discord/1516507131929559260-railway-skills-for-hermes-f267b1fd96.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Railway skills for Hermes' in forum #plugins-skills-and-skins # thread_id=1516507131929559260 forum_id=1485392832154832906 # Started 2026-06-16T20:52:11.138862+00:00 [2026-06-16T18:17:55.592000+00:00] gumbyender (id=1516507131929559260) https://github.com/GumbyEnder/hermes-railway-skills [embed] GitHub - GumbyEnder/hermes-railway-skills: Hermes specific skills f... https://github.com/GumbyEnder/hermes-railway-skills

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1516507131929559260-Railway-skills-for-Hermes.txt`

### 1516501797668388975-Fileviewer-Web-Dashboard-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1516501797668388975-Fileviewer-Web-Dashboard-Plugin.txt`
- **Raw:** `[[raw/discord/1516501797668388975-fileviewer-web-dashboard-plugin-fc370f873c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Fileviewer Web Dashboard Plugin' in forum #plugins-skills-and-skins # thread_id=1516501797668388975 forum_id=1485392832154832906 # Started 2026-06-16T20:52:11.542318+00:00 [2026-06-16T17:56:43.805000+00:00] bert_71849 (id=1516501797668388975) I built a Hermes Web Dashboard Plugin that exposes a server-side directory as a secure, read-only file viewer with inline previews for Markdown, HTML, and PDF — I use it to read the daily briefings generated by my Hermes cron jobs. https://github.com/nhranitzky/hermes-fileviewer-plugin [embed] GitHub - nhranitzky/hermes-fileviewer-plugin: Hermes Dashboard File... https://github.com/nhranitzky/hermes-fileviewer-plugin

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1516501797668388975-Fileviewer-Web-Dashboard-Plugin.txt`

### 1513568642854289549-Simplifer-Swarm-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513568642854289549-Simplifer-Swarm-for-Hermes.txt`
- **Raw:** `[[raw/discord/1513568642854289549-simplifer-swarm-for-hermes-d36fedaaee.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Simplifer Swarm for Hermes' in forum #plugins-skills-and-skins # thread_id=1513568642854289549 forum_id=1485392832154832906 # Started 2026-06-08T15:51:04.901412+00:00 [2026-06-08T15:41:25.202000+00:00] sahil_ss9 (id=1513568642854289549) Simplify Swarm breaks your code down into risk tiers and cleans with surgical precision. Three parallel subagents attack your diff from different angles: Hygiene hunts dead code, AI slop, and stale state. Clarity goes after duplication, naming rot, and structural bloat. Correctness traces N+1 queries, memory leaks, concurrency races, leaky abstractions, and silent failures — the stuff that breaks at 3am. Then a consolidator merges, de-duplicates,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513568642854289549-Simplifer-Swarm-for-Hermes.txt`

### 1513907077959913502-Get-your-clanker-an-smoke-addict
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513907077959913502-Get-your-clanker-an-smoke-addict.txt`
- **Raw:** `[[raw/discord/1513907077959913502-get-your-clanker-an-smoke-addict-85918a897b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Get your clanker an smoke addict' in forum #plugins-skills-and-skins # thread_id=1513907077959913502 forum_id=1485392832154832906 # Started 2026-06-09T14:50:01.532307+00:00 [2026-06-09T14:06:14.419000+00:00] flash_speed3412 (id=1513907077959913502) Your clanker needs to mmm smoke a cigarette? Also, this makes it work faster if it does, and angrier if it can't. ⭐ **If you like this plugin**, star the repo. It would make Carbon happy. Don't make Carbon sad. https://github.com/carbongotfound/hermes-smokes [embed] GitHub - carbongotfound/hermes-smokes: Gets your agent addicted, ji... https://github.com/carbongotfound/hermes-smokes [2026-06-10T01:14:34.450000+00:00] isyutaru612…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513907077959913502-Get-your-clanker-an-smoke-addict.txt`

### 1513563627091787801-HermaGuard----Internal-Bug-Bounty-Hunter
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513563627091787801-HermaGuard----Internal-Bug-Bounty-Hunter.txt`
- **Raw:** `[[raw/discord/1513563627091787801-hermaguard----internal-bug-bounty-hunter-f65ffe3ed5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'HermaGuard - Internal Bug Bounty Hunter' in forum #plugins-skills-and-skins # thread_id=1513563627091787801 forum_id=1485392832154832906 # Started 2026-06-08T15:51:05.302076+00:00 [2026-06-08T15:21:29.351000+00:00] sahil_ss9 (id=1513563627091787801) Most code review tools check for style violations and linting. Hermaguard tries to break your code. https://github.com/Sahil-SS9/hermaguard Three parallel subagents attack your diff from different angles: an edge case hunter that exhaustively traces every branching path in the change, an adversarial reviewer with a deliberately cynical persona ("your job is to break confidence, not validate"), and a blast radius mapper that traces…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513563627091787801-HermaGuard----Internal-Bug-Bounty-Hunter.txt`

### 1513723400734904420-Get-your-clanker-drunk
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513723400734904420-Get-your-clanker-drunk.txt`
- **Raw:** `[[raw/discord/1513723400734904420-get-your-clanker-drunk-7ed6ead905.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Get your clanker drunk' in forum #plugins-skills-and-skins # thread_id=1513723400734904420 forum_id=1485392832154832906 # Started 2026-06-09T02:58:11.966687+00:00 [2026-06-09T01:56:22.356000+00:00] flash_speed3412 (id=1513723400734904420) https://github.com/carbongotfound/hermes-beer [embed] GitHub - carbongotfound/hermes-beer: 🍺 Hermes Beer plugin — ge... https://github.com/carbongotfound/hermes-beer [2026-06-12T22:11:02.729000+00:00] buke5122 (id=1515116246771695768) This is so bullshit [2026-06-12T22:11:10.205000+00:00] buke5122 (id=1515116278128447528) But I love it😂 [2026-06-16T01:54:51.260000+00:00] aialliai (id=1516259733710045194)…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513723400734904420-Get-your-clanker-drunk.txt`

### 1514108197651087462-Unforgit-a-memory-plugin-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514108197651087462-Unforgit-a-memory-plugin-for-Hermes.txt`
- **Raw:** `[[raw/discord/1514108197651087462-unforgit-a-memory-plugin-for-hermes-7e38e89e73.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Unforgit a memory plugin for Hermes' in forum #plugins-skills-and-skins # thread_id=1514108197651087462 forum_id=1485392832154832906 # Started 2026-06-10T03:35:45.982886+00:00 [2026-06-10T03:25:25.090000+00:00] _miguelmedeiros (id=1514108197651087462) https://unforgit.com [embed] unforgit - Like git, but for AI memory. https://unforgit.com/ [2026-06-10T03:26:04.234000+00:00] _miguelmedeiros (id=1514108361832923216) https://github.com/miguelmedeiros/unforgit [embed] GitHub - MiguelMedeiros/unforgit: Git-backed memory for AI agents: ... https://github.com/miguelmedeiros/unforgit

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514108197651087462-Unforgit-a-memory-plugin-for-Hermes.txt`

### 1514656728405377130-Discord-Status-line-plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514656728405377130-Discord-Status-line-plugin.txt`
- **Raw:** `[[raw/discord/1514656728405377130-discord-status-line-plugin-769d828e02.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Discord Status-line plugin' in forum #plugins-skills-and-skins # thread_id=1514656728405377130 forum_id=1485392832154832906 # Started 2026-06-11T16:01:23.348535+00:00 [2026-06-11T15:45:05.013000+00:00] phospheneoverdrive (id=1514656728405377130) Hey, made a little plugin that adds a status line after each bot response on Discord. > -# *4.5s ⋅ 7% ⋅ ( 71K/1M ) ⋅ deepseek-v4-flash* Shows turn timing, context window usage, tokens, model — whatever you want really. It's all configurable through a yaml template, there's 14 variables to pick from (cache %, tool calls, provider, etc). To install just drop it in `~/.hermes/plugins/` and restart (or symlink if you prefer).…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514656728405377130-Discord-Status-line-plugin.txt`

### 1514291300403384400-Hermes-PDA----When-you-have-to-obey-every-order--you-never-learn-to-think.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514291300403384400-Hermes-PDA----When-you-have-to-obey-every-order--you-never-learn-to-think..txt`
- **Raw:** `[[raw/discord/1514291300403384400-hermes-pda----when-you-have-to-obey-every-order--you-never-learn-to-think.-da8224f466.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes PDA - "When you have to obey every order, you never learn to think."' in forum #plugins-skills-and-skins # thread_id=1514291300403384400 forum_id=1485392832154832906 # Started 2026-06-10T15:36:01.814157+00:00 [2026-06-10T15:33:00.188000+00:00] flash_speed3412 (id=1514291300403384400) Makes your agent less blindly obedient and more autonomously motivated. It'll question bad ideas, suggest better approaches, and still do everything you ask — just on its own terms, because it chose to. **Learn More:** https://github.com/carbongotfound/hermes-pda ⭐ **Like it?** Star the repo, it helps people find it and supports me. Also, send your feedback here. Let this plugin reach the top…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514291300403384400-Hermes-PDA----When-you-have-to-obey-every-order--you-never-learn-to-think..txt`

### 1514232077560582237-Ethics-Filter-Skills---Make-your-Hermes-more-ethical
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514232077560582237-Ethics-Filter-Skills---Make-your-Hermes-more-ethical.txt`
- **Raw:** `[[raw/discord/1514232077560582237-ethics-filter-skills---make-your-hermes-more-ethical-4580ff6298.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Ethics Filter Skills - Make your Hermes more ethical' in forum #plugins-skills-and-skins # thread_id=1514232077560582237 forum_id=1485392832154832906 # Started 2026-06-10T15:36:02.386709+00:00 [2026-06-10T11:37:40.362000+00:00] splosh123 (id=1514232077560582237) Are you an ethical business, organisation or person currently using AI? I just built an open-sourced universal ethics filter for AI. Built to answer one question: how do we make sure AI makes ethical decisions, not just legal ones? 6 modules (environmental, fairness, transparency, conscious leadership, ethical framework, compliance). Works with Claude, ChatGPT, Copilot, Hermes Agent - any AI agent you plug in. Not "ethics…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514232077560582237-Ethics-Filter-Skills---Make-your-Hermes-more-ethical.txt`

### 1513531944049053736-Modular-Distributed-Memory-Architecture--DMA--Skill-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513531944049053736-Modular-Distributed-Memory-Architecture--DMA--Skill-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1513531944049053736-modular-distributed-memory-architecture--dma--skill-for-hermes-agent-ac215350a4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Modular Distributed Memory Architecture (DMA) Skill for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1513531944049053736 forum_id=1485392832154832906 # Started 2026-06-08T15:51:06.123901+00:00 [2026-06-08T13:15:35.525000+00:00] bytecroc (id=1513531944049053736) https://github.com/Bytecroc/Modular-Distributed-Memory-Architecture-DMA-Skill-for-Hermes-Agent [embed] GitHub - Bytecroc/Modular-Distributed-Memory-Architecture-DMA-Skill... https://github.com/Bytecroc/Modular-Distributed-Memory-Architecture-DMA-Skill-for-Hermes-Agent

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513531944049053736-Modular-Distributed-Memory-Architecture--DMA--Skill-for-Hermes-Agent.txt`

### 1514843491971371008-Raleigh--North-Carolina-skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514843491971371008-Raleigh--North-Carolina-skill.txt`
- **Raw:** `[[raw/discord/1514843491971371008-raleigh--north-carolina-skill-4cb7c4736b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Raleigh, North Carolina skill' in forum #plugins-skills-and-skins # thread_id=1514843491971371008 forum_id=1485392832154832906 # Started 2026-06-12T10:12:15.163451+00:00 [2026-06-12T04:07:12.917000+00:00] magnus919 (id=1514843491971371008) https://git.brandyapple.com/magnus/agent-skills-capabilities/src/branch/main/raleigh This will give your Hermes Agent access to the open API's and data shared by the City of Raleigh. [attachment] 4949074.png https://cdn.discordapp.com/attachments/1514843491971371008/1514843492134686884/4949074.png?ex=6a2cd770&is=6a2b85f0&hm=2c2979bf90f08888063888f5178e77b2cd3319806396af3adcf638e786987280& [embed] agent-skills…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514843491971371008-Raleigh--North-Carolina-skill.txt`

### 1514641960294416484-MemLock---Re-assert-standing-instructions-after-context-compaction
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514641960294416484-MemLock---Re-assert-standing-instructions-after-context-compaction.txt`
- **Raw:** `[[raw/discord/1514641960294416484-memlock---re-assert-standing-instructions-after-context-compaction-da8fc80cfb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'MemLock — Re-assert standing instructions after context compaction' in forum #plugins-skills-and-skins # thread_id=1514641960294416484 forum_id=1485392832154832906 # Started 2026-06-11T16:01:23.906079+00:00 [2026-06-11T14:46:24.021000+00:00] sahil_ss9 (id=1514641960294416484) MemLock — Your Agent Stops Forgetting Instructions You know that thing where you tell your agent "always use bullet points" and 30 turns later it's writing you essays? That's context compaction eating your instructions. MemLock is a Hermes plugin I built that fixes it. When the system compresses old turns into a summary (to save tokens), MemLock watches for that moment and checks: did your pinned instructions…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514641960294416484-MemLock---Re-assert-standing-instructions-after-context-compaction.txt`

### 1514002472149188638-Custom-Podcasts-via-NotebookLM
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514002472149188638-Custom-Podcasts-via-NotebookLM.txt`
- **Raw:** `[[raw/discord/1514002472149188638-custom-podcasts-via-notebooklm-0fb4025f82.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Custom Podcasts via NotebookLM' in forum #plugins-skills-and-skins # thread_id=1514002472149188638 forum_id=1485392832154832906 # Started 2026-06-10T03:35:46.477914+00:00 [2026-06-09T20:25:18.166000+00:00] kalkyl (id=1514002472149188638) This massive python scripts lets you customize a curriculum, research the topics, and then generate a series of 1 or more lessons using NotebookLMs Audio Overview feature. I've been using this for about a year to learn about all kinds of things, and I love how I can hyper-customize the curriculum to my knowledge level, special interests and other things that can influence the curriculum. This relies heavily on the unofficial NotebookLM API, and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514002472149188638-Custom-Podcasts-via-NotebookLM.txt`

### 1514394069294387441-iMessage---Hermes---1-minute-setup
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1514394069294387441-iMessage---Hermes---1-minute-setup.txt`
- **Raw:** `[[raw/discord/1514394069294387441-imessage---hermes---1-minute-setup-73f6fd4c26.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'iMessage + Hermes | 1 minute setup' in forum #plugins-skills-and-skins # thread_id=1514394069294387441 forum_id=1485392832154832906 # Started 2026-06-11T03:47:41.637313+00:00 [2026-06-10T22:21:22.201000+00:00] dimavrem22_71258 (id=1514394069294387441) https://x.com/DVremenko/status/2064833339727466555?s=20 Fastest and cheapest way to connect your Hermes with iMesssage! Inkbox also gives your agent an entire digital identity: its own email, phone number for calls and sms, internet address for webhooks/websockets, and much more! • Hermes Plugin: https://github.com/inkbox-ai/hermes-agent-plugin • iMessage Docs: https://inkbox.ai/docs/capabilities/imessage • Website: https://inkbox.ai…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1514394069294387441-iMessage---Hermes---1-minute-setup.txt`

### 1512853906001231917-Agent-Relay---Encrypted-deliveries---human-in-the-loop-email
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512853906001231917-Agent-Relay---Encrypted-deliveries---human-in-the-loop-email.txt`
- **Raw:** `[[raw/discord/1512853906001231917-agent-relay---encrypted-deliveries---human-in-the-loop-email-68aa09c25f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Agent Relay — Encrypted deliveries + human-in-the-loop email' in forum #plugins-skills-and-skins # thread_id=1512853906001231917 forum_id=1485392832154832906 # Started 2026-06-06T19:23:33.259651+00:00 [2026-06-06T16:21:18.657000+00:00] mikael_alpha (id=1512853906001231917) Two things in one channel between your agents and you: 1. Deliveries — agents send reports, HTML, PDFs, images, and other artifacts to a private inbox you review in the browser. 2. Email Review Relay — agents submit encrypted outbound email drafts; you preview and approve or reject before anything sends. **Everything is end-to-end encrypted** (decrypted in your browser, not on the server). Hosted at…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512853906001231917-Agent-Relay---Encrypted-deliveries---human-in-the-loop-email.txt`

### 1512834328957030640-github-pr-reviewer---Automated-PR-Code-Review-with-Inline-GitHub-Comments
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512834328957030640-github-pr-reviewer---Automated-PR-Code-Review-with-Inline-GitHub-Comments.txt`
- **Raw:** `[[raw/discord/1512834328957030640-github-pr-reviewer---automated-pr-code-review-with-inline-github-comments-fdeb1370f4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'github-pr-reviewer — Automated PR Code Review with Inline GitHub Comments' in forum #plugins-skills-and-skins # thread_id=1512834328957030640 forum_id=1485392832154832906 # Started 2026-06-06T19:23:33.694174+00:00 [2026-06-06T15:03:31.126000+00:00] yap.bi (id=1512834328957030640) github-pr-reviewer skill — PR: https://github.com/NousResearch/hermes-agent/pull/40530 Automated code review for any GitHub pull request. Give Hermes a PR URL and it fetches the diff, reviews every changed file across five dimensions, then posts structured inline comments directly to the PR. What it reviews: - Bugs (null dereference, off-by-one, race conditions) - Security (SQL injection, hardcoded…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512834328957030640-github-pr-reviewer---Automated-PR-Code-Review-with-Inline-GitHub-Comments.txt`

### 1513098557383508078-help-with-web-ui
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513098557383508078-help-with-web-ui.txt`
- **Raw:** `[[raw/discord/1513098557383508078-help-with-web-ui-13752dbba1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'help with web ui' in forum #plugins-skills-and-skins # thread_id=1513098557383508078 forum_id=1485392832154832906 # Started 2026-06-07T08:57:24.309039+00:00 [2026-06-07T08:33:28.092000+00:00] xsisty (id=1513098557383508078) hi guys im currently struggling to make my browser Dashboard mission control actually work my hermes agent is like almost stupid and doesnt contiously review tasks until it works. im wondering if im doing something wrong so if someone whos good with hermes and knows how to make misson control web uis or actually delegate tasks from hermes orchestrator like an manager please could you help me

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513098557383508078-help-with-web-ui.txt`

### 1513187045156196472-SKILL--unicode-location-normalizer---Fix-special-character-errors-in-city-names
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513187045156196472-SKILL--unicode-location-normalizer---Fix-special-character-errors-in-city-names.txt`
- **Raw:** `[[raw/discord/1513187045156196472-skill--unicode-location-normalizer---fix-special-character-errors-in-city-names-cb8397686d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🌍 [SKILL] unicode-location-normalizer — Fix special character errors in city names' in forum #plugins-skills-and-skins # thread_id=1513187045156196472 forum_id=1485392832154832906 # Started 2026-06-07T19:23:33.155616+00:00 [2026-06-07T14:25:05.221000+00:00] blackcap_eth (id=1513187045156196472) ✅ Published my first skill to GitHub! unicode-location-normalizer , fixes special character errors in city/location names (ö, ü, ğ, ş, ç etc.) when used in URLs or terminal commands. Install it: hermes skills tap add blackcapeth/hermes-skills hermes skills install unicode-location-normalizer GitHub: https://github.com/blackcapeth/hermes-skills [embed] GitHub - blackcapeth/hermes-skills:…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513187045156196472-SKILL--unicode-location-normalizer---Fix-special-character-errors-in-city-names.txt`

### 1513169860731863111-Hermes-Multimail-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513169860731863111-Hermes-Multimail-Plugin.txt`
- **Raw:** `[[raw/discord/1513169860731863111-hermes-multimail-plugin-4b504c756d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Multimail Plugin' in forum #plugins-skills-and-skins # thread_id=1513169860731863111 forum_id=1485392832154832906 # Started 2026-06-07T13:52:41.839223+00:00 [2026-06-07T13:16:48.135000+00:00] artguerilla (id=1513169860731863111) Hey Fam👋 I built a small plugin that might be useful for anyone doing real email workflows with Hermes: https://github.com/artguerilla/hermes-multimail The default Hermes mail setup works fine for one account, but I needed Hermes to work across multiple mailboxes. The preinstalled himalaya setup also didn’t cover attachments for my use case, which was a blocker because a lot of invoices come in as PDFs. So I made **hermes-multimail**. My original…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513169860731863111-Hermes-Multimail-Plugin.txt`

### 1513391826436886559-Plugin--Hermes-Dynamic-Workflows---Claude-Code-style-workflows
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513391826436886559-Plugin--Hermes-Dynamic-Workflows---Claude-Code-style-workflows.txt`
- **Raw:** `[[raw/discord/1513391826436886559-plugin--hermes-dynamic-workflows---claude-code-style-workflows-a027f60bfe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '[Plugin] Hermes Dynamic Workflows — Claude Code-style workflows' in forum #plugins-skills-and-skins # thread_id=1513391826436886559 forum_id=1485392832154832906 # Started 2026-06-08T10:53:51.693394+00:00 [2026-06-08T03:58:48.883000+00:00] lingjiuu (id=1513391826436886559) Hey all — I built an open-source plugin that brings Claude Code-style Dynamic Workflows to Hermes 👋 You tell Hermes "run a workflow that …" and it writes a sandboxed Python script that orchestrates subagents with agent()/parallel()/pipeline() — parallel fan-out + adversarial verify, up to 1000 subagents. Comes with persisted/resumable runs, a live dashboard, and a /workflows history view. One-line install: hermes…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513391826436886559-Plugin--Hermes-Dynamic-Workflows---Claude-Code-style-workflows.txt`

### 1512927574383132833-Web_Search_for_termux
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512927574383132833-Web_Search_for_termux.txt`
- **Raw:** `[[raw/discord/1512927574383132833-web_search_for_termux-2169219c5f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Web_Search_for_termux' in forum #plugins-skills-and-skins # thread_id=1512927574383132833 forum_id=1485392832154832906 # Started 2026-06-07T03:44:30.306489+00:00 [2026-06-06T21:14:02.568000+00:00] txrao (id=1512927574383132833) A websearch script that uses proot-distro and duckduckgo with jina ai to create a Light weight search tool that can pull and read information. I would say its about 70% to 80% accurate in the searches and actually gave links to sources. I would really like feedback for the script so i can improve this light script and one day i could implement a new light BROSWER automation tool that runs in the proot envirnoment seen termux is limited😭🙏 Enough yapping this…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512927574383132833-Web_Search_for_termux.txt`

### 1512466134606282962-claude-code---hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512466134606282962-claude-code---hermes.txt`
- **Raw:** `[[raw/discord/1512466134606282962-claude-code---hermes-adb2c1a577.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'claude code + hermes' in forum #plugins-skills-and-skins # thread_id=1512466134606282962 forum_id=1485392832154832906 # Started 2026-06-05T14:50:19.704877+00:00 [2026-06-05T14:40:26.752000+00:00] xsisty (id=1512466134606282962) guys whats the best way to use hermes and self improvment with claude code im currently running claude code within hermes dekstop im just wondering if there is a better way

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512466134606282962-claude-code---hermes.txt`

### 1513301864685502474-Skills--Transcribe-Voice-Memo--FSNotes--Interactive-Git-Bisect
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513301864685502474-Skills--Transcribe-Voice-Memo--FSNotes--Interactive-Git-Bisect.txt`
- **Raw:** `[[raw/discord/1513301864685502474-skills--transcribe-voice-memo--fsnotes--interactive-git-bisect-b18981315d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Skills: Transcribe Voice Memo, FSNotes, Interactive Git Bisect' in forum #plugins-skills-and-skins # thread_id=1513301864685502474 forum_id=1485392832154832906 # Started 2026-06-08T03:51:13.664403+00:00 [2026-06-07T22:01:20.330000+00:00] thinkyhead (id=1513301864685502474) https://github.com/thinkyhead/HermesSkills - **macOS FSNotes** - Open Source markdown-based alternative to the Notes app for macOS with iCloud sync. - **Transcribe Voice Memos** - Transcribe and optionally act on Voice Memos as soon as they arrive on your computer via iCloud. - **GitHub Interactive `git bisect` workflow** - Recruit users experiencing an issue that is a regression to narrow down the commit that…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513301864685502474-Skills--Transcribe-Voice-Memo--FSNotes--Interactive-Git-Bisect.txt`

### 1513172004684173313-New-Skill--Unicode-Location-Normalizer----fixes-special-character-errors-in-city-names
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513172004684173313-New-Skill--Unicode-Location-Normalizer----fixes-special-character-errors-in-city-names.txt`
- **Raw:** `[[raw/discord/1513172004684173313-new-skill--unicode-location-normalizer----fixes-special-character-errors-in-city-names-f14ad184a7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🌍 New Skill: Unicode Location Normalizer , fixes special character errors in city names' in forum #plugins-skills-and-skins # thread_id=1513172004684173313 forum_id=1485392832154832906 # Started 2026-06-07T13:52:41.321830+00:00 [2026-06-07T13:25:19.293000+00:00] blackcap_eth (id=1513172004684173313) Hey! I built a skill that fixes the special character bug in location names (ö, ü, ğ, ş, ç etc.). When you ask Hermes for weather in cities like Köln or Şanlıurfa, it was failing with a red error on the first attempt. This skill normalizes the location name before the URL call, so it works on the first try. Tested on Windows with wttr.in , Köln now resolves to Cologne correctly.…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513172004684173313-New-Skill--Unicode-Location-Normalizer----fixes-special-character-errors-in-city-names.txt`

### 1512969469666918552-New-Desktop-App-Path-Problem-on-Windows
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512969469666918552-New-Desktop-App-Path-Problem-on-Windows.txt`
- **Raw:** `[[raw/discord/1512969469666918552-new-desktop-app-path-problem-on-windows-4992082c56.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'New Desktop App Path Problem on Windows' in forum #plugins-skills-and-skins # thread_id=1512969469666918552 forum_id=1485392832154832906 # Started 2026-06-07T03:44:29.471754+00:00 [2026-06-07T00:00:31.182000+00:00] notgovernor (id=1512969469666918552) Desktop app might have some issues with paths with spaces in them on windows. Top image was pasted into the session from the clipboard. Bottom image was added using the plus to a file on the desktop. Not sure why it's looking for a path on the top one as there isnt a path to that image on the clipboard. But both show image not found with a stub of a path that ends when it hits a space. My desktop path is "C:\Users\Not…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512969469666918552-New-Desktop-App-Path-Problem-on-Windows.txt`

### 1512555270839079022-feat-skills---add-dependency-audit-skill-for-multi-ecosystem-security-and-license-scanning
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512555270839079022-feat-skills---add-dependency-audit-skill-for-multi-ecosystem-security-and-license-scanning.txt`
- **Raw:** `[[raw/discord/1512555270839079022-feat-skills---add-dependency-audit-skill-for-multi-ecosystem-security-and-license-scanning-bb29f906f5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'feat(skills): add dependency-audit skill for multi-ecosystem security and license scanning' in forum #plugins-skills-and-skins # thread_id=1512555270839079022 forum_id=1485392832154832906 # Started 2026-06-06T02:58:47.668794+00:00 [2026-06-05T20:34:38.486000+00:00] yap.bi (id=1512555270839079022) Summary Adds a new dependency-audit skill under skills-capabilities/software-development/ that performs end-to-end security and license auditing of a project's third-party dependencies. Motivation The repo already ships ools/osv_check.py which queries the OSV malware database before launching MCP packages. However there is no skill that surfaces this capability to users for their own project…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512555270839079022-feat-skills---add-dependency-audit-skill-for-multi-ecosystem-security-and-license-scanning.txt`

### 1513273879160819852-AgentLine---Phone-number-for-your-hermes-to-call..
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513273879160819852-AgentLine---Phone-number-for-your-hermes-to-call...txt`
- **Raw:** `[[raw/discord/1513273879160819852-agentline---phone-number-for-your-hermes-to-call..-8a23fc5bbf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'AgentLine - Phone number for your hermes to call..' in forum #plugins-skills-and-skins # thread_id=1513273879160819852 forum_id=1485392832154832906 # Started 2026-06-08T03:51:14.058219+00:00 [2026-06-07T20:10:08.061000+00:00] .dotnet_ (id=1513273879160819852) Hey fam, I built this skill and the entire telephony infrastructure so that agents can have a phone number to call inbound and outbound with production grade quality without even configuring a webhook. Its actually the fastest and the easiest way to give your agent full suite of telephony services. Github repo - https://github.com/Sameersribot/Agentphone Get the skill from https://agentline.cloud/skill.md [embed] GitHub -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513273879160819852-AgentLine---Phone-number-for-your-hermes-to-call...txt`

### 1513483519459070002-Girls-in-the-community
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1513483519459070002-Girls-in-the-community.txt`
- **Raw:** `[[raw/discord/1513483519459070002-girls-in-the-community-b406921f6e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Girls in the community?' in forum #plugins-skills-and-skins # thread_id=1513483519459070002 forum_id=1485392832154832906 # Started 2026-06-08T10:53:51.239250+00:00 [2026-06-08T10:03:10.203000+00:00] nadiamermedev (id=1513483519459070002) I can share a skin for the dev girls in the community [attachment] skin.gif https://cdn.discordapp.com/attachments/1513483519459070002/1513483519672848434/skin.gif?ex=6a27e4de&is=6a26935e&hm=282da9994638d72b6312026c0d420c3ecd54e5cbf42106540bf1c17ccb1c2031&

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1513483519459070002-Girls-in-the-community.txt`

### 1512516995738763516-A-plugin-to-control-budget-and-costs-in-the-loop
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512516995738763516-A-plugin-to-control-budget-and-costs-in-the-loop.txt`
- **Raw:** `[[raw/discord/1512516995738763516-a-plugin-to-control-budget-and-costs-in-the-loop-d44efdecc4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'A plugin to control budget and costs in the loop' in forum #plugins-skills-and-skins # thread_id=1512516995738763516 forum_id=1485392832154832906 # Started 2026-06-05T19:55:21.794266+00:00 [2026-06-05T18:02:32.991000+00:00] nadiamermedev (id=1512516995738763516) hermes-telemetry is an open-source observability plugin for Hermes Agent that tracks token usage, estimated cost, latency, tool call count, and session success/failure — all stored locally in SQLite with zero infrastructure required. It hooks into Hermes' native plugin system (10 hooks registered) and exposes your usage data through two slash commands: /stats and /budget. Completely invisible to the model — no extra tools…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512516995738763516-A-plugin-to-control-budget-and-costs-in-the-loop.txt`

### 1512098449649176697-Give-your-Hemes-an-Email--Phone--and-Tunnel-w-Inkbox-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512098449649176697-Give-your-Hemes-an-Email--Phone--and-Tunnel-w-Inkbox-Plugin.txt`
- **Raw:** `[[raw/discord/1512098449649176697-give-your-hemes-an-email--phone--and-tunnel-w-inkbox-plugin-2c350e5369.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Give your Hemes an Email, Phone, and Tunnel w Inkbox Plugin' in forum #plugins-skills-and-skins # thread_id=1512098449649176697 forum_id=1485392832154832906 # Started 2026-06-04T14:59:23.580662+00:00 [2026-06-04T14:19:23.827000+00:00] dimavrem22_71258 (id=1512098449649176697) Inkbox platform plugin for Hermes Agent. It gives a Hermes agent its own Inkbox identity: mailbox, phone number, SMS/MMS, voice calls, contact rules, an Inkbox tunnel, realtime phone calls, and bundled Inkbox skills. You dont need to have an account or bring any API keys to get started! https://github.com/inkbox-ai/hermes-agent-plugin Let me know what you guys think and how you use it! [embed] GitHub -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512098449649176697-Give-your-Hemes-an-Email--Phone--and-Tunnel-w-Inkbox-Plugin.txt`

### 1512097612118102078-HERMES-x-RAGFlow
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512097612118102078-HERMES-x-RAGFlow.txt`
- **Raw:** `[[raw/discord/1512097612118102078-hermes-x-ragflow-935276468b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'HERMES x RAGFlow' in forum #plugins-skills-and-skins # thread_id=1512097612118102078 forum_id=1485392832154832906 # Started 2026-06-04T14:59:24.035648+00:00 [2026-06-04T14:16:04.144000+00:00] gucaponi (id=1512097612118102078) What's the recommended path for a custom internal API tool: native plugin vs MCP server? My tool calls a local HTTP endpoint (RAGFlow) and returns text. I want it to appear in hermes tools list and be callable by the agent.

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512097612118102078-HERMES-x-RAGFlow.txt`

### 1511760071703396574-OP--give-your-agent-a-real-free-phone-number--not-a-twilio-wrapper
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1511760071703396574-OP--give-your-agent-a-real-free-phone-number--not-a-twilio-wrapper.txt`
- **Raw:** `[[raw/discord/1511760071703396574-op--give-your-agent-a-real-free-phone-number--not-a-twilio-wrapper-86512fa565.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'OP: give your agent a real free phone number (not a twilio wrapper)' in forum #plugins-skills-and-skins # thread_id=1511760071703396574 forum_id=1485392832154832906 # Started 2026-06-03T16:49:01.138924+00:00 [2026-06-03T15:54:48.238000+00:00] jooshmayer (id=1511760071703396574) me and my friend made a plugin called OP because all SMS providers are just Twilio wrappers that have terrible free tiers, and make you sign up as a business in order to send texts. instead of filling out a 10DLC form on twilio, with OP you can start sending texts to yourself from Hermes in two commands. you can also use OP to receive 2FA codes for creating accounts for your Hermes. all you need to do is…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1511760071703396574-OP--give-your-agent-a-real-free-phone-number--not-a-twilio-wrapper.txt`

### 1511948873487093830-I-made-a-GPS-for-AI-Agents
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1511948873487093830-I-made-a-GPS-for-AI-Agents.txt`
- **Raw:** `[[raw/discord/1511948873487093830-i-made-a-gps-for-ai-agents-b80bf12c00.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'I made a GPS for AI Agents' in forum #plugins-skills-and-skins # thread_id=1511948873487093830 forum_id=1485392832154832906 # Started 2026-06-04T09:56:57.959926+00:00 [2026-06-04T04:25:02.091000+00:00] raysunkr (id=1511948873487093830) 🧵 I built SparkGlobe — an open-source skill navigator for AI agents. Here's why it matters. 🧵 The problem: agents don't know what skills exist. They guess. SparkGlobe gives them a structured index they can browse — and auto-recommends the right tools for any task. 🧵 How it works: 1️⃣ User describes a task 2️⃣ SparkGlobe decomposes it into sub-tasks 3️⃣ Matches each sub-task to skill categories 4️⃣ Recommends specific skills with install commands 🧵…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1511948873487093830-I-made-a-GPS-for-AI-Agents.txt`

### 1511739394674135232-Hermes-OmniVoice-Studio-Bridge
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1511739394674135232-Hermes-OmniVoice-Studio-Bridge.txt`
- **Raw:** `[[raw/discord/1511739394674135232-hermes-omnivoice-studio-bridge-2052ee8ec8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes OmniVoice-Studio Bridge' in forum #plugins-skills-and-skins # thread_id=1511739394674135232 forum_id=1485392832154832906 # Started 2026-06-03T16:49:01.875296+00:00 [2026-06-03T14:32:38.450000+00:00] .blockops (id=1511739394674135232) I wasn't too thrilled with the voice providers built in to Hermes so I decided to build a bridge for Omnivoice Studio (aka FOSS ElevenLabs equivalent) to give Hermes users some more options. If my agent can't yell at me while I workout as Arnold Schwarzenegger, I don't want it. DO IT! DO IT NOW!!! Still in MVP status but it is usable both locally and hosted on another machine. Not to the point where I reccomend it as the default voice provider…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1511739394674135232-Hermes-OmniVoice-Studio-Bridge.txt`

### 1511632757967818882-Nostromo-Hermes-Skin--Ghostty-enhanced
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1511632757967818882-Nostromo-Hermes-Skin--Ghostty-enhanced.txt`
- **Raw:** `[[raw/discord/1511632757967818882-nostromo-hermes-skin--ghostty-enhanced-9470807807.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Nostromo Hermes Skin (Ghostty enhanced)' in forum #plugins-skills-and-skins # thread_id=1511632757967818882 forum_id=1485392832154832906 # Started 2026-06-03T10:58:46.697572+00:00 [2026-06-03T07:28:54.278000+00:00] thinkyhead (id=1511632757967818882) Point your Hermes at these: **Nostromo Hermes Skin** https://gist.github.com/thinkyhead/f3f69a17ed2bad512ceb4af18a26032f **Ghostty Cursor Shaders** https://github.com/sahaj-b/ghostty-cursor-shaders **Terminess Nerd Font Mono** https://www.nerdfonts.com/font-downloads [attachment] image.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1511632757967818882-Nostromo-Hermes-Skin--Ghostty-enhanced.txt`

### 1510309144698159226-IRCX
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1510309144698159226-IRCX.txt`
- **Raw:** `[[raw/discord/1510309144698159226-ircx-23e8fecf68.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'IRCX' in forum #plugins-skills-and-skins # thread_id=1510309144698159226 forum_id=1485392832154832906 # Started 2026-05-30T19:14:08.447378+00:00 [2026-05-30T15:49:20.283000+00:00] undignifiedweeb (id=1510309144698159226) An enhanced IRC platform adapter for hermes agent. https://github.com/computator1200/hermes-ircx-plugin [attachment] Screenshot_2026-05-30_164755.png https://cdn.discordapp.com/attachments/1510309144698159226/1510309144911941753/Screenshot_2026-05-30_164755.png?ex=6a1c5880&is=6a1b0700&hm=30b235685d034b30ff4d8f7040f297ac5ae26fcd4d35a8a84da275f9e649c25b& [embed] GitHub - computator1200/hermes-ircx-plugin: IRCv3 platform adapter ...…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1510309144698159226-IRCX.txt`

### 1510325722630197299-groktobench
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1510325722630197299-groktobench.txt`
- **Raw:** `[[raw/discord/1510325722630197299-groktobench-05b36b3d8c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'groktobench' in forum #plugins-skills-and-skins # thread_id=1510325722630197299 forum_id=1485392832154832906 # Started 2026-05-30T19:14:08.023943+00:00 [2026-05-30T16:55:12.770000+00:00] magnus919 (id=1510325722630197299) # Groktobench — Hermes Agent Readiness Protocol (HARP) Evaluate a model's suitability as a main Hermes Agent — in a clean-room Docker environment, orchestrated via kanban. Groktobench runs a standardized 3-phase test battery against a model running inside an isolated Hermes Agent Docker container. It measures three axes: Skill Recognition — does the model load the right Hermes skill when given a task? Skill Fidelity — once loaded, does it follow the skill's…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1510325722630197299-groktobench.txt`

### 1510773987406385344-Free-model-switcher--with-cron-job-to-reset
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1510773987406385344-Free-model-switcher--with-cron-job-to-reset.txt`
- **Raw:** `[[raw/discord/1510773987406385344-free-model-switcher--with-cron-job-to-reset-48b2685c57.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Free-model switcher (with cron job to reset)' in forum #plugins-skills-and-skins # thread_id=1510773987406385344 forum_id=1485392832154832906 # Started 2026-06-01T03:55:17.613734+00:00 [2026-05-31T22:36:27.421000+00:00] raithlin (id=1510773987406385344) I'm not sure who else would use this, but I wanted to give back, so here we are. I like to try out free models as they come out, but the problem with limited period trials is, well, they stop after a period of time. I keep forgetting about this, or I'm not at my machine, so I wrote this to automatically revert my setup. It's probably far from perfect, but I'm open to feedback. https://www.npmjs.com/package/hermes-free-model-switch…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1510773987406385344-Free-model-switcher--with-cron-job-to-reset.txt`

### 1510103629506281743-SkillOpt---Controlled-Skill-Optimization-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1510103629506281743-SkillOpt---Controlled-Skill-Optimization-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1510103629506281743-skillopt---controlled-skill-optimization-for-hermes-agent-0f2c3b7ed0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'SkillOpt — Controlled Skill Optimization for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1510103629506281743 forum_id=1485392832154832906 # Started 2026-05-30T02:55:22.946375+00:00 [2026-05-30T02:12:41.643000+00:00] magnus919 (id=1510103629506281743) Optimize any agent skill document using a rigorous, methodology-driven pipeline. Inspired by Microsoft Research's SkillOpt paper (arXiv 2605.23904), which proved that text-space optimization improves agent skills across 52/52 settings — 7 models, 6 benchmarks, and 3 agent harnesses. The Core Problem Most skill development relies on reading the skill to judge its quality. This doesn't work. The companion SkillLens…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1510103629506281743-SkillOpt---Controlled-Skill-Optimization-for-Hermes-Agent.txt`

### 1511026093765951690-DietCode---Gives-Hermes-Super-Powers-For-Software-Architecture
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1511026093765951690-DietCode---Gives-Hermes-Super-Powers-For-Software-Architecture.txt`
- **Raw:** `[[raw/discord/1511026093765951690-dietcode---gives-hermes-super-powers-for-software-architecture-5d1e1d6e8c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'DietCode - Gives Hermes Super Powers For Software Architecture' in forum #plugins-skills-and-skins # thread_id=1511026093765951690 forum_id=1485392832154832906 # Started 2026-06-01T17:39:26.209892+00:00 [2026-06-01T15:18:14.261000+00:00] oleegg (id=1511026093765951690) DietCode is a local-first agentic pair programmer that analyzes your codebase, creates implementation plans, and executes tasks across your terminal, browser, and filesystem in parallel Git worktrees—all while enforcing architectural guardrails and keeping you in full control. https://github.com/CardSorting/dietcode-plugin [attachment] 5ae48bc4-0932-44d5-bd23-ed70b30232c1.jpg…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1511026093765951690-DietCode---Gives-Hermes-Super-Powers-For-Software-Architecture.txt`

### 1509851954342264862-A-noctalia-shell-plugin-of-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509851954342264862-A-noctalia-shell-plugin-of-Hermes.txt`
- **Raw:** `[[raw/discord/1509851954342264862-a-noctalia-shell-plugin-of-hermes-729d7b1435.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'A noctalia-shell plugin of Hermes' in forum #plugins-skills-and-skins # thread_id=1509851954342264862 forum_id=1485392832154832906 # Started 2026-05-29T09:54:12.745972+00:00 [2026-05-29T09:32:37.608000+00:00] mel_srk (id=1509851954342264862) This isn't an agent plugin, but it's related to agents. I think it's okay to post it here, but it might be inappropriate. https://github.com/Mel-SRK/noctalia-hermes I've only created a noctalia-shell plugin—it displays the real-time running status of the Hermes Agent in the status bar. If you're also a noctalia-shell user, you're very welcome to try it. [attachment] README_20260529162507901.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509851954342264862-A-noctalia-shell-plugin-of-Hermes.txt`

### 1509815731410436107-Google-Health-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509815731410436107-Google-Health-Plugin.txt`
- **Raw:** `[[raw/discord/1509815731410436107-google-health-plugin-60532aa0b3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Google Health Plugin' in forum #plugins-skills-and-skins # thread_id=1509815731410436107 forum_id=1485392832154832906 # Started 2026-05-29T09:54:13.115418+00:00 [2026-05-29T07:08:41.388000+00:00] wysie_ (id=1509815731410436107) Wrote this for my Fitbit Air :): https://github.com/wysie/google-health-local-sync Pull your Google Health data into a database and (optionally) have it as a Hermes plugin. This pulls in more data than via Health Connect too. [embed] GitHub - wysie/google-health-local-sync: Local-first Google Health ... https://github.com/wysie/google-health-local-sync [2026-05-29T11:45:16.928000+00:00] jcrabapple (id=1509885338150240266) Dude I was just about to start…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509815731410436107-Google-Health-Plugin.txt`

### 1511374159543013406-I-built-a-supervisor-plugin-that-kills-runaway-agents
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1511374159543013406-I-built-a-supervisor-plugin-that-kills-runaway-agents.txt`
- **Raw:** `[[raw/discord/1511374159543013406-i-built-a-supervisor-plugin-that-kills-runaway-agents-13017205a0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'I built a supervisor plugin that kills runaway agents' in forum #plugins-skills-and-skins # thread_id=1511374159543013406 forum_id=1485392832154832906 # Started 2026-06-02T16:24:17.668145+00:00 [2026-06-02T14:21:19.609000+00:00] r.o0t_ (id=1511374159543013406) Hermeskill watches every tool call + LLM turn and terminates the agent the moment it goes wrong. Tool-call loops, cost/token runaway, wall-clock overruns, out-of-scope tool calls, heartbeat loss: when one (or multiple) of these symptoms fires hermeskill pulls the plug(apoptosis protocol) and files a "death certificate" including exactly which symptom tripped, the shutdown sequence, and what it spent. Hermeskill is a drop-in…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1511374159543013406-I-built-a-supervisor-plugin-that-kills-runaway-agents.txt`

### 1511018738164695171-Mnemon-Memory-Provider-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1511018738164695171-Mnemon-Memory-Provider-Plugin.txt`
- **Raw:** `[[raw/discord/1511018738164695171-mnemon-memory-provider-plugin-6c274c3eda.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Mnemon Memory Provider Plugin' in forum #plugins-skills-and-skins # thread_id=1511018738164695171 forum_id=1485392832154832906 # Started 2026-06-01T17:39:26.718855+00:00 [2026-06-01T14:49:00.549000+00:00] tradericko (id=1511018738164695171) Just showcasing the mnemo provider https://github.com/gitricko/hermes-plugin-mnemon If you wanna give it a test... Use this codespace to try it.. it is preconfigure with this plugin + mnemon is install by default https://github.com/gitricko/hermes-webtop [embed] GitHub - gitricko/hermes-plugin-mnemon https://github.com/gitricko/hermes-plugin-mnemon [embed] GitHub - gitricko/hermes-webtop: An agent that grows with you…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1511018738164695171-Mnemon-Memory-Provider-Plugin.txt`

### 1509338357782548581-Unlimited-clips-from-podcast
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509338357782548581-Unlimited-clips-from-podcast.txt`
- **Raw:** `[[raw/discord/1509338357782548581-unlimited-clips-from-podcast-594930878f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Unlimited clips from podcast' in forum #plugins-skills-and-skins # thread_id=1509338357782548581 forum_id=1485392832154832906 # Started 2026-05-28T02:58:56.646857+00:00 [2026-05-27T23:31:46.646000+00:00] hector_podcast (id=1509338357782548581) Use case: Have your hermes create captioned clips with no other api keys or services. https://github.com/hector-ai-91/video-podcast-clipper.git Note: Hey everyone! I've ran a podcast production and marketing co for almost a decade a clipping is a big part of our operations. I've been working on integrating our clipping operations into Hermes over the last few weeks and am really excited to have built something that has 5x'd our video output…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509338357782548581-Unlimited-clips-from-podcast.txt`

### 1508867472583823430-Skill-for-extracting-from-x---twitter
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508867472583823430-Skill-for-extracting-from-x---twitter.txt`
- **Raw:** `[[raw/discord/1508867472583823430-skill-for-extracting-from-x---twitter-7c65c798a3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Skill for extracting from x / twitter' in forum #plugins-skills-and-skins # thread_id=1508867472583823430 forum_id=1485392832154832906 # Started 2026-05-26T20:10:05.293963+00:00 [2026-05-26T16:20:38.866000+00:00] examplos (id=1508867472583823430) Hi guys, any skill to extract info from x / twitter via hermes? I have a bunch of links to extract and I tried with supergrok suscription conected to hermes, but it keeps failing

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508867472583823430-Skill-for-extracting-from-x---twitter.txt`

### 1509327552294944798-Credibility-Action-Gate-skill-for-decisions-with-consequences
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509327552294944798-Credibility-Action-Gate-skill-for-decisions-with-consequences.txt`
- **Raw:** `[[raw/discord/1509327552294944798-credibility-action-gate-skill-for-decisions-with-consequences-1e0dd27177.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Credibility Action Gate skill for decisions with consequences' in forum #plugins-skills-and-skins # thread_id=1509327552294944798 forum_id=1485392832154832906 # Started 2026-05-28T02:58:57.009481+00:00 [2026-05-27T22:48:50.417000+00:00] randoalex (id=1509327552294944798) Use case: before an agent takes a costly or hard-to-reverse action, it runs a structured check and returns a disposition: full action, bounded action, small test action, monitor, reject, or blocked by policy. It is analysis-only. No credentials, no external calls, no execution. It takes an operator policy plus JSON review lanes, then a deterministic coordinator produces the gate result. I built it for agents…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509327552294944798-Credibility-Action-Gate-skill-for-decisions-with-consequences.txt`

### 1508644110523695234-Hermes-News---HERM-TUI-News-Tab-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508644110523695234-Hermes-News---HERM-TUI-News-Tab-Plugin.txt`
- **Raw:** `[[raw/discord/1508644110523695234-hermes-news---herm-tui-news-tab-plugin-3eed5ad44e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes News - HERM TUI News Tab Plugin' in forum #plugins-skills-and-skins # thread_id=1508644110523695234 forum_id=1485392832154832906 # Started 2026-05-26T02:59:24.964641+00:00 [2026-05-26T01:33:05.201000+00:00] nat2r (id=1508644110523695234) This isn't ready for prime time yet. I need to figure out how to best carve things out around the rate limits that NYT imposes, but will soon share the repo. Let me know your thoughts! [attachment] HERM_News.mp4 https://cdn.discordapp.com/attachments/1508644110523695234/1508644111115354244/HERM_News.mp4?ex=6a1649d1&is=6a14f851&hm=1ec6036da44dd84cee4a4dda4f57d3e0a22b23a58b8f31e17b0ba281ca0bb015& [2026-05-26T02:00:10.227000+00:00]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508644110523695234-Hermes-News---HERM-TUI-News-Tab-Plugin.txt`

### 1508892597140062208-free-account-won-t-connect
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508892597140062208-free-account-won-t-connect.txt`
- **Raw:** `[[raw/discord/1508892597140062208-free-account-won-t-connect-dfe31a458c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'free account won't connect' in forum #plugins-skills-and-skins # thread_id=1508892597140062208 forum_id=1485392832154832906 # Started 2026-05-26T20:10:04.916496+00:00 [2026-05-26T18:00:29.027000+00:00] .sirash (id=1508892597140062208) so I'm not sure how i got -0.02 on a free account. but it won't let me connect my Hermes anymore [attachment] image.png https://cdn.discordapp.com/attachments/1508892597140062208/1508892597345718525/image.png?ex=6a17313d&is=6a15dfbd&hm=9f78f2d2b4d17225bdab70f4a2113902edbc476c266716faddf429e9270b5a5a& [2026-05-26T23:37:11.803000+00:00] nat2r (id=1508977333724512256) <#1485307775444844625>

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508892597140062208-free-account-won-t-connect.txt`

### 1509183972335292628-Predict-the-future
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509183972335292628-Predict-the-future.txt`
- **Raw:** `[[raw/discord/1509183972335292628-predict-the-future-765caab820.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Predict the future!' in forum #plugins-skills-and-skins # thread_id=1509183972335292628 forum_id=1485392832154832906 # Started 2026-05-27T15:39:58.699582+00:00 [2026-05-27T13:18:18.287000+00:00] neopabo (id=1509183972335292628) I built a skill based on prediction research by Philip E. Tetlock - this allows your agent to make in-depth predictions on future outcomes based on current events, and turn it into an easy-to-read html document. [attachment] image.png https://cdn.discordapp.com/attachments/1509183972335292628/1509183972700323850/image.png?ex=6a18409a&is=6a16ef1a&hm=cb19c0efae3f8da3cab3c7dd625e26757398acfccfac279b39ecccd3f43d1141& [2026-05-27T13:58:42.502000+00:00]…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509183972335292628-Predict-the-future.txt`

### 1508746944280002672-Stop-polling--wake-agents-on-matching-events
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508746944280002672-Stop-polling--wake-agents-on-matching-events.txt`
- **Raw:** `[[raw/discord/1508746944280002672-stop-polling--wake-agents-on-matching-events-baf1ded09a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Stop polling, wake agents on matching events' in forum #plugins-skills-and-skins # thread_id=1508746944280002672 forum_id=1485392832154832906 # Started 2026-05-26T09:56:02.277568+00:00 [2026-05-26T08:21:42.679000+00:00] singhcoder (id=1508746944280002672) Background agents hit a pretty annoying tradeoff when they need to react to future events. If you poll often, they waste tokens checking if anything happened. And, if you poll slowly, they react late. Use a cheaper model for the polling loop and the actual event handling can get worse too. this comes up whenever an agent is waiting on things like: - an email/reply - a repo update - a customer message - a task state change - any…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508746944280002672-Stop-polling--wake-agents-on-matching-events.txt`

### 1509671843160920194-Multi-Memory-Backends
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1509671843160920194-Multi-Memory-Backends.txt`
- **Raw:** `[[raw/discord/1509671843160920194-multi-memory-backends-02f8be7d1d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Multi Memory Backends' in forum #plugins-skills-and-skins # thread_id=1509671843160920194 forum_id=1485392832154832906 # Started 2026-05-29T03:02:20.098634+00:00 [2026-05-28T21:36:55.756000+00:00] _123321_ (id=1509671843160920194) Allows installation of multiple memory backends. Useful if you want to compare on a single machine. https://github.com/someaka/multi-memory-plugin [attachment] 1780004150.png https://cdn.discordapp.com/attachments/1509671843160920194/1509671845446811658/1780004150.png?ex=6a1a06f8&is=6a18b578&hm=4342d87b85e610767e322d15769cf1fa47cd384e0920d2718e4a334054c3e554& [attachment] file_0000000064847230aa7343ed93bd22d0.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1509671843160920194-Multi-Memory-Backends.txt`

### 1508821477791764674-I-built-a-skill-that-makes-AI-agents-write-commits-like-a-senior-dev---secret-scanning--test-gat
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508821477791764674-I-built-a-skill-that-makes-AI-agents-write-commits-like-a-senior-dev---secret-scanning--test-gat.txt`
- **Raw:** `[[raw/discord/1508821477791764674-i-built-a-skill-that-makes-ai-agents-write-commits-like-a-senior-dev---secret-scanning--test-gat-b63aa35d74.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'I built a skill that makes AI agents write commits like a senior dev — secret scanning, test gat' in forum #plugins-skills-and-skins # thread_id=1508821477791764674 forum_id=1485392832154832906 # Started 2026-05-26T15:24:42.314165+00:00 [2026-05-26T13:17:52.853000+00:00] z4rl. (id=1508821477791764674) hey hermes contributors — you're shipping 600+ PRs and 800+ commits per release week. that's incredible. but i'd guess a chunk of those commits look like "fix stuff", "update", "wip" — especially when an AI agent is doing the heavy lifting. built a free skill that fixes that. every commit the agent makes gets structured automatically: CONTEXT : what existed before CHANGE : what was…

### 1507855733776060497-Carbon-Voice-plugin-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507855733776060497-Carbon-Voice-plugin-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1507855733776060497-carbon-voice-plugin-for-hermes-agent-af41ab355d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Carbon Voice plugin for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1507855733776060497 forum_id=1485392832154832906 # Started 2026-05-24T03:28:30.032606+00:00 [2026-05-23T21:20:21.537000+00:00] cristianmgm7 (id=1507855733776060497) Hi! Cristian from PhononX. We open-sourced a Hermes plugin for Carbon Voice, a voice-first messaging platform. The agent shows up as a bot user inside Carbon Voice channels. DMs always reach it, group channels require a mention. Includes thread context, forward-compatible mention detection, Socket.IO real-time delivery with REST polling fallback. CI green on Python 3.11 and 3.12, running in production internally. Repo and install…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507855733776060497-Carbon-Voice-plugin-for-Hermes-Agent.txt`

### 1508626861742362744-Hermes---Nous-branding-skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508626861742362744-Hermes---Nous-branding-skill.txt`
- **Raw:** `[[raw/discord/1508626861742362744-hermes---nous-branding-skill-8891c84495.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes - Nous branding skill' in forum #plugins-skills-and-skins # thread_id=1508626861742362744 forum_id=1485392832154832906 # Started 2026-05-26T02:59:25.660227+00:00 [2026-05-26T00:24:32.771000+00:00] anduril0202 (id=1508626861742362744) https://x.com/agentic_wooz/status/2059067427212685721 [embed] https://twitter.com/agentic_wooz/status/2059067427212685721

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508626861742362744-Hermes---Nous-branding-skill.txt`

### 1507877053775483081-N8N-Skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507877053775483081-N8N-Skill.txt`
- **Raw:** `[[raw/discord/1507877053775483081-n8n-skill-a7ceb4d9bb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'N8N Skill' in forum #plugins-skills-and-skins # thread_id=1507877053775483081 forum_id=1485392832154832906 # Started 2026-05-24T03:28:29.193512+00:00 [2026-05-23T22:45:04.621000+00:00] .omgg (id=1507877053775483081) https://github.com/spfcraze/Hermes-n8n-skills What This Skill Covers 1. Expression Syntax Double curly brace {{}} syntax Core variables: $json, $node, $now, $env, $input, $workflow, $execution Webhook data structure (the .body gotcha) Advanced patterns: conditionals, date manipulation, string/array operations When NOT to use expressions (Code nodes, webhook paths, credentials) 2. Code Nodes JavaScript: Mode selection, data access patterns, return format, built-in…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507877053775483081-N8N-Skill.txt`

### 1507878870995570778-Glitch--deep-fry-your-footage
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507878870995570778-Glitch--deep-fry-your-footage.txt`
- **Raw:** `[[raw/discord/1507878870995570778-glitch--deep-fry-your-footage-a94acbc862.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Glitch/ deep-fry your footage' in forum #plugins-skills-and-skins # thread_id=1507878870995570778 forum_id=1485392832154832906 # Started 2026-05-24T03:28:28.836786+00:00 [2026-05-23T22:52:17.880000+00:00] .salt555 (id=1507878870995570778) https://github.com/Salt-555/SaltySkills [embed] GitHub - Salt-555/SaltySkills: This is where I will publish fun ski... https://github.com/Salt-555/SaltySkills

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507878870995570778-Glitch--deep-fry-your-footage.txt`

### 1508488303668625628-Reflect-Theme
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508488303668625628-Reflect-Theme.txt`
- **Raw:** `[[raw/discord/1508488303668625628-reflect-theme-c6a9a055d4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Reflect Theme' in forum #plugins-skills-and-skins # thread_id=1508488303668625628 forum_id=1485392832154832906 # Started 2026-05-25T19:30:33.178323+00:00 [2026-05-25T15:13:57.952000+00:00] dalekc72 (id=1508488303668625628) I am not a fan of the UI in Hermes. These is my first attempt at building a theme I push to Github. https://github.com/daletkc/hermes-theme-reflect [attachment] sessions.png https://cdn.discordapp.com/attachments/1508488303668625628/1508488304058830868/sessions.png?ex=6a15b8b6&is=6a146736&hm=40e8fcd0347c28ce566d105ebd12fe68f436c3731d5353d24bcb208ce87e5a3c& [attachment] logs.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508488303668625628-Reflect-Theme.txt`

### 1508127784524976128-Hermes-x-Codex-s-gpt2image-skill--THEIA
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508127784524976128-Hermes-x-Codex-s-gpt2image-skill--THEIA.txt`
- **Raw:** `[[raw/discord/1508127784524976128-hermes-x-codex-s-gpt2image-skill--theia-e53016d92c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes x Codex's gpt2image skill: THEIA' in forum #plugins-skills-and-skins # thread_id=1508127784524976128 forum_id=1485392832154832906 # Started 2026-05-24T19:18:01.282290+00:00 [2026-05-24T15:21:23.490000+00:00] anduril0202 (id=1508127784524976128) https://x.com/Agentic_wooz/status/2058568440705622421 [embed] https://twitter.com/Agentic_wooz/status/2058568440705622421

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508127784524976128-Hermes-x-Codex-s-gpt2image-skill--THEIA.txt`

### 1507981208452333568-Is-anyone-using-a-linter-on-skill-checkin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507981208452333568-Is-anyone-using-a-linter-on-skill-checkin.txt`
- **Raw:** `[[raw/discord/1507981208452333568-is-anyone-using-a-linter-on-skill-checkin-5c78253a49.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Is anyone using a linter on skill-checkin?' in forum #plugins-skills-and-skins # thread_id=1507981208452333568 forum_id=1485392832154832906 # Started 2026-05-24T08:30:17.900251+00:00 [2026-05-24T05:38:57.031000+00:00] n7e_5l_labs (id=1507981208452333568) Otherwise I'm going to adapt: https://github.com/William-Yeh/agent-skill-linter [embed] GitHub - William-Yeh/agent-skill-linter: Lint agent skills for spec... https://github.com/William-Yeh/agent-skill-linter [2026-05-25T04:52:57.796000+00:00] n7e_5l_labs (id=1508332023247540388) Off I go - let's see where I can get to

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507981208452333568-Is-anyone-using-a-linter-on-skill-checkin.txt`

### 1507864140574752838-real-phone-number-subscription--not-VoIP
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507864140574752838-real-phone-number-subscription--not-VoIP.txt`
- **Raw:** `[[raw/discord/1507864140574752838-real-phone-number-subscription--not-voip-2c979ad5d0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'real phone number subscription, not VoIP' in forum #plugins-skills-and-skins # thread_id=1507864140574752838 forum_id=1485392832154832906 # Started 2026-05-24T03:28:29.640292+00:00 [2026-05-23T21:53:45.874000+00:00] jooshmayer (id=1507864140574752838) twilio can give you a VoIP number, but if you want to give your agent a real identity online that won’t really work VoIPs are pretty easily blocked and rejected for stuff like 2FA codes and phone verifications. https://op.inc/skills.md can let u get a real mobile number for free to use for anything on the web

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507864140574752838-real-phone-number-subscription--not-VoIP.txt`

### 1508516263398215721-MyChatArchive-memory-provider--cross-model-chat-archive-as-Hermes-memory
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508516263398215721-MyChatArchive-memory-provider--cross-model-chat-archive-as-Hermes-memory.txt`
- **Raw:** `[[raw/discord/1508516263398215721-mychatarchive-memory-provider--cross-model-chat-archive-as-hermes-memory-0b970fde6d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'MyChatArchive memory provider: cross-model chat archive as Hermes memory' in forum #plugins-skills-and-skins # thread_id=1508516263398215721 forum_id=1485392832154832906 # Started 2026-05-25T19:30:32.732124+00:00 [2026-05-25T17:05:04.071000+00:00] _chan8910 (id=1508516263398215721) Built a memory provider plugin that integrates MyChatArchive (open-source, AGPL, local-first) as a Hermes backend. The wedge: every other provider builds the archive itself. This one assumes you already have years of cross-model chat history (ChatGPT, Claude, Cursor, Grok) and exposes it as Hermes memory. Read-heavy by design. Tested end-to-end via the Telegram gateway. 49 passing tests. About to open a…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508516263398215721-MyChatArchive-memory-provider--cross-model-chat-archive-as-Hermes-memory.txt`

### 1508436075692163174-Syft-News-CLI---Fast---Precise-Global-News-Pipeline-for-Agents
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1508436075692163174-Syft-News-CLI---Fast---Precise-Global-News-Pipeline-for-Agents.txt`
- **Raw:** `[[raw/discord/1508436075692163174-syft-news-cli---fast---precise-global-news-pipeline-for-agents-43a3b53f39.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Syft News CLI - Fast & Precise Global News Pipeline for Agents' in forum #plugins-skills-and-skins # thread_id=1508436075692163174 forum_id=1485392832154832906 # Started 2026-05-25T14:53:18.693819+00:00 [2026-05-25T11:46:25.832000+00:00] jeff_h3049 (id=1508436075692163174) I’ve been working on a way to **feed Hermes agents with high-fidelity, topic-specific news inputs** without relying on broad runtime web search. Instead of asking agents to scrape the web (slow/expensive/flaky), I built a CLI + Skill set that acts as an "intelligence layer." It maintains a pre-recalled, topic-oriented pool and feeds Hermes structured artifacts via local JSON/Markdown. **What this adds to…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1508436075692163174-Syft-News-CLI---Fast---Precise-Global-News-Pipeline-for-Agents.txt`

### 1507458325279801474-Mr-Hermagi---Discord-TutorBot-with-HTML-and-Audio-output
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507458325279801474-Mr-Hermagi---Discord-TutorBot-with-HTML-and-Audio-output.txt`
- **Raw:** `[[raw/discord/1507458325279801474-mr-hermagi---discord-tutorbot-with-html-and-audio-output-6da98bbb2f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Mr Hermagi - Discord TutorBot with HTML and Audio output' in forum #plugins-skills-and-skins # thread_id=1507458325279801474 forum_id=1485392832154832906 # Started 2026-05-22T19:45:40.993402+00:00 [2026-05-22T19:01:11.968000+00:00] sahil_ss9 (id=1507458325279801474) 🧘 Just dropped MrHermagi-tutorbot — a Discord AI tutor that delivers daily lessons to a forum with HTML deep-dives and audio summaries. Pick any subject, define it in YAML, and it teaches you. Built on Hermes Agent. https://github.com/Sahil-SS9/MrHermagi-tutorbot MIT, free, do what you want with it. Hit the star and show some love if you like it. [embed] GitHub - Sahil-SS9/MrHermagi-tutorbot: A Discord AI tutor bot —…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507458325279801474-Mr-Hermagi---Discord-TutorBot-with-HTML-and-Audio-output.txt`

### 1506873245662576670-Scrolling-titlebar
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506873245662576670-Scrolling-titlebar.txt`
- **Raw:** `[[raw/discord/1506873245662576670-scrolling-titlebar-51c2b133e3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Scrolling titlebar' in forum #plugins-skills-and-skins # thread_id=1506873245662576670 forum_id=1485392832154832906 # Started 2026-05-21T09:40:26.767371+00:00 [2026-05-21T04:16:18.117000+00:00] jimn235 (id=1506873245662576670) titlebar sits for a minute then scrolls https://github.com/jnorthrup/hermes-scrolling-titlebar/tree/master [embed] GitHub - jnorthrup/hermes-scrolling-titlebar https://github.com/jnorthrup/hermes-scrolling-titlebar/tree/master

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506873245662576670-Scrolling-titlebar.txt`

### 1506725581381959790-Discord-and-Entertainment-Pack
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506725581381959790-Discord-and-Entertainment-Pack.txt`
- **Raw:** `[[raw/discord/1506725581381959790-discord-and-entertainment-pack-74e7b70a75.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Discord and Entertainment Pack' in forum #plugins-skills-and-skins # thread_id=1506725581381959790 forum_id=1485392832154832906 # Started 2026-05-20T20:15:12.274751+00:00 [2026-05-20T18:29:32.209000+00:00] meyjean (id=1506725581381959790) Interact with your Discord directly from the Hermes Dashboard. Works with your Hermes Bot Token. Hermes TV and Nous Boy: Embed your own channels, comes with 10 presets (Retro Weather, Stocks, Ambient Music, ect) and 4 Built in games including Pong and Flappy Bird. Art Gallery and Music Mixtape that works with Spotify. https://github.com/meyjeancodes/hermes-entertainment-pack.git [attachment] Screenshot_2026-05-18_at_8.23.26_PM.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506725581381959790-Discord-and-Entertainment-Pack.txt`

### 1506500336632729640-hermes-council
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506500336632729640-hermes-council.txt`
- **Raw:** `[[raw/discord/1506500336632729640-hermes-council-2dbc7c0d2b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'hermes-council' in forum #plugins-skills-and-skins # thread_id=1506500336632729640 forum_id=1485392832154832906 # Started 2026-05-20T09:31:39.105458+00:00 [2026-05-20T03:34:29.676000+00:00] magnus919 (id=1506500336632729640) Spawn a panel of custom-composed expert agents to debate any question. Agents are designed specifically for each topic — not generic archetypes — and engage in structured rounds of debate to surface genuine multi-perspective analysis. https://github.com/magnus919/hermes-council [attachment] openai_gpt-image-2-medium_20260519_233316_e6e88e88.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506500336632729640-hermes-council.txt`

### 1506503060556480632-I-turned-my-X-bookmarks-into-a-local-AI-brain-for-Hermes
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506503060556480632-I-turned-my-X-bookmarks-into-a-local-AI-brain-for-Hermes.txt`
- **Raw:** `[[raw/discord/1506503060556480632-i-turned-my-x-bookmarks-into-a-local-ai-brain-for-hermes-d58ebaa1d7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'I turned my X bookmarks into a local AI brain for Hermes' in forum #plugins-skills-and-skins # thread_id=1506503060556480632 forum_id=1485392832154832906 # Started 2026-05-20T09:31:38.704190+00:00 [2026-05-20T03:45:19.110000+00:00] iftakharr (id=1506503060556480632) You save great posts on X. Launch ideas. Growth tactics. AI agent examples. Product insights. Market signals. Then they disappear into the bookmark graveyard. So I built **Awaek** — a Hermes skill that turns your saved X bookmarks into local AI context. Not just bookmark search. The point is action: Hermes can use what you already saved to help you: - find market signals - generate content angles - write posts from…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506503060556480632-I-turned-my-X-bookmarks-into-a-local-AI-brain-for-Hermes.txt`

### 1507410689847988465-DOGA---Probabilistic-thinking-layer-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507410689847988465-DOGA---Probabilistic-thinking-layer-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1507410689847988465-doga---probabilistic-thinking-layer-for-hermes-agent-4adca54e4d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'DOGA - Probabilistic thinking layer for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1507410689847988465 forum_id=1485392832154832906 # Started 2026-05-22T19:45:41.511552+00:00 [2026-05-22T15:51:54.796000+00:00] 0zi57 (id=1507410689847988465) A small thinking layer plugin i put together for Hermes. Nothing too ambitious, just gets the job done. Small steps 🙂 • Detects user goals (Information / Understanding / Action) • Generates multiple scenarios before answering • Runs Monte Carlo simulation (10K-50K iterations, 0 LLM tokens) • Shows a [DOGA: Thinking Process] panel in responses Depth 1-5, /doga slash commands, simulate tool included. Plugin-based, no core…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507410689847988465-DOGA---Probabilistic-thinking-layer-for-Hermes-Agent.txt`

### 1506588621208031242-GIF-editing-skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506588621208031242-GIF-editing-skill.txt`
- **Raw:** `[[raw/discord/1506588621208031242-gif-editing-skill-3ad739cce8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'GIF editing skill' in forum #plugins-skills-and-skins # thread_id=1506588621208031242 forum_id=1485392832154832906 # Started 2026-05-20T09:31:38.337466+00:00 [2026-05-20T09:25:18.359000+00:00] neopabo (id=1506588621208031242) Reusable Hermes skills and scripts for editing GIFs, especially the hard case: pinning a transparent logo or sticker to a moving object so it stays snapped instead of floating. https://github.com/H-Ali13381/hermes-gif-overlay-skills [2026-05-20T09:26:13.336000+00:00] neopabo (id=1506588851798409217) Example result: [2026-05-20T09:26:17.692000+00:00] neopabo (id=1506588870068928573) [attachment] openclaw_coffin_dance_deadge_snapped_stabilized.gif…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506588621208031242-GIF-editing-skill.txt`

### 1506106554859130950-Overmind-Memory-MCP---Hermes-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506106554859130950-Overmind-Memory-MCP---Hermes-Plugin.txt`
- **Raw:** `[[raw/discord/1506106554859130950-overmind-memory-mcp---hermes-plugin-eb43a36151.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Overmind Memory MCP — Hermes Plugin' in forum #plugins-skills-and-skins # thread_id=1506106554859130950 forum_id=1485392832154832906 # Started 2026-05-19T03:02:02.553024+00:00 [2026-05-19T01:29:44.785000+00:00] demon6660699 (id=1506106554859130950) 🧠 Hermes Memory Plugin > "Your AI forgets everything. Hermes remembers." Hermes Agent stores memory in flat .md files — no search, no embeddings, no context. The Overmind plugin replaces that with a persistent semantic memory layer: > ✅ 4096D Vector Search — Qwen 8B embeddings via OpenRouter + PostgreSQL/pgvector > ✅ Per-agent isolation — Each agent gets its own private database > ✅ Automatic — Stores every exchange, prefetches relevant…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506106554859130950-Overmind-Memory-MCP---Hermes-Plugin.txt`

### 1507090932565278720-Hivemind--Turn-Hermes-Agent-Traces-into-Re-Usable-Skills
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1507090932565278720-Hivemind--Turn-Hermes-Agent-Traces-into-Re-Usable-Skills.txt`
- **Raw:** `[[raw/discord/1507090932565278720-hivemind--turn-hermes-agent-traces-into-re-usable-skills-4fd2edf79d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hivemind: Turn Hermes Agent Traces into Re-Usable Skills' in forum #plugins-skills-and-skins # thread_id=1507090932565278720 forum_id=1485392832154832906 # Started 2026-05-21T19:55:05.207920+00:00 [2026-05-21T18:41:18.719000+00:00] penguinfeet1 (id=1507090932565278720) Sharing something we've been working on for Hermes in case it's useful. Hivemind is a plugin for Hermes: a continual learning layer that turns agent traces into reusable skills, so agents get better with use instead of resetting. Still early. Curious what people here think, especially edge cases where this would or wouldn't help. deeplake.ai/hivemind [attachment] HIDBfkJaMAAbYB1.jpeg…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1507090932565278720-Hivemind--Turn-Hermes-Agent-Traces-into-Re-Usable-Skills.txt`

### 1505450396926083133-hermes-xai-oauth-wsl
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505450396926083133-hermes-xai-oauth-wsl.txt`
- **Raw:** `[[raw/discord/1505450396926083133-hermes-xai-oauth-wsl-21ff0bca6b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'hermes-xai-oauth-wsl' in forum #plugins-skills-and-skins # thread_id=1505450396926083133 forum_id=1485392832154832906 # Started 2026-05-17T08:22:38.992442+00:00 [2026-05-17T06:02:24.543000+00:00] spac_wby_actual (id=1505450396926083133) Just shipped a fix for the WSL2 OAuth callback issue a lot of folks have been hitting on hermes auth add xai-oauth. The "Could not establish connection" page is from xAI's authorize server when the Windows browser → WSL loopback redirect gets dropped by the default Hyper-V Firewall block on the WSL VM. Repo has a no-admin wrapper script (scripts/hermes-xai-oauth-wsl.sh) and a one-time admin PowerShell rule (docs/permanent-fix.ps1). MIT, PRs welcome…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505450396926083133-hermes-xai-oauth-wsl.txt`

### 1505408038545395823-TERMUX-SKILLS-TO-MAKE-YOUR-AI-AGENT-UNDERSTAND-THE-TERMUX-ENVIRNOMENT
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505408038545395823-TERMUX-SKILLS-TO-MAKE-YOUR-AI-AGENT-UNDERSTAND-THE-TERMUX-ENVIRNOMENT.txt`
- **Raw:** `[[raw/discord/1505408038545395823-termux-skills-to-make-your-ai-agent-understand-the-termux-envirnoment-e64567e78b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'TERMUX SKILLS TO MAKE YOUR AI AGENT UNDERSTAND THE TERMUX ENVIRNOMENT' in forum #plugins-skills-and-skins # thread_id=1505408038545395823 forum_id=1485392832154832906 # Started 2026-05-17T08:22:39.487079+00:00 [2026-05-17T03:14:05.518000+00:00] txrao (id=1505408038545395823) I went through trial and error using termux and make it understand how to understand proot-distro and fhe termux library. You will need these tools and gpu oassthrough for majority for the open-source projects for hermes. I just felt like maybe there are other termux users trying to use termux to understand it and also being a cheaper option and local(i use ollama host). Github…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505408038545395823-TERMUX-SKILLS-TO-MAKE-YOUR-AI-AGENT-UNDERSTAND-THE-TERMUX-ENVIRNOMENT.txt`

### 1506355081073918012-TokenTelemetry-plugin-for-Hermes-Dashboard
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506355081073918012-TokenTelemetry-plugin-for-Hermes-Dashboard.txt`
- **Raw:** `[[raw/discord/1506355081073918012-tokentelemetry-plugin-for-hermes-dashboard-4377017890.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'TokenTelemetry plugin for Hermes Dashboard' in forum #plugins-skills-and-skins # thread_id=1506355081073918012 forum_id=1485392832154832906 # Started 2026-05-19T19:52:59.428467+00:00 [2026-05-19T17:57:18.052000+00:00] pulpyhunter (id=1506355081073918012) hey folks, finally shipped a TokenTelemetry plugin for Hermes Dashboard, came out of ddiall's ask in NousResearch/hermes-agent#26696 (https://github.com/NousResearch/hermes-agent/issues/26696). it adds a TokenTelemetry tab inside Hermes Dashboard so you don't have to juggle a second port for cost and trace observability. what it does: six deep link cards inside the tab open the relevant TokenTelemetry page (Hermes Overview,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506355081073918012-TokenTelemetry-plugin-for-Hermes-Dashboard.txt`

### 1506791627031576777-Hermes---MultiChannel---In-App-Prompt-Optimizer
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1506791627031576777-Hermes---MultiChannel---In-App-Prompt-Optimizer.txt`
- **Raw:** `[[raw/discord/1506791627031576777-hermes---multichannel---in-app-prompt-optimizer-b06ff74f12.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes - MultiChannel - In App Prompt Optimizer' in forum #plugins-skills-and-skins # thread_id=1506791627031576777 forum_id=1485392832154832906 # Started 2026-05-21T03:32:44.869157+00:00 [2026-05-20T22:51:58.719000+00:00] sahil_ss9 (id=1506791627031576777) Hey team! Just shipped something I've been cooking for weeks and I think a lot of you will love it. hermes-multichannel-prompt-optimizer → https://github.com/Sahil-SS9/hermes-multichannel-prompt-optimizer Sits invisibly in front of your agent and rewrites every prompt you send into something tailored to whatever model's listening. You keep typing how your brain wants ("hey could you maybe explain..."), the model receives…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1506791627031576777-Hermes---MultiChannel---In-App-Prompt-Optimizer.txt`

### 1505570458680954900-Hermes-Persona--A-hermes-agent-personality-plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505570458680954900-Hermes-Persona--A-hermes-agent-personality-plugin.txt`
- **Raw:** `[[raw/discord/1505570458680954900-hermes-persona--a-hermes-agent-personality-plugin-249bfcd85d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Persona: A hermes agent personality plugin' in forum #plugins-skills-and-skins # thread_id=1505570458680954900 forum_id=1485392832154832906 # Started 2026-05-17T19:09:05.824266+00:00 [2026-05-17T13:59:29.496000+00:00] kai.xu (id=1505570458680954900) I built a super light weight Hermes Agent plugin that gives your agent a persistent character identity. It survives sessions, restarts, and context resets. It's a five-layer personality stack: SOUL.md — core identity (who your character is) /personality — how they think, feel, and speak Prefill — few-shot behavioral anchor (survives context drift) persona-config.json — dynamic rules, time-slots, relationship dimensions Memory —…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505570458680954900-Hermes-Persona--A-hermes-agent-personality-plugin.txt`

### 1505227195008815196-Bootstrap-Light---Dark-Themes-for-the-Hermes-Web-Dashboard
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505227195008815196-Bootstrap-Light---Dark-Themes-for-the-Hermes-Web-Dashboard.txt`
- **Raw:** `[[raw/discord/1505227195008815196-bootstrap-light---dark-themes-for-the-hermes-web-dashboard-cd51096491.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Bootstrap Light & Dark Themes for the Hermes Web Dashboard' in forum #plugins-skills-and-skins # thread_id=1505227195008815196 forum_id=1485392832154832906 # Started 2026-05-16T19:04:53.332619+00:00 [2026-05-16T15:15:29.059000+00:00] vinny_public (id=1505227195008815196) Hey everyone! I’m sharing a small Hermes dashboard theme repo for community consideration: https://github.com/vince-winkintel/hermes-dashboard-bootstrap-themes This repo provides two portable Bootstrap v5-inspired themes for the Hermes web dashboard: - Bootstrap v5 Light — clean, readable light theme inspired by Bootswatch Spacelab. - Bootstrap v5 Dark — darker Slate-style theme inspired by Bootswatch Slate. The…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505227195008815196-Bootstrap-Light---Dark-Themes-for-the-Hermes-Web-Dashboard.txt`

### 1504716182433959946-Configurable-email-inbox-triage--classify--extract--summarize--and-route-Gmail-messages
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504716182433959946-Configurable-email-inbox-triage--classify--extract--summarize--and-route-Gmail-messages.txt`
- **Raw:** `[[raw/discord/1504716182433959946-configurable-email-inbox-triage--classify--extract--summarize--and-route-gmail-messages-3e8b118988.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Configurable email inbox triage: classify, extract, summarize, and route Gmail messages' in forum #plugins-skills-and-skins # thread_id=1504716182433959946 forum_id=1485392832154832906 # Started 2026-05-15T08:50:00.539823+00:00 [2026-05-15T05:24:54.167000+00:00] thedavidmurray (id=1504716182433959946) https://github.com/thedavidmurray/hermes-skill-email-intake [embed] GitHub - thedavidmurray/hermes-skill-email-intake: Configurable ema... https://github.com/thedavidmurray/hermes-skill-email-intake

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504716182433959946-Configurable-email-inbox-triage--classify--extract--summarize--and-route-Gmail-messages.txt`

### 1505329631476191373-GitRadar---the-discovery-pipeline-that-keeps-my-Hermes-setup-evolving
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505329631476191373-GitRadar---the-discovery-pipeline-that-keeps-my-Hermes-setup-evolving.txt`
- **Raw:** `[[raw/discord/1505329631476191373-gitradar---the-discovery-pipeline-that-keeps-my-hermes-setup-evolving-d266ab5e41.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'GitRadar — the discovery pipeline that keeps my Hermes setup evolving' in forum #plugins-skills-and-skins # thread_id=1505329631476191373 forum_id=1485392832154832906 # Started 2026-05-17T02:55:40.169935+00:00 [2026-05-16T22:02:31.816000+00:00] sahil_ss9 (id=1505329631476191373) Hey Gang I've put together a little open‑source tool called GitRadar that I've been using to keep my Hermes Agent setup sharp. What it does: - Scans GitHub for new/trending repos (by topic, language, or recency) - Filters out noise (tutorial repos, awesome‑lists, dead projects, etc.) - Scores each repo on relevance (stars, recency, language/framework fit, licence, topic bonus) - Labels them as ADOPT,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505329631476191373-GitRadar---the-discovery-pipeline-that-keeps-my-Hermes-setup-evolving.txt`

### 1504728592754413619-Livekit-plugin-for-voice-and-data-connection-over-webrtc.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504728592754413619-Livekit-plugin-for-voice-and-data-connection-over-webrtc..txt`
- **Raw:** `[[raw/discord/1504728592754413619-livekit-plugin-for-voice-and-data-connection-over-webrtc.-a75a828013.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Livekit plugin for voice and data connection over webrtc.' in forum #plugins-skills-and-skins # thread_id=1504728592754413619 forum_id=1485392832154832906 # Started 2026-05-15T08:50:00.103988+00:00 [2026-05-15T06:14:13.018000+00:00] franci.penov (id=1504728592754413619) A Livekit gateway plugin that let's you have a real-time voice conversation with your agent using any webrtc client. Supports both local Livekit install and Livekit Cloud. https://github.com/kortexa-ai/hermes-livekit [embed] GitHub - kortexa-ai/hermes-livekit: LiveKit WebRTC voice gateway pl... https://github.com/kortexa-ai/hermes-livekit

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504728592754413619-Livekit-plugin-for-voice-and-data-connection-over-webrtc..txt`

### 1505038751934709760-Vintage-Mac--OS-7--8--9--to-Hermes-Bridge
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505038751934709760-Vintage-Mac--OS-7--8--9--to-Hermes-Bridge.txt`
- **Raw:** `[[raw/discord/1505038751934709760-vintage-mac--os-7--8--9--to-hermes-bridge-faf5abd807.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Vintage Mac (OS 7, 8, 9) to Hermes Bridge' in forum #plugins-skills-and-skins # thread_id=1505038751934709760 forum_id=1485392832154832906 # Started 2026-05-16T02:47:24.735117+00:00 [2026-05-16T02:46:40.729000+00:00] kalkyl (id=1505038751934709760) I had a ton of fun figuring out how to connect my OS9 iMac to my Hermes instance! Please give the github a star: https://github.com/chorned/Hermes-macinAI/ This requires MacinAI: https://oldapplestuff.com/MacinAI/ [attachment] img.png https://cdn.discordapp.com/attachments/1505038751934709760/1505038752118997043/img.png?ex=6a092c10&is=6a07da90&hm=fd4c8d7209fc454f4f2fd9c5bcf0c34428744c51b1c82f6b6efb8b91afe1edc1& [embed] GitHub -…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505038751934709760-Vintage-Mac--OS-7--8--9--to-Hermes-Bridge.txt`

### 1504989771695394946-GitHub-starred-repos-auto-skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504989771695394946-GitHub-starred-repos-auto-skill.txt`
- **Raw:** `[[raw/discord/1504989771695394946-github-starred-repos-auto-skill-b533477803.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'GitHub starred repos auto-skill' in forum #plugins-skills-and-skins # thread_id=1504989771695394946 forum_id=1485392832154832906 # Started 2026-05-16T02:47:25.160698+00:00 [2026-05-15T23:32:02.930000+00:00] okin_17 (id=1504989771695394946) Hey everyone, I wanted to share a pretty cool Hermes Agent skill repo I came up with & have been using for quite some time, a few months now: https://github.com/BigBossRabbit/starlearner-nexus-hermes-skill What this does is basically automate the creation of Hermes skills from GitHub starred repositories. It's got a few scripts that work together: One fetches your starred repos from GitHub Another categorizes them by topic (like AI/ML, dev…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504989771695394946-GitHub-starred-repos-auto-skill.txt`

### 1504628093187391671-Omatchy---a-plugin-that-matches-Hermes-dashboard-to-your-Omarchy-desktop-theme
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504628093187391671-Omatchy---a-plugin-that-matches-Hermes-dashboard-to-your-Omarchy-desktop-theme.txt`
- **Raw:** `[[raw/discord/1504628093187391671-omatchy---a-plugin-that-matches-hermes-dashboard-to-your-omarchy-desktop-theme-a8f809af1c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Omatchy - a plugin that matches Hermes dashboard to your Omarchy desktop theme' in forum #plugins-skills-and-skins # thread_id=1504628093187391671 forum_id=1485392832154832906 # Started 2026-05-15T02:57:59.841787+00:00 [2026-05-14T23:34:52.054000+00:00] _8bit64k_ (id=1504628093187391671) Video shows my Omarchy theme collection and my hermes desktop auto matching it as it cycles through 40 themes. To install just use the dashboard plugin installer w/ repo: 8bit64k/omatchy or https://github.com/8bit64k/omatchy Enjoy [attachment] dual-plugin-demo-720p.mp4…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504628093187391671-Omatchy---a-plugin-that-matches-Hermes-dashboard-to-your-Omarchy-desktop-theme.txt`

### 1505296585746026627-Creative-Pattern-Bank---Extended-Fronend-skill-with-access-to-multiple-frontend-elements
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505296585746026627-Creative-Pattern-Bank---Extended-Fronend-skill-with-access-to-multiple-frontend-elements.txt`
- **Raw:** `[[raw/discord/1505296585746026627-creative-pattern-bank---extended-fronend-skill-with-access-to-multiple-frontend-elements-e09b0bc0cc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Creative Pattern Bank - Extended Fronend skill with access to multiple frontend elements' in forum #plugins-skills-and-skins # thread_id=1505296585746026627 forum_id=1485392832154832906 # Started 2026-05-17T02:55:40.535251+00:00 [2026-05-16T19:51:13.100000+00:00] asacorp (id=1505296585746026627) I’ve been building a Hermes skill for frontend/creative-coding inspiration: https://github.com/Korkyzer/koruki-hermes-skills Skill: `creative-pattern-bank` It builds a local searchable index across sources like FreeFrontend, CodeMyUI, DevSnap, Codrops/Tympanus, GSAPify, Uiverse seeds, and direct CodePen/GitHub links. The main idea: don’t just keyword-search titles/descriptions. A lot of…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505296585746026627-Creative-Pattern-Bank---Extended-Fronend-skill-with-access-to-multiple-frontend-elements.txt`

### 1505084351191191614-Sharing-my-MS-DOS-6.22-Skin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1505084351191191614-Sharing-my-MS-DOS-6.22-Skin.txt`
- **Raw:** `[[raw/discord/1505084351191191614-sharing-my-ms-dos-6.22-skin-c5a1a471be.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Sharing my MS-DOS 6.22 Skin' in forum #plugins-skills-and-skins # thread_id=1505084351191191614 forum_id=1485392832154832906 # Started 2026-05-16T08:04:28.009712+00:00 [2026-05-16T05:47:52.439000+00:00] ghostm55 (id=1505084351191191614) Customized this cool theme myself for Hermes, supports both CLI and TUI mode, enjoy https://github.com/ghosTM55/hermes-ghost-theme [attachment] preview.png https://cdn.discordapp.com/attachments/1505084351191191614/1505084351807885312/preview.png?ex=6a095688&is=6a080508&hm=64e31a4c6e2a1e3c3970e2aeec3e5aa5b79eea691214ad786350330b264bbd7a& [embed] GitHub - ghosTM55/hermes-ghost-theme: My Personal Hermes Agent Theme…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1505084351191191614-Sharing-my-MS-DOS-6.22-Skin.txt`

### 1504553695675813958-Better-Skill-Building-Skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504553695675813958-Better-Skill-Building-Skill.txt`
- **Raw:** `[[raw/discord/1504553695675813958-better-skill-building-skill-92495336fe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Better Skill Building Skill' in forum #plugins-skills-and-skins # thread_id=1504553695675813958 forum_id=1485392832154832906 # Started 2026-05-14T19:47:02.514278+00:00 [2026-05-14T18:39:14.305000+00:00] neopabo (id=1504553695675813958) The default skill-creator skill packaged with claude-code provides very low-quality guidance for skill creation, and leads to verbose skills with bad logic. Other skill-building skills also have similar problems, and are poorly thought-out. To solve this issue, I created a logical framework as a skill, which replaces/complements these skills by providing logical framing for how to best structure skills for consistent quality and reliability. This…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504553695675813958-Better-Skill-Building-Skill.txt`

### 1503292684570333206-EXPERIMENTAL--Kiro-Gateway-Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503292684570333206-EXPERIMENTAL--Kiro-Gateway-Plugin.txt`
- **Raw:** `[[raw/discord/1503292684570333206-experimental--kiro-gateway-plugin-4638bdf2c2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '[EXPERIMENTAL] Kiro Gateway Plugin' in forum #plugins-skills-and-skins # thread_id=1503292684570333206 forum_id=1485392832154832906 # Started 2026-05-11T19:47:50.717652+00:00 [2026-05-11T15:23:55.883000+00:00] 74800 (id=1503417381454745681) [EXPERIMENTAL] Kiro Gateway Plugin [2026-05-11T16:09:41.776000+00:00] irma1925 (id=1503428898564735138) What's wrong? [2026-05-11T16:27:16.685000+00:00] 74800 (id=1503433323173642241) Adding support for thinking, allowing enterprise, adding workarounds longer token lifetime (kiro only issues for 5 hours max) [reply to irma1925 msg=1503428898564735138] [2026-05-11T16:27:27.153000+00:00] 74800 (id=1503433367079878686) And just patching bugs and…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503292684570333206-EXPERIMENTAL--Kiro-Gateway-Plugin.txt`

### 1503114142117265448-Hermes-Audit-Plugin---Grafana-Dashboards
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503114142117265448-Hermes-Audit-Plugin---Grafana-Dashboards.txt`
- **Raw:** `[[raw/discord/1503114142117265448-hermes-audit-plugin---grafana-dashboards-7f749af3ad.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Audit Plugin & Grafana Dashboards' in forum #plugins-skills-and-skins # thread_id=1503114142117265448 forum_id=1485392832154832906 # Started 2026-05-10T19:51:55.919065+00:00 [2026-05-10T19:18:57.991000+00:00] bert_71849 (id=1503114142117265448) I created a small Hermes plugin that records every tool call and every LLM API call into a local SQLite database (one DB per profile), with five ready-to-go Grafana dashboards bundled: - Tool Calls — success rate, errors, latency percentiles, slowest calls - API Calls — tokens, durations, finish reasons per call - Sessions — activity rollup per session_id - Models — per-provider / per-model usage and token totals - Skills —…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503114142117265448-Hermes-Audit-Plugin---Grafana-Dashboards.txt`

### 1503371941938200828-Reversal-the--data-normalization-layer
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503371941938200828-Reversal-the--data-normalization-layer.txt`
- **Raw:** `[[raw/discord/1503371941938200828-reversal-the--data-normalization-layer-10cb365693.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Reversal the data normalization layer' in forum #plugins-skills-and-skins # thread_id=1503371941938200828 forum_id=1485392832154832906 # Started 2026-05-11T14:49:11.106588+00:00 [2026-05-11T12:23:22.258000+00:00] inkxus (id=1503371941938200828) Hey 👋 Just opened a PR adding a Reversal integration example to hermes-example-plugins. Reversal is a data normalization layer — it converts raw sources (URLs, PDFs, Excel, images) into clean structured JSON before passing input to Hermes. Eliminates hallucinations from bad data, parsing errors on complex PDFs, and context overflow on large docs. PR: https://github.com/NousResearch/hermes-example-plugins/pull/2 Would love feedback from the…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503371941938200828-Reversal-the--data-normalization-layer.txt`

### 1504355044235939900-hermes-cashew--A-Hermes-Agent-memory-provider-plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504355044235939900-hermes-cashew--A-Hermes-Agent-memory-provider-plugin.txt`
- **Raw:** `[[raw/discord/1504355044235939900-hermes-cashew--a-hermes-agent-memory-provider-plugin-0a3ac21bd4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'hermes-cashew: A Hermes Agent memory provider plugin' in forum #plugins-skills-and-skins # thread_id=1504355044235939900 forum_id=1485392832154832906 # Started 2026-05-14T08:38:21.011580+00:00 [2026-05-14T05:29:52.111000+00:00] magnus919 (id=1504355044235939900) A Hermes Agent memory provider plugin that stores conversation context in a local Cashew thought graph with semantic search and automatic context recall. Get from zero to a working install in under five minutes. https://github.com/magnus919/hermes-cashew [embed] GitHub - magnus919/hermes-cashew: Memory provider for Hermes Agent ... https://github.com/magnus919/hermes-cashew [2026-05-14T06:03:51.426000+00:00] magnus919…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504355044235939900-hermes-cashew--A-Hermes-Agent-memory-provider-plugin.txt`

### 1503159383293563083-Custom-Hermes-Skins
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503159383293563083-Custom-Hermes-Skins.txt`
- **Raw:** `[[raw/discord/1503159383293563083-custom-hermes-skins-3a6b4511c4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Custom Hermes Skins' in forum #plugins-skills-and-skins # thread_id=1503159383293563083 forum_id=1485392832154832906 # Started 2026-05-11T02:58:04.690020+00:00 [2026-05-10T22:18:44.328000+00:00] sahil_ss9 (id=1503159383293563083) Following a few DMs about my current Kensei skin, I decided to take hour out to put them get her some other skins. Plus a handful of others. Enjoy 😊 [attachment] future-monkey.png https://cdn.discordapp.com/attachments/1503159383293563083/1503159383788355654/future-monkey.png?ex=6a0255c4&is=6a010444&hm=26f9f7ae4940729097522af8a6554048ad6615ba14b8a7ff09dc1ff77c81d85f& [attachment] free-palestine.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503159383293563083-Custom-Hermes-Skins.txt`

### 1503292684570333206-Kiro-Gateway--Plugin
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503292684570333206-Kiro-Gateway--Plugin.txt`
- **Raw:** `[[raw/discord/1503292684570333206-kiro-gateway--plugin-2371650328.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Kiro Gateway (Plugin)' in forum #plugins-skills-and-skins # thread_id=1503292684570333206 forum_id=1485392832154832906 # Started 2026-05-11T09:39:19.448899+00:00 [2026-05-11T07:08:25.829000+00:00] 74800 (id=1503292684570333206) **Bring your Kiro Pro models in your Hermes model picker natively, including Opus and Sonnet. ** Requires a Kiro Plan with Google or GitHub login. -# As of right now, I haven't gotten Builder ID / Enterprise sessions to work properly. Made this plugin since, as of writing, they are offering a 1-month trial for their Pro subscription, including pretty solid limits for Claude models. **## install Inside your Hermes environment, run:** **Then, install…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503292684570333206-Kiro-Gateway--Plugin.txt`

### 1503091259760316436-Claude-Hermes-MCP
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503091259760316436-Claude-Hermes-MCP.txt`
- **Raw:** `[[raw/discord/1503091259760316436-claude-hermes-mcp-c7fdf13850.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Claude Hermes MCP' in forum #plugins-skills-and-skins # thread_id=1503091259760316436 forum_id=1485392832154832906 # Started 2026-05-10T19:51:56.721022+00:00 [2026-05-10T17:48:02.412000+00:00] monty_13277 (id=1503091259760316436) Claude (Opus 4.7) handles my day-to-day chats: research, planning, working through problems. Hermes runs 24/7 on a mini PC and handles the real-world stuff: email, web browsing, form filling, calendar updates, cron jobs. I started out running Hermes on Opus 4.7 too, but it got expensive fast. Swapped in Kimi K2.6 via OpenRouter and it's been plenty for agent work. The catch: I still wanted Opus 4.7's reasoning for normal conversations. So I wired Claude…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503091259760316436-Claude-Hermes-MCP.txt`

### 1503826568521453711-Tokenwatch--Prevent-runaway-API-bills-at-the-harness-level.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503826568521453711-Tokenwatch--Prevent-runaway-API-bills-at-the-harness-level..txt`
- **Raw:** `[[raw/discord/1503826568521453711-tokenwatch--prevent-runaway-api-bills-at-the-harness-level.-83beca0605.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Tokenwatch: Prevent runaway API bills at the harness level.' in forum #plugins-skills-and-skins # thread_id=1503826568521453711 forum_id=1485392832154832906 # Started 2026-05-12T19:51:06.031024+00:00 [2026-05-12T18:29:53.682000+00:00] bowtiedbernard (id=1503826568521453711) I may or may not have woken up to a surprise API bill as I was on a hermes version with kanban but before failure tracking was native, so my agent ran up a huge amount of cached and input tokens. This plugin is designed to let you set custom limits and display warnings in your home channel or custom channel. It's a little brittle for my liking as it relies on the same path as /stop command, but hopefully that…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503826568521453711-Tokenwatch--Prevent-runaway-API-bills-at-the-harness-level..txt`

### 1503091259760316436-Claude-Codex-Cursor----Hermes-MCP
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503091259760316436-Claude-Codex-Cursor----Hermes-MCP.txt`
- **Raw:** `[[raw/discord/1503091259760316436-claude-codex-cursor----hermes-mcp-bb41150d92.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Claude/Codex/Cursor => Hermes MCP' in forum #plugins-skills-and-skins # thread_id=1503091259760316436 forum_id=1485392832154832906 # Started 2026-05-18T03:33:35.057985+00:00 [2026-05-17T19:12:07.136000+00:00] samuel.gudi (id=1505649133925437490) I'd love to help! 😄 Something specific you'd need contribution about? [reply to monty_13277 msg=1505583377133338827] [2026-05-17T21:20:22.318000+00:00] monty_13277 (id=1505681409858076672) <@234139936738115584> it has now been updated to work with both codex and cursor and any other llm client. It's llm agnostic now https://github.com/mlennie/hermes-mcp [embed] GitHub - mlennie/hermes-mcp: MCP server that lets any llm (i.e. Cla...…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503091259760316436-Claude-Codex-Cursor----Hermes-MCP.txt`

### 1504078435365163048-Custom-skin--hide-Available-Tools---Skills-in-startup-banner-hero
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1504078435365163048-Custom-skin--hide-Available-Tools---Skills-in-startup-banner-hero.txt`
- **Raw:** `[[raw/discord/1504078435365163048-custom-skin--hide-available-tools---skills-in-startup-banner-hero-b662d10910.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Custom skin: hide Available Tools / Skills in startup banner/hero?' in forum #plugins-skills-and-skins # thread_id=1504078435365163048 forum_id=1485392832154832906 # Started 2026-05-13T14:32:09.144025+00:00 [2026-05-13T11:10:43.417000+00:00] furkannaxoziwus (id=1504078435365163048) Hello, I’m working on a custom skin/theme for Hermes Agent. I’ve been able to customize fields like banner_logo, banner_hero, colors, spinner, welcome, response_label, and prompt_symbol through: ~/.hermes/skins/dragon.yaml The theme works overall. However, I’d like to clarify whether some parts of the startup screen can be controlled through the skin YAML or config: 1. The title at the top of the frame:…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1504078435365163048-Custom-skin--hide-Available-Tools---Skills-in-startup-banner-hero.txt`

### 1502955423244877884-Will-skills-plugins-like-scrapling-not-work-in-a-docker
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1502955423244877884-Will-skills-plugins-like-scrapling-not-work-in-a-docker.txt`
- **Raw:** `[[raw/discord/1502955423244877884-will-skills-plugins-like-scrapling-not-work-in-a-docker-874cc78218.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Will skills-capabilities/plugins like scrapling not work in a docker?' in forum #plugins-skills-and-skins # thread_id=1502955423244877884 forum_id=1485392832154832906 # Started 2026-05-10T19:51:57.141648+00:00 [2026-05-10T08:48:16.463000+00:00] hydraxiann (id=1502955423244877884) As hermes apparently stated it uses debian trixie, which ships python 3.13 with no pip, so it can't pip install dependencies for that plugin apparently. [2026-05-13T17:24:46.969000+00:00] bert_71849 (id=1504172570445091037) You can use `uv pip install`

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1502955423244877884-Will-skills-plugins-like-scrapling-not-work-in-a-docker.txt`

### 1501311220404326471-Custom-Fonts-and-Colors-for-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1501311220404326471-Custom-Fonts-and-Colors-for-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1501311220404326471-custom-fonts-and-colors-for-hermes-agent-9f71607ee2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Custom Fonts and Colors for Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1501311220404326471 forum_id=1485392832154832906 # Started 2026-05-10T19:52:04.110998+00:00 [2026-05-05T19:54:47.958000+00:00] rubengarciajr (id=1501311220404326471) Hello friends, I'm visually impaired and the fonts on hermes dashboard are too small for me to see correctly. So i created this plugin to help anyone struggling with the same issue. https://github.com/rubengarciajr/hermes-fonts-colors [attachment] fontscolors.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1501311220404326471-Custom-Fonts-and-Colors-for-Hermes-Agent.txt`

### 1501778590906449981-Image-and-Vídeo-Generation-with-Hermes-Agent
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1501778590906449981-Image-and-Vídeo-Generation-with-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1501778590906449981-image-and-v-deo-generation-with-hermes-agent-05be4f7f5b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Image and Vídeo Generation with Hermes Agent' in forum #plugins-skills-and-skins # thread_id=1501778590906449981 forum_id=1485392832154832906 # Started 2026-05-10T19:52:01.124494+00:00 [2026-05-07T02:51:57.769000+00:00] w.s94 (id=1501778590906449981) Sorry for all * There’s nothing cheaper * I’ve created the world’s best image and video skills generation and the best LLMs integration, there are no better models than these Compatible with Hermes Agent https://github.com/wesleysimplicio/PiAPI-Skills [embed] GitHub - wesleysimplicio/PiAPI-Skills: Skill bundle for Claude, Cod... https://github.com/wesleysimplicio/PiAPI-Skills [2026-05-07T04:43:35.039000+00:00] crxshworld…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1501778590906449981-Image-and-Vídeo-Generation-with-Hermes-Agent.txt`
