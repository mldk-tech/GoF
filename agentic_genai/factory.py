from .agent import PlannerAgent, ExecutorAgent, Agent


class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str, name: str) -> Agent:
        if agent_type == "planner":
            return PlannerAgent(name)
        if agent_type == "executor":
            return ExecutorAgent(name)
        raise ValueError(f"unknown type {agent_type}")
