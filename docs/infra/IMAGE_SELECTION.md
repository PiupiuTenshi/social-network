# PH01 image selection — 2026-09-09

| Service | Pinned image digest |
| --- | --- |
| PostgreSQL / migration runner | `postgres:17.11-alpine3.24@sha256:18cfe3ef5e6815560c98237d6216d1e5119702fb0f3894c8785dd58b8bbe5d73` |
| Kafka | `apache/kafka:4.3.1@sha256:77e3df9054047a88b520d0cc46e16696d3b22022e1d580aeccd2632df6532837` |
| Valkey | `valkey/valkey:8.1.10-alpine@sha256:d2e18f3410b6f616de1417f570fa55261af2898b9c5b2cfb6781ce2373ea43d1` |
| SeaweedFS | `chrislusf/seaweedfs:4.21@sha256:e0b528145ea514040ab00d03ff0833f56acb1f0e07aeab232e20485af9278fd8` |

The digests were observed from actual Docker pulls on this workstation. Review image
updates through a later infrastructure task, then repeat the local health and
persistence verification before accepting a new pin.
