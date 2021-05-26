from fastapi.testclient import TestClient
from app.main import app
import pytest
client = TestClient(app)
client.kappa = str()

def test_if_app_works():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}

def test_login():
    response = client.post("/login?username=daft&password=daft")
    assert response.status_code == 200
    assert response.cookies.get('access_token')

def test_registration():
    response = client.put("/register?username=notifaidaft&password=notifaidaft")
    assert response.status_code == 201
    assert response.json().get('id')

def test_already_registrated():
    response = client.put("/register?username=daft&password=daft")
    assert response.status_code == 409
    assert response.json() == {"detail": "User already exists in Database"}

def test_second_login():
    response = client.post("/login?username=notifaidaft&password=notifaidaft")
    assert response.status_code == 200
    assert response.cookies.get('access_token')
    client.kappa = response.cookies.get('access_token')
    
def test_wrong_login():
    response = client.post("/login?username=aft&password=daft")
    assert response.status_code == 406
    assert response.json() == {"detail": "Supplied wrong username or password"}

def test_viewing_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json()

def test_view_of_post():
    response = client.get("/post/3")
    assert response.status_code == 200
    assert response.json().get('postcontent')

def test_wrong_post_id():
    response = client.get("/post/3213213")
    assert response.status_code == 404
    assert response.json() == {"detail": "No post was found"}

client.idpost : int = int()

def test_inserting_post():
    response = client.put("/post", json={"postcontent": "notifai"})
    assert response.status_code == 201
    assert response.json().get('idpost')
    client.idpost = int(response.json().get('idpost'))
    print(client.idpost)

def test_updating_post():
    response = client.patch(f"/post/{client.idpost}", json={"postcontent": "daft"})
    assert response.status_code == 200
    assert response.json() == {"postcontent": "daft", "viewscounter": 0}

def test_deleting_post():
    response = client.delete(f"/post/{client.idpost}")
    assert response.status_code == 200
    assert response.json() == {"message": "post deleted"}


def test_logout():
    response = client.post("/logout", cookies={"access_token": client.kappa})
    assert response.status_code == 200

def test_logout_without_cookie():
    response = client.post("/logout")
    assert response.status_code == 204

def test_delete_user():
    response = client.delete("/delete_user?username=notifaidaft")
    assert response.status_code == 200

def test_delete_logged_out():
    response = client.delete("/post/3")
    assert response.status_code == 401
    
