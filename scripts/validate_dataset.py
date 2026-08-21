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
GOLDENS = ROOT / "goldens"
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
    "statement_of_work.docx",
    "uat_and_acceptance_plan.docx",
}
GOLDEN_COUNTS = {"ATLAS": 6, "PULSE": 6, "NOVA": 6, "HARBOR": 6, "ORBIT": 6, "ORGANIZATION": 9}
SOWS = {
    "atlas": ("MG-ATLAS-SOW-001", "Cedar Bridge Delivery Ltd.", "Lena Iyer"),
    "pulse": ("MG-PULSE-SOW-001", "Northlake Analytics Ltd.", "Leah Pillai"),
    "nova": ("MG-NOVA-SOW-001", "Redwood Signal Systems Ltd.", "Leah Mendes"),
    "harbor": ("MG-HARBOR-SOW-001", "Greyhaven Identity Services Ltd.", "Leo Singh"),
    "orbit": ("MG-ORBIT-SOW-001", "Blue Cedar Finance Systems Ltd.", "Omar White"),
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


def validate_organization(people: list[dict]) -> list[dict]:
    organization_dir = DATA / "organization"
    catalog = json.loads((organization_dir / "policy_catalog.json").read_text(encoding="utf-8"))
    assert len(catalog) == 9, f"expected 9 organization policies, found {len(catalog)}"
    assert len({policy["id"] for policy in catalog}) == 9, "duplicate organization policy IDs"
    assert {policy["function"] for policy in catalog} == {"HR", "IT", "Administration"}, "incomplete policy functions"

    people_by_id = {person["id"]: person for person in people}
    policy_ids = {policy["id"] for policy in catalog}
    for policy in catalog:
        assert policy["owner_id"] in people_by_id, f"{policy['id']}: unknown owner"
        assert policy["approver_id"] in people_by_id, f"{policy['id']}: unknown approver"
        policy_path = organization_dir / policy["file"]
        assert policy_path.is_file(), f"{policy['id']}: missing policy document"
        content = policy_path.read_text(encoding="utf-8")
        assert policy["id"] in content, f"{policy['id']}: document ID mismatch"
        assert people_by_id[policy["owner_id"]]["name"] in content, f"{policy['id']}: owner missing from document"
        assert len(content.split()) >= 300, f"{policy['id']}: policy document is too sparse"

    with (organization_dir / "policy_register.csv").open(encoding="utf-8", newline="") as source:
        register = list(csv.DictReader(source))
    assert {row["policy_id"] for row in register} == policy_ids, "policy register differs from catalog"
    register_by_id = {row["policy_id"]: row for row in register}
    for policy in catalog:
        row = register_by_id[policy["id"]]
        for field in ("title", "function", "version", "status", "owner_id", "approver_id", "effective_date", "review_date", "file"):
            assert row[field] == policy[field], f"{policy['id']}: register mismatch for {field}"

    records = read_jsonl(organization_dir / "records.jsonl")
    assert len(records) == 27, f"expected 27 organization records, found {len(records)}"
    assert len({record["id"] for record in records}) == 27, "duplicate organization record IDs"
    assert records == sorted(records, key=lambda record: (record["timestamp"], record["id"])), "organization records are not sorted"
    assert all(record["organization"] == "Meridian Group" for record in records), "organization record mismatch"
    assert all(record["project_id"] is None and record["scope"] == "organization" for record in records), "organization scope mismatch"
    assert {record["metadata"]["policy_id"] for record in records} == policy_ids, "organization records omit policies"
    return records


def validate_sows(people: list[dict]) -> None:
    people_by_name = {person["name"]: person for person in people}
    required_sections = {
        "1. Background and objectives",
        "2. In-scope services",
        "3. Deliverables and milestones",
        "4. Responsibilities",
        "5. Assumptions and dependencies",
        "6. Out of scope",
        "8. Commercial and change control",
        "9. Exit and transition",
    }
    for project, (sow_id, supplier, owner) in SOWS.items():
        assert owner in people_by_name, f"{sow_id}: unknown Meridian owner"
        sow_path = DATA / project / "artifacts" / "statement_of_work.docx"
        with zipfile.ZipFile(sow_path) as document:
            xml = ElementTree.fromstring(document.read("word/document.xml"))
        content = " ".join(node.text for node in xml.iter() if node.text)
        assert len(re.findall(r"\b\w+\b", content)) >= 650, f"{sow_id}: SOW is too sparse"
        assert sow_id in content, f"{sow_id}: document ID mismatch"
        assert supplier in content, f"{sow_id}: supplier mismatch"
        assert owner in content, f"{sow_id}: owner mismatch"
        assert all(section in content for section in required_sections), f"{sow_id}: required section missing"


def validate_golden_memories(records_by_scope: dict[str, list[dict]]) -> None:
    combined = []
    all_golden_ids = set()
    for scope, expected_count in GOLDEN_COUNTS.items():
        directory = GOLDENS / scope.lower()
        memories = json.loads((directory / "golden_memories.json").read_text(encoding="utf-8"))
        assert len(memories) == expected_count, f"{scope}: expected {expected_count} golden memories"
        records = {record["id"]: record for record in records_by_scope[scope]}
        for memory in memories:
            assert memory["id"] not in all_golden_ids, f"duplicate golden-memory ID: {memory['id']}"
            all_golden_ids.add(memory["id"])
            assert memory["scope"] == scope, f"{memory['id']}: scope mismatch"
            assert memory["status"] == "current" and memory["valid_to"] is None, f"{memory['id']}: invalid status"
            assert len(memory["canonical_fact"].split()) >= 8, f"{memory['id']}: canonical fact is too sparse"
            assert len(memory["rationale"].split()) >= 8, f"{memory['id']}: rationale is too sparse"
            assert len(memory["evidence"]) >= 3, f"{memory['id']}: insufficient evidence"
            assert len({item["source"] for item in memory["evidence"]}) >= 2, f"{memory['id']}: insufficient source diversity"
            for item in memory["evidence"]:
                assert item["record_id"] in records, f"{memory['id']}: unknown evidence {item['record_id']}"
                record = records[item["record_id"]]
                for field in ("source", "type", "timestamp"):
                    assert item[field] == record[field], f"{memory['id']}: stale evidence metadata for {item['record_id']}"
            assert memory["valid_from"] == min(item["timestamp"] for item in memory["evidence"]), f"{memory['id']}: invalid start date"
            evaluation = memory["evaluation"]
            assert len(evaluation["questions"]) >= 2, f"{memory['id']}: insufficient questions"
            assert len(evaluation["required_concepts"]) >= 2, f"{memory['id']}: insufficient required concepts"
            assert evaluation["invalid_claims"], f"{memory['id']}: missing invalid claims"
        combined.extend(memories)

    aggregate = read_jsonl(GOLDENS / "golden_memories.jsonl")
    assert len(aggregate) == sum(GOLDEN_COUNTS.values()), "aggregate golden-memory count mismatch"
    assert {memory["id"]: memory for memory in aggregate} == {memory["id"]: memory for memory in combined}, "aggregate golden memories differ from scope files"
    memories_by_id = {memory["id"]: memory for memory in aggregate}
    questions = read_jsonl(GOLDENS / "golden_questions.jsonl")
    assert len(questions) == sum(len(memory["evaluation"]["questions"]) for memory in aggregate), "golden-question count mismatch"
    assert len({question["id"] for question in questions}) == len(questions), "duplicate golden-question IDs"
    for question in questions:
        assert question["memory_id"] in memories_by_id, f"{question['id']}: unknown golden memory"
        memory = memories_by_id[question["memory_id"]]
        assert question["scope"] == memory["scope"], f"{question['id']}: scope mismatch"
        assert question["question"] in memory["evaluation"]["questions"], f"{question['id']}: unknown question text"
        assert question["canonical_answer"] == memory["canonical_fact"], f"{question['id']}: canonical answer mismatch"
        assert question["required_concepts"] == memory["evaluation"]["required_concepts"], f"{question['id']}: rubric mismatch"
        assert question["invalid_claims"] == memory["evaluation"]["invalid_claims"], f"{question['id']}: invalid-claim mismatch"
        assert question["evidence_ids"] == [item["record_id"] for item in memory["evidence"]], f"{question['id']}: evidence mismatch"


def main() -> None:
    total = 0
    all_ids = set()
    records_by_scope = {}
    for project, target in TARGETS.items():
        count, artifact_count = validate_project(project, target)
        records = read_jsonl(DATA / project / "records.jsonl")
        records_by_scope[project.upper()] = records
        ids = {record["id"] for record in records}
        assert not all_ids.intersection(ids), f"{project}: IDs overlap another project"
        all_ids.update(ids)
        total += count
        print(f"{project}: {count} records, {artifact_count} artifacts")

    people = json.loads((DATA / "people.json").read_text(encoding="utf-8"))
    assert len(people) == 93, f"expected 93 people, found {len(people)}"
    assert len({person["id"] for person in people}) == 93, "duplicate people IDs"
    organization_records = validate_organization(people)
    validate_sows(people)
    records_by_scope["ORGANIZATION"] = organization_records
    organization_ids = {record["id"] for record in organization_records}
    assert not all_ids.intersection(organization_ids), "organization IDs overlap project IDs"
    profile = json.loads((DATA / "organization.json").read_text(encoding="utf-8"))
    assert profile["total_records"] == total, "organization profile project count mismatch"
    assert profile["organization_records"] == len(organization_records), "organization profile policy-record count mismatch"
    assert profile["total_memory_records"] == total + len(organization_records), "organization profile total count mismatch"
    assert profile["total_people"] == len(people), "organization profile people count mismatch"
    validate_golden_memories(records_by_scope)
    compressed = list(DATA.rglob("*.gz")) + list(DATA.rglob("*.xz")) + list(DATA.rglob("*.zip"))
    assert not compressed, f"compressed files remain: {', '.join(str(path) for path in compressed)}"
    assert not list(DATA.rglob("*golden*")), "golden files must remain outside data/"
    assert people, "people directory is empty"
    assert total == 2000, f"expected 2000 total records, found {total}"
    print(f"organization: {len(organization_records)} records, 9 policies")
    print("statements of work: 5")
    print(f"golden memories: {sum(GOLDEN_COUNTS.values())} facts and 78 questions across {len(GOLDEN_COUNTS)} scopes")
    print(f"total: {total + len(organization_records)} records, {len(people)} people")


if __name__ == "__main__":
    main()
