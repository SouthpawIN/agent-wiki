# Senter — the architecture (Chris, 2026-09-05, verbatim-derived)

**Cursor for markdown.** The UI is an editor over one knowledge base whose files are *agentic artifacts that can be set in
motion*: SKILL.md, AGENTS.md, SOUL.md, memory.md, loop prompts — plus the context they came from. Editing a file IS
configuring the system. No dashboards; markdown is the API between human and machine.

## The five parts

| Part | Job | Explicitly NOT its job |
|---|---|---|
| **Sidebar (Hermes chat)** | Hold a conversation with Chris. Yes-and personality. Rubber-duck: draw ideas and context OUT of him. Receive every approval. | Doing tasks. It must stay unencumbered — it never builds, never runs the loops, never gets interrupted by work. |
| **Watcher** | Programmatically tail the Hermes agent logs / sessions as they are written and sort what it finds into topics. No hand-off from the sidebar — it reads the record directly. | Talking to the user. |
| **Topics** (wiki) | Hold ALL knowledge for one subject (full transcripts, artifacts, source — not summaries). Progressive disclosure via `.system/INDEX.md`. | — |
| **Per-topic loops** | Turn wiki → skills (exactly as Hermes already distils skills from sessions). When enough related skills accrue that a craft needs an intelligence around it → group them into a **bot** (profile). When a bot has a stable workflow → **suggest a loop** (cron/kanban). | Acting without approval. |
| **Approvals** | Every proposal — new skill, new bot, new loop, merge — lands in the sidebar as a card; Chris says yes/no in the flow of whatever he's talking about. | — |

## The flywheel (one topic's lifecycle)
chat → watcher files it under a topic → topic loop distils **skills** → related skills cluster into a **bot** → bot's workflow
becomes a **loop** → loop runs, produces more context → …  Every arrow that creates an artifact is an approval card in the sidebar.

## Why the sidebar must be idle
Chris jumps between topics mid-conversation. If the sidebar were executing, it would block, lose the thread, or interrupt him.
The watcher + topic loops absorb the work asynchronously; the sidebar only ever carries the conversation and the approvals.

## Mapping to what exists today
- Sidebar = the Hermes desktop default profile (this chat). Needs: a yes-and/rubber-duck SOUL, a "no tasks" AGENTS rule, and the
  INDEX-first read protocol.
- Watcher = NEW. Sources: `~/.hermes/state.db` sessions (via `hermes sessions export`), `~/.hermes/logs/agent.log`, the
  bridge `events.jsonl`. Sorting = the same TF-IDF the wiki already uses (topicDoc similarity) + an approval card when a
  message fits no topic ("new topic?").
- Topics = `wiki-topics/<t>/` (GOOP). Already hold full wiki for senter + senter-wiki; the rest get filled by the watcher.
- Topic loop = `hermes cron` per topic (Anser: WRAP) running the distil step; skill creation via the existing
  `hermes skills` / curator path; bot creation = `hermes profile create` + klerik review; loop suggestion = a kanban card.
