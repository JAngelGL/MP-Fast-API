from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_item():
    response = client.post("/items/", json={
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 1500.0,
        "available": True
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 1500.0


def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404


def test_update_item():
    # Crear primero
    create = client.post("/items/", json={
        "name": "Phone",
        "description": "Smartphone",
        "price": 800.0,
        "available": True
    })
    item_id = create.json()["id"]

    # Actualizar
    response = client.put(f"/items/{item_id}", json={
        "name": "Phone Updated",
        "description": "Smartphone updated",
        "price": 900.0,
        "available": False
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Phone Updated"


def test_delete_item():
    create = client.post("/items/", json={
        "name": "Tablet",
        "description": "Android tablet",
        "price": 400.0,
        "available": True
    })
    item_id = create.json()["id"]

    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204