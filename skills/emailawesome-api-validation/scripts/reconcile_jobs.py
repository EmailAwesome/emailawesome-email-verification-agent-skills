#!/usr/bin/env python3
"""Reconcile expected source IDs with asynchronous EmailAwesome job records."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

FINAL_RESULTS = {"VALID", "INVALID", "CATCH_ALL", "UNKNOWN"}
TERMINAL_JOBS = {"COMPLETE", "COMPLETED", "SUCCESS", "SUCCEEDED"}


def reconcile(expected: list[str], jobs: list[dict]) -> dict:
    if not expected or any(not isinstance(item, str) or not item.strip() for item in expected):
        raise ValueError("expected source IDs must be nonempty strings and the batch must not be empty")
    expected_set = set(expected)
    duplicate_expected_ids = sorted(item for item, count in Counter(expected).items() if count > 1)
    by_source: dict[str, dict] = {}
    duplicates: set[str] = set()
    records_without_source = 0
    for job in jobs:
        source_id = str(job.get("source_id", "") or "")
        if not source_id:
            records_without_source += 1
            continue
        if source_id in by_source:
            duplicates.add(source_id)
        by_source[source_id] = job

    missing = [source_id for source_id in expected if source_id not in by_source]
    unexpected = [source_id for source_id in by_source if source_id not in expected_set]
    states = Counter(
        str(job.get("job_status", job.get("status", "MISSING")) or "MISSING").upper()
        for job in by_source.values()
    )
    mapping_complete = not (
        missing or unexpected or duplicates or duplicate_expected_ids or records_without_source
    )
    nonterminal_or_unresolved = [
        source_id
        for source_id in expected
        if source_id in by_source
        and (
            str(by_source[source_id].get("job_status", by_source[source_id].get("status", "")) or "").upper()
            not in TERMINAL_JOBS
            or str(
                by_source[source_id].get("email_address_status", by_source[source_id].get("verification_result", ""))
                or ""
            ).upper()
            not in FINAL_RESULTS
        )
    ]
    terminal_results_complete = mapping_complete and not nonterminal_or_unresolved
    return {
        "expected": len(expected),
        "received_unique": len(by_source),
        "records_without_source_id": records_without_source,
        "missing": missing,
        "unexpected": unexpected,
        "duplicates": sorted(duplicates),
        "duplicate_expected_ids": duplicate_expected_ids,
        "job_states": dict(states),
        "nonterminal_or_unresolved": nonterminal_or_unresolved,
        "mapping_complete": mapping_complete,
        "terminal_results_complete": terminal_results_complete,
        "reconciled": terminal_results_complete,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected_ids", type=Path, help="JSON array of source IDs")
    parser.add_argument("jobs", type=Path, help="JSON array of records containing source_id")
    args = parser.parse_args()
    expected = json.loads(args.expected_ids.read_text(encoding="utf-8"))
    jobs = json.loads(args.jobs.read_text(encoding="utf-8"))
    print(json.dumps(reconcile([str(item) for item in expected], jobs), indent=2))


if __name__ == "__main__":
    main()
