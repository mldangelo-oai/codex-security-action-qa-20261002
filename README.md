# Codex Security Action synthetic QA

This public repository contains only synthetic code and a manually triggered
workflow for testing the Codex Security GitHub Action at commit
`86ef34f489c4374dbd19b49ff70f158d5e5c1a94`.

The **Action live QA** workflow runs two independent checks:

- A real model-backed standard scan of `fixture/`, using `gpt-5.6-sol` with low
  reasoning effort, a $1 estimated cost stop threshold, and a 20-minute job
  timeout. In-flight requests can exceed the cost threshold. The job requires
  complete scan coverage and uploads the Action's validated SARIF using its
  reported commit SHA and Git ref.
- A deterministic SARIF upload containing one explicitly synthetic warning.
  This separately verifies GitHub code scanning ingestion even when the model
  finds no vulnerabilities. The warning is a test marker, not a security finding.

Set the repository Actions secret `CODEX_SECURITY_API_KEY` before manually
dispatching the workflow. It is passed only to the scan step as `OPENAI_API_KEY`.
The workflow does not run on pushes, pull requests, or a schedule.

The scanner fixture has no external dependencies, service, real users, or data.
Reports contain only this public synthetic fixture and are retained for one day.
Local `.env.local` files are ignored and must never be committed.
