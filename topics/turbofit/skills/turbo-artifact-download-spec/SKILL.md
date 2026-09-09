---
name: turbo-artifact-download-spec
description: Use when downloading new TurboFit GGUF/MLX candidate artifacts. Build a reproducible curl-backed download record with size verification and wiki-ready evidence.
version: 0.1.0
distilled: 2026-09-07 08:45
topic: turbofit
---
# turbo-artifact-download-spec
1. Read the Hermes request for target repo/path/quant and destination under ~/Models/storage/.
2. Resolve exact filename via HuggingFace tree API when repo name is ambiguous.
3. Run `curl -L -m 1800 -o <path> <url> | tail -5`.
4. Verify final file size matches expectation.
5. Record artifact path, size, source URL, and completion time in the topic wiki entity page with `^[raw/inbox/...]` provenance.
6. Do not run model loads unless explicitly requested by Chris; downloading is enough.

## Evidence
> Download Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf to ~/Models/storage/nail/.
> The repo Dirk-Qwen3.8-27B-GGUF-MTP returned 404. The actual repo is peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF.
> Download Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf to ~/Models/storage/dirk-gguf/.
