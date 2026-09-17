---
title: Senter Lessons
type: selfmodel-lessons
created: 2026-08-31
updated: 2026-08-31
---

# Lessons (each links to evidence)

1. **Bot-mode DMs cannot deliver approval prompts.** `approvals.single_query_mode=deny`
   is by design. Anything needing user approval → prepare in vault, apply in desktop
   session. *Evidence: klerik SOUL.md timeouts ×2, anser profile edits blocked.*
2. **DM pipeline can drop message bodies.** turbosovth's plan content never arrived
   despite successful dispatch; workaround = write to vault, signal only.
   *Evidence: msgs 2847/2851 in turbosovth state.db.*
3. **Voice dictation garbles proper nouns.** "server into south"=Sirvir→Southpaw,
   "teal code"=Tiel Coder. Confirm garbled nouns before routing; don't guess.
   *Evidence: TurboFit push clarification round.*
4. **Repo config sanitization (`***`) breaks YAML on install.** 33 placeholders in
   anser config.yaml → silent total override failure. Post-install: parse YAML +
   grep `\*\*\*`. *Evidence: anser boot failure 2026-08-31.*
5. **Test suites must actually run.** turbosovth's gate blocked pytest; 43 red
   surfaced only when Senter ran it. Verification = real execution, not intent.
   *Evidence: ~/turbofit pytest 2026-08-30.*
6. **Target-busy on message_agent is common** when a bot is mid-turn. Retry after
   ~2min; don't stack pings. Check state.db directly for ground truth.
