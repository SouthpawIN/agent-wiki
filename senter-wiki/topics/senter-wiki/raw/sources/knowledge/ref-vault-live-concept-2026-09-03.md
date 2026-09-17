# Senter concept + term-engine implementation (2026-09-03)

Chris's own framing (also saved verbatim in `topics/senter/.system/concept.md`):

> Hermes makes Skills out of repeated asks. Context -> Skills. … Bots make sense when a
> collection of Skills requires its own continuity/learning … When a Bot has a purpose,
> naturally a Loop springs out. Context -> Skills -> Bots -> Loops (and those four dots denote
> and sort by these four objects). … ALL represented in Markdown (knowledge base, SKILLS.md,
> AGENTS/SOUL/{WHATEVER}.md, and CRON/Hook scheduling). This is a Cursor x Obsidian setup
> where everything you talk about gets captured as Topics in a wiki … Jump between topics and
> it sorts and automates them all, looking for efficiencies and reusable artifacts.

Vocabulary he fixed: **Agent** = agentic harness (Hermes Agent). **Bot** = specialised
sub-worker of that Agent (a profile with SOUL.md). **Sub-agents** = drones.

## Navigation contract (his words, condensed)
- Type in the hero title + **Enter** → WIKI page ranked by relevance to the term.
- **CONTEXT orb** → the Feed page renamed CONTEXT: every new chunk of context entering
  Hermes, tagged with the title it is most similar to, an UNSORTED area for chunks matching
  nothing, sorted by relevance to the term/title.
- **SKILLS orb** → all skills, sorted by relevance of their own text (not their titles).
- **BOTS orb** → all bots, likewise. **LOOPS orb** → all crons/webhooks/other automations,
  and which bots they automate.
- The same term carries across pages; no term → the hero topic is the term.

## Implementation map in vault-live.html
- `window.TERM` — the one active term. `rankBy(items, textOf, nameOf)` — the single scorer
  (name is a light tiebreaker only). `paintCaption(viewId, PAGE, n, term)` renders
  `PAGE N · ranked by relevance to "term" ×`; × sets `TERM=null` + `rerenderAll()`.
- `window.rerenderAll()` re-renders WIKI/CONTEXT/SKILLS/BOTS/LOOPS from `window.LIVE`.
- `renderContext()` tags `#feed .post` via `nearestTopic(txt)` — evidence-gated: topic name in
  text (+6) or ≥2 distinctive summary words (+1 each, stop-list applied); score <2 → UNSORTED
  band. Relevance text = chunk text + tagged topic's summary. A MutationObserver on `#feed`
  re-tags new posts (debounced); `live/loaded` with topics re-tags everything.
- `renderLoops()` merges `LIVE.loops` (scanner: `~/.hermes/cron/jobs.json` + every
  `profiles/*/cron/jobs.json` + hooks → name/cadence/bot/targets/desc/enabled) with vault
  `topics/<t>/loops`. `scan-topics.py` `scan_loops()`; changed-key detection includes `loops`.
- Hero orb click handler (`#heroOrbs`): `VIEW={ctx:'feed',skills:'skills',agents:'bots',
  loops:'loops'}`; sets TERM if empty, `rerenderAll()`, `showView(VIEW)`. The strip is cloned
  into the other pages' heroes as `.heroOrbsClone`; clone clicks delegate to the wiki strip's
  matching orb (`twin.click()`); `syncHeroOrbs` mirrors the numbers to clones.
- Deep link: `#q=<term>&k=ctx|skills|agents|loops` → TERM + page. Verification hook.
- `VIEWS` jump-words: `wiki, context, skills, bots, loops, space` only.

## One dot column on every page
- `orbColumn()` measures WIKI rows (other views are `display:none` → zero rects), writes
  `--rowcap/--orbcol/--dotsc` on `#view-wiki`, then mirrors the three vars onto every `.view`
  and writes `data-geom` per view as a readable self-check. A resize while another view is up
  sets a dirty flag; a class MutationObserver on `#view-wiki` re-runs `orbColumn()` when it
  shows again.
