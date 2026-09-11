[CmdletBinding()]
param()

$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$composeFile = Join-Path $root 'deploy/compose/compose.infrastructure.yml'
$envFile = Join-Path $root 'deploy/compose/.env'
if (-not (Test-Path -LiteralPath $envFile)) { throw 'Missing deploy/compose/.env.' }

$compose = @('compose', '--env-file', $envFile, '-f', $composeFile)
$prefixLine = Get-Content -LiteralPath $envFile | Where-Object { $_ -match '^KAFKA_TOPIC_PREFIX=' }
if (-not $prefixLine) { throw 'KAFKA_TOPIC_PREFIX is required.' }
$topic = ($prefixLine -replace '^KAFKA_TOPIC_PREFIX=', '') + '-infra-probe'

& docker @compose exec -T kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --create --if-not-exists --topic $topic --partitions 1 --replication-factor 1
if ($LASTEXITCODE -ne 0) { throw 'Kafka probe topic could not be created.' }
& docker @compose restart kafka
if ($LASTEXITCODE -ne 0) { throw 'Kafka restart failed.' }
& docker @compose up --detach --wait --wait-timeout 180
if ($LASTEXITCODE -ne 0) { throw 'Kafka did not become healthy after restart.' }
$topics = @()
$retained = $false
for ($attempt = 1; $attempt -le 12; $attempt++) {
    $topics = & docker @compose exec -T kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --list
    if ($LASTEXITCODE -eq 0 -and $topics -contains $topic) { $retained = $true; break }
    Start-Sleep -Seconds 2
}
if (-not $retained) { throw "Kafka topic was not retained after restart: $topic" }
Write-Output 'Kafka probe topic retained after restart.'
