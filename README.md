# BehaviorDiff Action smoke test

This repository is a minimal external-consumer smoke test for the public
`abheeshtroy/BehaviorDiff@v0.1.0-rc.1` GitHub Action. It intentionally contains
no regression: its clean `main` branch provides a deterministic baseline for a
future pull-request comparison.

The Dockerized FastAPI application exposes:

- `GET /health` — returns HTTP 200.
- `GET /quote` — returns `{"currency":"USD","amount":100}`.

`behaviordiff.yaml` defines the Docker build and a single workflow that calls
`GET /quote` and captures the complete JSON response. The GitHub workflow runs
on pull requests, supplies the PR base and head SHAs to BehaviorDiff, fails on
findings, and uploads `.behaviordiff-results` even if the comparison fails.

## Run locally

```bash
docker build -t behaviordiff-action-smoke .
docker run --rm -p 8000:8000 behaviordiff-action-smoke
curl -i http://localhost:8000/health
curl http://localhost:8000/quote
```

Expected quote response:

```json
{"currency":"USD","amount":100}
```

The BehaviorDiff GitHub Action is intentionally not run locally; it is tested
by the pull-request workflow using its public release reference.
