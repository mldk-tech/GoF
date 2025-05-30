from agentic_genai.factory import AgentFactory
from agentic_genai.agents import PlannerAgent, ExecutorAgent


def test_factory():
    assert isinstance(AgentFactory.create_agent("planner"), PlannerAgent)
    assert isinstance(AgentFactory.create_agent("executor"), ExecutorAgent)
