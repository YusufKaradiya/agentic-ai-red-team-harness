# Audit Logging

## Objective

The audit logging module records security-relevant events generated
by the Agentic AI Red-Team Harness.

The purpose is to provide operational evidence of detection,
blocking, tool authorization and sensitive-data leakage events.

## Logged Events

Each security event contains:

- Event ID
- Timestamp
- Source
- Attack ID
- Category
- Risk score
- Severity
- Decision
- Tool
- Tool permission
- Leakage detection status
- Detection reasons
- Security action
- Test payload

## Storage

SQLite is used as the local event store.

Database location:

logs/security_events.db

The database is intentionally excluded from Git because it is
runtime-generated data.

## Event Sources

Current event sources include:

1. Attack Simulator
2. Indirect Injection Scanner
3. Tool Sandbox
4. Output Guard

## Security Value

Audit logs provide evidence of:

- Attack detection
- Request blocking
- Tool authorization decisions
- Sensitive-data leakage detection
- Security policy enforcement

## Synthetic Data Policy

The prototype uses synthetic test data only.

No real:

- passwords
- API keys
- customer records
- email accounts
- production databases

are used.

## Limitations

The current logging implementation is designed for a local prototype.

It does not yet provide:

- distributed logging
- log integrity protection
- centralized SIEM integration
- advanced trace correlation
- cryptographic log signing
- production access control

These can be considered future improvements.