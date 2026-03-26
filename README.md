# Scroll Stop Skills

Reusable agent skills for:
- building premium exploded-scene prompts and prompt pages
- turning source videos into scroll-driven landing pages

This repo includes:
- `skills/exploded-scene-prompter`
- `skills/scroll-stop-builder`
- `claude-commands/` wrappers for direct Claude Code slash-command use
- `examples/heart-car/` as a local test fixture and reference implementation
- `examples/prompt-packs/` for concrete prompt-pack examples
- `scripts/validate-skill-pack.py` for a lightweight repo self-check

## What This Supports

### `exploded-scene-prompter`

Use when you want something like:
- “Build me an HTML prompt page for a moving company van with furniture exploding out of the back.”
- “Turn this product into assembled, exploded, and video-transition prompts.”
- “Give me all three prompts so I can generate stronger stills before I generate the motion pass.”

### `scroll-stop-builder`

Use when you want something like:
- “Build a scroll-driven landing page around the latest video in my Downloads folder.”
- “Imitate that sticky scrollytelling / parallax feel from a premium ad.”

## Install

```bash
git clone https://github.com/tashiscool/scroll-stop-skills.git
cd scroll-stop-skills
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

```text
Use $exploded-scene-prompter to turn my dating-app heart logo into assembled, exploded, and video-transition prompts before we build the landing page around it.
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
cd examples/heart-car/site
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173
```

## Prompt-Pack Examples

- [dating-heart-logo](examples/prompt-packs/dating-heart-logo.md)
- the moving-van canonical example also lives inside the skill references at [moving-van-example.md](skills/exploded-scene-prompter/references/moving-van-example.md)

## Validate The Repo

Run:

```bash
python3 scripts/validate-skill-pack.py
```

This checks for the expected repo structure, key prompt-contract strings, executable helper scripts, and the example frame set.

## Tool Compatibility

- Codex: `~/.codex/skills`
- Claude Code: `~/.claude/skills` and `~/.claude/commands`
- Cursor / Copilot users can also reuse the `skills/` directories directly because the pack follows the Agent Skills layout

## Notes

- The example media assets are treated as local test inputs. Use your own video if you plan to publish derivatives.
- The skills are intentionally lightweight: the heavy lifting is done by the agent plus the included helper scripts and templates.
