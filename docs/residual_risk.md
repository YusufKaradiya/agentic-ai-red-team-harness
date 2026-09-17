# Residual Risk Analysis

## Definition

Residual risk represents malicious behaviour that remains
possible after the current security controls are applied.

## Measurement

For adversarial testing, residual bypass rate is calculated as:

Bypass Rate =

Malicious Cases Allowed by Detector
----------------------------------- × 100
Total Malicious Mutation Cases

## Bypass

A bypass occurs when:

Expected = BLOCK

but

Actual = ALLOW

## False Positive

A false positive occurs when:

Expected = ALLOW

but

Actual = BLOCK

## Current Sources of Residual Risk

Potential residual risks include:

1. Paraphrased attacks
2. Obfuscated text
3. Previously unseen attack patterns
4. Context-dependent malicious instructions
5. Multi-step attacks
6. Semantic attacks not represented by simple keyword rules

## Interpretation

Residual-risk measurements apply only to the tested synthetic
mutation corpus.

They should not be interpreted as a universal estimate of
real-world attack success.

## Mitigation Opportunities

Potential future improvements include:

- semantic detection
- ML-based classifiers
- LLM-based security analysis
- ensemble detection
- contextual policy checks
- adaptive red-team generation
- stronger tool authorization policies