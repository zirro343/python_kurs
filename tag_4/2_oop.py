"""
Öffentliche und nicht-öffentliche Attribute
Property: Regel für Name: darf nicht < 3 Zeichen sein
"""


class Person:
    def __init__(self, name: str, department: str) -> None:
        self.name = name  # öffentliches Attribut (hier wird der Setter aufgerufen)
        self.department = department
        self._gehalt = 1000  # nicht-öffentliches Attribut (Konvention)

    @property
    def name(self) -> str:
        """GETTER für das Attribut name. Der Wert von name wird intern
        in self._name gehalten."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) < 3:
            raise ValueError("Name ist zur kurz.")

        self._name = new_name

    def __str__(self) -> str:
        """Die String-Repräsentation der Klasse Person (Nutzer)"""
        return self.name

    def __repr__(self) -> str:
        """interne Repräsentation für Debugging."""
        return f"Person({repr(self.name)}, {repr(self.department)})"


bob = Person("Bob", "Technik")
bob.name = "Bobby"
print("Direktes Addresseriern von name:", bob.name)
# bob._gehalt = 100  BAD! nicht-öffentliche Attribute sollen von außen nicht
# angesprochen werden
