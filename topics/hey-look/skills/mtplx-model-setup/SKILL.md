---
name: mtplx-model-setup
description: Use when setting up MTPLX for a local model on Mac.
version: 0.1.0
distilled: 2026-09-06 21:58
topic: hey-look
---
# mtplx-model-setup
# MTPLX model setup

## Steps
1. Install MTPLX.
2. Download the target model via MTPLX.
3. If download stalls near completion, restart MTPLX to complete.
4. Start the MTPLX server with the desired MTP depth.
5. Test speed with `tok/s` measurement.
6. Record model size, peak memory, context length, and speed.

## Pitfalls
- 20.4GB models can stall at 19G/20.4G; restarting usually completes quickly.
- Always test speed after server start.
- Record baseline tok/s before changing MTP depth.

## Evidence
> MTPLX process died at 19G/20.4G. Nearly done. Let me restart — it should complete quickly now.
> MTPLX is up with MTP depth 3. Let me test it.
