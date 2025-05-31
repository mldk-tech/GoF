from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from .factory import AgentFactory
from .mediator import AgentMediator
from .rag import search_documents, migrate
# from .rag import search, migrate

from .builder import PromptBuilder

app = FastAPI()

migrate()

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


# planner = AgentFactory.create_agent("planner")
# executor = AgentFactory.create_agent("executor")
# mediator = AgentMediator(planner, executor)

# HTML_FORM = """
# <form method='post' action='/task'>
#   <input name='task' />
#   <button type='submit'>Run</button>
# </form>
# """

# @app.get("/", response_class=HTMLResponse)
# def index():
#     return HTML_FORM

# @app.post("/task")
# def run_task(task: str = Form(...)):
#     prompt = PromptBuilder().add(task).build()
#     docs = search(task)
#     if docs:
#         prompt += "\n" + "\n".join(docs)
#     result = mediator.handle(prompt)
#     return {"result": result}
