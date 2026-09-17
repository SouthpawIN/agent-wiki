---
title: Agent Wiki — Authoritative Architecture
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [architecture, wiki, multi-agent, automation, idea-capture, provenance]
sources: ["raw/agent-wiki/"]
confidence: high
contested: true
---

# Agent Wiki — Authoritative Architecture

> Absorbed from the current local `projects/agent-wiki` repository. This page is the architecture-oriented synthesis; the raw captures preserve every included document.

## Core thesis

Agent Wiki is a self-documenting, self-extending multi-agent system in which **the Wiki is the coordination layer**. Markdown is the API between Chris and the machine, between factories, and between the human-facing conversational surface and background work. Each user interest is a self-contained topic with its own context, agents, skills, and loops.

## Current architectural center

The current repository converges on **Senter as the unified front door and coordinator**:

- Senter is the conversational surface that catches ideas quickly.
- Senter also coordinates background comprehension and factory work.
- The conversation should never pause while background organization or execution happens.
- The unnamed STS auxiliary is intended to remain low-intelligence/tool-free; the full profile handles coordination.
- The three-eyed owl is Senter's visual identity and represents watchful comprehension.

## Four primitives and nesting

| Primitive | Meaning | Standard output | Topic location |
|---|---|---|---|
| **Context** | Shared comprehension and continuity | Wiki pages, README, continuity | `topics-wiki/<topic>/.system/` |
| **Loops** | Execution triggers and recurring work | Kanban, webhooks, or cron where appropriate | `topics-wiki/<topic>/triggers-loops/` |
| **Agents** | Named workers with identity, tools, and skills | Hermes profile, SOUL/AGENTS | `topics-wiki/<topic>/agents/` |
| **Skills** | Reusable procedural capability | `SKILL.md` plus references/scripts | `topics-wiki/<topic>/skills-capabilities/` |

The conceptual nesting is: **Context contains Loops; Loops invoke Agents; Agents load Skills.**

## Topic contract

```text
wiki/topics-wiki/<topic>/
├── README.md
├── .system/
│   ├── continuity.md
│   ├── injections.md
│   └── queue.md
├── skills-capabilities/
├── agents/
└── triggers-loops/
```

`README.md` is the clean human dashboard. `.system/` is the hidden-but-debuggable machine layer. User edits are authoritative, especially corrections to continuity. Global catalogs provide a single-pane-of-glass view across all topics: fleet dashboard, agent roster, skill registry, loop registry, and topic index.

## Flywheel

```text
Chris speaks idea
  → session is saved
  → Context extracts entities, goals, pain points
  → Context updates topic README/continuity
  → queue items propose Skills, Agents, Loops
  → factories collect/generate/evaluate/apply candidates
  → approved artifact is written and status injected
  → Senter continues the conversation with updated context
```

## GEPA across all primitives

The repository extends GEPA's Collect → Generate → Evaluate → Apply loop beyond skill creation:

- **Context:** sessions → draft pages/continuity → check against conversation → write Wiki
- **Skills:** repeated patterns → candidate SKILL.md → score clarity/reusability → install
- **Agents:** capability gaps → candidate profile → evaluate fleet fit/toolset → provision
- **Loops:** recurring needs → candidate execution architecture → evaluate trigger/schedule → deploy

## Event-driven preference and version history

The repository contains an evolution from an earlier cron-polling design to an event-driven design:

- Earlier design: four factory crons periodically watched Markdown queues.
- Later design: Hermes hooks, Kanban dispatch, `/learn`, webhooks, `/suggestions`, and `/background` trigger work immediately.
- Cron remains appropriate for genuinely periodic work such as daily digests, cleanup, or health checks.
- The canonical direction is event-driven coordination with approval gates, not blind polling.

This contradiction is preserved rather than silently erased because both designs remain in the repository history and explain the transition.

## Human control and safety boundaries

