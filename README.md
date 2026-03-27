# AWS Cost Optimisation Toolkit

A practical toolkit for identifying common sources of AWS waste and surfacing quick-win optimisation opportunities. This repository is intended to make cloud cost management tangible through lightweight scripts, simple reporting, and operational recommendations.

## What it checks

- Idle EC2 instances
- Unattached EBS volumes
- Underutilised instances
- Idle load balancers
- Old snapshots

## Why this repository matters

Cloud cost optimisation is not only a finance exercise; it is part of resilient platform engineering. Removing waste improves:

- Spend efficiency
- Operational discipline
- Infrastructure visibility
- Long-term scalability

## Repository structure

```text
.
├── reports/
├── requirements.txt
├── scripts/
│   ├── idle_ec2.py
│   ├── unattached_ebs.py
│   ├── old_snapshots.py
│   └── report_merge.py
└── sample-output/
    └── optimisation-report.csv
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure AWS credentials via environment variables, AWS CLI profile, or instance role.

## Usage

```bash
python3 scripts/idle_ec2.py --region eu-west-2
python3 scripts/unattached_ebs.py --region eu-west-2
python3 scripts/old_snapshots.py --region eu-west-2 --days 30
python3 scripts/report_merge.py
```

## Engineering approach

The scripts are intentionally:

- Small and readable
- Easy to extend
- Suitable for scheduling
- Friendly for integration into CI/CD or operational cron workflows

## Potential next steps

- Add rightsizing recommendations via CloudWatch metrics
- Add pricing estimates using Cost Explorer
- Add Slack or email notifications
- Add multi-account support through AWS Organizations

## Disclaimer

Always validate recommendations against business, compliance, and availability requirements before deleting or modifying resources.
