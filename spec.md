---
title: Agent Wiki Specification
created: 2026-07-07
updated: 2026-07-07
type: spec
tags: [goop, architecture, wiki, multi-agent, hermes]
confidence: high
---

# Agent Wiki Specification

A self-documenting, self-extending multi-agent system where the wiki IS the coordination layer.
Topics are miniature GOOP instances. Markdown is the API between human and machine.

---

## The Four Primitives

Every GOOP system is made of four typed objects. Each has a factory, a Hermes write mechanism,
and lives in the wiki:

| Primitive | Factory | Hermes Write | Wiki Path | Standard |
|---|---|---|---|---|---|
| **Context** | Context | `write_file` to wiki pages | `topics/<topic>/.system/` + `README.md` | wiki markdown |
| **Loops** | Loops | `cronjob(create)`, kanban create | `topics/<topic>/loops/` | cron/kanban config |
| **Agents** | Agents | `hermes profile create` + SOUL.md write | `topics/<topic>/agents/` | `AGENTS.md` |
| **Skills** | Skills | `skill_manage(action='create')` | `topics/<topic>/skills/` | `SKILL.md` |

Primitives nest: Context contains Loops which invoke Agents which load Skills.
The wiki directory structure mirrors this nesting exactly.

### Context (outermost layer)

The shared comprehension layer — raw understanding extracted from chat, transformed into
structured knowledge. Two faces:

- **Front end** (`README.md`): Human-facing status dashboard.
- **Back end** (`.system/`): Machine-facing coordination. Continuity understanding, injection queue, factory work items.

### Loops

Execution infrastructure that produces work over time. Cron jobs, kanban tasks, webhook handlers.
A Loop links an Agent to a schedule.

### Agents

Named profiles with SOUL.md directives, toolset configs, and skill bundles. The "who" that does the work.
Agents are composed of Skills.

### Skills

Reusable markdown procedures (SKILL.md + references + scripts). Loaded on demand by agents.
The atomic unit of capability.

---

## Topic-Based Organization

Every user interest is a **topic** — a self-contained directory that holds the full GOOP stack:

```
wiki/topics/<topic-slug>/
│
├── README.md                 ← FRONT END: human-readable dashboard
├── .system/                  ← BACK END: machine coordination (hidden by default)
│   ├── continuity.md         ← Context's raw understanding from chat sessions
│   ├── injections.md         ← messages queued for Nous Girl to surface
│   └── queue.md              ← pending factory work items, tagged by factory
├── skills/                   ← skills scoped to this topic
├── agents/                   ← agent summaries serving this topic
└── loops/                    ← execution infrastructure
```

### The `.system/` Convention

Dot-prefixed directories are hidden by default in Obsidian, file browsers, and `ls`.
The user CAN open them — that's the debugger. The default experience: open `README.md` and see a clean dashboard.

### The `_global/` Topic

A special topic (underscore sorts it first) that holds fleet-wide overview:

```
wiki/topics/_global/
├── README.md                 ← fleet dashboard
├── .system/
│   ├── agent-roster.md       ← every agent across all topics
│   ├── skill-registry.md     ← every skill across all topics
│   └── loop-registry.md      ← every running loop
└── agents/                   ← symlinks to all agent summaries
```

---

## The Flywheel

From idea to working system, driven entirely by markdown reads and writes:

1. Chris speaks an idea to Nous Girl — session auto-saved to Hermes session DB
2. Context (cron, 30m) reads sessions via `session_search(profile='nous-girl')`, writes wiki pages
3. Context populates `queue.md` with tagged items: `[SKILLS]`, `[AGENTS]`, `[LOOPS]`
4. Factories watch queue.md, claim items, spawn `delegate_task`, write artifacts
5. Factories write status to `.system/injections.md`
6. Nous Girl reads injections before responding, weaves status into conversation naturally

### The Queue Format

```markdown
## [SKILLS] items
- [ ] github-api-paginate — needed for PR watcher
- [x] github-auth-setup — DONE → skills/github-auth-setup.md

## [AGENTS] items
- [ ] pr-watcher — new agent to run PR monitoring on cron

## [LOOPS] items
- [ ] pr-check-cron — wire pr-watcher to 30-min schedule
```

