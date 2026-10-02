# Synthetic scan scope

This repository is a QA fixture, not a deployed application. Review the Python
code under `fixture/` for concrete security problems. Do not invent findings to
satisfy the test: a complete scan with zero findings is a valid result.

The SARIF file under `qa/` is an independent ingestion control and is explicitly
synthetic. It does not describe a vulnerability.
