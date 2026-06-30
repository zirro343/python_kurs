"""
Python Funktionen

Funtionsname: snake case (klein, underscore)
Parameterkopf
Type Hints: Typ-Hinweise in Python-Funktionen und auch sonst überall
Tools wie mypy oder pyright (zum Beispiel in CD/CI prüfen dann gegen Typ-Verstöße)
Jede Funktion hat einen Default-Rückgabewert: None
Variablenname: Typ

pip install mypy

mypy .\5_functions_intro.py
"""


def summe(a: int, b: int) -> int:
    return a + b


def snake_case(values: list, index: int) -> bool:
    """Das ist eine kleine Funktion."""
    if index in values:
        return True

    return False


snake_case([1, 2, 3], 2)
print("Summe:", summe("1", "3"))
