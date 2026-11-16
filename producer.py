import random
import string
import time
from datetime import datetime, timezone

from database import init_db, get_conn


def generate_phone() -> str:
    return "+48" + "".join(random.choices(string.digits, k=9))


def produce(count: int = 10, interval: float = 2.0) -> None:
    init_db()
    with get_conn() as conn:
        for _ in range(count):
            now = datetime.now(timezone.utc).isoformat()
            cur = conn.execute(
                "INSERT INTO tasks (phone_number, status, created_at) "
                "VALUES (?, 'pending', ?)",
                (generate_phone(), now),
            )
            print(f"[producer] dodano zadanie id={cur.lastrowid}")
            time.sleep(interval)


if __name__ == "__main__":
    produce()