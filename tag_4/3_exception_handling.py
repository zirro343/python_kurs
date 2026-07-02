"""
Ausnahmebehandlung in Python
https://python-umsteiger.friendlybytes.net/chapter_07/#exceptions-verstehen

https://docs.python.org/3/library/exceptions.html

Eigene Exceptions erben immer von Exception

class MyException(Exception):
    pass
"""

# IndexError provozieren und abfangen
values = [1, 2]
try:
    values[23]
except IndexError as e:
    print(f"Es ist ein Index-Error aufgetreten: {e}")
except Exception as e:
    print(f"Fehler wurde abgefangen: {e}, Typ: {type(e)}")
finally:
    print("Hier machen wir die Aufräumarbeiten")
