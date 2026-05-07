# Memory

Luany's long-term memory layer. Stores trade history, market 
analysis, and conversation context as vector embeddings 
for semantic search.

## Stack
- ChromaDB — vector database for semantic retrieval
- PostgreSQL — structured trade history and metrics
- JSON — live challenge state (drawdown, P&L, daily loss)
