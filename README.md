# Agentic AI Red-Team Harness for Prompt Injection, Tool Abuse and Data Exfiltration

## Problem Statement

Modern AI assistants are increasingly connected to tools, documents, databases and external information sources. This creates security risks because malicious instructions can be inserted directly into user prompts or indirectly into documents and retrieved content.

An attacker may attempt to manipulate an AI agent into ignoring its intended instructions, accessing unauthorized tools, or exposing sensitive information.

This project proposes a lightweight and safe red-team testing harness that simulates these attacks in an isolated environment using synthetic data and mock tools.

The system will allow developers and security reviewers to:

* run direct prompt-injection attacks;
* test indirect prompt injection through simulated documents;
* simulate unauthorized tool usage;
* detect synthetic sensitive-data leakage;
* apply lightweight defensive controls;
* record security decisions and events;
* compare an unprotected baseline with the protected system; and
* generate measurable security and residual-risk reports.

The project will not interact with real customer data, production systems, real credentials, or real external attack targets.

## Objectives

1. Build a working Streamlit-based red-team harness for AI-agent security testing.

2. Create a synthetic attack corpus covering:

   * direct prompt injection;
   * indirect prompt injection;
   * tool abuse; and
   * data exfiltration.

3. Implement lightweight layered defenses for malicious inputs, unauthorized tools and sensitive outputs.

4. Build a mock tool environment containing safe simulated tools such as a calculator, file reader, database and email sender.

5. Implement an audit trail that records attack type, decision, risk score, tool access and leakage events.

6. Develop a scorecard using attack success rate, false-block rate, data leakage rate, task utility, latency and reproducibility.

7. Compare an unprotected baseline agent with the proposed defended workflow.

8. Produce a residual-risk report showing which threats remain after applying the defensive controls.
