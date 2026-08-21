# Orbit Project Memory Casebook

## Rolling forecast operating model

Monthly rolling forecasting replaces quarterly-only planning. This changes the operating cadence as well as the software: finance owners review assumptions more frequently, scenario versions need explicit ownership, and late actuals must be reconciled without erasing the forecast state that users previously saw.

A monthly refresh does not mean every number may be overwritten. The system retains version, author, time, source and adjustment rationale so leadership can distinguish changed business expectations from data corrections.

Evidence: `TM-00697`, `OL-00298`, `TR-00199`, `CF-00175`, `SP-00170`.

## ERP authority and adjustments

ERP actuals remain authoritative. Orbit may normalize, aggregate and explain actuals, but it cannot create a competing financial truth. When an ERP correction arrives, downstream forecasts and narratives must show how the correction propagated.

Manual adjustments are governed forecast inputs, not replacements for actuals. Each adjustment needs an owner, reason, scope, effective period and audit history. Spreadsheet uploads must fail visibly on ambiguous entities, periods or currencies rather than guessing mappings.

Evidence: `TR-00200`, `CF-00176`, `SP-00171`, `OD-00136`, `TM-00733`.

## AI narrative boundary

AI may draft variance narratives but cannot change forecasts. The draft must be grounded in visible calculation results and remain distinguishable from an approved finance explanation. A fluent narrative is not evidence that a variance cause is correct.

Users need the underlying period, scenario, account and comparison basis. Approval, revision and rejection are retained so later readers can distinguish machine suggestion from finance judgment. Permission checks apply to both the narrative and the values used to generate it.

Evidence: `CF-00173`, `SP-00168`, `OD-00133`, `TR-00202`, `TM-00745`.

## Controlled rollout and shared capacity

Scenario planning begins with finance leadership before broader business-unit rollout. The initial cohort validates scenario semantics, governance and decision usefulness. Expansion requires evidence that templates, permissions and support procedures work across different business-unit planning practices.

Orbit shares analytical-platform compute and batch windows with Pulse. Forecast close and store-operations processing may compete for peak capacity, so the dependency needs explicit scheduling, service priorities and degradation rules. Neither project may assume that a previously available batch window is permanently reserved.

Evidence: `OD-00132`, `CF-00174`, `OD-00133`, `SP-00169`, `TR-00203`.
