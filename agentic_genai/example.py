from .factory import AgentFactory
from .mediator import AgentMediator
from .builder import PromptBuilder
from .rag import search_documents


def main(task: str) -> None:
    planner = AgentFactory.create_agent("planner", "planner")
    executor = AgentFactory.create_agent("executor", "executor")
    mediator = AgentMediator(planner, executor)
    context = search_documents(task)
    builder = PromptBuilder().add(task)
    if context:
        builder.add(context)
    prompt = builder.build()
    result = mediator.handle(prompt)
    print(result)


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "demo")
