# 🚀 Quick Start Guide

## Schnellstart in 3 Schritten

### Option 1: Streamlit App (Empfohlen)

#### Schritt 1: Installation
```bash
cd job_scraper
pip install -r requirements.txt
```

#### Schritt 2: App starten
```bash
# Linux/macOS
./run_streamlit.sh

# Windows
run_streamlit.bat

# Oder manuell
streamlit run streamlit_app.py
```

#### Schritt 3: Nutzen
- Browser öffnet sich automatisch bei `http://localhost:8501`
- Klicken Sie auf "🔄 Jetzt scrapen" in der Sidebar
- Warten Sie, bis das Scraping abgeschlossen ist
- Visualisierungen werden automatisch angezeigt

---

### Option 2: HTML/JS Webapp

#### Schritt 1: Installation
```bash
cd job_scraper
pip install -r requirements.txt
```

#### Schritt 2: Backend starten
```bash
python backend_api.py
```
Backend läuft auf `http://localhost:5000`

#### Schritt 3: Frontend öffnen

**WICHTIG:** `app.js` ist Browser-JavaScript, nicht Node.js! Führen Sie es NICHT mit `node app.js` aus!

**Option A: Mit lokalem Webserver (Empfohlen)**
```bash
# Neues Terminal-Fenster (im job_scraper Verzeichnis)
python -m http.server 8000
```
Dann öffnen Sie `http://localhost:8000/index.html` im Browser

**Option B: Direkt im Browser**
- Öffnen Sie `index.html` direkt im Browser (Doppelklick)
- Funktioniert, aber CORS-Probleme möglich

#### Schritt 4: Nutzen
- Klicken Sie auf "🔄 Jetzt scrapen"
- Warten Sie, bis das Scraping abgeschlossen ist
- Klicken Sie auf "📊 Daten laden"
- Visualisierungen werden angezeigt

---

## Erste Schritte

### Berufsfelder anpassen

**In der App:**
1. Geben Sie ein neues Berufsfeld ein
2. Klicken Sie auf "➕ Hinzufügen"
3. Zum Entfernen: Klicken Sie auf das "×" neben dem Berufsfeld

**Im Code (config.py):**
```python
JOB_CATEGORIES = [
    "Business Intelligence",
    "Full-Stack",
    "Ihr neues Berufsfeld"
]
```

### Daten exportieren

Beide Apps bieten einen Export-Button:
- Klicken Sie auf "📥 Daten exportieren"
- CSV-Datei wird heruntergeladen
- Öffnen Sie in Excel, Google Sheets, etc.

### Automatisches tägliches Scraping

```bash
python scheduler.py
```

Das Programm:
- Führt sofort ein Scraping durch
- Scraped dann täglich um 09:00 Uhr
- Läuft kontinuierlich (Strg+C zum Beenden)

---

## Beispiel-Workflow

### Szenario: Wöchentliche Job-Markt-Analyse

1. **Montag morgen:**
   ```bash
   streamlit run streamlit_app.py
   ```
   - Scraping durchführen
   - Aktuelle Zahlen ansehen

2. **Automatisch täglich:**
   ```bash
   python scheduler.py
   ```
   - Läuft im Hintergrund
   - Sammelt täglich Daten

3. **Freitag:**
   - Streamlit-App öffnen
   - Zeitverlauf-Diagramme ansehen
   - Trends der Woche analysieren
   - Daten als CSV exportieren

---

## Häufige Probleme

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Connection refused" (HTML-Version)
- Stellen Sie sicher, dass Backend läuft: `python backend_api.py`
- Überprüfen Sie, ob Port 5000 frei ist

### Keine Daten sichtbar
- Führen Sie zuerst ein Scraping durch
- Warten Sie, bis "Scraping abgeschlossen" angezeigt wird
- Laden Sie die Seite neu

### API-Fehler
- Überprüfen Sie Ihre Internetverbindung
- Die Arbeitsagentur-API könnte temporär nicht verfügbar sein
- Versuchen Sie es in einigen Minuten erneut

---

## Nächste Schritte

1. **Erkunden Sie die Visualisierungen:**
   - Bar Charts für jede Angebotsart
   - Zeitverlauf-Diagramme
   - Interaktive Plotly-Charts (Streamlit)

2. **Passen Sie die Berufsfelder an:**
   - Fügen Sie relevante Berufsfelder hinzu
   - Entfernen Sie nicht benötigte

3. **Automatisieren Sie:**
   - Richten Sie den Scheduler ein
   - Oder nutzen Sie Cron/Task Scheduler

4. **Analysieren Sie Trends:**
   - Sammeln Sie Daten über mehrere Tage
   - Vergleichen Sie verschiedene Berufsfelder
   - Identifizieren Sie Wachstumsbereiche

---

## Support

Weitere Informationen finden Sie in:
- `README.md` - Vollständige Dokumentation
- `config.py` - Konfigurationsoptionen
- Kommentare im Code

Bei Problemen:
1. Überprüfen Sie die Fehlermeldung
2. Lesen Sie die Troubleshooting-Sektion in README.md
3. Überprüfen Sie, ob alle Abhängigkeiten installiert sind