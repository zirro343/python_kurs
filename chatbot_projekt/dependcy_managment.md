# Dependency Management in Python

## Warum?

Python-Projekte benötigen häufig externe Pakete (Dependencies),
z. B. `requests`, `numpy` oder `pyyaml`.

Damit verschiedene Projekte sich nicht gegenseitig beeinflussen,
arbeitet man mit **virtuellen Umgebungen (venv)**.

---

# Virtuelle Umgebung erstellen

Im Projektverzeichnis:

```bash
python -m venv .venv
```

Es wird ein Ordner `.venv` erstellt.

---

# Virtuelle Umgebung aktivieren

## Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

## Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

## Linux / macOS

```bash
source .venv/bin/activate
```

Nach der Aktivierung erscheint meist der Name der Umgebung:

```text
(.venv) PS C:\Projekt>
```

---

# Paket installieren

```bash
pip install requests
```

Mehrere Pakete:

```bash
pip install requests pyyaml
```

---

# Installierte Pakete anzeigen

```bash
pip list
```

Oder detaillierter:

```bash
pip freeze
```

---

# requirements.txt erstellen

Alle installierten Pakete speichern:

```bash
pip freeze > requirements.txt
```

Beispiel:

```text
certifi==2025.6.15
charset-normalizer==3.4.2
idna==3.10
PyYAML==6.0.2
requests==2.32.4
urllib3==2.5.0
```

---

# Abhängigkeiten installieren

Ein anderes Projekt kann alle Pakete mit einem Befehl installieren:

```bash
pip install -r requirements.txt
```

---

# Virtuelle Umgebung verlassen

```bash
deactivate
```

---

# Typischer Ablauf

```bash
python -m venv .venv

# Umgebung aktivieren

pip install requests
pip install pyyaml

pip freeze > requirements.txt
```

Ein anderer Entwickler:

```bash
python -m venv .venv

# Umgebung aktivieren

pip install -r requirements.txt
```

---

# Best Practice

- Für jedes Projekt eine eigene virtuelle Umgebung
- `.venv` nicht in Git einchecken
- `requirements.txt` mit ins Repository aufnehmen
- Immer in der virtuellen Umgebung arbeiten