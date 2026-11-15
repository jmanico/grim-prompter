# SYSTEM_UNDER_REVIEW: Northwind Health, PayStream payroll

Prepared 2026-10-30 from registered material; workshop section added 2026-11-04. No source code or configuration was available (code access: none).

## Purpose

Northwind Health is replacing its in-house payroll module with PayStream, a multi-tenant SaaS payroll product. The review supports Northwind's decision to go live with the integration.

## Supplied facts

All facts from documents and diagrams are claims. None was observed in code or configuration.

| Label | Fact | Source | Locator |
| --- | --- | --- | --- |
| F-01 | The HRIS is the system of record for employees, salaries, bank accounts and tax file numbers. | M-001 v0.9 | `materials/design/solution-architecture.md:12` |
| F-02 | The integration host runs the nightly extract job and holds the SFTP private key. | M-001 v0.9 | `materials/design/solution-architecture.md:13` |
| F-03 | Staff sign in to PayStream by SAML single sign-on through Microsoft Entra ID. | M-001 v0.9 | `materials/design/solution-architecture.md:14` |
| F-04 | A full employee extract (CSV) is written nightly and uploaded to PayStream's SFTP endpoint with key authentication. | M-001 v0.9 | `materials/design/solution-architecture.md:21-22` |
| F-05 | Payroll administrators sign in to the administration console from the corporate network. | M-001 v0.9 | `materials/design/solution-architecture.md:24` |
| F-06 | PayStream posts a journal to the general ledger webhook after each pay run. | M-001 v0.9 | `materials/design/solution-architecture.md:25` |
| F-07 | A payroll administrator downloads the payment file and uploads it to the bank portal. | M-001 v0.9 | `materials/design/solution-architecture.md:26` |
| F-08 | Control described: multi-factor authentication enforced by Entra ID conditional access. | M-001 v0.9 | `materials/design/solution-architecture.md:30` |
| F-09 | Control described: administrator rights by membership of the Entra ID group PAYROLL-ADMINS. | M-001 v0.9 | `materials/design/solution-architecture.md:31` |
| F-10 | Control described: payments require dual approval in the bank portal. | M-001 v0.9 | `materials/design/solution-architecture.md:33` |
| F-11 | Open item: webhook authentication is to be confirmed with the vendor. | M-001 v0.9 | `materials/design/solution-architecture.md:37` |
| F-12 | Open item: the joiner, mover and leaver process for PayStream accounts is not designed. | M-001 v0.9 | `materials/design/solution-architecture.md:38` |
| F-13 | Vendor statement: tenants are logically separated; data at rest is encrypted with vendor-managed keys. | M-003 v4.2 | `materials/vendor/paystream-security-overview.md:7-8` |
| F-14 | Vendor statement: each tenant has local administrator accounts with a password; multi-factor authentication for them is optional and customer-configured. | M-003 v4.2 | `materials/vendor/paystream-security-overview.md:12-14` |
| F-15 | Vendor statement: support engineers can access a tenant; access is approved internally and logged; customers can request the log. | M-003 v4.2 | `materials/vendor/paystream-security-overview.md:16-17` |
| F-16 | Vendor statement: outbound webhooks can be signed with an HMAC shared secret when the customer enables signing. | M-003 v4.2 | `materials/vendor/paystream-security-overview.md:22` |
| F-17 | Vendor statement: a SOC 2 Type II report is available on request. The report itself was not supplied. | M-003 v4.2 | `materials/vendor/paystream-security-overview.md:26-27` |

## Diagram in text (M-002 v0.3)

Source: `materials/diagrams/context-diagram.mmd:1-22`.

- **Corporate network**: Northwind HRIS, integration host, finance general ledger, payroll administrator. HRIS sends to the integration host.
- **Internet**: employee.
- **PayStream cloud**: SFTP endpoint, employee portal, administration console, PayStream platform, PayStream data store. The three entry points feed the platform; the platform writes to the data store.
- **Crossings**: integration host to SFTP endpoint (nightly extract); employee to employee portal (single sign-on); payroll administrator to administration console; Entra ID to PayStream platform (SAML assertion); PayStream platform to general ledger (journal webhook); payroll administrator to bank portal (payment file).
- **Not shown or unclear**: Entra ID and the bank portal sit outside every zone; vendor support access is not drawn; the payment file's path from PayStream to the administrator is not drawn.

## Workshop W-01, 2026-11-04 (M-004)

Statements are claims by the named speaker. Locators are lines in `materials/_text/M-004-2026-11-04-architecture-walkthrough.vtt.txt`.

| Label | Fact | Speaker | Lines |
| --- | --- | --- | --- |
| F-18 | Two local administrator accounts from the implementation project are still in use, shared, and without multi-factor authentication. Supplements F-14. | Marcus Lee | 2 |
| F-19 | The extract job deletes the file after a successful transfer. The SFTP key is in the service account's home folder and has not been rotated. | Priya Raman | 4 |
| F-20 | The webhook endpoint accepts traffic from PayStream's address range only; whether signing is enabled is not known. F-11 stays open. | Priya Raman | 6 |
| F-21 | The payment file is downloaded to the administrator's laptop and uploaded to the bank portal; a second approver releases it there. | Marcus Lee | 7 |
| F-22 | Northwind has never requested the vendor support access log. | Marcus Lee | 9 |

## Conflicts and gaps

- F-08 says multi-factor authentication is enforced; F-14 and F-18 describe local accounts outside single sign-on. Not a contradiction in the documents, but the control does not reach those accounts.
- Webhook signing (F-11, F-16, F-20): unknown.
- Leaver process (F-12): not designed.
- Vendor audit report (F-17): not supplied.

## Inspection coverage

| Item | Read | Notes |
| --- | --- | --- |
| M-001 solution architecture v0.9 | Full | |
| M-002 context diagram v0.3 | Full | Mermaid source; text equivalent above |
| M-003 vendor security overview v4.2 | Full | Vendor's own statements |
| M-004 workshop transcript | Full | |
| Source code | Not available | |
| Tenant configuration | Not available | No export supplied |
| Vendor SOC 2 report | Not available | Requested |
