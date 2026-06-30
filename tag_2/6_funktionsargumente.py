"""
Funktionsargumente und Default-Parameter
"""

from typing import Any


def volume(a: int, b: int, c: int) -> int:
    return a * b * c


def area(width: float, height: float = 100):
    print("Area:", width, height)


# postionelle Argumente
volume(1, 23, 3)

# per Keyword Argument (benanntes Argument)
volume(b=3, c=2, a=1)

# Area (Detfault-Parameter b hat den Wert 100 und muss nur übergeben werden, wenn ein
# anderer Wert genutzt werden soll)
area(1)
area(1, 2)  # überschreibt Defaultwert 100

"""

Schreiben Sie eine Funktion filter_integer_data(values), 
die eine Sequenz als Parameter erhält und eine neue Liste 
zurückgibt, die ausschließlich Elemente vom Typ int enthält. 
Verwenden Sie zur Typprüfung die Funktion isinstance(objekt, typ).
"""


def filter_integer_data(values: list[Any]) -> list[int]:
    """Filtere Integer aus einer heterogenen Liste."""
    out = []
    for value in values:
        if isinstance(value, int):
            out.append(value)
    return out


cleaned_values = filter_integer_data(values=[1, 2, "3", 2.2, 42])  # [1, 2, 42]
print(cleaned_values)
