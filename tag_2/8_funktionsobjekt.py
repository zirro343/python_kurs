"""
Funktionsobjekt

alles ist ein Objekt, Funktionen sind auch Objekte

Call by object reference (Call by assignment)
"""

MAX = 3


def fn(a: int, values: list) -> None:
    """das ist der Docstring der Funktion fn."""
    # global MAX => bad pratice
    # values = values.copy()
    MAX = 4
    values.append(12374932798)
    print("Loakele Variablen von fn:", locals())


meine_liste = [1, 2]
fn(3, meine_liste)

# das Funktions-Objekt fn
print(fn.__doc__, fn.__code__.co_varnames)

fx = fn  # hier wird die Referenz kopiert
fx(4, meine_liste)
print(f"Typ von fn: {type(fn)}")
print("globals:", globals())
