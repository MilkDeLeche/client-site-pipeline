#!/usr/bin/env bash
# Launch audit — inspect a production BUILD output directory (not the dev server).
# Usage:  bash audit.sh [build-dir]   (default: dist)
# Also pass a known body-text snippet to strengthen the empty-view-source check:
#   BODY_TEXT="Your Headline" bash audit.sh dist
set -u

DIR="${1:-dist}"
BODY_TEXT="${BODY_TEXT:-}"

if [ ! -d "$DIR" ]; then
  echo "Build dir '$DIR' not found. Build first (e.g. npm run build), or pass the dir."
  exit 1
fi

pass() { printf '  ✅ %s\n' "$1"; }
warn() { printf '  ⚠️  %s\n' "$1"; }
fail() { printf '  ❌ %s\n' "$1"; }

echo "== Launch audit: $DIR =="

echo "[1] View source not empty"
idx="$DIR/index.html"
if [ -f "$idx" ]; then
  bytes=$(grep -o '<body' "$idx" >/dev/null && wc -c < "$idx" || echo 0)
  hits=0
  [ -n "$BODY_TEXT" ] && hits=$(grep -c "$BODY_TEXT" "$idx" || true)
  if [ -n "$BODY_TEXT" ] && [ "$hits" -gt 0 ]; then pass "found body text '$BODY_TEXT' ($hits)"; \
  elif [ "${bytes:-0}" -gt 3000 ]; then pass "index.html is ${bytes} bytes of HTML (looks rendered)"; \
  else warn "index.html is small (${bytes} bytes) — confirm it isn't a JS shell"; fi
else fail "no $idx"; fi

echo "[2] 404 page"
{ [ -f "$DIR/404.html" ] && pass "404.html present"; } || fail "no 404.html"

# Every built page, whichever layout the build uses: dist/about/index.html (directory) or dist/about.html
# (Astro build.format: "file"). Pages without a <title> (e.g. verification files) simply add no title.
pages=$(find "$DIR" -name '*.html' -not -path '*/_astro/*')

echo "[3] Unique titles"
titles=$(echo "$pages" | while IFS= read -r f; do [ -n "$f" ] && grep -ho '<title>[^<]*</title>' "$f"; done)
n=$(echo "$titles" | grep -c .); u=$(echo "$titles" | sort -u | grep -c .)
if [ "$n" = "$u" ]; then pass "$n pages, $u unique titles"; else fail "$n pages but only $u unique titles (duplicates)"; fi

echo "[4] OG image"
{ grep -rq 'property="og:image"' "$DIR" --include=*.html && pass "og:image present"; } || fail "no og:image"

echo "[5] Structured data (JSON-LD)"
c=$(grep -rl 'application/ld+json' "$DIR" --include=*.html | wc -l)
{ [ "$c" -gt 0 ] && pass "JSON-LD on $c page(s)"; } || fail "no JSON-LD"

echo "[6] Canonical"
c=$(grep -rl 'rel="canonical"' "$DIR" --include=*.html | wc -l)
p=$(find "$DIR" -name '*.html' | wc -l)
{ [ "$c" -ge "$p" ] && pass "canonical on all $p page(s)"; } || warn "canonical on $c of $p pages"

echo "[7] robots.txt allows AI"
if [ -f "$DIR/robots.txt" ]; then
  if grep -qiE 'Disallow: /$' "$DIR/robots.txt" && ! grep -qi 'Allow: /' "$DIR/robots.txt"; then
    fail "robots.txt appears to block everything"
  else
    for bot in GPTBot ClaudeBot PerplexityBot Google-Extended; do
      grep -qi "$bot" "$DIR/robots.txt" && pass "mentions $bot" || warn "no explicit rule for $bot (allowed by default if not Disallowed)"
    done
    grep -qi '^Sitemap:' "$DIR/robots.txt" && pass "Sitemap: line present" || warn "no Sitemap: line in robots.txt"
  fi
else fail "no robots.txt"; fi

echo "[8] Sitemap"
{ ls "$DIR"/sitemap*.xml >/dev/null 2>&1 && pass "sitemap present"; } || fail "no sitemap*.xml"

