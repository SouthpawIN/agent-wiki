---
name: agent-wiki-vault
description: Use when working in the user's agent-wiki Obsidian vault.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [obsidian, agent-wiki, goop, workflow, hermes]
metadata:
  hermes:
    tags: [obsidian, agent-wiki, goop, workflow, hermes]
    related_skills: [obsidian]
---

# Agent-Wiki Vault Workflow

## When to use

- The user references "the vault", "the canvas", Obsidian vault edits, or agent-wiki.
- Starting a session that touches `~/Documents/Projects/Projects`.
- Spawning async agents whose briefs live in a topic's `.system/session.md`.

The user runs an Obsidian vault as the **session canvas**, structured per their
[agent-wiki](https://github.com/SouthpawIN/agent-wiki) spec (GOOP). The vault is not just
documentation — it is the coordination layer between the user, the agent, and async agents.

## Vault path

Resolve at session start: check the memory entry, else
`~/Library/Application Support/obsidian/obsidian.json` (`vaults.*.path`), else
`~/Documents/Projects/Projects`.

## Per-turn contract (user-mandated)

1. **Read first**: `topics/<active-topic>/.system/session.md` — live state: verified steps,
   in-flight work, fix list, and the async-agent launchpad.
2. **Update every turn**: session.md (state changes) + `.system/queue.md` (new fixes/ideas)
   + `log.md` (dated one-liner). Stale canvas = broken workflow; the user checks this.
3. **Ideas verbatim**: user ideas land in `Ideas.md` quoted verbatim, then triaged with a
   framing paragraph and a status line.

## Structure (GOOP)

- `index.md` — entry; `catalogs/` (fleet-dashboard, topic-index, agent-roster, skill-registry,
  loop-registry); mirrored into `topics/_global/.system/`.
- `topics/<topic>/` — one per repo/project: `README.md` (human dashboard: facts + README
  extract), `.system/` (continuity.md, session.md, queue.md, injections.md), `skills/`,
  `agents/`, `loops/`.
- User edits ARE the steering wheel: user corrections to continuity.md are never overwritten;
  queue items `[SKILLS]/[AGENTS]/[LOOPS]/[PLUGINS]` typed by the user are actionable work.

## Async-agent launchpad

session.md carries lettered agent briefs (A, B, C…). Each brief: goal, inputs, blockers.
Launch pattern: user says "launch B and D" → delegate_task with the session doc content as
context (children see nothing of this conversation). Keep briefs self-contained.

## Layout for live watching

User likes watching vault edits live with the Hermes HUD docked at the bottom of the screen.
- Position via osascript System Events (needs Accessibility grant; ask user to click Allow).
  Obsidian top (0,25 → 1512x600), Hermes HUD bottom (0,640 → 1512x230) on a 1512x894 pt display.
- Pitfall: cua-driver focus_app/window matching misses Electron apps (Obsidian) after
  AppleScript positioning — drive positioning through `osascript` System Events instead.
- Never click macOS permission dialogs; hand them to the user.

## Pitfalls

- Web-scraped GitHub repo lists undercount; the API (`/users/<u>/repos?per_page=100`)
  returns more. Pull via API, READMEs via raw.githubusercontent (not rate-limited).
- Deep vault builds: write a Python builder script (write_file + terminal), not dozens of
  write_file calls. Verify with a walk + spot-read one topic.
- Read `references/remote-absorption-ssh.md` before any SSH-based consolidation (surveying or
  pulling Hermes data from another machine — pty password pattern, scp-vs-base64 transfer
  gotchas, async du recipe, consent gate for passwords shared in chat).

## Fleet consolidation (multi-machine absorption, validated 2026-08-28 senter→Mac)

When the user asks to absorb another machine's Hermes/files into the vault as "one source of
truth", the working shape is:

1. **Topic per effort** (`topics/<host>-consolidation/`): README.md = the survey (fleet table,
   what lives where, redundancy clusters, phase plan); `.system/session.md` = live state +
   lettered agent briefs; `.system/queue.md` = steering items (password rotation, dirty
   worktrees, cron fate). The survey IS the absorption artifact.
2. **Redundancy clusters** are the deliverable the user cares most about — enumerate dupe
   variants (e.g. repo vs repo-local vs repo-upstream vs scratch variants), record last-commit
   dates + sizes + non-git status, and propose MERGE/KEEP/DELETE per cluster for user approval.
   Never delete anything during survey.
3. **Order of pull**: memories + skills + config first (small, high value), then sessions
   manifest (index before content), then project docs. Multi-TB model weights are documented
   via their registry file (e.g. MODEL-REGISTRY.md), never pulled wholesale.
4. **Dedup execution policy varies by user mandate** — default is propose-then-approve, but on
   2026-08-28 Chris overrode it mid-run: "act without my permission … I can recover whatever
   you delete, important stuff is on GitHub." When the user grants blanket deletion authority,
   execute the matrix autonomously in recoverable form: MERGE = `cp -Rn donor/. keeper/.merged-<donor>/`
   then `mv` donor aside; ARCHIVE = plain `mv` into `_archive_<date>/`; DELETE only tiny assets;
   write a MANIFEST.md in the archive dir mapping every move. Big `cp -Rn` merges (500M+) exceed
   foreground SSH timeouts — run detached remotely with a sentinel file (`echo DONE > /tmp/status`),
   then poll.
5. **Destructive phases (wipe/reinstall) need explicit user go-ahead per phase** — a survey
   that surfaced dirty worktrees, live cron jobs, and disk-capacity data feeds that decision;
   don't start it unasked. (Exception: a mid-run blanket mandate like "act without my
   permission" transfers approval authority for that phase — see item 4.)
   `~/.hermes/config.yaml` outright (security-sensitive path); `hermes config set providers.<name>.api <url>`
   etc. works and takes nested dotted keys. Back up config first (`cp config.yaml config.yaml.bak.<tag>`).
   Switching a provider to a remote gateway = set `api` + `default_model` + per-model
   `models.<key>.model`, then verify with `hermes config get providers.<name>` + curl the gateway.

## Repo rename / fleet consolidation into Senter (2026-08-29, validated)

The GitHub org was consolidated: `agent-wiki` + `klerik` + `senter` → one repo **Senter**
(user directive: "this should combine senter, agent wiki, and klerik … replace all with
Senter"). The vault-side procedure that worked:

1. `git mv`-style topic rename: `topics/agent-wiki` → `topics/senter` (mv the dir). If a
   same-named topic already exists (old senter), archive its README as
   `fleet-orchestrator-profile.md` inside the merged topic before overwriting; same for
   klerik → `klerik-profile.md`.
2. Preserve the old topic's `.system/` under `.system/archive/<old-name>-old/` — never
   delete continuity/queue history.
3. Repoint catalogs with targeted replaces: `[[topics/klerik/README|klerik]]` →
   `MERGED into [[topics/senter/README|senter]]`, `SouthpawIN/agent-wiki` →
   `SouthpawIN/Senter`, and the status cell → `ACTIVE (consolidated <date>)`. Verify with
   `grep -rn "topics/klerik\|topics/agent-wiki" catalogs/ index.md` → must be 0 hits.
4. Update `log.md` with a dated consolidation line.
5. Repo side: clone all three shallow, merge secondary repos into `profiles/<name>/`
   subdirs of the primary, strip usage/lock state files before `git add`, commit with a
   merge-mapping table, rename the primary repo via GitHub API (PATCH `/repos/{owner}/{repo}`
   `{"name":"Senter"}` — old URLs auto-redirect). The skill keeps the name
   `agent-wiki-vault` for compatibility; treat "Senter vault" and "agent-wiki vault" as the
   same target.

Note: GitHub repo renames need a PAT with Administration scope; on a fresh Mac without
auth, prepare commits + rename commands and hand them to the user (see `github-auth`).

## vault-live.html UI surgery (the Senter wiki front-end; validated 2026-09-03)

`vault-live.html` is a single-file app (CSS + several `<script>` blocks, ~350KB) rendered in
the Hermes desktop **preview pane**, fed by `.system-live.json` (written by
`assets/scan-topics.py --watch`, now launchd `com.senter.scanwatch`) and the senter-bridge
(`127.0.0.1:8643`: `/health /file /post /write /ask /events`). Chris steers it live by voice.

**How Chris wants this class of work done (his corrections, verbatim-derived):**
- **No band-aids.** "you had a couple things interacting with each other and … you put a
  band-aid over it — I would like you to not work like that." When a visual regresses after a
  change, find the interacting cause (this session: a measurement pass reading hover-grown
  geometry; a wrapper element changing what `rowW` measured) and fix THAT — never re-nudge a
  constant on top.
- Layout rules are stated in plain geometry; encode them as one number, not iteration. E.g.
  "dots flush right, all lined up" = row box has an exact width and the dots are its right
  anchor; icons `margin-left:auto; flex-direction:row-reverse` so extras grow toward the title;
  repo-less rows get an EMPTY spacer element so nothing shifts.
- Voice cuts off mid-sentence. Ship the clear items, then close with the dangling clause
  quoted ("you cut off at '…' — waiting on the rest").
- Code comments in the file are dated and quote Chris (`/* 2026-09-03 (Chris): "…" */`).
  Keep that convention — it's how he audits intent later.
- Per-turn canvas contract still applies: append a dated line to `log.md` and tick
  `topics/senter/.system/queue.md` for every UI batch.

**Verification loop that works (no Chrome on this Mac):**
1. Extract `<script>` blocks → `node --check` (`~/.hermes/node/bin/node`) before every reload.
   **AND brace-balance the CSS** (2026-09-03 "you broke some stuff"): strip `/*…*/` from the
   `<style>` blocks and assert `count('{')==count('}')`. A python replace that ended a rule with a
   `… */\n` and no `}` swallowed every rule after it — rows rendered stuck-open with editor
   toolbars and no charts, and vision misread it as "the elements scan expanded the rows". Run
   `scripts/vault-live-check.py` (does both checks) instead of hand-typing either.
2. `drive_preview reload` → `drive_preview hover selector=…` (`#wiki-list .topic[data-topic="x"] .thead`).
   The hover result's `acted` string dumps the row's text — proves LOCK pill / icon / orb
   numbers are in the DOM without any screenshot.
3. `screencapture -x /tmp/x.png` **immediately** after the hover, then `vision_analyze` — the
   UI has a ~2.5s idle timer that reverts hover visuals, so a late capture shows "tiny dots"
   and looks like a bug that isn't there.
4. `desktop_preview read` gives the full rendered text (nav state, cluster contents, row order).
5. Vision crops on the 2x screen miss the title column easily; crop from the pane's left edge
   (~x660) or use the whole frame with a pointed question.

**Pitfalls seen:**
- A stale `scan-topics.py --watch` process kept overwriting `.system-live.json` with pre-change
  fields after the scanner was edited → check `pgrep -fl scan-topics`, kill, relaunch (now
  launchd-managed so this can't recur).
- Wrapping `.tname` in a new element broke two things at once: the row-width measurement and
  the DOM anchor `initTopic` used to move icons. Any wrapper around a measured/anchored node →
  grep for every selector that targets it.
- Preview pane cannot run arbitrary JS; the temporary-debug pattern is a readout written by the
  page itself, read back, then removed. What the readers actually surface: `desktop_preview read`
  = visible text only; `drive_preview elements` = buttons/links/labelled divs. So make the readout
  a `<button id="dbgOut">` appended to `document.body` with `position:fixed` (an `aria-label`,
  a `data-*` attr, or an element inside a hidden/collapsed hero never shows up). Dump computed
  geometry per row cell: `class{x w flexGrow/Shrink/Basis maxWidth marginLeft}` + hero/dots
  centres — that one line found the `--orbcol` clamp instantly. Re-run it on `click` (capture
  phase) so orb navigation refreshes it. Remove with a script + `assert 'dbgOut' not in s`.
- The `#q=…&k=…` hash entry point is NOT reliable from `desktop_preview open`: the app rewrites
  `location.hash` to the current view during boot, before `applyHash` runs, so the page comes up
  unranked. Drive the real path instead (click `#heroGap` → type → orb click); treat the hash as
  a human deep link to verify separately, not as a test harness.
- New UI elements reusing a base class (`.orb`, `.thead`) inherit its rest state (`font-size:0`,
  hover-only reveals). Give them explicit rest styles with `!important` or one will render
  half-right (first hero orb showed a number, the other three didn't).
- Ranking/filter features need the FULL data (pairwise matrix), not the thresholded report
  the pipeline already writes — check what the snapshot actually carries before building UI on it.
- **Pixel alignment across two elements: never trust vision for the last few px.** Chris sees
  "3 pixels off" that `vision_analyze` reports as flush. Align by MEASURING the rendered rect of
  the reference element (after flushing layout with `void el.offsetWidth`), write the CSS var,
  then in a `requestAnimationFrame` measure both again and fold the residual back into the var
  (2 passes converge). Record the final Δ in a `data-*` attribute so you can prove 0.00 instead
  of arguing with a screenshot. See the reference file, "Right-anchored column".
- **When the measured Δ IS 0.00 and Chris still sees it off, stop measuring — he is aligning
  CENTRES, not edges.** Resolved 2026-09-03: a 48px disc column "a few px left" of a 4px dot
  column went 3→7→11px right with "still off" each time; 22px = (48−4)/2 = centre-on-centre was
  "what I was looking at", and he then asked for it explicitly: "centered — exploded, extending
  out equal distance on both sides across the other dots." Rule: when two aligned elements
  differ in size, anchor the CENTRE of the group over the centre of the reference
  (`left:var(--dotsc); transform:translateX(-50%)`), self-check on `(l+r)/2` of both rects, and
  retire edge-nudge knobs — a nudge constant is a patch on the wrong anchor. Always say which way
  you moved it, in px — he misclicked a direction prompt once; a plain "now +11px right" lets
  him correct instantly.
- **Alignment geometry must never depend on lettering (Chris: "I'm worried the positioning is
  based on the lettering … different titles are making the four dots move").** He caught it by
  hovering rows: the hero title rotates on hover, a MutationObserver re-ran the alignment, and
  the pass read the title's ink rect → column drifted per title. Rule: the anchor column is
  computed from the reference geometry ONLY (row dots / figure edge), re-measured only on real
  layout events (load, fonts.ready, resize, live re-render) — a title/text mutation re-syncs
  NUMBERS, never position. Prove it with `scripts/pixel-span-diff.py` over two `screencapture`s
  taken while hovering the longest and shortest titles: the disc spans must be byte-identical.
- **Sticky header vs row stacking contexts.** Row icon stacks carry `z-index:30` so hover cards
  float over neighbours; the sticky `.hero` was `z-index:8`, so icons scrolled OVER the header
  while titles/dots (no z-index) tucked under. Any sticky/top bar in the list must out-rank every
  row-level z-index (hero → 40; fixed overlays chat 50 / search 55 / HUD 58 / strip 60 stay above).
  When adding a z-index to a row child, grep `z-index:` and check the header still wins.
- Title-vs-nav collision: derive the hero title's `max-width` from the nav geometry it must not
  hit (`dotsr + nudge − orbsWidth − breathing`) and ellipsize; Chris also accepted a one-step
  font drop (3.3→3.0em) — "shrink by one or two" means a small step, not a redesign.
- **Verify that self-checks actually ran.** A one-character typo (`querivalector`) made the
  alignment loop return early for a whole round while I reported it as working. After adding any
  self-correcting pass, read its `data-*` result back (via `desktop_preview read` on a temp
  text readout) before claiming it converged.
- **"Expanded" is a rest size, not a hover animation.** Chris: "when I hover over them they
  don't need to grow anymore … they just need to shift up and show the card." When he says the
  hovered size is the size he wants, collapse the stages: row hover → every orb at max
  (48px/2.2em) instantly; pointer on one orb → `translateY` lift + caption + card, zero size change.
  Mirror instances (hero orbs) sit at that max permanently.
- When Chris says a row of things must "line up", he means the RIGHT edge, and expansions must
  grow toward the title (left) so that edge never moves: `width +N; margin-left −N`.
- Size feedback ("bigger, lettering bigger too") applies to every instance of the class (rows AND
  hero mirror) — change both, and grep comments/constants for the old px values (22/38/142) so
  measurement code doesn't keep the stale geometry.
- Colour is a signal Chris reads: `#FFE45A` = attention (approvals, LOCK on, pending). Don't
  reuse it for typing/focus states — he rejected a yellow title immediately.
- **Chris's navigation model (superseded THREE times on 2026-09-03 — current = ONE PAGE):**
  Context → Skills → Bots → Loops, but as SECTIONS of the front wiki page, not separate pages
  ("just use the front wiki page and have that reorder by what we're searching for … a top
  wiki for Topics, then below that sections for Skills, Bots, and Loops, all on the same list.
  Get rid of the Feed/Context page entirely — the Feed is the bottom-corner feed"). ONE term
  drives the list: typed into the hero title + Enter, else the hero topic; EMPTY + Enter = plain
  wiki. The four orbs (first labelled TOPICS) = the four sections: click → re-sort to the term
  + smooth-scroll to that section header. Section headers carry live counts and the
  `ranked by relevance to "…"` caption. Sort rules unchanged: skills by own description "not by
  their title", bots by SOUL role, loops by prompt/cadence/bots. Expect this model to move again —
  when Chris restates navigation, treat the newest statement as the whole spec and re-read
  `references/vault-live-concept-2026-09-03.md` (has the history + implementation map).
- **Restructure by RE-HOMING, not rewriting.** Turning four pages into one list was done at
  startup: move the existing `#skills-list/#bots-list/#loops-list` elements under `#wiki-list`
  with inserted `.secHead` rows, mark the old views `.retired`, and map old view names → `wiki`
  inside `showView()`. Render functions, hover previews, dot geometry, editor: untouched. Two
  traps hit doing it: (a) a `MutationObserver({subtree:true})` on the list that WROTE section
  counts into that same tree looped the page ("page stopped answering") — recount from explicit
  events (`live/loaded`, wrap `rerenderAll`) and only write when the text changed; (b) an
  exception in one render (`R is not defined` in renderBots) surfaced as "live data error" in
  a DIFFERENT list because the caller's try/catch paints into the skills list — when one section
  shows an error, read the whole render chain. Also: a preview tab that "stopped answering" was
  the tab restoring a stale `#bots/<name>` editor hash, not a JS hang — `desktop_preview close`
  then `open` the bare URL before assuming a loop.
- **Fixed flex-basis on a title cell collapses it to one letter the moment a row gains another
  cell (Chris: "titles are truncated to the first letter even though there is still space").**
  The wiki rows were title+dots only, so `flex:0 0 var(--orbcol)` + a blanket
  `.thead > * { flex-shrink:0 }` looked fine; BOTS/LOOPS rows add an avatar/tag cell and the
  title was the only thing left to give. Rule: the dots are the anchor (`margin-left:auto`), the
 TITLE is the one flexible cell (`flex:1 1 auto; max-width:none` — Chris then said "I like all
 the space", so the wiki's `--orbcol` cap must NOT clamp titles on any page; a title runs to the
 gutter before the dots and ellipsizes only there), tags are a fixed clipped cell, and
 `flex-shrink:0` exempts `.tname/.tnameWrap/.sdots`. THE STANDARD ROW, every page:
 `[chev][title …flex][tags | GitHub mark, fixed][dots = anchor]`; hero = `[title][orbs centred
 on --dotsc]`. Chris asked for exactly this: "every page is going to have exactly the same layout."
 Before claiming a truncation fix, READ the computed cell widths (see the debug-readout pattern
 below) — the first fix here still left `tname{w=258 maxw=258px}` in a 564px row.
- **Geometry scoped to one view silently breaks the others.** `--rowcap/--orbcol/--dotsc` were
  set on `#view-wiki` only, so the other pages' dots sat at the title's edge. Hidden views are
  `display:none` (zero rects) — measure on the visible wiki rows, then MIRROR the vars onto every
  `.view` from the same pass; re-run when the wiki view comes back after a resize.
- Any word list that jumps to a view on typing (`VIEWS={senter:…, feed:…}`) will eat real search
  terms — "senter" is a topic. Keep only words that are not vault content (`space`, `context`).
  EMPTY title + Enter = the plain WIKI (clear `TERM`/`RANK`, natural order) — Chris's reset gesture.
- **Reuse the wiki page's machinery for every other page; never build a per-page copy** (Chris:
  "standardize and reuse elements from the front wiki page for all the other pages so you do not
  have to reinvent any wheels or get lost in redundancies"). Everything is already ONE path: rows =
  `mkTopic()+initTopic()`, previews = the generic `.topic[data-overview]` hover, nav = the cloned
  orb strip, column = one `orbColumn()` pass mirrored to every `.view`, full window = `openEditor(row)`.
  New behaviour "for every page" = one document-level handler keyed on state the shared path
  already leaves behind (e.g. each `.hero` remembers its previewed row in `h.__row`; click on
  `.heroOverview` → `openEditor(h.__row)`). If you find yourself writing `#view-bots …` and
  `#view-loops …` variants, stop — the divergence IS the bug. Remaining holdout: the wiki's
  hardcoded 5-topic `TOPICS`/`rotateHero` table (bridged, not yet folded in).
- Closing the editor from the driver: `drive_preview press key=Escape selector=#edBody` (scoped
  to the page — never a global Escape). Reload restores `#bots/<name>` and it overrides an explicit
  `#wiki` URL; Enter doesn't search while the editor is open. Both pre-existing, queued: Chris's
  next ask replaces the editor page with an inline one (hover the preview → expands; click → LOCKS
  open as a quick markdown editor for that item) — build that rather than patching the old page.
- Grep/sed pipelines with several quoted alternations trip the terminal's hardline payload block
  ("BLOCKED (hardline): command parser limit"). Use `search_files` / `read_file` for lookups and
  a `python3 - <<'EOF'` script for multi-line edits; keep shell one-liners short.
- When the preview pane can't be driven into a state (no eval; synthetic clicks hit element
  centres), add a URL-hash entry point (`#q=…&k=…`) that reaches the same code path — it doubles
  as a deep link. Test pure ranking/sorting logic with a small node script over the live JSON
  snapshot before touching the pane. **But this is a supplement, not a substitute for driving
  the real UI** — see next item.
- **Chris wants the UI actually driven, not simulated (2026-09-03: "no try again … you need to
  practice your computer use, not work around").** Resolved the same day — the WORKING method
  and the trap, in order:
  1. **The trap: the wiki lives inside the Hermes app I run in.** `computer_use` /
     `cua-driver` clicks and keys sent to pid Hermes land in *this* app: keyboard focus sits in
     the chat composer, so `type_text` typed into Chris's chat box and **Escape = Stop agent**
     — I cancelled my own run four times (shell exit 130) before seeing it. Never send global
     Escape/Enter or `delivery_mode='foreground'` to Hermes for page work. Background pixel
     clicks (`cua-driver call click … window_id=4956`) route as AX and never fire page
     handlers, so they "succeed" and do nothing.
  2. **The working method: make the page element-drivable, then drive it by selector with
     `drive_preview`.** Blank-space hit targets must be real elements (`#heroGap` beside the
     hero title, geometry set by the alignment pass); hidden inputs must be on-screen and
     outside any clipped/`pointer-events:none` container (`#senterHiddenInput` moved to body,
     1px). Then: `click selector=#heroGap` → `type selector=#senterHiddenInput text=… submit=true`
     → `click selector=#heroOrbs .orb[data-k=skills]` → `desktop_preview read` to prove the
     result. This IS driving the real pane Chris is looking at (the preview is the UI); it
     satisfied him. Hash-URL entry points and node scripts over the JSON are supplements only.
  3. If a click "lands" but nothing happens, check what ELSE the handler filters: the hero-orb
     click fell through to the blank-space handler until `.heroOrbs, #rankBar` were excluded.
  4. Full drive recipe + selector map: `references/vault-live-ui-2026-09-03.md`, "Driving the pane".
- When a foreground command keeps dying with exit 130 and no error, suspect **your own input
  hitting your own host app** before suspecting the tool. Run the suspect call detached
  (`nohup … > /tmp/x.json &` then poll) to separate "the driver hangs" from "I got killed".

- **Paint ≠ hit area (Chris 2026-09-03: "the underline and black bar go all the way across
  the screen into the dead zone, but the mouse should only activate over the title like it is
  now").** Extend visuals with `::before/::after { pointer-events:none; width:100vw }` on the
  row (`isolation:isolate`, `overflow-x:clip` on the scroll view), never by widening the box.
  Animate both pseudo-elements with the SAME property (`width 0→100vw .4s ease`) when he says
  "go together"; a 1px seam between band and underline = overhang the band `bottom:-1px` and
  z-order the line above it. Thickness tweaks are one knob (`--bandInset`, trimmed from the
  TOP so the band still touches the underline).
- **"Doesn't jump" = reserve the GROWN geometry at rest.** Every cell that grows on hover
  (dots 4→32px, title 1.25→1.5em) gets its hovered width as its rest width (`flex:0 0 164px`
  dots cell, right-aligned inside) so neighbours never move; charts/strips are FIXED width
  pushed against the dots (`margin-left:auto`) so all rows share both edges (Chris: "aligned
  on their right sides"). "Shrink everywhere" = one pass over every instance of the class
  (row dots, hero orbs, hero title, hover title cap) + the constants that mirror them
  (half-group width, `--tw`, `orbColumn` cap).
- **Orb click must PIN the hero topic.** Rows brushed on the way to the orb strip rotate the
  hero, so the sort anchored to the wrong topic. `pointerenter` on the strip sets `HERO_PIN`
  (rotateHero/mouseover early-return); typed search or `#rankOff` clears it. The wiki list is
  its OWN scroll container (`#view-wiki {height:100vh; overflow-y:auto}`) — scroll IT, not
  `window`, or "click the orb does not jump to the section". The dead-zone rule must exclude
  `.hero` (`mousemove` `closest('.hero')`) or the right-hand hero orbs lose labels/size.
- **Similarity = whole-document TF-IDF cosine, not keyword hits** (Chris: "consider the context
  of the entire topic … the entire file"). Scanner emits full `text` (README+context.md, SOUL.md,
  SKILL.md; loops = prompt); page builds `SIM.vec` over the live corpus; anchor topic → Infinity.
  Watch `rank`-null paths: `rank.anchor` inside a loop threw when `score` was set without `rank`.
- Usage/heat strip data = `~/.hermes/state.db` `messages_fts` per day per name (`scan_usage`,
  98-day series, page shows last `WEEKS=10`, 3px circles — Chris: "I like the dot element, tiny
  dots"). Add every new snapshot key to the watcher's changed-keys tuple or it never refreshes.
- `desktop_preview read` caps ~24k chars — debug readouts appended to `body` at the bottom are
  unreadable on long lists; `prepend` them to `#view-wiki .hero` instead.
- A black `screencapture` = display asleep while Chris is away; fall back to `desktop_preview read`.

- **Pin overlays to the wallpaper's DRAWN rect (contain/centre, `WALL_AR`), never the viewport**
  — same math as `orbColumn()`. Locate features on the asset with a tight `vision_analyze` crop
  (pixel "largest pale square" scans grab hair, not the headphone plate). Nudges Chris asks for
  in px convert to fractions of the drawn size (2px ≈ 0.0011 w / 0.0017 h).
- **"They look gray, not black" on his black/white ink wallpaper = opacity or anti-aliasing,
  not z-order.** Idle-state opacity (with nothing playing every dot is idle) and sub-4px circles
  both read gray. Rule for anything drawn over the girl: solid `#000`, `opacity:1`, ≥4px, and
  express level/state by SIZE or presence, never by translucency. Don't chase z-index first.
- **"The feed" = the bottom-corner `#chat .mini .msg` / `#stream .msg`, not `.post`** (the
  retired Feed page). Grep the class actually rendered before restyling.
- URL query flags (`?eqdemo`) are stripped by the pane like `#q=`; a demo/debug trigger must be a
  visible fixed `<button id=…>` clicked via `drive_preview`. Say a demo "runs for N seconds" — "N
  seconds from now" reads as a delay.

- **Fixed-position widgets on a shared axis (gear over player): container `inset:0` with NO
  transform** — a transformed ancestor becomes the containing block for `position:fixed` children
  and they land nowhere near their vars. Old positioning rules on the moved widget (`position:
  relative; transform; left`) need `!important` overrides. Axis math = same wallpaper drawn-rect
  formula as `orbColumn()`; align the meaningful glyph (play ring), not the widget box.
- **Vision "element not present" is a crop error until proven otherwise.** The preview pane is
  narrower than the screen; three crops at x>1700 "found nothing" while the HUD sat at x≈1100.
  First move on any "missing" verdict: dump the element's `getBoundingClientRect()` into a fixed
  `<button>` and read it via `drive_preview click` (the `acted` string echoes the text). One round.
- Rest-state fades on the corner feed are one `mask-image` on the stack, and Chris pushes them
  HARDER once he knows hover = solid — never soften a fade he said he liked.

- **Hand-placement mode (Chris's idea, 2026-09-03, worked first try): when px-by-voice stalls,
  make the widgets draggable/resizable and let him place them.** Temp `<script>`: `position:fixed`
  + pointer capture (drag = move, white corner grip = `scale()`), click suppressed in capture
  phase, a fixed readout box of the numbers to bake (line y, centre x, top/bottom, gaps, axis Δ).
  Disable the auto-placer while it's on. **DO NOT RELOAD while he is positioning** — a reload
  wiped his placement twice ("you're jumbling all around"); read the readout by screenshot +
  vision (it sits past the 24k `desktop_preview read` cap), then bake on "go" and strip the layer.
  Recipe + readout code: `references/vault-live-hud-place-2026-09-03.md`.
- **Before baking positions, find every OTHER writer of that element's style.** `placeHud` set
  the gear/player and a pre-HUD `alignCluster()` (still scheduled on resize/mutation) re-wrote
  them after — DOM said media t132 while the bake said t105. `grep -n "<id>.*\.style\.\|getElementById('<id>')"`
  and retire the old writer; then prove with a rect readout, not a screenshot.
- **A function defined but never scheduled is the quietest bug here.** The `placeHud` scheduling
  line was lost TWICE to python `s.replace(...)` patches that swallowed the line after the target
  (`runs=0` in the readout while `typeof fn === 'function'`). Keep an invocation counter
  (`window.__xRuns++`) in every layout pass and read it back after each patch; when replacing a
  line, assert the neighbour line still exists.
- **Font glyphs can't be centred in a disc (⚙ ink sits low-left in its em box, caps at ~34px).**
  When Chris says "centre it and make it bigger" about an icon character, swap it for an inline
  SVG (its bbox IS its ink) sized by `--gearSize` inside the disc; nudges become purely optical.
- **SPACE star map is navigable** ("no way to get back to the wiki"): canvas takes pointer only
  while `body.space` (MutationObserver on body class), hit-test in world space (inverse CAM),
  labels draw for the hovered star only, hub → `showView('wiki')` + `scrollTop=0`, star → scroll
  `#view-wiki` to that topic row (`offsetTop − hero height`) and flash `.rankAnchor`.

- **"Hover/click does nothing" on a full-screen canvas = an empty sibling view is on top.** `#view-senter`
  (z5, empty `100vh` div) sat over the star canvas (z1) and ate every pointer event in SPACE. Before
  writing hit-testing, list the fixed/absolute siblings by z-index; in the mode where the canvas IS
  the page, lift it (`body.space #mindmap { z-index:6; pointer-events:auto }`) and make the empty view
  `pointer-events:none`. Exclude the canvas from the dead-zone click handler or a star click re-opens SPACE.
- **A wrapper installed before its target exists never attaches** (`const _rr=window.rerenderAll; if(_rr) …`
  ran ~50 lines before `rerenderAll` was defined → `paintUsage` never re-ran and the usage charts
  vanished on every re-render; Chris: "I'm not seeing the usage dots … those were pretty locked in").
  Call the hook from INSIDE the target function (and after any direct render call), not via a
  monkey-patch that depends on script order.
- **Active orb = the section under the hero** (scroll-spy on `#view-wiki`, last `.secHead` above the
  hero line wins), drawn INVERSE: `background:transparent; box-shadow:0 0 0 2px #fff inset; color:#fff`.
  Arrow keys: ↑/↓ move a `.thead.kbd` cursor (same paint as hover + `mouseover` dispatch so the hero
  follows), ←/→ click the neighbouring orb (keeps the sort), Enter opens the editor, mousemove clears.
  Guard: skip when typing in an input with text, in SPACE, or with `#view-editor.on`.
- **SPACE hides the chrome**: `body.space #chat, #intRail, #hudCluster { display:none !important }`.
- **Cleanest DOM readout = `document.title`.** Every `drive_preview` result (`click`, `elements`,
  `hover`) echoes the page `title` in full, while `acted` strings truncate (~80 chars) and
  `desktop_preview read` caps at 24k. For any geometry proof set
  `document.title='X rect='+[...]` from a temp handler (e.g. on the element's own click, or
  `setTimeout` after the pass), then call `elements max=1` — one round, no screenshot, no vision.
  Strip the hook afterwards (`assert 'TEMP-' not in s`).
- **Hollow = selected/rest, solid = hover/active — one ring knob.** Chris's inverse recipe for
  any circle that mirrors the row dots (active hero orb, gear): `background:transparent;
  box-shadow:0 0 0 var(--ringW) #fff inset; color:#fff` (glyph/number white), hover → solid
  `#fff` + black glyph. `--ringW` (1px, "thinner") lives on `:root` so every hollow circle
  changes together — he compares them side by side.
- **Editor is a hover CARD over the wiki, not a page** (Chris 2026-09-03). Same `#view-editor`
  DOM + `openEditor/closeEditor/edSave` path; only presentation changed: `position:fixed` black
  card, 1px white border (feed-card style), anchored under `#heroOverview` via `--edX/--edY`,
  `showView('editor')` leaves the wiki view ON. States: hover overview → *peek* after 160ms
  (toolbar hidden); click overview/card → *pinned* (editable); pointerdown outside → close +
  SAVE. Trap hit: `.peek { pointer-events:none }` made the card vanish the instant the pointer
  left the overview — the peek must be hoverable and close only when the pointer is outside
  BOTH overview and card (two `over*` flags; close on the next frame — Chris rejected a 260ms
  grace as "delays half a second"). The pointerdown that closes a pinned card is swallowed with
  one-shot capture eaters so the page underneath doesn't get that click. Details:
  `references/vault-live-editor-card-2026-09-03.md`.
- **Every open path of a card must set the SAME state the click-off guard keys on.** The guard checked
  `.pinned`, but only the overview click set it — row click / Enter / star / deep link opened the card
  un-pinned, so click-off fell through to the dead-zone handler and opened SPACE behind the card. Set
  the canonical state inside `openEditor()` itself (locked by default; the hover-peek path downgrades
  right after), and make the guard fire on "card is open" rather than on one sub-state.
- Hero orb numbers are the HERO TOPIC's per-lane counts; the section header `.secN` is the section
  total. When a lane looks empty ("LOOPS 0") read `#<lane>-list .topic` count before touching data.
- **Modal-ish overlays vs the scroll-spy: LOCK the spy during programmatic jumps.** Orb click /
  ←→ set `SPY_LOCK=k` (spy paints that key), released 160ms after the last `scroll` event (700ms
  fallback if nothing scrolls). Plain wheel scrolling keeps location-based highlighting. Chris:
  "they're kind of fighting each other … temporarily disable the location-based highlighting".
- **Hover = keyboard focus** ("have my mouse over this pane and be able to use the arrows"):
  `document.body.tabIndex=-1`; on `pointermove`, if the active element isn't an input/textarea/
  contenteditable, `window.focus(); body.focus({preventScroll:true})`. OS-level app focus is
  outside the page's control — say so once rather than promising.
- SPACE blank click (no star/hub hit) → `showView('wiki')`; stars/hub keep their own actions.
- **"Only X needs to change" = touch only X and do not reload if he is mid-placement.** After
  the hand-placement round he said "nothing else needs to be moved but the gear icon" — the fix
  was CSS-only on the glyph; a reload there would have been read as "jumbling" again.
- Feed expanded (`#chat.open`) out-ranks EVERYTHING incl. a pinned editor card: z-index 80
  (HUD 58, card 70), and `body:has(#chat.open) #hudCluster { display:none !important }` removes
  the player+gear while it's open (Chris: "the media player is still visually in the way"). Drive
  both off the feed's existing `open` class so they cannot desync.
- Shell `$(grep …)` command substitution inside `sed -n` also trips the hardline block —
  `search_files` for the line number, then `read_file offset=…`.
- **Demo videos: full screen, Hermes sidebar INCLUDED** (Chris: "the sidebar is part of it — it's a
  cursor-style setup"). Recipe in `references/vault-live-demo-video.md`: temp `<script>` that feeds the
  REAL event pipeline (re-add `window.__senterHandle=(e)=>handle(e)` inside the bridge IIFE — it
  was stripped with the demo buttons on 2026-09-03 → feed cards, approval cards, star pulses),
  `hpEq.demo()`, a drawn-cursor row sweep for the hover cascade, editor open/close, SPACE round-trip;
  record with `screencapture -v -V <sec> -x ~/Desktop/x.mov &`, then `drive_preview click #demoGo`.

- **"I'm in nowhere / the back room" = zero views on.** The gear sits in the right-hand dead-zone
  band, so its click ALSO hit the dead-zone handler → `showView('senter')` → `#view-senter` no longer
  exists → every `.view` lost `.on` and the page went blank behind the settings dimmer. Three rules,
  all now in the file: (1) dead-zone `mousemove` + click exclude `#hudCluster, #warnMask, #view-editor`
  (chrome and cards are never dead space); (2) `showView()` must never return with no view on — missing
  target → fall back to `view-wiki`; (3) any overlay's close path lands on the wiki explicitly. Diagnose
  with the `document.title` readout: `body=deadzone views= viewWikiDisp=none` told the whole story in one
  round where three screenshots had not.
- **Settings is a CARD too, same contract as the editor card.** `#warnMask.settings` is a layout shell
  only (`background:transparent; pointer-events:none; z-index:90`), the `.warn` inside is `pointer-events:
  auto; background:#000` (1px white border inherited), anchored under the gear (`--setY/--setR` from the
  gear rect) and stretched left to the hero underline's x (`--setL` from `#heroLine`) plus `--setNudge`
  (Chris dialled 10 → 40px by feel — keep it a knob). Click-off = a `document` capture `pointerdown`
  listener installed on the next tick (the shell no longer receives events) that ignores `.warn` and
  `#navSettings`, closes, and swallows that press with one-shot eaters. Chris: "settings should not make
  everything else go black … overlay everything instead of making everything else hide."

- **Tone complaints ("cream", "doesn't match the girl", "is there a filter over it?", "gray bar")
  are MEASURED, never eyeballed: `screencapture -x`, stdlib PNG decode, histogram the region.** The
  whole tone system is ONE knob, `--paper` (cool blue-white), that every CSS `#fff` and every palette
  role resolves to; the wallpaper is the picture used as a LUMINANCE MASK over a flat `--paper` fill
  (stacked twice for strength), so her ink is literally the paper colour. Recipe, pitfalls (filter
  order vs blend, element background leaking below a `contain` image = the "gray bar", neutral grey
  reads WARM next to blue-white, whole-page `filter` dims the star canvas) and the measuring
  script: `references/vault-live-palette.md`. Do NOT soften the diagonal mask when he complains about
  tint — mask = approved fade; tint = colour variables. Keep `.approval` out of any white-border rule
  so `#FFE45A` survives (rule order matters).
- **A CSS-var knob that "does nothing" = an inline style wins.** JS `el.style.cssText='…opacity:.22'`
  on the star canvas overrode `--spaceGlow` silently. Before adding a knob, `grep` the element id for
  `style.` / `cssText` writers and move the value into the stylesheet var.
- **Offline fallback rows on screen = a `<script>` threw before `loadLive`.** Boot-time calls must not
  touch a `const` declared later in the file (TDZ throws even inside `typeof`); the star camera boot
  (`mmHome()` reading `CAM`) killed live rendering that way. After any top-level insert, reload and
  check the first row is a LIVE row (`drive_preview elements max=3`).
- **One camera framing for the star map.** `mmHome()` (the SPACE framing) is used at boot, behind the
  wiki, on unfocus and on resize — never let one view set a camera the others don't reset
  ("it sits higher after I visit SPACE and stays there" = two framings).
- **Arrow keys own navigation everywhere; Shift+arrow is the caret.** Register the arrow handler on
  `window` in the CAPTURE phase with `stopImmediatePropagation` — the composer's handlers swallow
  arrows otherwise, so ←/→ only worked with the hero input focused. Pause only in SPACE or with a
  pinned card. Scroll-spy for the LAST section: when `scrollTop+clientHeight>=scrollHeight-2`, the
  last visible `.secHead` wins (a short final section never scrolls under the hero, so ←→ to LOOPS
  "fell back" to BOTS). Hover-focus: grab on `pointerenter` and re-assert every ~150ms of `pointermove`.
- **Default list order = usage, highest first; typed search = relevance; orb pin = similarity.** One
  `usageOf(kind,name)` (same series the heat chart paints) feeds `rankBy` and the topics sort so chart
  and order can never disagree. The `ranked by …` caption bar is gone for good (Chris: unasked-for).
- **Content-card bottom bar (`#edBar`)**: SHARE → part toggles (context/skills/bots/loops) + COPY
  (markdown bundle: title, path, sections) + SEND TO HERMES (`hermes.send`). Hidden while peeking.
  New card buttons go here (queued: LOCK via bridge `/write`, HISTORY from log.md, ASK, OPEN IN
  OBSIDIAN); verify COPY with `pbpaste`.
- **Volume rocker as a page-level control** (Chris trial, kept): track length is `--volLen` (495px, top
  anchored to the player so only the bottom moves; hit-zone height derives from it). While `#media.volOpen`
  or `.drag`, a `document` capture `wheel` listener (`passive:false`) owns the wheel — volume moves, the
  list does NOT scroll; hidden → wheel is the list's again. Direction INVERTED at his request (scroll
  down = louder); sensitivity proportional to `deltaY` and capped (he tuned 3% → 1.5% → 2.2%/event —
  `Math.max(-.022,Math.min(.022,deltaY*0.0006))`). Scope trap: inside the radio IIFE the player is `m`,
  not `media`. Gear toggles the settings card (open → click again closes); no CLOSE button — click-off closes.

**MVP checkpoint 2026-09-03 ~20:40** — Chris: "the UI is at a good enough spot that we can start
working on the back end." Demo buttons (`#demoGo`, `#hpEqDemo`) and the `__senterHandle` hook are
removed; `window.hpEq.demo(sec)` and `window.senterDemo` recipe remain callable/re-addable. Treat UI asks
from here as polish, not redesign — verify with the `document.title` readout, not screenshots.

## Backend phase — working procedure (every turn from here)

1. **Use the product while building it.** Post progress into the wiki's own feed as you work:
   `curl -X POST http://127.0.0.1:8643/post -H "X-Senter-Token: $(cat ~/.hermes/senter-bridge/token)"
   -H 'Content-Type: application/json' -d '{"bot":"senter","status":"working|done|blocked|needs_chris","text":"…"}'`.
   Auth is the `X-Senter-Token` header (or `?token=`), NOT `Authorization: Bearer` — a 401
   `{"error":"token"}` means the header name, not the token. Chris test-drives between turns; the corner
   cards are how he sees you working.
2. **Native before custom.** Before writing any new backend piece (watcher, message bus, registry,
   evidence store), ask the `anser` profile what Hermes already ships and VERIFY read-only
   (`hermes <cmd> --help`, `list`). One-shot: `hermes -p anser -z "<q>. Plain text, no MEDIA, no TL;DR —
   internal fleet conversation." --no-restore-cwd` (~15 s). Anser's SOUL forces Discord TL;DR+MEDIA
   unless told otherwise. For a full interview, delegate a subagent with the brief file path, one
   capability per turn, transcript + verdict table written as it goes
   (`topics/senter-wiki/.system/anser/`), plus a blunt "claimed but did not verify" list — Anser
   hallucinates features.
3. **The wiki documents itself — as ROWS Chris can see, not as a report.** Findings from research
   (interviews, audits, plans) land in the four lanes of the topic they belong to: per-item
   `loops/<name>.md` (H1 `# Loop: <name> (owner: <bot>)`, `## Cadence`, `## Status` — the scanner
   turns these into LOOP rows even before a cron exists), `agents/README.md`, `skills/`, and a section
   in the topic README so its hero overview says what the topic IS. Durable knowledge goes in
   `topics/<t>/.system/{concept,rules,context}.md` (concept = the model; rules = Chris's standing
   corrections as numbered law; context = files/knobs/functions/contracts) — the scanner folds
   `concept/rules/context/continuity/hermes-native-map.md` into the similarity text, never
   `session.md`/`queue.md` (100k+, churn). A `.system/` file alone is invisible in the UI; if he says
   "I only see one line", the fix is lane files + README, not more .system prose. After writing,
   confirm in `.system-live.json` that the topic's `text` contains a phrase from the new file and
   that the new loops appear in `loops[]`; if not, the scanner's include list or the 40k text cap is
   the bug, not the watcher. Then `drive_preview click #heroOrbs .orb[data-k=loops]` + a
   `document.title` readout of `#loops-list .topic` count to prove the rows render.
4. **Restarting the scan watcher** (`launchctl kickstart -k gui/$(id -u)/com.senter.scanwatch`) needs
   Chris's approval each time (kills running agents) — batch scanner edits and restart once.
5. Topic split: `senter` = the fleet/system (process, lessons, orchestrator); `senter-wiki` = the UI
   surface. Keep them separate.
6. **Unasked-for UI elements get removed, not restyled.** "That's an element I never asked for" → delete
   it outright; never hide it behind another widget or dim it.

Settings-card conversion + the dead-zone → blank-page root cause:
`references/vault-live-settings-card-2026-09-03.md`.

Details, selectors and knobs for the 2026-09-03 afternoon pass (one-list sections, hover band,
usage strip, sort semantics): `references/vault-live-hover-usage-2026-09-03.md`. Evening pass
(headphone EQ geometry + true-black lesson, hover cards retired, feed card restyle):
`references/vault-live-eq-feed-2026-09-03.md`. Late pass (HUD gear/player axis via `placeHud`,
feed diagonal mask): `references/vault-live-hud-2026-09-03.md`.

See `references/vault-live-ui-2026-09-03.md` for the concrete geometry, the header-as-input
module, the search overlay, and the bot→chat relay design. `scripts/pixel-span-diff.py`
(stdlib-only PNG decode) prints the white-disc x-spans in a horizontal band of one or more
screenshots — the way to PROVE two UI states place an element at the same pixels when vision
says "looks aligned" and Chris says it moved.

## Parallel agents on one git repo (validated 2026-08-27, 4-agent fan-out)

- Branch checkout races are real: agent B committed on agent A's branch mid-flight and had
  to move its own commit. Prevent it: instruct each child to create its own
  `git worktree` (e.g. `~/repo-<branch>`) up front, or accept post-hoc repair.
- Two agents independently "fixing" the same failing test produce conflicting merge
  conflicts (each encodes its interim understanding as assertions). Resolution rule:
  keep assertions describing the POST-fix behavior of the combined change, drop both
  agents' interim reasoning comments.
- After merging child branches, re-run the combined test suite yourself — each child only
  proved its own subset (72 combined vs 45/24 individually).
- Children note "tests fail" for environment reasons (missing PYTHONPATH=src). Verify
  their claims before trusting failure reports; the fix may be invocation, not code.
