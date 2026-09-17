# Queue — add-one

## [CONTEXT]
- [ ] research model-tok-s-benchmarks — SUGGESTED 2026-09-17 00:01: Want me to look into real-world tokens-per-second benchmarks for the models on your table, so the tok/s column has an ex
- [ ] research table-domain-research — SUGGESTED 2026-09-16 19:55: I see you're adding a parameters category to a comparison table — want me to look into what the table actually compares 
- [~] research — dispatched 2026-09-16 19:51

## [SKILLS]

## [AGENTS]

## [LOOPS]
- [ ] fit-table-tok-s-benchmark-tracker — SUGGESTED 2026-09-17 12:03: You track best tok/s after flags across GPU, CPU, and unified — want a loop that flags which model is now fastest on eac → triggers-loops/fit-table-tok-s-benchmark-tracker.md.proposed
- [ ] fit-table-tok-s-updater — SUGGESTED 2026-09-17 12:03: I see you now track the highest recorded tok/s after flags on your GPU, CPU, and unified fit tables — want a loop that u → triggers-loops/fit-table-tok-s-updater.md.proposed
- [ ] model-benchmark-tracker — SUGGESTED 2026-09-17 00:01: Want a loop that periodically checks each model's best tokens-per-second across your runs and flags which one is fastest → triggers-loops/model-benchmark-tracker.md.proposed
- [ ] turbo-fit-tok-s-updater — SUGGESTED 2026-09-17 00:01: Every time TurboFit runs a model, want me to loop in the best tok/s it hit and update that column on your TurboFit list? → triggers-loops/turbo-fit-tok-s-updater.md.proposed
