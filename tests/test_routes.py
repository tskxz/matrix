import pytest

from app import app


@pytest.fixture
def client():
    """Create test client for Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_sum_sub_get_route(client):
    """Test GET request returns HTML page"""
    response = client.get("/sum-sub")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data


def test_add_matrices(client):
    """Test addition of two 2x2 matrices"""
    payload = {
        "rows": 2,
        "cols": 2,
        "matrix_a": [[1, 2], [3, 4]],
        "matrix_b": [[5, 6], [7, 8]],
        "operation": "add",
    }

    response = client.post("/sum-sub", json=payload, content_type="application/json")

    data = response.get_json()

    assert response.status_code == 200
    assert "result" in data
    assert data["result"] == [[6, 8], [10, 12]]


def test_subtract_matrices(client):
    """Test subtraction of two 2x2 matrices"""
    payload = {
        "rows": 2,
        "cols": 2,
        "matrix_a": [[5, 6], [7, 8]],
        "matrix_b": [[1, 2], [3, 4]],
        "operation": "subtract",
    }

    response = client.post("/sum-sub", json=payload, content_type="application/json")

    data = response.get_json()

    assert response.status_code == 200
    assert "result" in data
    assert data["result"] == [[4, 4], [4, 4]]


def test_invalid_operation(client):
    """Test invalid operation returns error"""
    payload = {
        "rows": 2,
        "cols": 2,
        "matrix_a": [[1, 2], [3, 4]],
        "matrix_b": [[5, 6], [7, 8]],
        "operation": "invalid",
    }

    response = client.post("/sum-sub", json=payload, content_type="application/json")

    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data


def test_add_3x3_matrices(client):
    """Test addition of two 3x3 matrices"""
    payload = {
        "rows": 3,
        "cols": 3,
        "matrix_a": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "matrix_b": [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
        "operation": "add",
    }

    response = client.post("/sum-sub", json=payload, content_type="application/json")

    data = response.get_json()

    assert response.status_code == 200
    assert data["result"] == [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
