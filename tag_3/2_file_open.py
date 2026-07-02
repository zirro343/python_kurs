"""
Datei öffnen zum Lesen.

Übersicht Modi
'r'     Open for reading (default). Fehler wenn Datei nicht exisitert
'w'     Open for writing, overwriting file. Legt Datei an, wenn nicht exist
'a'     Append. Legt Datei an, wenn nicht exist
'rb' or 'wb'  Open in binary mode (read/write using byte data)
"""

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# Datei im Lesemodus öffnen
f = open(DATA_DIR / "cities.txt", mode="r", encoding="utf-8")
content = f.read()
print(content)
f.close()

# Bessere Variante, da das File automatisch geschlossen wird
# auch im Fehlerfall wird die Datei garantiert wieder geschossen
with open(DATA_DIR / "cities.txt", mode="r", encoding="utf-8") as f:
    content = f.read()
    print(content)

print("*" * 40)
# Zeilen-Iterator (iterativ über Datei streamen)
with open(DATA_DIR / "cities.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print("=>", line, end="")
    print("*" * 40)

    for line in f:
        print("=>", line, end="")

    print("*" * 40)
