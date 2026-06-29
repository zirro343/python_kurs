"""
Aufgabe: Eingabe validieren

Schreibe ein Python-Programm, das den Benutzer zur Eingabe eines Wortes auffordert.

Die Eingabe gilt nur dann als gültig, wenn alle folgenden Bedingungen erfüllt sind:

- Das Wort enthält keine Leerzeichen.
- Das Wort enthält den Großbuchstaben 'A'.
- Das Wort ist mindestens 3 Zeichen lang.

Ist mindestens eine Bedingung nicht erfüllt, gib aus:

    Ihre Eingabe war: <Eingabe>
    Ihre Eingabe ist leider falsch.

Andernfalls gib aus:

    Ihre Eingabe ist korrekt.

in-operator, if, else, len(), (x not in [....])
"""


eingabe = input("Bitte gebe ein gültiges Wort ein: ")

if " " in eingabe or "A" not in eingabe or len(eingabe) < 3:
    print("Ihre Eingabe war:", eingabe)
    print("Ihre Eingabe ist leider falsch.")
else:
    print("Ihre Eingabe ist korrekt.")