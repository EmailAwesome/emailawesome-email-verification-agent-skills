# Output and list-quality rules

## Required outputs

- An unchanged source file or its recorded hash and location.
- A complete source-to-result mapping with stable IDs; a sum of output buckets is only a partition check.
- Separate `VALID`, `INVALID`, `CATCH_ALL`, `UNKNOWN`, explicitly excluded, and unresolved views.
- Duplicate relationships that point to the retained source row.
- A machine-readable summary and a short human-readable quality report.

Use `preflight_csv.py` for CSV or one-address-per-line TXT input. Run `segment_results.py` with `--source` pointing to the working CSV; pass explicit `--excluded-ids` when applicable. `mapping_complete` and `terminal_results_complete` must both be true before reporting a fully reconciled verification. Without a source copy, segmentation alone does not prove coverage.

## List-quality decision

Return `LIST QUALITY READY`, `LIST QUALITY READY WITH CONDITIONS`, or `LIST QUALITY NOT READY` using thresholds supplied by the user. When none exist, propose provisional thresholds and label them as assumptions.

Consider verification coverage, list age, duplicates, malformed rows, consent/suppression completeness, and unresolved work. This decision describes data quality only. A valid result is not permission to contact the address and does not guarantee delivery.
