#!/usr/bin/env bash
# One-time setup in the user's project. Installs Playwright + Chromium into ./motion/node_modules and the Python packages.
# Works in macOS/Linux shells and Git Bash on Windows.
set -e
MOTION_DIR="${1:-./motion}"
mkdir -p "$MOTION_DIR"/{clips,dist,out,work,brand,inputs/shots,models}
PY=python3; command -v python3 >/dev/null || PY=python
missing=()
command -v node >/dev/null || missing+=("node 18+ (https://nodejs.org, or: winget install OpenJS.NodeJS.LTS)")
command -v ffmpeg >/dev/null || missing+=("ffmpeg (macOS: brew install ffmpeg | Windows: winget install Gyan.FFmpeg)")
command -v $PY >/dev/null || missing+=("python 3.10-3.12 (Windows: winget install Python.Python.3.12)")
if [ ${#missing[@]} -gt 0 ]; then printf 'Missing:\n'; printf ' - %s\n' "${missing[@]}"; exit 1; fi
pipi(){ $PY -m pip install -q "$@" 2>/dev/null || $PY -m pip install -q --user "$@" 2>/dev/null || $PY -m pip install -q --break-system-packages "$@"; }
pipi numpy opencv-python-headless fonttools brotli
pipi "mediapipe==0.10.14" || echo "Note: mediapipe didn't install; background looks will fall back to rembg (pip install rembg onnxruntime)."
pipi sherpa-onnx || echo "Note: sherpa-onnx didn't install; transcription will rely on faster-whisper."
pipi faster-whisper || echo "Note: faster-whisper didn't install; transcription will use the Parakeet fallback."
if [ ! -d "$MOTION_DIR/node_modules/playwright" ]; then
  ( cd "$MOTION_DIR" && { [ -f package.json ] || echo '{"private":true}' > package.json; } && npm install --silent playwright && npx playwright install chromium )
fi
ffmpeg -hide_banner -encoders 2>/dev/null | grep -q prores_ks || echo "Note: your ffmpeg has no prores_ks encoder; transparent clips (.mov) will fail."
ffmpeg -hide_banner -filters 2>/dev/null | grep -q " ass " || echo "Note: your ffmpeg has no libass; captions can't be burned in."
echo "Ready. Clips go in $MOTION_DIR/clips, renders in $MOTION_DIR/out."
