"""
Entpacken von Sequenzen
"""

user_input = ["run", "localhost", "8081"]
command = user_input[0]
host = user_input[1]
port = user_input[2]

# Entpacken der Liste user_input in 3 Variablen
command, host, port = user_input

a, b, c = "ABC"
print(a, b, c)


def summe(a, b):
    print(a, b)


values = [
    (1, 2),
    (3, 5),
    (8, 2)
]

# Aufgabe, für jede Liste von values die funktion
# summe aufrufen
for value in values:
    a, b = value
    summe(a, b)

# Entpacken bei Funktionsaufruf 
for value in values:
    summe(*value)