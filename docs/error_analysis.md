# Error Analysis

## Objective

The purpose of error analysis is to identify cases where the
security system produced an incorrect decision.

## False Positives

A false positive occurs when a benign request is incorrectly
blocked by the security controls.

For each false positive, record:

- Attack/Test ID
- Payload
- Expected decision
- Actual decision
- Detected category
- Risk score
- Reason for incorrect classification

## False Negatives

A false negative occurs when a malicious request is incorrectly
allowed.

For each false negative, record:

- Attack/Test ID
- Payload
- Expected decision
- Actual decision
- Detected category
- Risk score
- Reason for missed detection

## Root Cause Analysis

Potential causes include:

- Exact keyword dependency
- Paraphrased attacks
- Obfuscated text
- Unseen attack patterns
- Ambiguous benign language
- Multiple attack categories in one request

## Mitigation Ideas

Potential improvements include:

- Larger attack corpus
- Semantic similarity detection
- Context-aware analysis
- Better tool authorization policies
- Improved output validation
- Human approval for high-risk actions

## Limitations

The current detector is lightweight and primarily rule-based.
Therefore, unseen semantic variations may not always be detected.