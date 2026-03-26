# Scroll Stop Skills

Reusable agent skills for:
- building premium exploded-scene prompts and prompt pages
- turning source videos into scroll-driven landing pages

This repo includes:
- `skills/exploded-scene-prompter`
- `skills/scroll-stop-builder`
- `claude-commands/` wrappers for direct Claude Code slash-command use
- `examples/heart-car/` as a local test fixture and reference implementation

## What This Supports

### `exploded-scene-prompter`

Use when you want something like:
- “Build me an HTML prompt page for a moving company van with furniture exploding out of the back.”
- “Turn this product into assembled, exploded, and detail-shot prompts.”

### `scroll-stop-builder`

Use when you want something like:
- “Build a scroll-driven landing page around the latest video in my Downloads folder.”
- “Imitate that sticky scrollytelling / parallax feel from a premium ad.”

## Install

```bash
cd /Users/tkhan/IdeaProjects/scroll-stop-skills
./install.sh
```

This installs:
- skills into `~/.codex/skills`
- skills into `~/.claude/skills`
- Claude slash-command wrappers into `~/.claude/commands`

Restart Codex and Claude Code after install.

## Usage

### Codex

```text
Use $scroll-stop-builder to turn the latest video in my Downloads folder into a premium scroll-driven landing page.
```

```text
Use $exploded-scene-prompter to create an HTML prompt page for a moving van with furniture exploding out of the back.
```

### Claude Code

```text
/scroll-stop-builder
```

```text
/exploded-scene-prompter
```

## Local Example

The `examples/heart-car` folder contains a tested scroll-demo workspace built from a local MP4.

Open the example locally:

```bash
cd /Users/tkhan/IdeaProjects/scroll-stop-skills/examples/heart-car/site
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173
```

## Notes

- The example media assets are treated as local test inputs. Use your own video if you plan to publish derivatives.
- The skills are intentionally lightweight: the heavy lifting is done by the agent plus the included helper scripts and templates.
