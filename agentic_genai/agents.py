from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

class BaseAgent:
    def run(self, task: str) -> str:
        raise NotImplementedError

@dataclass
class Memory:
    messages: List[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.messages.append(message)

class PlannerAgent(BaseAgent):
    def __init__(self, memory: Optional[Memory] = None):
        self.memory = memory or Memory()

    def run(self, task: str) -> str:
        self.memory.add(task)
        return f"PLAN:{task}"

class ExecutorAgent(BaseAgent):
    def __init__(self, memory: Optional[Memory] = None):
        self.memory = memory or Memory()

    def run(self, plan: str) -> str:
        self.memory.add(plan)
        return f"DONE:{plan}"
