"""
JSON in Python nutzen

json.load() => eine Json-Datei einlesen
json.dump() => schreibt eine Json-Datei

json.loads() => liest json string
json.dumps() => schreibt Json String

Python                  JSON
-----------------------------------------
dict                =>  object
list, tuple         =>  array
str                 =>  string
int, float          =>  number
True                =>  true
False               =>  false
None                =>  null
"""

import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "hobbies": ("Coden", "Schach"),
    },
}

# Ein Python Dict / Liste in einen Json-String konvertieren
json_string = json.dumps(data)
print("JSON:", json_string)

# einen JSON-String konvertieren nach Python
python_dict = json.loads(json_string)
print("Python:", python_dict)
