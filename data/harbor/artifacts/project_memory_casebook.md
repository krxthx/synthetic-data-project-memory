# Harbor Project Memory Casebook

## Readiness-based migration waves

Applications migrate in waves based on criticality and provisioning readiness. The program rejected a single date-driven cutover because legacy applications differ in identity integration, support ownership and recovery options. A wave is not ready because implementation is complete; it also needs role mappings, operational ownership, test evidence and a reversible cutover plan.

Readiness evidence is evaluated per application. Difficult legacy systems do not silently block lower-risk applications, and schedule pressure does not waive privileged-access controls. Deferred applications retain an owner and an explicit review condition.

Evidence: `TM-00496`, `OL-00212`, `TR-00142`, `SP-00120`, `OD-00095`.

## RBAC baseline and governed exceptions

Role-based access control is the baseline. Exceptions are possible where business duties cannot yet fit the standard model, but they require a named owner, rationale, scope, compensating control and expiry or review date. An exception is not a new permanent role created through local convention.

Directory cleanup and ambiguous role mappings are governance risks as well as technical defects. Testing must include over-provisioning, under-provisioning, conflicting duties, stale assignments and revocation. Audit evidence must show both the rule applied and any approved deviation.

Evidence: `TR-00143`, `SP-00121`, `OD-00096`, `CF-00126`, `TM-00532`.

## Atlas interim bridge

Harbor provides an interim SSO bridge for the Atlas pilot. The bridge allows Atlas to proceed without waiting for full Harbor migration, but it remains inside Harbor's identity-control boundary. It needs supported authentication flows, correlation identifiers, monitoring, incident ownership and a retirement path.

The bridge must not become an undocumented permanent platform. Changes that broaden users, applications or assurance requirements trigger a new review. Atlas schedule pressure cannot authorize local credentials or weaken step-up controls.

Evidence: `TR-00144`, `TM-00508`, `SP-00122`, `CF-00127`, `OD-00097`.

## Legacy provisioning and privileged access

Legacy applications without SCIM are not forced into phase one. Their provisioning gaps are documented and handled through later waves or controlled interim procedures. Pretending manual provisioning is automated would hide revocation latency and support cost.

Privileged accounts require step-up controls before migration because their blast radius is materially higher. The control applies even when standard-user migration is ready. Acceptance evidence covers enrollment, recovery, emergency access, logging and revocation; a successful login alone is insufficient.

Evidence: `CF-00123`, `TR-00145`, `SP-00123`, `OD-00098`, `TM-00544`, `SP-00119`, `OD-00094`, `CF-00124`, `TR-00146`.
