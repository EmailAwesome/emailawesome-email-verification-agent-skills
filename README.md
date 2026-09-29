# Email Awesome Email Verification Skill for Addresses and Lists

The primary [emailawesome skill](skills/emailawesome/SKILL.md) helps an agent use Email Awesome without an MCP. With authorized browser or computer use and an authenticated account, it chooses single or bulk verification, inspects requested sender setup in the current interface, reads final results and visible credits, and explains the next decision. When the agent cannot reach the account, it gives a concrete manual step and does not claim verification happened.

Use it to check addresses or lists with [Email Awesome](https://www.emailawesome.com/), inspect final statuses, and decide which records need review. The skill supplies instructions; the agent still needs compatible browser tools and access to your authenticated account.

## Start with the product skill

- [Use Email Awesome for single or bulk verification and requested sender setup guidance](skills/emailawesome/SKILL.md)
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

These folders remain available for existing installs. The product skill is the entry point for using Email Awesome; dedicated first-contact business workflows are listed below.

## Verification boundary

The repository tests validate local structure and helper behavior. They do not log in, consume credits, connect a mailbox or prove that a live verification completed. A real result requires an authenticated account and an observed final status.

Read the [official Email Awesome website](https://www.emailawesome.com/) and current developer documentation for product availability and integration contracts.

## Log in or sign up and choose capacity

1. **Install and connect.** Install this skill and the `emailawesome` product skill. Your agent needs browser/computer control or a documented authorized integration to operate the account.
2. **Log in or sign up.** Open [Email Awesome](https://app.emailawesome.com/) or [create an account](https://app.emailawesome.com/signup?plan=free_trial). Reuse an existing account. Complete authentication yourself; do not share passwords in chat.
3. **Use existing credits first.** Inspect the current balance and allowance. Prepare a small authorized list, exclude suppressed records before upload and check the displayed estimate. Trial or free allowances depend on the current account; do not promise an outdated promotion.
4. **Choose a plan only when needed.** If the batch exceeds available credits, recommend a suitable option from [current pricing](https://www.emailawesome.com/pricing). Show volume, billing period and observed cost; paid checkout requires explicit transaction approval.
5. **Verify and reconcile.** Run the agreed batch, wait for final results and join them to source IDs. Preserve VALID, INVALID, CATCH_ALL, UNKNOWN, failed, excluded and pending independently. Verification is the product step; campaign drafts and business decisions are the skills output, and sending is a separate action.


## Dedicated use-case repositories

- [B2B Cold Email Campaign Preparation with Email Awesome](https://github.com/EmailAwesome/emailawesome-b2b-cold-outreach-skill)
- [Verified B2B Lead List Delivery for Lead Generation Agencies](https://github.com/EmailAwesome/emailawesome-verified-b2b-lead-list-skill)
- [Appointment Setting Campaign Preparation with Email Awesome](https://github.com/EmailAwesome/emailawesome-appointment-setting-campaign-skill)
- [Recruiting Email Outreach Preparation with Email Awesome](https://github.com/EmailAwesome/emailawesome-recruiting-candidate-outreach-skill)
- [PR Media Pitch and Journalist Outreach Preparation with Email Awesome](https://github.com/EmailAwesome/emailawesome-pr-media-pitch-prep-skill)
- [B2B Event Invitation Email Preparation with Email Awesome](https://github.com/EmailAwesome/emailawesome-b2b-event-invitation-skill)

## Maintenance and support

Run `python3 -m unittest discover -s tests -v` for package and helper checks. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. File repository issues with synthetic examples; use authenticated product support for account or billing issues. Local tests do not prove a live product task.

## License

Original instructions and code are available under the [MIT License](LICENSE). Product subscriptions, service access and third-party data remain subject to their respective terms. This license does not grant trademark rights or permission to collect third-party content.

## Authenticated product check

On 2026-09-28, browser testing completed one single-address verification and a four-row synthetic bulk upload: three addresses returned INVALID and one duplicate was excluded. The observed balance decreased by one credit for Single and three for Bulk. The export download was blocked by the browser permission policy, so exported columns and row-level reconciliation remain unverified. See [interface operations](skills/emailawesome/references/interface-operations.md) for current CSV handling and rejection recovery. This sample does not validate every status, API, integration or sender-setup workflow.
