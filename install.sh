#!/usr/bin/env bash
# Install the pipeline skills into a Claude Code / Agent SDK skills directory,
# then install what they need (companion skills, ffmpeg, the PDF kit's Python
# packages) through client-site-pipeline/scripts/setup.mjs.
#
#   ./install.sh                 → ~/.claude/skills/
#   ./install.sh /path/to/skills → a custom location
#   ./install.sh --project       → ./.claude/skills/ in the current repo
#   ./install.sh --no-setup      → copy the skills only

set -euo pipefail

src="$(cd "$(dirname "${BASH_SOURCE[0]}")/skills" && pwd)"

dest=""
setup=1
for arg in "$@"; do
  case "$arg" in
    --project)  dest="$(pwd)/.claude/skills" ;;
    --no-setup) setup=0 ;;
    *)          dest="$arg" ;;
  esac
done
dest="${dest:-${HOME}/.claude/skills}"

mkdir -p "$dest"

for skill in "$src"/*/; do
  name="$(basename "$skill")"
  rm -rf "${dest:?}/${name}"
  cp -r "$skill" "$dest/$name"
  echo "installed  $name"
done

echo
echo "→ $dest"

[ "$setup" = 1 ] || exit 0

# Node runs the setup (and every Astro build), so get it first.
if ! command -v node >/dev/null 2>&1; then
  echo
  if command -v brew >/dev/null 2>&1; then
    echo "Node not found; installing it with Homebrew..."
    brew install node
  else
    echo "Node 18+ is required. Install the LTS from https://nodejs.org, then run:"
    echo "  node \"$dest/client-site-pipeline/scripts/setup.mjs\""
    exit 1
  fi
fi

echo
node "$dest/client-site-pipeline/scripts/setup.mjs"
