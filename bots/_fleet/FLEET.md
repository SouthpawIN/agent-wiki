---
type: index
title: Fleet
updated: 2026-11-11
tags: [fleet, index]
---

# Fleet

Nine bots: eight per topic, plus `bot-wiki` (Klerik), which maintains the method
they all run on. Status legend: `live` (running now), `seeding` (skills written,
loops not yet armed), `blocked` (needs a human decision). Verified against every
`bots/*/BOT.md` on 2026-11-11.

| Bot | Callsign | Topic | Status | Live loops | Blocked on |
|---|---|---|---|---|---|
| [[bots/bot-wiki/BOT\|bot-wiki]] | Klerik | the method itself | live | 1 | — |
| [[bots/hermes/BOT\|hermes]] | Mesh | one Hermes across devices | live | 1 | device sign-in; phone OS |
| [[bots/turbofit/BOT\|turbofit]] | TurboSouth | TurboFit support + fit matrix | seeding | 0 | Darwin 125 GiB download; an 8 GB card for the smoke test; Arete's ladder placement |
| [[bots/pocketshop/BOT\|pocketshop]] | Binder | MTG card flipping | seeding | 0 | printer IP; eBay token; fee + restock limits |
| [[bots/youtube/BOT\|youtube]] | Cutroom | Discord rants → YouTube | seeding | 0 | OBS output path; a 30-minute sample; channel identity |
| [[bots/ai-daw/BOT\|ai-daw]] | Riff | music generation plugin | seeding | 0 | GPU host for ACE-Step; plugin vs existing DAW UI |
| [[bots/anser/BOT\|anser]] | Anser | mod answer bot | seeding | 0 | X read credentials; channel list + mention policy |
| [[bots/kart-racer/BOT\|kart-racer]] | Apex | **Nous Racers** — Unity kart racer | seeding | 0 | repo visibility; Unity version; a controller to tune deadzones |
| [[bots/ssi/BOT\|ssi]] | Beacon | TX benefits paperwork | blocked | 0 | program list + documents; children's initials; any active denial |

## What is built, not just specified

| Bot | Working artifact | Proof |
|---|---|---|
| bot-wiki | `scripts/verify_bots.py`, `tools/publish_skills.py`, `fleet-reconcile` cron | 9 bots + the shared `sovthpaw-voice` skill published; loop has run and committed |
| hermes | tailnet serve of the web app + 9 bot profiles | https://hermes-vps.tail6ff78b.ts.net:8443/ → 302 to Nous OAuth; `mesh-health` armed 06:30; `hermes profile list` shows all nine |
| turbofit | 62 catalog variants + recipes + manifest + matrix | [PR #51](https://github.com/SouthpawIN/turbofit/pull/51), 936 tests pass |
| pocketshop | `restock_ev.py` decision math | [PR #2](https://github.com/SouthpawIN/pocket-shop/pull/2), 13 tests |
| youtube | `scripts/cutroom.py` render + package | 27 tests on synthetic media |
| ai-daw | `plugin/` — six `daw_*` tools, adapters, renderer | 14 tests, real audio via ffmpeg; `stem-separation` skill written 2026-11-10 |
| anser | `scripts/corpus.py` fetch/cache/cite/refuse | 12 tests, import mode needs no credentials; `faq-distill` skill written 2026-11-11 |
| kart-racer | Unity project at [SouthpawIN/nrcu-kart](https://github.com/SouthpawIN/nrcu-kart): 7 C# scripts + 35-character roster | 8 roster tests; `tools/check_project.py` ok; **not yet compiled** — needs a Unity editor |
| ssi | `scripts/casefile.py` intake/deadlines/review/fill | 9 tests on synthetic AcroForm PDFs |

## Known drift

- `ai-daw/stem-separation` and `anser/faq-distill` exist on disk but are not yet
  declared in their own Skills tables — only the owning bot edits its BOT.md.
- `hermes`: the 443 serve proxy points at `127.0.0.1:8788` (nothing listening),
  not the documented `8091`; `:9119` binds `0.0.0.0`. Recorded in its own log,
  unfixed.

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
