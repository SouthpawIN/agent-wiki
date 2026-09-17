---
title: Context fallback threshold (>65K) requires auxiliary.compression pin
created: 2026-09-08
updated: 2026-09-08
type: decision
tags: [decision, infra, hermes-config, fallback, hysteresis]
sources: [raw/inbox/2026-09-07-from-anser.md, raw/inbox/2026-09-07-from-hermes-agent.md]
confidence: high
---

# Context fallback threshold (>65K) requires auxiliary.compression pin

**The claim.** Anser (2026-09-07 00:35): *"Use Nous cloud fallback for contexts >65K"*

**The problem.** This fallback threshold is theoretical — Hermes compression timeouts prevent reaching it in practice. The rule cannot be exercised until `auxiliary.compression` is explicitly pinned.

**Chris's context.** From 2026-09-07 raw: *"context compression timed out without reducing this conversation. No messages were dropped."* Evidence of `/compress` timeout not message loss.

**Root cause.** The `auxiliary.compression` setting controls when compression runs and how hard it tries. When set to `auto`, compression may timeout before reaching the >65K threshold, causing no fallback to occur. The fix: pin `auxiliary.compression` to a specific value or strategy that ensures the threshold is reachable.

**Decision.** This is a Hermes CLI configuration concern; the fix belongs in senter's profile config, not in turbofit inference code. The profile's `config.yaml` should have:

```yaml
auxiliary:
  compression:
    # Pin to avoid auto-timeouts that prevent >65K threshold
    strategy: "aggressive"
    max_time_s: 30
  fallback:
    providers:
      - name: nous
        condition: "context_tokens > 65000"
```

**What's blocked.** Without this fix, large context runs stay on the local model past the point where cloud fallback would be faster/lower-cost. Vision credits have shown similar fallback needs.

**Action.** Verify the current `auxiliary.compression` setting in the `senter` profile, then pin it before relying on the >65K fallback threshold.

**Related.** [[wiki-topics/senter/wiki/entities/anser|anser]]; [[wiki-topics/senter/wiki/entities/senter|sebter]]; [[wiki-topics/senter/wiki/concepts/nous-managed-gateway|Nous managed gateway]]; config/fallback ordering.

^[raw/inbox/2026-09-07-from-anser.md]