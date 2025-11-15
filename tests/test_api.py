# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.i18n import SUPPORTED_LANGUAGES

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"

def test_languages():
    r = client.get("/languages")
    assert r.status_code == 200
    data = r.json()
    for code in SUPPORTED_LANGUAGES:
        assert code in data["languages"]

def test_greet_get_success():
    r = client.get("/greet", params={"name": "Alice", "lang": "en"})
    assert r.status_code == 200
    assert "Alice" in r.json()["greeting"]

def test_greet_post_success():
    r = client.post("/greet", json={"name": "Bob", "lang": "fr"})
    assert r.status_code == 200
    assert "Bob" in r.json()["greeting"]

def test_greet_post_invalid_lang():
    r = client.post("/greet", json={"name": "Charlie", "lang": "xx"})
    assert r.status_code == 422
    assert "Unsupported language code" in r.text
