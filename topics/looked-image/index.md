# looked-image — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-07 | Total pages: 10

## Entities
- [[topics/looked-image/wiki/entities/131k-optimization-target|131K optimization target]] — An explicit size/resource constraint introduced by Chris for an unnamed artifact.^[raw/inbox/2026-09-07.md]
- [[topics/looked-image/wiki/entities/memory-shard|Memory shard]] — A Chris-coined term for a surviving local copy that can be used to reconstruct a desired state after something went wrong.
- [[topics/looked-image/wiki/entities/screenshot-2026-09-05-4-38-59-pm|Screenshot 2026-09-05 4.38.59 PM]] — Visual content of this file was not successfully analyzed for this compile, so this page records known provenance and Chris’s use of it as a target reference.

## Concepts
- [[topics/looked-image/wiki/concepts/visual-revert-target|Visual revert target]] — A concept introduced by this topic: restore a broken or incorrect state by reference to a known-good visual artifact instead of verbal description.

## Decisions
- [[topics/looked-image/wiki/decisions/recovery-before-recreation|Recovery before recreation]] — When a state has diverged from a known-good screenshot, the first action is to search for a local memory shard; only if no shard exists should the state be rebu
- [[topics/looked-image/wiki/decisions/research-optimization-before-rebuild|Research optimization before rebuild]] — When an artifact must meet a size/resource target, prefer researching applicable optimization flags or quantization paths before rebuilding.
- [[topics/looked-image/wiki/decisions/revert-or-recreate|Revert-or-recreate decision]] — Prefer reverting to a known good visual state when possible; if revert is not possible, recreate it to match the screenshot.

## Comparisons
- [[topics/looked-image/wiki/comparisons/131k-abstract-vs-stafford-douglasal|131K abstract vs Stafford-Douglasal]] — The 131K target is not yet pinned to one definition. It appears first as a generic artifact constraint, then as a local benchmark at Stafford-Douglasal Science 

## Queries
- [[topics/looked-image/wiki/queries/locate-memory-shard|Locate memory shard for revert target]] — Is there a local memory shard for the desired UI state that can be used to revert instead of recreating from scratch?
- [[topics/looked-image/wiki/queries/meet-131k-with-optimization|Meet 131K with optimization]] — Can the current artifact meet the 131K target through further optimization research, rather than rebuilding?

