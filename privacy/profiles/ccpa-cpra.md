---
id: privacy/profiles/ccpa-cpra
title: CCPA and CPRA Privacy Assessment Profile
shape: reference
last_reviewed: 2026-11-07
sources:
  - https://www.cppa.ca.gov/regulations/
  - https://www.cppa.ca.gov/pdf/20260101_ccpa_statute.pdf
  - https://www.cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf
  - https://www.cppa.ca.gov/regulations/ccpa_updates.html
  - https://cppa.ca.gov/announcements/2025/20250923.html
  - https://oag.ca.gov/privacy/ccpa
  - https://oag.ca.gov/privacy/databreach/reporting
---
# CCPA and CPRA Privacy Assessment Profile

Profile ID: `ccpa-cpra`. Apply the [profile pattern](../../reference/privacy-profile-pattern.md). CPRA amended the CCPA; this is one profile, not two independent compliance assessments. The [CPPA source index](https://www.cppa.ca.gov/regulations/) and linked statute/regulations effective January 1, 2026 were inspected for this library revision on 2026-11-07. Recheck operative sources within authorized access for the actual assessment date.

## Applicability and consumer rights

Use the [statute](https://www.cppa.ca.gov/pdf/20260101_ccpa_statute.pdf), especially Civil Code sections 1798.100–1798.145, and the Attorney General's [CCPA guidance](https://oag.ca.gov/privacy/ccpa). Topic IDs below define required coverage rows, not presumed legal obligations for every system.

| Topic ID | Evidence and assessment questions | Proposed verification |
| --- | --- | --- |
| `applicability` | Establish California consumer context, business thresholds for the relevant period, entity relationships and scoped exemptions. Obtain organizational facts outside the repository. | Challenge an exemption against each affected data category and activity. |
| `notice` | Do collection notices and policies match actual categories, purposes, recipients and retention? | Trace a newly introduced SDK field to the corresponding disclosure. |
| `access-correction-deletion` | Can requests locate, retrieve, correct or delete relevant data, subject to supported exceptions? | Plan synthetic requests across operational stores, derivatives, backups and vendors. |
| `sale-sharing` | Identify sale/sharing relationships and opt-out paths, including applicable preference signals and age-related consent rules. | Define signal, anonymous-session and account-level propagation checks. |
| `sensitive-information` | Identify covered sensitive information and uses requiring limitation handling. | Trace a limitation request through analytics and downstream recipients. |
| `nondiscrimination` | Under Civil Code section 1798.125 and regulations sections 7080–7081, do exercising rights or refusing optional processing change service treatment or incentives, and is any permitted difference supported? | Compare synthetic user paths and document the supplied justification. |

## Processing and enforcement boundaries

Use the [CCPA regulations](https://www.cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf), particularly sections 7002–7004, 7011–7014, 7020–7027, 7050–7053, 7060–7063 and 7080–7081. The CPPA source index links this document under “CCPA Regulations (Effective January 1, 2026)”; its contents identify Title 11, Division 6, Chapter 1, and the numbered regulatory sections. The filename contains `statute`, but document identity was checked against the index and PDF contents rather than inferred from the filename.

| Topic ID | Evidence and assessment questions | Proposed verification |
| --- | --- | --- |
| `purpose-retention` | Map collection, use, disclosure and retention to stated purposes and necessity; identify secondary use and excessive persistence. | Follow a purpose change and an expired synthetic record through queues and restores. |
| `choice-request-handling` | Inspect choice symmetry, dark patterns, request channels, authorized agents, verification, response timing and denial handling. Sections 7060–7063 distinguish verified requests from opt-outs/limitation requests that must not require identity verification. | Separate impersonation resistance from unnecessary friction; define pass/fail/inconclusive outcomes. |
| `recipient-contracts` | Compare actual recipient behavior with business/service-provider/contractor roles and supplied contract restrictions. | Trace opt-outs, correction and deletion obligations across recipient boundaries. |

## Security and breach dependencies

For `security-breach`, examine safeguards for the actual information and processing under Civil Code section 1798.100(e), and distinguish the narrower circumstances addressed by section 1798.150's private civil action. The [current CPPA statute compilation](https://www.cppa.ca.gov/pdf/20260101_ccpa_statute.pdf), pages 4 and 46–47, supports these distinct questions. Trace unauthorized access, disclosure, destructive changes and credential exposure; preserve evidence about protection and detection. Plan a synthetic incident timeline covering detection, containment, recipient coordination and decision evidence. Do not infer a private-action claim from every CCPA concern, or treat an audit exemption as eliminating security obligations.

Separately screen California Civil Code [section 1798.81.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.81.5.&lawCode=CIV) for security duties and [section 1798.82](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.82.&lawCode=CIV) for breach notification. These are not interchangeable with CCPA applicability or audit thresholds. Use coverage lenses `privacy:ccpa-cpra:california-security-screening` and `privacy:ccpa-cpra:california-breach-screening`; identify the entity, data definitions, incident conditions, notification recipients, operative deadlines and exemptions that need confirmation. The [Attorney General's reporting guidance](https://oag.ca.gov/privacy/databreach/reporting) confirms separate notification/reporting duties. Full legislative pages were unavailable during this library review, so this is screening coverage only: obtain current statutory text before reaching a substantive conclusion, and record an open source gap where unavailable. Do not infer notification timing from the CCPA or invent an incident or notice.

## Risk assessments, audits and ADMT

The [completed rulemaking](https://www.cppa.ca.gov/regulations/ccpa_updates.html) became effective January 1, 2026. The [CPPA timing announcement](https://cppa.ca.gov/announcements/2025/20250923.html) distinguishes this date from phased compliance. Do not use an earlier draft as the operative rule.

- `risk-assessment`: screen each processing activity under section 7150; inspect purposes, benefits, negative effects on people, safeguards and supplied review records under sections 7152–7157. Plan checks for newly introduced processing and material changes. Under section 7155, covered new processing requires assessment before initiation; continuing pre-2026 processing has a December 31, 2027 assessment deadline. First assessment-information submissions are due April 1, 2028 under section 7157. Confirm the activity-specific timing and retention duties from the actual source.
- `cybersecurity-audit`: establish applicability separately under section 7120. Record evidence needed for scope, independence, findings, remediation and certification under sections 7121–7124. First audit-report deadlines are phased across April 1 of 2028, 2029 and 2030; use the applicable revenue reference year and audit period. A code review is not the required independent audit.
- `admt`: establish the technology and significant-decision conditions under section 7200. Examine pre-use notice, opt-out/access handling and supported exceptions under the subsequent ADMT provisions. Plan a synthetic adverse-outcome/opt-out path. Section 7200 sets January 1, 2027 compliance for covered earlier use and requires compliance during covered use from that date onward. Do not equate every automation with covered ADMT.

## Completion boundary

Assess every declared topic or record explicit partial/unassessed coverage. Keep scope, role, source and timing gaps visible. A supported engineering concern is not automatically a statutory violation. Outputs supply evidence for privacy, assessment and audit owners; they do not execute attestations or certify compliance. Data-broker/Delete Act obligations and additional California sector laws require separate screening and sourced follow-up; this profile does not claim full coverage of them.
