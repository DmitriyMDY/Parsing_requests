import requests

# URL для получения записей
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    'userId': 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    # Печать полученных записей
    print("Response JSON:", response.json())
else:
    print("Failed to retrieve data. Status Code:", response.status_code)
