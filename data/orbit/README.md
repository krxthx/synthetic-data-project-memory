# Orbit Financial Planning

Orbit replaces fragmented planning spreadsheets with a governed rolling-forecast and scenario-planning experience for Contoso Finance. The project connects authoritative ERP actuals to a shared analytical platform while keeping forecast ownership and approval with finance users.

## Scope

- Domain: Finance
- Core team: 15 project members, plus shared enterprise specialists
- Dataset records: 340
- Primary outcome: consistent monthly rolling forecasts, scenario planning, and traceable variance narratives

## Key project decisions

- Monthly rolling forecast replaces quarterly-only planning.
- ERP actuals remain authoritative. Manual spreadsheet adjustments are exceptions.
- Orbit uses the shared analytical platform that also supports Pulse.
- AI may draft variance narratives but cannot change forecasts.
- Scenario planning is phase 1 for finance leadership and phase 2 for business units.

## Important dependencies

Orbit shares analytical platform capacity, compute windows, and governance with Pulse. These shared constraints create realistic scheduling and prioritization discussions across otherwise separate projects.

## People and expertise

The project includes leadership, program and project management, product, BAs, architects, engineering and data specialists, QA, change management, client roles, and shared enterprise SMEs. `people.json` and `artifacts/project_roster.csv` document expertise, responsibilities, and what each person has built.

## Synthetic data sources

- `teams.jsonl`: forecasting discussions, platform constraints, business rules, and decision updates
- `outlook.jsonl`: leadership rationale, milestone communication, client feedback, and escalations
- `transcript.jsonl`: steering committee and finance working-session transcripts
- `sharepoint.jsonl`: business announcements, status reports, steering decisions, and client updates
- `onedrive.jsonl`: implementation specs, test plans, working notes, and process maps
- `confluence.jsonl`: architecture decisions, implementation decisions, anti-patterns, and dependency notes

## Rich artifacts

The `artifacts/` folder includes a steering committee PDF, implementation DOCX, project roster CSV, risk register CSV, and architecture diagram. These artifacts intentionally repeat and evolve information already present in the normalized source records.

## Memory challenges represented

Orbit includes authoritative-source rules, manual-adjustment exceptions, finance governance, AI scope boundaries, shared-platform contention, changing scenario-planning scope, point-in-time status snapshots, and business rationale distributed across leadership conversations and implementation artifacts.