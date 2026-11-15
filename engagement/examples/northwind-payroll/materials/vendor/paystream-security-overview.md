# PayStream security overview

Document version 4.2, August 2026. Published by PayStream Pty Ltd for customers under NDA.

## Hosting and tenancy

PayStream is a multi-tenant service. Customer data is logically separated by tenant identifier.
Data at rest is encrypted with AES-256 using keys managed by PayStream.

## Access

Customers can sign in by SAML single sign-on. Each tenant also has local administrator accounts
for initial setup and emergency access. Local accounts use a password; multi-factor authentication
for local accounts is optional and is configured by the customer.

PayStream support engineers can access a customer tenant to resolve a support case. Access is
approved internally and logged. Customers can request the access log.

## Integrations

Bulk data is received over SFTP with key or password authentication.
Outbound webhooks can be signed with an HMAC shared secret when the customer enables signing.

## Assurance

PayStream holds a SOC 2 Type II report covering security and availability, renewed annually.
The report is available on request.
