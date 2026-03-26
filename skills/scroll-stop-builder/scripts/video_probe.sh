#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <video-path>" >&2
  exit 1
fi

video_path="$1"

ffprobe -v quiet -print_format json -show_streams -show_format "$video_path"
