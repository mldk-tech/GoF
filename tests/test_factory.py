from agentic_genai.factory import AgentFactory
from agentic_genai.agent import PlannerAgent, ExecutorAgent


def test_create_planner():
    agent = AgentFactory.create_agent("planner", "p")
    assert isinstance(agent, PlannerAgent)


def test_create_executor():
    agent = AgentFactory.create_agent("executor", "e")
    assert isinstance(agent, ExecutorAgent)

    
def test_factory():
    assert isinstance(AgentFactory.create_agent("planner"), PlannerAgent)
    assert isinstance(AgentFactory.create_agent("executor"), ExecutorAgent)