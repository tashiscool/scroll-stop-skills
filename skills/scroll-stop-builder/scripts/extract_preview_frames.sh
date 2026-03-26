#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <video-path> <out-dir>" >&2
  exit 1
fi

video_path="$1"
out_dir="$2"

mkdir -p "$out_dir"

duration="$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$video_path")"
if [ -z "$duration" ]; then
  echo "Could not determine duration" >&2
  exit 1
fi

midpoint="$(python3 - <<'PY' "$duration"
import sys
d = float(sys.argv[1])
print(max(d / 2, 0.0))
PY
)"

tailpoint="$(python3 - <<'PY' "$duration"
import sys
d = float(sys.argv[1])
print(max(d - 0.25, 0.0))
PY
)"

ffmpeg -y -i "$video_path" -ss 0 -frames:v 1 "$out_dir/preview_01.jpg" >/dev/null 2>&1
ffmpeg -y -i "$video_path" -ss "$midpoint" -frames:v 1 "$out_dir/preview_02.jpg" >/dev/null 2>&1
ffmpeg -y -i "$video_path" -ss "$tailpoint" -frames:v 1 "$out_dir/preview_03.jpg" >/dev/null 2>&1
