# GitHub Actions — CI/CD Workflows

Automated pipelines that run on every push to main.

## Workflows
- `ci.yml` — Runs all tests before any deployment
- `deploy.yml` — Auto-deploys to VPS (Hostinger) if tests pass
- `benchmark.yml` — Weekly agent accuracy report

## Flow
push to main → run tests → if pass → deploy to VPS
                         → if fail → block deployment, notify
