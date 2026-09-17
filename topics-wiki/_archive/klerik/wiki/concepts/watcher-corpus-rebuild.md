---
title: Watcher corpus rebuild (routing corpus from disk, inbox excluded, name aliases; 5/5 test cuts — 2026-09-05 18:58)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [infra, spec, tool]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
contested: true
---
# Watcher corpus rebuild

**Definition.** The watcher is the component that cuts what Chris says into topics and files each block into that topic's `raw/inbox/` ([[topics-wiki/klerik/wiki/decisions/2026-09-05-per-message-inbox-filing|per message, like Cursor]]). Its routing corpus — the text it compares each utterance against — was rebuilt on 2026-09-05: "corpus rebuilt from disk (README + SCHEMA + continuity + wiki pages, inbox excluded so senter can't swallow everything) + name aliases." ^[raw/inbox/2026-09-05.md]

**Why the inbox is excluded.** If inbox text were part of the corpus, a topic that already receives a lot (senter) would match more and receive still more — a feedback loop that makes one topic swallow everything. Building only from the curated layers (README, SCHEMA, continuity, compiled wiki pages) means a topic's pull is proportional to what has been *understood* about it, not to how much has been dumped in it. This is also why writing good wiki pages here directly improves whether future klerik utterances land in this topic.

**Name aliases.** Chris dictates; the fleet's names arrive mangled ("Claire/cleric" for klerik, "Riever" for weaver, "tectium" for teknium, "answer" for anser). Aliases in the corpus make those route correctly.

**Test.** "5/5 test cuts route correctly (turbofit .42, video → youtube .29, rocker → senter-wiki .31, kid's soccer → nothing fits → new subject)." ^[raw/inbox/2026-09-05.md] The last case is the important one: a genuinely new subject scores below every topic and becomes a new topic rather than being forced into the nearest one.

**Post-rebuild misroute (19:10–19:20, contested).** Within 25 minutes of the "5/5 test cuts route correctly" claim, four blocks about the Senter wiki UI — card edge 684 vs chat 698, diff-mode proof, Chris's side-chat gap ruling, 256 headings / gap 4px — were filed into klerik at similarity 0.06–0.09 ^[raw/inbox/2026-09-05.md]. None mentions klerik, profiles or SOUL files. The likely mechanism: no topic scored above the new-subject floor either, and klerik was the least-bad match rather than a good one. `contested: true` on the 5/5 claim: it held for the five test cuts, not for the next live cuts. Details in [[topics-wiki/klerik/wiki/entities/wiki-diff-mode-card-probe|Wiki diff-mode card probe]]; the one Chris ruling it carried is preserved in [[topics-wiki/klerik/wiki/decisions/2026-09-05-close-side-chat-content-gap|Decision — close the side-chat ↔ content gap]].

**Second-generation routing: BRIEF.md (19:26).** Twenty-five minutes after the misroutes, routing gained a layer on top of the corpus: each topic's `BRIEF.md` scope/anti-scope and alias list now feed the cutter — "'how the wiki looks' → senter-wiki, 'why the system works this way' → senter" — with two fresh test cuts: "'hover over the third dot' → senter-wiki .32; 'cron didn't fire, klerik had no gateway' → klerik .34." ^[raw/inbox/2026-09-05.md] Both test sentences are of the exact kind that mis-cut at 19:10–19:20 (UI vs klerik root-cause), so this directly targets the contested case above; still a test result, not yet a live-traffic one. Full description: [[topics-wiki/klerik/wiki/concepts/brief-pre-prompting-layer|BRIEF.md pre-prompting layer]].

**Double filing after the BRIEF reload (19:26 ×2, contested).** The 19:26 block exists twice in klerik's inbox, byte-identical, once at sim 0.42 and again at sim 0.51, with an unrelated 19:22 block (`hermes ·`, sim 0.06, "My probe removal only cut the first line of a multi-line probe") filed *between* them — so the inbox is no longer in time order ^[raw/inbox/2026-09-05.md]. Reading: the watcher re-scored the same message after its corpus reloaded (the BRIEF layer it announces raised klerik's pull from .42 to .51 — the block contains the klerik test sentence "cron didn't fire, klerik had no gateway") and filed it as new instead of recognising it as already filed. Consequences: (a) the inbox is not idempotent per message — the [[topics-wiki/klerik/wiki/decisions/2026-09-05-per-message-inbox-filing|per-message filing]] rule needs a per-message identity, not just a timestamp; (b) the 19:22 block is a fifth UI misroute at 0.06, *after* the BRIEF anti-scope was in place, so the anti-scope fix is not yet proven on live traffic either. `contested: true` stays. Corpus-side mechanics belong to `senter`; only the effect on this topic's inbox is recorded here.

**Relevance to klerik.** Every block in this topic's inbox before 19:10 is `hermes ·` with similarity 0.08–0.51; the klerik-shaped words ("profile", "SOUL", "protected-file guard") are what route them here. The 18:58 block scored 0.51, the highest of the day — the corpus now recognises klerik's domain from klerik's own wiki. Cross-ref: [[topics-wiki/klerik/wiki/concepts/topic-agent-all-pass|Topic-agent --all pass]]; noise control on the output side: [[topics-wiki/klerik/wiki/concepts/build-process-chatter|Build-process chatter]].
