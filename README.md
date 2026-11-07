![Bot Wiki](assets/hero-agent-wiki.png)

# Bot Wiki

> **Senter is the three-eyed owl: a self-documenting, self-extending swarm of bots. The wiki IS the coordination layer.**
>
> Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com).
> One bot per topic. The bot is the markdown, the queue, the skill bundle, and the clock.
> `SENTER.md` is the language layer. Senter is the agent you talk to; the bots are the ones with jobs.

---

## What this is

This started as a wiki about topics. Every interest got a page, every page got a
stack of four primitives — **Context**, **Loops**, **Agents**, **Skills** — and the
whole thing was supposed to organize a fleet of agents as a well-kept markdown
vault. Markdown was the API, the filesystem was the database, and you steered by
editing files instead of config panels.

The idea was right. The unit was wrong.

A topic page is a filing cabinet. It collects links, it never comes due, and
nothing in it can be invoked. So the vault grew beautiful dashboards that nobody
executed, and every project quietly depended on a human remembering it existed.

**Bot Wiki keeps the vault and changes the unit.** A topic no longer has a page;
a topic has an owner. The bot is a directory that can be loaded, questioned,
scheduled, and held to a definition of done. Nine of them exist today, one per
project Chris is actually running — plus a tenth that maintains the method the
other nine run on.

## The agent that works on all of it

Nine projects, one conversation. The thing on the other end of that conversation is
**Senter** — personified as the three-eyed owl in Herm, backed by an unnamed,
tool-free speech-to-speech auxiliary. It is not a tenth bot and it does not hold
project state. It routes.

| Role | Who | Job |
|---|---|---|
| **Front door** | Senter | hears the request, decides which bot owns it, loads that bot, reports back in plain language |
| **Maintainer** | Klerik (`bot-wiki`) | keeps the fleet index honest, materializes missing skills, bounds its own writes |
| **Executors** | the nine bots | hold their own mission, queue, skills, and clock |

The important part is where the state lives. Nothing is remembered "in the chat":
it is in `bots/<slug>/`, on disk, in markdown. Senter can pick up any of the nine
projects cold, on any device, because resuming is a procedure — and the procedure
is written down.

### How Senter resumes nine projects

1. **Read the index.** `bots/_fleet/FLEET.md` — one row per bot: callsign, topic,
   status, live loops, blocker. The only page that claims to be current.
2. **Load one bot.** `skill: bot-<slug>`. Nine bots in context is noise; one bot
   plus the index is enough to be useful immediately.
3. **Read its `.system/`.** `continuity.md` for what it understands, `injections.md`
   for what changed since you last spoke, `queue.md` for what is owed.
4. **Respect the boundary.** Cross-bot work goes in the fleet queue. No bot edits
   another bot's `BOT.md`, and no request quietly borrows another project's asset —
   the scanner, the GPU, your hands: those are shared, and sharing is stated.
5. **One mission per exchange.** Switching projects mid-task is how you get two
   half-finished artifacts and no diagnosis.
6. **Leave a line behind.** Append to the bot's `## Log` before switching away. That
   line is the next session's only memory of what happened.

This is also why the fleet is readable at a glance: Senter's working set is the
index plus one bot, not nine dashboards. If a project is stuck, the index says so
and names the ask; if it is moving, the bot's log says what moved.

## The shift, in one table

| | Topic-first (July 2026) | Bot-first (now) |
|---|---|---|
| Unit | A page about a subject | An actor that owns a subject |
| Lives in | `topics/<topic>/` | `bots/<slug>/` |
| Front door | `README.md` dashboard | `BOT.md` mission + operating loop |
| Can it act? | only via a factory that read the page | it holds skills and a clock |
| When it decays | silently | it reports `blocked` and names the unblocker |
| In Hermes | a profile per agent, chosen by hand | a bot *is* a profile, rendered in Bot Mode |

The four primitives survived; they just got an owner. A **Bot** holds **Context**,
runs **Loops**, and loads **Skills**. That is the same nesting as before, with a
subject that can be woken up.

---

## How it organizes

```
wiki/
├── bots/
│   ├── _fleet/                  ← the only shared mutable surface
│   │   ├── FLEET.md             ← every bot: status, live loops, blocker
│   │   └── .system/             ← cross-bot queue, fleet continuity
│   ├── bot-wiki/                ← Klerik: the method, as a bot
│   ├── youtube/                 ← Cutroom
│   ├── pocketshop/              ← Binder
│   ├── turbofit/                ← TurboSouth (TurboFit support)
│   ├── kart-racer/              ← Apex
│   ├── ai-daw/                  ← Riff
│   ├── anser/                   ← Anser
│   ├── hermes/                  ← Mesh
│   └── ssi/                     ← Beacon
├── catalogs/                    ← fleet, roster, skills, loops
├── BOT_SCHEMA.md                ← what a bot must contain
├── SENTER.md                    ← the language/context layer
└── log.md                       ← append-only history
```

Every bot is the same shape:

```
bots/<slug>/
├── BOT.md                  mission · operating loop · skills · loops · holds · needs
├── .system/                continuity.md · queue.md · injections.md
├── skills/<slug>/SKILL.md  procedures, not descriptions
└── loops/<slug>.md         a skill bound to a clock
```

`BOT.md` is the only file you have to write. It carries the mission as an
outcome, the numbered loop the bot runs, the artifacts it owns, the skills it
loads, the loops it runs, the things it may never do alone, and — when stuck —
the exact ask that would unstick it. A bot that cannot act says so in one line at
the top and names what it needs.

`.system/` is dot-prefixed so file browsers hide it. Open it anyway; that is the
debugger. Front end clean, back end inspectable.

## The nine bots

