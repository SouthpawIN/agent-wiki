# vault-live.html — 2026-09-03 live-session batch (Chris, voice-driven)

Session id for recovery: `20260903_001447_7bc70a`.

## Nav / primitives (GOOP spec)
Context → Loops → Agents/Bots → Skills. Nav labels: WIKI · CONTEXT (routing id stays `feed`) ·
SKILLS · BOTS · LOOPS. SPACE removed from nav; the ONLY dead-zone activation is click → SPACE.
By end of session the top strip itself was retired (`#topstrip` clip-path hidden, tabs
`display:none`), player+rocker+⚙ moved into fixed `#hudCluster` top-right "above the girl's head".

## Row geometry (WIKI list)
- Order left→right: `●` · title (`.tnameWrap` > `.tname`, LOCK pill absolutely inside the wrap)
  · `.idots` (ONE GitHub svg; `data-repos="a|b|c"`; hover card lists every repo as a link)
  · `.orbs` (4 dots; rest 4×4+3×12 = 52px, hover 142px, bloom grows LEFT).
- `orbColumn()` computes: `dotsCentre=(titleRight+figLeft)/2-5`, `dotsRight=dotsCentre+26`,
  `--rowcap = dotsRight+10-rowLeft` (row box EXACT width), `--orbcol=min(widestTitle+gutter, 46% rowcap)`
  caps only the title cell. `window.__deadLeft=dotsRight` is the dead-zone boundary.
- `figLeft` = girl's fingertips from sampled wall image (`window.__figFrac`, fallback .62).
- Measurement pass holds `.orbMeasure` on `#view-wiki` for the whole read (`try/finally`);
  CSS under `#view-wiki.orbMeasure` forces rest geometry on hover-grown orbs/idots/title.
  Root cause of the original "dots snap back toward titles": class was released before rects
  were read, so a hovered row measured grown geometry.
- Second regression: after wrapping the title, `rowW` was measured from the wrap (text width)
  → 46% cap collapsed → dots clamped near titles. Measure `.thead`, not the title cell.
