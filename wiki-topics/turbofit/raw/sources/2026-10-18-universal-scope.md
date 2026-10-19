# Universal scope clarification — 2026-10-18

Captured verbatim from Chris (2026-10-18) to lock the intent before work. These override earlier personal-fleet framing.

## Verbatim (Chris, 2026-10-18)

> "This is supposed to be a universal system. I'm using there are many users on this It's already has a hundred likes. There's many things that need to be fixed presently. There's a lot of slop The readme needs to be updated Lots of things that I promise need to be built in yeah, so that's where we're at"

> "we should be simultaneously working on both we should be testing turbo fit with my local installation but keeping in mind that we need to keep this Available for everything And now we do have the advantage of having a Linux workstation and a MacBook here and both of them are connected over tail scale And then also we I want to solidify the tail scale functionalities within turbo fit"

> "yes, I want you to integrate salt core as an engine I'm particularly interested in the part that streams From the hard drive and the kb stuff and anything that we could do to optimize models within turbofit Just like how I want the salt core to be integrate within turbofit the whole idea of turbofit is that there's it is in an Entirely self-managed Server not just an inference engine, but it will addition models and therefore also inference engines because we will be benchmarking different models, different hardware tiers and then I also want to be showing those benchmarks people have been asking for those too to determine which models and engines are the best at each hardware tier for each machine."

> "Notice there should be two different turbo fintless. There's a dedicated fit list for GPUs, machines that have VRAM and that should be for both AMD and Nvidia and Intel I guess and any other GPUs that we'll be coming out and any other GPUs that are out. And then also there is a unified fit list which would be for Mac and CPU only. If you notice the dedicated GPUs tends to favor, it's supposed to favor the dense models and then the unified is supposed to favor for the M.O.E.s."

## Framing

- Scope = **public product**, not personal fleet (100+ likes, many users).
- Method = **validate on the local fleet** (MacBook + Omarchy Linux workstation, both on Tailscale) **while keeping it universal.**
- New first-class features: **two fit lists** (GPU-dense / unified-MoE), **benchmark publication to users**, **dynamic model + engine registry**, **SALT-core engine** (HDD streaming + KV offload), **Tailscale solidification.**
- Open debt: README slop, cross-OS test failures, self-install promise.
- Standing preference (continuity.md): "the Fit List IS the fallback chain" — Scan/recommend/Fit-List consolidation is the architectural fix.
