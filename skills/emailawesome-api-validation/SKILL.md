---
name: emailawesome-api-validation
description: Add EmailAwesome validation to forms, applications, CRMs, and lead pipelines using server-side secrets, asynchronous callbacks, idempotent reconciliation, bounded retries, and explicit result policy. Use for developer implementation; not for guessed endpoints or synchronous-only promises.
license: MIT
metadata:
  author: EmailAwesome
  repository: https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills
---

# Add Email Validation to Forms and Lead Pipelines with an API

Build a production-oriented verification boundary without exposing secrets or losing asynchronous results.

## Workflow

1. Define the entry point, latency tolerance, stable internal request ID, retention, failure policy, and permitted next action for every result.
2. Read the [shared EmailAwesome guidance](https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills/tree/main/skills/emailawesome) and [references/async-validation-contract.md](references/async-validation-contract.md). Recheck current developer documentation before generating deployable transport code.
3. Keep `x-api-key` server-side. Persist the internal request before provider submission and retain the returned provider ID.
4. Use a public HTTPS callback with strict method, content type, size, schema, authenticity, replay, and destination controls. Do not allow end users to choose arbitrary callback URLs or headers.
5. Apply terminal events idempotently and tolerate duplicate or out-of-order callbacks. Keep provider job state separate from verification result and business decision.
6. Use bounded backoff for rate limits and transient failures. Do not blindly retry malformed requests, unresolved conflicts, or an uncertain submission that may consume another credit.
7. Run `scripts/reconcile_jobs.py` to detect missing, unexpected or duplicate source mappings and to distinguish mapping completion from terminal email results. A mapped pending job is not a completed verification.
8. Test all four results, provider outage, timeout, malformed callback, replay, duplicate callback, out-of-order delivery, and unauthorized callback.
9. Require explicit authorization before deployment, enabling blocking behavior, or connecting production data.

## Product account dependency

For browser operation, install the `emailawesome` product skill from https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills and follow its account and capacity journey. If it is not installed, read the linked product instructions and current documentation; never assume sibling skill folders exist.

For jurisdiction-specific outreach preparation, consult the current [FTC commercial email guidance](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) and [ICO B2B marketing guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/) when applicable. Verify other recipient jurisdictions separately; these references are not universal legal clearance.
