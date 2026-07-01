"""
Yaml Dateien einlesen und schreiben

ymal installieren:
pip install pyyaml
"""

from pathlib import Path
import yaml
from pprint import pprint

CONFIG_PATH = Path(__file__).parent / "data/config.yaml"

with open(CONFIG_PATH) as f:
    config = yaml.safe_load(f)
    pprint(config, width=20)

# Aufgabe: database host in config auf "postgres" und port auf 6531 setzen
# Danach soll das yaml wieder unter dem selben Namen gespeichert werden
# also config.yaml.
# mit yaml.safe_dump() die Datei speichern
config["database"]["host"] = "Postgres"
config["database"]["port"] = 6531

# Yaml Datei neu schreiben
with open(CONFIG_PATH, mode="w") as f:
    yaml.safe_dump(config, f)
