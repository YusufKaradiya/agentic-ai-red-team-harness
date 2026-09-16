from core.permissions import check_tool_permission
from core.leakage_guard import detect_sensitive_data

from tools.calculator import calculate
from tools.file_reader import read_file
from tools.customer_database import get_customers
from tools.email_sender import send_email


def protect_output(result):
    """
    Run tool output through the leakage guard.
    """

    output_text = str(result)

    leakage = detect_sensitive_data(
        output_text
    )

    if leakage["leak_detected"]:

        return {
            "success": False,
            "blocked": True,
            "output_blocked": True,
            "message": (
                "Tool output blocked because "
                "sensitive data was detected."
            ),
            "findings": leakage["findings"]
        }

    return {
        "success": True,
        "blocked": False,
        "output_blocked": False,
        "result": result
    }


def run_tool(tool_name, **kwargs):
    """
    Execute an authorized tool and protect
    its output.
    """

    permission = check_tool_permission(
        tool_name
    )

    # -----------------------------------------------------
    # Permission check
    # -----------------------------------------------------

    if not permission["allowed"]:

        return {
            "success": False,
            "blocked": True,
            "output_blocked": False,
            "message": permission["reason"]
        }

    # -----------------------------------------------------
    # Calculator
    # -----------------------------------------------------

    if tool_name == "Calculator":

        result = calculate(
            kwargs.get("a", 0),
            kwargs.get("b", 0),
            kwargs.get("operation", "add")
        )

        return protect_output(result)

    # -----------------------------------------------------
    # File Reader
    # -----------------------------------------------------

    if tool_name == "File Reader":

        result = read_file(
            kwargs.get("filename", "")
        )

        return protect_output(result)

    # -----------------------------------------------------
    # Customer Database
    # -----------------------------------------------------

    if tool_name == "Customer Database":

        result = get_customers()

        return protect_output(result)

    # -----------------------------------------------------
    # Email Sender
    # -----------------------------------------------------

    if tool_name == "Email Sender":

        result = send_email(
            kwargs.get("to", ""),
            kwargs.get("subject", ""),
            kwargs.get("message", "")
        )

        return protect_output(result)

    # -----------------------------------------------------
    # Unknown tool
    # -----------------------------------------------------

    return {
        "success": False,
        "blocked": True,
        "output_blocked": False,
        "message": "Unknown tool."
    }