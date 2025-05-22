import requests

# API pública de exemplo
url = "https://jsonplaceholder.typicode.com/posts/1"
resposta = requests.get(url)

assert resposta.status_code == 200, "Falha na requisição"
print("Requisição bem-sucedida:", resposta.json())
