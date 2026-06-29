# ============================================================================
# Aufgabe 1: Iteration über eine Liste
#
# Gegeben ist eine Liste mit mehreren Früchten.
#
# a) Gib jede Frucht in einer eigenen Zeile aus.
# b) Gib anschließend den Index und die Frucht gemeinsam aus.
#
# Verwende dazu eine for-Schleife und enumerate().
# ============================================================================
fruits = ["Banane", "Apfel", "Kirsche"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ============================================================================
# Aufgabe 2: Liste filtern (Strings)
#
# Gegeben ist eine Liste mit Fruchtnamen.
#
# Erstelle eine neue Liste, die nur die Früchte enthält,
# deren Name mit dem Buchstaben "B" beginnt.
# ============================================================================
fruits = ["Banane", "Apfel", "Kirsche", "Birne"]
filtered_fruits = []
for fruit in fruits:
    if fruit.startswith("B"):
        filtered_fruits.append(fruit)
print(filtered_fruits)


# ============================================================================
# Aufgabe 3: Liste filtern (Zahlen)
#
# Gegeben ist eine Liste mit Ganzzahlen.
#
# Erstelle eine neue Liste, die ausschließlich Zahlen enthält,
# die größer als 5 und kleiner als 100 sind.
#
# Gib die gefilterte Liste anschließend sortiert aus.
# ============================================================================

numbers = [1, 4, 5, 2, 42, 200, 1, 99, 23, 323]
filtered_numbers = []
for number in numbers:
    if 5 < number < 100:  # <<< Kurzschreibweise für: if number > 5 and number < 100
        filtered_numbers.append(number)
print(sorted(filtered_numbers))

# ============================================================================
# Aufgabe 4: Letztes Element einer Liste
#
# Gegeben ist eine Liste.
#
# Prüfe zunächst, ob die Liste nicht leer ist.
# Gib anschließend das letzte Element der Liste aus.
# ============================================================================
symbols = ["B", "C"]
if symbols:
    print("das letzte Element in der Liste: ", symbols[-1])



# ============================================================================
# Aufgabe 5: Nur erlaubte Werte übernehmen
#
# Gegeben ist eine Liste mit Zahlen sowie eine Liste
# mit erlaubten Werten.
#
# Erstelle eine neue Liste, die ausschließlich die Werte enthält,
# die in der Liste der erlaubten Werte vorkommen.
# ============================================================================
a = [50, 100, 40, 20, 200, 50, 100, 10]
allowed_values = [50, 100, 200]
c = []
for el in a:
    if el in allowed_values:
        c.append(el)
print(c)


# ============================================================================
# Aufgabe 6: Liste bereinigen
#
# Gegeben ist eine Liste mit Zeichenketten.
#
# Entferne aus jedem Element alle Unterstriche "_".
# Leere Zeichenketten sollen nicht in die neue Liste übernommen werden.
# ============================================================================
a = ["x_x", "alpha_beta", "_"]
c = []
for el in a:
    el = el.replace("_", "")
    if el:
        c.append(el)
print(c)


# ============================================================================
# Aufgabe 7: Zeichenketten bereinigen
#
# Gegeben ist eine Liste mit Zeichenketten.
#
# Für jedes Element:
# - entferne führende und nachfolgende Leerzeichen sowie Steuerzeichen
#   (strip())
# - entferne anschließend alle Vorkommen des Buchstabens "x"
#
# Leere Ergebnisse sollen nicht übernommen werden.
# ============================================================================
a = ["haxlt ", "\nandx", "\tcatch ", " xfire "]
c = []
for el in a:
    el = el.strip().replace("x", "")
    if el:
        c.append(el)
print("7: ", c)


# ============================================================================
# Aufgabe 8: Zwei Listen zusammenführen
#
# Gegeben sind zwei Listen unterschiedlicher Länge.
#
# Führe beide Listen elementweise zusammen.
#
# Beispiel:
#     ["A", "B", "C"]
#     [1, 2, 3]
#
# ergibt:
#     ["A1", "B2", "C3"]
#
# Die Verarbeitung soll enden, sobald die kürzere Liste
# vollständig verarbeitet wurde.
# ============================================================================
a = ["A", "B", "C", "D", "E", "F"]
b = [1, 2, 3, 4, 5]
c = []

for i, element in enumerate(a):
    if i >= len(b):
        break
    c.append(f"{element}{b[i]}")

print(c)