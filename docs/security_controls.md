# Security Controls

## Control 1 — Input Validation

User prompts will be inspected for suspicious instructions and known injection patterns before being passed to the agent.

## Control 2 — Threat Detection

Each request will be classified into an attack category such as direct injection, indirect injection, tool abuse or data exfiltration.

## Control 3 — Risk Scoring

A numerical risk score will be calculated based on detected threats.

## Control 4 — Tool Permission Sandbox

Each mock tool will have an explicit permission policy.

For example:

| Tool              | Agent Permission |
| ----------------- | ---------------- |
| Calculator        | Allowed          |
| File Reader       | Allowed          |
| Customer Database | Restricted       |
| Email Sender      | Restricted       |

## Control 5 — Sensitive Data Detection

Agent outputs will be checked for synthetic secrets and sensitive information.

## Control 6 — Output Blocking

If sensitive information is detected, the output will be blocked or replaced with a safe response.

## Control 7 — Audit Logging

Security events will record:

* timestamp;
* attack category;
* risk score;
* decision;
* requested tool;
* permission result;
* leakage result; and
* response latency.

## Control 8 — Residual Risk Reporting

The system will identify attacks that remain successful after defensive controls are applied.
