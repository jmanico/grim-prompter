# Initial understanding: Northwind Health, PayStream payroll

Prepared from the registered materials on 2026-10-30. For consultant review before any workshop.

## What the system is

Northwind Health is replacing its in-house payroll module with PayStream, a multi-tenant SaaS payroll product run by PayStream Pty Ltd (M-001). Northwind keeps its HRIS as the system of record and sends PayStream a nightly employee extract. Staff sign in through Entra ID. PayStream posts payroll journals to the finance general ledger, and a payroll administrator carries the payment file to the bank portal by hand.

## Components and who runs them

| Component | Run by | Source |
| --- | --- | --- |
| Northwind HRIS | Client | M-001 |
| Integration host | Client | M-001 |
| Microsoft Entra ID | Shared (Microsoft platform, Northwind configuration) | M-001 |
| PayStream platform, portal, administration console, SFTP endpoint, data store | Vendor | M-001, M-002, M-003 |
| Finance general ledger | Client | M-001 |
| Bank portal | Third party | M-001 |

## Data

Employee master data, salaries, bank account details and tax file numbers leave Northwind every night in a full extract (M-001). The payment file and payroll journals come back.

## Trust boundaries

1. Corporate network to PayStream cloud: SFTP upload, SAML sign-on, administration console, journal webhook (M-002).
2. Public internet to PayStream cloud: employee portal (M-002).
3. Corporate network to the bank: payment file upload (M-001).

## Controls described in the material

- Single sign-on with multi-factor authentication by Entra ID conditional access (M-001).
- Administrator rights by membership of an Entra ID group (M-001).
- SFTP for the extract; vendor encryption at rest (M-001, M-003).
- Dual approval of payments in the bank portal (M-001).
- Vendor approval and logging of support access; SOC 2 Type II report (M-003).

None of these was observed. All are statements in documents.

## What the material does not tell us

1. Whether PayStream's local administrator accounts are in use and whether they have multi-factor authentication (M-003 says it is optional).
2. What happens to the extract file on the integration host, and how the SFTP key is stored.
3. Whether the journal webhook is authenticated (M-001 lists it as open).
4. How the payment file is protected between PayStream and the bank.
5. Whether Northwind sees vendor support access.
6. How accounts are removed when staff leave (M-001 lists it as not designed).
7. The diagram (M-002) shows Entra ID and the bank outside any zone and does not show vendor support access.

## Material read

All three documents registered at this point (M-001 to M-003) were read in full. No source code or configuration is available for this engagement.
