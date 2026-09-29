# Email Awesome interface operations

Use the visible current interface as the authority for menu names, credit counts and available controls. Public starting points are the [Email Awesome product](https://www.emailawesome.com/) and [developer documentation](https://developers.emailawesome.com/). Do not infer account state from the marketing site.

## One address

1. Confirm the address is supplied or authorized by the user and the selected account is correct.
2. Open the current single-address verifier, review any displayed credit/limit information and run the check.
3. Wait for and record the final status, verification time and any visible details. If the UI only shows submission, timeout or an error, say `result pending` or `failed`, not `VALID`.

## A list prepared for bulk CSV upload

1. Keep the original file intact. Record its row count and a stable source ID for each row; identify the email column in CSV or the one-address-per-line convention in TXT. Preserve duplicates, blank/malformed rows and exclusions for reconciliation.
2. Inspect the current bulk upload requirements. The interface observed on 2026-09-28 accepted CSV; convert TXT to a working CSV locally instead of promising direct TXT upload. Download the product's sample if the expected format is unclear. Its observed headers were `first_name,last_name,email`; this is an example, not proof that those are the only accepted columns. Keep stable source IDs and a duplicate map locally even if the upload does not preserve them.
3. Upload through the current UI and inspect the preview before confirming. Record the count to validate, duplicate/syntax exclusions, header checkbox and maximum credits. A four-row synthetic example produced three addresses to validate and one exclusion. Do not charge the excluded duplicate again by silently resubmitting it. Record the job and wait for terminal completion before downloading results; do not guess the export schema. An authorized small sample is enough to prove this step before expanding scope.
4. Join the result to the source IDs, flag missing or duplicate mappings, and keep every record in exactly one of final status, excluded or unresolved. A successful upload or matching bucket total is not a source-to-result reconciliation.
5. Summarize the four final statuses and unresolved work separately. Use [result-policy.md](result-policy.md) for the business interpretation. Preserve the source file, and do not send, delete or write to a CRM merely because a list was verified.

The repository's legacy `emailawesome-list-cleaner` has helper scripts for preparation and segmentation. Use them only after confirming the input and output contract against this reconciliation rule; script output is not evidence that Email Awesome completed a live verification.

### File rejection and safe test fixtures

In the authenticated check on 2026-09-28, a CSV using `example.invalid` was rejected with `This file is not valid`, including after matching the sample headers. The same sample with `example.com` reached the preview and completed with three INVALID results. This supports a domain-dependent validation difference in that sample, not a universal rule about all rejected files. Use a reserved example domain for synthetic QA and never reuse the product sample's listed addresses as test recipients. If a real file is rejected, preserve it, compare its syntax and headers with the current sample, and report unresolved reasons after a bounded correction. Never alter real email domains to force acceptance.

The observed result menu was **more > Download all emails**. If download permission is denied, stop that path and report `export and row reconciliation unverified`; aggregate counts do not prove exported identities or columns. Keep signed download URLs out of reports and public repositories.

## Delivery Optimizer and Warm-up guidance

Use this mode only for a requested sender-domain or inbox setup. The navigation observed on 2026-09-28 called it **Delivery Optimizer Beta**; do not assume a menu named Warm-up or infer the feature's capabilities from its label. Check which inbox/domain the user means, the current UI guidance, connected state and any visible schedule or volume. Explain what is pending before invoking external account permissions. A connected mailbox or active indicator proves only the displayed setup state, not future inbox placement. Do not change live campaign sending without authorization.
