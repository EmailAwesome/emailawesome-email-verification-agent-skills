# Asynchronous validation contract

## State separation

`source record -> internal request -> provider submission -> provider job -> validated callback or bounded reconciliation -> business policy`

Persist:

- source record ID
- internal request and idempotency key
- provider ID
- submission time and attempt
- provider job state
- final verification result
- callback event fingerprint when available
- retry count and terminal time
- business decision and policy version

The reconciliation helper reports `mapping_complete` separately from `terminal_results_complete`. A mapped `PENDING` job is not a final email result. Treat `reconciled` as true only when every expected source ID has a terminal job and an explicit final `email_address_status` or `verification_result` in the four supported states.

## Bulk admission and callbacks

Inspect the submission response before waiting for results. Map accepted provider job IDs to source records and retain rejected input records and their reasons separately. The [in-app API guide](https://app.emailawesome.com/api-verifications), read on 2026-11-02, describes one callback per accepted address, not one per batch; addresses in `rejected_validations` do not trigger callbacks. Recheck the current response schema in the official documentation before implementing this mapping.

Wait for callbacks only for accepted jobs. A submission rejection is not an `INVALID` verification result. Reconcile accepted source IDs with the helper, and report original input, accepted, rejected and still-pending counts together so rejected records do not disappear from the overall handoff. The guide and example payload are documentation, not a live delivery test or a retry guarantee.

## Form decisions

Perform local syntax checks before consuming verification work. Choose fail-open, fail-closed, or queue-for-review behavior based on workflow risk and latency. A raw asynchronous endpoint should not hold a browser form open indefinitely.

## Callback rules

- Restrict the callback to the configured HTTPS route and expected method.
- Authenticate it using a current verified mechanism. A caller-supplied static header is useful only when the provider reliably returns it.
- Validate content type, body size, schema, provider ID, state, and result enum.
- After authenticating and validating a callback, durably record or queue it and acknowledge promptly with `2xx`; defer slower business processing. A public webhook demo is a separate data destination: use an endpoint controlled by the user for real contacts and secrets, and obtain authorization before sending any test data elsewhere.
- Apply a terminal transition once. Duplicate callbacks should return success without duplicating the downstream action.
- Do not log full addresses, API keys, authorization headers, or raw callback secrets.
