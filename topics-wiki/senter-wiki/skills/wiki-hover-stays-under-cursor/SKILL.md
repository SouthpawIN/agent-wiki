---
name: wiki-hover-stays-under-cursor
description: Use when a Senter wiki element grows, lifts or expands on hover. The thing under the pointer must still be under the pointer after the transition; grow away from the cursor, never across it.
version: 0.1.0
distilled: 2026-09-05 19:27
topic: senter-wiki
---
# wiki-hover-stays-under-cursor
Written to topics-wiki/senter-wiki/skills-capabilities/wiki-hover-stays-under-cursor/SKILL.md: anchor = hovered element's pre-transition centre; siblings grow outward from it; rest geometry keeps right-edge alignment, transient hover may overhang right; right-anchored grow only correct for the rightmost sibling; verify centre delta 0±1px for each dot in the real window.

## Evidence
> when I hover over the third dot and it expands, the third dot should still be under my mouse and everything else should grow and expand like it should, even if it goes to the right a little bit
> when I hover over them they don't need to grow anymore … they just need to shift up and show the card
