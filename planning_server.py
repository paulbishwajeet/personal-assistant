import sqlite3
from datetime import datetime
import uuid
from fastmcp import FastMCP
from pathlib import Path

# Match the exactWorking structure of time_server.py
mcp = FastMCP("life-ops-planning")

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = str(BASE_DIR / "planning.db")

@mcp.tool()
def create_task(title: str, description: str | None = None) -> dict:
    """Create a new pending task."""
    task_id = str(uuid.uuid4())
    now = datetime.now().isoformat(timespec="seconds")
    task = {"id": task_id, "title": title, "description": description, "status": "pending", "created_at": now, "updated_at": now}
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)", (task["id"], task["title"], task["description"], task["status"], task["created_at"], task["updated_at"]))
    conn.commit()
    conn.close()
    return task

@mcp.tool()
def list_tasks(status: str | None = None) -> list[dict]:
    """List tasks."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    if status:
        cur.execute("SELECT * FROM tasks WHERE status = ? ORDER BY created_at", (status,))
    else:
        cur.execute("SELECT * FROM tasks ORDER BY created_at")
    rows = cur.fetchall()
    conn.close()
    return [{"id": row[0], "title": row[1], "status": row[3]} for row in rows]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT, description TEXT, status TEXT, created_at TEXT, updated_at TEXT)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    mcp.run(show_banner=False)
