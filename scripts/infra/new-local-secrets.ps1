[CmdletBinding()]
param(
    [ValidateSet('dev', 'test', 'staging')]
    [string]$Environment = 'dev',
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$target = Join-Path $root 'deploy/compose/.env'
if ((Test-Path -LiteralPath $target) -and -not $Force) {
    throw "Refusing to overwrite existing ignored secret file: $target"
}

function New-HexSecret {
    $bytes = New-Object byte[] 32
    [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
    return [BitConverter]::ToString($bytes).Replace('-', '').ToLowerInvariant()
}

function New-KafkaClusterId {
    $bytes = New-Object byte[] 16
    [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
    return [Convert]::ToBase64String($bytes).TrimEnd('=').Replace('+', '-').Replace('/', '_')
}

$lines = @(
    "COMPOSE_PROJECT_NAME=twilight-$Environment",
    "INFRA_ENV=$Environment",
    "KAFKA_TOPIC_PREFIX=twilight-$Environment",
    "POSTGRES_ADMIN_PASSWORD=$(New-HexSecret)",
    "ACCOUNT_DB_PASSWORD=$(New-HexSecret)",
    "SOCIAL_DB_PASSWORD=$(New-HexSecret)",
    "CHAT_DB_PASSWORD=$(New-HexSecret)",
    "FEED_DB_PASSWORD=$(New-HexSecret)",
    "VALKEY_PASSWORD=$(New-HexSecret)",
    "KAFKA_CLUSTER_ID=$(New-KafkaClusterId)"
)
[System.IO.File]::WriteAllLines($target, $lines, [System.Text.UTF8Encoding]::new($false))
Write-Output "Created ignored local environment file for $Environment at deploy/compose/.env."
