import argparse
import csv
from pathlib import Path
import boto3

def main(region: str):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running", "stopped"]}]
    )
    rows = []
    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            rows.append({
                "resource_type": "ec2",
                "instance_id": instance["InstanceId"],
                "state": instance["State"]["Name"],
                "instance_type": instance["InstanceType"],
                "region": region
            })

    Path("reports").mkdir(exist_ok=True)
    with open("reports/idle_ec2.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["resource_type", "instance_id", "state", "instance_type", "region"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    args = parser.parse_args()
    main(args.region)
