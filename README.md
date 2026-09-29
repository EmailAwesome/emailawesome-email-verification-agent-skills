# Email Awesome Agent Skill for Email Verification

The primary [emailawesome skill](skills/emailawesome/SKILL.md) helps an agent use Email Awesome without an MCP. With authorized browser or computer use and an authenticated account, it chooses single or bulk verification, guides Warm-up setup, reads final results and visible credits, and explains the next decision. When the agent cannot reach the account, it gives a concrete manual step and does not claim verification happened.

## Start with the product skill

- [Use Email Awesome for single or bulk verification and Warm-up guidance](skills/emailawesome/SKILL.md)
- [Install the skill](INSTALL.md) and read the [security boundaries](SECURITY.md).

## Existing technical recipes

- [Prepare and reconcile a CSV or TXT list](skills/emailawesome-list-cleaner/README.md)
- [Design a HubSpot workflow through Zapier](skills/emailawesome-hubspot-verification/README.md)
- [Design asynchronous API validation](skills/emailawesome-api-validation/README.md)

These folders remain available for existing installs. The product skill is the entry point for using Email Awesome; complete cold-sales, lead-capture and agency workflows will be separate use-case skills.

## Verification boundary

The repository tests validate local structure and helper behavior. They do not log in, consume credits, connect a mailbox or prove that a live verification completed. A real result requires an authenticated account and an observed final status.

Read the [official Email Awesome website](https://www.emailawesome.com/) and current developer documentation for product availability and integration contracts.
