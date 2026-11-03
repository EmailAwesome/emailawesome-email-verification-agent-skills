# EmailAwesome product contract

Revalidate these facts against current product and developer documentation before consequential use.

Use the official [Validation API project](https://developers.emailawesome.com/docs/validation-api) for request schemas, authentication, processing states and limits. If a developer-portal introduction link is unavailable, use the portal's **Validations** navigation. An unavailable documentation page is not evidence that the API itself is down; keep an unconfirmed contract pending rather than inventing replacement endpoints.

## Confirmed product capabilities

- One-off verification in the product.
- Bulk CSV uploads; prepare TXT lists locally as CSV unless the current interface explicitly accepts TXT.
- Asynchronous API verification.
- Zapier-based integrations, including HubSpot workflows.
- Sender-readiness and warm-up guidance as a separate product workflow.

## Interface availability observed on 2026-11-03

These facts come from authenticated read-only product navigation. They do not establish launch dates, eligibility for every account, successful saves, scheduled execution or an MCP connection.

- [Contacts](https://app.emailawesome.com/contacts) provides search, status/source filters and contact lists for the user's own records. The [Verifications](https://app.emailawesome.com/email-verification) interface says a valid email is saved to Contacts and an existing contact with that email has its status updated. Do not infer that every historical result is imported, that every result creates a contact or that the product supplies prospect data.
- **Verify emails** opens **Single email** and **Upload a list** modes. The CSV modal lists a 20 MB limit, a header checkbox, optional contact-list selection and **Check file**. No upload or stage after Check file was exercised in this review. These product modals are not lead-capture widgets.
- **New list** offers Manual or Scheduled revalidation. Its form displays a minimum interval of one hour and one credit per contact revalidated. List saving, membership changes and scheduled execution were not tested. Visible options are not evidence that an automation was activated or performed.
- **Export** and **Columns** in Contacts were disabled with **Coming soon** titles. This says nothing about a separate completed Bulk job's result download or an authorized API response. Inspect the relevant surface rather than declaring all exports unavailable.
- [AI agents (MCP)](https://app.emailawesome.com/integrations/mcp) is an official in-app setup guide. It documents `https://api.emailawesome.com/api/validations/mcp` and the `x-api-key` header. No key was revealed, connection configured or tool invoked. Installing this skill is not MCP configuration, access authorization or approval for credit-consuming calls. Browser operation remains an available route when supported.
- The MCP guide describes single/bulk validations, lookup, validation lists and metrics. Its lists are validation lists, not proof of operations on Contacts lists, tags or schedules. Inspect the actual authorized connection and current schemas before implementation; do not infer tools from the name of a UI feature.
- The guide describes an immediate validation helper that waits up to nine seconds and otherwise returns `UNKNOWN`, plus background Bulk admission for 1–200 addresses with credits for accepted addresses. These are documented limits, not measured runtime behavior. Do not turn `UNKNOWN` into `INVALID` or blindly submit again; inspect the actual response before inferring provider-job state, and use only a job ID the product actually returned.
- Native HubSpot, Salesforce and Pipedrive cards in [Integrations](https://app.emailawesome.com/integrations) are marked **Coming soon**. Zapier remains a distinct current integration route. Data enrichment is user-reported roadmap, with no operational feature, fields, coverage or pricing verified by this review.

Contacts implies stored records beyond the immediate verification interaction. Retention periods, raw-upload retention, deletion behavior and the relationship between validation history and Contacts need Product confirmation. Do not promise verification-only transient storage or invent an erasure policy.

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

Before following a **Create API Key** prompt, check the current **API** section (previously **API Verifications**) for an existing suitable key. Reuse it through the product or secret store without revealing, regenerating or deleting it. Key-creation copy alone does not prove that the account has no key. If an authorized connection fails, inspect the actual error and selected account before proposing a new key; do not replace credentials just to clear an inconsistent prompt.

HubSpot workflows are currently presented as Zapier integrations, not as a proprietary native HubSpot connector. A HubSpot trigger may already have created a submission or record before validation runs. Do not promise otherwise.
