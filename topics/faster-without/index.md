# faster-without — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-07 | Total pages: 10

## Entities
- [[topics/faster-without/wiki/entities/27b-model|27B Model]] — The 27B model is the concrete inference target in this topic. Chris’s standing requirement is that it run at a minimum 131K context length, even if D-flash is r
- [[topics/faster-without/wiki/entities/d-flash|D-Flash]] — D-flash is the feature under review for removal to improve inference speed. Chris asked, "Would it be faster without it?" and later clarified: "By faster, I mea
- [[topics/faster-without/wiki/entities/d-flash2|DFlash2]] — DFlash2 appears in a live setup labeled `Unleashed + DFlash2`, which is reported up at 131K and intended for speed testing against a separate `Unleashed` server
- [[topics/faster-without/wiki/entities/unleashed|Unleashed]] — Unleashed is a speed reference point in Chris’s comparison. A measured state of 8.4 tok/s for 1000 tokens was described as faster than Unleashed. ^[raw/inbox/20

## Concepts
- [[topics/faster-without/wiki/concepts/d-flash-tradeoff|D-Flash Tradeoff]] — Chris questions whether D-flash is why current speeds are lower than he remembers. ^[raw/inbox/2026-09-06.md#L7] He wants to know whether removing it would make
- [[topics/faster-without/wiki/concepts/measured-performance|Measured Performance]] — Chris recalled earlier speeds being much higher than current performance. The only explicit benchmark captured so far is 8.4 tok/s for 1000 tokens, described as
- [[topics/faster-without/wiki/concepts/performance-target|27B at 131K]] — Chris’s explicit requirement is that the 27B model run at a minimum 131K context length. ^[raw/inbox/2026-09-06.md#L17] This target holds even when reconsiderin

## Decisions
- [[topics/faster-without/wiki/decisions/retain-131k-context|Retain 131K Context]] — Chris decided that any speed change must preserve the hard floor of 131K context length for the 27B model. ^[raw/inbox/2026-09-06.md#L17]

## Comparisons
- [[topics/faster-without/wiki/comparisons/unleashed-vs-dflash2|Unleashed vs DFlash2]] — A planned head-to-head performance comparison between the separate `Unleashed` server and the `Unleashed + DFlash2` setup. Both are reported running, and the st
- [[topics/faster-without/wiki/comparisons/with-without-d-flash|With vs Without D-Flash]] — Chris is comparing the current D-flash-enabled state against a hypothetical faster state without it. He recalls earlier speeds being much higher and suspects D-

## Queries


