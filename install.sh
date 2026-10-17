#!/usr/bin/env bash
# Install the pipeline skills into a Claude Code / Agent SDK skills directory.
#
#   ./install.sh                 → ~/.claude/skills/
#   ./install.sh /path/to/skills → a custom location
#   ./install.sh --project       → ./.claude/skills/ in the current repo

set -euo pipefail

src="$(cd "$(dirname "${BASH_SOURCE[0]}")/skills" && pwd)"

case "${1:-}" in
  --project) dest="$(pwd)/.claude/skills" ;;
  "")        dest="${HOME}/.claude/skills" ;;
  *)         dest="$1" ;;
esac

mkdir -p "$dest"

for skill in "$src"/*/; do
  name="$(basename "$skill")"
  rm -rf "${dest:?}/${name}"
  cp -r "$skill" "$dest/$name"
  echo "installed  $name"
done

echo
echo "→ $dest"

# Required companion skills (see client-site-pipeline → "Required companion skills").
missing=""
[ -d "$dest/copywriting" ] || missing="$missing copywriting"
[ -d "$dest/antislop" ] || missing="$missing antislop"
if [ -n "$missing" ]; then
  echo
  echo "Required companion skills missing:$missing"
  echo "  npx skills add coreyhaines31/marketingskills --skill copywriting -g"
  echo "  npx skills add miqdadbadjuber/anti-slop -g"
fi
