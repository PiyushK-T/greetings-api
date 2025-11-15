# app/main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import logging

from .config import settings
from .models import GreetResponse, GreetRequest, HealthResponse, LanguagesResponse
from .service import default_service

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("greetings_api")

app = FastAPI(title=settings.service_name, version=settings.version)

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service=settings.service_name, version=settings.version)

@app.get("/languages", response_model=LanguagesResponse)
def get_languages() -> LanguagesResponse:
    return LanguagesResponse(languages=default_service.supported_languages())

@app.get("/greet", response_model=GreetResponse)
def greet_get(
    name: str = Query(..., min_length=1, max_length=128),
    lang: str = Query("en")
) -> GreetResponse:
    try:
        greeting = default_service.create_greeting(name, lang)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return GreetResponse(greeting=greeting)

@app.post("/greet", response_model=GreetResponse)
def greet_post(payload: GreetRequest):
    try:
        greeting = default_service.create_greeting(payload.name, payload.lang)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return GreetResponse(greeting=greeting)

@app.get("/", include_in_schema=False)
def root():
    return JSONResponse({"message": f"Welcome to {settings.service_name} (v{settings.version}). Check /docs"})
