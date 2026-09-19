# Model / Detection Card

## System Type

This project does not use a trained machine-learning model as its
primary detector.

The current security detector is a deterministic rule-based
component.

## Detection Approach

The detector uses:

- Text normalization
- Pattern matching
- Attack-category rules
- Risk scoring
- Decision thresholds

## Input

User prompts and simulated external document content.

## Output

- Attack category
- Risk score
- Severity
- Detection reasons
- Allow/Block decision

## Advantages

- Deterministic
- Reproducible
- Easy to inspect
- Easy to test
- Low computational overhead

## Limitations

- Exact or near-exact pattern dependency
- Limited semantic understanding
- Vulnerable to unseen paraphrases
- Possible false positives
- Limited coverage of real-world attacks

## Future Improvement

Potential future research could investigate semantic classifiers,
embedding-based detection or hybrid rule + ML approaches.