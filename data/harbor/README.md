# Harbor Identity Modernization

**Organization:** Meridian Group  
**Project ID:** HARBOR  
**Domain:** Cybersecurity  
**Records:** 480  
**Core team:** 19 members plus shared enterprise SMEs

## Purpose
Modernize enterprise identity, provisioning and access governance.

## Memory storyline
Harbor covers SSO migration, RBAC, SCIM gaps, privileged access, directory cleanup and the interim Atlas authentication bridge. It includes security leadership, client, BA, QA and architecture perspectives across a long-running migration.

## Key decisions
- Applications migrate in waves based on criticality and readiness.
- RBAC is the baseline, with governed exceptions.
- Harbor provides an interim SSO bridge for the Atlas pilot.
- Legacy applications without SCIM are not forced into phase 1.
- Privileged accounts require step-up controls before migration.

## Dependencies
- **Atlas:** pilot authentication dependency.
- **Nova:** account-team authorization model.

## Sources
`records.jsonl` is the canonical normalized corpus. The six directly readable source-specific files used to rebuild it are in `sources/`.

## Artifacts
`artifacts/` contains 17 directly readable architecture, decision, requirements, implementation, readiness, quality, risk, roster and casebook artifacts.

## People
See `../people.json` for project members, SMEs, responsibilities and what they built.
