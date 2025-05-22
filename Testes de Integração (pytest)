# test_api_integracao.py
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_consulta_posts():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert "userId" in response.json()
