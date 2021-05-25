from fastapi.testclient import TestClient
from app.main import app
import pytest
client = TestClient(app)

def test_if_app_works():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}

