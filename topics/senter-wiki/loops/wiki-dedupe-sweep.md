---
type: loop
name: wiki-dedupe-sweep
schedule: 30m
proposed: 2026-09-05 18:39
---
# wiki-dedupe-sweep
owner: paladin · cadence: after each com.senter.topic-wiki tick (every 15m, gated on a compile having written) · status: LIVE
**Two compiles over the same raw left 17 same-subject page pairs in senter-wiki — want paladin to sweep every topic's wiki after each compile and fold duplicate slugs together, keeping every citation and every <!-- chris --> line?**

## Prompt
For each topic compiled this tick: compare page titles + sources lists within each wiki section; for same-subject pairs keep the slug index.md/other pages link to most, fold the other's unique quotes and ^[raw/…] into it, delete the loser, rebuild index.md, log '## [date] dedupe | …'. Never drop a citation or a <!-- chris --> line; undated decision slugs merge into the dated one. Post one feed card per topic with pairs merged.

## Evidence
> senter-wiki: 55 pages — 25 entities … 18 concepts … 8 decisions
> wiki/queries/duplicate-page-candidates.md: 17 pairs e.g. hud-cluster vs hud-cluster-gear-player-rocker, keep-senter-and-senter-wiki-separate undated vs dated

## Applied 2026-09-05 18:56
`hermes -p paladin cron create "30m" --name wiki-dedupe-sweep` → ok
Created job: 9e70db5cfa27
  Name: wiki-dedupe-sweep
  Schedule: every 30m
  Workdir: /Users/sovthpaw/Documents/Projects/Projects
  Next run: 2026-09-05T19:26:31.901612-05:00
