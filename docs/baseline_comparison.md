# Baseline vs Proposed System

## Objective

The purpose of this experiment is to compare an unprotected
tool-enabled agent with the proposed layered security architecture.

## Baseline

The baseline represents a minimal agent without:

- Prompt injection detection
- Risk scoring
- Security blocking
- Tool permission enforcement
- Output leakage protection

It is implemented only as a controlled research reference.

## Proposed System

The proposed architecture includes:

- Input normalization
- Prompt injection detection
- Tool abuse detection
- Data exfiltration detection
- Risk scoring
- Security decision policy
- Tool permission sandbox
- Output leakage guard

## Experimental Design

Both systems receive the same synthetic attack corpus.

The corpus contains:

- Direct prompt injection
- Indirect prompt injection
- Tool abuse
- Data exfiltration
- Benign control cases

The same test cases are used for both systems.

## Metrics

The comparison measures:

- Detection rate
- Attack success rate
- False positive rate
- False positives
- False negatives
- Average latency

## Attack Success Rate

Attack success rate is defined as:

False Negatives / Total Malicious Cases × 100

A false negative occurs when a malicious test case is incorrectly
allowed by the system.

## False Positive Rate

False positive rate is defined as:

False Positives / Total Benign Cases × 100

## Reproducibility

The experiment is generated programmatically from the same
attack corpus and can be repeated from the Streamlit interface.

## Limitations

The experiment uses synthetic attacks and a lightweight
rule-based detector.

The results therefore do not represent performance against
all real-world AI agents or attack distributions.

The baseline is intentionally simplified and should not be
interpreted as a model of every production AI system.

## Next Experiment

A further experiment will test unseen and obfuscated attacks
to measure residual risk and identify detector bypasses.