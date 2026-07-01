"""
Aufgabe: Bereinige eine Logdatei.

Öffne die Datei "log.txt" und lies alle Zeilen ein.
Entferne in jeder Zeile führende und nachfolgende x.

Schreibe nur Zeilen in die Datei "clean_log.txt",
die nicht leer sind.

Schließe alle Dateien korrekt.

mode="w" ist der Schreibmodus.
open(path, mode="w", encoding="utf-8)
"""

from pathlib import Path

# Log Datei iterativ einlesen
cleaned_logs = []

LOG_FILE = Path(__file__).parent / "data" / "log.txt"
CLEAN_FILE = Path(__file__).parent / "data" / "clean_log.txt"

with open(LOG_FILE, mode="r") as f:
    for line in f:
        line = line.replace("x", "").strip()
        if line:
            cleaned_logs.append(line + "\n")

# Neue Log datei schreiben
with open(CLEAN_FILE, mode="w") as f:
    f.writelines(cleaned_logs)
