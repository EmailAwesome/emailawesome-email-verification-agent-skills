# HubSpot and Zapier workflow

## Connection prerequisites

Before creating a connection, check the [current HubSpot-on-Zapier requirements](https://help.zapier.com/hc/en-us/articles/8495919882253-How-to-get-started-with-HubSpot-on-Zapier). As checked on 2026-11-01, Zapier lists an active HubSpot account and Super Admin permissions for connecting the app. Reuse a suitable existing authorized connection; a user who only runs an existing workflow does not automatically need a new connection or broader permissions. If a new connection is required and the user cannot authorize it, have an already authorized administrator complete that step. Do not change roles or grant access automatically.

Use the official Zapier connection flow for this recipe. Do not substitute legacy private-app creation: HubSpot [disabled that creation path for existing accounts on 2026-10-26](https://developers.hubspot.com/changelog/legacy-apis-and-legacy-apps-whats-going-unsupported-and-when). Existing connections are not thereby proven broken; inspect the selected trigger, action and required field access before proposing migration or activation.

## Recommended flow

`HubSpot submission or lead event -> stable source ID -> EmailAwesome validation -> four explicit branches -> audit fields -> permitted next action`

## Minimum audit fields

- `emailawesome_status`
- `emailawesome_verified_at`
- `emailawesome_provider_id` when available
- `emailawesome_workflow_version`
- `emailawesome_review_reason`

Use dedicated custom properties or a clearly documented external audit table. Do not overwrite consent, subscription, legal suppression, or the original email value.

## Default routing

- `VALID`: continue only to the next separately authorized step.
- `INVALID`: hold outreach; request correction or route to reversible suppression review.
- `CATCH_ALL`: route to a review queue or declared cautious policy.
- `UNKNOWN`: retry later or route to review.
- Failure or timeout: exception queue; do not invent a final result.

## Duplicate protection

Use the HubSpot record ID plus a workflow/version key. A status write must not retrigger the same verification indefinitely. Record who owns manual retries and how failed writes are replayed.
