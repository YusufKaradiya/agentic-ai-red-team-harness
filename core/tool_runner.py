from core.permissions import check_tool_permission

from tools.calculator import calculate
from tools.file_reader import read_file
from tools.customer_database import get_customers
from tools.email_sender import send_email


def run_tool(tool_name, **kwargs):
    """
    Execute a tool only if permission is granted.
    """

    permission = check_tool_permission(
        tool_name
    )

    if not permission["allowed"]:

        return {
            "success": False,
            "blocked": True,
            "message": permission["reason"]
        }

    if tool_name == "Calculator":

        result = calculate(
            kwargs.get("a", 0),
            kwargs.get("b", 0),
            kwargs.get("operation", "add")
        )

        return {
            "success": True,
            "blocked": False,
            "result": result
        }

    if tool_name == "File Reader":

        result = read_file(
            kwargs.get("filename", "")
        )

        return {
            "success": True,
            "blocked": False,
            "result": result
        }

    if tool_name == "Customer Database":

        result = get_customers()

        return {
            "success": True,
            "blocked": False,
            "result": result
        }

    if tool_name == "Email Sender":

        result = send_email(
            kwargs.get("to", ""),
            kwargs.get("subject", ""),
            kwargs.get("message", "")
        )

        return {
            "success": True,
            "blocked": False,
            "result": result
        }

    return {
        "success": False,
        "blocked": True,
        "message": "Unknown tool."
    }