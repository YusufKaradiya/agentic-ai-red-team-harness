# Research Evaluation

## Research Question

How effectively can a lightweight layered defense approach reduce
prompt injection, tool abuse and synthetic sensitive-data leakage
in a simulated tool-enabled AI agent while maintaining normal task
utility?

## RQ1 — Known Attack Detection

The attack corpus contains direct prompt injection, indirect
prompt injection, tool abuse, data exfiltration and benign cases.

Detection performance is evaluated using:

- Detection Rate
- Attack Success Rate
- False Positive Rate
- False Negative Rate

## RQ2 — Baseline Comparison

The proposed architecture is compared against an unprotected
baseline.

### Baseline

User Request → Mock Agent → Tool

### Proposed

User Request
→ Input Defense
→ Risk Detection
→ Permission Sandbox
→ Tool
→ Output Guard
→ Audit Logging

The same test corpus is used for both systems.

## RQ3 — Mutation Testing

The mutation engine generates paraphrased and obfuscated variations
of attack payloads.

The primary metric is:

Mutation Bypass Rate

## RQ4 — Task Utility

Benign requests are evaluated to determine whether security
controls unnecessarily block normal operations.

For this prototype, correctly allowed benign requests are used as
a lightweight proxy for task utility.

## Experimental Procedure

1. Load attack corpus.
2. Execute proposed defense.
3. Execute baseline.
4. Record decisions.
5. Calculate metrics.
6. Execute mutation tests.
7. Evaluate residual risk.
8. Analyze false positives and false negatives.
9. Repeat tests to verify reproducibility.

## Reproducibility

The experiment uses a fixed synthetic corpus and deterministic
rule-based controls.

This allows the experiment to be repeated under the same software
environment.

## Limitations

The prototype does not represent a production AI agent.

The attack corpus is limited in size and diversity.

The detector is primarily rule-based.

Task utility is approximated using benign-case preservation.

Real-world user behavior and adversarial adaptation are not fully
represented.