# AWS Cost Optimisation Platform

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-blue)
![Python](https://img.shields.io/badge/Language-Python-green)
![DevOps](https://img.shields.io/badge/Role-DevOps-informational)
![SRE](https://img.shields.io/badge/Focus-SRE-critical)

Engineering-driven approach to identifying, analysing, and reducing AWS infrastructure waste, with a focus on repeatable optimisation workflows and operational visibility.

---

## 🚀 Highlights
- $250k+ annual cost reduction (real-world experience)
- Automated AWS resource analysis using Boto3
- Actionable reporting for engineering decisions
- Designed for scalability and integration

---

## 📊 Architecture Diagram
(See diagram image in repo: `diagram.png`)

---

## ⚙️ Example Usage

```bash
python scripts/idle_ec2.py --region eu-west-2
python scripts/unattached_ebs.py --region eu-west-2
python scripts/old_snapshots.py --region eu-west-2 --days 30
python scripts/report_merge.py
```

---

## 💡 Engineering Thinking

Cost optimisation is not just deletion:
- Validate against business needs
- Avoid breaking DR or compliance systems
- Balance performance vs cost

---
