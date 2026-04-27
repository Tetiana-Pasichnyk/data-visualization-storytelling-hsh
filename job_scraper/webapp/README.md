# Arbeitsagentur Job Scraper - Webapp Version

Eine moderne, browserbasierte Anwendung zur Überwachung von IT-Stellenangeboten der Bundesagentur für Arbeit mit erweiterten Analyse-Features.

## 🌟 Features

### Basis-Funktionen
- ✅ **Modulare Berufsfelder**: Anpassbare Liste von IT-Berufsfeldern
- ✅ **Mehrere Angebotsarten**: Arbeit, Ausbildung, Selbstständigkeit
- ✅ **Interaktive Charts**: Bar Charts und Zeitverlaufs-Diagramme
- ✅ **Daten-Export**: CSV-Export für weitere Analysen
- ✅ **Persistente Speicherung**: Automatische Datenspeicherung

### Erweiterte Features (NEU!)
- 🗺️ **Deutschland Heatmap**: Geografische Visualisierung aller Stellenangebote
- 🏢 **Unternehmen-Analyse**: Top-Arbeitgeber mit CRUD-Funktionalität
- 📊 **Detailliertes Scraping**: Sammelt Standort- und Unternehmensdaten
- 🔍 **Erweiterte Filter**: Nach Angebotsart, Berufsfeld und Standort

## 📋 Voraussetzungen

- Python 3.8+
- Moderner Webbrowser (Chrome, Firefox, Safari, Edge)
- Internetverbindung

## 🚀 Installation

### 1. Abhängigkeiten installieren

```bash
cd webapp
pip install -r requirements.txt
```

**requirements.txt** enthält:
```
flask==3.0.0
flask-cors==4.0.0
requests==2.31.0
pandas==2.1.4
```

### 2. Backend starten

```bash
python backend.py
```

Der Server startet auf `http://localhost:5000`

### 3. Webapp öffnen

Öffnen Sie Ihren Browser und navigieren Sie zu:
```
http://localhost:5000
```

## 📖 Verwendung

### Tab 1: ⚙️ Einstellungen

#### Berufsfelder verwalten
1. **Hinzufügen**: Geben Sie ein neues Berufsfeld ein und klicken Sie auf "➕ Hinzufügen"
2. **Entfernen**: Klicken Sie auf das "×" neben einem Berufsfeld

#### Scraping durchführen
- **🔄 Jetzt scrapen**: Schnelles Scraping (nur Anzahl der Stellen)
- **🔍 Detailliertes Scraping**: Sammelt zusätzlich Standorte und Unternehmen (5-10 Min.)

#### Weitere Aktionen
- **📊 Daten laden**: Lädt gespeicherte Daten und zeigt Charts an
- **📥 Daten exportieren**: Exportiert Daten als CSV
- **🗑️ Daten löschen**: Löscht alle lokalen Daten

### Tab 2: 📊 Diagramme

Zeigt interaktive Bar Charts für jede Angebotsart:
- **Arbeit**: Reguläre Stellenangebote
- **Ausbildung**: Ausbildungsplätze
- **Selbstständigkeit**: Freiberufler/Selbstständige

Plus **Zeitverlauf-Diagramm** zur Verfolgung von Trends.

### Tab 3: 🗺️ Heatmap (NEU!)

Visualisiert Stellenangebote geografisch auf einer interaktiven Karte.

#### Features
- **Interaktive Karte**: Zoomen, Verschieben, Marker anklicken
- **Filter**: Nach Angebotsart und Berufsfeld filtern
- **Popup-Informationen**: Unternehmen, Stadt, Kategorie
- **Statistiken**: Anzahl Standorte, Städte, Unternehmen

#### Verwendung
1. Führen Sie **Detailliertes Scraping** durch (Tab 1)
2. Wechseln Sie zum Heatmap-Tab
3. Verwenden Sie die Filter-Dropdowns
4. Klicken Sie auf Marker für Details

