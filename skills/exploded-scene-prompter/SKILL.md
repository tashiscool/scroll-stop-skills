---
name: exploded-scene-prompter
description: Builds premium exploded-scene image prompts and prompt pages for products, vehicles, food, furniture, and service visuals. Use when the user wants a subject broken apart, bursting open, or staged with components flying outward in a clean commercial style.
---

# Exploded Scene Prompter

Use this skill when the user wants:
- an object or container visually exploding open
- a structured hero prompt for image generation
- a premium HTML prompt page around the concept
- product, food, vehicle, furniture, or service scenes with components clearly art directed

## Core Behavior

- Convert rough creative intent into crisp commercial-image prompts.
- Default to photoreal, premium, ad-ready language unless the user requests a different aesthetic.
- If the user asks for a web or HTML view, use [assets/prompt-page-template.html](assets/prompt-page-template.html) as the output scaffold.
- If the object class is ambiguous, ask one concise clarifying question. Otherwise infer reasonable details and keep moving.

## Output Package

Produce these sections unless the user asks for fewer:
1. `PROMPT A - ASSEMBLED SHOT`
2. `PROMPT B - EXPLODED SHOT`
3. `PROMPT C - DETAIL / ALT ANGLE`
4. `ART DIRECTION NOTES`
5. `HTML VIEW` when the user asks for a page, mockup, or prompt page

## Prompt Rules

- Start with the subject, camera angle, and background.
- Name visible components explicitly.
- Keep the scene physically believable even when dramatic.
- Prefer white or restrained studio backgrounds unless the user wants an environmental scene.
- Avoid logos and text unless requested.
- Use a high-end product photography tone, not generic “AI art” language.
- For service businesses, show recognizable operational props. Example: moving van, boxes, rugs, lamp, wrapped art, straps.

## Scene Construction Workflow

### 1. Interpret the subject
- Identify the hero object or container.
- Identify 6-20 components worth surfacing.
- Group them by category: structural parts, payload, styling props, motion debris.

### 2. Decide the visual mode
- **Assembled**: clean intact subject, organized contents visible.
- **Exploded**: parts suspended in controlled motion, readable spacing, premium ad feel.
- **Detail**: one tighter angle or alternate crop for texture and realism.

### 3. Write the prompts
- Use complete, polished paragraphs.
- Mention aspect ratio when the user implies a format like hero banner, landing page, or social asset.
- Add camera, lens, lighting, and quality cues at the end.

### 4. Build the HTML view when requested
- Read [references/prompt-patterns.md](references/prompt-patterns.md) for scene formulas.
- Read [assets/prompt-page-template.html](assets/prompt-page-template.html).
- Replace placeholders with the generated prompt package and scene summary.
- Keep the page elegant and readable, optimized for copy/paste into image tools or creative reviews.

## Default Output Style

- Tone: premium commercial art direction
- Format: easy to scan, copy, and refine
- Detail level: rich enough to generate strong images without becoming rambling

## Example Use Cases

- “Make a laptop exploded into chips, ports, keys, and screen layers.”
- “Create a tropical smoothie burst with fruit, ice, and liquid arcs.”
- “Build an HTML prompt page for a moving company van with furniture exploding out the back.”

## Special Notes

- If the user names a real brand, keep identifiers generic unless they explicitly want brand-accurate styling.
- If motion would become chaotic, bias toward controlled suspension rather than debris chaos.
- When writing furniture or logistics scenes, emphasize order, packing realism, and believable load-out details.
