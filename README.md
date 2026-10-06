# Codex Security Action synthetic QA

This public repository contains only synthetic code and a manually triggered
workflow for testing the Codex Security GitHub Action at commit
`6091910126a2adf5d0b6081e80818e3812d6fb36`.

The **Action live QA** workflow runs two independent checks:

- A real model-backed standard scan of `fixture/`, using `gpt-5.6-sol` with low
  reasoning effort, a $5 estimated cost stop threshold, and a 20-minute job
  timeout. In-flight requests can exceed the cost threshold. The job requires
  complete scan coverage and uploads the Action's validated SARIF using its
  reported commit SHA and Git ref.
- A deterministic SARIF upload containing one explicitly synthetic warning.
  This separately verifies GitHub code scanning ingestion even when the model
  finds no vulnerabilities. The warning is a test marker, not a security finding.

Set the repository Actions secret `CODEX_SECURITY_API_KEY` before manually
dispatching the workflow. It is passed only to the scan step as `OPENAI_API_KEY`.
Manual dispatch runs the repository scan and ingestion control. Same-repository
pull requests changing `fixture/` run a diff scan that must find the intentionally
introduced vulnerability, fail its severity policy, and upload validated SARIF
for the exact PR head. Fork PRs are skipped. No scan runs on pushes or a schedule.
Each model-backed invocation has a $5 estimated stop threshold.

Ubuntu jobs install system Bubblewrap and load its distribution AppArmor profile
as required by CLI 0.2.0. The kernel namespace restriction remains enabled.

The scanner fixture has no external dependencies, service, real users, or data.
Reports contain only this public synthetic fixture and are retained for one day.
Local `.env.local` files are ignored and must never be committed.
