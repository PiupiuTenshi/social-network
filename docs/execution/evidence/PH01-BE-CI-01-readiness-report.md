# Definition of Ready — PH01-BE-CI-01

- TASK_ID: `PH01-BE-CI-01`
- Scope: repository CI workflows, deterministic validation scripts, SBOM/checksum artifacts, local CI verification, and the remote branch ruleset after the first approved source push.
- Owner boundary: CI governs verification only. It does not change product contracts, data ownership, runtime configuration, migrations, or production.

## Inputs confirmed

- `PH01-BE-PLATFORM-01` is `DONE`; its review explicitly leaves service-owned runtime faults and BOLA checks to later feature tasks.
- `TwightLight.slnx` is the only solution artifact. Architecture and migration verification are executable console harnesses, not `dotnet test` projects.
- The frontend workspace has locked `npm ci`, `lint`, `typecheck`, `test:foundation`, `test:adapters`, and `build` commands.
- Current `ci.yml` can incorrectly skip backend because it searches only for `*.sln`, and can incorrectly pass frontend because it uses `--if-present`.
- The remote `PiupiuTenshi/social-network` is public but empty: GitHub reports no default branch and no rulesets. The local branch is `master`; the intended protected branch is `main`.

## Delivery and verification

CI will replace detection/skip behavior with explicit governance, backend (Linux and Windows), frontend, security/SBOM and documentation jobs. Missing expected projects, scripts, dependency manifests or generated checksum artifacts will fail the relevant job. The workflow will generate dependency inventories and a CycloneDX SBOM from restored .NET assets and the locked npm dependency graph, then upload artifacts with SHA-256 manifests.

Local verification will run each known command, unit-test the CI helper scripts, parse the workflow, execute the gate validator on Linux-compatible Python, and inspect generated SBOM/checksums. The remote process will create the initial `main` candidate only after local checks pass, wait for real GitHub status checks, then apply a `main` ruleset requiring pull requests and the actual workflow contexts. No secret is added to files, logs, artifacts or evidence.

## Stop conditions

Stop if an expected command, lockfile, remote repository ownership, required status context, or ruleset API capability differs from the evidence. The remote ruleset is not claimed configured until its returned GitHub configuration is captured. No production deployment, migration or credential change is in scope.
