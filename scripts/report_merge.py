import csv
from glob import glob
from pathlib import Path

rows = []
for file in glob("reports/*.csv"):
    with open(file, newline="", encoding="utf-8") as f:
        rows.extend(list(csv.DictReader(f)))

Path("sample-output").mkdir(exist_ok=True)
output = Path("sample-output/optimisation-report.csv")

if rows:
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

print(f"Wrote consolidated report to {output}")
