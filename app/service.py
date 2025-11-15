# app/service.py
from typing import Dict
import logging
from .i18n import LOCALIZATIONS, LANGUAGE_DISPLAY
from .config import settings

logger = logging.getLogger(__name__)

class GreetingsService:
    def __init__(self, templates: Dict[str, str] = LOCALIZATIONS):
        self._templates = templates.copy()

    def supported_languages(self) -> Dict[str, str]:
        return {code: LANGUAGE_DISPLAY.get(code, code) for code in sorted(self._templates.keys())}

    def create_greeting(self, name: str, lang: str = "en") -> str:
        name = name.strip()
        if not name:
            raise ValueError("Name must not be empty")
        if len(name) > settings.max_name_length:
            raise ValueError(f"Name cannot exceed {settings.max_name_length} characters")
        if lang not in self._templates:
            raise ValueError(f"Unsupported language code: '{lang}'")

        greeting = self._templates[lang].format(name=name)
        logger.info("Generated greeting: %s (lang=%s)", greeting, lang)
        return greeting

# Default service instance
default_service = GreetingsService()
