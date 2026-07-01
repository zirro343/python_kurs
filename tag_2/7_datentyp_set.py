"""
Datentyp Set: verändlicher Datentyp (Menge aus der Mengenlehre)

Beim Umwandlung von einer liste in ein Set geht die Reihenfolge verloren!
"""

cities = ["Hamburg", "Hamburg", "Berlin"]

# klassisch (Eindedutige Städte bestimmen)
unique_cities = []
for city in cities:
    if city not in unique_cities:
        unique_cities.append(city)

print("Eindeutige Städte:", unique_cities)

# python
unique_cities = list(set(cities))  # {"hamburg", "berlin"}
print("Eindeutige Städte:", unique_cities)

# Prüfen, welche Städte in beiden Listen vorkommen
cities_a = ["Hamburg", "Hamburg", "Berlin", "Dresden", "Freiburg"]
cities_b = ["München", "Passau", "Berlin", "Dresden"]
print("Städte in beiden Listen:", set(cities_a) & set(cities_b))  # & => intersection

# leeres Set
empty = set()
empty.add(42)

# Prüfen, ob ein Set ein anderes Set beinhaltet
cities_c = ["München", "Passau"]
if set(cities_c) < set(cities_b):
    print("Cities C ist in Cities B enthalten")


# Iteration über ein Set
cities_a = ["Hamburg", "Hamburg", "Berlin", "Dresden", "Freiburg"]
for el in set(cities_a):
    print(el)
