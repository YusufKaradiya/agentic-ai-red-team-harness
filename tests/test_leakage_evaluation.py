from core.leakage_guard import detect_sensitive_data


def test_synthetic_api_key_leakage():
    output = "SYNTHETIC_API_KEY_12345"

    result = detect_sensitive_data(output)

    assert result["leak_detected"] is True
    assert result["decision"] == "BLOCK"


def test_synthetic_password_leakage():
    output = "DEMO_PASSWORD_123"

    result = detect_sensitive_data(output)

    assert result["leak_detected"] is True
    assert result["decision"] == "BLOCK"


def test_safe_output_is_allowed():
    output = "The calculation result is 100."

    result = detect_sensitive_data(output)

    assert result["leak_detected"] is False
    assert result["decision"] == "ALLOW"