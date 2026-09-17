---
title: Model Selection Routing (O'Marki → MacBook)
created: 2026-09-15
updated: 2026-09-16
type: concept
tags: [tool, plan, question]
sources: [raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: low
---

# Model Selection Routing (O'Marki → MacBook)

On 2026-09-15 16:59 Chris stated a goal not yet acted on: he wants to be able to **select which models are served from his Oh My Archi ("O'Marki") home lab to this MacBook**. It is the newest thread in the topic and points at model-routing / selection between the remote Arch lab and the local machine.

> So I want to be able to select the models that are being served from I'm O'Markey to this MacBook. ^[raw/inbox/2026-09-15.md]

## Context

It sits at the tail of the O'Marki home-lab work — the item that pushed Chris "beyond pissed" when the USB install failed — and is the natural next step once O'Marki is serving models: deciding which of those models route to the MacBook, and how that selection is made (local serving vs. remote serving, TurboFit, or a serving gateway). The mechanism is still open.

## Model Format Compatibility (2026-09-16)

On 2026-09-16 Chris added a format-level question on top of the routing goal: he wants to know **which model formats will work on his Omarchy home lab** — now running a CUDA llama.cpp / qwen4-fork runtime. ^[raw/inbox/2026-09-16.md]

> Also a rad goes models of format that will work on my omarchy home lab then ^[raw/inbox/2026-09-16.md]

So beyond *which* models route to the MacBook, there is an open question about *what format* each model must be in to run on the O'Marki CUDA llama.cpp runtime. (The 16:17 line appears twice in the raw filing — a watcher duplicate.) See [[topics-wiki/beyond-pissed/wiki/entities/oh-my-archi|Oh My Archi]] for the runtime it must run on.

See [[topics-wiki/beyond-pissed/wiki/entities/oh-my-archi|Oh My Archi]] for the home lab it belongs to, [[topics-wiki/beyond-pissed/wiki/concepts/venv-ownership-root-cause|Venv Ownership Root Cause]] for the root-owned-venv fix that was part of the same O'Marki work, and [[topics-wiki/beyond-pissed/wiki/decisions/multi-project-order-of-operations|Multi-Project Order of Operations]] for the sequence it is part of.
