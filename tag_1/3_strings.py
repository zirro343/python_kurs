""" 
Zeichenketten in Python
"""
username = "Bobby"  # einfaches String-Literatel
home_town = 'Nürnberg' # einfaches String-Literatel
raw_string = r"D:\bla\blu\n" # mit Raw-String das Escapen sparen

# mehrzeiliger String
poem = """
Das ist 
ein 
Gedicht
"""
print("Poem:", poem)

# per Index zugreifen
print("Hometown an Index 0:", home_town[0])  # N
print("Hometown an Index 0:", home_town[-1]) # g

# home_town[0] = "M" DAS GEHT NICHT!
print("Länge von home_town:", len(home_town))

# String-Methoden erzeugen immer einen neuen String
username = username.replace("b", "x")
print("Username wurde b durch x  ersetzt", username)

# Gibt True oder False zurück, wenn ein String mit einer Zeichenkette startet
if home_town.startswith("Nü"):
    print("Fängt mit Nü an")

# Strings konkatenieren
first_name = "Alice"
last_name = "Schneider"

# Konkat mit + - OPerator
full_name = first_name + "," + last_name
# Zum Konkatieren von vielen Strings besser join nehmen
full_name = ",".join([first_name, last_name])


# Strings multiplizieren
print("*" * 40)