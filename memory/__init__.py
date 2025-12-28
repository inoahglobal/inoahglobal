"""
iNoah Memory - The Unified Memory Core (Exocortex)
Vector database for persistent memory and RAG retrieval.
Uses ChromaDB for storage and Ollama for embeddings.
"""

from .store import MemoryStore
from .ingest import DocumentIngester

__all__ = ["MemoryStore", "DocumentIngester"]


