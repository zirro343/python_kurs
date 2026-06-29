"""
Zahlentypen in Python:

- int (keine Begrenzung)
- float (64bit, ieee 754)
- complex (komplexe Zahlen)

Arithmetische Operatoren

x + y   Summe von x und y
x - y   Differenz von x und y
x * y   Produkt von x und y
x / y   Quotient von x und y
x % y   Rest beim Teilen von x durch y*
+x  positives Vorzeichen
-x  negatives Vorzeichen
x ** y  x hoch y
x // y  abgerundeter Quotient von x und y*

Weitere nützliche builtin Funktionen:
- `sum()`: Summiert alle Werte in einer Sequenz.
- `min()`: Gibt den kleinsten Wert einer Sequenz zurück.
- `max()`: Gibt den größten Wert einer Sequenz zurück.

Für Decimal-Berechnungen das decimal Modul nutzen, um 
rundundsfehler zu vermeiden (zb. für Preise summieren)
import decimal

Statistische Grundfunktionen finden sich in statistics
import statistics

"""
import math 

x = 34837
print("Datentyp von x:", type(x)) # Objekt der Klasse <class 'int'>
# man könnte problemlos x auch einem String Objekt zuweisen (kein guter Stil!)
x = "hamburg"
print("Datentyp von x:", type(x)) 

# Datentyp float 
y = 3.14
print("Datentyp von y:", type(y)) 

# Divisionsoperator (Division erzeugt immer Float)
a = 4  # int
b = 2  # int
result = a / b
print("Ergebnis:", result)
print("Reslt nach int casten:", int(result))

# Floor-Div (Abrundungs-Division)
print("8 // 3:", 8 // 3, type(8 // 3))  # 2
print("-8 // 3:", -8 // 3, type(-8 // 3))  # -3

## Exponent
y = 3
x = y**2
print(x)


"""
Aufgabe:
Wieviele Baumstämme passen der Länge nach in die Halle.
Baumstamm-Länge 4, Hallenlänge 19. Wieviele Meter sind noch übrig?
Nutze Konstanten und Variablen.

Es passen ... Baumstämme in die Halle
"""
HALL_LENGTH = 19
tree_length = 4
total_trees = HALL_LENGTH // tree_length
total_rest = HALL_LENGTH % tree_length
print("Es passen in die Halle: ", total_trees, "Baumstämme")
print("Es ist übrig:", total_rest, "Meter")

# Nach int und float casten
zahl = "42"
zahl = int(zahl)
float_zahl = float(zahl)

print("Prüfen, ob zwei Floats nahe sind:", math.isclose(1.12, 1.14))
