# Nova Sales Opportunity Intelligence

**Organization:** Meridian Group  
**Project ID:** NOVA  
**Domain:** Sales  
**Records:** 400  
**Core team:** 16 members plus shared enterprise SMEs

## Purpose
Assist strategic account teams with evidence-backed opportunity recommendations.

## Memory storyline
Nova combines CRM signals, approved meeting evidence, human review, recommendation explainability and permission-aware access. Business and technical conversations deliberately disagree at points so current truth must be reconstructed from provenance and later decisions.

## Key decisions
- Nova recommends actions but cannot automatically change CRM opportunity stages.
- Every recommendation requires approved evidence.
- Pilot access is limited to strategic account directors.
- Evidence visibility follows the requesting account team's permissions.

## Dependencies
- **Atlas:** customer/account identity quality.
- **Harbor:** account-team authorization mappings.

## Sources
`records.jsonl.gz` preserves the original Teams, Outlook, transcript, SharePoint, OneDrive and Confluence source identity.

## People
See `../people.json.gz` for member roles, SMEs, responsibilities and contribution history.