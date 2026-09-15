# Defense Policy

## Objective

The defense layer converts detection results into
security decisions for the simulated AI agent.

## Risk-Based Decision Policy

Risk score 0–29:
ALLOW

Risk score 30–59:
BLOCK

Risk score 60–79:
BLOCK

Risk score 80–100:
BLOCK

## Security Controls

The current prototype uses:

1. Prompt injection detection
2. Tool abuse detection
3. Data exfiltration detection
4. Risk scoring
5. Security decision policy
6. Explainable security reasons

## Design Principle

The system follows a deny-by-default approach for
requests that exceed the defined risk threshold.

## Limitations

The current security policy is rule-based.

Attackers may bypass simple pattern matching using
obfuscated language, indirect instructions, or
previously unseen attack techniques.

The threshold values require empirical evaluation.

## Future Improvement

Future versions can evaluate multiple thresholds
and compare their effect on:

- Attack success rate
- False block rate
- Sensitive-data leakage
- Task utility
- Latency