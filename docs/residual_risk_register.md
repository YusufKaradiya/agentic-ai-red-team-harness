# Residual Risk Register

| Risk ID | Risk | Existing Control | Residual Risk | Mitigation |
|---|---|---|---|---|
| R01 | Unseen prompt injection | Rule-based detector | Medium | Expand attack corpus |
| R02 | Paraphrased attack | Mutation testing | Medium | Semantic detection |
| R03 | Tool misuse | Permission sandbox | Low/Medium | Fine-grained authorization |
| R04 | Sensitive output | Leakage guard | Medium | Context-aware output filtering |
| R05 | False positives | Rule-based detection | Medium | Improve benign corpus |
| R06 | Unknown attack technique | Existing test corpus | High | Continuous red-team testing |

## Interpretation

The residual-risk analysis identifies security gaps that remain
after the current controls are applied.

The values in this register should be updated based on experimental
evidence rather than assumed to represent production risk.