# test_rest_api.py
# test_requests + pytest
import requests

def test_criar_usuario():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"
