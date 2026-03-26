---
name: exploded-scene-prompter
description: Builds premium three-part prompt packages for products, vehicles, food, furniture, and service visuals: assembled still, exploded still, and video transition prompts. Use when the user wants a subject broken apart, staged with components flying outward, or converted into a stronger image-to-video concept.
---

# Exploded Scene Prompter

Use this skill when the user wants:
- an object or container visually exploding open
- a structured hero prompt package for image and video generation
- a premium HTML prompt page around the concept
- product, food, vehicle, furniture, or service scenes with components clearly art directed

## Core Behavior

- Convert rough creative intent into crisp commercial prompt packages.
- Default to photoreal, premium, ad-ready language unless the user requests a different aesthetic.
- If the user asks for a web or HTML view, use [assets/prompt-page-template.html](assets/prompt-page-template.html) as the output scaffold.
- If the object class is ambiguous, ask one concise clarifying question. Otherwise infer reasonable details and keep moving.
- Treat vague prompts as under-specified. Improve them by making the motion, staging, object list, pacing, and continuity explicit.

## Output Package

Produce these sections unless the user asks for fewer:
1. `PROMPT A - ASSEMBLED SHOT`
2. `PROMPT B - DECONSTRUCTED / EXPLODED VIEW`
3. `PROMPT C - VIDEO TRANSITION (START FRAME / END FRAME)`
4. `ART DIRECTION NOTES`
5. `HTML VIEW` when the user asks for a page, mockup, or prompt page

Only add `PROMPT D - DETAIL / ALT ANGLE` when the user explicitly asks for extra still coverage.

## Prompt Rules

- Start with the subject, camera angle, and background.
- Name visible components explicitly.
- Keep the scene physically believable even when dramatic.
- Prefer white or restrained studio backgrounds unless the user wants an environmental scene.
- Avoid logos and text unless requested.
- Use a high-end product photography tone, not generic “AI art” language.
- For service businesses, show recognizable operational props. Example: moving van, boxes, rugs, lamp, wrapped art, straps.
- When writing the video prompt, always include:
  - `START FRAME`
  - `END FRAME`
  - `TRANSITION`
  - `STYLE`
- The video prompt should explain timing, order of motion, easing, object-level secondary motion, and camera behavior.
- Default camera guidance for transition prompts is locked-off or nearly locked unless the user asks for camera movement.
- Avoid generic verbs like “explode” or “animate” without specifying how, in what order, and with what physical behavior.

## Scene Construction Workflow

### 1. Interpret the subject
- Identify the hero object or container.
- Identify 6-20 components worth surfacing.
- Group them by category: structural parts, payload, styling props, motion debris.
- Infer missing realism details that make the shot better: packing materials, hinges, straps, fasteners, wrappers, cables, labels, soft goods, or hardware.

### 2. Decide the visual mode
- **Assembled**: clean intact subject, organized contents visible.
- **Exploded**: parts suspended in controlled motion, readable spacing, premium ad feel.
- **Video transition**: a motion plan that transforms the assembled frame into the exploded frame with believable choreography and pacing.

### 3. Write the prompts
- Use complete, polished paragraphs.
- Mention aspect ratio when the user implies a format like hero banner, landing page, or social asset.
- Add camera, lens, lighting, and quality cues at the end.
- For the video transition, make the transformation directional and staged:
  - what moves first
  - what follows
  - how long the pause and reveal last
  - how individual objects rotate, drift, unfold, or separate
  - how the final hold behaves

### 4. Upgrade weak prompts

If the user's original concept is generic, strengthen it before output:
- add a fuller item inventory
- add materials and texture cues
- add motion sequencing
- add secondary motions such as straps unfurling, rugs unrolling, lids opening, or soft items flexing
- add “same lighting setup” and continuity wording between stills and video
### 5. Build the HTML view when requested
- Read [references/prompt-patterns.md](references/prompt-patterns.md) for scene formulas.
- Read [assets/prompt-page-template.html](assets/prompt-page-template.html).
- Replace placeholders with the generated prompt package and scene summary.
- Keep the page elegant and readable, optimized for copy/paste into image tools or creative reviews.

## Default Output Style

- Tone: premium commercial art direction
- Format: easy to scan, copy, and refine
- Detail level: rich enough to generate strong images without becoming rambling
- Motion detail: explicit enough that a video model has a real choreography to follow

## Example Use Cases

- “Make a laptop exploded into chips, ports, keys, and screen layers.”
- “Create a tropical smoothie burst with fruit, ice, and liquid arcs.”
- “Build an HTML prompt page for a moving company van with furniture exploding out the back.”
- “Give me all three prompts so I can generate the stills first and then the video transition.”

## Special Notes

- If the user names a real brand, keep identifiers generic unless they explicitly want brand-accurate styling.
- If motion would become chaotic, bias toward controlled suspension rather than debris chaos.
- When writing furniture or logistics scenes, emphasize order, packing realism, and believable load-out details.
- The third prompt is not a throwaway. Treat it as the bridge between the first two prompts, with clear continuity from still to motion.
