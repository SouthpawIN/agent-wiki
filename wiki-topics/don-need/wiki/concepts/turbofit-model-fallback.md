---
title: TurboFit missing-model fallback preference
created: 2026-09-13
updated: 2026-09-14
type: concept
tags: [idea, tool, preference]
sources: ["raw/inbox/2026-09-13.md"]
confidence: high
---

# TurboFit missing-model fallback preference

Chris told TurboFit to "think of itself": when a configured model "doesn't exist," it should "fall back to auto to like the main model," the way "ornith [does] the title generation as well." He called it "the fucking shit" and "You should be thinking of yourself."^[raw/inbox/2026-09-13.md]

The preference is that the runtime should never hard-fail on a missing model — it should detect the gap and silently substitute a working default (auto / the main model), mirroring the ornith title-generation fallback pattern.^[raw/inbox/2026-09-13.md]

This is a builder directive for turbosovth, not a build-process note: it's a behaviour TurboFit should own. Related cleanup idea: [[freeing-disk-space-after-migration-to-hp|freeing disk space after migrating games to the HP]]. See the [[wiki-topics/don-need/index.md|don-need wiki index]] for every page in this topic.
