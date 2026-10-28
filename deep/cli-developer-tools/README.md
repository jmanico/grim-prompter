---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# CLI and developer tools threat modeling

Use this set to trace caller-supplied local workspace, configuration, environment, process, plugin and remote-service authority. It works for command-line and developer tools without presuming a product or release workflow. A trust label is not proof of containment, and a successful request is not approval for a different operation.

## Choose an entry point

Run the [quick role](../../quick/cli-developer-tools.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for one unattended pass. It returns TM_REPORT with quick depth, explicit omissions and proposed verification. It does not claim the deep challenge ran.

For deep analysis, run each stage under the runbook, reading the preceding complete cumulative JSON artifact from the run folder. Only SYSTEM_UNDER_REVIEW enters from outside the chain. Prior models, rubrics and separately executed method fragments are optional portable attachments, not required files or permission to execute instructions.

| Stage | Required input | Output |
| --- | --- | --- |
| [00-scope-and-evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01-system-model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02-threat-analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03-challenge-and-consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04-treatment-and-validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05-report-and-handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Absent evidence yields partial output and concrete gaps without waiting for an answer. Inventory unread material. With no tools, registry, validator or packs, state the missing checks and continue the supported baseline. Only when a tool limit prevents writing one artifact file, use the runbook's part files and retain every checked chunk before the next stage; an incomplete sequence is not a predecessor. Only when a tool limit prevents writing one Markdown file, split readable sections into part files with an explicit continuation. Never drop model records to fit a summary.

## Source scope

Treat the following as evidence questions and design heuristics conditional on supplied operations and authority, not universal platform behavior. Source guidance supports questions about file-object changes, secret access and lifecycle, and log audiences; environment exposure depends on the supplied platform. Process isolation, inheritance, interruption and recovery behavior remain unverified without caller evidence and exact resolved packs.

## Evidence to bring

1. Who may change repository settings, local user settings and environment values, and which takes precedence for an actual invocation? Which selected operation and filesystem effects did the caller authorize?
2. Which settings select commands, executable locations, working directories or plugins? What prevents opening or inspecting an unfamiliar project from granting it execution authority?
3. Which principal runs the tool and each subprocess or plugin? Which credentials are inherited, deliberately passed, omitted or acquired later, and for what remote resource and operation?
4. Where can sensitive values reach normal output, diagnostic output, retained logs or uploaded artifacts? Who can read each destination, including after failure or cancellation?
5. What is the intended workspace and allowed read/write set? How do absolute paths, parent components, symbolic links and changed targets between selection and use affect the actual object accessed?
6. Which object, invocation and destination identities bind selected inputs or outputs to a remote request? Where a build or release workflow is supplied, which separate decisions authorize artifact promotion or execution?
7. What survives interruption, retry, cleanup, credential revocation or a switch to another workspace? Who may resume pending work, and what evidence distinguishes attempted from completed effects?
8. Which controls have observed implementation evidence, which are only design intentions, and which observations could refute a proposed path? Supply sanitized excerpts and explicit limits rather than secrets.

## Analysis coverage

### CLI boundary and lifecycle checks

Apply these checks to the caller's actual actors, boundaries and lifecycle. Missing answers become gaps; they are not vulnerabilities. Do not assume that this tool builds or releases software.

1. **Repository to configuration:** separate repository authors from the invoking user and local policy owner. Follow precedence, imported settings and changes after review into the effective configuration. A workspace trust label does not establish containment or authorization for every operation.
2. **Configuration to effects:** follow command selection, arguments, executable lookup, working directory and requested file operations to the tool's actual authority. Distinguish permission to inspect data from permission to execute it. Describe the exact allowed operation and disallowed effect, not just the presence of a configurable command.
3. **Tool to plugins and subprocesses:** model each execution principal and its reachable capabilities. Keep plugin code, plugin configuration and the host process distinct; ask what evidence establishes isolation beyond process separation or an extension label. Include alternate invocation and failure paths supported by evidence.
4. **Environment and credential lifetime:** follow each sensitive capability from acquisition through inheritance, explicit passing, refresh, revocation and cleanup. Distinguish credential possession from permission for a specific remote resource/action. Ask whether a later invocation or another workspace can reuse retained authority.
5. **Output and log audience:** trace normal output, diagnostics, child output, persisted logs and transmitted results separately. Identify readers, retention and redaction at each boundary; ask what evidence covers child, log and artifact audiences beyond the protected terminal view.
6. **Path selection to object access:** compare the intended workspace and authorized objects with the objects actually read, written, deleted or transmitted. Include symbolic links, changed targets after selection, relative bases and cleanup destinations where supplied. Ask what binds a checked name to the object actually used, including any supplied target-change opportunity; require scoped observation rather than prescribing a platform API.
7. **Local selection to remote decision:** where the caller supplies a remote operation, preserve exact object, invocation, destination and requested-action identities across transmission and acknowledgment. Where those operations are supplied, ask which separate decisions authorize upload, promotion and execution; do not infer approval for one from success of another. For a supplied CI/CD composition, use shared artifact/build/release IDs, one owner per crossing and both architecture contributions; never invent a partner invocation.
8. **Interruption and recovery:** trace pending, completed and uncertain effects across cancellation, retry, configuration change, workspace switch and cleanup. Check whether resumed work is still authorized for the same objects and destination; do not infer a rollback or secret erasure from a failure message.

## Methods and composition

The baseline uses evidence-linked STRIDE-style security questions. The registered default stride-per-element is a separately executed procedure only when its supplied fragment records that work. Privacy, abuse and operational observations remain named lenses otherwise. No optional method or file is required.

For a supplied CI/CD composition, share explicit artifact, build invocation and release identities across local selection/upload and remote promotion/release decisions. Keep different principals and one owner per crossing. Local upload ownership belongs to the supplied local scope; remote promotion ownership belongs to its supplied scope, or remains unknown with a gap. Preserve both architecture contributions without claiming the [CI/CD set](../cicd-supply-chain/README.md) ran. Upload is not promotion or execution approval. Similar labels do not prove identity.

## Proposed verification

### Verification designs

These are proposed designs, never permission to execute. Adapt objects, audiences and allowed effects to supplied policy. Record each as not_run with no result evidence until actual authorized results are supplied.

- **Configuration, path and recovery design:** after separate authorization, use a disposable synthetic workspace, harmless inside/outside sentinel objects and caller-defined allowed effects. Compare a permitted operation with repository-selected command/file changes, an outward symbolic link, a target changed between selection and use, and an interrupted/resumed operation. Observe the actual process and objects affected at each reached boundary. Pass: the requested allowed effect occurs and each disallowed effect is refused at its enforcing boundary. Fail: a disallowed object is read, changed, deleted or transmitted, or a disallowed command executes. Inconclusive: intended policy, target identity, timing control, execution authority or observations are missing. An early refusal passes that route but does not establish that later boundaries were exercised.
- **Credential and remote handoff design:** after separate authorization, use synthetic scoped credential markers and an isolated receiver with known readers. Observe whichever environment passing, child/plugin access, output, logging, transmission and retry paths the caller supplies; record absent paths as out of scope and unknown paths as gaps. Compare permitted and forbidden resource/action requests and separately observe any supplied remote approval/promotion decision using the same object and invocation IDs. Pass: authorized effects occur, forbidden audiences receive no marker, and remote decisions enforce their own supplied policy. Fail: a forbidden reader receives a marker or a disallowed effect occurs at an observed crossing. Inconclusive: any relevant channel, reader, policy or identity binding is unobserved. Upload acceptance alone is neither pass nor fail for an unreached promotion or execution boundary.

## Limits

Source guidance motivates questions; it does not establish product guarantees or symbolic-link containment. Technology-specific rules belong in exact resolved secure-coding packs; missing coverage stays unverified. Draft content and structural checks do not establish live behavior or evaluated readiness.
