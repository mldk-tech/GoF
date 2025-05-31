from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .memory import Memory


@dataclass
class Agent:
    name: str
    memory: Memory = field(default_factory=Memory)

    def act(self, task: str) -> str:
        raise NotImplementedError


class PlannerAgent(Agent):
    def act(self, task: str) -> str:
        plan = f"Plan for {task}"
        self.memory.add(f"planned:{task}")
        return plan


class ExecutorAgent(Agent):
    def act(self, task: str) -> str:
        result = f"Executed {task}"
        self.memory.add(f"executed:{task}")
        return result
