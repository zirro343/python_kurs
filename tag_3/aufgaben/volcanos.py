"""
Aufgabe: CSV manuell einlesen und in JSON umwandeln

Nutze KEIN csv.reader, sondern split() zur Verarbeitung der Zeilen.

Die CSV enthält Vulkandaten im folgenden Format:

VolcanoID,V_Name,Country,Region,Subregion,Latitude,Longitude,...,risk

Beispiel-Zeile:
211020,Vesuvius,Italy,Mediterranean and W Asia,Italy,40.820999999999900,14.426000000000000,...,3

Erstelle daraus eine JSON-Liste von Objekten.

Jedes Objekt soll folgende Keys enthalten:
name, risk, lat, long, country, region

Beispiel-JSON-Ausgabe:

[
    {
        "name": "Vesuvius",
        "risk": "3",
        "lat": "40.820999999999900",
        "long": "14.426000000000000",
        "country": "Italy",
        "region": "Mediterranean and W Asia"
    },
    {
        "name": "Stromboli",
        "risk": "1",
        "lat": "38.789000000000000",
        "long": "15.212999999999900",
        "country": "Italy",
        "region": "Mediterranean and W Asia"
    }
]

ERstelle eine main.py und importiere die
json-logik aus einem eigenen Modul (zb. parser.py)
"""
