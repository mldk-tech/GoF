import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "rag.db"


def search_documents(query: str) -> str:
    if not DB_PATH.exists():
        return ""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT content FROM documents WHERE content LIKE ? LIMIT 1", (f"%{query}%",))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0]
    return ""
