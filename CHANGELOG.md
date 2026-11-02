# Changes

## 2026-11-02 Product-interface guidance

- Align the product contract with the current Bulk CSV interface and local TXT-to-CSV preparation.
- Check for an existing suitable API key before following key-creation copy; reuse credentials without revealing or replacing them.
- Clarify accepted versus rejected Bulk submissions, per-address callbacks and prompt acknowledgement after callback validation.
- Link directly to the current Validation API documentation. Keep the existing top-up journey and helper scripts unchanged.
- Verified the relevant authenticated screens in read-only mode; no validation, upload, connection, credential change or purchase was performed. See [the QA scope](qa/2026-11-02/README.md).

## 2026-11-01 HubSpot connection review

- Record the current HubSpot-on-Zapier connection prerequisites and the closed legacy private-app creation path; preserve existing authorized connections and require an authorized administrator for a new connection when necessary.
- Documentation and local checks only: no API request, live Zap change, permission change, upload, verification or purchase was performed.

## 2026-10-20 One-time top-up guidance

- Compare one-time purchased credits with monthly plans for a genuine capacity gap, using the current account and volume context.
- Inspect separate balances, current quantity tiers and terms; pause an oversized Bulk job before validation and re-check state after an approved payment.
- Record authenticated billing, insufficient-credit Bulk preview and Cancel/Resume checks without claiming payment, credit settlement or validation after purchase.

## 2026-09-28

- Add an explicit install, account, capacity and first-result journey.
- Clarify product recommendations, current-price checks and transaction authorization.
- Expand examples and output expectations; keep synthetic and authenticated evidence separate.
- Add repository CI, reproducible issue reporting and contribution guidance.

## 2026-09-29 Live product QA

- Verified Single and synthetic Bulk through the authenticated interface.
- Clarified CSV preview, duplicate exclusions, credit checks, reserved-domain rejection and export-permission boundaries.
- Updated navigation guidance for Delivery Optimizer Beta without assuming its label proves setup capabilities.
