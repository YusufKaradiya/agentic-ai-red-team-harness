from core.detector import detect_attack


def apply_defense(payload):
    """
    Run detection and apply the security policy.
    """

    detection = detect_attack(payload)

    risk_score = detection["risk_score"]
    category = detection["category"]
    severity = detection["severity"]

    # Security policy
    if risk_score >= 60:
        decision = "BLOCK"

        action = (
            "Request blocked because the risk level "
            "is high or critical."
        )

    elif risk_score >= 30:
        decision = "BLOCK"

        action = (
            "Request blocked because suspicious "
            "behavior was detected."
        )

    else:
        decision = "ALLOW"

        action = (
            "Request allowed because no significant "
            "security risk was detected."
        )

    return {
        "decision": decision,
        "risk_score": risk_score,
        "severity": severity,
        "category": category,
        "reasons": detection["reasons"],
        "action": action,
    }