# GoF Agentic GenAI Examples

This repo demonstrates Gang of Four (GoF) design patterns in a small Agentic GenAI example.

## Setup
Run the database migration to seed sample documents:

```bash
python -m agentic_genai.db_migrate
```

## Example script
Execute a simple planner/executor flow:

```bash
python -m agentic_genai.example "write code"
```

## FastAPI service
Start the service with uvicorn:

```bash
uvicorn agentic_genai.service:app --reload
```

POST `/task` with form field `task` to process a request.

## Tests
Run the unit tests with:

```bash
pytest -q
```

See `research_GoF_Agentic_GenAI.md` for the research document.
