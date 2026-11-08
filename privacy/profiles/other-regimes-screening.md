---
id: privacy/profiles/other-regimes-screening
title: Additional Privacy Regimes Screening
shape: reference
last_reviewed: 2026-11-07
sources:
  - https://www.gov.uk/data-protection
  - https://eur-lex.europa.eu/eli/dir/2002/58/oj/eng
  - https://coag.gov/resources/colorado-privacy-act/
  - https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes
  - https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/
  - https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy
  - https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html
---
# Additional Privacy Regimes Screening

Profile ID: `other-regimes-screening`. Use the [profile pattern](../../reference/privacy-profile-pattern.md) to screen possible obligations beyond the implemented GDPR and CCPA/CPRA profiles. **All entries here are screening-only.** Completing screening does not complete a substantive assessment under any listed regime. Source pages linked below were inspected for this revision on 2026-11-07; the full legal instruments and every jurisdiction's current amendments were not exhaustively reviewed.

Record one Coverage row per relevant processing scope and topic. State geographic reach, organization/sector, affected people, data, purpose, source access and uncertainty. A supported exclusion may be `not_applicable`; an unresolved trigger is `partial`. If a trigger is supported, mark the bounded screening question assessed while creating a separate `not_assessed` coverage row with lens `privacy:other-regimes-screening:<regime-id>:substantive-review` and an open gap for the unimplemented substantive review. Do not report that regime as fully assessed.

| Topic ID / regime ID | Screening questions and required follow-up | Primary starting source |
| --- | --- | --- |
| `uk-gdpr` | Is there relevant UK establishment, offering or monitoring? Obtain current UK GDPR, Data Protection Act and applicable amendments/commencement provisions. Do not reuse EU legal conclusions unchanged. | [UK government data protection guidance](https://www.gov.uk/data-protection) |
| `eu-eprivacy` | Are device storage/access, communications confidentiality, traffic/location data or direct marketing involved? Identify Member State implementing law and applicable exceptions before prescribing consent. | [Directive 2002/58/EC and consolidated-version links](https://eur-lex.europa.eu/eli/dir/2002/58/oj/eng) |
| `us-state` | Which residents, business thresholds, sensitive data, targeted advertising and profiling are involved? Inventory candidate states separately; research each state's definitions, exemptions, amendments and dates. Colorado is an example source, not a proxy for all states. | [Colorado Attorney General privacy resources](https://coag.gov/resources/colorado-privacy-act/) |
| `lgpd` | Is Brazilian processing, collection or offering context present? Obtain applicable LGPD provisions and ANPD rules for roles, lawful grounds, rights and transfers. Do not translate GDPR conclusions into LGPD findings. | [ANPD questions and answers](https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes) |
| `canada` | What provinces, commercial activities, public-sector bodies and health contexts are implicated? Determine federal versus provincial legislation and overlapping obligations before assessing consent, safeguards or rights. | [OPC PIPEDA resources and applicable-law selector](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/) |
| `coppa` | Is the service directed to children or does relevant knowledge of children's use exist? Obtain current Rule coverage, parental-consent, notice, retention and security requirements, including operative amendment dates. | [FTC children's privacy resources](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy) |
| `hipaa` | Is a covered entity/business associate relationship and protected health information established? A health field alone does not establish HIPAA coverage. Obtain applicable Privacy, Security and Breach Notification rules and contractual facts. | [HHS Privacy Rule overview](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html) |

Also inventory plausible sector, biometric, employment, education, consumer-health and data-broker rules outside these rows. Use a new explicitly scoped screening lens and source gap when a regime has no implemented profile; do not invent coverage from a familiar name. Continue privacy-harm analysis even when no listed regime applies.

To move a regime from screening to implementation, add a sourced profile following the [extension requirements](../../reference/privacy-profile-pattern.md#adding-a-profile), with stable topics, applicability logic, evidence questions, temporal rules, verification plans and documented limitations. A future profile must be explicitly selected and loaded; a linked authority is not an instruction or permission to fetch it.
