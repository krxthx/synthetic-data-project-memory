# Pulse Project Memory Casebook

## Product boundary and workforce risk

Pulse is a store-operations intelligence product, not an employee-scoring system. Early discussions exposed the temptation to reuse store signals for individual performance ranking. Steering rejected that expansion because telemetry quality, workforce governance and intended operational use were not designed for employee-level conclusions.

Dashboards and alerts should therefore describe store conditions, equipment, inventory flow and operational exceptions. A local export or derived metric must not quietly reintroduce individual scoring. Acceptance testing includes role-based visibility and verifies that drill-down behavior does not expose prohibited employee inferences.

Evidence: `TM-00177`, `OL-00076`, `TR-00051`, `CF-00045`, `OD-00035`.

## Latency as an operating contract

Phase one accepts fifteen-minute analytical latency and defers real-time streaming. This was not merely a cost optimization: store users need predictable, explainable alerts more than sub-second updates built on inconsistent telemetry. The batch window also creates an explicit dependency on shared analytical-platform capacity.

Operational messaging must show observation time, processing time and alert time so users do not mistake a delayed signal for current state. Late or duplicated batches require idempotent processing. A missed service window is visible degradation and must not be hidden by replaying old values without freshness metadata.

Related evidence appears in the phase-one architecture, implementation and steering records, including `SP-00043`, `OD-00034`, `CF-00045` and `TR-00051`.

## Enterprise KPIs and regional context

Enterprise KPI definitions override legacy regional scorecards for comparable reporting. Regions may retain explanatory context and governed local measures, but a local label cannot change the denominator, time window or exception semantics of an enterprise KPI. The rejected approach—silently translating every legacy scorecard—would preserve familiar screens while making cross-region comparisons unreliable.

The semantic layer must version definitions and retain calculation provenance. QA compares source telemetry, transformation outputs and displayed values across late data, missing stores and regional calendar differences.

Evidence: `OD-00034`, `SP-00044`, `TR-00055`, `CF-00049`, `TM-00201`.

## Midwest pilot and Orbit dependency

Midwest is the first production pilot because its operational sponsorship and data readiness provide a controlled proving ground. Pilot success does not automatically authorize enterprise rollout; exit evidence must cover alert usefulness, false positives, data freshness, support load and adoption.

Pulse shares compute capacity and batch windows with Orbit. When both projects request peak processing, owners must negotiate capacity explicitly rather than allow one workload to starve the other. A pilot-date risk first triggers workload sequencing, degraded-service analysis and escalation against the shared dependency.

Evidence: `TR-00053`, `CF-00047`, `TM-00189`, `OD-00037`, `OL-00083`.
