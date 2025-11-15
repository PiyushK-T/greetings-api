# tests/test_service.py
import pytest
from app.service import GreetingsService

@pytest.fixture
def service():
    return GreetingsService()

def test_supported_languages_contains_en(service):
    langs = service.supported_languages()
    assert "en" in langs
    assert isinstance(langs["en"], str) and langs["en"]

def test_create_greeting_default_en(service):
    g = service.create_greeting("Alice", "en")
    assert "Alice" in g
    assert g.startswith("Hello") or "Hello" in g

def test_create_greeting_other_language(service):
    g = service.create_greeting("Bob", "es")
    assert "Bob" in g
    assert "Hola" in g or "¡Hola" in g

def test_create_greeting_invalid_name(service):
    with pytest.raises(ValueError):
        service.create_greeting("", "en")

def test_create_greeting_unsupported_lang(service):
    with pytest.raises(ValueError):
        service.create_greeting("Alice", "xx")

def test_create_greeting_name_too_long(service):
    long_name = "a" * 500
    with pytest.raises(ValueError):
        service.create_greeting(long_name, "en")
