from .agent import Agent
from .decorator import monitor_call


class AgentMediator:
    def __init__(self, planner: Agent, executor: Agent):
        self.planner = planner
        self.executor = executor

    @monitor_call
    def handle(self, task: str) -> str:
        plan = self.planner.act(task)
        result = self.executor.act(plan)
        return result
