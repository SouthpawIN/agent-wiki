# vault-live.html — afternoon pass 2026-09-03: one-list sort, hover band, usage strip

Chris-driven, live in the preview pane. Every item below is his ask (quoted) → what was built → the knob.

## Sort semantics ("contextual similarity to the hero topic")
- "If I click on the orbs it will stay in topics but sort all the topics by their contextual similarity to
  evolutionary … consider the context of the entire topic, the entire file."
- Scanner (`assets/scan-topics.py`): topics carry `text` = README + `.system/context.md`; bots `text` = full
  SOUL.md; skills `text` = full SKILL.md (8k cap); loops `desc` = prompt. Regenerate: run the script once,
  then `launchctl kickstart -k gui/$(id -u)/com.senter.scanwatch`.
- Page: `SIM` = TF-IDF over the live corpus (`SIM.vec(text)`, cosine). `rankBy(items, textOf)` uses the typed
  `TERM` when present, else `ANCHOR` (pinned hero topic) → `topicDoc(anchor)` vector. Anchor row scores
  `Infinity`. `paintCaption` prints `sorted by similarity to <b>anchor</b>` + a clear ×.
- `window.HERO_PIN`: set on `pointerenter` of `#heroOrbs`; `rotateHero()` and the generic row `mouseover`
  early-return while pinned; cleared by typed search / `#rankOff`.
- Orb click → `rerenderAll()` then scroll the SECTION header inside `#view-wiki` (own scroll container):
  `view.scrollTo({top: head.offsetTop - heroHeight - 8, behavior:'smooth'})`.

## Hover band + underline ("all the way across the screen, mouse still only activates over the title")
- `.thead::before` = band: `position:absolute; left:0; top:var(--bandInset,20px); bottom:-1px; width:0;
  background:var(--surface); pointer-events:none; z-index:-1; transition:width .08s` → hover `width:100vw;
  transition:width .4s ease`. `.thead::after` = underline, same timings, `z-index:0` so it paints over the band.
- `.thead { isolation:isolate }`, `#view-wiki { overflow-x:clip }` (no horizontal scrollbar from 100vw).
- `body.idle`/`body.deadzone` hover → `width:0; transition:none` (dead zone still shows nothing).
- Knob: `--bandInset` on `.thead` (trim from top only; bottom stays on the line).

## Row anatomy now (every page, from `mkTopic`)
`[chev][title flex:1 1 auto, ellipsis][.sdots tags fixed][.usage fixed 140px, margin-left:auto][.orbs fixed 164px, flex-end]`
- Dots cell reserves hovered geometry (4×32 + 3×12) → right edge identical on every row, hovered or not.
- Hover sizes: `.thead:hover .orb {32px; 1.5em}` gap 12; title `--hfs` capped 1.5em (`orbColumn`).
- Hero: orbs 40px/1.8em gap 14 (half-group 101px in the title `max-width` calc); hero title 2.4em.
- Integration marks / GitHub octocat in rows RETIRED ("get rid of the integration symbols"). `wikiIdots()` is dead code.

## Usage strip ("GitHub usage chart … like a diffusion map … tiny dots")
- Data: `scan_usage()` in scan-topics.py → `LIVE.usage = {days:98, end, topics:{name:[98 ints]}, bots:{}, skills:{}}`,
  one int per local day = rows in `~/.hermes/state.db` `messages` whose rowid matches `messages_fts MATCH "name"`.
  Read-only sqlite (`file:…?mode=ro`). Included in the watcher's changed-keys tuple.
- Paint: `window.paintUsage()` after `live/loaded` and wrapped into `rerenderAll`; per row picks kind by
  `data-bot/data-skill/data-topic`; shows last `WEEKS=10` days×7 as `<i style="--a:…">` dots; alpha =
  `0.15+0.85*sqrt(n/rowMax)`, empty `.06`. `cell.title` = total mentions.
- CSS: `.thead .usage { flex:0 0 var(--usageW,140px); display:grid; grid-auto-flow:column;
  grid-template-rows:repeat(7,1fr); grid-auto-columns:minmax(0,1fr) }`, `.usage i {3px circle}`.
- Knobs: `--usageW`, `WEEKS`, dot size 3px.

## Dead-zone fix
`mousemove` dead test now `!closest('.hero') && clientX > __deadLeft` — the hero orbs centred on the dots
column had their two right discs inside the dead zone (labels hidden, size fought). Belt: 
`body.deadzone .hero .heroOrbs .orb::before { opacity:inherit !important }`.

## Verification recipe used
1. `python3 scripts/vault-live-check.py` (JS + CSS braces).
2. `drive_preview reload` → `hover selector=#wiki-list .topic[data-topic="kashik"] .thead` → `sleep 0.6;
   screencapture -x /tmp/x.png` → `vision_analyze` with a numbered question and approximate x asks.
3. `desktop_preview read` for order/caption text (≈24k cap — put temp readouts at the TOP of the hero).

## Open / queued
- Short titles leave air before the chart (by design: chart fixed, title flexible). Chris OK'd for now.
- "we're gonna be using the dots for one more thing" — unspecified.
- Inline hover-expand/click-to-lock markdown editor still queued; editor-hash-on-reload + Enter-while-editor-open bugs pre-existing.
