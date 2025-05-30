from .agents import BaseAgent

class AgentMediator:
    def __init__(self, planner: BaseAgent, executor: BaseAgent):
        self.planner = planner
        self.executor = executor

    def handle(self, task: str) -> str:
        plan = self.planner.run(task)
        return self.executor.run(plan)
