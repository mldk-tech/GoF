from agentic_genai.factory import AgentFactory
from agentic_genai.mediator import AgentMediator


def test_mediator_flow():
    planner = AgentFactory.create_agent("planner", "p")
    executor = AgentFactory.create_agent("executor", "e")
    mediator = AgentMediator(planner, executor)
    result = mediator.handle("task")
    assert result == "Executed Plan for task"