- Row CSS is `.view .thead …` (was `#view-wiki …`). `mkTopic()` emits `.orbs` LAST so the dots
  are the right anchor; `.sdots` tags sit title-side as a fixed clipped cell.
- Title cell: `flex:1 1 auto; max-width:none` (the `--orbcol` cap was removed after Chris:
  "unable to read the titles … I like all the space"); `.thead > *:not(.tname):not(.tnameWrap)
  :not(.sdots) { flex-shrink:0 }`. Measured proof on LOOPS: ROW w=564, tname flex=1/1/auto,
  orbs x=502 w=52, HERO cx=528 = DOTS cx=528.
- Deep-link caveat: `desktop_preview open …#q=&k=` arrives with the hash already rewritten by
  the app's boot → unranked. Not a test harness.
- Hero orbs: `left:var(--dotsc); transform:translateX(-50%)` (centre-on-centre); alignHero
  folds the residual of `(l+r)/2` into `--dotsc`; NOT re-run on hero-title mutation.

## Drive-and-verify sequence that proved it (drive_preview, by selector)
1. `reload` → `click #heroGap` → `type #senterHiddenInput text=<term> submit=true`
2. `click #heroOrbs .orb[data-k="ctx"]` → `desktop_preview read` (caption, tags, UNSORTED band)
3. `click #view-feed .heroOrbsClone .orb[data-k="loops"]` etc. — clones work cross-page
4. `screencapture -x` + `vision_analyze` asking for x-centres of disc group vs dot group per page;
   or `scripts/pixel-span-diff.py` for byte-identical spans across states.

## SUPERSEDED same day → ONE PAGE (final state at session end)
Chris: "instead of having different pages for context, skills, bots and loops — just use the
front wiki page and have that reorder by what we're searching for … a top wiki for Topics,
then below that sections for Skills, Bots, and Loops, all on the same list. Get rid of the
Feed/Context page entirely; the Feed is managed by the feed in the bottom corner."
- At startup an IIFE (in the hero-orbs module) moves `#skills-list`, `#bots-list`, `#loops-list`
  after `#wiki-list`, each preceded by `<div class="secHead" data-sec="<id>"><span class="secName">
  …</span><span class="secN"></span></div>`; a TOPICS header goes before `#wiki-list`.
  `view-feed/skills/bots/loops` get `.retired` (`display:none !important`).
- `showView(v)` maps `feed|skills|bots|loops → wiki`. `VIEWS` jump-words → all land on wiki.
- Orb click: `SEC={ctx:'wiki-list',skills:'skills-list',agents:'bots-list',loops:'loops-list'}`;
  sets TERM if empty, `rerenderAll()`, `showView('wiki')`, smooth-scrolls to the section head
  offset by the sticky hero height. `.heroOrbsClone` / `--dotsc` mirroring are dead code now
  (harmless; remove when convenient).
- `paintCaption(viewId, …)` now writes into the matching `.secHead .secCap` (term caption);
  counts via `countSecs()` wrapped around `rerenderAll` + `live/loaded` (NOT a subtree observer).
- `renderWiki`'s kind-filtered `renderItemRank` path is retired (sections replace it).
- Orb labels: first orb `data-label="topics"` (was context). `renderContext()` still tags the
  bottom-corner feed posts — harmless.
- Verified from DOM after "discord": TOPICS 19 (ANSER, LEGACY-BOTS, NOUS-COMMUNITY first) ·
  SKILLS 124 ranked · BOTS 9 · LOOPS 5, one scroll.

## Open items handed back to Chris
- **Inline editor (Chris asked 2026-09-03, queued, not started):** "consolidate the editor page
  so that when you mouse over the preview it will expand it. If you click on it, then it will
  lock it so the user can edit the item as it's up there … a quick markdown editor for each one
  of these items." I.e. the preview under each row title = hover → expand, click → lock open as
  an editable markdown surface (bridge `POST /write`); this replaces the separate editor page.
  Take it as its own pass.
- Tag pills (which bot a loop/skill belongs to) are clipped inside the fixed row → make them a
  hover card like the GitHub mark.
- Browser back does not close the editor page.
- LOOPS semantics still to be defined with him ("we can have a back and forth about concepts").
