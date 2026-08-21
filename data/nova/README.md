# Nova Sales Opportunity Intelligence

Nova assists Contoso's strategic account teams with evidence-backed opportunity recommendations. It combines CRM signals, approved meeting evidence, and account context while keeping sellers in control of final decisions.

## Scope

- Domain: Sales
- Core team: 16 project members, plus shared enterprise specialists
- Dataset records: 400
- Primary outcome: useful and explainable opportunity guidance without autonomous CRM decision-making

## Key project decisions

- Nova recommends actions but cannot automatically change CRM opportunity stages.
- Every recommendation must cite CRM, meeting, or account-plan evidence.
- The initial pilot is limited to strategic account directors.
- Expansion requires human-reviewed quality and hallucination thresholds.
- Nova may only surface evidence already visible to the requesting account team.

## Important dependencies

Nova depends on Atlas for shared CRM customer and account identity quality, and on Harbor for account-team authorization mappings. It also uses shared analytical capabilities governed by Contoso's data-platform specialists.

## People and expertise

The project includes leadership, program and project management, product, BAs, architects, engineers, data specialists, QA, client roles, and shared SMEs. `people.json` and `artifacts/project_roster.csv` capture expertise, responsibilities, and what each person has built.

## Synthetic data sources

- `teams.jsonl`: product debates, evidence-quality discussions, permissions questions, and decision updates
- `outlook.jsonl`: client feedback, leadership rationale, risk escalations, and corrections
- `transcript.jsonl`: calendar recording transcripts for steering and working sessions
- `sharepoint.jsonl`: status reports, steering decisions, business announcements, and client updates
- `onedrive.jsonl`: implementation specs, test plans, working notes, and process maps
- `confluence.jsonl`: ADRs, implementation decisions, anti-patterns, and dependency notes

## Rich artifacts

The `artifacts/` folder includes a steering committee PDF, implementation DOCX, project roster CSV, risk register CSV, and architecture diagram. The artifact set is intentionally redundant with the normalized corpus to exercise evidence reconciliation.

## Memory challenges represented

Nova includes evidence provenance, human-review constraints, client feedback, permissions decisions, AI-quality thresholds, shared CRM dependencies, rejected assumptions, changing pilot scope, and historical rationale that should remain available after decisions evolve.