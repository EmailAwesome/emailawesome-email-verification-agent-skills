# Product-interface guidance review — 2026-11-02

This review used authenticated read-only product navigation. It does not certify API transport, callback delivery, a new Zapier/HubSpot connection or a credit purchase.

| Source | Observed evidence | Instruction affected |
| --- | --- | --- |
| [Bulk Verifications](https://app.emailawesome.com/email-verification/bulk) | The upload interface lists CSV. | Prepare TXT locally as CSV unless the live interface confirms direct TXT support. |
| [API Verifications](https://app.emailawesome.com/api-verifications) and [Integrations](https://app.emailawesome.com/integrations) | In each of two authorized accounts, API Verifications showed an existing masked key and creation date while Integrations still displayed key-creation copy. | Check the actual account/key state; the caption alone does not justify creating or replacing a key. No connection failure was demonstrated. |
| [API Verifications](https://app.emailawesome.com/api-verifications) | The Bulk guide describes callbacks for individual accepted addresses and no callbacks for `rejected_validations`; it separates pending job state from four final verdicts and advises prompt `2xx` acknowledgement. | Track submission admission separately, correlate accepted jobs and preserve rejected records. Authenticate and validate callbacks before acknowledgement. These are documented examples, not results obtained by this review. |
| [My Subscription](https://app.emailawesome.com/billing) | One-time purchased credits were offered in the free accounts, separately from monthly allowance. | The top-up journey already published in October remains applicable; inspect the current account and terms rather than requiring a monthly upgrade automatically. |
| [Validation API project](https://developers.emailawesome.com/docs/validation-api) | The current project was accessible through the developer portal's Validations navigation; the older Documentation introduction link showed Project not found in the November review. | Use the direct official project. A failed documentation link does not prove an API outage. |

No lists, contact addresses, API keys, callback secrets or private account screenshots are included in this repository. No files were uploaded, verifications executed, keys revealed/created/rotated, external services connected, plans purchased or settings saved.

Local validation: the existing 31 repository tests passed, all four skill folders passed the package validator, and `git diff --check` passed. These checks validate packaging and helper regressions, not authenticated end-to-end operations. No new tests were added to assert documentation wording.
