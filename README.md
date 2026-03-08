# AWS IAM Security Automation

Automates AWS IAM Security tasks using Python and boto3.

This project demonstrates how to automate IAM administration and perform basic security checks such as MFA validation, policy auditing, and activity monitoring.

# Architecture

Python Scripts → boto3 AWS SDK → AWS IAM/CloudTrail APIs → Security Audit Report (JSON)

# Features

- Create IAM users and assign them to security groups
- Attach AWS managed policies to groups
- Detect IAM users without Multi-Factor Authentication (MFA)
- Retrieve and analyze CloudTrail events
- Generate automated IAM security audit reports

# AWS Services Used

- AWS Identity and Access Management (IAM)
- AWS CloudTrail

# Technologies Used

- Python 3
- boto3 (AWS SDK for Python)
- AWS CLI
- JSON reporting

# Project Files

- create_user_roles.py - Creates IAM users and assigns them to predefined groups such as Admins, Developers, and Auditors
- enforce_mfa.py - Checks whether IAM users have MFA enabled and alerts if MFA is currently not in use
- parse_logs.py - Retrieves recent CloudTrail events and displays information about user activity and API calls
- security_audit.py - Performs a security audit on IAM users, checking MFA status and attached policies as well as generates audit_report.json

# Requirements To Test Scripts
- Python 3.x
- boto3
- AWS CLI configured with IAM permissions

# Install dependencies
- pip install boto3
- Configure AWS credentials
- aws configure


# Run the Scripts
Run each Python Script individually in PowerShell:

```PowerShell
python create_users_roles.py
python enforce_mfa.py
python parse_logs.py
python security_audit.py
```

# Project Goal

This project demonstrates cloud security automation by using Python to interact with AWS services. It highlights IAM management, MFA enforcement, activity monitoring, and automated auditing.







