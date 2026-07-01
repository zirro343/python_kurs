"""
https://jsonplaceholder.typicode.com/todos

soll mit dem Paket "requests" ausgelesen werden.

pip install requests (http for humans)
"""

import requests


URL = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(URL)
todos = response.json()
# todos = json.loads(response.text)

# Aufgabe: alle Todos von userId 1 filtern (Erstelle eine Liste von todos für user id 1)
user_one_todos = []

for todo in todos:
    if todo["userId"] == 1:
        user_one_todos.append(todo)


print(user_one_todos)
