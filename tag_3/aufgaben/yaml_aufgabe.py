"""
Aufgabe: Benutzer aus einer YAML-Datei auslesen

Gegeben ist die Datei "users.yaml":

users:
  - name: Max
    role: admin
    active: true

  - name: Lisa
    role: user
    active: false

  - name: Tom
    role: admin
    active: true

Lies die YAML-Datei mit yaml.safe_load() ein.

Speichere die Benutzerliste in einer Variablen.

Gib anschließend alle Benutzer aus, deren Rolle "admin"
ist und die aktiv sind.
"""
