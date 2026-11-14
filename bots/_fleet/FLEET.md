---
type: index
title: Fleet
updated: 2026-11-14
tags: [fleet, index]
---

# Fleet

Nine bots: eight per topic, plus `bot-wiki` (Klerik), which maintains the method
they all run on. Status legend: `live` (running now), `seeding` (skills written,
loops not yet armed), `blocked` (needs a human decision). Verified against every
`bots/*/BOT.md` on 2026-11-14: status and live-loop count are read from each
BOT.md's frontmatter and its own Loops table; "Blocked on" compresses that bot's
`## Needs from Chris`, never invents one. Both `live` loops are backed by real
cron jobs, not just declared state — `fleet-reconcile` at `0 6 * * *` and
`mesh-health` at `30 6 * * *`, both in the `default` profile with this wiki as
workdir. A loop whose BOT.md says `live` with no job behind it is an index bug.

| Bot | Callsign | Topic | Status | Live loops | Blocked on |
|---|---|---|---|---|---|
| [[bots/bot-wiki/BOT\|bot-wiki]] | Klerik | the method itself | live | 1 | — |
| [[bots/hermes/BOT\|hermes]] | Mesh | one Hermes across devices | live | 1 | device sign-in; phone OS; whether the MacBook keeps a local TurboFit node role |
| [[bots/turbofit/BOT\|turbofit]] | TurboSouth | TurboFit support + fit matrix | seeding | 0 | Darwin 125.3 GiB download decision; Arete on the unified ladder; an 8 GB card for the smoke test |
| [[bots/pocketshop/BOT\|pocketshop]] | Binder | MTG card flipping | seeding | 0 | printer IP; eBay token; fee + restock limits |
| [[bots/youtube/BOT\|youtube]] | Cutroom | Discord rants → YouTube | seeding | 0 | OBS output path; a 30-minute sample; channel identity |
| [[bots/ai-daw/BOT\|ai-daw]] | Riff | music generation plugin | seeding | 0 | GPU host for ACE-Step; plugin vs existing DAW UI |
| [[bots/anser/BOT\|anser]] | Anser | mod answer bot | seeding | 0 | X read credentials; channel list + mention policy |
| [[bots/kart-racer/BOT\|kart-racer]] | Apex | **Nous Racers** — Unity kart racer | seeding | 0 | repo visibility; Unity version; a controller to tune deadzones |
| [[bots/ssi/BOT\|ssi]] | Beacon | TX benefits paperwork | blocked | 0 | program list + documents; children's initials; any active denial |

## What is built, not just specified

| Bot | Working artifact | Proof |
|---|---|---|
| bot-wiki | `scripts/verify_bots.py`, `tools/publish_skills.py`, `fleet-reconcile` cron | 9 bots + the shared `sovthpaw-voice` and `wifi-scanner-control` skills; loop has run and committed |
| hermes | tailnet serve of the web app + 9 bot profiles | https://hermes-vps.tail6ff78b.ts.net:8443/ → 302 to Nous OAuth; `mesh-health` armed 06:30; `hermes profile list` shows all nine |
| turbofit | 62 catalog variants + recipes + manifest + matrix; `release-gate` specs campaign coverage | [PR #51](https://github.com/SouthpawIN/turbofit/pull/51), 936 tests pass; 1,165-cell campaign is the evidence ledger for every `measured` rung |
| pocketshop | `restock_ev.py` decision math | [PR #2](https://github.com/SouthpawIN/pocket-shop/pull/2), 13 tests |
| youtube | `scripts/cutroom.py` render + package | 27 tests on synthetic media |
| ai-daw | `plugin/` — six `daw_*` tools, adapters, renderer | 14 tests, real audio via ffmpeg; `stem-separation` skill written 2026-11-10 |
| anser | `scripts/corpus.py` fetch/cache/cite/refuse | 12 tests, import mode needs no credentials; `faq-distill` skill written 2026-11-11 |
| kart-racer | Unity project at [SouthpawIN/nrcu-kart](https://github.com/SouthpawIN/nrcu-kart): 7 C# scripts + 35-character roster | 8 roster tests; `tools/check_project.py` ok; **not yet compiled** — needs a Unity editor |
| ssi | `scripts/casefile.py` intake/deadlines/review/fill | 9 tests on synthetic AcroForm PDFs |

## Known drift

- `ai-daw/stem-separation` and `anser/faq-distill` exist on disk but are not yet
  declared in their own Skills tables — only the owning bot edits its BOT.md.
  Open since 2026-11-10 and 2026-11-11; the validator counts them (33 skills) but
  neither bot's published skill lists them, so the procedure exists and is
  unreachable from the bot that owns it.
- `ssi`: the program inventory the fleet queue still lists as missing to-do work
  is already written into `bots/ssi/BOT.md` (six programs, first form each,
  2026-11-07). What is missing is Chris's per-child status, not the list — the
  queue row was reworded on 2026-11-13 rather than left to read as unstarted.
- `hermes`: the 443 serve proxy points at `127.0.0.1:8788` (nothing listening),
  not the documented `8091`; `:9119` binds `0.0.0.0`. Recorded in its own log,
  unfixed.
- `bots/_fleet/skills/*` (`sovthpaw-voice`, `wifi-scanner-control`) is not
  installed by `tools/publish_skills.py`, which renders `bots/*/BOT.md` only.
  Queued; needs a `tools/` change Klerik may not make.
- `.system/` is gitignored, so queues and injections are per-clone state. The
  clone at `~/.hermes/wiki` carried none on 2026-11-12; the maintainer edits
  `~/work/agent-wiki` and mirrors them. Two clones, one queue, is a fork waiting
  to happen — worth making `.system/` tracked or fixing the mirroring.
- Both clones were corrupt again at the 2026-11-13 run: five zero-byte loose
  objects in `~/.hermes/wiki`, `HEAD` unreadable, no working tree. The documented
  repair (delete only 0-byte objects, `git fetch`, `git reset --mixed
  origin/main`, `git checkout -- .`) restored both with nothing lost —
  `43ea9aa` on `main`. The corruption is not a one-off: the cron job's workdir is
  the clone it is repairing, so an interrupted run damages its own checkout
  first. Nothing in the wiki can prevent that; only a worktree the job does not
  share (or a re-clone step at the start of the run) can.
- `pocketshop` ↔ `ssi` flatbed arbitration is one table in
  `bots/_fleet/skills/wifi-scanner-control` (07:00–19:00 cards, 19:00–07:00
  documents, `deadline-watch` outranks both). It is written but unpublished —
  same `publish_skills.py` gap as below — so neither bot's installed skill
  contains it yet.

## Cross-bot dependencies

- `hermes` (Mesh) must land before `anser` and `ssi` are pleasant: both want to
  be reachable from the phone.
- `pocketshop` and `ssi` share one physical asset: the Wi-Fi printer/scanner.
  `pocketshop` gets it for card flatbeds, `ssi` for documents. Neither may
  reconfigure it without telling the other (queue item in both). The runtime
  contract between them is `bots/_fleet/skills/wifi-scanner-control`.
- `turbofit` computes the local hardware budget that `ai-daw` and `youtube`
  want for local inference. TurboSouth publishes the matrix; the other two read it.

## Standing rules

- Public output says **sovthpaw**, never Chris, never Southpaw.
- Nothing spends money without a hold point satisfied.
- Every bot's `## Log` is append-only and newest-first.
