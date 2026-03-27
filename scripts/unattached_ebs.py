import argparse
import boto3
from common import write_csv

def main(region: str):
    ec2 = boto3.client("ec2", region_name=region)
    volumes = ec2.describe_volumes(
        Filters=[{"Name": "status", "Values": ["available"]}]
    )["Volumes"]

    rows = []
    for volume in volumes:
        rows.append({
            "resource_type": "ebs",
            "resource_id": volume["VolumeId"],
            "size_gb": volume["Size"],
            "region": region,
            "recommendation": "Validate and delete unattached volume if no longer required"
        })

    path = write_csv(
        "unattached_ebs.csv",
        rows,
        ["resource_type", "resource_id", "size_gb", "region", "recommendation"],
    )
    print(f"Wrote {len(rows)} rows to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    args = parser.parse_args()
    main(args.region)