- Stage-1 hover (`.thead:hover`): orbs at 22px with numbers, `transition:none` (Chris: "very
  important"). Only stage-2 single-orb bloom animates.

## Lock
- `LOCKS` Set (localStorage `sw.locks`) + `wiki-topics/<t>/.system/lock.json {"locked":true}` via
  bridge `POST /write` (vault-allowlisted). `topic-similarity.py` downgrades locked pairs
  auto→propose; `merge-topics.py build_plan()` refuses plans touching a locked topic.

## Similarity calibration
Thresholds auto ≥0.50, propose ≥0.35. `name_contains(a,b)` floors sim to 0.65 (pocket-shop ⊂
pocket-shop-pricing). turbohaul vs turbofit share only token "turbo" → stay apart by construction.

## Live rows
`renderWiki(topics)` builds `#wiki-list` from `.system-live.json` newest-touched first; baked
rows remain only as offline fallback. `renderLoops` reads `wiki-topics/*/loops`. Scanner
`repos_of(readme)` collects frontmatter `repo:` + `## Repos` table rows + absorbed-topic rows
(skip `|---|` divider rows). `REPO[name]='SouthpawIN/'+repos[0]` so `wireIcons` links resolve.

## Header-as-input + whole-app search
- Composer buttons hidden; hidden textarea `#senterHiddenInput` receives keys when
  `body.heroTyping` (or legacy `zone.on`).
- Click blank space left/right of `.heroTitle` (title band, not the ink — Range rect test) →
  `_heroInput.start()`: title text swapped for typed text + `.hcaret`. Esc restores.
- Search module: >1 candidate → `#searchOverlay` `.srow` list (hover/click/↑↓/Enter); exactly
  1 → jump; 0 → Enter still sends to senter. `go()` dispatches `senter:navigated` so the
  header restores. Typing a view name (wiki/context/skills-capabilities/bots-profiles/triggers-loops/space) + Enter → `showView`.

## Right-anchored column (final geometry, batch 5)
- Row dots: `dotsRight = figLeft − 14` (fingertips minus a fixed gap; NOT band-centred any more),
  `--rowcap = dotsRight + 10 − rowLeft`. Rest 4×4+3×12 = 52px.
- Hero orbs sit ON the title line (`position:absolute; right:calc(100% − var(--dotsr))`,
  `justify-content:flex-end`), `.heroTitle` becomes inline-block with `max-width:calc(var(--dotsr) − 200px)`.
- `--dotsr` = real measured `orbsEl.getBoundingClientRect().right − hero.left` after
  `void orbsEl.offsetWidth` (flush the `--rowcap` write), then a rAF self-check: up to 2 passes of
  `Δ = heroOrbs.right − orbs.right; --dotsr −= Δ`; final Δ written to `#view-wiki[data-hero-align]`.
- Sizes (batch 6, FINAL — one expanded size): `.thead:hover .orb` = 48px / `font-size:2.2em`
  for all four; `.thead:hover .orb:hover` = same 48px, `margin:0` (no bloom — lift via the
  existing `transform:translateY(-12px)` + caption + card). Hero orbs 48px/2.2em `!important`
  permanently (base `.orb` rest is 4px/`font-size:0`), hover = `translateY(-6px)` + `::before` label.
- Optical nudge (batch 6): measured orb-to-orb Δ was 0.00 yet Chris read it a few px left →
  `#view-wiki{--heroNudge:3px}` folded into `right:calc(100% − var(--dotsr) − var(--heroNudge))`;
  `alignHero()` compares LAST hero orb vs LAST row orb (orb-to-orb, not container) and targets
  Δ = nudge (reads it via `getComputedStyle(v).getPropertyValue('--heroNudge')`). Runs on rAF +
  250ms; `window.__alignHero` re-runs it. Positive nudge = right.
- Temp readout pattern used to read Δ without JS access: page appends `#alignDbg` fixed div with
  the numbers → `desktop_preview read` shows the line → remove the div before shipping.

## Centre-anchored hero column (batch 9 — FINAL, supersedes the right-anchor + `--heroNudge` above)
Chris: "I don't like them flush with the right side — centered, exploded, equal distance on both
sides across the other dots." Then: "different titles are making the four dots move … I want
those four dots fixed in the center of the screen."
- `.heroOrbs { left:var(--dotsc); transform:translateX(-50%); justify-content:center }`.
  `--dotsc` = `(orbs.left+orbs.right)/2 − hero.left` from the REAL rest rect after
  `void orbsEl.offsetWidth`. `alignHero()` self-corrects on centres: `Δ = cx(heroOrbs) − cx(orbs)`,
  `--dotsc −= Δ`, ≤4 passes, final Δ → `data-hero-align`. `--heroNudge` is 0 / retired.
- `.heroTitle max-width = calc(var(--dotsc) − 123px − 28px)` (half the 246px group + breathing).
- **The lettering leak, root-caused:** the `#heroTitle` MutationObserver used to call
  `__alignHero` → it read `ink.right` for `#heroGap` and re-derived offsets → position drifted with
  the hovered row's title length. Fix: the observer calls `syncHeroOrbs()` ONLY (numbers); geometry
  runs only from `orbColumn()` (load / fonts.ready / `live/loaded` / resize). `#heroGap` is still
  sized from the ink but that's a hit-target, not the column.
- Proof method: hover the longest and shortest titles, `screencapture -x` each, run
  `scripts/pixel-span-diff.py A.png B.png` → disc spans byte-identical
  `[(1535,1614),(1667,1746),(1799,1878),(1931,2010)]` in both.

## Hero orbs = the nav + ranked filter (batch 4)
- `#heroOrbs` (4 `.orb`s on the `.heroTitle` line, right-aligned to the row-dots column — see above)
  replace the retired tabs. ALWAYS full size with numbers: base `.orb` has `font-size:0` and only row hover
  raises it, so hero orbs need their own `font-size:1.05em !important` or only the hovered
  one shows a number (that bug shipped once). `syncHeroOrbs()` mirrors the hero topic's
  counts; a MutationObserver on `#heroTitle` keeps it in step with hover/activity.
- Click an orb → `renderWiki(topics, {kind, anchor})`: anchor row first, all others ordered
  by `LIVE.similarity.matrix[anchor][n]`, each row body = JUST that section (CONTEXT/SKILLS/
  BOTS/LOOPS, `dim` "none" when empty). `#rankBar` caption + `×`; same orb again clears.
  `window.RANK` persists across live re-renders (`renderWiki(topics)` with rank undefined
  reuses it).
- Search term + Enter while hero-typing → `rankByQuery(term)` (section = lit orb, default
  ctx). Single-candidate auto-jump is suppressed while `body.heroTyping` so Enter decides.
- `topic-similarity.py` now emits `similarity.matrix` (full pairwise) — `pairs` only kept
  ≥0.15 and could not rank everything. `scan-topics.write()` does `live.update(snap)` so the
  `similarity` key survives watcher rewrites. TF-IDF cosines are low (0.12 top) — order is
  right, magnitudes aren't; `--provider openai` at a local embed server sharpens it.
- Chris rejected the title turning yellow while typing ("don't like how the title turned
  yellow") — accent colour `#FFE45A` is for approvals/locks/pending, never the hero title.

## Search navigation model (batch 7 — supersedes the "section = lit orb" line above)
Chris's spec, verbatim-derived: "type … hit enter → sort the wiki, the page that we're on, by
relevance to the search. Click any → open that wiki's page. Then click the context bubble → same
page but titles + context section, sorted by the context sections' relevance. Skills → sort ALL
the skills, not by their title, by relevance. Bots same. Loops same."
- `rankByQuery(q)` → `renderWiki(topics, {kind:null, query:q})`: topics, FULL rows, score =
  name + summary + skills + bots text. rankBar reads `WIKI ranked by relevance to "q"`.
- Orb click while `RANK.query` is set → RE-CUT the same query by kind (never anchor mode):
  - `ctx` → topics, score = context section ONLY (no name boost), rows show just CONTEXT.
  - `skills` / `agents` / `loops` → `renderItemRank(rank, topics)`: rows become the ITEMS
    (every `LIVE.skills` (124) / `LIVE.bots` (9) / every `topics[*].loops`), score = item's own
    text (`desc` / `role` / `name+cadence`) + 0.25×name as tiebreaker. Row click → item's own
    page (`bots` → `_clickThrough.openBot`, skill/loop → `openEditor` on the file path).
  - Same orb again → back to kind:null. `×` → clear. No query → anchor mode (unchanged).
- Deep link / verification hook: `vault-live.html#q=<term>&k=<ctx|skills|agents|loops>` runs the
  search after `live/loaded`. Kept as a deep link; NOT needed for testing any more — see
  "Driving the pane" below (batch 8 made the page element-drivable).
- Ranking logic is plain functions over `.system-live.json` → test it headless with a 30-line
  node script that reimplements `score()` against the snapshot (`node /tmp/ranktest.js`) before
  reloading the pane; that caught nothing this time but proved the item counts and orderings.
- Known thinness: only 2 loops exist and their text is name+cadence — "define loops" is an
  open conversation with Chris, not a bug.

## Driving the pane (batch 8 — Chris: "practice your computer use, not work around")
The preview pane IS the UI Chris watches; driving it by selector is driving the real thing.
Selector map and the exact sequence that passed end-to-end on 2026-09-03:

| Intent | Call |
|---|---|
| start header search (caret) | `drive_preview click selector=#heroGap` |
| type + Enter | `drive_preview type selector=#senterHiddenInput text=discord submit=true` |
| re-cut by kind | `drive_preview click selector='#heroOrbs .orb[data-k="skills"]'` (`ctx`/`agents`/`loops`) |
| open a ranked item | `drive_preview click selector='#wiki-list .topic[data-bot="anser"] .thead .tname'` (`data-topic` / `data-skill` / `data-loop`) |
| clear | `drive_preview click selector=#rankOff` |
| prove state | `desktop_preview read` (rankBar text, row order, `#bots-profiles/anser` in url) |

Page changes that made this possible (keep them):
- `#heroGap` — a real `<span>` after `#heroTitle`; `alignHero()` sets `--gapl/--gapw` = ink.right+10 →
  firstOrb.left−10 so it spans exactly the blank band. Click → `_heroInput.start()`.
- `#senterHiddenInput` is appended to `<body>` at startup and styled `left:0;top:0;1×1px;opacity:0`
  — inside the clipped `#topstrip` it was "off-screen" to element drivers and could not be typed into.
- The blank-space click handler excludes `.heroOrbs, #rankBar` (otherwise an orb click also started typing).

What NOT to do (each one cost a round): `computer_use`/`cua-driver` foreground clicks or
Escape/Enter to pid Hermes — focus is the chat composer; Escape stops the agent. Background
`cua-driver call click x,y` routes via AX (`"route":"accessibility"`) and never fires page
handlers. `get_window_state` → window `4956` is the real Hermes body (1512×949); `4988` is a
32-pt strip the driver picks by default. The 2× retina crop coordinates from `vision_analyze`
must be halved for pt.

Open nit noticed while driving: browser `back` after opening an item page leaves the editor
open (`#heroGap` still hit under it); reload to reset. Scoped close that works:
`drive_preview press key=Escape selector=#edBody` → url drops to `#bots`.

## Preview → full window + empty-Enter reset (batch 10)
- `.hero` elements carry `h.__row` — set by the generic `mouseover` on `.topic[data-overview]`
  (all live pages) and by `rotateHero()` for the wiki's `TOPICS` table (name-matched to the row).
  One document `click` on `.hero .heroOverview` → `openEditor(h.__row)` (guard: row connected +
  has `.tbody`). `.heroOverview { cursor:pointer }`. Verified: BOTS hover KLERIK → click preview →
  `#bots-profiles/klerik`, SOUL.md loaded.
- Empty `#senterHiddenInput` + Enter (hero-typing keydown, capture phase) → `TERM=null; RANK=null;
  rerenderAll(); showView('wiki')`, orbs un-lit. Verified: `#rankOff` disappears, natural order.
- Row standard, every page (mkTopic puts `.orbs` LAST): `[chev][.tname flex:1 1 auto max-width:none]
  [.sdots fixed ≤160px, clipped][.orbs = anchor]`; `.thead > *:not(.tname):not(.tnameWrap):not(.sdots)
  { flex-shrink:0 }`. Known cosmetic: `.sdots` bot/tag pills clip to nothing inside the capped row —
  planned as a hover card like the GitHub mark.
- Queued (Chris, 2026-09-03): inline editor — hover preview expands, click locks it open as a markdown
  editor per item, replacing the editor page (and its sticky `#bots-profiles/<name>` reload deep link).

## Bot messages → Hermes chat sidebar
No inject route exists in the desktop backend. Working path: `~/.hermes/scripts/senter-feed-relay.py`
(cursor-tail of bridge feed, 12 msgs/tick) run by cron `senter-fleet-feed` every 2m, `no_agent`,
`deliver=origin`. Delivery needs the gateway component running.

## Processes
- bridge: launchd `com.senter.bridge` → `launchctl kickstart -k gui/$(id -u)/com.senter.bridge`.
- scanner: launchd `com.senter.scanwatch` (`scan-topics.py --watch 20`).
- Force pane reload: `touch ~/.hermes/senter-bridge/preview-reload-needed` or `drive_preview reload`.
