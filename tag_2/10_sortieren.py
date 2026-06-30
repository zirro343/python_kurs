"""
Sortieren von Listen und Dictionaries
"""

numbers = [5, 2, 8, 2, 9, 3, 5, 4]
# numbers.sort() # macht ein inplace-Sortierung (mit Tim-Sort)
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)


chars = ["a", "f", "c", "d", "e"]
sorted_chars = sorted(chars)
print("Sorted chars:", sorted_chars)

chars = ["a", "f", "b", "B", "A", "d", "e", "u", "z", "a"]
sorted_chars = sorted(chars, key=lambda el: el.lower())
sorted_chars = sorted(chars, key=str.lower)
print("Sorted chars:", sorted_chars)

# AUFGABE (es soll nach dem letzten Zeichen sortiert werden)
ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
ids_sorted = sorted(ids, key=lambda x: x[-1])
print(ids_sorted)

# Snacks (Aufsteigend nach Preis)
snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}

print(list(snacks.items()))
snacks_aufsteigend = dict(sorted(snacks.items(), key=lambda x: x[1]))
print(snacks_aufsteigend)

# print(list(snacks))
# snacks_aufsteigend = sorted(snacks, key=lambda x: snacks[x])
# print(snacks_aufsteigend)

# Nach Preis sortieren
snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}
