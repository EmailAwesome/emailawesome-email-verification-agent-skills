# EmailAwesome product contract

Revalidate these facts against current product and developer documentation before consequential use.

Use the official [Validation API project](https://developers.emailawesome.com/docs/validation-api) for request schemas, authentication, processing states and limits. If a developer-portal introduction link is unavailable, use the portal's **Validations** navigation. An unavailable documentation page is not evidence that the API itself is down; keep an unconfirmed contract pending rather than inventing replacement endpoints.

## Confirmed product capabilities

- One-off verification in the product.
- Bulk CSV uploads; prepare TXT lists locally as CSV unless the current interface explicitly accepts TXT.
- Asynchronous API verification.
- Zapier-based integrations, including HubSpot workflows.
- Sender-readiness and warm-up guidance as a separate product workflow.

## Previously documented API facts

- Base URL: `https://api.emailawesome.com/api`.
- Authentication header: `x-api-key`.
- Previously documented single-create path: `POST /validations/email_validation`.
- A single request includes `email` and a `results_callback` object.
- Submission/job states and final verification results are separate state machines.
- Final results are `VALID`, `INVALID`, `CATCH_ALL`, or `UNKNOWN`.
- Documented error handling includes malformed requests, conflicts, and rate limits.

These are reference details, not a live connection test. Check the current developer documentation and an authorized account before generating deployable code. Do not infer bulk paths, callback authenticity behavior, retry safety, quotas or billing rules from the single-create contract.

## Integration facts

Before following a **Create API Key** prompt, check **API Verifications** for an existing suitable key. Reuse it through the product or secret store without revealing, regenerating or deleting it. Key-creation copy alone does not prove that the account has no key. If an authorized connection fails, inspect the actual error and selected account before proposing a new key; do not replace credentials just to clear an inconsistent prompt.

HubSpot workflows are currently presented as Zapier integrations, not as a proprietary native HubSpot connector. A HubSpot trigger may already have created a submission or record before validation runs. Do not promise otherwise.
