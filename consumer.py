import csv
import msvcrt
import os
import sys
import time
import uuid
from datetime import datetime

TASKS_FILE = "tasks.csv"
HEADER = ["id", "phone_number", "status", "created_at",
          "started_at", "finished_at", "consumer_id"]

CONSUMER_ID = f"consumer-{uuid.uuid4().hex[:6]}"
WORK_TIME = int(os.environ.get("WORK_TIME", "30"))     # 30 s w produkcji
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "5"))


def claim_task():
    """Atomowo: znajdź pending, oznacz in_progress, zwróć rekord."""
    with open(TASKS_FILE, "r+", newline="") as f:
        msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
        try:
            rows = list(csv.DictReader(f))
            for row in rows:
                if row["status"] == "pending":
                    row["status"] = "in_progress"
                    row["started_at"] = datetime.now().isoformat(timespec="seconds")
                    row["consumer_id"] = CONSUMER_ID
                    f.seek(0)
                    f.truncate()
                    writer = csv.DictWriter(f, fieldnames=HEADER)
                    writer.writeheader()
                    writer.writerows(rows)
                    return row
            return None
        finally:
            msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)


def finish_task(task_id: str):
    with open(TASKS_FILE, "r+", newline="") as f:
        msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
        try:
            rows = list(csv.DictReader(f))
            for row in rows:
                if row["id"] == task_id:
                    row["status"] = "done"
                    row["finished_at"] = datetime.now().isoformat(timespec="seconds")
                    break
            f.seek(0)
            f.truncate()
            writer = csv.DictWriter(f, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(rows)
        finally:
            msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)


def main():
    print(f"[{CONSUMER_ID}] start, praca={WORK_TIME}s, poll={POLL_INTERVAL}s")
    while True:
        if not os.path.exists(TASKS_FILE):
            print(f"[{CONSUMER_ID}] brak {TASKS_FILE}, czekam...")
            time.sleep(POLL_INTERVAL)
            continue

        task = claim_task()
        if task:
            print(f"[{CONSUMER_ID}] pobrano {task['id']} ({task['phone_number']}) – wykonuję...")
            time.sleep(WORK_TIME)                       # symulacja rozmowy 30 s
            finish_task(task["id"])
            print(f"[{CONSUMER_ID}] zakończono {task['id']}")
        else:
            print(f"[{CONSUMER_ID}] brak pracy, czekam {POLL_INTERVAL}s")
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()