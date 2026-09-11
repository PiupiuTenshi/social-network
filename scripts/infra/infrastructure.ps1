[CmdletBinding()]
param(
    [ValidateSet('up', 'down', 'status', 'config')]
    [string]$Action = 'up'
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$composeFile = Join-Path $root 'deploy/compose/compose.infrastructure.yml'
$envFile = Join-Path $root 'deploy/compose/.env'
if (-not (Test-Path -LiteralPath $envFile)) {
    throw 'Missing deploy/compose/.env. Run scripts/infra/new-local-secrets.ps1 first.'
}

$compose = @('compose', '--env-file', $envFile, '-f', $composeFile)
switch ($Action) {
    'up' { & docker @compose up --detach --wait --wait-timeout 180 }
    'down' { & docker @compose down }
    'status' { & docker @compose ps }
    'config' { & docker @compose config --quiet }
}
if ($LASTEXITCODE -ne 0) { throw "docker compose $Action failed" }
