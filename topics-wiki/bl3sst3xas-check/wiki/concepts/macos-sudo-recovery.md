---
title: macOS sudo password recovery workflow
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [pain, decision, preference]
sources: [raw/inbox/2026-09-13.md]
confidence: high
---

# macOS sudo password recovery workflow

Context: Chris had forgotten his Mac login/sudo password and wanted to avoid the
full Recovery Mode recovery (Shut Down -> hold power button -> "Loading startup
options") if at all possible ^[raw/inbox/2026-09-13.md].

## The gotcha: zsh history expansion
Running `sudo -S <<< "A111s1nmym!nd"` fails with:

```
zsh: event not found: nd
```

The trailing `!` in the password triggers zsh history expansion. Disabling it and
wrapping candidates in single quotes fixes the input ^[raw/inbox/2026-09-13.md].

## The workaround
Disable history expansion, then loop candidates manually in your own terminal:

```
set +H
for pw in 'A111s1nmym!nd' 'senterdelta' 'Bl3ssT3xas!' 'Bl3ssT3xas'; do
  if echo "$pw" | sudo -S true 2>/dev/null; then echo "WORKED: ${pw:0:3}..."; break; else echo "fail: ${pw:0:3}..."; fi
done
```

This confirmed **A111s1nmym!nd** as the working password ^[raw/inbox/2026-09-13.md].

## The agent's brute-force block
The Hermes agent terminal hard-blocks `sudo -S` loops, flagging them as a
"brute-force vector" — so password tests must run **manually in Chris's own
terminal, not through the agent** ^[raw/inbox/2026-09-13.md].

## Outcome
Candidates and result: [[topics-wiki/bl3sst3xas-check/wiki/entities/sudo-password-candidates.md|sudo password candidates]]. The recovered sudo feeds a pending
[[topics-wiki/bl3sst3xas-check/wiki/decisions/tailscale-reinstall.md|Tailscale reinstall]] plan.
