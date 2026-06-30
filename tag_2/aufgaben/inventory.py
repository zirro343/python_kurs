"""
Das Inventar eines Players (`inventory`) soll mit dem Inhalt einer Truhe (`loot`) zusammengeführt werden.

Existiert ein Gegenstand bereits im Inventar, werden die Werte addiert.
Existiert er noch nicht, wird er neu eingefügt.

inventory = {
    "potion": 2,
    "shield": 1,
    "map": 2,
}

loot = {
    "potion": 2,
    "map": 1,
    "food": 1,
}

Erwartetes Ergebnis:

{
    "potion": 4,
    "shield": 1,
    "map": 3,
    "food": 1,
}

Hinweise:

1. Mit dem `|`-Operator lassen sich zwei Dictionaries zusammenführen:

   c = a | b

   Bei gleichen Keys wird der alte Value jedoch überschrieben.

2. Verwende `dict.get()`, um einen vorhandenen Wert oder einen Standardwert zu erhalten:

   value = inventory.get(key, 0)
"""
