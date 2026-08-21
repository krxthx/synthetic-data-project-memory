# Pulse Store Operations Intelligence

**Organization:** Meridian Group  
**Project ID:** PULSE  
**Domain:** Retail Operations  
**Records:** 360  
**Core team:** 14 members plus shared enterprise SMEs

## Purpose
Create a unified operational intelligence and alerting layer for regional stores.

## Memory storyline
Pulse covers store telemetry, enterprise KPI definitions, alert thresholds, data quality, pilot rollout and shared analytical-platform capacity. The corpus includes regional disagreements, operational risks and dependencies that evolve over time.

## Key decisions
- Phase 1 focuses on store operations, not employee-level scoring.
- Fifteen-minute analytical latency is accepted; real-time streaming is deferred.
- Enterprise KPI definitions override legacy regional scorecards.
- Midwest is the first production pilot.

## Dependency
- **Orbit:** shared analytical-platform capacity and batch windows.

## Sources
`records.jsonl` is the canonical normalized corpus. The six directly readable source-specific files used to rebuild it are in `sources/`.

## Artifacts
`artifacts/` contains 18 directly readable architecture, decision, requirements, implementation, readiness, quality, risk, roster, casebook and contractual-scope artifacts.

## People
See `../people.json` for roles, SME areas, responsibilities and contribution history.
