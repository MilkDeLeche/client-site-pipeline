#!/usr/bin/env node
// Set up a new client project folder for the pipeline (references/kickoff.md).
//
//   node scaffold.mjs <folder> --name "Business Name"
//
// Makes the folders the steps write to, the gitignore entries that keep client
// prices and private files out of the repo, the state file, the capture Worker
// with its two tables, and the Cloudflare config. It never overwrites a file
// that already exists, so it is safe to run on a project that is half set up.
// It installs nothing: it prints the commands that add Astro and wrangler.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const args = process.argv.slice(2);
const nameAt = args.indexOf("--name");
const business = nameAt >= 0 ? args[nameAt + 1] : null;
const folder = args.find((a, i) => !a.startsWith("--") && i !== nameAt + 1);
if (!folder || !business) {
  console.error('Usage: node scaffold.mjs <folder> --name "Business Name"');
  process.exit(1);
}

const root = resolve(folder);
const here = dirname(fileURLToPath(import.meta.url));
const assets = join(here, "..", "assets");
const slug = business.toLowerCase().normalize("NFKD").replace(/[^\w\s-]/g, "").trim().replace(/[\s_]+/g, "-").slice(0, 40) || "client-site";
const today = new Date().toISOString().slice(0, 10);
const made = [];
const kept = [];

function file(path, content) {
  const target = join(root, path);
  if (existsSync(target)) return kept.push(path);
  mkdirSync(dirname(target), { recursive: true });
  writeFileSync(target, content, "utf8");
  made.push(path);
}

const fill = (text) => text.replaceAll("{{WORKER_NAME}}", slug).replaceAll("{{BUSINESS}}", business).replaceAll("{{DATE}}", today);
const asset = (path) => readFileSync(join(assets, path), "utf8");

for (const d of ["deliverables/owner-sheet/src", "deliverables/pitch/src", "deliverables/mockups/src", "deliverables/hype/src",
  "discovery", "intake", "reference", "assets/reference", "public", "src/data"]) {
  mkdirSync(join(root, d), { recursive: true });
}

file("worker/index.ts", asset("scaffold/worker/index.ts"));
file("worker/sql.d.ts", asset("scaffold/worker/sql.d.ts"));
file("migrations/0001_init.sql", asset("scaffold/migrations/0001_init.sql"));
file("wrangler.jsonc", fill(asset("scaffold/wrangler.jsonc")));
file("pipeline-state.md", asset("pipeline-state-template.md").replaceAll("{{BUSINESS}}", business).replace("| Started | {{date}} |", `| Started | ${today} |`));

// Add the ignore lines that are missing; leave the rest of the file alone.
const ignore = ["deliverables/", "discovery/", ".wrangler/", ".dev.vars", "reference/template*/", "node_modules/", "dist/", ".env", ".env.production"];
const ignorePath = join(root, ".gitignore");
const current = existsSync(ignorePath) ? readFileSync(ignorePath, "utf8") : "";
const have = new Set(current.split(/\r?\n/).map((l) => l.trim()));
const missing = ignore.filter((line) => !have.has(line));
if (missing.length) {
  const lead = current ? (current.endsWith("\n") ? "\n" : "\n\n") : "";
  const note = "# Pipeline: what goes to the owner by hand, what comes back, local secrets and saved templates stay out of the repo.\n";
  writeFileSync(ignorePath, current + lead + note + missing.join("\n") + "\n", "utf8");
  made.push(`.gitignore (+${missing.length} lines)`);
}

console.log(`${business} -> ${root}`);
for (const m of made) console.log(`  made  ${m}`);
for (const k of kept) console.log(`  kept  ${k} (already there)`);
const astro = existsSync(join(root, "package.json"))
  ? "(package.json exists: Astro is already here)"
  : "npm create astro@latest . -- --template minimal --install --no-git --yes";
console.log(`
Next, in ${root}:
  ${astro}
  npm install -D wrangler @cloudflare/workers-types
  add to package.json scripts:  "preview": "npm run build && wrangler dev",  "deploy": "npm run build && wrangler deploy"
Then start step 0. Git doesn't back up deliverables/ or discovery/.`);
