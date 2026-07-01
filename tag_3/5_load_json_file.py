# tag_3/load_json_file.py
from pathlib import Path
import json
from pprint import pprint

DATA_DIR = Path(__file__).parent / "data"


with open(DATA_DIR / "tasks.json", encoding="utf-8") as f:
    data = json.load(f)
    print(type(data))
    tasks = data["admin"]["tasks"]


# Wir setzten für alle tasks in result, die den Status "open" haben, den Status auf
# "closed" und speichern die Liste als JSon-Array in eine Datei.
for task in tasks:
    # prüfen, ob task status open ist, und falls ja auf closed setzen
    if task["status"] == "open":
        task["status"] = "closed"


# tasks-Liste als new_tasks.json speichern. json.dump(tasks, f). modus="w"
with open(DATA_DIR / "new_tasks.json", mode="w", encoding="utf-8") as f:
    # um eine eingerückte Darstellung zu haben, kann man indent=2 nutzen
    # Damit Umlaute auch Dargestellt werden, muss eincoding auf utf-8 sein und
    # ensure_ascii auf False
    json.dump(tasks, f, ensure_ascii=False, indent=2)
