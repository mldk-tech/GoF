from .factory import AgentFactory
from .mediator import AgentMediator
from .builder import PromptBuilder
from .rag import migrate, search


def main(task: str) -> None:
    migrate()
    planner = AgentFactory.create_agent("planner")
    executor = AgentFactory.create_agent("executor")
    mediator = AgentMediator(planner, executor)
    prompt = PromptBuilder().add(task).build()
    docs = search(task)
    if docs:
        prompt += "\n" + "\n".join(docs)
    result = mediator.handle(prompt)
    print(result)

if __name__ == "__main__":
    import sys
    task = sys.argv[1] if len(sys.argv) > 1 else "demo"
    main(task)
