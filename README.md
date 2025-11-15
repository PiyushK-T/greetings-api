# Greetings API

A small FastAPI project for generating international greetings.

## Features

- REST API with FastAPI
- Pydantic V2 models & validators
- Supports multiple languages: en, es, fr, de, it, pt, hi, zh, ja, ar
- GET & POST endpoints for greeting
- `/health` and `/languages` endpoints
- Unit tests with pytest

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
