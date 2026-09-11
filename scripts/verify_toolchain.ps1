$ErrorActionPreference = 'Stop'

dotnet tool restore
if ($LASTEXITCODE -ne 0) { throw 'dotnet tool restore failed' }

dotnet restore TwightLight.slnx --locked-mode
if ($LASTEXITCODE -ne 0) { throw 'dotnet restore failed' }

dotnet build TwightLight.slnx --no-restore
if ($LASTEXITCODE -ne 0) { throw 'dotnet build failed' }

dotnet run --project tests/Architecture/Architecture.Harness --no-build
if ($LASTEXITCODE -ne 0) { throw 'architecture harness failed' }

dotnet run --project tests/Integration/Migration.Harness --no-build
if ($LASTEXITCODE -ne 0) { throw 'migration harness failed' }