### Tab 4: 🏢 Unternehmen (NEU!)

Analysiert und visualisiert Top-Arbeitgeber.

#### Features
- **Top-Unternehmen**: Sortiert nach Anzahl Stellenangebote
- **Sichtbarkeits-Toggle**: Ein-/Ausblenden einzelner Unternehmen
- **Interaktives Chart**: Horizontales Bar Chart
- **CSV-Export**: Exportiert Unternehmensdaten

#### Verwendung
1. Führen Sie **Detailliertes Scraping** durch (Tab 1)
2. Wechseln Sie zum Unternehmen-Tab
3. Wählen Sie Angebotsart (Arbeit/Ausbildung/Selbstständigkeit)
4. Passen Sie Anzahl der angezeigten Unternehmen an (5-50)
5. Nutzen Sie Checkboxen zum Ein-/Ausblenden
6. Exportieren Sie Daten als CSV

## 🔧 Konfiguration

### Standard-Berufsfelder

Die Standard-Berufsfelder sind in `backend.py` definiert:

```python
DEFAULT_CATEGORIES = [
    "Business Intelligence",
    "Full-Stack",
    "Data Scientist",
    "Data Analyst",
    "System Administrator",
    "DevOps Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Machine Learning Engineer",
    "Cloud Architect"
]
```

### API-Endpunkte

Der Backend-Server bietet folgende Endpunkte:

#### Basis-Endpunkte
- `POST /api/scrape` - Schnelles Scraping
- `GET /api/data` - Alle historischen Daten
- `GET /api/categories` - Aktuelle Berufsfelder
- `GET /api/stats` - Zusammenfassende Statistiken
- `GET /api/health` - Health Check

#### Erweiterte Endpunkte (NEU!)
- `POST /api/scrape-detailed` - Detailliertes Scraping
- `GET /api/locations` - Standortdaten für Heatmap
- `GET /api/companies` - Unternehmensdaten
- `POST /api/companies/visibility` - Sichtbarkeit aktualisieren

## 📁 Datenspeicherung

Die Webapp speichert Daten in folgenden Dateien:

### Basis-Daten
- `job_data.json` - Alle Scraping-Ergebnisse
- `job_history.csv` - Historische Daten (CSV-Format)

### Erweiterte Daten (NEU!)
- `job_details.json` - Detaillierte Job-Informationen
- `locations_data.json` - Standortdaten mit Koordinaten
- `companies_data.json` - Unternehmensdaten mit Sichtbarkeit

## 🎨 Technologie-Stack

### Frontend
- **HTML5/CSS3**: Modernes, responsives Design
- **JavaScript (ES6+)**: Interaktive Funktionalität
- **Chart.js**: Datenvisualisierung
- **Leaflet.js**: Interaktive Karten

### Backend
- **Flask**: Python Web Framework
- **Flask-CORS**: Cross-Origin Resource Sharing
- **Requests**: HTTP-Bibliothek für API-Calls
- **Pandas**: Datenverarbeitung und -analyse

### API
- **Arbeitsagentur REST API**: Offizielle API der Bundesagentur für Arbeit

## 🔍 Beispiel-Workflow

### Szenario: Marktanalyse für Data Scientists

1. **Berufsfeld hinzufügen** (falls nicht vorhanden)
   - Gehe zu Tab "⚙️ Einstellungen"
   - Füge "Data Scientist" hinzu

2. **Detailliertes Scraping durchführen**
   - Klicke auf "🔍 Detailliertes Scraping"
   - Warte 5-10 Minuten

3. **Heatmap analysieren**
   - Wechsle zu Tab "🗺️ Heatmap"
   - Filtere nach "Data Scientist"
   - Identifiziere Hotspots (Berlin, München, Hamburg?)

4. **Top-Arbeitgeber identifizieren**
   - Wechsle zu Tab "🏢 Unternehmen"
   - Wähle "Arbeit"
   - Zeige Top 20 Unternehmen
   - Exportiere als CSV

