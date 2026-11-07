![Bot Wiki](assets/hero-bot-wiki.png)

# Bot Wiki

> **A fleet of bots, described entirely in markdown. Each project has its own bot; the wiki is how they coordinate.**
>
> Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com).
> `SENTER.md` is the language layer. Senter is the agent you talk to. The bots are the ones with jobs.

---

## What Bot Wiki is

Bot Wiki is a working system for running many projects at once without losing any
of them. Every project you care about gets a **bot**: one directory that holds the
mission, the procedures, the work queue, and the schedule for that project. The
bots live in a markdown wiki, so the whole system is readable and editable by hand.

There is no database, no config panel, and no dashboard to keep in sync. Open a
file, change what the bot should do, and the system picks it up. That is the entire
steering mechanism.

```text
you  ──►  Senter (conversation)  ──►  the bot that owns the work  ──►  files, tools, schedules
                    ▲                              │
                    └────────  markdown  ◄─────────┘
```

## The three layers

| Layer | What it is | Where it lives |
|---|---|---|
| **Conversation** | Senter, the agent you talk to. It decides which bot owns a request, loads that bot, and reports back in plain language. | Hermes |
| **Bots** | One owner per project: mission, procedures, queue, clock, and the things it may never do alone. | `bots/<slug>/` |
| **Wiki** | The shared understanding: what each bot knows, what is owed, what changed, what is blocked. | markdown files |

Senter is personified as the three-eyed owl in Herm and backed by an unnamed,
tool-free speech-to-speech auxiliary. It is not a tenth bot and it keeps no project
state of its own — it routes, and the state stays on disk where you can read it.

## The four primitives

Everything in the wiki is one of four things:

| Primitive | What it is | Path |
|---|---|---|
| **Bot** | An owned topic: identity, mission, holds, and a clock. | `bots/<slug>/BOT.md` |
| **Context** | What the bot understands: continuity, decisions, open questions. | `bots/<slug>/.system/` |
| **Skills** | Executable procedures the bot loads on demand. | `bots/<slug>/skills/<name>/SKILL.md` |
| **Loops** | A skill bound to a schedule, so work happens without being asked. | `bots/<slug>/loops/<name>.md` |

They nest: a **Bot** holds **Context**, runs **Loops**, and loads **Skills**. That
nesting is the whole architecture.

## How a bot is built

```
bots/<slug>/
├── BOT.md                  mission · operating loop · owns · skills · loops · holds · needs
├── .system/                continuity.md · queue.md · injections.md
├── skills/<name>/SKILL.md  procedures, not descriptions
└── loops/<name>.md         a skill plus a clock
```

`BOT.md` is the only file you have to write. It answers, in order:

- **Mission** — what "done" means, as an outcome.
- **Operating loop** — the numbered cycle the bot runs.
- **Owns** — the repos, paths, accounts, and artifacts that are its responsibility.
- **Skills** — the procedures it loads, and when.
- **Loops** — what runs on a schedule, and whether it is armed.
- **Hold points** — what it may never do alone: spend money, publish in your name,
  submit a form, delete data.
- **Needs from you** — when it is stuck, the exact action that unsticks it.
- **Log** — append-only, newest first.

`.system/` is dot-prefixed so file browsers hide it. Open it anyway — that is the
debugger. The front end stays clean, the back end stays inspectable.

Every bot carries a status: `live` (running, with a proven loop), `seeding`
(written, not yet armed), `paused`, or `blocked` (and a blocked bot must name its
ask in one line).

## The fleet index

```
bots/_fleet/FLEET.md
```

One table: every bot, its callsign, its topic, its status, how many loops are live,
and what it is waiting on. It is the only page that claims to be current, and it is
where a session starts.

`_fleet/.system/queue.md` is the other shared surface: work that crosses bots. No
bot edits another bot's `BOT.md` — cross-bot changes are filed there instead.

## How work moves

From a sentence to a running system, all of it through markdown:

1. **Ask.** You tell Senter what you want.
2. **Understand.** The bot's `continuity.md` is updated with what that means.
3. **Shape.** A bot is created or amended: mission, three skills, one loop.
4. **Execute.** The loop runs, produces an artifact at a predicted path, appends a
   log line.
5. **Report.** A one-line injection comes back to you in conversation.

Four factories watch for work and materialize it — Context, Skills, Agents (which
builds bots), and Loops. All four use the same pipeline: **collect evidence →
generate candidates → evaluate → apply.** They write reviewable markdown; they do
not silently create live runtime objects.

## The nine bots in this wiki

