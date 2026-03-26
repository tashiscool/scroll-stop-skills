#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

install_skill() {
  local source_dir="$1"
  local codex_dest="$HOME/.codex/skills/$(basename "$source_dir")"
  local claude_dest="$HOME/.claude/skills/$(basename "$source_dir")"

  mkdir -p "$HOME/.codex/skills" "$HOME/.claude/skills"
  rm -rf "$codex_dest" "$claude_dest"
  cp -R "$source_dir" "$codex_dest"
  cp -R "$source_dir" "$claude_dest"
}

install_command() {
  local source_file="$1"
  mkdir -p "$HOME/.claude/commands"
  cp "$source_file" "$HOME/.claude/commands/"
}

install_skill "$ROOT_DIR/skills/exploded-scene-prompter"
install_skill "$ROOT_DIR/skills/scroll-stop-builder"
install_command "$ROOT_DIR/claude-commands/exploded-scene-prompter.md"
install_command "$ROOT_DIR/claude-commands/scroll-stop-builder.md"

chmod +x "$HOME/.codex/skills/scroll-stop-builder/scripts/"*.sh
chmod +x "$HOME/.claude/skills/scroll-stop-builder/scripts/"*.sh

echo "Installed skills for Codex and Claude Code."
echo "Restart both tools to ensure the new skills are picked up."
