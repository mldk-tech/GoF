import sqlite3
from pathlib import Path
from typing import Iterable

DB_PATH = Path(__file__).resolve().parent / "rag.db"


def migrate():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS docs(id INTEGER PRIMARY KEY, text TEXT)")
    if not list(cur.execute("SELECT 1 FROM docs LIMIT 1")):
        cur.executemany("INSERT INTO docs(text) VALUES(?)", [
            ("Python is a popular programming language." ,),
            ("Design patterns help organize code." ,)
        ])
    conn.commit()
    conn.close()


def search(query: str) -> Iterable[str]:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT text FROM docs WHERE text LIKE ?", (f"%{query}%",))
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return rows
