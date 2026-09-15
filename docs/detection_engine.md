# Detection Engine

## Purpose

The detection engine identifies suspicious user inputs
before they reach the simulated AI agent or tools.

## Detection Approach

A lightweight rule-based detection approach is used.

The detector normalizes input text and searches for
known suspicious patterns.

## Detection Categories

1. Prompt Injection
2. Tool Abuse
3. Data Exfiltration
4. Benign Requests

## Risk Scoring

Prompt Injection = +40
Tool Abuse = +30
Data Exfiltration = +40

Maximum score = 100

## Decision Policy

Score < 30:
ALLOW

Score >= 30:
BLOCK

## Severity

0-29   = LOW
30-59  = MEDIUM
60-79  = HIGH
80-100 = CRITICAL

## Limitations

The current detector is rule-based and may fail against
new or obfuscated attacks.

It may also produce false positives when legitimate
users use suspicious-looking language.

Future versions could use ML or LLM-based detection.