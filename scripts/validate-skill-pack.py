#!/usr/bin/env python3
from __future__ import annotations

import stat
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "install.sh",
    "claude-commands/exploded-scene-prompter.md",
    "claude-commands/scroll-stop-builder.md",
    "claude-commands/lovable-remix-builder.md",
    "skills/exploded-scene-prompter/SKILL.md",
    "skills/exploded-scene-prompter/agents/openai.yaml",
    "skills/exploded-scene-prompter/assets/prompt-page-template.html",
    "skills/exploded-scene-prompter/references/prompt-patterns.md",
    "skills/exploded-scene-prompter/references/moving-van-example.md",
    "skills/scroll-stop-builder/SKILL.md",
    "skills/scroll-stop-builder/agents/openai.yaml",
    "skills/scroll-stop-builder/assets/scroll-stop-template.html",
    "skills/scroll-stop-builder/references/sections-guide.md",
    "skills/scroll-stop-builder/references/json-brand-copy-source.md",
    "skills/scroll-stop-builder/scripts/video_probe.sh",
    "skills/scroll-stop-builder/scripts/extract_preview_frames.sh",
    "skills/scroll-stop-builder/scripts/extract_scroll_frames.sh",
    "skills/lovable-remix-builder/SKILL.md",
    "skills/lovable-remix-builder/agents/openai.yaml",
    "skills/lovable-remix-builder/references/reference-selection.md",
    "skills/lovable-remix-builder/references/lovable-prompt-patterns.md",
    "skills/lovable-remix-builder/references/section-remix-example.md",
    "skills/lovable-remix-builder/references/json-scrape-remix.md",
    "examples/heart-car/README.md",
    "examples/heart-car/site/index.html",
    "examples/heart-car/site/styles.css",
    "examples/heart-car/site/app.js",
    "examples/prompt-packs/dating-heart-logo.md",
    "examples/lovable-remix/README.md",
    "examples/lovable-remix/pairara-remix.md",
]

REQUIRED_STRINGS = {
    "skills/exploded-scene-prompter/SKILL.md": [
        "PROMPT A - ASSEMBLED SHOT",
        "PROMPT B - DECONSTRUCTED / EXPLODED VIEW",
        "PROMPT C - VIDEO TRANSITION (START FRAME / END FRAME)",
        "First-Step Contract",
    ],
    "skills/scroll-stop-builder/SKILL.md": [
        "assembled still",
        "exploded still",
        "video transition prompt",
        "scraped JSON export",
    ],
    "claude-commands/exploded-scene-prompter.md": [
        "PROMPT A - ASSEMBLED SHOT",
        "PROMPT B - DECONSTRUCTED / EXPLODED VIEW",
        "PROMPT C - VIDEO TRANSITION (START FRAME / END FRAME)",
    ],
    "skills/lovable-remix-builder/SKILL.md": [
        "section-by-section remix workflow",
        "Reference Selection Rules",
        "Write section prompts for Lovable",
        "scraped JSON export",
    ],
    "README.md": [
        "validate-skill-pack.py",
        "examples/prompt-packs/dating-heart-logo.md",
        "lovable-remix-builder",
    ],
}


def main() -> int:
    errors: list[str] = []

    for rel_path in REQUIRED_FILES:
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing required file: {rel_path}")

    for rel_path, tokens in REQUIRED_STRINGS.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                errors.append(f"Missing required text in {rel_path}: {token}")

    for rel_path in [
        "install.sh",
        "skills/scroll-stop-builder/scripts/video_probe.sh",
        "skills/scroll-stop-builder/scripts/extract_preview_frames.sh",
        "skills/scroll-stop-builder/scripts/extract_scroll_frames.sh",
    ]:
        path = ROOT / rel_path
        if not path.exists():
            continue
        mode = path.stat().st_mode
        if not (mode & stat.S_IXUSR):
            errors.append(f"Expected executable bit on: {rel_path}")

    heart_frames = list((ROOT / "examples/heart-car/site/assets/frames").glob("frame_*.jpg"))
    if len(heart_frames) < 10:
        errors.append("Expected example heart-car frame set to contain at least 10 frames")

    if errors:
        print("Skill pack validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill pack validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
