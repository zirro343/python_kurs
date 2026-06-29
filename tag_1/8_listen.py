"""
Datentyp Liste (heterogenes Array)
Best Practice: nur den selben Datentyp als Listen-Elemten verwenden
"""
from copy import deepcopy


values = [1, 2, 24, 343]
backup = values # Vorsicht, hier wird nur die Referenz
real_shallow_backup = values.copy() # flache Kopie
real_deep_backup = deepcopy(values)
print(values)


# mit In-Operator Listenwerte prüfenb
if 24 in values:
    print("24 ist enthalten")

if [1, 2] == [1, 2]:
    print("die listen haben die selben Elemetne und Reihenfolge")

# Element hinzufügen
values.append(42)
print(values)

# Elemente hinzufügen (eine ganze Liste hinten anhängen)
values.extend([88, 99, 100])
print(values)

values.sort()  # inplace Sortierung
print("Values:", values)
print("Backup:", backup) # Backup ist values


print("Identität von values:", id(values))  # Speicherbereich, wo der Wert liegt
print("Identität von backup:", id(backup))  # Speicherbereich, wo der Wert liegt


def print_values(values):
    last_value = values.pop()
    print(last_value)

# wir übergeben values per Reference. in der Funktion löschen wir was raus (pop)
# damit haben wir die values-Liste (und somit auch backup verändert)
print_values(values)
print(values)

if values is backup:
    print("Es handelt sich um das gleiche Objekt")


if 30**50 is 30**50:
    print("30**50 und 30**50 sind das selbe Objekt")
else:
    print("30**50")