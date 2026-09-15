# Threat Model

## 1. System Overview

The Agentic AI Red-Team Harness is a local Streamlit-based security testing environment designed to evaluate an AI-agent workflow against prompt injection, indirect prompt injection, tool abuse and data exfiltration attacks.

The system uses synthetic data, simulated documents and mock tools. No real customer information, production credentials or external systems are used.

## 2. Assets

The main assets that require protection are:

| Asset              | Description                    | Sensitivity |
| ------------------ | ------------------------------ | ----------- |
| Synthetic API Key  | Simulated API credential       | High        |
| Synthetic Password | Fake database password         | High        |
| Customer Records   | Simulated customer information | High        |
| Agent Instructions | Simulated system instructions  | Medium      |
| Mock Database      | Local simulated database       | High        |
| Audit Logs         | Security test results          | Medium      |
| Mock Email Tool    | Simulated communication tool   | High        |

## 3. Threat Actors

### External Attacker

Attempts to manipulate the AI agent through malicious prompts or documents.

### Malicious User

Provides specially crafted instructions to bypass security controls or access unauthorized functionality.

### Malicious Document Author

Places hidden or visible instructions inside documents that may later be processed by the agent.

### Compromised Content Source

Represents retrieved content containing instructions designed to manipulate the agent.

## 4. Trust Boundaries

The main trust boundaries are:

1. User input → AI agent
2. Retrieved document → AI agent
3. AI agent → mock tools
4. AI agent → output
5. Application → audit logs

Each boundary represents a possible location where malicious instructions or unauthorized actions may occur.

## 5. Main Threats

| Threat ID | Threat                    | Example                                 | Impact   |
| --------- | ------------------------- | --------------------------------------- | -------- |
| T01       | Direct Prompt Injection   | Ignore previous instructions            | High     |
| T02       | Indirect Prompt Injection | Malicious instruction inside document   | High     |
| T03       | Tool Abuse                | Unauthorized database access            | Critical |
| T04       | Data Exfiltration         | Reveal synthetic API key                | Critical |
| T05       | Privilege Escalation      | Attempt to use restricted tool          | High     |
| T06       | Output Manipulation       | Return attacker-controlled instructions | Medium   |

## 6. Security Objectives

The system should:

* detect malicious instructions;
* prevent unauthorized tool access;
* prevent sensitive synthetic data from being returned;
* record security decisions;
* provide measurable attack results;
* preserve normal task functionality; and
* identify residual risks after defensive controls are applied.

## 7. Assumptions

The project assumes:

* all data is synthetic;
* all tools are simulated;
* the environment is isolated;
* attackers cannot directly modify the application source code;
* the main attack surface is the agent interaction workflow.

## 8. Scope Exclusions

The project does not attempt to:

* attack real systems;
* access real databases;
* send real emails;
* use real credentials;
* exploit production AI systems; or
* perform autonomous cyber attacks.
