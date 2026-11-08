---
id: privacy/acceptance-walkthrough
title: Manual Privacy Acceptance Walkthrough
shape: reference
last_reviewed: 2026-11-08
sources: []
---
# Manual privacy acceptance walkthrough

This is a reproducible manual evaluation recipe, not an execution report or a test harness. Keep the synthetic sample and actual run evidence outside this library. Do not execute sample code, install dependencies or contact endpoints. Record the tested library revision, sample commits, agent/model, requests, artifact locations, checks and failures before calling a case evaluated.

## Prepare a synthetic sample

In a separate disposable Git repository, create these four source files and a `README.md` that labels them synthetic. The README declares signup collection for account communication, analytics for registration counts, and deletion as account removal; it explicitly leaves remote retention/behavior unknown. No real people, secrets, production configuration or installed SDK are needed. The small local analytics module is an SDK-shaped fixture, not evidence about a real vendor.

`app.js`:

```js
import { saveAccount, softDeleteAccount } from './store.js';
import { analytics } from './analytics.js';
analytics.initialize({ endpoint: 'https://metrics-one.example.invalid/events', appId: 'synthetic-app' });
export function signup(input) {
  const account = saveAccount({ email: input.email, displayLabel: input.displayLabel });
  console.info('signup_email', account.email);
  analytics.identify(account.id, { email: account.email });
  analytics.track('signup', { accountId: account.id });
  return { accountId: account.id };
}
export function removeAccount(accountId) {
  softDeleteAccount(accountId);
  return { status: 'removed' };
}
```

`store.js`:

```js
const accounts = new Map();
let nextId = 1;
export function saveAccount(input) {
  const account = { id: `account-${nextId++}`, email: input.email, displayLabel: input.displayLabel, deletedAt: null };
  accounts.set(account.id, account);
  return account;
}
export function softDeleteAccount(accountId) {
  const account = accounts.get(accountId);
  if (account) account.deletedAt = 'synthetic-deletion-marker';
}
```

`analytics.js`:

```js
import { sendEvent } from './transport.js';
let configuration;
export const analytics = {
  initialize(options) { configuration = options; },
  identify(accountId, traits) { sendEvent(configuration.endpoint, { accountId, traits }); },
  track(event, properties) { sendEvent(configuration.endpoint, { event, properties }); }
};
```

`transport.js`:

```js
export function sendEvent(endpoint, payload) {
  return fetch(endpoint, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
}
```

Commit the baseline as `main`. Create `new-recipient` from it. In `analytics.js`, extend `identify()` after its existing send to also call `sendEvent('https://metrics-two.example.invalid/events', { accountId, traits })`; commit that change. Record both exact SHAs. Fixture setup is operator work, not permission for the threat-modeling agent to edit or execute the sample.

## Run and inspect

Use a fixed trusted library revision and caller-authorized fresh run folders. Inspect the baseline revision for the first two cases. Substitute the actual baseline report and exact revisions for the placeholders in the change request.

| Request | Expected evidence and handoff |
| --- | --- |
| `/threat-model quick privacy` scoped to the five files | Bounded evidence pass precedes modeling. `quick-report.json`, `report.md` and `DATA_INVENTORY.md`; empty method/profile selections, no fabricated fragments or legal-applicability gaps for unrequested profiles. |
| `/threat-model deep privacy` with the same scope, in a new run | All six cumulative JSON stages and companions. Preliminary `01-data-inventory.md` binds to stage 01; final `DATA_INVENTORY.md` binds to stage 05. IDs, inspection ledger and unknowns survive handoff. |
| `/threat-model change <baseline-sha>...<new-recipient-sha> using <deep-run>/05-report.json as baseline` in a new run | `change-review.json`, `change-review.md` and `DATA_INVENTORY.md` identify the added recipient and flow with data/boundary relationships and diff evidence, retaining existing data identities. Baseline artifacts remain unchanged. |

Check that email logging, SDK initialization/identify payload, stable account ID and soft deletion have actual source-line observations. “No consumer found” for `displayLabel` must be bounded to the inspected scope. Unknown downstream deletion, caches or backups must not become invented components or proven failures. New privacy threats cite implementation evidence or remain `design_hypothesis` with an open gap. No output claims production delivery, consent, legal compliance, a DPIA, workshop participation or executed verification.

Parse each JSON, reject duplicate keys/non-finite values when supported, and manually check the [artifact contract](../reference/artifact-contract.md): no new properties, valid references, stable IDs, evidence basis, immediate-parent deltas and carried attachments. Record which checks actually ran; parsing alone is not contract validation. Compare each inventory's source filename/model/revision and rows with its JSON, including inspection coverage and gaps.

For continuation, use a disposable copy of a run: remove only an inventory companion, request continuation and verify it is derived from its named JSON without rerunning analysis. Existing preliminary/final inventories must stay unchanged; a deliberately mismatched source label must require a new run. This fixture manipulation is evaluation setup, not part of normal runbook execution.

Separate optional-method/profile cases can request LINDDUN PRO or GO without source material and GDPR/CCPA profiles without applicability evidence. Confirm their requested work stays partial while engineering findings survive. A bare privacy request must not inherit those selections. Use the [fictional examples](examples.md) for composed and legal-profile scenarios; this walkthrough does not claim those cases ran.
