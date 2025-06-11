# Security Hardening Checklist

- All data encrypted in transit (TLS 1.2+) and at rest (S3 SSE, EBS encryption)
- IAM policies: Least-privilege, role separation, no root credentials
- All secrets (DB, API keys) in AWS Secrets Manager
- EMR, S3 in private subnets (VPC), with Security Groups limiting traffic
- Audit logging: CloudTrail for API, S3, EMR actions
- Network ACLs, firewall rules for EMR, EC2, S3 endpoints
- Docker containers: Use non-root, minimal base images
- MLflow: Authenticated, HTTPS, access logging
- Regular security patching, vulnerability scans