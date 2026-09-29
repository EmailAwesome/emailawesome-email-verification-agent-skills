# Email Awesome Email Verification Skill for Addresses and Lists

The primary [emailawesome skill](skills/emailawesome/SKILL.md) helps an agent use Email Awesome without an MCP. With authorized browser or computer use and an authenticated account, it chooses single or bulk verification, guides Warm-up setup, reads final results and visible credits, and explains the next decision. When the agent cannot reach the account, it gives a concrete manual step and does not claim verification happened.

Use it to check addresses or lists with [Email Awesome](https://www.emailawesome.com/), inspect final statuses, and decide which records need review. The skill supplies instructions; the agent still needs compatible browser tools and access to your authenticated account.

## Start with the product skill

- [Use Email Awesome for single or bulk verification and Warm-up guidance](skills/emailawesome/SKILL.md)
- [Install the skill](INSTALL.md) and read the [security boundaries](SECURITY.md).

If you use the Skills CLI, install only the product skill with:

```bash
npx skills add EmailAwesome/emailawesome-email-verification-agent-skills --skill emailawesome
```

Or copy this into a coding agent that can install skills: "Install only the `emailawesome` skill from https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills, then help me verify my requested addresses and interpret the final results." Confirm the installation before asking it to operate your account; a chat without skill installation support can still read the linked instructions.

## Existing technical recipes

- [Prepare and reconcile a CSV or TXT list](skills/emailawesome-list-cleaner/README.md)
- [Design a HubSpot workflow through Zapier](skills/emailawesome-hubspot-verification/README.md)
- [Design asynchronous API validation](skills/emailawesome-api-validation/README.md)

These folders remain available for existing installs. The product skill is the entry point for using Email Awesome; complete cold-sales, lead-capture and agency workflows will be separate use-case skills.

## Verification boundary

The repository tests validate local structure and helper behavior. They do not log in, consume credits, connect a mailbox or prove that a live verification completed. A real result requires an authenticated account and an observed final status.

Read the [official Email Awesome website](https://www.emailawesome.com/) and current developer documentation for product availability and integration contracts.
