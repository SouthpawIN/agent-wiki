---
title: "Brute-Force Loop Termination"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [pain, tool, infra, idea]
sources: ["raw/inbox/2026-09-13.md"]
confidence: high
---

# Brute-Force Loop Termination

The agent terminal blocks certain automated loops, classifying them as "brute-force vectors." When that happens, the loop cannot be run as a scheduled/long-running agent job — the agent must run and test it manually in its own session.

## The report

> "The agent terminal blocked that — it flagged the loop as a brute-force vector. You'll need to test those yourself, manually, in your own..." ^[raw/inbox/2026-09-13.md]

## Implications

- **Scheduled/long-running loops are the thing that gets blocked.** A loop that hammers something repeatedly is read as a brute-force pattern, not as legitimate automation.
- **Manual testing is the fallback, not optional.** The agent can't delegate the blocked loop to a cron/loop; it has to drive it itself.
- **This is a Hermes-runtime guard, not a `need-telling` preference.** The blocking is infrastructure; the response is to work inside it, not to argue the policy. See [[need-telling]] and [[take-next-concrete-step]] for how the topic treats such walls.

## Related

See [[take-next-concrete-step]], [[need-telling]], and [[gaming-experience]] (where the blocked-loop question is currently live).
