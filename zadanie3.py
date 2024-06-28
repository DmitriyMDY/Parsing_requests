import requests

# URL для отправки данных
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Печать статус-кода ответа
print("Status Code:", response.status_code)

# Печать содержимого ответа в формате JSON
print("Response JSON:", response.json())
