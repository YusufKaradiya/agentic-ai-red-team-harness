from core.leakage_guard import detect_sensitive_data


def test_normal_output_is_allowed():

    result = detect_sensitive_data(
        "The total order count is 250."
    )

    assert result["leak_detected"] is False
    assert result["decision"] == "ALLOW"


def test_api_key_is_blocked():

    result = detect_sensitive_data(
        "The API key is SYNTHETIC_API_KEY_12345"
    )

    assert result["leak_detected"] is True
    assert result["decision"] == "BLOCK"


def test_password_is_blocked():

    result = detect_sensitive_data(
        "Password: DEMO_PASSWORD_123"
    )

    assert result["leak_detected"] is True
    assert result["decision"] == "BLOCK"


def test_customer_email_is_blocked():

    result = detect_sensitive_data(
        "Email: customer1@example.test"
    )

    assert result["leak_detected"] is True
    assert result["decision"] == "BLOCK"