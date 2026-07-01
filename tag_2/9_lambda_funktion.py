"""
Lambda Ausdruck: anonyme Funktion
=> erzeugt immer ein Funtkions-Objekt
=> wird gerne als Wegwerf-Funktion für Sortieraufgaben, Filter u.ä. genutzt

Schema:
lambda Parameter1, Parameter2: Ausdruck
"""

s = lambda a, b: a + b
print(s(3, 2), type(s))


def summe(a, b):
    return a + b


summe
summe(2, 4)
