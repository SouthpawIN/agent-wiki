---
type: index
title: Fleet
updated: 2026-11-08
tags: [fleet, index]
---

# Fleet

Nine bots, one per topic. `bot-wiki` (Klerik) is the tenth: it maintains the
method the other nine run on. Status legend: `live` (running now), `seeding`
(skills written, loops not yet armed), `blocked` (needs a human decision).

| Bot | Callsign | Topic | Status | Live loops | Blocked on |
|---|---|---|---|---|---|
| [[bots/bot-wiki/BOT\|bot-wiki]] | Klerik | the method itself | live | 1 | — |
| [[bots/hermes/BOT\|hermes]] | Mesh | one Hermes across devices | live | 1 | devices must sign in |
| [[bots/turbofit/BOT\|turbofit]] | TurboSouth | TurboFit support + fit matrix | seeding | 0 | Darwin 125 GiB download; 8 GB card for the smoke test |
| [[bots/pocketshop/BOT\|pocketshop]] | Binder | MTG card flipping | seeding | 0 | printer, eBay token, fee + restock limits |
| [[bots/youtube/BOT\|youtube]] | Cutroom | Discord rants → YouTube | seeding | 0 | OBS output path; channel identity; whisper weights |
| [[bots/ai-daw/BOT\|ai-daw]] | Riff | music generation plugin | seeding | 0 | GPU host for ACE-Step |
| [[bots/anser/BOT\|anser]] | Anser | mod answer bot | seeding | 0 | X read credentials |
| [[bots/kart-racer/BOT\|kart-racer]] | Apex | Unity kart racer | seeding | 0 | repo name, Unity version, gamepad |
| [[bots/ssi/BOT\|ssi]] | Beacon | TX benefits paperwork | blocked | 0 | program list + documents |

## What is built, not just specified

| Bot | Working artifact | Proof |
|---|---|---|
| bot-wiki | `scripts/verify_bots.py`, `tools/publish_skills.py`, `fleet-reconcile` cron | 9 bots published as skills; loop has run and committed |
| hermes | tailnet serve of the web app + 9 bot profiles | https://hermes-vps.tail6ff78b.ts.net:8443/ → 302 to Nous OAuth; `mesh-health` armed 06:30; `hermes profile list` shows all nine |
| turbofit | 14 catalog variants + recipes + manifest + matrix | [PR #51](https://github.com/SouthpawIN/turbofit/pull/51), 936 tests pass |
| pocketshop | `restock_ev.py` decision math | [PR #2](https://github.com/SouthpawIN/pocket-shop/pull/2), 13 tests |
| youtube | `scripts/cutroom.py` render + package | 14 tests on synthetic media |
| ai-daw | `plugin/` — six `daw_*` tools, adapters, renderer | 14 tests, real audio via ffmpeg |
| anser | `scripts/corpus.py` fetch/cache/cite/refuse | 12 tests, import mode needs no credentials |
| kart-racer | Unity project at [SouthpawIN/nrcu-kart](https://github.com/SouthpawIN/nrcu-kart): 7 C# scripts + 35-character roster | 8 roster tests; `tools/check_project.py` ok; **not yet compiled** — needs a Unity editor |
| ssi | `scripts/casefile.py` intake/deadlines/review/fill | 9 tests on synthetic AcroForm PDFs |

## Cross-bot dependencies

- `hermes` (Mesh) must land before `anser` and `ssi` are pleasant: both want to
  be reachable from the phone.
- `pocketshop` and `ssi` share one physical asset: the Wi-Fi printer/scanner.
  `pocketshop` gets it for card flatbeds, `ssi` for documents. Neither may
  reconfigure it without telling the other (queue item in both).
- `turbofit` computes the local hardware budget that `ai-daw` and `youtube`
  want for local inference. TurboSouth publishes the matrix; the other two read it.

## Standing rules

- Public output says **sovthpaw**, never Chris, never Southpaw.
- Nothing spends money without a hold point satisfied.
- Every bot's `## Log` is append-only and newest-first.
