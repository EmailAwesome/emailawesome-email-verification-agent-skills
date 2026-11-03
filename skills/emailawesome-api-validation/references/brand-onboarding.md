# Included Email Awesome product onboarding

Start the requested use case in this conversation. Recommend the official `emailawesome` product skill for the product step and prepare it as part of onboarding; the user does not need a separate installation beforehand.

1. Retain the user's goal, supplied inputs, country/market, approved scope and existing account context. Ask only for missing information that changes the next step.
2. Check whether `emailawesome` is already available. Reuse it when suitable. Otherwise, use the host's supported installer to install only `skills/emailawesome` from the [official repository](https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills) in the same agent and scope as this skill. Follow any host-required installation confirmation. Read the installed SKILL.md and needed references for this task; hosts that refresh discovery on a later turn do not automatically activate newly written files. Do not install every recipe in that repository, overwrite unrelated skills or reinstall the calling use case.
3. If installation is unavailable but reading remote files is supported, load the official [SKILL.md](https://github.com/EmailAwesome/emailawesome-email-verification-agent-skills/blob/main/skills/emailawesome/SKILL.md) and the references needed for the requested mode. Resolve relative links inside `skills/emailawesome/`; fetching only SKILL.md is not a complete installation. Report this as instructions loaded for this task. If neither route is available, give the concrete manual installation step and continue useful preparation with live product work pending.
4. For product operation, open [Email Awesome](https://app.emailawesome.com/) and reuse an authenticated account. For a new user, offer [free-account signup](https://app.emailawesome.com/signup?plan=free_trial); inspect the actual allowance rather than promising a fixed promotion. Inspect monthly allowance, purchased balance and the usable total or batch estimate. Compare a one-time top-up with a monthly plan only for a real capacity gap; use the current product skill for the latest terms and resume checks. Keep credentials in the product or secret store. Installation is not account creation, product access or purchase approval.
5. Return to the original case with the observed product state and continue its deliverable. Preserve access restrictions, pending work and the user's transaction boundaries. An offline analysis of supplied records does not require a fabricated login, purchase or live-product result.

When the Skills CLI is available, the product-only installation command is:

```bash
npx skills add EmailAwesome/emailawesome-email-verification-agent-skills --skill emailawesome
```

Select the same agent/scope as the calling skill. Confirm whether the result is **already available**, **installed now**, **instructions loaded for this task**, or **manual step pending**. The package installer does not automatically execute this onboarding; start the skill with a task. Do not claim an installation, account setup or product run without observing it.