- Approvals = `hermes serve` `approval.pending/respond` → sidebar + feed (Anser: REPLACE #1).

## Tempo — DECIDED (Chris, 2026-09-05)
"Fast paced, live editing, just like Cursor. Everything I say in the sidebar, I should watch the wiki move around on its own —
skills, bots, loops proposed all the time. Not per session: PER MESSAGE. A live-acting second brain that edits my ideas into
knowledge and agentic flows and orchestrates those flows."
- Watcher granularity: **every message** (user and assistant), as it lands — not session-end.
- Loop runner — REVISED same day (Chris): **one senter-like worker PER TOPIC, all asynchronous** — each runs its own
  wiki → skills → bot → loop-suggestion cycle independently, so topics never wait on each other. Plus **one umbrella
  senter over all of them** that is *opinionated* about combining: proposes topic merges/splits, dedupes skills across
  topics, promotes a cluster to a bot. Everything it does is a proposal card; everything is user-editable (click the file, or
  say it in the sidebar) — automation and hand-editing are the same surface.
  Implementation: workers = `hermes -p senter` invocations with the topic as argument (same profile, per-topic cwd/cron —
  N cheap processes, not N profiles); umbrella = a senter cron over the whole vault. `hermes kanban` is the natural
  claim/heartbeat layer so two workers never touch one topic at once (Anser verdict #2).
- Approvals: **one card per proposal** — the feed should be visibly busy.
- Latency target: a message in the sidebar → its wiki filed under a topic and visible in the wiki within seconds; proposals
  within the same minute.

## Decision criteria
1. **Skill** — reusable ability that belongs on an existing bot or in Hermes itself. If it’s narrow, repeatable, and doesn’t need its own memory/profile, it’s a skill.
2. **Bot** — needs its own persistent identity, memory, or runtime. If it must remember prior turns, own a schedule, or spend money/resources unattended, it’s a bot.
3. **Loop** — time/event-driven workflow owned by a bot. If it runs on cron/kanban and produces artifacts without Chris in the loop, it’s a loop.
4. **Wiki** — the topic’s full knowledge layer; everything the topic knows about itself, including transcripts, decisions, and references.

## Open questions (were) — answered above
1. Watcher granularity: sort every message, or only session-end summaries + tool results? (Every message = richer, noisier.)
2. Who runs the topic loops — one `senter` profile iterating topics, or a profile per topic once it has a bot?
3. Approval batching: one card per proposal, or a digest card per topic per loop pass?

## Librarian — progressive discovery (DECIDED concept)
The wiki itself is the API surface. Discovery should match how Hermes already discovers skills:
frontmatter → file → section → detail. The librarian is a read-time policy layer, not a new filesystem.

For topics:
- `.system/INDEX.md` is the entrypoint, one line per page.
- `README.md` is the human dashboard.
- `wiki/` is the structured knowledge: `entities/`, `concepts/`, `decisions/`, `queries/`.
- `skills-capabilities/`, `bots-profiles/`, `triggers-loops/` are the action lanes.

For skills:
- `SKILL.md` frontmatter is the contract: when to use it.
- Body is the procedure.
- References/templates are deeper; only loaded when the skill activates.

For bots:
- frontmatter declares owner/trigger/cost.
- SOUL.md/AGENTS.md/USER.md/MEMORY.md are deeper; loaded only on spawn.

For loops:
- frontmatter declares cadence/owner/claim protocol.
- Implementation details are deeper; ignored unless the loop is being edited or applied.

Rule: do not add folder depth to discover things. Add frontmatter fields and a librarian pass that reads them, then loads the deeper layer only when matched.

## Hermes-native-first principle (DECIDED)
Chris is the hermit; Hermes Agent is the commander. Hermes already discovers its own abilities via skills frontmatter, slash commands, profile config, and built-in tools. The wiki should route through those native surfaces, not beside them. If Hermes can already do it with `hermes skills`, `hermes cron`, `hermes profile`, or `hermes kanban`, we use that. The wiki only adds: live multi-topic coordination, per-message filing, proactive pitching, and UI motion. Everything else is markdown glued to existing commands.

## Approval policy — DECIDED (Chris, 2026-09-05 evening)
"These are the things that I don't want to have to give approval on or edits to the wiki." → **Topics, wiki edits, continuity
and SKILLS auto-apply** (they are markdown; Chris edits or deletes in the wiki). **Only bots and loops are proposals**
(`.proposed`, APPROVE/REJECT on the card) — those spend money and run unattended.

## Reaction speed — DECIDED
"Bots need to trigger a lot sooner … if I talk about a new subject then it should suggest maybe researching it or scaffolding it …
use a bot we've used before to research a different subject, or create a new one." → the watcher, on a substantive user message
that fits no topic, **scaffolds the topic immediately** (README/.system/skills-capabilities/agents/loops) and **dispatches a research run**
to an existing profile (looker → senter fallback) that writes `.system/research.md` and a Status line. No card to approve.

## The UI performs the fleet — DECIDED
"I want to see this thing scrolling around and flying around and topics opening and being edited and being closed." →
bridge `POST /stage {act: open|edit|close|scroll, topic|skill|loop, text}` → SSE `kind:'wiki'` → `window.stage()` scrolls the row
in, peeks its card, typewriters the changed text, closes. User always wins: any pointer-down or pinned card cancels the queue.
Emitters: watcher (every filing = edit), topic-worker (continuity + skills), umbrella (catalog refresh). Music: Spotify via Hermes'
native `hermes auth spotify` (needs Chris's client id) — bridge already proxies status/play/search.

## REVISED — one agent per topic, no separation (Chris, 2026-09-05 night)
"The watcher is watching my conversation with the sidebar live and is just cutting out pieces that are by topic and sorting those
into their topic. Each individual topic has its own agent that rewrites all inbound context as a structured wiki, and then sets
out the skills and bots and loops out of that context. Bots shouldn't wait for a bunch of skills — bots are how it suggests action,
bots then loops. When a subject is made, be very proactive: 'do you want to research this? want a bot that can do X?'"
- Watcher = the CUTTER: splits a message at subject changes, files each cut into `wiki-topics/<t>/raw/inbox/<day>.md`.
- `assets/topic-agent.py` = the ONE agent per topic (wiki compile + proactive pitches in one run). Replaces topic-worker + topic-wiki compile.
- No thresholds: a new subject gets "want me to research it?" and "want a bot?" cards immediately; the topic agent pitches concrete
  bots-profiles/loops on its first read. Skills auto-apply. Bots/triggers-loops/research are cards (APPROVE/REJECT).

