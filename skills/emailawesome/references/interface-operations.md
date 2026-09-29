# Email Awesome interface operations

Use the visible current interface as the authority for menu names, credit counts and available controls. Public starting points are the [Email Awesome product](https://www.emailawesome.com/) and [developer documentation](https://developers.emailawesome.com/). Do not infer account state from the marketing site.

## One address

1. Confirm the address is supplied or authorized by the user and the selected account is correct.
2. Open the current single-address verifier, review any displayed credit/limit information and run the check.
3. Wait for and record the final status, verification time and any visible details. If the UI only shows submission, timeout or an error, say `result pending` or `failed`, not `VALID`.

## A CSV or TXT list

1. Keep the original file intact. Record its row count and a stable source ID for each row; identify the email column in CSV or the one-address-per-line convention in TXT. Preserve duplicates, blank/malformed rows and exclusions for reconciliation.
2. Prepare a working copy only if needed. Inspect the current bulk upload requirements and visible credit estimate before submission. A small, authorized batch is enough to prove the flow before larger use.
3. Upload through the current UI, note the job identifier or visible progress, and wait for terminal completion. Download the result only when available; do not guess the export schema.
4. Join the result to the source IDs, flag missing or duplicate mappings, and keep every record in exactly one of final status, excluded or unresolved. A successful upload or matching bucket total is not a source-to-result reconciliation.
5. Summarize the four final statuses and unresolved work separately. Use [result-policy.md](result-policy.md) for the business interpretation. Preserve the source file, and do not send, delete or write to a CRM merely because a list was verified.

The repository's legacy `emailawesome-list-cleaner` has helper scripts for preparation and segmentation. Use them only after confirming the input and output contract against this reconciliation rule; script output is not evidence that Email Awesome completed a live verification.

## Warm-up

Use this mode only for a requested sender-domain or inbox setup. Check which inbox/domain the user means, the current UI guidance, connected state and any visible schedule or volume. Explain what is pending before invoking external account permissions. A connected mailbox or active Warm-up indicator proves only the displayed setup state, not future inbox placement. Do not change live campaign sending without authorization.
