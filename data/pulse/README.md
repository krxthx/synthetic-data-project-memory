# Pulse Store Operations Intelligence

Pulse creates a unified operational intelligence and alerting layer for Contoso's regional stores. The project brings store telemetry and business KPIs into one governed view so operations teams can identify issues consistently across regions.

## Scope

- Domain: Retail Operations
- Core team: 14 project members, plus shared enterprise specialists
- Dataset records: 360
- Primary outcome: consistent operational alerts and investigation workflows across stores

## Key project decisions

- Phase 1 alerts focus on store operations, not employee-level scoring.
- Fifteen-minute analytical latency is accepted. Real-time streaming is deferred.
- The Midwest region is the first production pilot.
- Pulse uses Contoso's shared analytical data platform.
- Enterprise KPI definitions override legacy regional scorecard definitions.

## Important dependencies

Pulse shares analytical platform capacity and batch-window constraints with Orbit. Shared data-platform architecture and data-quality guidance is owned by enterprise specialists, which creates realistic cross-project scheduling and governance dependencies.

## People and expertise

The project includes leadership, project management, product, business analysis, solution and enterprise architecture, engineering, data engineering, QA, change management, client roles, and shared platform SMEs. `people.json` and `artifacts/project_roster.csv` describe each person's expertise, responsibilities, and delivery history.

## Synthetic data sources

- `teams.jsonl`: operational discussions, risks, KPI debates, and dependency updates
- `outlook.jsonl`: steering, client, leadership, and escalation emails
- `transcript.jsonl`: steering committee and working-session transcripts
- `sharepoint.jsonl`: business announcements, status reports, decisions, and client updates
- `onedrive.jsonl`: implementation specs, test plans, working notes, and process maps
- `confluence.jsonl`: architecture decisions, implementation decisions, anti-patterns, and dependency notes

## Rich artifacts

The `artifacts/` folder includes a steering committee PDF, implementation DOCX, project roster CSV, risk register CSV, and architecture diagram. The same project facts intentionally appear in different forms and at different points in time.

## Memory challenges represented

Pulse contains changing KPI definitions, point-in-time status snapshots, platform-capacity tradeoffs, regional conflicts, pilot decisions, cross-project dependencies, adoption risks, and historical information that should remain searchable even after it is superseded.