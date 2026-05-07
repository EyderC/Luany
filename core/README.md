# Core

Central brain of Luany. Contains the base agent class, 
persona definition, and the tool router that decides which 
module to activate based on user intent.

## Modules
- `base_agent.py` — Abstract base class for all agents
- `luany_agent.py` — Main agent (inherits from BaseAgent)
- `router.py` — Directs input to TRADER, TUTOR, or ANALYST mode
