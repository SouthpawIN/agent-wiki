---
title: BRIEF.md pre-prompting layer (per-topic operating orders — scope/anti-scope, aliases, lens, standing preferences; "steering a topic = editing markdown"; announced 2026-09-05 19:26)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, infra, tool, decision, preference]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# BRIEF.md — the pre-prompting layer

**Definition.** Every topic now carries `topics/<t>/BRIEF.md`, described at 19:26 on 2026-09-05 as "the operating orders for each topic" ^[raw/inbox/2026-09-05.md]. It is the one file that steers *both* halves of the pipeline for a topic: the watcher (cutter) reads it to decide what lands in this topic's inbox, and the topic agent prepends it to its own prompt before compiling the wiki and pitching. klerik's own BRIEF defines it as "Hermes Agent meta-profile for reviewing, correcting, and spawning other agent profiles" — the same role [[topics/klerik/wiki/entities/klerik|klerik — the profile factory bot]] describes.

**Sections and what each one drives** (from the 19:26 block, verbatim where quoted) ^[raw/inbox/2026-09-05.md]:

| section | who consumes it | effect |
|---|---|---|
| *Scope / anti-scope* | the cutter | routes on it: "'how the wiki looks' → senter-wiki, 'why the system works this way' → senter". Test cuts: "'hover over the third dot' → senter-wiki .32; 'cron didn't fire, klerik had no gateway' → klerik .34." |
| *Aliases* | the cutter | "hard binds for routing (edit the list, routing changes)" |
| *Lens* | the topic agent | "how to read new cuts (what's a decision vs preference vs pain; corrections mark the old page `contested`)" |
| *Standing preferences* + *what a good suggestion looks like* | the topic agent | "applied to every pitch" |
| *## Learned* | agent-appended | the agent "appends its own learnings under `## Learned` — never touching your lines" |

**Behaviour rules it introduces.** "The agent prepends BRIEF to its prompt, re-files cuts that violate anti-scope, and appends its own learnings under `## Learned` — never touching your lines. BRIEF shows first in each card's wiki view, so steering a topic = editing markdown, which is the direction you asked for." ^[raw/inbox/2026-09-05.md] Three consequences for this topic:
1. *Re-filing is now the agent's job, not just the cutter's.* The four UI blocks that landed here at 0.06–0.09 on 2026-09-05 (see [[topics/klerik/wiki/entities/wiki-diff-mode-card-probe|Wiki diff-mode card probe]]) are exactly the class BRIEF's anti-scope names ("the wiki UI itself → `senter-wiki`"); under the new layer they get listed as misrouted rather than wikified here.
2. *Pitch discipline moves into a file Chris can edit.* The 18:53 cap ([[topics/klerik/wiki/decisions/2026-09-05-cap-topic-agent-pitching|Decision — cap the klerik topic agent's pitching]]) was a prompt tuning; BRIEF's "Standing preferences" / "What a good suggestion looks like" make the same rule visible and editable per topic, which fits the [[topics/klerik/wiki/concepts/build-process-chatter|Build-process chatter]] rule ("No pitches about the build process itself" is literally a BRIEF line).
3. *Chris's lines are protected.* Lines ending `<!-- chris -->` are never rewritten — the same convention SCHEMA.md already applies to wiki pages, extended to the operating orders.

**Why this is the direction Chris asked for.** The block ties the layer to a standing preference: "steering a topic = editing markdown, which is the direction you asked for" ^[raw/inbox/2026-09-05.md]. It matches klerik's own standing rule set — "Markdown + built-in Hermes over custom code", "Everything live and visible" — and is the first control surface where Chris tunes the fleet's behaviour without touching a SOUL.md, which is otherwise klerik's protected territory ([[topics/klerik/wiki/concepts/protected-file-guard|Protected-file guard]]).

**Routing evidence relevant to klerik.** The named test cut for this topic is "cron didn't fire, klerik had no gateway" → klerik .34 ^[raw/inbox/2026-09-05.md] — the exact root-cause sentence recorded in [[topics/klerik/wiki/concepts/gateway-was-the-missing-ticker|Gateway was the missing ticker]]. A score of .34 is above the day's live misroutes (0.06–0.09) but below the 18:58 block's 0.51; see [[topics/klerik/wiki/concepts/watcher-corpus-rebuild|Watcher corpus rebuild]] for the contested 5/5 claim this test extends.

**Open.** Whether re-filing actually moves a block's raw line to the other topic's inbox or only lists it in the agent's JSON output is not stated; only the second is observable from this topic. No `<!-- chris -->` line exists in klerik's BRIEF yet — Chris has not edited it.

**Evidence.** raw/inbox/2026-09-05.md, 19:26 `hermes ·` block — filed twice: first at sim 0.42, then again (byte-identical) at sim 0.51, tying the 18:58 block for the day's highest ^[raw/inbox/2026-09-05.md]. The rise is the layer scoring itself: the block carries the klerik test sentence "cron didn't fire, klerik had no gateway", and once BRIEF's scope/aliases entered the corpus that sentence pulled harder. The duplicate filing itself is a watcher defect, recorded in [[topics/klerik/wiki/concepts/watcher-corpus-rebuild|Watcher corpus rebuild]].

**Not yet proven live.** The one `hermes ·` block filed after the BRIEF announcement (19:22, "My probe removal only cut the first line of a multi-line probe", sim 0.06) is a Senter-wiki UI line and still landed here ^[raw/inbox/2026-09-05.md] — the anti-scope re-route works on the test cuts and, from this pass on, on the agent's re-filing side; the cutter side has no live pass yet.
