# both-smarter — topic brief

## Scope
Chris's model-selection work for his unified-memory (Apple) hardware: finding, running, and benchmarking LLMs on his devices, and how models are presented in the Senter Wiki.

## Anti-scope
General Hermes configuration and non-model wiki UI belong elsewhere unless they serve model presentation.

## Lens
"Both smarter and faster" than free models; per-device lanes; benchmarks over vibes; research from official sources.

## Learned
- Portal pattern (clickable model → dedicated research page) is intended as a reusable template for how other topics present content in the wiki.
- Benchmarks must cover more than tokens/second and be kept current per model; define the most common cross-model benchmarks once.
- On the CPU/unified-memory lane, IQ3S is the quant for the whole range (24GB→48GB→full precision) because it's near-lossless and better than Q4 / runs on less power.
- TurboFit rules are to be tracked AND implemented incrementally as Chris states them, not batched at the end.
