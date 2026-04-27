# Neue Features - Deutschland Heatmap & Unternehmen-Analyse

## 🗺️ Deutschland Heatmap

### Beschreibung
Visualisiert Stellenangebote geografisch auf einer interaktiven Karte von Deutschland.

### Features
- **Interaktive Karte** mit Folium
- **Standort-Marker** für jedes Stellenangebot
- **Filter** nach Angebotsart und Berufsfeld
- **Popup-Informationen** mit Unternehmen, Stadt und Kategorie
- **Statistiken**: Anzahl Standorte, Städte und Unternehmen

### Verwendung

1. **Detailliertes Scraping durchführen:**
   ```python
   # In der Streamlit-App
   # Gehe zu Tab "🗺️ Deutschland Heatmap"
   # Klicke auf "🔍 Detailliertes Scraping starten"
   ```

2. **Karte erkunden:**
   - Zoomen und Verschieben
   - Auf Marker klicken für Details
   - Filter anwenden

3. **Daten:**
   - Gespeichert in `locations_data.json`
   - Enthält: Stadt, PLZ, Region, Koordinaten, Unternehmen

### Technische Details

**Datenstruktur:**
```json
{
  "city": "Berlin",
  "plz": "10115",
  "region": "Berlin",
  "lat": 52.5200,
  "lon": 13.4050,
  "category": "Data Scientist",
  "job_type": "Arbeit",
  "company": "Example GmbH"
}
```

**API-Methoden:**
- `scraper.scrape_all_detailed()` - Scraped detaillierte Job-Infos
- `scraper.load_locations_data()` - Lädt Standortdaten
- `scraper.save_detailed_data()` - Speichert detaillierte Daten

## 🏢 Unternehmen-Analyse

### Beschreibung
Analysiert und visualisiert die Top-Unternehmen pro Angebotsart mit CRUD-Funktionalität.

### Features
- **Top-Unternehmen** sortiert nach Anzahl Stellenangebote
- **Sortierung** aufsteigend/absteigend
- **Sichtbarkeits-Toggle** für jedes Unternehmen
- **Interaktive Bar Charts** mit Plotly
- **CSV-Export** der Unternehmensdaten
- **Persistente Speicherung** der Sichtbarkeitseinstellungen

### Verwendung

1. **Detailliertes Scraping durchführen:**
   ```python
   # In der Streamlit-App
   # Gehe zu Tab "🏢 Unternehmen-Analyse"
   # Klicke auf "🔍 Detailliertes Scraping starten"
   ```

2. **Analyse durchführen:**
   - Wähle Angebotsart (Arbeit, Ausbildung, Selbstständigkeit)
   - Passe Anzahl der angezeigten Unternehmen an (5-50)
   - Wähle Sortierung (Auf-/Absteigend)

3. **Unternehmen verwalten:**
   - Checkbox "Anzeigen" zum Ein-/Ausblenden
   - Einstellungen werden in JSON gespeichert
   - Nur sichtbare Unternehmen erscheinen im Chart

4. **Daten exportieren:**
   - Klicke auf "📥 Unternehmensdaten exportieren"
   - CSV-Datei wird heruntergeladen

### Technische Details

**Datenstruktur:**
```json
{
  "Arbeit": [
    {
      "name": "Deutsche Bahn AG",
      "count": 45,
      "visible": true
    },
    {
      "name": "SAP SE",
      "count": 38,
      "visible": false
    }
  ]
}
```

**API-Methoden:**
- `scraper.load_companies_data()` - Lädt Unternehmensdaten
- `scraper.update_company_visibility()` - Aktualisiert Sichtbarkeit
- `scraper.save_detailed_data()` - Speichert detaillierte Daten

**CRUD-Operationen:**
- **Create**: Automatisch beim Scraping
- **Read**: `load_companies_data()`
- **Update**: `update_company_visibility()`
- **Delete**: Manuell in JSON-Datei

## 📁 Neue Dateien

### Datenspeicherung

1. **job_details.json**
   - Alle detaillierten Job-Informationen
   - Enthält: Titel, Unternehmen, Standort, Koordinaten

2. **companies_data.json**
   - Aggregierte Unternehmensdaten pro Angebotsart
   - Sortiert nach Anzahl Stellenangebote
   - Sichtbarkeitseinstellungen

3. **locations_data.json**
   - Standortdaten mit Koordinaten
   - Für Heatmap-Visualisierung

## 🔧 Installation

### Zusätzliche Abhängigkeiten

```bash
pip install folium streamlit-folium
```

Oder:
```bash
cd backend
pip install -r requirements.txt
```

Die `requirements.txt` wurde aktualisiert mit:
- `folium==0.15.1`
- `streamlit-folium==0.16.0`

