import time
import uuid
from datetime import datetime, timezone

from database import init_db, get_conn

WORK_TIME   = 30
CONSUMER_ID = f"consumer-{uuid.uuid4().hex[:6]}"


def claim_next_task(conn):
    now = datetime.now(timezone.utc).isoformat()
    return conn.execute(
        """
        UPDATE tasks
        SET status       = 'in_progress',
            started_at   = ?,
            consumer_id  = ?
        WHERE id = (
            SELECT id FROM tasks
            WHERE status = 'pending'
            ORDER BY id
            LIMIT 1
        )
        RETURNING id, phone_number
        """,
        (now, CONSUMER_ID),
    ).fetchone()


def finish_task(conn, task_id: int) -> None:
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        "UPDATE tasks SET status = 'done', finished_at = ? WHERE id = ?",
        (now, task_id),
    )


def main() -> None:
    init_db()
    print(f"[{CONSUMER_ID}] start, WORK_TIME={WORK_TIME}s")

    with get_conn() as conn:
        while True:
            conn.execute("BEGIN IMMEDIATE")
            try:
                task = claim_next_task(conn)
                conn.execute("COMMIT")
            except Exception:
                conn.execute("ROLLBACK")
                raise

            if task is None:
                print(f"[{CONSUMER_ID}] brak zadań – czekam 5s")
                time.sleep(5)
                continue

            task_id, phone = task
            print(f"[{CONSUMER_ID}] zadanie {task_id} ({phone}) w toku...")

            time.sleep(WORK_TIME)

            conn.execute("BEGIN IMMEDIATE")
            try:
                finish_task(conn, task_id)
                conn.execute("COMMIT")
            except Exception:
                conn.execute("ROLLBACK")
                raise

            print(f"[{CONSUMER_ID}] zadanie {task_id} zakończone")


if __name__ == "__main__":
    main()