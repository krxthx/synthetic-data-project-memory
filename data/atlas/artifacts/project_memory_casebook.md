# Atlas Project Memory Casebook

## Customer identity authority

Atlas orchestrates onboarding but does not become a second customer master. CRM remains authoritative for customer identity and the status fields explicitly synchronized with onboarding. The rejected alternative was an Atlas-owned master record: it simplified local workflow lookups but created ambiguous remediation ownership, reconciliation work and the possibility that client-facing status would diverge from commercial operations.

Operationally, CRM lookup failures must stop visible progression rather than create a local identity. Retries must be idempotent, correlation identifiers must cross CRM, Atlas and Harbor, and support must distinguish a data-quality failure from an authentication failure. A free-text note may explain an exception but cannot override governed state.

Evidence: `SP-00001`, `OD-00001`, `CF-00001`, `TR-00003`, `TM-00013`.

## Phase-one boundary

The early program considered a broader onboarding release. Steering narrowed phase one to enterprise onboarding and deferred SMB because the two segments use materially different operating models. The decision protects the launch window without describing SMB as permanently out of scope. Later status reports may discuss SMB discovery, but that work is not authority to add it back into the release.

Acceptance coverage must therefore prove enterprise handoff, governed stages, exceptions and production support. A team cannot infer a scope change from prototype work, an optimistic status update or a stakeholder request. Only a later accepted steering record can supersede the boundary.

Evidence: `TM-00001`, `OL-00001`, `TR-00001`, `CF-00001`, `SP-00005`.

## Harbor bridge and degraded operation

Atlas uses Harbor's interim SSO bridge for the pilot rather than waiting for the full identity-modernization program. This is a deliberate dependency contract, not a general exemption from Harbor controls. The bridge needs an owner, support window, observability and an exit condition tied to Harbor migration readiness.

If the bridge slips, Atlas first evaluates resequencing and a visible degraded mode. It must not create local credentials or interpret silence from the Harbor owner as approval. Cutover evidence must separate identity availability, authorization correctness and workflow recovery.

Evidence: `TR-00001`, `SP-00001`, `OD-00001`, `TM-00003`, `CF-00002`.

## Regional stages and accountable exceptions

Enterprise stage names are mandatory for reporting and client status. Regions may add governed substeps where local process requires them, but those substeps cannot silently redefine enterprise semantics. The model preserves regional usability while keeping cross-region metrics comparable.

High-risk legal or contractual exceptions pause the affected path and require accountable human approval. The durable record needs the approver, timestamp, rationale and resulting transition. Automated routing may gather evidence, but it cannot manufacture approval. QA must cover approval, rejection, expiry, retry and stale-session behavior.

Evidence: `CF-00004`, `SP-00004`, `TR-00005`, `OD-00004`, `CF-00003`, `TR-00004`.
