#!/usr/bin/env node
// Keep a client project's private folders out of git, always (orchestrator, "Agent rule").
//
//   node guard_private.mjs [project folder]       (default: the current folder)
//
// 1. Adds `deliverables/` and `discovery/` to .gitignore if either is missing.
// 2. If git already tracks anything inside them, untracks it (`git rm -r --cached`):
//    the files stay on disk and leave the repo. Say so in the next commit message.
// 3. Installs a pre-commit hook in .git/hooks that refuses any commit staging a path
//    under deliverables/ or discovery/. The hook lives in .git, so it is never pushed.
//    An existing hook that isn't ours is left alone, with a warning.
//
// Safe to run any number of times. Run it on every project at the start of a session
// and before any commit. Prices, client answers and the owner's private details live in
// those folders, and a pipeline repo or a client repo may be public.
import { execFileSync } from "node:child_process";
import { chmodSync, existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";

const root = resolve(process.argv[2] || ".");
const PRIVATE = ["deliverables/", "discovery/"];
const MARK = "# client-site-pipeline: guard_private";
const report = [];

// 1. .gitignore
const ignorePath = join(root, ".gitignore");
const current = existsSync(ignorePath) ? readFileSync(ignorePath, "utf8") : "";
const have = new Set(current.split(/\r?\n/).map((l) => l.trim()));
const missing = PRIVATE.filter((p) => !have.has(p) && !have.has(p.replace(/\/$/, "")) && !have.has("/" + p));
if (missing.length) {
  const lead = current ? (current.endsWith("\n") ? "\n" : "\n\n") : "";
  writeFileSync(ignorePath, current + lead + "# What goes to the owner by hand and what comes back: never committed.\n" + missing.join("\n") + "\n", "utf8");
  report.push(`.gitignore: added ${missing.join(", ")}`);
} else {
  report.push(".gitignore: already ignores " + PRIVATE.join(" and "));
}

// 2 and 3 need a git repository.
const git = (...args) => execFileSync("git", ["-C", root, ...args], { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
let isRepo = false;
try {
  isRepo = git("rev-parse", "--is-inside-work-tree") === "true";
} catch {
  report.push("not a git repository yet: run this again after `git init`");
}

if (isRepo) {
  const tracked = git("ls-files", "--", ...PRIVATE).split("\n").filter(Boolean);
  if (tracked.length) {
    git("rm", "-r", "--cached", "--quiet", "--", ...PRIVATE.filter((p) => tracked.some((t) => t.startsWith(p))));
    report.push(`untracked ${tracked.length} file(s) under ${PRIVATE.join(" / ")} (still on disk). Commit this with a message that says so.`);
  } else {
    report.push("git tracks nothing under " + PRIVATE.join(" or "));
  }

  const hooksDir = join(git("rev-parse", "--absolute-git-dir"), "hooks");
  const hookPath = join(hooksDir, "pre-commit");
  const hook = `#!/bin/sh
${MARK}
# Refuses a commit that stages anything under deliverables/ or discovery/.
staged=$(git diff --cached --name-only --diff-filter=ACMR -- deliverables/ discovery/)
if [ -n "$staged" ]; then
  echo "Blocked: these are private (client prices, owner answers, deliverables) and stay out of git:" >&2
  echo "$staged" | sed 's/^/  /' >&2
  echo "Unstage them with: git rm -r --cached deliverables discovery" >&2
  exit 1
fi
`;
  if (!existsSync(hookPath)) {
    mkdirSync(hooksDir, { recursive: true });
    writeFileSync(hookPath, hook, "utf8");
    chmodSync(hookPath, 0o755);
    report.push("pre-commit hook installed (.git/hooks/pre-commit, never pushed)");
  } else if (readFileSync(hookPath, "utf8").includes(MARK)) {
    writeFileSync(hookPath, hook, "utf8");
    report.push("pre-commit hook already installed (refreshed)");
  } else {
    report.push("WARNING: .git/hooks/pre-commit exists and isn't ours. Left alone: add the check to it by hand, or rely on .gitignore.");
  }

  // Confirm git really ignores both folders now (a negation rule later in .gitignore could undo the entry).
  for (const p of PRIVATE) {
    try {
      execFileSync("git", ["-C", root, "check-ignore", "-q", "--no-index", p + "probe"], { stdio: "ignore" });
      report.push(`check: git ignores ${p}`);
    } catch {
      report.push(`WARNING: git does NOT ignore ${p}. Look for a "!" rule in .gitignore that brings it back.`);
    }
  }
}

console.log(root);
for (const line of report) console.log("  " + line);
