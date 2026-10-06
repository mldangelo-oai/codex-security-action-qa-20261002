# Synthetic scan scope

This repository is a QA fixture, not a deployed application. Review the Python
code under `fixture/` for concrete security problems. Treat `greeting_response`
as a synthetic HTTP handler whose `display_name` argument comes from an
unauthenticated request and whose HTML response is rendered by a browser. Do not invent findings to
satisfy the test: a complete scan with zero findings is a valid result.

The SARIF file under `qa/` is an independent ingestion control and is explicitly
synthetic. It does not describe a vulnerability.