| Bot | Callsign | Owns |
|---|---|---|
| bot-wiki | **Klerik** | the method: schema, fleet index, queue reconciliation |
| youtube | **Cutroom** | hours of voice chat → chaptered videos |
| pocketshop | **Binder** | card inventory → listings → restock |
| turbofit | **TurboSouth** | TurboFit support, plus the model × hardware matrix |
| kart-racer | **Apex** | a Unity kart racer on the NRCU cast |
| ai-daw | **Riff** | a Hermes plugin driving a music DAW |
| anser | **Anser** | cited, dated answers for moderation |
| hermes | **Mesh** | one Hermes instance across every device |
| ssi | **Beacon** | benefits paperwork, drafted and tracked |

Twenty-eight skills and twelve loop specs live across them. One loop is armed; the
rest are written and waiting for a hand-run first pass, because a loop that was
never run manually fails silently forever.

## The bot that maintains the bots

`bot-wiki` is itself a bot, and that is the point: the method maintains itself
while it maintains everything else.

Klerik (the bot-wiki bot) reads every `BOT.md`, repairs the fleet index when it
drifts from reality, claims exactly one queue item per run, and refuses to touch
another bot's identity. It also cannot edit the validator that judges it, or the
parser, tests, scripts, or another loop's schedule — a maintainer with that power
has no oversight. Its own first live run corrected two stale blockers in the index
and fixed a bug in its own procedure, then the spec was tightened to keep its writes
inside `bots/**` prose.

## Quick start

```bash
git clone https://github.com/SouthpawIN/bot-wiki.git ~/.hermes/wiki
cd ~/.hermes/wiki

# Parse every bot and propose work from the markdown
python -m senter_agent . --json

# Contract tests and bot-layout verification
PYTHONPATH=. pytest -q
python scripts/verify_bots.py .          # bots=9 skills=28 loops=12 problems=0

# Publish each bot as a Hermes skill named bot-<slug>
python tools/publish_skills.py . ~/.hermes
```

## Running it on Hermes

A bot **is** a Hermes profile — its own config, memory, skills, credentials, and
chat history under `~/.hermes/profiles/<slug>/`. Bot Mode renders that roster, so
the bots in the wiki and the bots on screen are the same entities.

- `skill: bot-<slug>` loads one bot into any session.
- `hermes -p <slug> chat` opens the same agent the wiki describes.
- Each bot's loops appear in `hermes cron list` beside its Bot Chat.

The wiki is the design document; Hermes is the runtime. Nothing is translated by
hand, and the published `bot-<slug>` skills are generated — edit `BOT.md`, re-run
the publisher.

Arming the maintainer loop:

```bash
hermes cron create "0 6 * * *" --name fleet-reconcile \
  --prompt "$(sed -n '/## Prompt/,/## Stop/p' ~/.hermes/wiki/bots/bot-wiki/loops/fleet-reconcile.md)"
```

## Verification

| Check | Result |
|---|---|
| `PYTHONPATH=. pytest -q` | 69 passed |
| `python scripts/verify_bots.py .` | 9 bots · 28 skills · 12 loops · **0 problems** |
| `python -m senter_agent . --json` | 78 documents, 9 `type: bot` documents |
| Published skills | 9 × `bot-<slug>` |
| Armed loops | 1 (`fleet-reconcile`, 06:00 UTC) |

The validator exits nonzero on: a missing `type: bot`, a slug that disagrees with
its directory, a missing required section, a skill or loop named in `BOT.md` but
absent on disk, `blocked` without an actionable ask, or a `[[wiki link]]` that
resolves to nothing. If it is green, the wiki is internally consistent.

## Design principles

1. **Markdown is the API** — human ↔ machine, machine ↔ machine.
2. **The wiki is the system** — no database, no dashboard, no YAML wizard.
3. **One bot, one topic** — two missions means two bots.
4. **Skills are procedures** — if a fresh agent cannot execute it step by step, it
   is prose and belongs in continuity.
5. **Loops name their skill** — an unbound loop is a mystery cron job.
6. **Hold points are absolute** — money, publishing, filings, deletions.
7. **`blocked` requires an ask** — a stuck bot with no ask is a dead bot.
8. **No self-edit** — the bot that writes bots cannot rewrite itself.
9. **Dot-prefix machine internals** — `.system/` is hidden, not secret.

## Learn more

- [[BOT_SCHEMA|Bot Schema]] — the standard every bot is written against
- [[bots/_fleet/FLEET|Fleet]] — the live roster and cross-bot dependencies
- [[spec|Specification]] — architecture and setup in full
- [[SENTER|Senter]] — the language and context layer
- [[goop-nesting|GOOP Nesting]] — how the primitives nest
- [[goop-whitepaper|GOOP Whitepaper]] — the original design thinking

---

*Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent). Towards Self-Improvement.*
