# Atlas Customer Onboarding

Atlas modernizes Contoso's enterprise customer onboarding journey from signed deal through production handoff. The project focuses on removing fragmented regional processes while preserving controlled exception handling and clear ownership of customer identity.

## Scope

- Domain: Customer Operations
- Core team: 17 project members, plus shared enterprise specialists
- Dataset records: 420
- Primary outcome: one traceable onboarding lifecycle with common stage definitions and governed regional variation

## Key project decisions

- Phase 1 covers enterprise onboarding. SMB onboarding is deferred.
- CRM remains authoritative for customer identity and onboarding status.
- High-risk onboarding exceptions require human approval.
- A common onboarding stage taxonomy is mandatory, with region-specific substeps allowed.
- Atlas uses an interim Harbor SSO bridge for the pilot instead of waiting for the full Harbor migration.

## Important dependencies

Atlas depends on Harbor for the interim SSO bridge and shares CRM data-quality concerns with Nova. These dependencies appear across Teams conversations, steering transcripts, Outlook threads, ADRs, and implementation specifications.

## People and expertise

The project includes business and executive ownership, program and project management, product, business analysis, architecture, engineering, QA, change management, client roles, and shared enterprise SMEs. `people.json` and `artifacts/project_roster.csv` describe roles, expertise, responsibilities, and what each member has built.

## Synthetic data sources

- `teams.jsonl`: working conversations, risks, corrections, SME requests, and decision updates
- `outlook.jsonl`: leadership, client, milestone, and escalation threads
- `transcript.jsonl`: calendar recording transcripts for steering committees and working sessions
- `sharepoint.jsonl`: business announcements, status reports, steering decisions, and client updates
- `onedrive.jsonl`: implementation specs, working notes, test plans, and process maps
- `confluence.jsonl`: ADRs, implementation decisions, anti-patterns, and dependency notes

## Rich artifacts

The `artifacts/` folder includes a steering committee PDF, implementation DOCX, risk register CSV, project roster CSV, and architecture diagram. These artifacts intentionally overlap with the normalized records so a memory compiler can reconcile duplicate, stale, and superseded information.

## Memory challenges represented

Atlas contains superseded assumptions, cross-project dependencies, business rationale, client feedback, SME ownership, architecture history, point-in-time status reports, exception policies, and decisions whose rationale is distributed across multiple sources.