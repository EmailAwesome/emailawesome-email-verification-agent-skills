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

## Form decisions

Perform local syntax checks before consuming verification work. Choose fail-open, fail-closed, or queue-for-review behavior based on workflow risk and latency. A raw asynchronous endpoint should not hold a browser form open indefinitely.

## Callback rules

- Restrict the callback to the configured HTTPS route and expected method.
- Authenticate it using a current verified mechanism. A caller-supplied static header is useful only when the provider reliably returns it.
- Validate content type, body size, schema, provider ID, state, and result enum.
- Apply a terminal transition once. Duplicate callbacks should return success without duplicating the downstream action.
- Do not log full addresses, API keys, authorization headers, or raw callback secrets.
