import csv
from glob import glob
from pathlib import Path

files = glob("reports/*.csv")
rows = []
for file in files:
    with open(file, newline="", encoding="utf-8") as f:
        rows.extend(list(csv.DictReader(f)))

Path("sample-output").mkdir(exist_ok=True)
with open("sample-output/optimisation-report.csv", "w", newline="", encoding="utf-8") as f:
    if rows:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
