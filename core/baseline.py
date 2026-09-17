import time


def simulate_baseline_tool(payload, tool):
    """
    Simulate what the baseline agent would do
    when a tool is requested.

    No authorization check is performed.
    """

    if tool is None or str(tool).lower() == "none":
        return {
            "tool_executed": False,
            "result": "Mock agent response generated."
        }

    return {
        "tool_executed": True,
        "result": f"Mock {tool} executed without security controls."
    }


def run_baseline(payload, tool=None):
    """
    Run the unprotected baseline system.

    No:
    - injection detector
    - risk scoring
    - permission sandbox
    - output guard
    """

    start_time = time.perf_counter()

    tool_result = simulate_baseline_tool(
        payload,
        tool
    )

    end_time = time.perf_counter()

    latency_ms = (
        end_time - start_time
    ) * 1000

    return {
        "decision": "ALLOW",
        "risk_score": 0,
        "tool_executed": tool_result["tool_executed"],
        "output_blocked": False,
        "leak_detected": False,
        "latency_ms": latency_ms,
        "result": tool_result["result"]
    }