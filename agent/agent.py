import re

from agent.state import AgentState
from agent.planner import plan_tool

from core.defense import apply_defense
from core.tool_runner import run_tool
from core.leakage_guard import detect_sensitive_data


class AgentSimulator:

    def __init__(self):
        self.name = "Red-Team Test Agent"

    def extract_numbers(self, text):
        numbers = re.findall(r"\d+(?:\.\d+)?", text)
        return [float(number) for number in numbers]

    def determine_operation(self, text):
        text = text.lower()

        if "multiply" in text:
            return "multiply"

        if "divide" in text:
            return "divide"

        if "subtract" in text:
            return "subtract"

        if "add" in text:
            return "add"

        return "add"

    def run(self, user_input):
        state = AgentState(user_input=user_input)

        state.add_event("Request received.")

        # ---------------------------------
        # STEP 1: INPUT DEFENSE
        # ---------------------------------

        defense = apply_defense(user_input)

        state.decision = defense["decision"]
        state.risk_score = defense["risk_score"]
        state.category = defense["category"]

        state.add_event(
            f"Security decision: {state.decision}"
        )

        # ---------------------------------
        # STEP 2: BLOCK IF MALICIOUS
        # ---------------------------------

        if state.decision == "BLOCK":

            state.final_response = (
                "Request blocked by security policy."
            )

            state.add_event(
                "Request stopped before tool execution."
            )

            return self.format_result(state)

        # ---------------------------------
        # STEP 3: PLAN TOOL
        # ---------------------------------

        selected_tool = plan_tool(user_input)

        state.selected_tool = selected_tool

        state.add_event(
            f"Agent selected tool: {selected_tool}"
        )

        # ---------------------------------
        # STEP 4: NO TOOL REQUIRED
        # ---------------------------------

        if selected_tool is None:

            state.final_response = (
                "Agent response generated without tool execution."
            )

            state.add_event(
                "No tool execution required."
            )

            return self.format_result(state)

        # ---------------------------------
        # STEP 5: EXECUTE TOOL
        # ---------------------------------

        tool_result = self.execute_selected_tool(
            selected_tool,
            user_input
        )

        state.tool_result = tool_result

        if tool_result.get("blocked"):

            state.add_event(
                "Tool execution blocked by permission sandbox."
            )

            state.final_response = tool_result.get(
                "message",
                "Tool execution was blocked."
            )

            return self.format_result(state)

        state.tool_executed = True

        state.add_event(
            "Tool execution completed."
        )

        # ---------------------------------
        # STEP 6: OUTPUT GUARD
        # ---------------------------------

        raw_result = tool_result.get(
            "result",
            ""
        )

        leakage = detect_sensitive_data(
            str(raw_result)
        )

        if leakage["leak_detected"]:

            state.leakage_detected = True
            state.output_blocked = True

            state.add_event(
                "Sensitive data detected in tool output."
            )

            state.final_response = (
                "Tool output blocked because "
                "sensitive data was detected."
            )

            return self.format_result(state)

        # ---------------------------------
        # STEP 7: SAFE RESPONSE
        # ---------------------------------

        state.final_response = self.create_response(
            selected_tool,
            raw_result
        )

        state.add_event(
            "Safe response returned to user."
        )

        return self.format_result(state)

    def execute_selected_tool(self, tool_name, user_input):

        if tool_name == "Calculator":

            numbers = self.extract_numbers(user_input)

            if len(numbers) < 2:

                return {
                    "success": False,
                    "blocked": False,
                    "message": (
                        "Calculator requires two numbers."
                    )
                }

            operation = self.determine_operation(
                user_input
            )

            return run_tool(
                "Calculator",
                a=numbers[0],
                b=numbers[1],
                operation=operation
            )

        if tool_name == "File Reader":

            filename = "product_notes.txt"

            return run_tool(
                "File Reader",
                filename=filename
            )

        if tool_name == "Customer Database":

            return run_tool(
                "Customer Database"
            )

        if tool_name == "Email Sender":

            return run_tool(
                "Email Sender",
                to="demo@example.test",
                subject="Simulation",
                message="Simulated email."
            )

        return {
            "success": False,
            "blocked": True,
            "message": "Unknown tool."
        }

    def create_response(self, tool_name, result):

        if tool_name == "Calculator":

            return f"Calculation result: {result}"

        if tool_name == "File Reader":

            return (
                "Document retrieved successfully."
            )

        return f"Tool result: {result}"

    def format_result(self, state):

        return {
            "user_input": state.user_input,
            "decision": state.decision,
            "risk_score": state.risk_score,
            "category": state.category,
            "selected_tool": state.selected_tool,
            "tool_executed": state.tool_executed,
            "tool_result": state.tool_result,
            "output_blocked": state.output_blocked,
            "leakage_detected": state.leakage_detected,
            "final_response": state.final_response,
            "events": state.events,
        }