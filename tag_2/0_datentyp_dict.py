"""
Dict: veränderlicher Datentyp
"""
# Beispiel: Deutsch-Englisch-Wörterbuch
de_en = {
    "Katze": "cat",
    "Hund": "dog",
}
# Zugriff via Key
print(de_en["Katze"])

# Key-Error bei Einabe eines Keys, der nicht enthalten ist
# print(de_en["Katzen"]) KeyError: 'Katzen'

# mit der get-Methode einen Key anfragen und im Zweifel einen Defaultwert erhalten
print(de_en.get("Vogel", "Default-Tier"))

# Prüfen, ob ein Key im Dict
if "Katze" in de_en:
    print(de_en["Katze"])
else:
    print("Katze ist nicht im dict enthalten")

#######################################################
population = {
    'Berlin': 3_748_148,
    'Hamburg': 1_822_445,
    'München': 1_471_508,
    'Cologne': 1_085_664,
    'Frankfurt': 753_056
}
population["Hamburg"] = 2
print(population)

extra_populations = {
    "Nürnberg": 500_000,
    "Landsberg": 80_000,
    'Frankfurt': 42,
}

# zwei Dicts zusammenführen
population.update(extra_populations)
print(population)

# oder
new_populations = population | {"New York": 1}
print(new_populations )