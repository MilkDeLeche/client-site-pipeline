<#
    Install the pipeline skills into a Claude Code / Agent SDK skills directory,
    then install what they need (companion skills, ffmpeg, the PDF kit's Python
    packages) through client-site-pipeline\scripts\setup.mjs.

      ./install.ps1                    -> $HOME\.claude\skills\
      ./install.ps1 C:\path\to\skills  -> a custom location
      ./install.ps1 -Project           -> .\.claude\skills\ in the current repo
      ./install.ps1 -NoSetup           -> copy the skills only
#>
param(
    [string]$Path,
    [switch]$Project,
    [switch]$NoSetup
)

$ErrorActionPreference = 'Stop'
$src = Join-Path $PSScriptRoot 'skills'

if ($Project) {
    $dest = Join-Path (Get-Location) '.claude\skills'
} elseif ($Path) {
    $dest = $Path
} else {
    $dest = Join-Path $HOME '.claude\skills'
}

New-Item -ItemType Directory -Force -Path $dest | Out-Null

Get-ChildItem -Directory $src | ForEach-Object {
    $target = Join-Path $dest $_.Name
    if (Test-Path $target) { Remove-Item -Recurse -Force $target }
    Copy-Item -Recurse $_.FullName $target
    Write-Host "installed  $($_.Name)"
}

Write-Host ""
Write-Host "-> $dest"

if ($NoSetup) { exit 0 }

$setup = Join-Path $dest 'client-site-pipeline\scripts\setup.mjs'

# Node runs the setup (and every Astro build), so get it first.
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host ""
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host "Node not found; installing the LTS with winget..."
        winget install --id OpenJS.NodeJS.LTS -e --silent --accept-source-agreements --accept-package-agreements
        $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
    }
    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        Write-Host "Node 18+ is required. Install the LTS from https://nodejs.org, then run:"
        Write-Host "  node `"$setup`""
        exit 1
    }
}

Write-Host ""
node $setup
exit $LASTEXITCODE
