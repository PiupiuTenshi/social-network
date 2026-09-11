[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$composeFile = Join-Path $root 'deploy/compose/compose.infrastructure.yml'
$envFile = Join-Path $root 'deploy/compose/.env'
if (-not (Test-Path -LiteralPath $envFile)) { throw 'Missing deploy/compose/.env. Run new-local-secrets.ps1 first.' }

$compose = @('compose', '--env-file', $envFile, '-f', $composeFile)
function Invoke-Compose {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments)
    & docker @compose @Arguments
    if ($LASTEXITCODE -ne 0) { throw "docker compose failed: $($Arguments -join ' ')" }
}

# Required Compose variables must fail before any container is started.
$missingEnv = [System.IO.Path]::GetTempFileName()
try {
    Get-Content -LiteralPath $envFile | Where-Object { $_ -notmatch '^VALKEY_PASSWORD=' } | Set-Content -LiteralPath $missingEnv -Encoding utf8
    $missingConfig = Start-Process -FilePath docker -ArgumentList @('compose', '--env-file', $missingEnv, '-f', $composeFile, 'config', '--quiet') -WindowStyle Hidden -PassThru -Wait
    if ($missingConfig.ExitCode -eq 0) { throw 'Compose accepted a missing required VALKEY_PASSWORD.' }
}
finally { Remove-Item -LiteralPath $missingEnv -Force -ErrorAction SilentlyContinue }

Invoke-Compose up --detach --wait --wait-timeout 180

# No service may bind a host port; all traffic stays on the internal Compose network.
$containerIds = & docker @compose ps -q
if ($LASTEXITCODE -ne 0 -or -not $containerIds) { throw 'No infrastructure containers are running.' }
foreach ($containerId in $containerIds) {
    $bindings = & docker inspect --format '{{json .HostConfig.PortBindings}}' $containerId
    if ($LASTEXITCODE -ne 0 -or $bindings.Trim() -ne '{}') { throw "Container $containerId publishes host ports: $bindings" }
}

# A service credential can use its owned database, but cannot CONNECT to another service database.
$ownedDatabaseCommand = @'
PGPASSWORD=$ACCOUNT_DB_PASSWORD psql -h postgres -U account_app -d account_db -v ON_ERROR_STOP=1 -Atc 'select current_database() || chr(58) || current_user' | grep -qx account_db:account_app
'@
Invoke-Compose exec -T postgres sh -ec $ownedDatabaseCommand
$crossDatabaseCommand = @'
if PGPASSWORD=$ACCOUNT_DB_PASSWORD psql -h postgres -U account_app -d social_db -v ON_ERROR_STOP=1 -c 'select 1'; then
  echo cross-database-credential-access-was-allowed >&2
  exit 1
fi
'@
& docker @compose exec -T postgres sh -ec $crossDatabaseCommand
if ($LASTEXITCODE -ne 0) { throw 'Account credential accessed social_db.' }

# The profile-gated runner is explicit and idempotent. It is never part of normal `up`.
& docker @compose run --rm --no-deps -e 'TARGET_DATABASE=account_db' -e 'MIGRATION_ID=infra-bootstrap-v1' migration-runner
if ($LASTEXITCODE -ne 0) { throw 'Initial migration runner failed.' }
& docker @compose run --rm --no-deps -e 'TARGET_DATABASE=account_db' -e 'MIGRATION_ID=infra-bootstrap-v1' migration-runner
if ($LASTEXITCODE -ne 0) { throw 'Idempotent migration runner failed.' }

# A second runner against the same database must fail while the first holds its advisory transaction lock.
$stdout = [System.IO.Path]::GetTempFileName(); $stderr = [System.IO.Path]::GetTempFileName()
try {
    $firstRunnerCommand = "docker compose --env-file `"$envFile`" -f `"$composeFile`" run --rm --no-deps -e TARGET_DATABASE=account_db -e MIGRATION_ID=infra-lock-probe-v1 -e MIGRATION_LOCK_HOLD_SECONDS=8 migration-runner"
    $firstRunner = Start-Process -FilePath $env:ComSpec -ArgumentList @('/d', '/s', '/c', $firstRunnerCommand) -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
    Start-Sleep -Seconds 2
    $concurrentLockCheckCommand = @'
PGPASSWORD=$POSTGRES_PASSWORD psql -h postgres -U $POSTGRES_USER -d account_db -v ON_ERROR_STOP=1 -Atc 'select pg_try_advisory_lock(410001)' | grep -qx f
'@
    Invoke-Compose exec -T postgres sh -ec $concurrentLockCheckCommand
    $firstRunner.WaitForExit()
    $lockProbeReceiptCommand = @'
PGPASSWORD=$ACCOUNT_DB_PASSWORD psql -h postgres -U account_app -d account_db -v ON_ERROR_STOP=1 -Atc 'select migration_id from infrastructure_migration_ledger where migration_id = $$infra-lock-probe-v1$$' | grep -qx infra-lock-probe-v1
'@
    Invoke-Compose exec -T postgres sh -ec $lockProbeReceiptCommand
}
finally { Remove-Item -LiteralPath $stdout, $stderr -Force -ErrorAction SilentlyContinue }

# PostgreSQL retains the infrastructure ledger across restart.
Invoke-Compose restart postgres
Invoke-Compose up --detach --wait --wait-timeout 180
$ledgerCommand = @'
PGPASSWORD=$ACCOUNT_DB_PASSWORD psql -h postgres -U account_app -d account_db -v ON_ERROR_STOP=1 -Atc 'select migration_id from infrastructure_migration_ledger where migration_id = $$infra-bootstrap-v1$$' | grep -qx infra-bootstrap-v1
'@
Invoke-Compose exec -T postgres sh -ec $ledgerCommand
Write-Output 'PostgreSQL ledger retained after restart.'

# Restore only to a new isolated probe database. No existing database is dropped or overwritten.
$restoreCommand = @'
set -eu
export PGPASSWORD=$POSTGRES_PASSWORD
restore_db=infra_restore_probe_$(date +%s)
pg_dump -U $POSTGRES_USER -d account_db -Fc -f /tmp/account_db.dump
createdb -U $POSTGRES_USER $restore_db
pg_restore -U $POSTGRES_USER -d $restore_db /tmp/account_db.dump
psql -U $POSTGRES_USER -d $restore_db -Atc 'select migration_id from infrastructure_migration_ledger where migration_id = $$infra-bootstrap-v1$$' | grep -qx infra-bootstrap-v1
'@
Invoke-Compose exec -T postgres sh -ec $restoreCommand
Write-Output 'Isolated PostgreSQL restore verified.'

Write-Output 'Infrastructure verification passed: config, health, internal ports, ACL, migration lock, PostgreSQL restart and isolated restore. Run verify-kafka-persistence.ps1 for Kafka persistence.'
