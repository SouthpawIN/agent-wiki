---
title: Bot Schema (bot-first v2)
type: spec
created: 2026-11-07
tags: [bot, schema, goop, standard]
---

# Bot Schema — bot-first v2

The unit of this system is the **bot**, not the topic. A topic is what a bot is
responsible for; it is not a directory of its own. Everything a bot needs lives
under `bots/<slug>/`.

```
bots/<slug>/
├── BOT.md                  ← identity + dashboard (the only file you must write)
├── .system/                ← machine coordination (hidden, still editable)
│   ├── continuity.md       ← what the bot understands about its job
│   ├── queue.md            ← [SKILLS]/[LOOPS]/[BOTS] work items
│   └── injections.md       ← status for the human's next conversation
├── skills/<slug>/SKILL.md  ← procedures the bot loads on demand
└── loops/<slug>.md         ← schedules; a loop is a skill bound to a clock
```

## Why bot-first

Topic-first wikis rot: the topic page is a filing cabinet that nobody opens.
Bot-first wikis act: every directory is an entity that can be *invoked*, that
owns a queue, that grows skills, and that has a clock. A topic with no bot is
unowned knowledge — and unowned knowledge does not get maintained.

Because the method itself is a topic (`bot-wiki`), the system builds itself
while it builds everything else. That recursion is the point.

## BOT.md frontmatter (required)

```yaml
---
type: bot
slug: <kebab-case, matches directory>
name: <one word, the bot's callsign>
owner: sovthpaw
status: active | seeding | paused | blocked
created: YYYY-MM-DD
tags: [bot, <topic tags>]
repos: [org/repo]
---
```

`type: bot` is what makes a document machine-detectable. `senter_agent` parses
it, `bots/` becomes the root, and a missing `type: bot` means the file is prose,
not an entity.

## BOT.md body (required sections)

A required section may be either a heading (`## Interface`) or a bold-line
declaration (`**Interface.**`) — the parser only needs the words present, and the
short form keeps BOT.md readable at a glance.

| Section | Content | Read by |
|---|---|---|
| `# <Name> — <Topic>` | one-line mission under it | humans |
| `## Mission` | what "done" means, in outcomes not tasks | humans, planner |
| `## Interface` | the exact skill name that invokes this bot | agent |
| `## Owns` | repos, paths, accounts, artifacts | humans |
| `## Operating loop` | numbered steps of one cycle | agent, loops factory |
| `## Skills` | table: skill, when it loads, state | skills factory |
| `## Loops` | table: loop, schedule, state (spec/live) | loops factory |
| `## Hold points` | what the bot may never do alone | everyone |
| `## Needs from Chris` | unblockers, phrased as decisions | humans |
| `## Log` | append-only, newest first | humans |

## Rules the schema enforces

1. **One bot, one topic.** If a bot needs two missions, it is two bots.
2. **Skills are procedures, not descriptions.** If a SKILL.md cannot be
   executed step by step by a fresh agent, it is not a skill.
3. **Loops are skills on a clock.** A loop that does not name the skill it
   invokes is not a loop.
4. **Hold points are absolute.** Payment, publishing under Chris's name,
   submitting government forms, and deleting data require a human.
5. **`status: blocked` requires a `Needs from Chris` line.** A blocked bot with
   no ask is a dead bot and gets archived.
6. **No bot writes another bot's BOT.md.** Cross-bot changes go through
   `bots/bot-wiki/.system/queue.md`.

## Publishing

The wiki is the source of truth; Hermes holds a deployed copy.

```bash
python tools/publish_skills.py . "$HERMES_HOME"
```

That renders each `BOT.md` into `$HERMES_HOME/skills/bots/<slug>/SKILL.md` named
`bot-<slug>`, so any session loads the bot with one `skill_view("bot-<slug>")`.
The published skill carries the mission, the operating loop, the artifact paths,
the hold points, and the unblockers — the BOT.md stays the long version.

When a bot's loop is `live`, its scheduled twin is a Hermes cron job whose prompt
is the loop file's `## Prompt` body verbatim and whose workdir is the wiki clone.
`hermes cron list` is the audit surface; `loops/<slug>.md` is the spec.

## Validation

```bash
python -m senter_agent . --json          # parses every bot
python -m senter_agent . --status       # queue + materialization reconciliation
pytest -q                               # contracts
```
