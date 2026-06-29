""" 
Iterieren über Listen
"""
values = [12, 43, 4, 553, 23]

for value in values:
    print(value)

# C-Style-Loop 
for i in range(0, 10):
    print(i)

# Auf die Listen-Indizies zugreifen im Range-Funktion
values = [12, 43, 4, 553, 23]
for i in range(0, len(values)):  # 0:5
    print(values[i])


# Aufgabe, filtere eine bestehende Liste
# nur Elemente >= 14 sollen in die neue Liste
numbers = [1, 33, 14, 8, 89]
numbers_filtered = []
 
for number in numbers:
    if number >= 14:
        numbers_filtered.append(number)
 
print(numbers)
print(numbers_filtered)
 