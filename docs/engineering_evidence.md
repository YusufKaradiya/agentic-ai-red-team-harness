# Engineering Evidence

## Objective

Day 13 focused on engineering hardening, reproducibility,
automated validation and deployment readiness.

## Automated Testing

The project uses Pytest for automated validation of:

- Prompt injection detection
- Defense decisions
- Indirect injection detection
- Tool permissions
- Tool execution
- Sensitive-data detection
- Audit logging
- Evaluation metrics
- Baseline behavior
- Mutation testing
- Security regression cases

## Security Regression Testing

Security regression tests ensure that previously implemented
security controls continue to operate after code modifications.

Examples include:

- Prompt injection remains blocked
- Restricted tools remain denied
- Synthetic secrets remain detectable
- Benign requests remain allowed

## Docker

The application can be packaged and executed using Docker.

Docker provides a reproducible runtime environment and reduces
differences between development and demonstration environments.

## Continuous Integration

GitHub Actions automatically performs:

1. Dependency installation
2. Pytest execution
3. Health checks
4. Dependency security auditing

## Dependency Security

pip-audit is used to identify known vulnerabilities in installed
Python dependencies.

## Health Check

A lightweight health check validates critical security components:

- Injection blocking
- Tool permission enforcement
- Sensitive-data detection

## Data Safety

The application uses synthetic data only.

No real credentials, customer information, external database or
real email service is connected.

## Limitations

- Security detection is primarily rule-based.
- Dependency scanning identifies known package vulnerabilities,
  not all application-level security flaws.
- Docker improves reproducibility but does not automatically make
  the application production secure.
- CI validates selected automated checks and does not replace
  comprehensive security testing.