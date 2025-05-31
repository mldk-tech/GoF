from .agent import PlannerAgent, ExecutorAgent, Agent, Memory


class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str, name: str, memory: Memory | None = None) -> Agent:
        if agent_type == "planner":
            return PlannerAgent(name, memory)
        if agent_type == "executor":
            return ExecutorAgent(name, memory)
        raise ValueError(f"unknown type {agent_type}")
