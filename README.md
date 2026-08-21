# Meridian Group Synthetic Project Memory Dataset

A dense synthetic enterprise corpus for testing long-term organizational and project memory across multiple projects.

## Organization
**Meridian Group** is a fictional enterprise used throughout this dataset. The corpus spans five transformation programs and intentionally contains overlapping facts, changing decisions, cross-project dependencies, shared SMEs, client feedback, historical context, and superseded artifacts.

## Scope
- 5 projects
- 2,000 normalized records
- Timeline: 2026-01-05 to 2026-06-19
- Sources: Teams, Outlook, calendar recording transcripts, SharePoint, OneDrive, Confluence
- Rich artifacts: PDF, DOCX, CSV and SVG architecture diagrams
- No source code or repository activity is part of the memory corpus

## Projects
- **Atlas Customer Onboarding**: enterprise customer onboarding and production handoff
- **Pulse Store Operations Intelligence**: retail operational intelligence and alerting
- **Nova Sales Opportunity Intelligence**: evidence-backed sales opportunity recommendations
- **Harbor Identity Modernization**: identity, provisioning, SSO and access governance
- **Orbit Financial Planning**: rolling forecast and scenario planning

The dataset is synthetic. Its purpose is to test ingestion, temporal reasoning, provenance, conflict resolution, SME discovery, and multi-file long-term memory generation.

## Storage format
Each project contains:

- `records.jsonl`: the canonical normalized corpus, ordered by timestamp and record ID.
- `sources/`: the six directly readable source-specific JSONL files for Teams, Outlook, transcripts, SharePoint, OneDrive and Confluence.
- `artifacts/`: directly readable PDF, DOCX, CSV and SVG project artifacts.

Every canonical record retains its original source (`teams`, `outlook`, `transcript`, `sharepoint`, `onedrive`, or `confluence`) and normalized metadata. The source-specific files contain the same 2,000 records split by originating system; they are mirrors, not additional records. The repository contains no compressed dataset archives.

## Integrity

Rebuild each canonical file from its six source files:

```sh
python3 scripts/rebuild_records.py
```

Validate record counts, source parity, global ID uniqueness, the absence of compressed files and artifact payloads:

```sh
python3 scripts/validate_dataset.py
```
