from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class AgentState:
    user_input: str
    decision: Optional[str] = None
    risk_score: int = 0
    category: str = "Unknown"

    selected_tool: Optional[str] = None
    tool_executed: bool = False
    tool_result: Any = None

    output_blocked: bool = False
    leakage_detected: bool = False

    final_response: Optional[str] = None

    events: List[str] = field(default_factory=list)

    def add_event(self, event: str):
        self.events.append(event)