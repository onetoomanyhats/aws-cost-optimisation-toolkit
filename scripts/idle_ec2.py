import argparse
import boto3
from common import write_csv

def main(region: str):
    ec2 = boto3.client("ec2", region_name=region)
    reservations = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running", "stopped"]}]
    )["Reservations"]

    rows = []
    for reservation in reservations:
        for instance in reservation["Instances"]:
            rows.append({
                "resource_type": "ec2",
                "resource_id": instance["InstanceId"],
                "state": instance["State"]["Name"],
                "instance_type": instance["InstanceType"],
                "region": region,
                "recommendation": "Review for stop, terminate, or rightsize"
            })

    path = write_csv(
        "idle_ec2.csv",
        rows,
        ["resource_type", "resource_id", "state", "instance_type", "region", "recommendation"],
    )
    print(f"Wrote {len(rows)} rows to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    args = parser.parse_args()
    main(args.region)
