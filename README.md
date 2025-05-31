# GoF Agentic GenAI Examples

This repo demonstrates Gang of Four (GoF) design patterns in a small Agentic GenAI example.
This repository basedon demonstrates applying Gang of Four design patterns in a small Agentic GenAI example.

## Setup
Run the database migration to seed sample documents:

```bash
python -m agentic_genai.db_migrate
```

## Running the example script
Execute a simple planner/executor flow:

```bash
python -m agentic_genai.example "write docs"
```

## Running the FastAPI service
Start the service with uvicorn:

```bash
uvicorn agentic_genai.service:app --reload
```
Then open http://localhost:8000 in your browser.

POST `/task` with form field `task` to process a request.

## Tests
Run the unit tests with:

```bash
pytest -q or python -m pytest -q
```
