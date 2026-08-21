# Atlas Customer Onboarding

**Organization:** Meridian Group  
**Project ID:** ATLAS  
**Domain:** Customer Operations  
**Records:** 420  
**Core team:** 17 members plus shared enterprise SMEs

## Purpose
Modernize enterprise customer onboarding from signed deal to production handoff.

## Memory storyline
Atlas contains business, delivery and architecture history around CRM identity, a governed onboarding stage model, exception handling, regional process variance, and an interim Harbor SSO dependency. The corpus intentionally contains repeated facts, corrections, superseded assumptions, client feedback and cross-project references.

## Key decisions
- CRM remains authoritative for customer identity and onboarding status.
- Enterprise onboarding is phase 1; SMB onboarding is deferred.
- The pilot uses Harbor's interim SSO bridge rather than waiting for the full Harbor migration.
- High-risk onboarding exceptions require human approval.
- Regions may add governed substeps under a common enterprise stage taxonomy.

## Dependencies
- **Harbor:** interim SSO bridge.
- **Nova:** shared CRM identity-quality concerns.

## Sources
`records.jsonl.gz` is the canonical normalized corpus. Every record retains its original `source` value: Teams, Outlook, calendar transcript, SharePoint, OneDrive or Confluence.

## People
The organization-wide `../people.json.gz` directory contains member roles, project membership, SME areas, responsibilities, and what each person has built or contributed.

## Artifacts
`artifacts/` contains architecture views, decision/risk registers and rich project documents intended to overlap with the normalized source evidence.