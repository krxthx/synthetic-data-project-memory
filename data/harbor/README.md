# Harbor Identity Modernization

Harbor modernizes Contoso's enterprise identity, provisioning, and access-governance foundation. It coordinates application migration, role design, provisioning compatibility, privileged access, and interim dependencies for other transformation projects.

## Scope

- Domain: Cybersecurity
- Core team: 19 project members, plus shared enterprise specialists
- Dataset records: 480
- Primary outcome: modern identity and access controls with explicit migration waves and governed exceptions

## Key project decisions

- Applications migrate in waves based on criticality and provisioning readiness.
- Role-based access is the baseline, with governed exceptions.
- Harbor provides an interim SSO bridge for the Atlas pilot.
- Legacy applications without SCIM are not forced into phase 1.
- Privileged accounts require step-up controls before migration.

## Important dependencies

Harbor directly supports Atlas through the interim SSO bridge and influences Nova through account-team authorization mappings. Identity decisions therefore appear as both local Harbor decisions and cross-project dependencies in the wider Contoso corpus.

## People and expertise

The project includes executive and business ownership, program and project management, product, BAs, solution and enterprise architects, engineering, QA, change roles, client stakeholders, security specialists, and shared enterprise SMEs. `people.json` and `artifacts/project_roster.csv` describe expertise, responsibilities, and delivery history.

## Synthetic data sources

- `teams.jsonl`: migration discussions, role-mapping issues, dependency updates, and SME requests
- `outlook.jsonl`: leadership, client, escalation, and correction threads
- `transcript.jsonl`: steering committee and technical working-session transcripts
- `sharepoint.jsonl`: business announcements, status reports, steering decisions, and client updates
- `onedrive.jsonl`: implementation specs, test plans, working notes, and process maps
- `confluence.jsonl`: architecture decisions, implementation decisions, anti-patterns, and dependency notes

## Rich artifacts

The `artifacts/` folder includes a steering committee PDF, implementation DOCX, project roster CSV, risk register CSV, and architecture diagram. The artifacts intentionally overlap with other sources so memory compilation must reason about recency, authority, and provenance.

## Memory challenges represented

Harbor contains migration-wave changes, role-mapping ambiguity, privileged-access constraints, legacy-system exceptions, cross-project commitments, client and security rationale, historical decisions, and older implementation paths that remain useful even after being superseded.