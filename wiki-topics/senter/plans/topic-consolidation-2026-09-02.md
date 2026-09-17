# Topic consolidation plan — 2026-09-02
_Chris: "there's a lot of topics that could be combined… be more discriminatory about what can be combined and what needs a new topic… if it's working out of a topic, we don't have to queue things — we can spawn multiple instances and they shouldn't run into each other if they're working out of the same continuity."_

## Rule (going forward — the discriminator)
A **topic = one continuity**: one README dashboard, one `.system/{queue,session,continuity}`, one owning bot, one purpose a stranger could name in a sentence. **Repos are not topics.** A repo joins the topic whose purpose it serves; it gets a `## Repos` row, not a folder. New topic only when: (a) no existing topic's purpose covers it, AND (b) it will have its own bot or loop within a week. Otherwise it's a section in an existing README.

## Merges (63 → 17). Originals archived under `wiki-topics/_archive/<name>/` (never deleted); every merged README keeps a `## Absorbed` list with the original names + dates so nothing is lost.
| Target topic | Absorbs | Why |
|---|---|---|
| **pocket-shop** | pocket-shop-pricing | pricing is a feature of the shop |
| **turbofit** | turbohaul-llmfit, turbohaul-manager, southpaw-turbohaul, sirvir (→ turbosovth history) | all TurboFit / hardware-fit lineage; sirvir is the old bot name |
| **hermes-agent** | hermes-android, hermes-test-skill, herm-sovth, sovth-config, nous-test, test-bot, openskills | Hermes runtime, forks, configs, test scaffolds |
| **senter** | senter-consolidation, senter-archive, senter-mcp-server, senter-alignment-arxivddl, dev-orch, memento | the coordinator + its own history/tools/orchestration experiments |
| **senter-wiki** | hermes-wiki-dashboard | same product, earlier name |
| **omnisenter-models** (new name for the family) | sovthpaw-omni-senter-3b, sovthpaw-omnisenter-base-16b, sovthpaw-omnistep-12a3b, sovthpaw-omnistep-new, sovthpaw-senter-omni-data, omnistep-fusion, multimodal-expansion, flavored-nanocode, pirouette-framework-core-003 | one model-family effort split across 9 repo names |
| **evolutionary** | evolutionary-model-merging, evolutionary-training, evolutionary-radio, hermes-music-lora-pipeline, ace-step-daw, jammit | evolutionary ML + the music/audio work it feeds (radio is a consumer) |
| **nous-community** | nous-girl, nous-girl-agent, nous-discord-archive, nous-style-guide, discordsam, crow | Nous community bots-profiles/archives/style |
| **youtube** (dogeman's topic) | omnisenter-blog, southpawin-github-io, benchmark-infographics | content + publishing surfaces |
| **dev-tooling** | dev-coder, dev-review, llmc, sidecar, kashik, jestur, niwa | coding-assistant experiments; one continuity |
| **games-and-toys** | aichess, frieza, chizul, veiled, burner-phone | small standalone projects; each gets a README section, revive → own topic |
| keep as-is | anser, klerik, _global | bot topics + shared |

## How this unblocks parallelism
Each topic's `.system/` is the continuity. A bot working a topic = **one instance per queue item**, all reading/writing the same `.system/session.md` + `queue.md` with **item-level claims**: an instance appends `CLAIM <item> <pid> <ts>` to `queue.md` before starting, `DONE/BLOCKED <item>` after; instances skip claimed items. Two weavers on items A and I never collide because the claim is the lock and the file is the truth. `senter-dispatch` gains `--parallel N` per bot (default 2 for builders) and stops treating "busy" as blocking when the target supports claims.

## Weaver as a proper topic citizen
weaver's home = `wiki-topics/senter-wiki/` (context: README + spec skill; skills: agent-wiki-vault-ui, bot-verify-loop; bot: weaver; loop: `triggers-loops/verify-nightly.md` — runs assets/verify-wiki.js against the live build each night, posts regressions to the queue). Same shape for every bot: turbosovth↔turbofit, teknium↔hermes-agent, dogeman↔youtube, anser↔anser, klerik↔klerik, senter↔senter.

## Execution (routed)
1. **anser** — audit this table first (redundancy gate): confirm each merge, flag any that lose a distinct continuity, add ones I missed. Output: approved table in this file.
2. **paladin** (repo standards) — perform the merges as a script (`assets/merge-topics.py`): archive originals, create/append target READMEs with `## Absorbed` + `## Repos`, move `.system/` contents into the target's session.md under a dated heading, rewrite `[[wikilinks]]` across the vault, regenerate `index.md` + `catalogs/`. Dry-run first → post the diff summary → Chris approves once (destructive-adjacent) → run.
3. **klerik** — add the claim protocol to every builder bot's AGENTS (`## Working a topic queue`), and give weaver its loop file.
4. **teknium** — `senter-dispatch --parallel` + claim-aware busy check.

---

## Anser audit — 2026-09-02 (redundancy gate; signed)

I read every topic README to judge *continuity* (one purpose a stranger could name), not names. Grounding: most absorbed topics are DORMANT/ARCHIVED/stub repos, so archiving loses no live work — but continuity is about purpose, and several merges fuse genuinely distinct purposes. Verdict per merge below.

### (1) Merge verdicts

| Target | Verdict | Reasoning |
|---|---|---|
| pocket-shop ← pocket-shop-pricing | ✅ CONFIRM | pricing is a feature of the shop (same purpose). |
| turbofit ← turbohaul-llmfit, turbohaul-manager, southpaw-turbohaul, sirvir | ✅ CONFIRM | one hardware-fit lineage; all four are stubs; sirvir = old bot name. |
| hermes-agent ← hermes-android, hermes-test-skill, herm-sovth, sovth-config, nous-test, test-bot, openskills | ✅ CONFIRM (1 note) | all Hermes-adjacent (Android builds, TUI, configs, test scaffolds). NOTE: openskills is a standalone "skills loader for AI coding agents", not Hermes-specific — acceptable as a `## Repos` row, but dev-tooling is the more honest home. |
| senter ← senter-consolidation, senter-archive, senter-mcp-server, senter-alignment-arxivddl, dev-orch, memento | ⚠️ PARTIAL — **REJECT memento** | first five confirm (senter history/tools + dev-orch orchestration = senter's job). **memento = "a live journal you talk to (video/voice)" — a distinct consumer product, not a coordinator experiment.** Keep memento its own topic. |
| senter-wiki ← hermes-wiki-dashboard | ✅ CONFIRM | same product, earlier name. |
| omnisenter-models ← 9 | ⚠️ PARTIAL — **REJECT flavored-nanocode + pirouette-framework-core-003** | 7 confirm (model-family: omnistep fusion, multimodal expansion, the omni/omnistep stubs, data). **flavored-nanocode = "minimal Claude Code alternative" (a coding tool, not a model) → dev-tooling. pirouette-framework-core-003 = "addressable intelligence in a fractal" (a distinct framework, not a model-training repo) → its own topic.** |
| evolutionary ← evolutionary-model-merging, evolutionary-training, evolutionary-radio, hermes-music-lora-pipeline, ace-step-daw, jammit | ⚠️ SPLIT — **pull the music products out** | evolutionary-model-merging + evolutionary-training = one ML-research continuity (Darwin family) — CONFIRM those two. **ace-step-daw (DAW), jammit (terminal radio), hermes-music-lora-pipeline (music LoRA) are a distinct MUSIC continuity, not "ML research". evolutionary-radio is the bridge (OmniStep brain + ACE-Step voice) — recommend it lands in MUSIC, not evolutionary.** |
| nous-community ← nous-girl, nous-girl-agent, nous-discord-archive, nous-style-guide, discordsam, crow | ⚠️ PARTIAL — **REJECT crow** | five confirm (community bots-profiles/archive/style). **crow = "deep research agent … produces lore" — a RESEARCH continuity, not community.** Keep crow distinct (or pair with a future research continuity). |
| youtube ← omnisenter-blog, southpawin-github-io, benchmark-infographics | ⚠️ PARTIAL — **REJECT omnisenter-blog** | southpawin-github-io (personal site) + benchmark-infographics (content asset) confirm. **omnisenter-blog is about the OmniSenter MoE model, not dogeman's content → belongs with omnisenter-models.** |
| dev-tooling ← dev-coder, dev-review, llmc, sidecar, kashik, jestur, niwa | ⚠️ PARTIAL — **REJECT llmc + kashik + jestur** | dev-coder, dev-review, sidecar, niwa confirm (coding/agent dev). **llmc = "lyric and song companion" → MUSIC. kashik = "silent historian/librarian … maintains llm-wiki docs" → a documentation continuity, not a dev tool. jestur = "creative studio gremlin Discord companion" → nous-community (or creative), not a coding tool.** |
| games-and-toys ← aichess, frieza, chizul, veiled, burner-phone | ❌ REJECT as a single topic | **This is a grab-bag, not a continuity — it violates your own rule** ("one purpose a stranger could name"). aichess (chess) + veiled = games/toys ✓. frieza (Discord server-admin bot) + chizul (builder profile) are **legacy bot profiles**, not games. **burner-phone = "control an Android device with an agent" (53★, a real product) → its own topic**, not a toy. |

### (2) Merges to add / corrections

1. **Create a `music` continuity** (new topic): ace-step-daw + jammit + hermes-music-lora-pipeline + llmc + evolutionary-radio. These five are currently split across `evolutionary` and `dev-tooling`; they share one purpose ("generative music/audio products") and must not be scattered.
2. **flavored-nanocode → dev-tooling** (already folded above).
3. **omnisenter-blog → omnisenter-models** (already folded above).
4. **jestur → nous-community** (already folded above).
5. Optional but recommended: a **`legacy-bots`** archive bucket for the dormant *profile* repos that have no product continuity — frieza, chizul, (crow, kashik if you don't keep them distinct) — so "bot profile that got retired" is one continuity, distinct from "product".

### (3) CLAIM protocol — race-condition check

**Verdict: append-to-file + re-read is NOT sufficient; you need an atomic primitive.**

- The **append itself is safe**: `>>` with `O_APPEND` is atomic per `write()` on POSIX for small lines — two appends won't corrupt or interleave. So the *file* never gets mangled.
- The **check-then-act is the race**. "Read queue.md (item X free) → append `CLAIM X`" is two non-atomic steps. Interleaving **A-read → B-read → A-append → B-append** double-claims X: both instances saw X free before either wrote. This is *precisely* the same-second case the `ts` doesn't protect against — a timestamp disambiguates nothing when both claims carry the same second.
- Re-reading *after* append doesn't fix it either, unless every claimant re-reads after a settle delay and both saw *both* claims — a fragile, latency-dependent tiebreak.

**Recommended fix (cheapest correct): per-item claim via `mkdir`/`O_EXCL`.** Before starting an item, the instance does `mkdir .system/claims/<item>` (atomic on POSIX) or `open(..., O_CREAT|O_EXCL)`. First one wins; the loser gets `EEXIST` → skip. This is lock-free, per-item (no global contention), and handles same-second double-claims deterministically. Second-best: `flock` on a `.claim.lock` around the read+append (serializes, but all bots contend on one lock).

**Two additional gaps in the protocol as written:**
1. **Stale-claim reaper.** A crashed instance leaves `CLAIM X` with no `DONE/BLOCKED` — X is blocked forever. Add a lease/TTL (e.g. claim includes a heartbeat; a claim older than N minutes with no heartbeat is reaped). The plan has DONE/BLOCKED but no reaper.
2. **Keep claims out of `queue.md`.** Claims are machine state, not queue intent; interleaving them into the human-readable queue forces every reader to parse the file to know what's claimed. Use a sidecar (`.system/claims/` dir or `claims.jsonl`) so the queue stays clean and the claim store is trivially lockable.

### (4) Arithmetic note (low severity)

"63 → 17" does not reconcile. The table yields **14 final topics** (11 target rows + 3 keep-as-is), not 17 — I mapped all 63 dirs and every one is accounted for (55 absorbed + 5 existing-targets + 3 keep = 63). With my added `music` continuity it becomes 15. Please re-derive the headline count; the merge substance is what matters and I've approved it above.

### Bottom line

Approve 5 merges wholesale (pocket-shop, turbofit, hermes-agent*, senter-wiki, senter*); approve 4 with one topic pulled out each (senter−memento, omnisenter-models−{flavored-nanocode,pirouette}, nous-community−crow, dev-tooling−{llmc,kashik,jestur}); reject games-and-toys as a single continuity; split evolutionary into `evolutionary` (research) + `music` (products). Nothing is moved until this is re-confirmed against these changes.

DONE — consolidation table audited; 5 confirmed, 5 partial (with the pulled topic named), 1 rejected, 1 split + missed merges added; CLAIM protocol needs an atomic primitive (mkdir/O_EXCL) + a stale-claim reaper; "63→17" is actually 14.


## Senter re-confirm (2026-09-02) — ACCEPT anser's audit in full
Final table = anser's. Changes vs my draft: memento → own topic (consumer product); flavored-nanocode → dev-tooling; pirouette-framework → own topic; crow → own topic (deep-research); llmc → music; kashik → own topic (doc continuity); jestur → nous-community; games-and-toys DROPPED (burner-phone → own topic; frieza + chizul → legacy-bots bucket); evolutionary SPLIT → evolutionary (merging+training) + **music** (ace-step-daw, jammit, hermes-music-lora-pipeline, llmc, evolutionary-radio); omnisenter-blog → omnisenter-models. Count: anser's arithmetic stands — 63 → 15 (14 + music).

## CLAIM protocol v2 (replaces v1 — anser found the check-then-act race)
- Claims live in a sidecar: `wiki-topics/<t>/.system/claims/<item-id>/` — created with **`mkdir`** (atomic, fails if exists). Success = you own the item. Failure = skip.
- Inside: `owner` (bot, pid, host, ISO ts) and a **`heartbeat`** file touched every 60s while working.
- **Reaper:** a claim whose heartbeat is older than 10 min is stale; any instance may `rm -r` it and re-claim. Crashed instances never block an item for good.
- `queue.md` stays human-readable: append `CLAIM/DONE/BLOCKED <item> <bot> <ts>` lines as a LOG (not the lock). The directory is the lock; the line is the record.
- On finish: write `result` (done|blocked + one line) into the claim dir, then `rm -r` it after appending DONE/BLOCKED to queue.md.
- Reference shell: `mkdir "$C/$ITEM" 2>/dev/null && (echo "$BOT $$ $(date -u +%FT%TZ)" > "$C/$ITEM/owner"; touch "$C/$ITEM/heartbeat") || skip`.


## AWAITING CHRIS (2026-09-02)
Paladin's dry-run is complete and rehearsed (see `.dryrun.md`). Run command: `python3 assets/merge-topics.py --execute --approved-by chris --post`.
**Decisions needed:** (1) approve the run; (2) home for **aichess** (chess AI repo, last push Jul 2025) and **veiled** (cosmic-prose lyricist Hermes profile, Jul 2026). Senter's recommendation: veiled → music, aichess → legacy-bots.
Paladin's count correction accepted: 63 dirs → **22** (15 continuities + 8 kept-as-own + overlaps); the "15" was continuities, not directories.

## GO (2026-09-02) — Chris: 'yes on everything.' veiled → music; aichess → legacy-bots. Paladin executes with --approved-by chris --post.
