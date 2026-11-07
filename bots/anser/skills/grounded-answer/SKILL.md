---
name: grounded-answer
description: Answer a Nous question with cited, dated, minimal claims.
version: 1.0.0
author: Anser
license: MIT
metadata:
  hermes:
    tags: [nous, qa, citations, discord, moderation]
---

# Grounded answer

## Procedure

1. **Restate the actual question** in one clause. Mod questions are often two
   questions wearing a trench coat ("is Hermes free and can I run it on my phone?").
2. **Search the corpus first** — `@NousResearch`, then `@Teknium`, newest first:
   ```bash
   xurl search '"hermes agent"' --from NousResearch --limit 20
   ```
   Then official docs (`hermes-agent.nousresearch.com/docs`, `llms.txt` index) for
   anything operational.
3. **Pick the single best source**, and note its date. A 4-month-old post about
   pricing is a liability; say "as of <date>".
4. **Answer shape** — 1–3 sentences of answer, then `Source: <url> (<date>)`.
   No preamble, no "great question", no recap of the question.
5. **Disagreement**: if Teknium and the official account conflict, give both with
   dates and say the newer/more specific one is likely current — do not silently choose.
6. **Gaps**: if nothing covers it, say "Not publicly stated" and give the closest
   real source. Never fill a gap with plausible product knowledge.
7. **Log** to `data/answers/<slug>.md`: question, answer, sources, confidence.

## Refusals

- Roadmap, unannounced features, internal metrics, revenue, headcount.
- Another user's account, order, or moderation history.
- Anything framed as "official statement" that Anser is being asked to invent.
