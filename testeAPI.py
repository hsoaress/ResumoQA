import requests

# API pública de exemplo
url = "https://jsonplaceholder.typicode.com/posts/1"
resposta = requests.get(url)

assert resposta.status_code == 200, "Falha na requisição"
print("Requisição bem-sucedida:", resposta.json())

#Saída: 
     #Requisição bem-sucedida: {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

