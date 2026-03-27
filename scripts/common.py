from pathlib import Path
import csv

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

def write_csv(filename, rows, fieldnames):
    path = REPORTS_DIR / filename
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path
