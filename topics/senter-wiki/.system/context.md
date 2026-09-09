# Senter Wiki — context (what exists, where, how it's wired) — 2026-09-03

## Files
| Path | Role |
|---|---|
| `vault-live.html` | the app: one file, CSS + several `<script>` blocks (~450 KB) |
| `.system-live.json` | the live snapshot the page renders (topics 19 · skills 124 · bots 9 · loops 5 · usage · similarity) |
| `assets/scan-topics.py` | scanner: walks the vault + `~/.hermes/profiles/*`, emits full texts, usage series; `--watch` under launchd `com.senter.scanwatch` |
| `~/.hermes/plugins/senter-bridge/server.py` | bridge on `127.0.0.1:8643` — `/health /file /post /write /ask /events /pending`; token in `~/.hermes/senter-bridge/token` (header `X-Senter-Token`) |
| `~/.hermes/senter-bridge/events.jsonl` | the feed's event log (bot messages, approvals, tool starts) |
| `~/.hermes/state.db` (`messages_fts`) | source of the usage heat charts |
| `assets/wall-contain-1456x914-wallonly.png` | the girl; ear-cup plate centre frac (0.8282, 0.3937) |
| `topics/senter-wiki/.system/anser/` | the Anser interview: brief, transcript, verdicts (native-vs-custom) |

## Knobs (CSS custom properties on `:root` unless noted)
`--paper` (tone, cool blue-white `#dfe8f5`) · `--paperPct` (dim, 96%) · `--ringW` (1px) · `--spaceGlow` (.46) ·
`--wallInk` (girl strength) · `--volLen` (495px) · `--fadeNear/--fadeFar` on `#chat .mini` (30%/82%) ·
`--bandInset` (20px) · `--usageW` (140px) · `--heroOrbsTop` (16px) · `--eqCX/--eqCY/--eqW/--eqH` ·
`--gearSize` (30px) · `--setNudge` (40px) · `--edX/--edY` (card anchor, set by JS).

## Key functions (window.*)
`rerenderAll()` · `renderWiki(topics, rank)` · `rankBy(items, textOf, nameOf, kind)` · `usageOf(kind, name)` ·
`paintUsage()` · `orbColumn()` · `placeHud()` · `openEditor(row)` / `closeEditor(save)` · `showView(v)` ·
`secSpy()` + `SPY_LOCK` · `mmHome()` / `mmBuild()` / `mmFocus()` · `hpEq.demo(sec)` · `TERM` / `ANCHOR` / `HERO_PIN`.

## Bot ↔ wiki contract
- A bot posts progress: `POST /post {bot, text, status: working|done|blocked|needs_chris, url?}` → feed card.
- A bot needs Chris: an approval event → yellow-bordered card until decided.
- The page writes vault state (locks etc.): `POST /write {path: topics/<t>/.system/…, text}`.
- Sharing a page: `#edBar` SHARE → COPY (markdown) or SEND TO HERMES (composer).

## Open (queue)
- Anser verdicts → replace custom pieces with Hermes-native ones (see `anser/02-verdicts.md` when done).
- Fill remaining content-card buttons: LOCK, HISTORY, ASK, OPEN IN OBSIDIAN.
- Settings card build-out: appearance knobs, feed, bridge health, keys, data/regen.
- `topics/senter` vs `topics/senter-wiki`: decide merge or keep (senter = the system/fleet; senter-wiki = the UI surface).
