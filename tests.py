from fastapi.testclient import TestClient
from app.main import app
import pytest
client = TestClient(app)

def test_if_app_works():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}

def test_registration():
    response = client.put("/register?username=daft&password=daft")
    assert response.status_code == 201
    assert response.json().get('id')

def test_already_registrated():
    response = client.put("/register?username=daft&password=daft")
    assert response.status_code == 409
    assert response.json() == {"detail": "User already exists in Database"}

def test_login():
    response = client.post("/login?username=daft&password=daft")
    assert response.status_code == 200
    assert response.cookies.get('access_token')

def test_wrong_login():
    response = client.post("/login?username=aft&password=daft")
    assert response.status_code == 406
    assert response.json() == {"detail": "Supplied wrong username or password"}


def test_delete_user():
    response = client.delete("/delete_user?username=daft")
    assert response.status_code == 200
    
