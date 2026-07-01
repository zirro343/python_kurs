"""
Daten an alte Datei anhängen mit dem Modus a (append)
wenn Datei nicht existiert, wird sie neu erstellt, ansonsten wird angehängt
"""

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


# Neue Städte in Datei cities.txt eintragen
cities = [
    {"name": "Rostock", "population": 2329389},
    {"name": "Berlin", "population": 233489},
    {"name": "Dortmund", "population": 12329389},
    {"name": "Gütersloh", "population": 42329389},
]


def add_cities(cities: list) -> None:
    """Füge Städte der Cities-Datei hinzu."""
    with open(DATA_DIR / "cities.txt", mode="a", encoding="utf-8") as f:
        for city in cities:
            f.write(city["name"] + "\n")


add_cities(cities)
