#!/usr/bin/env bash
# Builds dist/<skill>.zip for each skill: the folder claude.ai's "Upload skill" expects (a folder with SKILL.md inside).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/validate.py
rm -rf dist && mkdir -p dist
for d in skills/*/; do
  name=$(basename "$d")
  (cd skills && zip -qr "../dist/$name.zip" "$name" -x '*.DS_Store')
  echo "dist/$name.zip"
done
(cd dist && shasum -a 256 *.zip > SHA256SUMS)
