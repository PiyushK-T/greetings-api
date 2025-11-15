# app/config.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    service_name: str = "Greetings API"
    version: str = "1.0.0"
    max_name_length: int = 64

settings = Settings()
