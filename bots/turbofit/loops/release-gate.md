---
type: loop
slug: release-gate
bot: turbofit
schedule: "on tag"
state: spec
skill: fit-list-sync
created: 2026-11-07
---

# release-gate

Runs on a tagged release, before the artifact is published.

## Prompt

Run `fit-list-sync` and the full contract suite. Verify: catalog schema validates,
both ladders monotonic, every main variant covered, README phrases the contract
tests assert are still present (the README is generated from
`wiki-topics/turbofit/README.md` on the wiki branch — edit there, then
`tools/sync-wiki-readme.sh`). Report a single PASS/FAIL line with failing test names.

## Stop condition

Any test failure blocks the tag. No exceptions, no "known flaky" — a red gate is
the point of a gate.
