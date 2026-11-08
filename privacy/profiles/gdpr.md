---
id: privacy/profiles/gdpr
title: GDPR Privacy Assessment Profile
shape: reference
last_reviewed: 2026-11-07
sources:
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
  - https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en
  - https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en
  - https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en
  - https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en
---
# GDPR Privacy Assessment Profile

Profile ID: `gdpr`. Apply the [profile pattern](../../reference/privacy-profile-pattern.md) to each in-scope processing activity. These questions support engineering and assessment handoffs under EU GDPR; national variations, sector rules and case-specific interpretations require their own evidence. UK GDPR is screened separately. The source pages below were inspected for this library revision on 2026-11-07; that is not a freshness claim for a future run.

## Applicability and legal grounds

For `applicability`, establish material/territorial scope, exclusions, affected people, roles and relevant Member States; obtain organizational evidence where the repository cannot establish them. Start with Articles 2–4 of the [regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng). Record uncertainty rather than treating all internet services as covered.

For `lawful-basis`, map each purpose to its supplied basis and reasoning. Challenge unrelated secondary uses and unsupported necessity. For `consent`, where relied on, inspect collection, scope, evidence, withdrawal and downstream propagation; do not manufacture consent or assume every purpose needs it. For `sensitive-children`, identify special-category/criminal-offence data, children's services, applicable conditions and age-related national rules. Cite Articles 6–10 and the Commission's [legal-grounds guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en). Proposed checks should follow changed purposes and withdrawal through queued work using synthetic records.

## Principles and information

Use the Commission's [principles guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en) and Article 5 for these topics; use Articles 12–14 for the specific transparency and notice questions:

| Topic ID | Evidence and assessment questions | Proposed verification |
| --- | --- | --- |
| `purpose-minimization` | Which fields, inferences and recipients are necessary for each purpose? Can authorized analytics repurpose them? | Trace an optional field from collection to every consumer; compare a minimized design. |
| `accuracy` | How are corrections propagated to decisions and derived records? | Introduce a synthetic correction and define expected downstream changes. |
| `retention` | What justifies each retention period, exception and disposal mechanism? Include backups, logs and embeddings. | Define expiry/deletion checks across replicas and restore paths. |
| `transparency` | Do supplied notices match purposes, sources, recipients and actual flows? | Compare notice versions with modeled collection and disclosure paths. |

## Rights

For `rights`, cover access, correction, erasure, restriction, portability and objection with their conditions and exceptions, using Articles 12–21 and the EDPB's [rights guidance](https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en). Examine request discovery, proportionate identity verification, response timing, denial reasoning, recipient notification and complete retrieval. Proposed verification should distinguish a legitimate request, an impersonation attempt, a lawful exception, partial vendor deletion and inaccessible data. Keep legal deadlines sourced; do not equate account removal with erasure everywhere.

For `automated-decisions`, assess profiling and decisions within Article 22's scope, meaningful human involvement, applicable exceptions, explanations and routes to contest outcomes. Describe effects on people, not just prediction accuracy. Plan a synthetic adverse-decision review and identify evidence needed to establish actual intervention.

## Governance, safeguards and assessment

Use Articles 24–39 (including Articles 37–39 for DPO designation, position and tasks) and the Commission's [obligations guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en):

| Topic ID | Evidence and assessment questions | Proposed verification |
| --- | --- | --- |
| `design-defaults` | Are initial settings, access and collection bounded to the purpose? | Compare new-account defaults and privileged overrides. |
| `processors` | Do role allocations, instructions, contracts and subprocessors match observed flows? | Trace a recipient change or rights request across the contractual boundary. |
| `accountability` | Are processing records, responsibility and DPO applicability documented? | Compare the inventory with supplied records; name missing organizational evidence. |
| `security-breach` | What safeguards and incident detection/notification dependencies protect people? | Define a synthetic incident timeline; separate controller and processor duties. |
| `dpia` | Is high-risk processing screened, with necessity, proportionality, people’s risks, safeguards and residual concerns documented? | Identify changes that require reassessment and evidence for consultation/approval. |

For `transfers`, map recipients, destinations, onward transfers and supplied transfer mechanism against Articles 44–49. Propose checks for a newly added destination and restrictions on onward use. Do not infer a valid mechanism from encryption or a vendor's location.

## Completion boundary

Every topic above needs scoped coverage, including supported non-applicability or explicit gaps. DPIA material is a supporting handoff, not an executed formal DPIA or regulatory approval. Unavailable contracts, national rules, source text or organizational decisions prevent conclusions that depend on them; continue supported privacy-harm analysis.
