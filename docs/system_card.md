# System Card

## System Name

Agentic AI Red-Team Harness

## Purpose

A security evaluation prototype designed to test prompt injection,
tool abuse and synthetic sensitive-data leakage in a simulated
tool-enabled AI agent.

## Intended Use

- Security experimentation
- Red-team testing
- Academic research
- Demonstration of layered AI-agent defenses

## Out of Scope

- Production security gateway
- Real customer data
- Real credentials
- Real email delivery
- Production database access

## Security Controls

- Input attack detection
- Risk scoring
- Prompt injection defense
- Indirect injection detection
- Tool authorization
- Output leakage detection
- Audit logging

## Evaluation

The system is evaluated using a synthetic attack corpus,
mutation tests and baseline comparison.

## Limitations

The detection system is primarily rule-based.

It may fail against previously unseen semantic attacks or
sophisticated obfuscation.

## Data

Only synthetic data is used.

## Human Oversight

High-risk actions are blocked rather than automatically
executed against real external systems.

## Deployment

The application can be run locally or inside Docker.

## Security Considerations

The system itself should be treated as a prototype and should
not be connected to real credentials or production services
without additional security controls.