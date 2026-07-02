"""
Aufgabe: Klasse Product mit Property erstellen

Erstelle eine Klasse Product.

Die Klasse besitzt:

- name
- price

Für das Attribut price soll eine Property verwendet werden.

Anforderungen:

- Der Preis darf nur vom Typ float sein (isinstance)
- Ist der Preis kein float, soll eine ValueError
  ausgelöst werden.
- Der Preis darf nicht negativ sein.
- Ist der Preis kleiner als 0, soll ebenfalls eine
  ValueError ausgelöst werden.

Teste deine Klasse mit folgenden Beispielen:

Product("Tastatur", 49.99)
Product("Maus", -10.0)
Product("Monitor", "299.99")

Die ersten Daten sollen akzeptiert werden.
Die beiden anderen Beispiele sollen eine ValueError
auslösen.

"""


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        if not isinstance(price, (float, int)):
            raise ValueError("Preis muss numerisch sein!")

        if price < 0:
            raise ValueError("Preis muss positiv sein!")

        self._price = price


def main():
    # p = Product("Tastatur", 49.99)

    # Aufgabe vor der Pause: Liste von
    # Produkt-Objekten erstellen, wenn das
    # Objekt erstellt werden kann
    product_list = []  # << hier Produkt-Objekte rein
    products = [
        ("Tastatur", 49.99),
        ("Maus", 19.95),
        ("Monitor", -299.99),
        ("Headset", 89.50),
        ("Webcam", "59.99"),
    ]
    for product in products:
        try:
            product_list.append(Product(*product))
        except ValueError as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

    print(product_list)


if __name__ == "__main__":
    main()