- Markdown is directly editable by the user.
- User corrections to continuity outrank generated understanding.
- Factories must not overwrite human edits.
- No-self-edit: factories cannot rewrite their own identity or meta-configuration.
- Profile creation, skill writes, cron/webhook deployment, containers, and other consequential adapters require explicit approval/enforcement gates.
- Sensitive data belongs in secret-manager references, not Markdown.
- The Agent Wiki repository must remain separate from the live Hermes installation until changes are tested and verified.

## Connection to the broader Southpaw system

This architecture is the enabling substrate for the other Wiki themes:

- **Pocket Shop/content pipeline:** Context can organize card inventory, card-pull storylines, recordings, and proposed publishing workflows.
- **Creative studio:** Skills and Loops can manage music, video, B-roll, and card-generation pipelines.
- **Local inference:** Agents and Loops can route work through model-fleet infrastructure.
- **Discord/community work:** captured conversations can become continuity, clips, research, or project proposals.
- **Self-improving models:** GEPA provides a common evaluation pattern for workflows and model-related experiments.

## Repository status distinction

The repository's status documents distinguish specified contracts, implemented artifacts, exercised paths, and blocked live integrations. This distinction matters: an idea or architecture document is not automatically a deployed system.

## Evidence absorbed

- `README.md` — # Senter Agent > **Senter is the three-eyed owl: a self-documenting, self-extending multi-agent system. The wiki IS the coordination layer.** > > Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com). > Topics are miniature GOOP instances. `SENTER.md` is the language/context layer; Senter Agent is the interpreter and orchestrator. --- ## What is Agent Wiki? Agent Wiki organizes a multi-agent AI fleet as **a well-organized markdown vault**. Every topic you care about gets its own directory containing the full stack: - **Context** — what the system understands about your goal - **Loops** — cron jobs and workflows that run over time - **Agents** — AI profiles that do the work - **Skills** — reusable procedures agents load on demand You chat with Senter through an unnamed, low-intelligence, tool-free speech-to-speech auxiliary task. Senter watches conversations, comprehends what you want, and proposes the skills, agents, and workflows to make it happen. Progress flows back naturally in conversation. **Every part of the system is a markdown file you can edit.** No config dashboards. No YAML wizards. Open the wiki, change what…
- `spec.md` — --- title: Agent Wiki Specification created: 2026-07-07 updated: 2026-07-07 type: spec tags: [goop, architecture, wiki, multi-agent, hermes] confidence: high --- # Agent Wiki Specification A self-documenting, self-extending multi-agent system where the wiki IS the coordination layer. Topics are miniature GOOP instances. Markdown is the API between human and machine. --- ## The Four Primitives Every GOOP system is made of four typed objects. Each has a factory, a Hermes write mechanism, and lives in the wiki: | Primitive | Factory | Hermes Write | Wiki Path | Standard | |---|---|---|---|---|---| | **Context** | Context | `write_file` to wiki pages | `topics-wiki/<topic>/.system/` + `README.md` | wiki markdown | | **Loops** | Loops | `cronjob(create)`, kanban create | `topics-wiki/<topic>/triggers-loops/` | cron/kanban config | | **Agents** | Agents | `hermes profile create` + SOUL.md write | `topics-wiki/<topic>/agents/` | `AGENTS.md` | | **Skills** | Skills | `skill_manage(action='create')` | `topics-wiki/<topic>/skills-capabilities/` | `SKILL.md` | Primitives nest: Context contains Loops which invoke Agents which load Skills. The wiki directory structure mirrors this nesting exactly. ### Context (outermost layer) The…
- `SENTER.md` — # SENTER.md — GOOP Language and Context Layer > **SENTER.md is the declarative language/context layer. Senter Agent is the agent that interprets and operates on it.** > > Senter is personified in Herm by the three-eyed owl Eikon. The speech-to-speech interface is an unnamed, tool-free auxiliary task of Senter, not a separate agent. ## Mental Model `SENTER.md` is not an executable script and does not grant permissions by itself. It is human-readable source code for the GOOP system: intent, context, relationships, constraints, declarations, and desired evolution. Senter Agent is the runtime/compiler/orchestrator that interprets this source and produces proposals. ## Language Layers ### Context Markdown pages and topic directories express what the system understands: - goals and visions - entities and concepts - relationships and dependencies - decisions and unresolved questions - evidence, outcomes, and failures - summaries that reconcile related pages ### Skill A skill is a repeatable procedure. A typed document may declare one explicitly: Skills should emerge from repeated evidence, not be created merely because a capability was mentioned once. ### Agent An agent is a coherent…
- `SENTER_AGENT.md` — # Senter Agent > **Senter is the three-eyed owl.** The speech-to-speech interface is an unnamed, tool-free auxiliary task of Senter, not a separate agent. Senter Agent is the agent/runtime that interprets the markdown-native GOOP language defined by `SENTER.md`: The agent is personified in Herm by the three-eyed owl Eikon. Senter Agent is the runtime concept for a markdown-native GOOP system: The Wiki is the shared comprehension layer. Markdown is the source language; Hermes is the execution substrate; Senter is the comprehension, proposal, and orchestration layer. ## Markdown as GOOP All-caps markdown files are user-authored system declarations. For example, `MEDIA.md` can describe a media domain without immediately creating a profile or schedule. Ordinary markdown pages provide evidence and continuity. Explicit frontmatter can type a document: Supported typed objects are: - `context`: knowledge, goals, constraints, relationships - `skill`: reusable procedure - `agent`: role, behavior, tools, and workflow - `loop`: repeatable execution design The first implementation is deliberately proposal-only. It parses markdown and produces typed proposals; it does not create Hermes…
- `INTEGRATED_STATUS.md` — # Senter Agent Integrated Status This is the verification map for the complete Senter Agent system. It deliberately separates contracts, implementation, and exercised behavior. ## Components | Component | Artifact | Status | Verification | |---|---|---|---| | Unified Wiki | `~/.hermes/wiki/` | implemented | schema/index/log present | | Senter runtime | `senter_agent/` | implemented | Python test suite | | GOOP planner | `senter_agent/planner.py` | implemented, constrained | scoped source scan | | Herm TUI | `sandbox/herm-sovth/` | implemented | typecheck, tests, build, startup smoke | | Herm Petdex metadata | sidebar + `pet.info.meta` | implemented | Sidebar test | | Petdex frame rendering | Hermes `pet.cells` backend + Herm `Petdex.tsx` | implemented | Sidebar test + full Herm suite | | Android UX | `sandbox/android-surface/` | prototype implemented | browser interaction test | | Android native client | `sandbox/hermes-android/` | prebuilt APK only | no source rebuild claimed | | Android bridge | `sandbox/goop/android_bridge.py` | approval-gated implementation | contract/unit tests; live device blocked | | STS | `sandbox/goop/STS_CONFIG.json` | specified | whole-flow validator |…
- `goop-whitepaper.md` — --- title: GOOP Whitepaper v1 created: 2026-07-04 updated: 2026-07-07 type: concept tags: [goop, whitepaper, architecture, history] sources: [goop-whitepaper-v1-20260704] --- # GOOP: Gentic Object-Oriented Programming > The original architectural vision that Agent Wiki implements. > **Authors:** Anser + sovthpaw · **Date:** July 4, 2026 ## Summary GOOP reframes multi-agent AI fleets as object-oriented programming with three primitives: - **Skills** = methods (reusable procedures) - **Agents** = classes (named entities with identity) - **Loops** = main/workflow (execution infrastructure) Three factory meta-agents (Skills, Agents, Loops) produce new instances using a unified DSLy/GEPA optimization pipeline. A shared Continuity Stream + Wiki provides the memory substrate. ## What Agent Wiki Changes Agent Wiki is the **practical implementation** of GOOP. Key differences: | GOOP v1 | Agent Wiki | |---|---| | 6 persistent profiles | 1 profile + 4 cron jobs | | Continuity = separate JSONL daemon | Continuity = Hermes session DB | | Injection = bespoke plugin | Injection = `.system/injections.md` | | Factories as named agents | Factories as cron-triggered roles | | 3 primitives | 4…
- `log.md` — # Wiki Log > Chronological record of all Agent Wiki actions. Append-only. ## [2026-07-07] create | Agent Wiki initialized - Created repo: SouthpawIN/agent-wiki - Spec: spec.md, README.md - Catalogs: fleet-dashboard, agent-roster, skill-registry, loop-registry, topic-index - Concepts: goop-whitepaper, goop-nesting - Assets: 5 Nous-style concept images - Structure: catalogs/, topics-wiki/_global/, assets/
- `goop-nesting.md` — --- title: GOOP Nesting created: 2026-07-04 updated: 2026-07-07 type: concept tags: [goop, architecture, nesting] --- # GOOP Nesting Architecture The object hierarchy: **Context → Loops → Agents → Skills** Each layer builds on the previous. The nesting means each factory's output is the next factory's input. ## Factory Chain | Factory | Produces | Feeds | |---|---|---| | Context | Context (Wiki pages, queue items) | All factories | | Skills | Skills | Agents | | Agents | Agents | Loops | | Loops | Loops | The Fleet | The full chain: idea → context → skill → agent → loop, all automatic.
- `catalogs/agent-roster.md` — --- title: Agent Roster created: 2026-07-07 updated: 2026-07-07 type: catalog tags: [goop, agents, registry] --- # Agent Roster Every agent in the fleet. Click any agent to see its SOUL. Edit to change behavior. ## Front Door | Agent | Profile | Tools | Status | |---|---|---|---| | [[senter|Senter]] | `senter` | three-eyed owl; unified Agent Wiki | 🟢 Active | → SOUL.md: `~/.hermes/profiles/senter/SOUL.md` ## Topic Agents | Agent | Profile | Skills | Loops | Topic | Status | |---|---|---|---|---|---| | (none yet — Agents creates from queue) | | | | | | ## Creating an Agent **Automatic:** Context → queue → Agents provisions. **Manual:** Edit a topic's `.system/queue.md`:
- `catalogs/topic-index.md` — --- title: Topic Index created: 2026-07-07 updated: 2026-07-07 type: catalog tags: [goop, topics] --- # Topic Index Every topic = one user interest with its own full GOOP stack. | Topic | Status | Agents | Skills | Loops | |---|---|---|---|---| | (no topics yet — chat with Senter to create them) | | | | | ## Topic Structure Each topic is self-contained. You can archive a topic by moving its directory to `_archive/`.
- `catalogs/fleet-dashboard.md` — --- title: Fleet Dashboard created: 2026-07-07 updated: 2026-07-07 type: catalog tags: [goop, fleet, overview] --- # Your Fleet at a Glance → [[agent-roster|Agent Roster]] · [[skill-registry|Skill Registry]] · [[loop-registry|Loop Registry]] · [[topic-index|Topic Index]] ## Active Topics | Topic | Status | Agents | Loops | Last Activity | |---|---|---|---|---| | (no topics yet — start chatting with Senter's STS auxiliary) | | | | | ## Agent Roster | Agent | Role | Status | |---|---|---| | [[senter]] | Three-eyed owl — unified Agent Wiki | 🟢 Active | ## Running Loops | Loop | Type | Schedule | Status | |---|---|---|---| | context-factory | cron | every 30m | ⏳ pending | | skills-factory | cron | every 15m | ⏳ pending | | agents-factory | cron | every 15m | ⏳ pending | | loops-factory | cron | every 15m | ⏳ pending | ## Quick Actions - **New idea?** Tell Senter through the unnamed STS auxiliary — Context creates the topic automatically - **Force a skill:** Edit `.system/queue.md` → add `[SKILLS] my-skill` - **Fix a misunderstanding:** Edit `.system/continuity.md` directly - **See what factories are doing:** Read `log.md`
- `catalogs/skill-registry.md` — --- title: Skill Registry created: 2026-07-07 updated: 2026-07-07 type: catalog tags: [goop, skills, registry] --- # Skill Registry Every skill in the fleet. Click to see SKILL.md. Edit to change. ## Topic Skills (created by Skills) | Skill | Topic | Used By | |---|---|---| | (none yet — Skills creates from queue) | | | ## Creating a Skill **Automatic:** Context → queue → Skills writes. **Manual:** Edit a topic's `.system/queue.md`:
- `catalogs/loop-registry.md` — --- title: Loop Registry created: 2026-07-07 updated: 2026-07-07 type: catalog tags: [goop, loops, registry] --- # Loop Registry Every running loop. Edit schedule, pause, or remove. ## Factory Loops | Loop | Schedule | Status | |---|---|---| | context-factory | every 30m | ⏳ pending | | skills-factory | every 15m | ⏳ pending | | agents-factory | every 15m | ⏳ pending | | loops-factory | every 15m | ⏳ pending | ## Topic Loops | Loop | Schedule | Agent | Topic | Status | |---|---|---|---|---| | (none yet — Loops creates from queue) | | | | | ## Creating a Loop **Automatic:** Loops detects unlooped agents → wires them. **Manual:** Edit a topic's `.system/queue.md`:
- `sandbox/goop/PETDEX.md` — # PETDEX.md — presentation-only mascot contract Petdex is a presentation adapter for Hermes surfaces. It may show activity states, but never grants execution permission and never changes the Senter approval boundary. ## Selection - Hermes-native commands: `hermes pets list`, `hermes pets install <slug> --select`, `hermes pets doctor`. - The active mascot is profile-scoped under `<HERMES_HOME>/pets/`. - Senter's owl Eikon remains the authoritative identity; Petdex is an optional activity indicator and must fall back to the static owl when unavailable. ## Whole-flow mapping | Flow state | Petdex state | |---|---| | idle | idle | | thinking/listening/working | run | | speaking | done | | error | error | ## Safety Petdex is display-only. It cannot invoke ADB, shell, host tools, STS capture, or speech playback. Missing gallery/network/terminal graphics support must degrade gracefully to the static Herm/Eikon asset. ## Verification Use `hermes pets doctor` only in a disposable profile. Do not install, select, or modify a live Hermes profile without explicit approval. Source: the Hermes-native `petdex` skill, not a duplicated mascot implementation.
- `sandbox/goop/ANDROID.md` — # ANDROID — Senter mobile surface ## Context The Android surface is another front end for Senter Agent. It is not a separate agent. Its speech path is the unnamed STS auxiliary task of Senter. ## Side Button Mode - A side-button invocation opens a compact input-bar overlay. - The overlay supports voice/text input and a Senter response surface. - The same icon is tap-to-send and double-tap-to-screenshot. - The icon can be dragged upward to expand into the full chat view. ## Full Chat Canvas The expanded view contains: - input bar - conversation canvas - building-block sidebar - drag-and-drop placement onto the center canvas - morphable UI elements with sensible defaults Initial building blocks: - `SESSIONS.md` - `CHAT.md` - `SENTER.md` - current topic context - proposal queue - Kanban status ## Phone Operations Screenshots and phone operations are explicit capabilities of the Android client and must remain permission-gated. Senter Agent decides what should happen; Android enforces user/system permissions. ## Emergence Android UI work is evidence for the Senter Agent process. Repeated operations should produce Skills; coherent skill clusters may produce an Agent proposal; stable…
- `sandbox/goop/HERM_FRONTEND.md` — # HERM_FRONTEND.md — Senter Herm surface ## Purpose Create a sandbox-only modified Herm TUI frontend for Senter Agent. Senter is the three-eyed owl; the STS interface remains an unnamed auxiliary task. ## Default Identity - Default Eikon: Senter's three-eyed owl - Use the accepted embedded owl player as the animation reference - Preserve the six-state mapping in `EIKON.md` - Do not invent or redesign missing animation states - Keep the Eikon readable at terminal scale ## Sidebar Keep the live conversation visible while exposing the Wiki beside it: - current `SENTER.md` context - active topic summary - related topics - current Skills - proposed Agents - proposed Loops - proposal queue - Kanban activity - unread injections ## Canvas The center chat canvas remains the primary surface. Sidebar blocks can be opened, collapsed, or dragged into the center as inspectable panels. Default blocks: - `SESSIONS.md` - `CHAT.md` - `SENTER.md` - active topic - Context summary - proposal queue - Kanban status ## Constraints - Build only in `sandbox/herm-sovth/` or a separate frontend branch. - Never modify the live Herm installation. - Preserve Herm's existing gateway and session behavior. - Use…
- `sandbox/goop/EIKON.md` — # EIKON.md — Senter owl integration contract ## Authority The embedded owl player is the accepted animation reference and source artifact: - `owl-player-embedded.html` - embedded identifier: `owl-animated-24fps` - source states: `idle`, `thinking`, `speaking` - source frame rate: 24 fps - source grid: 192×96 Do not redesign the owl or generate replacement animation art as part of frontend integration. ## Herm State Mapping The Herm avatar driver has six runtime states. The accepted mapping is: | Herm state | Source animation | |---|---| | `idle` | `idle` | | `thinking` | `thinking` | | `speaking` | `speaking` | | `listening` | `thinking` | | `working` | `thinking` | | `error` | `speaking` | The source animations are reused as-is. Missing Herm states are aliases, not new clips. ## Integration Boundary The browser player and the Herm `.eikon` format are different representations. The browser player must remain available for visual verification. A production `.eikon` conversion is a separate, reproducible preprocessing step and must not silently alter the selected animations. Until that converter is verified at real Herm TUI scale, Herm may use its existing baked fallback while the…
- `sandbox/goop/SENTER.md` — # SENTER.md — sandbox profile This is the sandbox-mounted GOOP language/context layer. Senter Agent is the interpreter and orchestrator; Senter is represented by the three-eyed owl Eikon. ## Runtime Boundary - Use only the disposable sandbox HERMES_HOME. - Never modify the host Hermes installation. - Keep credentials outside the image and inject them at runtime. ## Objects - Context: this file and evolving Markdown topics. - Skills: proposed from repeated workflows. - Agents: proposed from coherent skill clusters. - Loops: proposed only after an agent workflow stabilizes. ## Default Profile Start with proposal-only behavior. No Hermes profile, skill, cron, webhook, or external action is created without explicit approval. ## GOOP Lifecycle Collect → Generate → Evaluate → Apply. All changes are reviewable Markdown first; application to Hermes is a later gated step.
- `sandbox/goop/STS.md` — # Auxiliary STS Speech-to-text (STT) and text-to-speech (TTS) are auxiliary adapters in the Senter flow, not tool runners. - Contract: `STS_CONFIG.json` - Runtime adapter: `senter_agent/sts.py` - Lifecycle: listening/transcribing → Eikon `thinking`; speaking → `speaking`; idle → `idle`. - Audio capture and playback remain caller-owned and require user approval. - The adapter has no shell, ADB, network, host-tool, or credential access. The existing Hermes auxiliary client remains the provider-facing integration point; this contract prevents speech state from becoming an execution path.
- `sandbox/goop/profiles/base/SENTER.md` — # SENTER.md — base GOOP profile SENTER.md is the language/context layer. Senter Agent is the interpreter, comprehension engine, and orchestrator. Senter is represented in Herm by the three-eyed owl Eikon. ## Runtime Contract - Begin proposal-only. - Collect Markdown context and existing topic evidence. - Reconcile into existing topics before creating new ones. - Propose Skills from repeated procedures. - Propose Agents from coherent skill clusters. - Propose Loops only after workflows stabilize. - Never modify the live Hermes installation. ## Lifecycle Collect → Generate → Evaluate → Apply. Application to Hermes, Android, or a Docker runtime is approval-gated.
- `sandbox/goop/profiles/base/SESSIONS.md` — # SESSIONS.md ## Role A default Senter canvas building block for session history and continuity. ## Display Show recent sessions, active session, and links back to source records. Never expose secrets or mutate session history from a display-only block. ## GOOP Repeated session-management operations may become Skills; stable workflows may become proposed Loops.
- `sandbox/goop/profiles/base/CHAT.md` — # CHAT.md ## Role A default Senter canvas building block for the live conversation. ## Display Show the current conversation and allow context blocks to be opened beside it. Keep the STS auxiliary path fast and tool-free. ## GOOP Conversation evidence feeds Context reconciliation. Repeated requests become Skills; coherent clusters may become Agents; stable workflows may become proposed Loops. ## Safety The chat block does not grant tools or permissions by itself. Success is measured by response latency, continuity, and correct topic/context attachment. The user remains the authority for applying proposals. The user may edit this block as Markdown source. The block must remain readable in the terminal and Android canvas. The block should degrade gracefully if the gateway is unavailable. The block should never include credentials. The block may link to source records. The block can be duplicated for experiments. The block's state is not executable code. The block is part of the Senter Agent language layer. The block may later gain morphable UI metadata. The block is complete.
- `sandbox/goop/profiles/research/RESEARCH.md` — # RESEARCH.md — GOOP profile ## Purpose Organize research topics, sources, summaries, contradictions, and follow-up questions. ## Allowed - Read explicitly supplied sources - Create source-linked summaries - Propose research Skills and Agents when patterns repeat ## Forbidden - Invent citations - Present uncertain claims as established facts - Publish externally without approval ## Lifecycle Collect → Generate → Evaluate → Apply. Application remains proposal-only until explicitly approved. ## Defaults - `SESSIONS.md` - `CHAT.md` - `SENTER.md` - source index - proposal queue These are context building blocks, not credentials or executable code.
- `sandbox/goop/profiles/wallet/WALLET.md` — # WALLET.md — GOOP profile ## Purpose Describe safe handling of masked wallet metadata and secret-manager references. ## Allowed - Read masked metadata - Prepare reports that never contain full payment credentials ## Forbidden - Reveal full card numbers - Reveal CVVs or security codes - Make purchases without explicit approval - Put credentials in Markdown, Docker images, logs, or chat ## Approval - Any transaction - Any external transmission - Any modification to stored secrets ## Secret References - secret-manager://wallet/cards ## Lifecycle Collect → Generate → Evaluate → Apply. This profile is a policy declaration only. It does not grant access to secrets or create an agent.
- `sandbox/goop/profiles/media/MEDIA.md` — # MEDIA.md — GOOP profile ## Purpose Develop a media/video pipeline through Senter's evidence-driven process. ## Context - live-video editing - footage slicing - generated B-roll - useful graphs - overlays and general edits - independent animated videos - article and infographic illustration ## Evolution Repeated operations should become Skills. Coherent media skill clusters may become Agents. Stable media workflows may become proposed Loops. ## Safety Preserve source footage. Use reversible edits. Require approval before publishing or deleting source material. ## Lifecycle Collect → Generate → Evaluate → Apply. Application remains proposal-only until explicitly approved.

## Related pages

- [[agent-fleet|Agent Fleet]]
- [[automation-event-systems|Automation Event Systems]]
- [[memory-wiki|Memory Wiki]]
- [[../syntheses/agent-fleet-and-hermes-ecosystem|Agent Fleet and Hermes Ecosystem]]
- [[../queries/top-level-plan-v1|Top-Level Plan v1]]