| Bot | Callsign | Owns | State |
|---|---|---|---|
| bot-wiki | **Klerik** | the method: schema, fleet index, queue reconciliation | **live**, one loop at 06:00 |
| youtube | **Cutroom** | hours of Discord voice chat → chaptered videos | seeding · OBS output path |
| pocketshop | **Binder** | four boxes of MTG cards → listings → restock | seeding · scanner, eBay token |
| turbofit | **TurboSouth** | TurboFit support, plus the model × hardware matrix | seeding · Darwin, unified-dense policy |
| kart-racer | **Apex** | Unity kart racer on the NRCU cast | seeding · repo, Unity version, gamepad |
| ai-daw | **Riff** | Hermes plugin driving a music DAW | seeding · where the GPU lives |
| anser | **Anser** | Nous moderation answers, cited and dated | seeding · X read credentials |
| hermes | **Mesh** | one Hermes instance across every device | seeding · device pairing |
| ssi | **Beacon** | children's SSI and Texas benefits paperwork | **blocked** · program list + documents |

Twenty-eight skills and twelve loop specs live across them. One loop is armed;
the rest are written and waiting for a manual pass, because a loop that was never
run by hand fails silently forever.

## How a bot acts

1. **It is addressed by name.** Each bot publishes as a Hermes skill,
   `bot-<slug>`, so any session can load it and be that bot. Its `BOT.md` stays
   the long version.
2. **It follows a numbered loop.** Read state, do the one thing, validate, write
   the artifact where the BOT.md predicted it, log one line.
3. **It carries hold points.** Paying, publishing under Chris's name, submitting
   government forms, deleting data — never alone. Binder drafts listings, Beacon
   fills forms, Cutroom renders cuts; a human clicks the last button.
4. **It reports upward.** A one-line injection lands in `.system/injections.md`
   and surfaces in conversation, not on a dashboard.
5. **It is gated.** `pytest -q` and `scripts/verify_bots.py` must pass before any
   bot claims work as done. The maintainer cannot edit its own validator.

## The recursion

`bot-wiki` is a bot. Klerik reads every `BOT.md`, repairs the fleet index when it
drifts from reality, claims exactly one queue item per run, and refuses to touch
another bot's identity. On its first live run it corrected two stale blockers in
`FLEET.md` and fixed a `PYTHONPATH` bug in its own procedure — then the spec was
tightened so a maintainer may only commit `bots/**` prose, behind both gates.

That is the method describing itself: the wiki that builds the wiki, under the
same rules as everything it builds.

---

## Quick Start

```bash
git clone https://github.com/SouthpawIN/bot-wiki.git ~/.hermes/wiki
cd ~/.hermes/wiki

# Parse every bot and propose work from the markdown
python -m senter_agent . --json

# Contract tests + bot layout verification
PYTHONPATH=. pytest -q
python scripts/verify_bots.py .          # bots=9 skills=28 loops=12 problems=0

# Publish each bot as a Hermes skill (bot-<slug>)
python tools/publish_skills.py . ~/.hermes
```

Then, in Hermes:

```bash
hermes cron create "0 6 * * *" --name fleet-reconcile \
  --prompt "$(sed -n '/## Prompt/,/## Stop/p' ~/.hermes/wiki/bots/bot-wiki/loops/fleet-reconcile.md)"
```

## From wiki to runtime

A Bot **is** a Hermes profile — isolated config, memory, skills, credentials, and
chat history under `~/.hermes/profiles/<slug>/`. Bot Mode is a UI over that
primitive, so the roster in the wiki and the roster on screen are the same nine
entities. `hermes -p <slug> chat` opens the same agent the wiki describes, and
each bot's routines appear in `hermes cron list` beside its Bot Chat.

The wiki is the design doc. Hermes is the runtime. Nothing is translated by hand.

## Verification

| Check | Result |
|---|---|
| `PYTHONPATH=. pytest -q` | 69 passed |
| `python scripts/verify_bots.py .` | 9 bots · 28 skills · 12 loops · **0 problems** |
| `python -m senter_agent . --json` | 78 documents, 9 `type: bot` documents |
| Published skills | 9 × `bot-<slug>` |
| Armed loops | 1 (`fleet-reconcile`, 06:00 UTC) |

`scripts/verify_bots.py` checks identity (`type: bot`, slug matches directory),
required sections, declared skills and loops on disk, `blocked` bots having a real
ask, and every `[[wiki link]]` resolving. `INTEGRATED_STATUS.md` records what is
specified, implemented, exercised, and still blocked.

## Design principles

1. **Markdown is the API** — human ↔ machine, machine ↔ machine.
2. **The wiki is the system** — no database, no config dashboard, no YAML wizard.
3. **One bot, one topic** — two missions means two bots.
4. **Skills are procedures** — if a fresh agent cannot execute it step by step, it
   is prose and belongs in continuity.
5. **Loops name their skill** — an unbound loop is a mystery cron job.
6. **Hold points are absolute** — money, publishing, filings, deletions.
7. **`blocked` requires an ask** — a stuck bot with no ask is a dead bot.
8. **No self-edit** — the bot that writes bots cannot rewrite itself, and a
   maintainer cannot edit the validator that judges it.
9. **Dot-prefix machine internals** — `.system/` is hidden, not secret.

## Learn More

- [[BOT_SCHEMA|Bot Schema]] — the standard every bot is written against
- [[bots/_fleet/FLEET|Fleet]] — the live roster and cross-bot dependencies
- [[spec|Specification]] — full architecture, setup, history
- [[goop-whitepaper|GOOP Whitepaper v1]] — the original vision, July 2026
- [[goop-nesting|GOOP Nesting]] — primitive nesting
- [[SENTER|Senter]] — the language/context layer

---

*Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent). Towards Self-Improvement.*
