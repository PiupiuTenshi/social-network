# Local development: PH00 toolchain harness

This document is the verified command reference for the PH00 harness. It does not
replace the root local-development guide, which remains an input artifact for this
gated subtask.

## Requirements

- .NET SDK `10.0.204`, selected by `global.json`.
- Node `22.19.0`, selected by `.nvmrc`.
- npm via `npm.cmd` on this Windows workstation because the PowerShell npm script is
  blocked by the local execution policy.
- Docker Compose is optional. The image pin is in
  `deploy/compose/compose.toolchain.yml`; its daemon was unavailable during this task.

## Backend and harness commands

```powershell
dotnet tool restore
dotnet restore TwightLight.slnx --locked-mode
dotnet build TwightLight.slnx --no-restore
dotnet run --project tests/Architecture/Architecture.Harness --no-build
dotnet run --project tests/Integration/Migration.Harness --no-build
```

`Migration.Harness` creates and migrates a disposable SQLite database under
`work/toolchain-migration/`. It does not access a shared, production, or Docker
database.

## Angular commands

```powershell
Set-Location frontend
npm.cmd ci
npm.cmd run build
```
