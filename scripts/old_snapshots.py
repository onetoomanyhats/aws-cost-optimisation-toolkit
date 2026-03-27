import argparse
from datetime import datetime, timezone, timedelta
import boto3
from common import write_csv

def main(region: str, days: int):
    ec2 = boto3.client("ec2", region_name=region)
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    snapshots = ec2.describe_snapshots(OwnerIds=["self"])["Snapshots"]

    rows = []
    for snapshot in snapshots:
        if snapshot["StartTime"] < cutoff:
            rows.append({
                "resource_type": "snapshot",
                "resource_id": snapshot["SnapshotId"],
                "start_time": snapshot["StartTime"].isoformat(),
                "region": region,
                "recommendation": f"Review snapshots older than {days} days"
            })

    path = write_csv(
        "old_snapshots.csv",
        rows,
        ["resource_type", "resource_id", "start_time", "region", "recommendation"],
    )
    print(f"Wrote {len(rows)} rows to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    parser.add_argument("--days", type=int, default=30)
    args = parser.parse_args()
    main(args.region, args.days)
