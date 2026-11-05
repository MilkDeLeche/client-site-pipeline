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
 * Installed too: Google Chrome and Python 3.9+ with the pitch kit packages
 * (client-web-delivery/scripts/requirements.txt), for the pitch kit.
 * Optional: reportlab and pypdf, for brand-discovery's PDF kit.
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
const pitchRequirements = join(skillsDir, 'client-web-delivery', 'scripts', 'requirements.txt');

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
const venvPython = WIN ? join(pdfVenv, 'Scripts', 'python.exe') : join(pdfVenv, 'bin', 'python');

// Installs one Python kit from its requirements file: a user install first,
// a private environment where user installs are blocked (PEP 668).
function pythonKit(py, label, requirements, imports, fallback) {
  const ready = ([cmd, pre]) => run(cmd, [...pre, '-c', `import ${imports}`]).ok;
  if (!py) { report(label, false, `Python not found; ${fallback}`, false); return; }
  if (ready(py) || (existsSync(venvPython) && ready([venvPython, []]))) {
    report(label, true, `ready: ${ready(py) ? [py[0], ...py[1]].join(' ') : venvPython}`, false);
    return;
  }
  if (CHECK_ONLY) {
    report(label, false, `missing: ${[py[0], ...py[1]].join(' ')} -m pip install --user -r "${requirements}"`, false);
    return;
  }
  const [cmd, pre] = py;
  console.log(`  installing ${label}...`);
  let ok = run(cmd, [...pre, '-m', 'pip', 'install', '--user', '-r', requirements], { quiet: false }).ok && ready(py);
  let using = [cmd, ...pre].join(' ');
  if (!ok) {
    console.log(`  user install not allowed here; using ${pdfVenv}`);
    ok = (existsSync(venvPython) || run(cmd, [...pre, '-m', 'venv', pdfVenv], { quiet: false }).ok)
      && run(venvPython, ['-m', 'pip', 'install', '-r', requirements], { quiet: false }).ok
      && ready([venvPython, []]);
    using = venvPython;
  }
  report(label, ok, ok ? `ready: ${using}` : `install failed; ${fallback}`, false);
}

let py = findPython();
if (!py && !CHECK_ONLY) {
  installWith('Python', WIN
    ? [['winget', ['install', '--id', 'Python.Python.3.12', '-e', '--silent', '--accept-source-agreements', '--accept-package-agreements']]]
    : MAC ? [['brew', ['install', 'python']]] : []);
  py = findPython();
}

if (!SKIP_OPTIONAL) {
  pythonKit(py, 'PDF kit (reportlab, pypdf)', pdfRequirements, 'reportlab, pypdf', 'the PDF kit stays off, ask by text or call');
}

// 5. Pitch kit (client-web-delivery → "Pitch kit"): Google Chrome renders the
// poster pages and drives the screenshots; Python makes and checks the QR.
const CHROME_PATHS = WIN
  ? [join(process.env.ProgramFiles || 'C:\\Program Files', 'Google', 'Chrome', 'Application', 'chrome.exe'),
     join(process.env['ProgramFiles(x86)'] || 'C:\\Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe'),
     join(process.env.LOCALAPPDATA || '', 'Google', 'Chrome', 'Application', 'chrome.exe')]
  : MAC ? ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'] : [];
const chromeFound = () => CHROME_PATHS.some((p) => existsSync(p))
  || ['google-chrome', 'google-chrome-stable', 'chromium'].some((c) => has(c));
if (chromeFound()) {
  report('Google Chrome', true, 'installed', false);
} else if (CHECK_ONLY) {
  report('Google Chrome', false, 'missing', false);
} else {
  const ok = installWith('Google Chrome', WIN
    ? [['winget', ['install', '--id', 'Google.Chrome', '-e', '--silent', '--accept-source-agreements', '--accept-package-agreements']]]
    : MAC ? [['brew', ['install', '--cask', 'google-chrome']]] : []) && chromeFound();
  report('Google Chrome', ok, ok ? 'installed now' : (WIN || MAC ? 'install failed; the pitch kit can\'t render' : 'missing: install Chrome or Chromium with your package manager'), false);
}
pythonKit(py, 'Pitch kit (QR, shots, render)', pitchRequirements, 'qrcode, PIL, cv2, numpy, playwright, pypdf', 'the pitch kit can\'t make its QR or pages');

// Summary
console.log('\nClient Site Pipeline setup');
for (const r of results) {
  console.log(`  ${r.ok ? 'ok     ' : r.required ? 'MISSING' : 'off    '}  ${r.item.padEnd(28)} ${r.note}`);
}
const missing = results.filter((r) => r.required && !r.ok);
console.log(missing.length ? `\n${missing.length} required item(s) missing.` : '\nReady.');
process.exit(missing.length ? 1 : 0);
