from agentic_genai.factory import AgentFactory
from agentic_genai.mediator import AgentMediator


def test_mediator_flow():
    planner = AgentFactory.create_agent("planner")
    executor = AgentFactory.create_agent("executor")
    mediator = AgentMediator(planner, executor)
    result = mediator.handle("task")
    assert result == "DONE:PLAN:task"
