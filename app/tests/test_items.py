from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={
        "name": "Test Item",
        "description": "A test item",
        "price": 10.5,
        "available": True
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404