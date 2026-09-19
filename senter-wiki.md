---
title: Senter Wiki
created: 2026-07-07
updated: 2026-09-19
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

The Senter Wiki is the **master orchestration layer** for everything Chris cares about. It coordinates the entire Hermes fleet — turning haphazard conversations into organized, actionable work across dozens of topics simultaneously.

---

## How This Works

The wiki mirrors how Hermes itself works. Hermes has:
- **Memory** (MEMORY.md + USER.md) — persistent facts that survive across sessions
- **Skills** (SKILL.md files) — reusable procedures with frontmatter for discovery
- **Profiles** (SOUL.md files) — autonomous agents with defined roles
- **Cron/Kanban** — scheduled automations and task boards
- **Sessions** — conversation history that gets compressed and archived

The Senter Wiki takes these same patterns and makes them **visible, editable, and navigable** in Obsidian. Every piece of Hermes capability has a markdown representation in this wiki. Edit the wiki → Hermes sees the change.

### Progressive Disclosure

Just like Hermes discovers skills by scanning frontmatter before loading the full SKILL.md, this wiki uses the same pattern for everything:

1. **Scan** — README shows names + one-line descriptions
2. **Click** — Open any entry to see full detail
3. **Drill** — Sub-entities link to their definitions
4. **Act** — Edit any file, approve any card, spawn any bot

This applies to Topics, Skills, Bots, and Loops alike.

---

## Inspiration & Integrations

Everything that feeds data into the wiki. This is the *sensory layer* — without integrations, the wiki has no input.

### How It Works

Hermes ingests data from multiple sources:
- **Memory tool** — reads/writes MEMORY.md and USER.md (persistent facts)
- **Sessions** — conversation history stored in `~/.hermes/state.db`
- **Gateway** — messages from Telegram, Discord, Slack, WhatsApp, etc.
- **Webhooks** — event-driven HTTP callbacks
- **Cron** — scheduled jobs that produce output
- **Skills** — built-in capabilities like github, arxiv, rss-feeds, blogwatcher

The wiki captures all of this into `raw/inbox/` (daily cuts from sessions) and `wiki/assets/` (inspiration bin for images, clips, bookmarks).

### Hermes Capabilities for Ingestion

| Capability | What | Wiki Section |
|------------|------|--------------|
| `/learn <source>` | Learn a skill from dirs/URLs/this chat | Skills |
| `hermes sync` | Sync skills across devices | Skills |
| `hermes gateway` | Messaging gateway (20+ platforms) | Integrations |
| `hermes webhook` | Dynamic webhook subscriptions | Integrations |
| `hermes peer` | Bot-to-bot DMs across machines | Integrations |
| `hermes project` | Multi-folder workspaces | Topics |
| Memory tool | Persistent MEMORY.md / USER.md | Integrations |
| Sessions | Conversation history in state.db | Integrations |
| Built-in skills | github, arxiv, rss-feeds, blogwatcher, etc. | Integrations |

