---
name: scroll-stop-builder
description: Builds scroll-driven landing pages from video files, frame sequences, or hero motion references. Use when the user wants a parallax, scrollytelling, sticky-frame, or premium video-led website experience.
---

# Scroll Stop Builder

Use this skill when the user wants:
- a scroll-driven website built around a video
- a premium landing page that imitates ad-style parallax or scrollytelling
- a hero sequence synchronized to extracted frames
- a video-led campaign page with sticky sections and motion pacing
- a coded website builder flow that should also inherit brand/copy guidance from a scraped JSON export

If the user does not have a finished video yet and is still shaping the visual concept, first generate the three-part prompt package with `exploded-scene-prompter`:
1. assembled still
2. exploded still
3. video transition prompt

Use that package to improve the motion brief before building the site around the resulting asset.

## Default Workflow

### 0. Read any brand/source export first
- If the user provides a scraped JSON export, use it as a source of truth for:
  - colors
  - fonts
  - CTA hierarchy
  - copy tone
  - section ordering clues
- Do not treat that JSON as the literal page layout. Treat it as a brand/copy brief that informs the coded implementation.
- If the export includes markdown content or branding tokens, extract them before building.

See [references/json-brand-copy-source.md](references/json-brand-copy-source.md).

### 1. Find or confirm the source video
- If the user gives a path, use it.
- If the user says “the latest file in Downloads,” inspect `~/Downloads` and confirm the best video candidate if there is any ambiguity.
- Prefer `.mp4`, `.mov`, or `.webm`.
- If there is no source video yet, stop and strengthen the visual brief first instead of pretending the video already exists.

### 2. Inspect the asset
- Run `scripts/video_probe.sh <video-path>` to get duration, fps, dimensions, and codec.
- Extract 3 preview frames with `scripts/extract_preview_frames.sh <video-path> <out-dir>` so you can understand the opening, middle, and ending visual beats.

### 3. Choose the scroll pattern
- **Short premium promo**: hero + sticky sequence + feature cards + CTA
- **Strong visual narrative**: sticky image sequence with text panels
- **Minimal build**: single-page HTML/CSS/JS with progressive reveal

Default to a static-site implementation unless the existing repo clearly wants React/Next/Vite.

### 4. Build the page
- Read [references/sections-guide.md](references/sections-guide.md).
- If the user provided a scrape export, use the extracted copy hierarchy and CTAs while composing the page sections.
- If you need a starting scaffold, use [assets/scroll-stop-template.html](assets/scroll-stop-template.html).
- Create a premium page with:
  - strong opening hero
  - sticky viewport sequence or scroll-scrubbed visual region
  - layered copy tied to video beats
  - restrained parallax
  - mobile fallbacks

### 5. Extract frames when needed
- For true scroll-scrubbed sequences, run `scripts/extract_scroll_frames.sh <video-path> <frames-dir> [fps] [width]`.
- Do not extract huge frame sets unless the page really needs them.
- If the video is long, sample key beats rather than forcing every second into the scroll.

### 6. Validate the result
- Open locally.
- Check desktop and mobile widths.
- Make sure the page still reads well if motion is reduced or JavaScript fails.

## Design Rules

- The page must feel intentional and premium, not like a generic template.
- Use typography with personality.
- Use motion to reveal meaning, not just to decorate.
- Let the strongest shot carry the hero section.
- Avoid cluttered copy overlays on top of dense video frames.

## Output Checklist

Deliver:
1. The implemented page
2. The chosen scroll structure
3. Any extracted frame assets or directories
4. Notes on performance tradeoffs
5. A quick validation summary

## Behavioral Rules

- Ask only the minimum clarifying questions required.
- If the repo already contains a front-end stack, adapt to it.
- If the user only wants the concept or prompt, do not overbuild.
- If the video concept is weak or generic, recommend generating the assembled / exploded / transition trio first.
- If the user supplied a brand JSON export, preserve its best tokens and CTA logic even while redesigning the actual page.
- If the video is unsuitable for frame-by-frame scrubbing, fall back to:
  - autoplay hero loop
  - sticky text reveals
  - section parallax tied to the existing video

## Common Requests

- “Build a scroll-stop site around the last downloaded video.”
- “Imitate the parallax feel from this ad.”
- “Turn this moving-van explosion clip into a high-conversion landing page.”
