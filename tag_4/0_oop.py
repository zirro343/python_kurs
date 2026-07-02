"""
Objektorientierung in Python

https://python-umsteiger.friendlybytes.net/chapter_05/
"""


class House:
    pass


a = House()
print("Typ von a:", type(a))  # <class '__main__.House'>
print("Prüfen, ob Haus:", isinstance(a, House))


x = 42
print(dir(x))

print("*" * 30)
print(dir(a))
