# Docker

Container configuration for Luany OS.
Orchestrates the agent, vector database, and API 
as isolated, reproducible services.

## Services
- `luany` — Main agent + FastAPI server
- `chromadb` — Vector database
- `postgres` — Trade history database

## Usage
```bash
docker-compose up --build
```
