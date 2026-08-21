#!/usr/bin/env python3

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def timestamp(value: str, days: int, hour: int) -> str:
    date = datetime.fromisoformat(value).replace(tzinfo=timezone.utc)
    return (date + timedelta(days=days, hours=hour)).isoformat().replace("+00:00", "Z")


def main() -> None:
    catalog = json.loads((DATA / "organization" / "policy_catalog.json").read_text())
    people = {person["id"]: person for person in json.loads((DATA / "people.json").read_text())}
    records = []

    for policy in catalog:
        owner = people[policy["owner_id"]]["name"]
        approver = people[policy["approver_id"]]["name"]
        participants = [owner, approver]
        controls = "; ".join(policy["key_controls"])
        base = len(records) + 1
        common = {
            "organization": "Meridian Group",
            "project_id": None,
            "scope": "organization",
            "thread_id": f"MERIDIAN-{policy['id']}",
            "participants": participants,
        }
        records.extend([
            {
                "id": f"OP-{base:05d}",
                **common,
                "source": "sharepoint",
                "type": "policy_announcement",
                "timestamp": timestamp(policy["effective_date"], 0, 9),
                "author": owner,
                "content": f"Policy effective: {policy['id']} {policy['title']} v{policy['version']}. {policy['summary']} Owner: {owner}. Approved by: {approver}. This policy is authoritative from {policy['effective_date']} and supersedes {policy['supersedes'] or 'no prior Meridian policy'}.",
                "metadata": {"fictional": True, "signal": "high", "memory_type": "policy", "policy_id": policy["id"], "version": policy["version"], "authority": "current"},
            },
            {
                "id": f"OP-{base + 1:05d}",
                **common,
                "source": "teams",
                "type": "implementation_guidance",
                "timestamp": timestamp(policy["effective_date"], 7, 11),
                "author": owner,
                "content": f"Implementation guidance for {policy['id']}: {controls}. Exception route: {policy['exception_route']} An informal manager or project decision does not override these controls.",
                "metadata": {"fictional": True, "signal": "high", "memory_type": "policy_guidance", "policy_id": policy["id"], "version": policy["version"], "authority": "interpretive"},
            },
            {
                "id": f"OP-{base + 2:05d}",
                **common,
                "source": "outlook",
                "type": "policy_clarification",
                "timestamp": timestamp(policy["effective_date"], 30, 14),
                "author": approver,
                "content": f"Subject: Clarification on {policy['id']}\n\nQuestion: {policy['common_question']}\nAnswer: {policy['clarification']} The full policy remains authoritative; this clarification addresses the stated scenario and does not create a broader exception.",
                "metadata": {"fictional": True, "signal": "high", "memory_type": "policy_clarification", "policy_id": policy["id"], "version": policy["version"], "authority": "approved_clarification"},
            },
        ])

    records.sort(key=lambda record: (record["timestamp"], record["id"]))
    output = DATA / "organization" / "records.jsonl"
    output.write_text("".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records))
    print(f"organization: {len(records)} records")


if __name__ == "__main__":
    main()
