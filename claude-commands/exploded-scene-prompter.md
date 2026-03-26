# Exploded Scene Prompter

Use the installed `exploded-scene-prompter` skill from `~/.claude/skills/exploded-scene-prompter`.

## Goal
Turn a rough creative request into premium exploded-scene prompts and, when requested, an HTML prompt page.

## Workflow

1. Identify the hero object or container.
2. Infer the important components or payload items.
3. Produce:
   - `PROMPT A - ASSEMBLED SHOT`
   - `PROMPT B - EXPLODED SHOT`
   - `PROMPT C - DETAIL / ALT ANGLE`
   - `ART DIRECTION NOTES`
4. If the user asks for an HTML view, use the skill template and generate the page.

## Default Behavior

- Default to premium commercial product-photography language.
- Keep scenes readable and physically believable.
- Ask one concise clarifying question only if the subject is genuinely ambiguous.
