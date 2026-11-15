# PayStream payroll: solution architecture

Version 0.9, 21 October 2026. Author: Northwind Health enterprise architecture.

## Purpose

Northwind Health is replacing its in-house payroll module with PayStream, a multi-tenant SaaS payroll
product operated by PayStream Pty Ltd. This document describes the target integration.

## Components

- Northwind HRIS (on premises): system of record for employees, salaries, bank accounts and tax file numbers.
- Integration host (on premises): runs the nightly extract job and holds the SFTP private key.
- Microsoft Entra ID: Northwind's identity provider. Staff sign in to PayStream by SAML single sign-on.
- PayStream platform (vendor cloud): employee portal, administration console and payroll engine.
- Finance general ledger (on premises): receives payroll journals from PayStream by webhook.
- Bank portal: payroll administrators upload the payment file produced by PayStream.

## Data flows

1. Each night the HRIS writes a full employee extract (CSV) to the integration host.
2. The integration host uploads the extract to PayStream's SFTP endpoint using key authentication.
3. Employees sign in to the PayStream portal through Entra ID to view payslips.
4. Payroll administrators sign in to the administration console from the corporate network.
5. After each pay run PayStream posts a journal to the finance general ledger webhook.
6. A payroll administrator downloads the payment file and uploads it to the bank portal.

## Security controls

- Single sign-on with multi-factor authentication is enforced by Entra ID conditional access.
- Payroll administrator rights are granted by membership of the Entra ID group PAYROLL-ADMINS.
- The extract is transferred over SFTP. Data at rest in PayStream is encrypted by the vendor.
- Payments require dual approval in the bank portal.

## Open items

- Webhook authentication between PayStream and the general ledger is to be confirmed with the vendor.
- Joiner, mover and leaver process for PayStream accounts is not yet designed.
