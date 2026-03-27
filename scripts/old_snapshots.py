import argparse
import csv
from datetime import datetime, timezone, timedelta
from pathlib import Path
import boto3

def main(region: str, days: int):
    ec2 = boto3.client("ec2", region_name=region)
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    response = ec2.describe_snapshots(OwnerIds=["self"])
    rows = []
    for snapshot in response.get("Snapshots", []):
        if snapshot["StartTime"] < cutoff:
            rows.append({
                "resource_type": "snapshot",
                "snapshot_id": snapshot["SnapshotId"],
                "start_time": snapshot["StartTime"].isoformat(),
                "region": region
            })

    Path("reports").mkdir(exist_ok=True)
    with open("reports/old_snapshots.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["resource_type", "snapshot_id", "start_time", "region"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    parser.add_argument("--days", type=int, default=30)
    args = parser.parse_args()
    main(args.region, args.days)
