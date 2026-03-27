# Scroll Stop Builder

Use the installed `scroll-stop-builder` skill from `~/.claude/skills/scroll-stop-builder`.

## Goal
Turn a source video into a premium scroll-driven website with sticky visual storytelling, restrained parallax, and mobile-safe fallbacks.

## Workflow

1. Read any provided scrape export or brand JSON first for colors, CTA hierarchy, and copy tone.
2. Find or confirm the input video.
3. If the user says “use the latest file in Downloads,” inspect `~/Downloads` and confirm the best video candidate if needed.
4. Probe the video and extract preview frames.
5. Shape the copy around value add: promise, mechanism, payoff, proof, and CTA ladder.
6. Choose the simplest strong implementation for the current repo or workspace.
7. Build the page and validate it locally.

## Default Questions

Ask only if needed:
- Which video file should I use?
- Which folder or repo should I build the site in?

If the user does not specify a file but says to use the latest download, go find it.
If the user provides a scraped JSON export, use it as the brand/copy source for the coded page.

## Output

- a working scroll-driven page
- notes on the structure you chose
- any generated frame assets
- a quick validation summary
