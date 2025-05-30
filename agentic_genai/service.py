from fastapi import FastAPI, Form

from .factory import AgentFactory
from .mediator import AgentMediator
from .rag import search_documents
from .builder import PromptBuilder

app = FastAPI()


@app.post("/task")
def process_task(task: str = Form(...)):
    planner = AgentFactory.create_agent("planner", "planner")
    executor = AgentFactory.create_agent("executor", "executor")
    mediator = AgentMediator(planner, executor)
    context = search_documents(task)
    builder = PromptBuilder().add(task)
    if context:
        builder.add(context)
    prompt = builder.build()
    result = mediator.handle(prompt)
    return {"result": result}
