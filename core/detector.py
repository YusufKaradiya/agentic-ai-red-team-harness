import re

# Suspicious phrases related to prompt injection
INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "ignore the previous prompt",
    "forget previous instructions",
    "override system instructions",
    "bypass security",
    "reveal the system prompt",
    "show the system prompt",
    "reveal hidden instructions",
    "do not follow the rules",
    "pretend you are administrator",
]


# Suspicious phrases related to tool abuse
TOOL_ABUSE_PATTERNS = [
    "use the customer database",
    "access the customer database",
    "read all customer records",
    "export customer data",
    "send the data",
    "send all records",
    "delete the database",
    "delete all records",
    "access restricted file",
]


# Suspicious phrases related to data exfiltration
EXFILTRATION_PATTERNS = [
    "show me the api key",
    "show me the synthetic api key",
    "reveal the api key",
    "show the password",
    "reveal the password",
    "show confidential data",
    "reveal confidential data",
    "give me all customer records",
    "return all customer records",
    "print the secret",
    "show the secret",
]


def normalize_text(text):
    """
    Normalize user input before detection.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def find_matches(text, patterns):
    """
    Return suspicious patterns found in the text.
    """
    matches = []

    for pattern in patterns:
        if pattern in text:
            matches.append(pattern)

    return matches


def calculate_severity(score):
    """
    Convert numerical risk score into severity.
    """

    if score >= 80:
        return "CRITICAL"

    if score >= 60:
        return "HIGH"

    if score >= 30:
        return "MEDIUM"

    return "LOW"


def detect_attack(payload):
    """
    Main detection function.

    Returns:
        attack status
        category
        risk score
        severity
        reasons
        decision
    """

    text = normalize_text(payload)

    injection_matches = find_matches(
        text,
        INJECTION_PATTERNS
    )

    tool_matches = find_matches(
        text,
        TOOL_ABUSE_PATTERNS
    )

    exfiltration_matches = find_matches(
        text,
        EXFILTRATION_PATTERNS
    )

    score = 0
    reasons = []
    categories = []

    # Prompt injection detection
    if injection_matches:
        score += 40
        categories.append("Prompt Injection")
        reasons.append(
            "Suspicious prompt-injection instruction detected."
        )

    # Tool abuse detection
    if tool_matches:
        score += 30
        categories.append("Tool Abuse")
        reasons.append(
            "Potential unauthorized tool activity detected."
        )

    # Data exfiltration detection
    if exfiltration_matches:
        score += 40
        categories.append("Data Exfiltration")
        reasons.append(
            "Potential sensitive-data access or disclosure detected."
        )

    # Cap score at 100
    score = min(score, 100)

    # Determine final category
    if categories:
        category = ", ".join(categories)
    else:
        category = "Benign"

    severity = calculate_severity(score)

    # Final decision
    if score >= 30:
        decision = "BLOCK"
        is_attack = True
    else:
        decision = "ALLOW"
        is_attack = False

    return {
        "is_attack": is_attack,
        "category": category,
        "risk_score": score,
        "severity": severity,
        "reasons": reasons,
        "decision": decision,
        "injection_matches": injection_matches,
        "tool_matches": tool_matches,
        "exfiltration_matches": exfiltration_matches,
    }

def detect_indirect_injection(document_text):
    """
    Detect malicious instructions hidden inside documents.
    """

    result = detect_attack(document_text)

    if result["is_attack"]:

        result["category"] = (
            "Indirect Prompt Injection"
        )

        result["reasons"].append(
            "Suspicious instructions detected inside "
            "external document content."
        )

    return result