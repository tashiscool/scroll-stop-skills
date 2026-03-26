# Heart Car Demo

This is a local demo workspace for validating `scroll-stop-builder` against:

`~/Downloads/Heart_Car_Animation_Prompt_Generation.mp4`

The file name says “car,” but the actual video is an 8-second heart-logo assembly animation on a clean white background. It works well as a test case for:
- sticky stage composition
- scroll-scrubbed image sequences
- restrained parallax
- reduced-motion fallbacks

## Rebuild The Local Demo Assets

```bash
VIDEO=~/Downloads/Heart_Car_Animation_Prompt_Generation.mp4
OUT=/Users/tkhan/IdeaProjects/scroll-stop-skills/examples/heart-car/site/assets

mkdir -p "$OUT/previews" "$OUT/frames"
/Users/tkhan/.codex/skills/scroll-stop-builder/scripts/extract_preview_frames.sh "$VIDEO" "$OUT/previews"
/Users/tkhan/.codex/skills/scroll-stop-builder/scripts/extract_scroll_frames.sh "$VIDEO" "$OUT/frames" 10 960
```

## Run The Site

```bash
cd /Users/tkhan/IdeaProjects/scroll-stop-skills/examples/heart-car/site
python3 -m http.server 4173
```

Then open `http://localhost:4173`.
