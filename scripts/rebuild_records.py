#!/usr/bin/env python3

import argparse
import json
from pathlib import Path


PROJECTS = ("atlas", "pulse", "nova", "harbor", "orbit")
SOURCES = ("teams", "outlook", "transcript", "sharepoint", "onedrive", "confluence")


def load_records(project_dir: Path) -> list[dict]:
    records = []
    source_dir = project_dir / "sources"
    for source_name in SOURCES:
        with (source_dir / f"{source_name}.jsonl").open(encoding="utf-8") as source:
            records.extend(json.loads(line) for line in source if line.strip())
    return sorted(records, key=lambda record: (record["timestamp"], record["id"]))


def write_records(path: Path, records: list[dict]) -> None:
    payload = b"".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")).encode() + b"\n"
        for record in records
    )
    path.write_bytes(payload)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    args = parser.parse_args()

    for project in PROJECTS:
        project_dir = args.data_dir / project
        records = load_records(project_dir)
        write_records(project_dir / "records.jsonl", records)
        print(f"{project}: {len(records)} records")


if __name__ == "__main__":
    main()
