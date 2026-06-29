""" 
If elif else

Was ist unwahr?
Python als falsch interpretiert:
0 => Ganzahl 0
0.0 => Float 0.0
"" => leerer String
[] => leere Liste
() => leerer Tupel
{} => leeres Dictionary
None
Folgende Werte, die an die Funktion bool() übergeben werden, werden von 
False => der boolsche Wert False

"""
x = bool(0)
print(x)

values = [1, 2, 3]
# klasssische SChreibweise, um zu prüfen, ob Elemente in x vorhanden sind
if len(values) > 0:
    print("values enthält Elemente")

# Wenn die Liste min. ein Element enthält, ist es truthy
if values:
    print("values enthält Elemente")


# Else und elif. Man kann in Python keine Blöcke leer lassen.
# Dazu nutzt man das pass-Keyword.
apples = 3
if apples > 2 and apples < 5:
    pass
elif apples > 3:
    print("test")
else:
    print("else")


# In-Operator (Membership)
values = [1, 2, 3, 4]
if 3 in values:
    print("die 3 ist in values enthalten")

# Is-Operator (vor allem Zum Prüfen, ob ein Wert None ist)
x = None 
if x is None:
    print("x ist None")


def check(value):
    if value < 3:
        return 42
    
    return None

if check(44) is None:
    print("check is None")