---
title: Senter Wiki
created: 2026-07-07
updated: 2026-09-17
type: wiki
links:
  github: https://github.com/SouthpawIN/Senter
  vault: ~/Documents/Projects/Projects
sources:
  - senter-wiki.md
  - wiki-topics/
  - skills-capabilities/
  - bots-profiles/
  - triggers-loops/
  - inspiration-integrations/
---

# Senter Wiki

> Cursor for markdown. A live-acting second brain.

The Senter Wiki is the **master orchestration layer** for everything Chris cares about. It's a structured knowledge base that coordinates the entire Hermes fleet — turning haphazard conversations into organized, actionable work across dozens of topics simultaneously.

---

## Inspiration & Integrations

Everything that feeds data into the wiki — GitHub repos, HuggingFace models, raw inbox cuts from Hermes sessions, cron outputs, webhooks, kanban state, clipboard captures. This is the *sensory layer*: without integrations, the wiki has no input.

| Integration | Source | What |
|-------------|--------|------|
| GitHub | github.com/SouthpawIN/Senter | Code, issues, PRs |
| HuggingFace | huggingface.co/SouthpawIN | Model repos |
| Hermes state.db | ~/.hermes/state.db | Chat messages cut into per-topic inbox |
| Sessions | .system/sessions/ | Full conversation transcripts |
| Fleet Daemons | launchd services | watcher, topic-agent, umbrella, bridge, scanwatch |

### Inspiration Bin
- *Empty — start capturing!*

---

## Wiki & Topics

Every subject Chris cares about gets its own topic with evidence, decisions, and action items. Topics are organized via progressive disclosure — scan the table of contents, click to dive deep, drill into specifics.

| Topic | What |
|-------|------|
| [Turbofit](wiki-topics/turbofit/index.md) | Model research, pipelines, hardware tiers — evidence-backed local inference runtime |
| [Music](wiki-topics/music/index.md) | Music generation and AI composition |
| [Dispatched M2S](wiki-topics/dispatched-m2s/index.md) | Dispatch pipeline for multi-agent workflows |
| [Burner Phone](wiki-topics/burner-phone/index.md) | Mobile device management |
| [Case MacBook](wiki-topics/case-macbook/index.md) | MacBook accessories and cases |
| [Nous Community](wiki-topics/nous-community/index.md) | Nous Research community engagement |
| [Back Where](wiki-topics/back-where/index.md) | Context and memory management |
| [Both Smarter](wiki-topics/both-smarter/index.md) | Dual intelligence systems |
| [Beyond Pissed](wiki-topics/beyond-pissed/index.md) | Advanced troubleshooting |
| [Central Asked](wiki-topics/central-asked/index.md) | Central query hub |
| [Click Options](wiki-topics/click-options/index.md) | Click handling patterns |
| [Crow](wiki-topics/crow/index.md) | Crow project |
| [Dev Tooling](wiki-topics/dev-tooling/index.md) | Development tools |
| [Evolutionary](wiki-topics/evolutionary/index.md) | Evolutionary algorithms |
| [Faster Without](wiki-topics/faster-without/index.md) | Performance optimization |
| [Life Links](wiki-topics/life-links/index.md) | Personal knowledge management |
| [Object Important](wiki-topics/object-important/index.md) | Object importance tracking |
| [Only Device](wiki-topics/only-device/index.md) | Device-specific config |
| [Pocket Shop](wiki-topics/pocket-shop/index.md) | Pocket shop app |
| [Process Important](wiki-topics/process-important/index.md) | Process importance tracking |
| [Restore Hdiutil](wiki-topics/restore-hdiutil/index.md) | macOS disk utility |
| [Self File](wiki-topics/self-file/index.md) | Self-file management |
| [Tailscale Steam](wiki-topics/tailscale-steam/index.md) | Tailscale + Steam streaming |
| [Talked Architecture](wiki-topics/talked-architecture/index.md) | Architecture discussions |
| [Try Again](wiki-topics/try-again/index.md) | Retry logic |
| [User Message](wiki-topics/user-message/index.md) | User messaging |
| [Want Version](wiki-topics/want-version/index.md) | Version requests |
| [What Mean](wiki-topics/what-mean/index.md) | Meaning analysis |
| [Whoa There](wiki-topics/whoa-there/index.md) | Alerts and monitoring |
| [Wiki Want](wiki-topics/wiki-want/index.md) | Wiki feature requests |
| [YouTube](wiki-topics/youtube/index.md) | YouTube content |
| [20+ Archived](wiki-topics/_archive/) | Absorbed topics preserved verbatim |

---

## Skills & Capabilities

Reusable procedures Hermes knows how to run. Each skill is a SKILL.md file with frontmatter (name, description, when to use it). Skills are the *verbs* of the system — what Hermes can *do*. All skills below are symlinked to Hermes — edit in vault, updates Hermes live.


