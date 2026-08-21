#!/usr/bin/env python3

import csv
import json
import re
import zipfile
from io import StringIO
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TARGETS = {
    "atlas": 420,
    "pulse": 360,
    "nova": 400,
    "harbor": 480,
    "orbit": 340,
}
SOURCES = {"teams", "outlook", "transcript", "sharepoint", "onedrive", "confluence"}
ARTIFACTS = {
    "architecture_overview.svg",
    "architecture_decision_compendium.pdf",
    "business_requirements_document.docx",
    "client_readiness_assessment.pdf",
    "data_and_integration_control_review.pdf",
    "decision_register.csv",
    "dependency_register.csv",
    "implementation_specification.docx",
    "operational_readiness_runbook.docx",
    "pilot_post_implementation_review.pdf",
    "project_roster.csv",
    "project_memory_casebook.md",
    "risk_register.csv",
    "solution_design_specification.docx",
    "steering_committee_decision_pack.pdf",
    "steering_committee_pack.pdf",
    "uat_and_acceptance_plan.docx",
}


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as source:
        return [json.loads(line) for line in source if line.strip()]


def read_sources(project_dir: Path) -> list[dict]:
    records = []
    source_dir = project_dir / "sources"
    expected = {f"{source}.jsonl" for source in SOURCES}
    present = {path.name for path in source_dir.glob("*.jsonl")}
    assert present == expected, f"{project_dir.name}: incomplete source files"
    for source_name in sorted(SOURCES):
        records.extend(read_jsonl(source_dir / f"{source_name}.jsonl"))
    return records


def validate_artifact(path: Path) -> None:
    assert path.stat().st_size > 0, f"empty artifact: {path}"
    if path.suffix == ".docx":
        with zipfile.ZipFile(path) as document:
            assert document.testzip() is None, f"invalid DOCX: {path}"
            assert "word/document.xml" in document.namelist(), f"invalid DOCX: {path}"
    elif path.suffix == ".pdf":
        assert path.read_bytes().startswith(b"%PDF-"), f"invalid PDF: {path}"
    elif path.suffix == ".csv":
        rows = list(csv.reader(StringIO(path.read_text(encoding="utf-8"))))
        assert len(rows) >= 2, f"empty CSV: {path}"
    elif path.suffix == ".svg":
        ElementTree.parse(path)


def validate_project(project: str, target: int) -> tuple[int, int]:
    project_dir = DATA / project
    records = read_jsonl(project_dir / "records.jsonl")
    source_records = read_sources(project_dir)

    assert len(records) == target, f"{project}: expected {target} records, found {len(records)}"
    assert len(source_records) == target, f"{project}: source files contain {len(source_records)}"
    assert len({record["id"] for record in records}) == target, f"{project}: duplicate IDs"
    assert records == sorted(records, key=lambda record: (record["timestamp"], record["id"])), f"{project}: records are not sorted"
    assert {record["source"] for record in records} == SOURCES, f"{project}: incomplete sources"
    assert all(record["project_id"] == project.upper() for record in records), f"{project}: project mismatch"
    assert all(record["organization"] == "Meridian Group" for record in records), f"{project}: organization mismatch"
    assert all(record["content"].strip() for record in records), f"{project}: empty content"

    canonical = {record["id"]: record for record in records}
    sources = {record["id"]: record for record in source_records}
    assert canonical == sources, f"{project}: canonical and source records differ"

    artifact_names = {path.name for path in (project_dir / "artifacts").iterdir() if path.is_file()}
    missing = ARTIFACTS - artifact_names
    assert not missing, f"{project}: missing artifacts: {', '.join(sorted(missing))}"
    for artifact_name in ARTIFACTS:
        validate_artifact(project_dir / "artifacts" / artifact_name)
    casebook = (project_dir / "artifacts" / "project_memory_casebook.md").read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"`([A-Z]{2}-\d{5})`", casebook))
    unknown_ids = evidence_ids - canonical.keys()
    assert not unknown_ids, f"{project}: unknown casebook evidence IDs: {', '.join(sorted(unknown_ids))}"
    return len(records), len(artifact_names)


def main() -> None:
    total = 0
    all_ids = set()
    for project, target in TARGETS.items():
        count, artifact_count = validate_project(project, target)
        records = read_jsonl(DATA / project / "records.jsonl")
        ids = {record["id"] for record in records}
        assert not all_ids.intersection(ids), f"{project}: IDs overlap another project"
        all_ids.update(ids)
        total += count
        print(f"{project}: {count} records, {artifact_count} artifacts")

    people = json.loads((DATA / "people.json").read_text(encoding="utf-8"))
    compressed = list(DATA.rglob("*.gz")) + list(DATA.rglob("*.xz")) + list(DATA.rglob("*.zip"))
    assert not compressed, f"compressed files remain: {', '.join(str(path) for path in compressed)}"
    assert people, "people directory is empty"
    assert total == 2000, f"expected 2000 total records, found {total}"
    print(f"total: {total} records, {len(people)} people")


if __name__ == "__main__":
    main()
