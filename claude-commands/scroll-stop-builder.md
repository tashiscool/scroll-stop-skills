# Scroll Stop Builder

Use the installed `scroll-stop-builder` skill from `~/.claude/skills/scroll-stop-builder`.

## Goal
Turn a source video into a premium scroll-driven website with sticky visual storytelling, restrained parallax, and mobile-safe fallbacks.

## Workflow

1. Find or confirm the input video.
2. If the user says “use the latest file in Downloads,” inspect `~/Downloads` and confirm the best video candidate if needed.
3. Probe the video and extract preview frames.
4. Choose the simplest strong implementation for the current repo or workspace.
5. Build the page and validate it locally.

## Default Questions

Ask only if needed:
- Which video file should I use?
- Which folder or repo should I build the site in?

If the user does not specify a file but says to use the latest download, go find it.

## Output

- a working scroll-driven page
- notes on the structure you chose
- any generated frame assets
- a quick validation summary
