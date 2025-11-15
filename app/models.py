# app/models.py
from pydantic import BaseModel, Field, field_validator
from typing import Dict

SUPPORTED_LANGUAGES: Dict[str, str] = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "hi": "Hindi",
    "zh": "Chinese (Simplified)",
    "ja": "Japanese",
    "ar": "Arabic",
}

class GreetRequest(BaseModel):
    name: str
    lang: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Name must not be empty")
        if len(v) > 128:
            raise ValueError("Name too long (max 128 chars)")
        return v

    @field_validator("lang")
    @classmethod
    def validate_lang(cls, v: str) -> str:
        if v not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language code: {v}")
        return v

class GreetResponse(BaseModel):
    greeting: str

    model_config = {
        "json_schema_extra": {
            "examples": [{"greeting": "Hello, Piyush!"}]
        }
    }

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str

class LanguagesResponse(BaseModel):
    languages: Dict[str, str]
