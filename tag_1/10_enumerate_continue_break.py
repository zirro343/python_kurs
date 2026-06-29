""" 
Iteration: enumerate, break, continue 
"""
students = ["Bob", "Alice", "Grumpy"]
grades = [2, 1, 6]

# ENUMERATE

# Ziel: Bob: 2, Alice: 1, Grumpy: 6
for i in range(0, len(students)):
    print(f"Der Schüler {students[i]} hat die Note: {grades[i]}")

# Pythonische Lösung:
for index, student in enumerate(students):
    print(f"Der Schüler {student} hat die Note: {grades[index]}")



# BREAK (brich die aktuelle Schleife ab)
for student in students:
    if student == "Bob":
        print("Bob wurde gefuden")
        break


# Suche nach einem Schüler (klassisch, ohne for-else)
students = ["Bob", "Alice", "Grumpy"]
found = False

search = "Bobby"
for student in students:
    if student == search:
        print(f"{search} wurde gefuden")
        found = True
        break

if not found:
    print(f"{search} wurde nicht gefunden")


# Suche nach einem Schüler
# for-else (else wird ausgeführt, wenn der loop nicht mit break abgebrochen hat)
students = ["Bob", "Alice", "Grumpy"]
search = "Bobby"

for student in students:
    if student == search:
        print(f"{search} wurde gefuden")
        break
else:
    print(f"{search} wurde nicht gefunden")


# ein continue bricht den aktuellen Schleifendurch gang 
students = ["Bob", "Alice", "Grumpy"]
for student in students:
    if student.startswith("A"):
        continue 

    # hier folgte aufwändige Verarbéitung von Studenten, die nicht mit A 
    # anfangen
    print(student)

