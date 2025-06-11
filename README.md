# Closed-Loop Cellsite Energy Saving Platform (OpenRAN-based)

A scalable, secure, cloud-native platform for 5G/4G cellsite energy saving automation, supporting 5000+ gNodeBs, 15000+ cells, and adhering to OpenRAN Alliance guidelines.

## System Architecture
- **AWS EMR**: Distributed Spark processing
- **S3 Feature Store**: Scalable, versioned storage
- **MLflow**: Experiment/model registry
- **Auto-scaling**: EMR + serverless pipeline
- **Security**: Encryption, IAM, network hardening, audit logs

## Closed-loop Workflow
1. **Collect**: Real-time network, biometric, device, and context data
2. **Engineer**: Compute advanced features (Spark)
3. **Predict**: ML ensemble (Isolation Forest + Random Forest)
4. **Act**: Automated cell sleep/wake, parameter adjust
5. **Monitor**: Model, infra, security, anomaly detection

## Security Highlights
- End-to-end encryption (TLS, S3 SSE)
- AWS IAM least-privilege
- AWS Secrets Manager for credentials
- Network security groups, VPC, audit logging

## Prerequisites
- Python 3.7+
- AWS account (EMR, S3, IAM, VPC permissions)
- Docker (optional)
- Git

## Usage
See `infrastructure/` for AWS setup, then run pipeline and controller as in `README.md`.