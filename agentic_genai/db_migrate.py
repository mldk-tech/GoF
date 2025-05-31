import sqlite3
from pathlib import Path

from .rag import DB_PATH

SAMPLE_DOCS = [
    "Python is a programming language.",
    "Design patterns help structure code.",
    "FastAPI is a modern web framework.",
]


def migrate() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE documents (id INTEGER PRIMARY KEY, content TEXT)")
    cur.executemany("INSERT INTO documents(content) VALUES (?)",
                    [(d,) for d in SAMPLE_DOCS])
    conn.commit()
    conn.close()


if __name__ == "__main__":
    migrate()
    print("database migrated")