### Integration Links
- [GitHub](https://github.com/SouthpawIN/Senter) — code, issues, PRs
- [HuggingFace](https://huggingface.co/SouthpawIN) — model repos
- Hermes state.db — chat messages cut into per-topic inbox
- Sessions — full conversation transcripts
- Fleet Daemons — watcher, topic-agent, umbrella, bridge, scanwatch

### Inspiration Bin
- *Empty — start capturing!*

---

## Wiki & Topics

Processing information into structured knowledge. Every subject Chris cares about gets its own topic with evidence, decisions, and action items.

### How It Works

Based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and the GOOP spec. Each topic is a self-contained wiki:

```
topics/<slug>/
├── README.md          ← human dashboard (facts + source extract)
├── .system/           ← machine internals
│   ├── continuity.md  ← raw understanding; user corrects here
│   ├── queue.md       ← [SKILLS]/[AGENTS]/[LOOPS] work items
│   └── injections.md  ← status feed
├── skills/  agents/  loops/  ← topic-specific capabilities
└── wiki/              ← structured knowledge (entities, concepts, decisions)
```

The agent ingests sources → creates entity/concept pages → cross-references with `[[wikilinks]]` → maintains index.md and log.md for navigation.

### Hermes Capabilities for Wiki Processing

| Capability | What | Wiki Section |
|------------|------|--------------|
| `/llm-wiki` | LLM Wiki slash command | Wiki |
| `/curator` | Skill maintenance and discovery | Skills |
| `hermes skills` | Skill discovery and management | Skills |
| `hermes kanban` | Task board for tracking work | Loops |
| `hermes sessions` | Session management and history | Integrations |
| Built-in: apple-notes, obsidian, knowledge-vault | Note taking and vault building | Wiki |
| Built-in: document-to-action-items, meeting-action-items | Extract tasks from docs | Wiki |
| Built-in: weekly-review-planning, session-librarian | Review and organization | Wiki |

### Current Topics

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

Reusable procedures Hermes knows how to run. Each skill is a SKILL.md file with frontmatter (name, description, when to use it). Skills are the *verbs* of the system.

### How It Works

Hermes discovers skills via **progressive disclosure**:
1. **Scan** — Read frontmatter (name, description, tags) from all SKILL.md files
2. **Match** — When a task matches a skill's description, load the full SKILL.md
3. **Execute** — Follow the skill's instructions
4. **Learn** — `/learn` creates new skills from experience

The **curator** maintains skill lifecycle: tracks usage, marks stale skills, archives unused ones, backs up before changes.

### Hermes Capabilities for Skills

| Capability | What | Wiki Section |
|------------|------|--------------|
| `/skills` | Search/install/manage skills | Skills |
| `/bundles` | List skill bundles (load multiple) | Skills |
| `/learn <source>` | Learn a reusable skill from dirs/URLs/chat | Skills |
| `/curator [sub]` | Skill maintenance (status, run, pin, archive) | Skills |
| `/reload-skills` | Re-scan skills directory | Skills |
| `hermes sync` | Sync skills across devices | Skills |
| `hermes curator` | CLI for curator (status, usage, run, pause, resume, pin, archive) | Skills |
| Skill frontmatter | name, description, version, author, tags, metadata | Skills |
| Skill trust levels | local, builtin, official — controls auto-apply | Skills |

### All Skills (Symlinked to Hermes)

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

Autonomous Hermes agents, each with its own SOUL.md defining its role, behavior, and boundaries. Bots are the *nouns* of the system.

### How It Works

A **profile** is a complete Hermes instance with:
- `SOUL.md` — defines the bot's personality, role, and behavior
- `AGENTS.md` — project-specific instructions
- `MEMORY.md` — persistent memory for that profile
- `USER.md` — user-specific facts
- `skills/` — profile-specific skills
- `config.yaml` — profile-specific config

Profiles are discovered the same way as skills: scan frontmatter → load full definition. The `hermes profile` CLI manages creation, installation, and distribution.

### Hermes Capabilities for Bots

| Capability | What | Wiki Section |
|------------|------|--------------|
| `/profile` | Active profile info | Bots |
| `/new (/reset) [name]` | Fresh session | Bots |
| `/personality [name]` | Set a personality | Bots |
| `/agents (/tasks)` | Show active agents | Bots |
| `hermes profile` | Profile management (create, install, list) | Bots |
| `hermes chat -p <profile>` | Run commands against a profile | Bots |
| Profile install | `hermes profile install <path>` distributes profiles | Bots |
| SOUL.md | Defines role, behavior, boundaries | Bots |
| AGENTS.md | Project-specific instructions | Bots |
| Profile distribution | Share profiles via git or packages | Bots |

### Active Bots (Symlinked to Hermes)

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

### How It Works

Hermes has four background systems:

1. **Cron** — Durable scheduler. Jobs run on schedules (30m, 2h, daily, etc.), can chain output into other jobs, deliver to multiple platforms.
2. **Kanban** — Multi-profile task board. Tasks flow through todo → running → done/blocked. Dispatcher spawns workers for each task.
3. **Webhooks** — Event-driven HTTP callbacks. External services trigger Hermes runs.
4. **Delegation** — Subagent spawning. `delegate_task` creates isolated workers for parallel work.

All four produce output that feeds back into the wiki (via cron jobs that update markdown, or via the watcher that cuts sessions into topics).

### Hermes Capabilities for Automation

| Capability | What | Wiki Section |
|------------|------|--------------|
| `/cron [sub]` | Manage scheduled tasks | Loops |
| `/suggestions (/suggest)` | Review suggested automations | Loops |
| `/blueprint (/bp) [name]` | Set up automation from blueprint | Loops |
| `/kanban [sub]` | Multi-profile collaboration board | Loops |
| `/goal [text|sub]` | Standing goal across turns | Loops |
| `/subgoal [text]` | Add/manage criteria | Loops |
| `hermes cron` | Cron job management (list, add, edit, pause, resume, run, remove) | Loops |
| `hermes kanban` | Task board (init, create, list, show, assign, link, complete, block, archive) | Loops |
| `hermes webhook` | Webhook management | Loops |
| `hermes send` | Send messages to platforms | Loops |
| `delegate_task` | Subagent spawning (single or batch) | Loops |
| Cron schedules | duration ("30m"), "every" phrase, 5-field cron, ISO timestamp | Loops |
| Cron chaining | `context_from` chains job A's output into job B | Loops |
| Kanban dispatcher | Auto-spawns workers, reclaims stale claims, blocks on failure | Loops |

### Active Automations

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

---

## How They All Work Together

```
Chris talks → Hermes sidebar (senter)
     ↓
Watcher cuts messages → raw/inbox/<topic>/
     ↓
Topic agent ingests → wiki/topics/<topic>/ (entities, concepts, decisions)
     ↓
Patterns emerge → Hermes proposes skills/bots/loops
     ↓
Chris approves → Capability created (SKILL.md, SOUL.md, cron job)
     ↓
Capability runs → Output feeds back into wiki
     ↓
Wiki self-organizes → Progressive discovery of everything
```

The wiki is not separate from Hermes — it's the **visible, editable surface** of Hermes. Edit a SKILL.md in the wiki → Hermes reads it next session. Edit a SOUL.md → the bot's behavior changes. Create a cron job → the wiki updates itself.

This is the bonsai pattern: the same structure at every scale, all the way down.
