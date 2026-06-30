"""
Gegeben ist eine Liste mit Wetterdaten. Jeder Eintrag beschreibt einen Tag und
enthält den Wochentag, das Datum sowie die gemessene Temperatur.

Schreibe eine Funktion

    get_hot_work_days(temp: list[dict], min_temp: int) -> list[tuple]

Die Funktion soll alle **Werktage** (Montag bis Freitag) auswählen, an denen
die Temperatur mindestens `min_temp` Grad beträgt.

Die Rückgabe ist eine Liste von Tupeln im Format:

(date, temperature)

Beispiel:

[
    ("2019-07-15", 31),
    ("2019-07-16", 33),
    ("2019-07-23", 31),
]

Hinweise:

* Nutze die Konstanten `MIN_TEMPERATURE` und `WEEKEND`.
* Die Funktion soll keine Ausgabe erzeugen, sondern das Ergebnis zurückgeben.
"""

MIN_TEMPERATURE = 30
WEEKEND = ("Saturday", "Sunday")


weekday_temperatures = [
    {"day": "Monday", "date": "2019-07-15", "temperature": 31},
    {"day": "Tuesday", "date": "2019-07-16", "temperature": 33},
    {"day": "Wednesday", "date": "2019-07-17", "temperature": 27},
    {"day": "Thursday", "date": "2019-07-18", "temperature": 25},
    {"day": "Friday", "date": "2019-07-19", "temperature": 30},
    {"day": "Saturday", "date": "2019-07-20", "temperature": 31},
    {"day": "Sunday", "date": "2019-07-21", "temperature": 29},
    {"day": "Monday", "date": "2019-07-22", "temperature": 25},
    {"day": "Tuesday", "date": "2019-07-23", "temperature": 31},
    {"day": "Wednesday", "date": "2019-07-24", "temperature": 26},
    {"day": "Thursday", "date": "2019-07-25", "temperature": 23},
    {"day": "Friday", "date": "2019-07-26", "temperature": 22},
    {"day": "Saturday", "date": "2019-07-27", "temperature": 23},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
]


def get_hot_work_days(temp: list[dict], min_temp: int) -> list[tuple]:
    """Filtere heiße Arbeitstage aus einer Temperatur-Liste."""
    hot_work_days: list[tuple] = []

    for temp_dict in temp:
        if temp_dict["day"] not in WEEKEND and temp_dict["temperature"] >= min_temp:
            t = (temp_dict["date"], temp_dict["temperature"])
            hot_work_days.append(t)

    return hot_work_days


result = get_hot_work_days(weekday_temperatures, min_temp=MIN_TEMPERATURE)
print(result)
