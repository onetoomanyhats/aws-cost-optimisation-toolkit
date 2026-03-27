import argparse
import csv
from pathlib import Path
import boto3

def main(region: str):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_volumes(Filters=[{"Name": "status", "Values": ["available"]}])
    rows = []
    for volume in response.get("Volumes", []):
        rows.append({
            "resource_type": "ebs",
            "volume_id": volume["VolumeId"],
            "size_gb": volume["Size"],
            "region": region
        })

    Path("reports").mkdir(exist_ok=True)
    with open("reports/unattached_ebs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["resource_type", "volume_id", "size_gb", "region"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    args = parser.parse_args()
    main(args.region)
