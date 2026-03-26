#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ] || [ "$#" -gt 4 ]; then
  echo "Usage: $0 <video-path> <frames-dir> [fps=12] [width=1920]" >&2
  exit 1
fi

video_path="$1"
frames_dir="$2"
fps="${3:-12}"
width="${4:-1920}"

mkdir -p "$frames_dir"

ffmpeg -y -i "$video_path" -vf "fps=${fps},scale=${width}:-2" -q:v 2 "$frames_dir/frame_%04d.jpg"
