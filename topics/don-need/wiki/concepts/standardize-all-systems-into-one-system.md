---
title: Standardize all systems into one system
created: 2026-09-16
updated: 2026-09-16
type: concept
tags: [plan, idea, goal, infra]
sources: ["raw/inbox/2026-09-16.md"]
confidence: high
---

# Standardize all systems into one system

On 2026-09-16 Chris stated the overarching goal in his own words: *"what we've been trying to do if you pay attention is we've been trying to connect and standardize all of my systems into one system."*^[raw/inbox/2026-09-16.md]

He frames it as a **long-running** effort ("we've been trying to"), not a one-shot — and he wants the agent to be paying attention to that arc. The concrete target he names is model consolidation: *"all my models downloaded … across all my systems, including Omarqi, which is going to be the main model server anyways."*^[raw/inbox/2026-09-16.md] So the first visible slice of "one system" is a single, unified model registry spanning the current machine, the HP, and Omarqi (the future main model server).

The thread ties together earlier don-need items:

- [[topics/don-need/wiki/concepts/session-model-autonomy|Session model autonomy]] — he wants the real model name surfaced, not hidden as `auto`.
- [[topics/don-need/wiki/concepts/turbofit-model-fallback|TurboFit missing-model fallback]] — the runtime should know its own models and fall back rather than fail.
- [[topics/don-need/wiki/concepts/freeing-disk-space-after-migration-to-hp|Freeing disk space after migrating games to the HP]] — systems are already being consolidated (games moved to the HP); models are the next target.
- [[topics/don-need/wiki/concepts/terminal-work-autonomy|Terminal-work autonomy]] — the agent does the cross-machine SSH/terminal work itself rather than pushing commands back to Chris.

**Pain / open issue:** when Chris looked at the vault he had open he reported *"I'm not really seeing any changes"* — i.e. the wiki UI is not visibly reflecting updates. That observability gap matters here, because a standardization project only works if he can watch the unified picture grow. (Build-process note; see weaver.)

See the [[topics/don-need/index.md|don-need wiki index]] for every page in this topic.