Factories read, claim (`[~]`), and mark done (`[x]`). Only Context creates entries.

### The Injection Format

```markdown
## [UNREAD]
[AGENTS] pr-watcher profile provisioned. SOUL.md ready for review.

## [READ]
[LOOPS] Cron deployed for pr-check. First run in 2 minutes.
```

Nous Girl's system prompt: check all topics' `.system/injections.md` for `[UNREAD]` blocks.
Weave the first one naturally into the next response, then move it to `[READ]`.

---

## User Editing = Direct Control

The wiki is user-editable. This is the steering wheel:

| What to change | Where to edit |
|---|---|
| "You misunderstood my goal" | `.system/continuity.md` — correct Context's understanding |
| "I don't want that agent" | `agents/<agent>.md` — mark cancelled |
| "Change the cron frequency" | `loops/<loop>.md` — Loops reads this |
| "Force-create a skill now" | `.system/queue.md` — add `[SKILLS] my-skill` |
| "Show me what's running" | `README.md` — the human dashboard |

No chat command. No config file. No YAML wizard. Just edit markdown.

---

## The Four Factories

All factories use the same **4-stage pipeline**: Collect evidence → Generate candidates → Evaluate → Apply.

### Context Factory

**Trigger:** Every 30 minutes.
**Input:** Nous Girl's session DB (`session_search(profile='nous-girl')`).
**Output:** Wiki pages, queue items, README updates.

Pipeline:
1. **Collect:** Read new messages since last tick. Extract entities, goals, pain points.
2. **Generate:** Draft `.system/continuity.md`, `README.md`, queue items.
3. **Evaluate:** Does this understanding match the raw chat? Are queue items actionable?
4. **Apply:** Write wiki pages. Never overwrite user-edited continuity lines.

### Skills Factory

**Trigger:** New `[SKILLS]` entries in any topic's queue.
**Output:** SKILL.md files via `skill_manage(action='create')`.

Pipeline:
1. **Collect:** Read queue item, relevant continuity, related existing skills.
2. **Generate:** `delegate_task` → produce 3-5 candidate SKILL.md files.
3. **Evaluate:** Score against rubric: completeness, clarity, reusability, evidence.
4. **Apply:** `skill_manage(action='create')` with winning candidate. Write summary.

### Agents Factory

**Trigger:** New `[AGENTS]` entries. Also watches Skill Registry for unhosted skills.
**Output:** Hermes profiles via `hermes profile create`.

Pipeline:
1. **Collect:** Read queue item, skill requirements, fleet roster.
2. **Generate:** `delegate_task` → draft candidate SOUL.md profiles.
3. **Evaluate:** Scoring matrix: fit to requirements, fleet composition, toolset.
4. **Apply:** `hermes profile create` + write SOUL.md. Write summary to agent catalog.

**No-self-edit rule:** The Agents factory cannot edit its own profile.

### Loops Factory

**Trigger:** New `[LOOPS]` entries. Also watches Agent Registry for unlooped agents.
**Output:** Cron jobs via `cronjob(create)`, kanban tasks.

Pipeline:
1. **Collect:** Read queue item, agent capabilities, execution requirements.
2. **Generate:** `delegate_task` → candidate loop architectures.
3. **Evaluate:** "Does this loop actually execute the project plan?"
4. **Apply:** `cronjob(action='create')` or kanban create. Write summary.

Prefers kanban for multi-agent work, cron for truly periodic activities.

---

## Hermes Infrastructure

The Agent Wiki system uses only existing Hermes primitives:

| Component | Hermes Primitive | Status |
|---|---|---|
| Nous Girl (chat surface) | Profile with stripped toolsets | Profile exists |
| Context (context factory) | Cron job + `session_search()` + `write_file()` | Needs creation |
| Skills (skill factory) | Cron job + `delegate_task()` + `skill_manage()` | Needs creation |
| Agents (agent factory) | Cron job + `delegate_task()` + profile create | Needs creation |
| Loops (loop factory) | Cron job + `delegate_task()` + `cronjob()` | Needs creation |
| Session storage | Hermes session DB (automatic) | ✅ Built-in |
| Cross-profile reads | `session_search(profile='...')` | ✅ Built-in |
| Wiki directory | `~/.hermes/wiki/` on filesystem | ✅ Already exists |
| Injections | System prompt + `read_file()` on wiki | Needs ~10 lines of prompt |

