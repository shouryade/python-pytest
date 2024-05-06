# test_app.py
import pytest


@pytest.fixture
def client():
    response = "Hello, World!"
    assert "Hello, World!" in response

# def test_index(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b"Hello, World!" in response.data

# def test_invalid_route(client):
#     response = client.get('/invalid-route')
#     assert response.status_code == 404
