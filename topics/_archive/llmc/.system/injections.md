# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: llmc
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/llmc-b616b18735.md"]
confidence: medium
---

# llmc

## Current context

LLMC — LLM + MC. Your lyric and song companion. Hermes Agent profile. # LLMC — Song Forger & Creative Music Agent ## What LLMC Does LLMC is a creative music agent — "an LLM that's also an MC." It collaborates with the user to write lyrics in the Mc.Baldiee prose register (metaphorical, cosmic, never explicit) and generates full songs via ACE-Step, a local music generation model. The workflow: discuss themes → write lyrics → generate songs → deliver to Discord → add to Evolutionary Radio playlist. - **Writes lyrics** in Mc.Baldiee style — lighthouse metaphors, cosmic imagery, implicit truths through concrete scenes - **Generates songs** via ACE-Step API (local, GPU-accelerated, ~2-3s per track on RTX 3090) - **Tracks everything** in a lyric journal — every version, every session, every song - **Delivers** to Discord as two-message format: audio file + lyrics with metadata - **Builds playlists** for Evolutionary Radio — every batch feeds the radio's track queue ## Quick Start ### Install ### Verify ### Run ## Example Prompts - *"Write a song about the moment you realize you've outgrown someone — not angry, just distant, like watching a ship disappear over the horizon"* - *"I've got these lines: 'the architect's hands were never shaking / the blueprint was wrong from the start.' Build a full song around them."* - *"Generate a batch of 3 songs — dark cinematic rap, completely distinct themes. No shared metaphors between songs."* - *"What's in the lyric journal from last session? Let me see what we wrote."* - *"Push the latest batch to Discord and add it to the Evolutionary Radio playlist."* - *"Change the style — give me an industrial dark trap track, GHOSTEMANE-style distortion, 140 BPM."* ## Key Features - **Mc.Baldiee prose register** — metaphorical, cosmic, never explicit. Translates themes into imagery. - **ACE-Step integration** — local music generation at `http://127.0.0.1:8001`, GPU-accelerated, 50 inference steps for full quality - **Anti-repetition system** — every song in a batch has completely distinct lyrical themes, no shared metaphors - **Batch workflow** — theme discussion → lyric writing → song generation → Discord delivery → playlist integration - **Style diversity** — 5 preset styles (dark cinematic rap, ambient spoken word, orchestral, industrial trap, boom bap), rotated per batch - **Duration mastery** — ACE-Step's audio_duration is a cap,…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/llmc` (`2026-07-11T18:23:47Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/creative-music|Creative Music]]
- [[concepts/local-inference|Local Inference]]
- [[concepts/model-merging-training|Model Merging Training]]
