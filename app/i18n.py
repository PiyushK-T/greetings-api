# app/i18n.py
from typing import Dict

# In-memory localization templates.
# Templates use {name} placeholder.
LOCALIZATIONS: Dict[str, str] = {
    "en": "Hello, {name}!",
    "es": "¡Hola, {name}!",
    "fr": "Bonjour, {name}!",
    "de": "Hallo, {name}!",
    "it": "Ciao, {name}!",
    "pt": "Olá, {name}!",
    "hi": "नमस्ते, {name}!",
    "zh": "你好，{name}！",
    "ja": "こんにちは、{name}！",
    "ar": "مرحبًا، {name}!",
}

# Map for display names
LANGUAGE_DISPLAY: Dict[str, str] = {
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

SUPPORTED_LANGUAGES = sorted(list(LOCALIZATIONS.keys()))