echo "[9] Lang attribute (+ hreflang when the site has a second language)"
{ grep -q '<html[^>]*\blang=' "$idx" && pass "$(grep -o '<html[^>]*lang="[^"]*"' "$idx" | head -1 | grep -o 'lang="[^"]*"') on index.html"; } || fail "no <html lang>"
# Every page, not just the home page: count pages per <html lang>, and flag pages with none.
langs=$(echo "$pages" | while IFS= read -r f; do [ -n "$f" ] && { grep -o '<html[^>]*>' "$f" | head -1 | grep -o ' lang="[^"]*"' || echo ' lang="(none)"'; }; done | sort | uniq -c | sed 's/ lang=//; s/"//g' | awk '{printf "%s%s (%s)", sep, $2, $1; sep=", "}')
echo "      per page: $langs"
case "$langs" in *"(none)"*) fail "some pages have no <html lang>";; esac
nlang=$(echo "$langs" | tr ',' '\n' | grep -vc '(none)')
if [ "$nlang" -gt 1 ]; then
  # Two or more languages: every page except the 404s needs hreflang alternates (incl. x-default).
  content=$(echo "$pages" | grep -vc '/404\.html$\|/404/index\.html$')
  alt=$(echo "$pages" | while IFS= read -r f; do [ -n "$f" ] && grep -l 'hreflang="x-default"' "$f"; done | grep -c .)
  if [ "$alt" -ge "$content" ]; then pass "hreflang + x-default on $alt of $content non-404 pages"; else fail "hreflang + x-default on only $alt of $content non-404 pages"; fi
fi

echo "[10] Alt text"
total=$(grep -rho '<img[^>]*>' "$DIR" --include=*.html | wc -l)
noalt=$(grep -rho '<img[^>]*>' "$DIR" --include=*.html | grep -vc 'alt=' || true)
{ [ "$noalt" -eq 0 ] && pass "$total <img>, all have alt"; } || fail "$noalt of $total <img> missing alt"

echo "[11] Source maps not exposed"
maps=$(find "$DIR" -name '*.map' 2>/dev/null)
{ [ -z "$maps" ] && pass "no .map files shipped"; } || { fail "source maps exposed:"; echo "$maps" | sed 's/^/      /'; }

echo "[12] No exposed secrets / keys"
secrets=$(find "$DIR" -type f \( -iname '*.env*' -o -iname '*key*.json' -o -iname '*secret*' -o -iname '*credential*' \) 2>/dev/null | grep -v '_astro' || true)
{ [ -z "$secrets" ] && pass "no secrets/keys in build output"; } || { fail "possible secret files shipped:"; echo "$secrets" | sed 's/^/      /'; }

echo "[12b] Third-party embeds — every external host here must be disclosed in the privacy policy"
hosts=$(grep -rhoE '(src|href)="https?://[^"]+"' "$DIR" --include=*.html 2>/dev/null | grep -oE 'https?://[^"/]+' | sort | uniq -c | sort -rn)
if [ -n "$hosts" ]; then echo "$hosts" | sed 's/^/      /'; echo "      ^ cross-check each (analytics, maps, fonts, chat widgets, booking) against /privacy"; else pass "no external hosts embedded"; fi

echo
echo "== Legal items (verify by hand in code) =="
if [ -f "$DIR/privacy/index.html" ] || [ -f "$DIR/privacy.html" ]; then priv='page present'; else priv='MISSING'; fi
# One privacy page per language: /privacy plus e.g. /es/privacy (directory or file layout).
nprivacy=$(echo "$pages" | grep -cE '(^|/)privacy(\.html|/index\.html)$')
[ "$nprivacy" -gt 1 ] && priv="$priv ($nprivacy language versions)"
# A link counts with or without a locale prefix: /privacy, /es/privacy, /pt-br/privacy.
plinks=$(echo "$pages" | while IFS= read -r f; do [ -n "$f" ] && grep -lE 'href="(/|\./|\.\./)*([a-z]{2}(-[a-z]{2})?/)?privacy(\.html|/)?(#[^"]*)?"' "$f"; done | grep -c .)
echo "  [13] /privacy page exists + linked in footer?  ->  $priv; linked from $plinks of $(echo "$pages" | grep -c .) pages"
echo "  [14] data-collection disclosed (analytics/forms)?"
echo "  [15] AI usage disclosed (generated imagery = illustrative)?"
echo "  [16] third-party processors listed (analytics, maps, fonts, booking)?"
echo "  [17] testimonials real + sourced + permissioned?"
