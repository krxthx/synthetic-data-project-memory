# Nova Project Memory Casebook

## Advisory boundary

Nova recommends actions but cannot automatically change CRM opportunity stages. The boundary preserves accountable commercial judgment and prevents an inferred signal from becoming authoritative pipeline state. Earlier automation ideas remain useful design history, but they do not authorize stage mutation.

Every recommendation needs a visible explanation, evidence references and a human disposition. Accept, reject and defer outcomes are captured without rewriting the source evidence. Integration credentials must be technically unable to bypass the boundary, and QA must test attempted writes rather than relying only on interface behavior.

Evidence: `TM-00328`, `OL-00140`, `TR-00094`, `SP-00080`, `CF-00085`.

## Evidence quality and provenance

A recommendation requires approved evidence. Meeting-derived signals are eligible only when the underlying material has the required approval and provenance; an unapproved transcript, private note or ambiguous account match cannot be promoted merely because it improves model confidence.

The evidence chain retains source, capture time, account identity, approval state and the transformation that produced the recommendation. If evidence becomes unavailable or its approval is revoked, Nova must show that limitation and reevaluate affected recommendations. Free-form summaries supplement the chain but are not substitutes for source references.

Related evidence is distributed across the implementation specifications, decision records and meeting transcripts, including `OD-00062`, `CF-00085`, `TR-00094` and `SP-00080`.

## Pilot audience and permission-aware retrieval

Pilot access is limited to strategic account directors. This is a controlled learning cohort, not a statement that other roles will never use Nova. Expansion requires evidence that explanations are usable, recommendations are appropriately cautious and account boundaries hold under real operating conditions.

Evidence visibility follows the requesting account team's permissions. Nova cannot reveal a restricted source through a generated explanation, citation snippet, cached recommendation or aggregate drill-down. Retrieval must evaluate current authorization at request time; prior access is not durable permission.

Evidence: `OD-00062`, `OD-00063`, `TR-00096`, `TM-00340`, `SP-00082`, `SP-00079`, `CF-00084`, `OD-00064`, `TR-00098`.

## Cross-project identity dependencies

Nova depends on Atlas-related customer and account identity quality and on Harbor's account-team authorization mappings. Those are separate dependencies: a correct account match does not prove the viewer may see the evidence, and a correct authorization mapping does not repair a duplicate CRM identity.

Failure handling must tell support which boundary failed. Ambiguous identity should block or qualify a recommendation; missing authorization should deny evidence without leaking its existence. Temporary mappings require named owners and expiry conditions, and neither dependency owner's silence counts as acceptance.

Evidence includes `TM-00352`, `SP-00079`, `OD-00064` and the dependency records associated with Atlas and Harbor.
