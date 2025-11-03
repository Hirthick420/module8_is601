from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def post(path, a, b):
    return client.post(path, json={"a": a, "b": b})

def test_add_endpoint():
    r = post("/add", 2, 3)
    assert r.status_code == 200
    assert r.json() == {"result": 5}

def test_subtract_endpoint():
    r = post("/subtract", 5, 3)
    assert r.status_code == 200
    assert r.json() == {"result": 2}

def test_multiply_endpoint():
    r = post("/multiply", 2, 4)
    assert r.status_code == 200
    assert r.json() == {"result": 8}

def test_divide_endpoint():
    r = post("/divide", 6, 3)
    assert r.status_code == 200
    assert r.json() == {"result": 2}

def test_divide_by_zero_returns_client_error():
    r = post("/divide", 1, 0)
    assert r.status_code in (400, 422)
