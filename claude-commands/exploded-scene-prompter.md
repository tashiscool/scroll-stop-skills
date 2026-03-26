# Exploded Scene Prompter

Use the installed `exploded-scene-prompter` skill from `~/.claude/skills/exploded-scene-prompter`.

## Goal
Turn a rough creative request into premium assembled, exploded, and video-transition prompts and, when requested, an HTML prompt page.

## Workflow

1. Identify the hero object or container.
2. Infer the important components or payload items.
3. Produce:
   - `PROMPT A - ASSEMBLED SHOT`
   - `PROMPT B - DECONSTRUCTED / EXPLODED VIEW`
   - `PROMPT C - VIDEO TRANSITION (START FRAME / END FRAME)`
   - `ART DIRECTION NOTES`
4. If the user asks for an HTML view, build the HTML page around those prompts.

## Default Behavior

- Default to premium commercial product-photography language.
- Keep scenes readable and physically believable.
- Ask one concise clarifying question only if the subject is genuinely ambiguous.
- If the user asks for HTML, generate the prompt package first and the HTML second.