5. **Trends verfolgen**
   - Wechsle zu Tab "📊 Diagramme"
   - Wähle "Data Scientist" im Zeitverlauf
   - Analysiere Entwicklung über Zeit

## 🐛 Troubleshooting

### Problem: Backend startet nicht

**Lösung:**
```bash
# Überprüfen Sie Python-Version
python --version  # Sollte 3.8+ sein

# Installieren Sie Abhängigkeiten neu
pip install --upgrade -r requirements.txt
```

### Problem: CORS-Fehler im Browser

**Lösung:**
- Stellen Sie sicher, dass der Backend-Server läuft
- Öffnen Sie die Webapp über `http://localhost:5000` (nicht als Datei)

### Problem: Keine Standortdaten auf Heatmap

**Lösung:**
1. Führen Sie **Detailliertes Scraping** durch
2. Warten Sie, bis Scraping abgeschlossen ist
3. Klicken Sie auf "🔄 Daten aktualisieren" im Heatmap-Tab

### Problem: Unternehmen-Tab zeigt keine Daten

**Lösung:**
1. Führen Sie **Detailliertes Scraping** durch
2. Wechseln Sie zum Unternehmen-Tab
3. Klicken Sie auf "🔄 Daten aktualisieren"

### Problem: Karte wird nicht angezeigt

**Lösung:**
- Überprüfen Sie Internetverbindung (Leaflet lädt Karten-Tiles online)
- Aktualisieren Sie die Seite (F5)
- Öffnen Sie Browser-Konsole für Fehlermeldungen

## 📊 Performance-Tipps

### Scraping optimieren
```python
# In backend.py anpassen:
max_per_category = 25  # Statt 50 für schnelleres Scraping
```

### Weniger Berufsfelder
- Entfernen Sie nicht benötigte Berufsfelder
- Reduziert Scraping-Zeit erheblich

### Daten bereinigen
```bash
# Alte Daten löschen
rm job_data.json job_history.csv
rm job_details.json locations_data.json companies_data.json
```

## 🔐 Sicherheit

### API-Key
- Der API-Key `jobboerse-jobsuche` ist öffentlich
- Keine Authentifizierung erforderlich
- Rate-Limiting durch Arbeitsagentur API

### Lokale Daten
- Alle Daten werden lokal gespeichert
- Keine Cloud-Speicherung
- Keine persönlichen Daten gesammelt

## 🆕 Changelog

### Version 2.0.0 (2026-04-25)
- ✨ **NEU**: Deutschland Heatmap mit Leaflet.js
- ✨ **NEU**: Unternehmen-Analyse mit CRUD
- ✨ **NEU**: Detailliertes Scraping für Standorte und Unternehmen
- ✨ **NEU**: Tab-basierte Navigation
- 🔧 Erweiterte API-Endpunkte
- 📊 Verbesserte Datenvisualisierung

### Version 1.0.0 (Initial)
- ✅ Basis-Scraping-Funktionalität
- ✅ Bar Charts und Zeitverlauf
- ✅ Modulare Berufsfelder
- ✅ CSV-Export

## 📚 Weiterführende Links

- [Arbeitsagentur API Dokumentation](https://jobsuche.api.bund.de/)
- [Chart.js Dokumentation](https://www.chartjs.org/)
- [Leaflet.js Dokumentation](https://leafletjs.com/)
- [Flask Dokumentation](https://flask.palletsprojects.com/)

## 🤝 Support

Bei Fragen oder Problemen:
1. Überprüfen Sie die Troubleshooting-Sektion
2. Öffnen Sie die Browser-Konsole (F12) für Fehlermeldungen
3. Überprüfen Sie die Backend-Logs im Terminal

## 📝 Lizenz

Dieses Projekt nutzt die öffentliche API der Bundesagentur für Arbeit.

---

**Version:** 2.0.0  
**Datum:** 2026-04-25  
**Made with Bob** 🤖