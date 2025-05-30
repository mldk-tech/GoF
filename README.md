# GoF

This repository demonstrates applying Gang of Four design patterns in a small Agentic GenAI example.

## Running the example
```bash
python -m agentic_genai.example "write docs"
```

## Running the FastAPI service
```bash
uvicorn agentic_genai.service:app --reload
```
Then open http://localhost:8000 in your browser.

## Tests
```bash
python -m pytest -q
```

See `research_GoF_Agentic_GenAI.md` for a research guide explaining the patterns.
