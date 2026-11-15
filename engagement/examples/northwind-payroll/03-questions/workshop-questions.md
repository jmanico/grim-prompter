# Workshop questions: Northwind Health, PayStream payroll

Questions for the architecture walkthrough, drawn from what the registered material leaves open. Prepared after the consultant's review of the initial understanding.

7 questions, 1 open. Priority: **must** blocks the threat model, **should** changes a finding, **could** adds detail.

## Access and identity

Who should attend: Payroll systems lead

- [x] **Q-001** (must) Does the PayStream tenant have local administrator accounts in use? Who holds them, and do they have multi-factor authentication?
  - Why it matters: The vendor says local accounts exist and multi-factor authentication is optional. A local account would bypass single sign-on.
  - Listen for: Shared accounts, accounts left from implementation, break-glass arrangements.
  - Relates to: M-003
  - Answer (W-01): Two shared local administrator accounts exist without multi-factor authentication.
- [x] **Q-002** (must) How are PayStream accounts removed or changed when someone leaves or changes role?
  - Why it matters: The design records the joiner, mover and leaver process as not yet designed.
  - Listen for: Manual steps, reliance on single sign-on alone, periodic reconciliation.
  - Relates to: M-001
  - Answer (W-02): Accounts are not removed; single sign-on stops working but the account stays active.

## Integration

Who should attend: Integration engineer

- [x] **Q-003** (must) What happens to the nightly extract on the integration host after transfer, and where is the SFTP key stored and rotated?
  - Why it matters: The extract holds every employee's bank account and tax file number.
  - Listen for: Retention period, who can sign in to the host, key in a file or a vault.
  - Relates to: M-001
  - Answer (W-01, W-02): Key in the service account's home folder, never rotated. Extract is archived for thirty days (corrected in W-02).
- [~] **Q-004** (must) Is the journal webhook into the general ledger authenticated? Is signing enabled, and does the ledger check it?
  - Why it matters: The design lists webhook authentication as open, and the vendor says signing is optional.
  - Listen for: Address filtering only, shared secret, replay protection.
  - Relates to: M-001, M-003
  - Answer (W-01): Address filtering only is known; signing status to be checked with the vendor.

## Payments

Who should attend: Payroll systems lead

- [x] **Q-005** (should) Walk us through how the payment file gets from PayStream to the bank. Who can change it on the way, and what does the bank approver see?
  - Why it matters: A changed payment file redirects salaries.
  - Listen for: Downloads to a laptop, email, shared drives, what dual approval actually checks.
  - Relates to: M-001
  - Answer (W-01): Downloaded to a laptop and uploaded by hand; a second approver releases it in the bank portal.

## Vendor

Who should attend: Payroll systems lead, vendor manager, Vendor manager

- [x] **Q-006** (should) Can Northwind see when PayStream support accesses the tenant? Has the SOC 2 report been obtained and read?
  - Why it matters: Vendor staff can reach payroll data; the client relies on the vendor's controls.
  - Listen for: Whether the access log has ever been requested; contract terms.
  - Relates to: M-003
  - Answer (W-01): Northwind does not see support access and has not requested the log. SOC 2 report not yet obtained.
- [ ] **Q-007** (could) Does PayStream encrypt tax file numbers separately from other data, and who holds the keys?
  - Why it matters: Tax file numbers carry specific handling obligations.
  - Listen for: Field-level encryption, customer-managed keys.
  - Relates to: M-003
