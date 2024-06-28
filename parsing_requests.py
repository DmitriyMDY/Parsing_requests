import requests

# URL для поиска репозиториев с кодом html
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    'q': 'language:html'
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Печать статус-кода ответа
print("Status Code:", response.status_code)

# Печать содержимого ответа в формате JSON
print("Response JSON:", response.json())