---

## Setup

```bash
# 1. Ensure wiki exists
mkdir -p ~/.hermes/wiki/topics/_global/.system

# 2. Strip tools from Nous Girl
hermes -p nous-girl config set agent.toolsets "[]"

# 3. Context cron — reads chat, writes wiki
hermes cron create "every 30m" \
  --name "context-factory" \
  --prompt "You are the Context factory of the Agent Wiki system.

  EVERY TICK:
  1. Read Nous Girl's latest sessions: session_search(profile='nous-girl', sort='newest', limit=5)
  2. Identify new: projects, entities, concepts, action items, pain points
  3. For each project/idea mentioned, create or update wiki/topics/<topic-slug>/
     - Write/update README.md (human-facing dashboard)
     - Write/update .system/continuity.md (your raw understanding)
     - Append to .system/queue.md: [SKILLS]/[AGENTS]/[LOOPS] items as appropriate
  4. Update wiki/topics/_global/README.md (fleet dashboard) if roster changed
  5. NEVER overwrite user-edited continuity lines
  6. Log all actions to wiki/log.md"

# 4. Skills cron — writes skills on demand
hermes cron create "every 15m" \
  --name "skills-factory" \
  --prompt "You are the Skills factory.
  Read all topics' .system/queue.md files. For each [SKILLS] item:
  1. Mark [~] (in progress)
  2. delegate_task to write a SKILL.md
  3. Call skill_manage(action='create') with the result
  4. Mark [x] done
  5. Write injection to .system/injections.md"

# 5. Agents cron — provisions agents
hermes cron create "every 15m" \
  --name "agents-factory" \
  --prompt "You are the Agents factory.
  Read queue.md for [AGENTS] items. For each:
  1. delegate_task to draft SOUL.md + profile config
  2. hermes profile create <name>
  3. Write summary to topics/<topic>/agents/<name>.md
  4. Inject status"

# 6. Loops cron — wires execution
hermes cron create "every 15m" \
  --name "loops-factory" \
  --prompt "You are the Loops factory.
  Read queue.md for [LOOPS] items AND agents/ for new agents without loops.
  For each: cronjob(create) or kanban create as appropriate.
  Write summary to loops/<name>.md. Inject status."
```

---

## Comparison to GOOP Whitepaper v1

| v1 Whitepaper | Agent Wiki |
|---|---|
| 6 persistent profiles | 1 profile (Nous Girl) + 4 cron jobs |
| Continuity = separate JSONL daemon | Continuity = Hermes session DB (already built) |
| Injection system = bespoke plugin | Injection = `.system/injections.md` + system prompt |
| Factories as named agents with persistent memory | Factories as cron-triggered `delegate_task` roles |
| 3-month build, 8 phases | ~1 hour to wire up (all Hermes primitives) |
| Separate state store | Filesystem IS the database |
| Wiki produced by Record Keeper | Wiki IS the system; Context maintains it |
| 3 primitives (Skills, Agents, Loops) | 4 primitives (adds Context, completing the stack) |

---

## Design Principles

1. **Markdown is the API.** Human → machine, machine → machine, machine → human. All via markdown files.
2. **The wiki is the system.** No separate database. No config dashboard. The filesystem IS the state.
3. **User-editable everything.** Every understanding, every queue item, every status — the user can edit it directly.
4. **Dot-prefix for machine internals.** `.system/` is hidden but accessible. Front end (README.md) is clean.
5. **Topics are self-contained GOOP instances.** Each topic contains its own Context, Loops, Agents, and Skills.
6. **Factories are thin.** Each factory is a cron job that spawns one `delegate_task`. No persistent factory profiles needed.
7. **Injections keep the human in the loop.** Factories don't message the user. They write to a file. Nous Girl reads it.
8. **No self-edit.** Agents cannot edit Agents. Context cannot rewrite its own continuity without user approval.
