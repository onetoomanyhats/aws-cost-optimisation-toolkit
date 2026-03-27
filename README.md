# AWS Cost Optimisation Platform

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-blue)
![Python](https://img.shields.io/badge/Language-Python-green)
![DevOps](https://img.shields.io/badge/Role-DevOps-informational)
![SRE](https://img.shields.io/badge/Focus-SRE-critical)

Engineering-driven approach to identifying, analysing, and reducing AWS infrastructure waste, with a focus on repeatable optimisation workflows and operational visibility.
This project is inspired by real-world experience delivering $250k+ annual savings across production environments.

---

## 🚀 Highlights
- Cost optimisation as a DevOps/SRE responsibility
- Practical AWS resource analysis using Boto3
- Repeatable optimisation workflows
- Translating infrastructure waste into actionable engineering decisions
- Bridging technical metrics → business impact

---

## 📊 Architecture Overview
(See diagram image in repo: `diagram.png`)

---

📊 Core Capabilities

1. Compute Optimisation
- Identify idle or underutilised EC2 instances
- Highlight right-sizing opportunities
- Detect stopped or orphaned instances
2. Storage Optimisation
- Detect unattached EBS volumes
- Identify old snapshots beyond retention thresholds
- Highlight storage waste patterns
3. Reporting Engine
- Consolidates findings into actionable CSV reports
- Designed for integration into:
  monthly reviews, 
  cost governance workflows, 
  automation pipelines

---

## ⚙️ Example Usage

```bash
python scripts/idle_ec2.py --region eu-west-2
python scripts/unattached_ebs.py --region eu-west-2
python scripts/old_snapshots.py --region eu-west-2 --days 30
python scripts/report_merge.py
```
---



## ⚙️ Example Output
| Resource Type | ID       | Issue              | Recommendation    |
| ------------- | -------- | ------------------ | ----------------- |
| EC2           | i-xxx    | Running but idle   | Stop or downsize  |
| EBS           | vol-xxx  | Unattached         | Delete            |
| Snapshot      | snap-xxx | Older than 30 days | Archive or remove |


---

## 💡 Engineering Thinking

Cost optimisation is not just deletion:
- Validate against business needs
- Avoid breaking DR or compliance systems
- Balance performance vs cost

---
