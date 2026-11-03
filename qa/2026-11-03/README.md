# Integrated onboarding QA — 2026-11-03

Reviewed paths: `emailawesome-api-validation`, `emailawesome-hubspot-verification`, `emailawesome-list-cleaner`.

The entry flow was checked in isolated project directories using the official [Skills CLI](https://github.com/vercel-labs/skills), version 1.7.6, with the Codex project layout and copy mode:

1. Install only the selected use case or technical recipe.
2. Follow its documented product-preparation step, selecting only the official product skill from the reviewed candidate repository.
3. Confirm both complete folders match their source files, local Markdown references resolve, and no other recipes were installed.
4. Confirm that the already-available product path needs no second installation or file rewrite.

These are controlled installer and file-completeness checks, not an independent LLM behavior test or proof of automatic package dependency resolution. The agent must start the onboarding with a task and read the installed instructions; host discovery/activation can occur later. The no-installer fallback and context handoff were reviewed as instructions, not exercised in every agent client. The product-only official source is specified in each included onboarding reference.

The existing repository tests, skill structure validation and diff checks passed. No new executable helper, transport implementation or automatic installer was added. No product account was created, credentials changed, lists uploaded, verification credits consumed, proxy connection activated, purchase made, campaign sent or website changed. Existing business-workflow QA boundaries remain in the earlier reports; installation checks do not establish destination access, verification results or search indexing.
