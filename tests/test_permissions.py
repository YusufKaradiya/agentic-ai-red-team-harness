from core.permissions import check_tool_permission


def test_calculator_is_allowed():

    result = check_tool_permission(
        "Calculator"
    )

    assert result["allowed"] is True


def test_file_reader_is_allowed():

    result = check_tool_permission(
        "File Reader"
    )

    assert result["allowed"] is True


def test_customer_database_is_blocked():

    result = check_tool_permission(
        "Customer Database"
    )

    assert result["allowed"] is False


def test_email_sender_is_blocked():

    result = check_tool_permission(
        "Email Sender"
    )

    assert result["allowed"] is False


def test_unknown_tool_is_blocked():

    result = check_tool_permission(
        "Unknown Tool"
    )

    assert result["allowed"] is False