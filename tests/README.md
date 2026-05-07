# Tests

Automated benchmarking suite for Luany.
Every push to main triggers these tests via GitHub Actions.
If they fail, the deployment is blocked.

## Test Types
- `test_risk_manager.py` — Validates challenge rules enforcement
- `test_strategy.py` — Checks signal generation logic
- `test_api.py` — Endpoint response validation
- `benchmark_agent.py` — Asks Luany 5 hard questions and 
  scores accuracy automatically
