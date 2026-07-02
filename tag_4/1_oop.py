"""
Konstruktor: ein Objekt bauen
__new__ => das ist der eigegentliche Konstruktor (den man nie braucht)
__init__ => das ist der Initialisierer

__str__ => öffentliche String-Repräsentation
__repr__ => interne, Debugging Repräsentation


https://python-umsteiger.friendlybytes.net/chapter_05/
"""


class Person:
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department

    def __str__(self) -> str:
        """Die String-Repräsentation der Klasse Person (Nutzer)"""
        return self.name

    def __repr__(self) -> str:
        """interne Repräsentation für Debugging."""
        return f"Person({repr(self.name)}, {repr(self.department)})"


bob = Person(name="Bob", department="IT")
print(f"Name von bob: {bob.name}")

print("Bob Objekt:", bob)
print("Listen Objekt:", [1, 2, 3])

str(bob)  # => Person.__str__()
print("Repr:", repr(bob))
