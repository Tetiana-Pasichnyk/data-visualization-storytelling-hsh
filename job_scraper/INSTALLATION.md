# Installation Guide

Detaillierte Installationsanleitung für beide Versionen des Job Scrapers.

## 📋 Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)
- Internetverbindung

## 🔧 Installation

### Option 1: Mit venv (Empfohlen)

#### Schritt 1: Repository klonen/herunterladen

```bash
cd job_scraper
```

### Option 2: Mit uv (Schneller)

[uv](https://github.com/astral-sh/uv) ist ein ultra-schneller Python Package Manager.

#### Schritt 1: uv installieren

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Schritt 2: Virtuelle Umgebung erstellen und aktivieren

```bash
cd job_scraper

# Venv erstellen
uv venv

# Aktivieren
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

#### Schritt 3: Abhängigkeiten installieren

**Für Streamlit:**
```bash
cd backend
uv pip install -r requirements.txt
```

**Für Webapp:**
```bash
cd webapp
uv pip install -r requirements.txt
```

#### Schritt 4: Anwendung starten

**Streamlit:**
```bash
cd backend
streamlit run streamlit_app.py
```

**Webapp:**
```bash
cd webapp
python backend.py
```

### pip-Version prüfen

```bash
pip --version
```

### Installierte Pakete anzeigen

```bash
pip list
```

Sie sollten Pakete wie `streamlit`, `flask`, `pandas`, etc. sehen.

## 🐛 Troubleshooting

### Problem: "python: command not found"

**Lösung:**
- Installieren Sie Python von [python.org](https://www.python.org/downloads/)
- Oder verwenden Sie `python3` statt `python`

### Problem: "pip: command not found"

**Lösung:**
```bash
# macOS/Linux
python3 -m ensurepip --upgrade

# Windows
python -m ensurepip --upgrade
```

### Problem: "Permission denied"

**Lösung:**
```bash
# Verwenden Sie --user flag
pip install --user -r requirements.txt

# Oder verwenden Sie sudo (Linux/macOS)
sudo pip install -r requirements.txt
```

### Problem: "Module not found" nach Installation

**Lösung:**
1. Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist
2. Installieren Sie die Pakete erneut:
   ```bash
   pip install -r requirements.txt
   ```

### Problem: uv Installation schlägt fehl

**Lösung:**
Verwenden Sie die traditionelle venv-Methode (Option 1).

### Problem: Streamlit startet nicht

**Lösung:**
```bash
# Deinstallieren und neu installieren
pip uninstall streamlit
pip install streamlit

# Oder spezifische Version
pip install streamlit==1.31.0
```

### Problem: Flask-CORS Fehler

**Lösung:**
```bash
pip install flask-cors
```

## 📦 Abhängigkeiten

### Streamlit (backend/)

- streamlit==1.31.0
- requests==2.31.0
- beautifulsoup4==4.12.3
- pandas==2.2.0
- matplotlib==3.8.2
- plotly==5.18.0
- schedule==1.2.0
- lxml==5.1.0

### Webapp (webapp/)

- flask==3.0.0
- flask-cors==4.0.0
- requests==2.31.0
- pandas==2.2.0

## 🔄 Virtuelle Umgebung deaktivieren

Wenn Sie fertig sind:

```bash
deactivate
```

## 🗑️ Deinstallation

### Virtuelle Umgebung löschen

```bash
# Im Projektverzeichnis
rm -rf venv      # oder .venv bei uv
rm -rf __pycache__
```

### Systemweite Pakete deinstallieren

```bash
pip uninstall streamlit flask flask-cors requests pandas matplotlib plotly schedule beautifulsoup4 lxml
```

## 💡 Tipps

### Schnellere Installation mit uv

uv ist bis zu 10-100x schneller als pip:

```bash
# Vergleich
time pip install -r requirements.txt    # ~30-60 Sekunden
time uv pip install -r requirements.txt # ~3-5 Sekunden
```

### Virtuelle Umgebung automatisch aktivieren

**Für bash/zsh (macOS/Linux):**

Fügen Sie zu `~/.bashrc` oder `~/.zshrc` hinzu:
```bash
# Auto-activate venv when entering project directory
cd() {
    builtin cd "$@"
    if [[ -d ./venv ]] ; then
        source ./venv/bin/activate
    fi
}
```

### Requirements einfrieren

Um die exakten Versionen zu speichern:

```bash
pip freeze > requirements-lock.txt
```

### Upgrade aller Pakete

```bash
pip install --upgrade -r requirements.txt
```

## 🆘 Weitere Hilfe

Bei weiteren Problemen:

1. Überprüfen Sie die Python-Version: `python --version`
2. Überprüfen Sie die pip-Version: `pip --version`
3. Lesen Sie die Fehlermeldung sorgfältig
4. Suchen Sie nach der Fehlermeldung online
5. Stellen Sie sicher, dass Sie im richtigen Verzeichnis sind

## 📚 Weiterführende Links

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [uv Documentation](https://github.com/astral-sh/uv)
- [pip Documentation](https://pip.pypa.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)