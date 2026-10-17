<#
    Install the pipeline skills into a Claude Code / Agent SDK skills directory.

      ./install.ps1                    -> $HOME\.claude\skills\
      ./install.ps1 C:\path\to\skills  -> a custom location
      ./install.ps1 -Project           -> .\.claude\skills\ in the current repo
#>
param(
    [string]$Path,
    [switch]$Project
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

# Required companion skills (see client-site-pipeline -> "Required companion skills").
$missing = @('copywriting', 'antislop') | Where-Object { -not (Test-Path (Join-Path $dest $_)) }
if ($missing) {
    Write-Host ""
    Write-Host "Required companion skills missing: $($missing -join ', ')"
    Write-Host "  npx skills add coreyhaines31/marketingskills --skill copywriting -g"
    Write-Host "  npx skills add miqdadbadjuber/anti-slop -g"
}
