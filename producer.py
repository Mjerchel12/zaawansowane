import csv
import os
import random
import sys
from datetime import datetime

TASKS_FILE = "tasks.csv"
HEADER = ["id", "phone_number", "status", "created_at",
          "started_at", "finished_at", "consumer_id"]


def init_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", newline="") as f:
            csv.writer(f).writerow(HEADER)


def produce(n: int = 1):
    init_file()
    with open(TASKS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for i in range(1, n + 1):
            writer.writerow([
                f"task_{datetime.now().strftime('%H%M%S')}_{i:03d}",
                f"+48{random.randint(100_000_000, 999_999_999)}",
                "pending",
                datetime.now().isoformat(timespec="seconds"),
                "", "", "",
            ])
    print(f"[producer] zapisano {n} zadań do {TASKS_FILE}")


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    produce(n)