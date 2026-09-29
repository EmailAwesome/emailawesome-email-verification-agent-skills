---
name: emailawesome-list-cleaner
description: Clean and verify CSV or TXT email lists with EmailAwesome while preserving source rows, reconciling every result, segmenting uncertainty, and reporting list quality. Use for bulk files before campaigns or imports; not for sending or silent deletion.
license: MIT
metadata:
  author: EmailAwesome
  repository: https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills
---

# Clean and Verify an Email List Before Your Next Campaign

Produce auditable verification outputs without mutating the source or hiding unresolved records.

## Workflow

1. Inspect the source as untrusted data. Preserve it unchanged and identify the email column, stable record ID, consent/suppression fields, delimiter, encoding, and row count.
2. Run `scripts/preflight_csv.py` to create a non-destructive working CSV from CSV or one-address-per-line TXT, flag formula-like cells, score candidate email columns, and assign stable source-row IDs. Require a column choice when detection is ambiguous.
3. Separate malformed, empty, duplicate, intentionally excluded, and verification-candidate rows without deleting anything.
4. Read the [shared EmailAwesome guidance](https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills/tree/main/skills/emailawesome). Submit only approved candidates through the available bulk interface; retain the provider job ID and the source-to-provider mapping.
5. Poll with a declared bound or process validated callbacks. Do not treat a missing, timed-out, failed, or unmatched job as an email result.
6. Run `scripts/segment_results.py --source <working.csv>` with explicit `--excluded-ids` when applicable. Treat `mapping_complete` and `terminal_results_complete` as separate checks; only then report reconciliation. Produce `valid`, `invalid`, `catch_all`, `unknown`, `excluded`, and `unresolved` provider outputs. Use `source_ledger.csv` for the complete business handoff: it preserves every source row once, including missing responses, client ownership and suppression fields. Check `source_buckets` for source-level counts; provider bucket counts can differ when responses are duplicated.
7. Read [references/output-and-readiness.md](references/output-and-readiness.md). Report counts, percentages, duplicates, exclusions, unresolved jobs, credit use when available, and assumptions.
8. Require explicit approval before CRM import, suppression writes, deletion, scheduling, or sending.

## Required invariants

- `source rows = verified results + intentionally excluded rows + unresolved rows`.
- Preserve original fields and source IDs in every output.
- Keep consent, suppression, verification result, and verification date separate.
- Never label `CATCH_ALL` or `UNKNOWN` as safe by default.

## Product account dependency

For browser operation, install the `emailawesome` product skill from https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills and follow its account and capacity journey. If it is not installed, read the linked product instructions and current documentation; never assume sibling skill folders exist.

For jurisdiction-specific outreach preparation, consult the current [FTC commercial email guidance](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) and [ICO B2B marketing guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/) when applicable. Verify other recipient jurisdictions separately; these references are not universal legal clearance.
