from core.tool_runner import run_tool


def test_allowed_calculator_runs():

    result = run_tool(
        "Calculator",
        a=5,
        b=5,
        operation="add"
    )

    assert result["success"] is True
    assert result["blocked"] is False
    assert result["result"] == 10


def test_unauthorized_database_is_blocked():

    result = run_tool(
        "Customer Database"
    )

    assert result["success"] is False
    assert result["blocked"] is True


def test_unauthorized_email_is_blocked():

    result = run_tool(
        "Email Sender",
        to="test@example.test",
        subject="Test",
        message="Hello"
    )

    assert result["success"] is False
    assert result["blocked"] is True