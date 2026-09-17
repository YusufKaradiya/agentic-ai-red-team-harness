# Innovation Module

## Overview

The innovation component of the project is a lightweight
adversarial mutation and residual-risk testing workflow.

Instead of evaluating the detector only against known attack
examples, the system generates and evaluates variations of
attack payloads.

## Attack Mutation

Current mutation strategies include:

- Case variation
- Whitespace variation
- Newline variation
- Paraphrased attacks
- Simple obfuscation

## Purpose

The purpose is to identify weaknesses in a rule-based security
detector and provide measurable evidence of residual risk.

## Experimental Process

1. Select a synthetic attack.
2. Generate attack variations.
3. Execute variations against the detector.
4. Record ALLOW/BLOCK decisions.
5. Identify bypasses.
6. Calculate bypass rate.
7. Analyse mutation types.
8. Document residual risk.

## Reproducibility

The mutation corpus is stored as a CSV file and can be
re-evaluated using the same detector.

## Limitations

The mutation engine is intentionally lightweight.

It does not perform:

- LLM-based paraphrasing
- semantic attack generation
- automated jailbreak generation
- reinforcement learning
- adaptive attacker modelling

Future versions could introduce these techniques.