"""
Arbeiten mit Dateien und Pfaden
pathlib.Path arbeitet abstrahiert für Linux, Unix (u.a. auch OsX) und Windows-Pfade
"""

from pathlib import Path

print("Aktuelles Arbeitsverzeichnis:", Path.cwd())
print("Der aktuelle Pfad zu diesem Skript:", __file__)  # Dunder File
path = Path(__file__)
print(f"Path Objekt: {path}", f"Verzeichnis des Skripts: {path.parent}")

pfad = r"C:\Users"  # mit rawstring einen Pfad erstellen
path = Path(pfad)
if path.exists():
    print(f"Der Knoten {path} existiert")

print("*" * 40)

# Aufgabe: liste rekursiv alle Dateien auf im Root-Verzeichnis pythonkurs
# Rekursive Glob (rglob) durchläuft alle Verzeichnisse rekursiv anhand von
# einem Pattern (*.* => alle Dateien)
BASE_DIR = Path(__file__).parent.parent

for path in BASE_DIR.rglob("*.*"):
    print(path)
