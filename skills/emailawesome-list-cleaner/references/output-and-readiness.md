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

## Identity and safe export

Pass `--source-email-column` and `--result-email-column` when both files contain addresses, using their actual field names. This cross-check preserves local-part case and normalizes domain case. Mismatches, duplicate IDs, unexpected IDs and excluded/result overlaps go to `unresolved.csv`, even if the raw status says VALID. Without those flags, `email_identity_checked` is false: source-ID reconciliation alone does not prove the address was mapped correctly. `outreach_permission_checked` is always false; evaluate permission and suppression separately.

The export neutralizes spreadsheet formula prefixes. Keep the original provider file private as raw evidence. Missing source rows are listed in the summary and must be accounted for in the final ledger; they are not fabricated provider results. Do not assume the provider preserves custom columns: establish a supported row or job mapping before running the helper.
