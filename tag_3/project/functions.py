"""
project/functions.py

Functions stellt math. Funtionen zur Verfügung
Maintainer: B. Fischer (Abteilung 3, 038938923)
"""

# __main__  => wenn es direkt ausgeführkt wird
# functions => wenn es importiert wird
print("Name des Moduls functions:", __name__)


def summe(a: int, b: int) -> int:
    return a + b


# die folgende Zeile ist nur wahr, wenn
# das Modul direkt ausgeführt wird.
# Wenn es importiert wird, ist __name__ nicht
# __main__.
if __name__ == "__main__":
    print("Summe:", summe(3, 2))
