#!/usr/bin/env node
/**
 * Pipeline setup: checks every tool the pipeline needs and installs what's missing.
 * Agents run this themselves before step 0; the user never has to.
 *
 *   node <skills>/client-site-pipeline/scripts/setup.mjs            check and install
 *   node <skills>/client-site-pipeline/scripts/setup.mjs --check    report only
 *   node <skills>/client-site-pipeline/scripts/setup.mjs --no-optional   skip the PDF kit
 *
 * Required: Node 18+, the companion skills (copywriting, antislop), ffmpeg.
 * Optional: Python 3.9+ with reportlab and pypdf, for brand-discovery's PDF kit.
 * Exit code 1 only when a required item is still missing at the end.
 */
import { spawnSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { homedir, platform } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const args = new Set(process.argv.slice(2));
const CHECK_ONLY = args.has('--check');
const SKIP_OPTIONAL = args.has('--no-optional');
const WIN = platform() === 'win32';
const MAC = platform() === 'darwin';

const here = dirname(fileURLToPath(import.meta.url));
const skillsDir = resolve(here, '..', '..');
const globalSkills = join(homedir(), '.claude', 'skills');
const pdfRequirements = join(skillsDir, 'brand-discovery', 'scripts', 'requirements.txt');
const pdfVenv = join(homedir(), '.client-site-pipeline', 'pyenv');

const COMPANIONS = [
  { name: 'copywriting', args: ['coreyhaines31/marketingskills', '--skill', 'copywriting'] },
  { name: 'antislop', args: ['miqdadbadjuber/anti-slop'] },
];

const results = [];
const report = (item, ok, note, required = true) => results.push({ item, ok, note, required });

function run(cmd, cmdArgs, { quiet = true } = {}) {
  // npx is a .cmd shim on Windows and needs a shell; nothing else gets one, so
  // arguments (inline Python, paths with spaces) pass through untouched.
  const r = spawnSync(cmd, cmdArgs, { encoding: 'utf8', shell: WIN && cmd === 'npx', stdio: quiet ? 'pipe' : 'inherit' });
  return { ok: r.status === 0, out: `${r.stdout || ''}${r.stderr || ''}`.trim() };
}

const has = (cmd, versionArg = '--version') => run(cmd, [versionArg]).ok;

function installWith(label, attempts) {
  for (const [cmd, cmdArgs] of attempts) {
    if (!has(cmd)) continue;
    console.log(`  installing ${label} with ${cmd}...`);
    if (run(cmd, cmdArgs, { quiet: false }).ok) return true;
  }
  return false;
}

// 1. Node
const [major] = process.versions.node.split('.').map(Number);
report('Node 18+', major >= 18, `found ${process.versions.node}${major >= 18 ? '' : ': install the LTS from nodejs.org'}`);

// 2. Companion skills
for (const c of COMPANIONS) {
  const found = [skillsDir, globalSkills].some((d) => existsSync(join(d, c.name, 'SKILL.md')));
  if (found) { report(`skill: ${c.name}`, true, 'installed'); continue; }
  if (CHECK_ONLY) { report(`skill: ${c.name}`, false, `missing: npx -y skills add ${c.args.join(' ')} -g -a claude-code -y`); continue; }
  console.log(`  installing companion skill ${c.name}...`);
  const ok = run('npx', ['-y', 'skills', 'add', ...c.args, '-g', '-a', 'claude-code', '-y'], { quiet: false }).ok
    && [skillsDir, globalSkills].some((d) => existsSync(join(d, c.name, 'SKILL.md')));
  report(`skill: ${c.name}`, ok, ok ? 'installed now; it loads in the next session (read its SKILL.md directly for this one)' : 'install failed');
}

// 3. ffmpeg (reading motion out of template videos)
if (has('ffmpeg', '-version')) {
  report('ffmpeg', true, 'installed');
} else if (CHECK_ONLY) {
  report('ffmpeg', false, 'missing');
} else {
  const ok = installWith('ffmpeg', WIN
    ? [['winget', ['install', '--id', 'Gyan.FFmpeg', '-e', '--silent', '--accept-source-agreements', '--accept-package-agreements']]]
    : MAC ? [['brew', ['install', 'ffmpeg']]] : []);
  report('ffmpeg', ok, ok
    ? 'installed now; open a new terminal so it is on PATH'
    : (WIN || MAC ? 'install failed' : 'missing: install it with your package manager (sudo apt install ffmpeg)'));
}

// 4. Python packages for the optional PDF kit
function findPython() {
  for (const [cmd, pre] of [['python3', []], ['python', []], ['py', ['-3']]]) {
    const r = run(cmd, [...pre, '-c', 'import sys; print(sys.version_info >= (3, 9))']);
    if (r.ok && r.out.endsWith('True')) return [cmd, pre];
  }
  return null;
}
const pdfReady = ([cmd, pre]) => run(cmd, [...pre, '-c', 'import reportlab, pypdf']).ok;
const venvPython = WIN ? join(pdfVenv, 'Scripts', 'python.exe') : join(pdfVenv, 'bin', 'python');

if (!SKIP_OPTIONAL) {
  let py = findPython();
  if (!py && !CHECK_ONLY) {
    installWith('Python', WIN
      ? [['winget', ['install', '--id', 'Python.Python.3.12', '-e', '--silent', '--accept-source-agreements', '--accept-package-agreements']]]
      : MAC ? [['brew', ['install', 'python']]] : []);
    py = findPython();
  }
  if (!py) {
    report('PDF kit (Python 3.9+)', false, 'Python not found; the PDF kit stays off, ask by text or call', false);
  } else if (pdfReady(py) || (existsSync(venvPython) && pdfReady([venvPython, []]))) {
    report('PDF kit (reportlab, pypdf)', true, `ready: ${pdfReady(py) ? [py[0], ...py[1]].join(' ') : venvPython}`, false);
  } else if (CHECK_ONLY) {
    report('PDF kit (reportlab, pypdf)', false, `missing: ${[py[0], ...py[1]].join(' ')} -m pip install --user -r "${pdfRequirements}"`, false);
  } else {
    const [cmd, pre] = py;
    console.log('  installing the PDF kit packages...');
    let ok = run(cmd, [...pre, '-m', 'pip', 'install', '--user', '-r', pdfRequirements], { quiet: false }).ok && pdfReady(py);
    let using = [cmd, ...pre].join(' ');
    if (!ok) {
      // Systems that block user installs (PEP 668) get a private environment instead.
      console.log(`  user install not allowed here; creating ${pdfVenv}`);
      ok = run(cmd, [...pre, '-m', 'venv', pdfVenv], { quiet: false }).ok
        && run(venvPython, ['-m', 'pip', 'install', '-r', pdfRequirements], { quiet: false }).ok
        && pdfReady([venvPython, []]);
      using = venvPython;
    }
    report('PDF kit (reportlab, pypdf)', ok, ok ? `ready: ${using}` : 'install failed; ask by text or call', false);
  }
}

// Summary
console.log('\nClient Site Pipeline setup');
for (const r of results) {
  console.log(`  ${r.ok ? 'ok     ' : r.required ? 'MISSING' : 'off    '}  ${r.item.padEnd(28)} ${r.note}`);
}
const missing = results.filter((r) => r.required && !r.ok);
console.log(missing.length ? `\n${missing.length} required item(s) missing.` : '\nReady.');
process.exit(missing.length ? 1 : 0);
