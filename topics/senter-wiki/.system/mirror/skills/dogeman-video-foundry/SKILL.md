# Dogeman Video Foundry

Turn scripts into visuals — artsy, not stock.

## Capabilities
- **Backgrounds**: generative loops (p5js, comfyui, image_generate) — 16:9 ambient for rant segments
- **Shorts**: 9:16 punch cuts from long-form beats — hook in first 2s, burned captions
- **Cutscenes**: interstitial game-like animations between rant chunks (manim-video, excalidraw, comfyui)

## Workflow
1. Read `workspace/scripts/<episode>.md` for B-roll cues
2. Generate assets into `workspace/shorts/` and `workspace/cutscenes/`
3. Use: `image_generate`, `comfyui`, `p5js`, `manim-video`, `excalidraw`, `design-md`

Always keep boss's voice; visuals support, don't overwrite.
