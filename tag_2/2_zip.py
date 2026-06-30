"""
Die zip-Funktion (Reißverschluss)
"""

students = ["Bob", "Alice", "Grumpy"]
grades = [2, 1, 6]

for student, grade in zip(students, grades):
    print(student, grade)


# aus zwei Listen via zip und dict ein Dictionary erstellen
d = dict(zip(students, grades))
print(d)

###################################################
print("*" * 40)
cities = ["Hamburg", "Nürnberg", "Berlin"]
for r in zip(students, grades, cities):
    print(r)
