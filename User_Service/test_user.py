import pytest
from uService import app, db, User

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        
        with app.app_context():
            db.drop_all()

def test_register_user(client):
    response = client.post("/register", json={"name": "Edward", "email": "edward@gmail.com"})
    assert response.status_code == 201
    assert response.json["message"] == "User registered"
    assert response.json["user"]["name"] == "Edward"

def test_get_users(client):
    client.post("/register", json={"name": "Dexter", "email": "dexter@gmail.com"})
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Dexter"

def test_get_user(client):
    client.post("/register", json={"name": "Gerald", "email": "gerald@gmail.com"})
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json["name"] == "Gerald"

def test_update_user(client):
    client.post("/register", json={"name": "Kim", "email": "kim@gmail.com"})
    response = client.put("/users/1", json={"name": "Kim", "email": "kim@gmail.com"})
    assert response.status_code == 200
    assert response.json["message"] == "User updated"
    assert response.json["user"]["name"] == "Kim"

def test_delete_user(client):
    client.post("/register", json={"name": "Francis", "email": "francis@gmail.com"})
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json["message"] == "User deleted"
    response = client.get("/users/1")
    assert response.status_code == 404