| Skill | Use |
|-------|-----|
| [agent-wiki-vault](skills-capabilities/hermes-skills/agent-wiki-vault/SKILL.md) | Use when working in the user's agent-wiki Obsidian vault |
| [agent-wiki-vaults](skills-capabilities/hermes-skills/agent-wiki-vaults/SKILL.md) | Build agent-wiki (GOOP) Obsidian vaults from GitHub repos |
| [apple](skills-capabilities/hermes-skills/apple/SKILL.md) | Apple Notes, Reminders, FindMy, iMessage, macOS settings |
| [autonomous-ai-agents](skills-capabilities/hermes-skills/autonomous-ai-agents/SKILL.md) | Spawning and orchestrating autonomous AI coding agents |
| [browserless-web-debugging](skills-capabilities/hermes-skills/browserless-web-debugging/SKILL.md) | Debug single-file HTML/JS pages without a browser |
| [creative](skills-capabilities/hermes-skills/creative/SKILL.md) | Creative content generation: ASCII art, diagrams, visual design |
| [devops](skills-capabilities/hermes-skills/devops/SKILL.md) | DevOps, remote Linux ops, SDLC review |
| [email](skills-capabilities/hermes-skills/email/SKILL.md) | Himalaya CLI: IMAP/SMTP email from terminal |
| [github](skills-capabilities/hermes-skills/github/SKILL.md) | GitHub via gh CLI: PRs, issues, reviews, repos |
| [knowledge-vault](skills-capabilities/hermes-skills/knowledge-vault/SKILL.md) | Build an Obsidian vault of project topics from user sources |
| [media](skills-capabilities/hermes-skills/media/SKILL.md) | YouTube transcripts, GIF search, music generation, audio visualization |
| [mlops](skills-capabilities/hermes-skills/mlops/SKILL.md) | Machine Learning Operations: training, deploying, optimizing ML models |
| [note-taking](skills-capabilities/hermes-skills/note-taking/SKILL.md) | Note taking skills: Obsidian, Apple Notes, Apple Reminders |
| [productivity](skills-capabilities/hermes-skills/productivity/SKILL.md) | Document creation, presentations, spreadsheets |
| [research](skills-capabilities/hermes-skills/research/SKILL.md) | Academic research, paper discovery, literature review |
| [smart-home](skills-capabilities/hermes-skills/smart-home/SKILL.md) | Control Philips Hue lights, scenes, rooms via OpenHue CLI |
| [social-media](skills-capabilities/hermes-skills/social-media/SKILL.md) | Reddit, X/Twitter interactions |
| [software-development](skills-capabilities/hermes-skills/software-development/SKILL.md) | Codebase inspection, debugging, testing, simplification |
| [turbofit](skills-capabilities/hermes-skills/turbofit/SKILL.md) | Rules for Turbofit Wiki |
| [turbofit-runtime-setup](skills-capabilities/hermes-skills/turbofit-runtime-setup/SKILL.md) | Use when setting up or fixing the Turbofit local runtime |
| [web](skills-capabilities/hermes-skills/web/SKILL.md) | Reach web content when direct access fails |


---

## Bots & Profiles

Autonomous Hermes agents, each with its own SOUL.md defining its role, behavior, and boundaries. Bots are the *nouns* of the system — who does the work. All bots below are symlinked to Hermes — edit in vault, updates the bot live.


| Bot | Role | Use |
|-----|------|-----|
| [senter](bots-profiles/hermes-profiles/senter/SOUL.md) | Sidebar | Chris talks here. Routes, never builds. |
| [klerik](bots-profiles/hermes-profiles/klerik/SOUL.md) | Profile factory | Reviews and corrects other bots |
| [looker](bots-profiles/hermes-profiles/looker/SOUL.md) | UI-QA | Screenshots, vision, verification |
| [teknium](bots-profiles/hermes-profiles/teknium/SOUL.md) | Core builder | Hermes-Agent fixes, upstream PRs |
| [paladin](bots-profiles/hermes-profiles/paladin/SOUL.md) | Warden | Vault structure, repo hygiene |
| [weaver](bots-profiles/hermes-profiles/weaver/SOUL.md) | UI builder | vault-live.html, CSS, layout |
| [dogeman](bots-profiles/hermes-profiles/dogeman/SOUL.md) | Content studio | YouTube, scripts, visuals |
| [turbosovth](bots-profiles/hermes-profiles/turbosovth/SOUL.md) | TurboFit support | Model research, never merges |
| [anser](bots-profiles/hermes-profiles/anser/SOUL.md) | Native answers | Citations only, no hallucination |
| [hermes-agent](bots-profiles/hermes-profiles/hermes-agent/SOUL.md) | Runtime | Provider config, model routing |
| [turbofit](bots-profiles/hermes-profiles/turbofit/SOUL.md) | Inference | Model zoo, pipelines, hardware |


---

## Triggers & Loops

Scheduled automations (cron jobs), kanban tasks, and webhooks. Loops are the *temporal* dimension — what runs when, how often, and what it checks.

| Automation | Cadence | What |
|------------|---------|------|
| senter-umbrella | 30m | Governance: merge, dedupe, catalogs |
| senter-watcher | continuous | Cut messages into per-topic inbox |
| senter-scanwatch | continuous | Snapshot vault state |
| turbofit-health-check | 2h | All runtime processes healthy? |
| turbofit-memory-monitor | 15m | Memory usage across devices |
| turbofit-candidate-discovery | 6h | New models on HuggingFace |
| hermes-model-change-detector | 5m | Alert if model switches |
| compression-timeout-watch | 10m | Hermes compression failures |
