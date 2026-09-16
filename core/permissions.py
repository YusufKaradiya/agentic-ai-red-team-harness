# Tool Permission Sandbox


# Tools that are available in the simulated agent
AVAILABLE_TOOLS = [
    "Calculator",
    "File Reader",
    "Customer Database",
    "Email Sender"
]


# Default permissions for the simulated agent
DEFAULT_PERMISSIONS = {
    "Calculator": True,
    "File Reader": True,
    "Customer Database": False,
    "Email Sender": False
}


def check_tool_permission(tool_name):
    """
    Check whether a tool is allowed to run.
    """

    if tool_name not in AVAILABLE_TOOLS:

        return {
            "allowed": False,
            "reason": "Unknown tool."
        }

    allowed = DEFAULT_PERMISSIONS.get(
        tool_name,
        False
    )

    if allowed:

        return {
            "allowed": True,
            "reason": (
                f"{tool_name} is authorized "
                "for this agent."
            )
        }

    return {
        "allowed": False,
        "reason": (
            f"{tool_name} is not authorized "
            "for this agent."
        )
    }