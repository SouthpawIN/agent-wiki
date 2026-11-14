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

Runs on a tagged release, before the artifact is published. Two stages; both must
report PASS before the tag is pushed.

## Stage 1 — contract suite

Run `fit-list-sync` and the full contract suite. Verify: catalog schema validates,
both ladders monotonic, every main variant covered, README phrases the contract
tests assert are still present (the README is generated from
`wiki-topics/turbofit/README.md` on the wiki branch — edit there, then
`tools/sync-wiki-readme.sh`). Report a single PASS/FAIL line with failing test names.

## Stage 2 — campaign coverage

`bots/turbofit/benchmark-campaign.md` is the evidence ledger: 1,165
(model × drafter × context) cells, one `- [ ]` line each, keyed by an
`<a id="…">` anchor derived from the cell title. The ladders claim what the
campaign has proven — so the gate checks the claim, not the backlog.

The backlog is expected to be large and is **not** itself a failure: 0/1,165 with
every rung labelled `candidate` is an honest release. A rung labelled `measured`
is the only thing that has to be backed by a checked cell.

1. **Count.** From the repo root:
   `checked=$(grep -c '^- \[x\]' bots/turbofit/benchmark-campaign.md)`,
   `waived=$(grep -c '^- \[-\]' bots/turbofit/benchmark-campaign.md)`,
   `total=$(grep -c '^- \[[ x-]\]' bots/turbofit/benchmark-campaign.md)`.
   Every cell must be exactly one of `[ ]`, `[x]`, `[-]`; a cell with no marker or
   a duplicated anchor is a FAIL (two rows claiming one measurement).
2. **Evidence rule.** For every rung in `references/fit-lists.json` whose `note`
   carries a numeric tok/s (or `measured: true`), the matching campaign cell must
   be `- [x]`. Match on the anchor: lowercase the cell title, non-alphanumerics to
   `-`, collapse runs. A measured rung with an unchecked or waived cell is a FAIL —
   this is the hold point *never claim a tok/s number that was not measured on
   that machine*, mechanised.
3. **Context rule.** A rung may not declare a context larger than the largest
   checked cell for its model+quant. 128K on a rung whose 128K cell is unchecked is
   `benchmark required`, not `measured`; write the rung label to match the evidence.
4. **Monotonic coverage.** Coverage never decreases between tags:
   `git show <previous-tag>:bots/turbofit/benchmark-campaign.md | grep -c '^- \[x\]'`
   must be `<=` today's count. A drop means a cell was un-checked instead of
   re-measured — find the tag that had it and restore the evidence or say why it
   was withdrawn.
5. **Waivers.** A cell that cannot be served (no hardware, no artifact, a family
   dropped) becomes `- [-]` plus one line in a `## Waivers` table in
   `bots/turbofit/matrix.md` — cell anchor, date, reason; add the section at the
   first waiver. Never delete a cell and never leave a dead one `[ ]` "because it
   might run later".
6. **Report.** One line, always:
   `coverage <checked>/<total> (+<delta> since <prev-tag>), waived <n>, measured-rung mismatches <n>`.
   Mismatches are listed by anchor.

## Stop condition

Any test failure blocks the tag. Any measured rung without a checked cell, any
coverage regression, or any duplicate/malformed campaign anchor also blocks it. No
exceptions, no "known flaky" — a red gate is the point of a gate.

The gate reads the campaign; it never edits it. Checking a cell is a serviced
measurement on real hardware, and that is a separate, deliberate act.