## 🚀 Schnellstart

### 1. Detailliertes Scraping

```bash
cd backend
python -c "from scraper import JobScraper; s = JobScraper(); jobs = s.scrape_all_detailed(); s.save_detailed_data(jobs)"
```

### 2. Streamlit-App starten

```bash
streamlit run streamlit_app.py
```

### 3. Features nutzen

- **Tab 4**: 🗺️ Deutschland Heatmap
- **Tab 5**: 🏢 Unternehmen-Analyse

## 📊 Beispiel-Workflow

### Szenario: Marktanalyse für Data Scientists

1. **Scraping durchführen:**
   - Detailliertes Scraping für alle Berufsfelder
   - Wartezeit: ~5-10 Minuten

2. **Heatmap analysieren:**
   - Wo sind die meisten Data Scientist Jobs?
   - Welche Regionen sind Hotspots?
   - Filter: Nur "Data Scientist" + "Arbeit"

3. **Unternehmen identifizieren:**
   - Top 20 Unternehmen für Data Scientists
   - Welche Unternehmen stellen am meisten ein?
   - Unerwünschte Unternehmen ausblenden

4. **Daten exportieren:**
   - CSV für weitere Analyse
   - Teilen mit Team

## ⚙️ Konfiguration

### Scraping-Parameter anpassen

In `scraper.py`:

```python
# Anzahl Jobs pro Kategorie
max_per_category = 50  # Standard: 50, Max: 100

# Beispiel
jobs = scraper.scrape_all_detailed(
    job_categories=['Data Scientist'],
    max_per_category=100
)
```

### Karten-Einstellungen

In `streamlit_app.py`:

```python
# Karten-Zentrum (Deutschland)
location=[51.1657, 10.4515]

# Zoom-Level
zoom_start=6  # 1-18 (höher = näher)

# Marker-Farbe
color='red'  # 'blue', 'green', 'purple', etc.
```

## 🔍 Datenqualität

### Standortdaten

- **Verfügbarkeit**: ~80-90% der Jobs haben Koordinaten
- **Genauigkeit**: Stadt-Level (nicht Straßen-genau)
- **Quelle**: Arbeitsagentur API

### Unternehmensdaten

- **Vollständigkeit**: ~95% der Jobs haben Unternehmensnamen
- **Normalisierung**: Keine (z.B. "SAP" vs "SAP SE")
- **Duplikate**: Möglich bei verschiedenen Schreibweisen

## 🐛 Bekannte Einschränkungen

1. **API-Limits**: Max 100 Jobs pro Request
2. **Koordinaten**: Nicht alle Jobs haben Geo-Daten
3. **Unternehmensnamen**: Keine Normalisierung
4. **Performance**: Detailliertes Scraping dauert länger
5. **Speicher**: Große Datenmengen bei vielen Kategorien

## 💡 Tipps

### Performance optimieren

```python
# Weniger Kategorien
job_categories = ['Data Scientist', 'Data Analyst']

# Weniger Jobs pro Kategorie
max_per_category = 25
```

### Daten bereinigen

```python
# Duplikate entfernen
import json
with open('companies_data.json', 'r') as f:
    data = json.load(f)

# Unternehmensnamen normalisieren
# z.B. "SAP SE" und "SAP" zusammenführen
```

### Backup erstellen

```bash
# Vor jedem Scraping
cp job_details.json job_details_backup.json
cp companies_data.json companies_data_backup.json
cp locations_data.json locations_data_backup.json
```

## 📚 Weiterführende Informationen

- [Folium Documentation](https://python-visualization.github.io/folium/)
- [Streamlit-Folium](https://github.com/randyzwitch/streamlit-folium)
- [Arbeitsagentur API](https://jobsuche.api.bund.de/)

## 🆘 Troubleshooting

### Problem: Keine Standortdaten

**Lösung:**
```python
# Detailliertes Scraping durchführen
python -c "from scraper import JobScraper; s = JobScraper(); jobs = s.scrape_all_detailed(); s.save_detailed_data(jobs)"
```

### Problem: Karte wird nicht angezeigt

**Lösung:**
```bash
pip install --upgrade folium streamlit-folium
```

### Problem: Unternehmen-Sichtbarkeit wird nicht gespeichert

**Lösung:**
- Überprüfen Sie Schreibrechte für `companies_data.json`
- Stellen Sie sicher, dass die Datei existiert

### Problem: Zu viele Marker auf der Karte

**Lösung:**
- Verwenden Sie Filter
- Reduzieren Sie `max_per_category`
- Clustern Sie Marker (zukünftiges Feature)

---

**Version:** 2.0.0  
**Datum:** 2026-04-25  
**Autor:** Job Scraper Team