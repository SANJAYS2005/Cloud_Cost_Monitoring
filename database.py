import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("cloudwise.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cost_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                estimated_cost REAL NOT NULL,
                budget REAL NOT NULL,
                avg_cpu REAL NOT NULL
            )
        """)

def save_snapshot(estimated_cost, budget, avg_cpu):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO cost_history (estimated_cost, budget, avg_cpu) VALUES (?, ?, ?)",
            (estimated_cost, budget, avg_cpu)
        )

def get_history(limit=20):
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, created_at, estimated_cost, budget, avg_cpu FROM cost_history ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()
    return [dict(row) for row in rows]
