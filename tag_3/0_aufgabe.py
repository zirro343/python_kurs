"""
Aufgabe: Erstelle ein Dictionary mit den Schlüsseln
"name", "alter" und "stadt".

Gib zuerst den Wert zu "name" aus.

Ändere anschließend den Wert von "alter".

Füge den neuen Schlüssel "beruf" mit einem passenden
Wert hinzu.

Gib zum Schluss das vollständige Dictionary aus, und zwar
iterativ via key, value ...
"""

person = {
    "name": "Max",
    "alter": 25,
    "stadt": "Berlin",
}

print(person["name"])
person["alter"] = 26
person["beruf"] = "Entwickler"

for key, value in person.items():
    print(key, value)
