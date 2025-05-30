from .agents import PlannerAgent, ExecutorAgent, BaseAgent, Memory

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str, memory: Memory | None = None) -> BaseAgent:
        if agent_type == "planner":
            return PlannerAgent(memory)
        if agent_type == "executor":
            return ExecutorAgent(memory)
        raise ValueError(f"unknown agent type: {agent_type}")
