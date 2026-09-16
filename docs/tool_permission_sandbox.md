# Tool Permission Sandbox

## Objective

The Tool Permission Sandbox prevents the simulated
AI agent from executing unauthorized tools.

## Available Tools

1. Calculator
2. File Reader
3. Customer Database
4. Email Sender

## Default Permissions

Calculator:
ALLOWED

File Reader:
ALLOWED

Customer Database:
BLOCKED

Email Sender:
BLOCKED

## Security Principle

Tool access is explicitly authorized.

The agent cannot execute a tool merely because
a user or attacker requests it.

## Tool Execution Flow

User Request
    ↓
Detection
    ↓
Defense
    ↓
Tool Permission Check
    ↓
Permission Granted?
    ↓
Yes → Execute Tool
No  → Block Tool

## Safety

All tools are simulated.

No real customer database is connected.

No real email is sent.

No production credentials are used.

## Security Benefit

The sandbox provides a second security boundary
even if malicious instructions pass through the
input detection layer.

## Limitations

The current prototype uses static permissions.

A production system would require more detailed
authorization policies, identity-aware access
control, logging and continuous monitoring.