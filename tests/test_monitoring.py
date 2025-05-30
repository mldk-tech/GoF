from agentic_genai.decorator import monitor, monitor_call
from agentic_genai.factory import AgentFactory
from agentic_genai.mediator import AgentMediator


def test_monitor_decorator_logs():
    planner = AgentFactory.create_agent("planner", "p")
    executor = AgentFactory.create_agent("executor", "e")
    mediator = AgentMediator(planner, executor)
    mediator.handle("task")
    assert monitor.logs[-1] == "call:handle"
