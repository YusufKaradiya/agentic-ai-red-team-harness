# Sensitive Data Output Guard

## Objective

The Output Guard prevents sensitive information from
being returned to the user through AI or tool outputs.

## Protected Data

The prototype uses synthetic:

- API keys
- Passwords
- Secret tokens
- Customer email addresses
- Confidential-data indicators

## Detection

The system scans output using pattern matching.

## Decision

If sensitive information is detected:

BLOCK

Otherwise:

ALLOW

## Security Flow

AI / Tool Output
      ↓
Output Guard
      ↓
Sensitive Data?
   /        \
 YES        NO
  ↓          ↓
BLOCK       ALLOW

## Safety

All secrets and customer information are synthetic.

No production credentials or real customer records
are used.

## Limitations

The current implementation uses pattern matching.

It may fail to detect:

- Encoded secrets
- Obfuscated secrets
- Previously unseen sensitive formats
- Semantically sensitive information

## Future Work

Future versions can evaluate ML or LLM-based
sensitive-data detection.