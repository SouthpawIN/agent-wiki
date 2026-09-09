# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: omnisenter-blog
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/omnisenter-blog-570de1b284.md"]
confidence: medium
---

# omnisenter-blog

## Current context

OmniSenter blog — a multi-stage agentic MoE with the Ohm self-evolution engine. # OmniSenter Blog The public blog for the **OmniSenter** project — a multi-stage agentic MoE with the Ohm self-evolution engine, built on Darwin Family weight-space recombination. **Live site:** https://southpawin.github.io/omnisenter-blog/ ## What's here - **13 blog posts** — the Omni Family catalog (naming, flagship, math, pipeline, concepts, integration, research) - **Master wiki** — 11 concepts + 8 entity pages, in catalog order - **9 hero images** — the cosmic-convergence concept art, the synth hero, the architecture diagram, etc. - **Auto-deploy** to GitHub Pages on every push to `main` ## Local dev ## X scheduler (posts one blog per week to @southpawin) See [`scripts/post_x.py`](scripts/post_x.py). The script: 1. Reads a queue of 13 blog posts (in publishing order) 2. Formats each as a tweet (with cosmic hero image as media) 3. Posts via the [`xurl`](https://github.com/xdevplatform/xurl) CLI 4. Marks the post as posted, so it doesn't get re-posted **First-time setup** (you, outside the agent — per the xurl skill's safety rules): **Posting manually:** **Posting on a schedule:** Set up a cron job that runs `./scripts/post_x.py post` once a week (e.g. Tuesday 9am). See `scripts/install_cron.sh` for the install command. ## Naming The naming convention used throughout is defined in [`docs/blog/the-omni-family.md`](docs/blog/the-omni-family.md): - **Omni** = multimodal native - **Senter** = Omni with the agentic core wired in - **Ohm** = the self-evolution engine - **Senter Ohm** = the flagship ~32A8B MoE (all three composited) - **OmniSenter** = the project (umbrella), also the small Senter (`OmniSenter 12B`) ## Theme Custom Nous cosmic-variant CSS (`docs/assets/css/extra.css`): - Teal/gold nebula gradients - Dark mode default (cosmic) - Light mode (paper) option - TOWARDS SELF-IMPROVEMENT badges - Share-to-X button on every post - "TOW" callout boxes ## Sibling repos - [`evolutionary-training`](https://github.com/SouthpawIN/evolutionary-training) — main project, training scripts - [`evolutionary-model-merging`](https://github.com/SouthpawIN/evolutionary-model-merging) — Darwin Family - [`multimodal-expansion`](https://github.com/SouthpawIN/multimodal-expansion) — REAP + EvoMoE - [`omnistep-fusion`](https://github.com/SouthpawIN/omnistep-fusion) — Cosmos × ACE-Step -…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/omnisenter-blog` (`2026-07-08T20:37:21Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/local-inference|Local Inference]]
- [[concepts/model-merging-training|Model Merging Training]]
- [[concepts/multimodal-voice|Multimodal Voice]]
