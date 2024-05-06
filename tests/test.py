# test_app.py
import pytest


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

# def test_index(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b"Hello, World!" in response.data

# def test_invalid_route(client):
#     response = client.get('/invalid-route')
#     assert response.status_code == 404
