---
type: index
title: Fleet
updated: 2026-11-07
tags: [fleet, index]
---

# Fleet

Nine bots, one per topic. `bot-wiki` (Klerik) is the tenth: it maintains the
method the other nine run on. Status legend: `live` (running now), `seeding`
(skills written, loops not yet armed), `blocked` (needs a human decision).

| Bot | Callsign | Topic | Status | Live loops | Blocked on |
|---|---|---|---|---|---|
| [[bots/bot-wiki/BOT\|bot-wiki]] | Klerik | the method itself | live | 1 | — |
| [[bots/youtube/BOT\|youtube]] | Cutroom | Discord rants → YouTube | seeding | 0 | OBS output path |
| [[bots/pocketshop/BOT\|pocketshop]] | Binder | MTG card flipping | seeding | 0 | printer, eBay token, fee + restock limits |
| [[bots/turbofit/BOT\|turbofit]] | Fitment | model × hardware matrix | seeding | 0 | Darwin needs GGUF conversion |
| [[bots/kart-racer/BOT\|kart-racer]] | Apex | Unity kart racer | seeding | 0 | repo name/visibility, Unity version, test gamepad |
| [[bots/ai-daw/BOT\|ai-daw]] | Riff | music generation plugin | seeding | 0 | GPU host for ACE-Step |
| [[bots/anser/BOT\|anser]] | Anser | mod answer bot | seeding | 0 | X API credentials |
| [[bots/hermes/BOT\|hermes]] | Mesh | one Hermes across devices | seeding | 0 | device pairing |
| [[bots/ssi/BOT\|ssi]] | Beacon | TX benefits paperwork | blocked | 0 | program list + documents |

## Cross-bot dependencies

- `hermes` (Mesh) must land before `anser` and `ssi` are pleasant: both want to
  be reachable from the phone.
- `pocketshop` and `ssi` share one physical asset: the Wi-Fi printer/scanner.
  `pocketshop` gets it for card flatbeds, `ssi` for documents. Neither may
  reconfigure it without telling the other (queue item in both).
- `turbofit` computes the local hardware budget that `ai-daw` and `youtube`
  want for local inference. Fitment publishes the matrix; the other two read it.

## Standing rules

- Public output says **sovthpaw**, never Chris, never Southpaw.
- Nothing spends money without a hold point satisfied.
- Every bot's `## Log` is append-only and newest-first.
